"""Roll up raw atoms into theme clusters for the graph explorer.

Two modes, same clusters.json output (the UI doesn't care which produced it):

  1. k-means on real embeddings (preferred):
       uv run --with numpy graph/build_clusters.py \
           --embeddings ../earnings-wiki/.graph-lab/embeddings.json
     Spherical k-means (unit-normalized vectors, cosine geometry). k is picked by
     silhouette score on a 2k-atom sample across a few candidate k's — cheap enough
     to run in ~a minute, real enough to not eyeball k. Representative = atom
     nearest the true centroid. Inter-theme edges = centroid cosine similarity,
     pruned to each theme's TOP_EDGES strongest.

  2. label propagation on the public kNN similarity edges (fallback, stdlib only):
       python3 graph/build_clusters.py

clusters.json schema (per cluster): id, label, repId, memberIds, terms,
dominant sector/section/quarter/index, first_date; plus clusterEdges
[{sourceId, targetId, weight}] and top-level {method, k}.

Deterministic in both modes (fixed seeds).
"""
import argparse
import collections
import json
import math
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_MEMBERS = 4      # label-prop only: communities smaller than this stay unclustered
MAX_ITERS = 30
SEED = 42
TOP_EDGES = 4        # keep each cluster's N strongest inter-cluster links
N_TERMS = 5          # distinctive terms per cluster (TF-IDF over member text)
K_CANDIDATES = (150, 250, 350)
SIL_SAMPLE = 2000    # atoms sampled for silhouette scoring

STOP = set("""a an and are as at be but by for from has have in into is it its more not of on or
over than that the their they this to was were will with we our you your""".split())

nodes = json.load(open(os.path.join(HERE, "nodes.json")))["nodes"]
edges = json.load(open(os.path.join(HERE, "edges.json")))["edges"]
by_id = {n["id"]: n for n in nodes}

adj = collections.defaultdict(list)
for e in edges:
    adj[e["sourceId"]].append((e["targetId"], e["weight"]))
    adj[e["targetId"]].append((e["sourceId"], e["weight"]))


# ---------------------------------------------------------------- shared helpers

def toks(s):
    return [t for t in re.findall(r"[a-z][a-z0-9-]{2,}", s.lower()) if t not in STOP]

doc_freq = collections.Counter()
node_toks = {}
for n in nodes:
    node_toks[n["id"]] = collections.Counter(toks(n["name"] + " " + n["description"]))
    doc_freq.update(node_toks[n["id"]].keys())

def top_terms(members):
    tf = collections.Counter()
    for m in members:
        tf.update(node_toks[m])
    scored = sorted(tf, key=lambda t: -tf[t] * math.log(len(nodes) / (1 + doc_freq[t])))
    return scored[:N_TERMS]

def dominant(members, key):
    return collections.Counter(by_id[m][key] for m in members).most_common(1)[0][0]

def make_cluster(cid, members, rep, label_atom=None):
    return {
        "id": cid,
        "label": by_id[label_atom or rep]["name"],
        "repId": rep,
        "memberIds": sorted(members),
        "sector": dominant(members, "sector"),
        "section": dominant(members, "section"),
        "quarter": dominant(members, "quarter"),
        "index": dominant(members, "index"),
        "first_date": min(by_id[m]["call_date"] for m in members),
        "terms": top_terms(members),
    }

def prune_edges(agg):
    """Keep each cluster's TOP_EDGES strongest links; the full inter-cluster graph
    is dense enough to collapse the force layout into a ball."""
    ranked = collections.defaultdict(list)
    for pair in agg:
        ranked[pair[0]].append(pair)
        ranked[pair[1]].append(pair)
    keep = set()
    for pairs in ranked.values():
        pairs.sort(key=lambda p: (-agg[p]["weight"], -agg[p].get("count", 0)))
        keep.update(pairs[:TOP_EDGES])
    return [{"sourceId": a, "targetId": b, **agg[(a, b)]} for (a, b) in sorted(keep)]


# ---------------------------------------------------------------- k-means mode

