"""Roll up raw atoms into theme clusters for the graph explorer.

Runs weighted label propagation over the similarity edges (no embeddings needed —
the public repo only ships the kNN graph), then emits clusters.json:

  clusters: one entry per community with >= MIN_MEMBERS members
    - id, label (representative atom's name), repId (medoid: max weighted degree
      inside the community), memberIds, dominant sector/section, first_date
  clusterEdges: aggregated inter-cluster links (max member-pair weight + count)

Atoms in tiny communities (< MIN_MEMBERS) stay unclustered; the UI keeps showing
them as individual dots in atom view and drops them from the cluster view.

Usage: python3 graph/build_clusters.py   (writes graph/clusters.json; copy to space/graph/)
Deterministic: fixed shuffle seed, ties broken by sorted label id.
"""
import collections
import json
import math
import os
import random
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_MEMBERS = 4
MAX_ITERS = 30
SEED = 42
TOP_EDGES = 4        # keep each cluster's N strongest inter-cluster links
N_TERMS = 5          # distinctive terms per cluster (TF-IDF over member text)

STOP = set("""a an and are as at be but by for from has have in into is it its more not of on or
over than that the their they this to was were will with we our you your""".split())

nodes = json.load(open(os.path.join(HERE, "nodes.json")))["nodes"]
edges = json.load(open(os.path.join(HERE, "edges.json")))["edges"]
by_id = {n["id"]: n for n in nodes}

adj = collections.defaultdict(list)
for e in edges:
    adj[e["sourceId"]].append((e["targetId"], e["weight"]))
    adj[e["targetId"]].append((e["sourceId"], e["weight"]))

MAX_SIZE = 150       # communities bigger than this get re-split with stronger edges
SPLIT_STEP = 0.04    # threshold bump per split level


def label_prop(ids, min_w, seed):
    """Weighted label propagation restricted to `ids` and edges >= min_w."""
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


def split(ids, min_w, seed):
    """Split oversized communities by re-running label prop on stronger edges."""
    if len(ids) <= MAX_SIZE:
        return [ids]
    parts = label_prop(ids, min_w + SPLIT_STEP, seed)
    if len(parts) == 1:  # refused to split even with stronger edges — accept as-is
        return [ids]
    out = []
    for i, p in enumerate(sorted(parts, key=lambda p: (-len(p), p))):
        out.extend(split(p, min_w + SPLIT_STEP, seed * 31 + i + 1))
    return out


base_w = min(w for nbrs in adj.values() for _, w in nbrs)
communities = []
for i, part in enumerate(label_prop(sorted(by_id), base_w, SEED)):
    communities.extend(split(part, base_w, SEED * 17 + i))
groups = {min(c): c for c in communities}

def dominant(members, key):
    return collections.Counter(by_id[m][key] for m in members).most_common(1)[0][0]

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

clusters, cluster_of = [], {}
for lab in sorted(groups, key=lambda l: -len(groups[l])):
    members = sorted(groups[lab])
    if len(members) < MIN_MEMBERS:
        continue
    mset = set(members)
    wdeg = {m: sum(w for t, w in adj[m] if t in mset) for m in members}
    rep = max(members, key=lambda m: wdeg[m])
    cid = f"c{len(clusters)}"
    for m in members:
        cluster_of[m] = cid
    clusters.append({
        "id": cid,
        "label": by_id[rep]["name"],
        "repId": rep,
        "memberIds": members,
        "sector": dominant(members, "sector"),
        "section": dominant(members, "section"),
        "quarter": dominant(members, "quarter"),
        "index": dominant(members, "index"),
        "first_date": min(by_id[m]["call_date"] for m in members),
        "terms": top_terms(members),
    })

agg = {}
for e in edges:
    a, b = cluster_of.get(e["sourceId"]), cluster_of.get(e["targetId"])
    if not a or not b or a == b:
        continue
    k = (a, b) if a < b else (b, a)
    cur = agg.setdefault(k, {"weight": 0.0, "count": 0})
    cur["weight"] = max(cur["weight"], e["weight"])
    cur["count"] += 1

# prune to each cluster's strongest links (by shared-pair count, then weight) —
# the full inter-cluster graph is dense enough to collapse the layout into a ball
ranked = collections.defaultdict(list)
for (a, b), v in agg.items():
    ranked[a].append((a, b))
    ranked[b].append((a, b))
keep = set()
for cid, pairs in ranked.items():
    pairs.sort(key=lambda k: (-agg[k]["count"], -agg[k]["weight"]))
    keep.update(pairs[:TOP_EDGES])
cluster_edges = [{"sourceId": a, "targetId": b, **agg[(a, b)]} for (a, b) in sorted(keep)]

sizes = sorted((len(c["memberIds"]) for c in clusters), reverse=True)
covered = sum(sizes)
print(f"{len(clusters)} clusters covering {covered}/{len(nodes)} atoms "
      f"({len(groups) - len(clusters)} tiny communities left unclustered)")
print(f"sizes: max={sizes[0]} p50={sizes[len(sizes)//2]} min={sizes[-1]}")
print(f"{len(cluster_edges)} inter-cluster edges")

out = os.path.join(HERE, "clusters.json")
json.dump({"clusters": clusters, "clusterEdges": cluster_edges}, open(out, "w"))
print("wrote", out, f"({os.path.getsize(out) // 1024} KB)")