def kmeans_mode(emb_path):
    import numpy as np

    emb = json.load(open(emb_path))
    ids = [n["id"] for n in nodes]
    missing = [i for i in ids if i not in emb]
    if missing:
        raise SystemExit(f"{len(missing)} public atoms missing embeddings, e.g. {missing[:3]}")
    X = np.asarray([emb[i]["vec"] for i in ids], dtype=np.float32)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    print(f"embeddings: {X.shape[0]} x {X.shape[1]}")

    def kmeans(k, seed):
        rng = np.random.default_rng(seed)
        # k-means++ init
        C = np.empty((k, X.shape[1]), dtype=np.float32)
        C[0] = X[rng.integers(len(X))]
        d2 = np.full(len(X), np.inf, dtype=np.float32)
        for i in range(1, k):
            d2 = np.minimum(d2, 1.0 - X @ C[i - 1])
            p = np.clip(d2, 1e-9, None); p /= p.sum()
            C[i] = X[rng.choice(len(X), p=p)]
        assign = None
        for _ in range(MAX_ITERS):
            new = np.argmax(X @ C.T, axis=1)          # cosine == dot on unit sphere
            if assign is not None and (new == assign).all():
                break
            assign = new
            for j in range(k):
                m = assign == j
                C[j] = X[m].mean(axis=0) if m.any() else X[rng.integers(len(X))]
            C /= np.linalg.norm(C, axis=1, keepdims=True)
        return assign, C

    def silhouette(assign, seed):
        rng = np.random.default_rng(seed)
        idx = rng.choice(len(X), size=min(SIL_SAMPLE, len(X)), replace=False)
        S, A = X[idx], assign[idx]
        D = 1.0 - S @ S.T
        score = np.zeros(len(idx))
        means = {j: D[:, A == j].mean(axis=1) for j in np.unique(A)}
        for r in range(len(idx)):
            own = A[r]
            same = (A == own).sum()
            if same < 2:
                continue
            a = means[own][r] * same / (same - 1)      # exclude self-distance
            b = min(v[r] for j, v in means.items() if j != own)
            score[r] = (b - a) / max(a, b)
        return score.mean()

    best = None
    for k in K_CANDIDATES:
        assign, C = kmeans(k, SEED)
        sil = silhouette(assign, SEED)
        occupied = len(np.unique(assign))
        print(f"k={k}: silhouette={sil:.4f} ({occupied} non-empty clusters)")
        if best is None or sil > best[0]:
            best = (sil, k, assign, C)
    sil, k, assign, C = best
    print(f"picked k={k}")

    clusters = []
    for j in range(k):
        m = np.flatnonzero(assign == j)
        if not len(m):
            continue
        order = m[np.argsort(-(X[m] @ C[j]))]          # members by closeness to true centroid
        rep = ids[order[0]]
        # label: closest-to-centroid atom whose name is descriptive (terse names like
        # "Belief" or "Working" make bad theme labels)
        label_atom = next((ids[i] for i in order[:10] if len(by_id[ids[i]]["name"].split()) >= 4), rep)
        clusters.append(make_cluster(f"c{len(clusters)}", [ids[i] for i in m], rep, label_atom))

    sims = C @ C.T
    agg = {}
    live = [j for j in range(k) if (assign == j).any()]
    remap = {j: f"c{i}" for i, j in enumerate(live)}
    for ai, a in enumerate(live):
        for b in live[ai + 1:]:
            agg[(remap[a], remap[b])] = {"weight": round(float(sims[a, b]), 4)}
    cluster_edges = prune_edges(agg)
    ws = sorted(e["weight"] for e in cluster_edges)
    print(f"kept edge weights: min={ws[0]} med={ws[len(ws)//2]} max={ws[-1]}")
    return clusters, cluster_edges, {"method": "kmeans", "k": k}


# ---------------------------------------------------------------- label-prop mode

def label_prop_mode():
    def label_prop(ids, min_w, seed):
        idset = set(ids)
        labels = {i: i for i in ids}
        order = sorted(ids)
        rng = random.Random(seed)
        for _ in range(MAX_ITERS):
            rng.shuffle(order)
            changed = 0
            for nid in order:
                votes = collections.defaultdict(float)
                for m, w in adj[nid]:
                    if w >= min_w and m in idset:
                        votes[labels[m]] += w
                if not votes:
                    continue
                best = max(sorted(votes), key=lambda l: votes[l])
                if best != labels[nid]:
                    labels[nid] = best
                    changed += 1
            if changed == 0:
                break
        groups = collections.defaultdict(list)
        for nid, lab in labels.items():
            groups[lab].append(nid)
        return list(groups.values())

    MAX_SIZE, SPLIT_STEP = 150, 0.04

    def split(ids, min_w, seed):
        if len(ids) <= MAX_SIZE:
            return [ids]
        parts = label_prop(ids, min_w + SPLIT_STEP, seed)
        if len(parts) == 1:
            return [ids]
        out = []
        for i, p in enumerate(sorted(parts, key=lambda p: (-len(p), p))):
            out.extend(split(p, min_w + SPLIT_STEP, seed * 31 + i + 1))
        return out

    base_w = min(w for nbrs in adj.values() for _, w in nbrs)
    communities = []
    for i, part in enumerate(label_prop(sorted(by_id), base_w, SEED)):
        communities.extend(split(part, base_w, SEED * 17 + i))

    clusters, cluster_of = [], {}
    for members in sorted(communities, key=lambda c: (-len(c), c)):
        if len(members) < MIN_MEMBERS:
            continue
        mset = set(members)
        wdeg = {m: sum(w for t, w in adj[m] if t in mset) for m in members}
        rep = max(members, key=lambda m: wdeg[m])
        c = make_cluster(f"c{len(clusters)}", members, rep)
        for m in members:
            cluster_of[m] = c["id"]
        clusters.append(c)

    agg = {}
    for e in edges:
        a, b = cluster_of.get(e["sourceId"]), cluster_of.get(e["targetId"])
        if not a or not b or a == b:
            continue
        k = (a, b) if a < b else (b, a)
        cur = agg.setdefault(k, {"weight": 0.0, "count": 0})
        cur["weight"] = max(cur["weight"], e["weight"])
        cur["count"] += 1
    return clusters, prune_edges(agg), {"method": "label-prop"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--embeddings", help="path to private embeddings.json (id -> {vec}); enables k-means mode")
    args = ap.parse_args()

    if args.embeddings:
        clusters, cluster_edges, meta = kmeans_mode(args.embeddings)
    else:
        clusters, cluster_edges, meta = label_prop_mode()

    clusters.sort(key=lambda c: -len(c["memberIds"]))
    sizes = sorted((len(c["memberIds"]) for c in clusters), reverse=True)
    covered = sum(sizes)
    print(f"{len(clusters)} clusters covering {covered}/{len(nodes)} atoms")
    print(f"sizes: max={sizes[0]} p50={sizes[len(sizes)//2]} min={sizes[-1]}")
    print(f"{len(cluster_edges)} inter-cluster edges")

    out = os.path.join(HERE, "clusters.json")
    json.dump({**meta, "clusters": clusters, "clusterEdges": cluster_edges}, open(out, "w"))
    print("wrote", out, f"({os.path.getsize(out) // 1024} KB)")
