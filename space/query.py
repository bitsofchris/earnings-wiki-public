"""query — context selection over the public earnings-wiki corpus.

Public mirror of the private CLI interfaces (tools/earnwiki.py `gold`,
tools/clusters.py digest): the chat and the CLI share this one module.

  select(corpus, symbols=, sector=, since=, until=, questions=, text=, k=)
      filter the answer fragments the way `earnwiki gold` filters silver notes
      (symbols / sector / date range / standing-question keys), then rank by
      BM25 relevance to free text within that scope.

  theme_digest(corpus, symbols=, sector=, since=, until=, top=)
      per-theme over-time rollup from the k-means theme layer: distinct
      companies, claims per quarter, share-per-1000 trend, emerging/fading
      classification — same metrics as the private clusters.py digest.

CLI (for testing and terminal use):
  python3 query.py --symbols NVDA,AMD --text "capex guidance"
  python3 query.py --sector semis --question scarcity --since 2026-01-01
  python3 query.py --themes [--sector semis]
"""
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- corpus

def load(root=HERE):
    """Load fragments + graph metadata once; returns the corpus dict all queries take."""
    frags = json.load(open(os.path.join(root, "fragments.json")))
    nodes = json.load(open(os.path.join(root, "graph", "nodes.json")))["nodes"]
    cj = json.load(open(os.path.join(root, "graph", "clusters.json")))
    by_id = {n["id"]: n for n in nodes}
    sector_of = {}
    for n in nodes:
        sector_of.setdefault(n["ticker"], n["sector"])
    for f in frags:
        f["sector"] = sector_of.get(f["ticker"], "other")
        f["_toks"] = Counter(_toks(f["ticker"] + " " + f["question"] + " " + f["text"]))
    df = Counter()
    for f in frags:
        df.update(f["_toks"].keys())
    quarters = sorted({n["quarter"] for n in nodes})
    q_totals = Counter(n["quarter"] for n in nodes)
    return {
        "fragments": frags, "df": df, "n": len(frags),
        "nodes": by_id, "clusters": cj["clusters"],
        "sectors": sorted(set(sector_of.values())),
        "questions": sorted({f["question"] for f in frags}),
        "quarters": quarters, "q_totals": q_totals,
        "max_date": max(f["date"] for f in frags),
    }


def _toks(s):
    return re.findall(r"[a-z0-9]{2,}", s.lower())


# ---------------------------------------------------------------- fragment selection

def select(corpus, symbols=None, sector=None, since=None, until=None,
           questions=None, text=None, k=28):
    """Filter fragments (gold-style scope), then BM25-rank by `text` inside the scope.
    With no text, returns the scope ordered newest-first (capped at k)."""
    symbols = {s.upper() for s in symbols} if symbols else None
    questions = set(questions) if questions else None
    scope = [f for f in corpus["fragments"]
             if (not symbols or f["ticker"] in symbols)
             and (not sector or f["sector"] == sector)
             and (not since or f["date"] >= since)
             and (not until or f["date"] <= until)
             and (not questions or f["question"] in questions)]
    if not text:
        return sorted(scope, key=lambda f: f["date"], reverse=True)[:k]
    q, n, df = _toks(text), corpus["n"], corpus["df"]
    scored = []
    for f in scope:
        s = sum(f["_toks"][t] * math.log(1 + n / (1 + df[t])) for t in q if t in f["_toks"])
        if s > 0:
            scored.append((s, f))
    scored.sort(key=lambda x: (-x[0], x[1]["date"]))
    out = [f for _, f in scored[:k]]
    if len(out) < k:
        # the scope is the user's real filter; zero-overlap fragments still belong
        # in it — backfill newest-first rather than starving the context
        chosen = {id(f) for f in out}
        rest = sorted((f for f in scope if id(f) not in chosen),
                      key=lambda f: f["date"], reverse=True)
        out += rest[:k - len(out)]
    return out


# ---------------------------------------------------------------- theme trends

def theme_digest(corpus, symbols=None, sector=None, since=None, until=None, top=20):
    """Rank themes by cross-company weight in scope; classify their trajectory.

    share/1000 = scoped claims per 1000 corpus atoms that quarter (normalizes for
    uneven quarter coverage — same normalization as the private digest).
    trend: emerging (born in the two newest quarters), rising / fading
    (last-quarter share vs. mean of prior quarters), else steady.

    Trend math uses only MATURE quarters: a quarter mid-earnings-season has a
    handful of atoms, and shares computed against a tiny denominator are noise
    (the private digest excludes such partitions outright).
    """
    symbols = {s.upper() for s in symbols} if symbols else None
    quarters, q_totals = corpus["quarters"], corpus["q_totals"]
    median_total = sorted(q_totals.values())[len(q_totals) // 2]
    mature = [q for q in quarters if q_totals[q] >= 0.25 * median_total] or quarters
    out = []
    for c in corpus["clusters"]:
        ms = [corpus["nodes"][i] for i in c["memberIds"]]
        ms = [m for m in ms
              if (not symbols or m["ticker"] in symbols)
              and (not sector or m["sector"] == sector)
              and (not since or m["call_date"] >= since)
              and (not until or m["call_date"] <= until)]
        tickers = Counter(m["ticker"] for m in ms)
        if len(tickers) < 3:          # cross-company rule, also enforced per-scope
            continue
        qc = Counter(m["quarter"] for m in ms)
        share = {q: round(1000 * qc.get(q, 0) / q_totals[q], 2) for q in quarters}
        first_q = min(qc)
        last = share.get(mature[-1], 0)
        prior = [share[q] for q in mature[:-1]]
        delta = round(last - (sum(prior) / max(1, len(prior))), 2)
        if first_q > quarters[0]:      # born after the corpus start = genuinely new
            trend = "emerging"
        elif delta >= 1.0:
            trend = "rising"
        elif delta <= -1.0:
            trend = "fading"
        else:
            trend = "steady"
        out.append({
            "id": c["id"], "label": c["label"], "terms": c.get("terms", []),
            "n_tickers": len(tickers), "n_claims": len(ms),
            "top_tickers": [t for t, _ in tickers.most_common(6)],
            "per_quarter": {q: qc.get(q, 0) for q in quarters},
            "share_per_1000": share, "first_quarter": first_q,
            "delta_share": delta, "trend": trend,
            "samples": [f"{m['ticker']} {m['call_date']}: {m['name']}"
                        for m in sorted(ms, key=lambda m: m["call_date"], reverse=True)[:3]],
        })
    out.sort(key=lambda t: (-t["n_tickers"], -t["n_claims"]))
    return out[:top]


def format_themes(themes):
    """Render a digest for LLM context (or terminal reading)."""
    lines = []
    for t in themes:
        pq = " ".join(f"{q.split('-')[1]}:{n}" for q, n in t["per_quarter"].items())
        new = "NEW THEME (did not exist at corpus start) — " if t["trend"] == "emerging" else ""
        lines.append(
            f"[THEME {t['id']}] {new}{t['label']}\n"
            f"  {t['n_tickers']} companies · {t['n_claims']} claims · claims/quarter {pq} · "
            f"{t['trend']} (Δshare {t['delta_share']:+}) · since {t['first_quarter']}\n"
            f"  top: {', '.join(t['top_tickers'])}\n"
            + "".join(f"  · {s}\n" for s in t["samples"]))
    return "\n".join(lines)


def format_fragments(frags):
    return "\n".join(f"[{f['ticker']} {f['date']} {f['question']}] {f['text']}" for f in frags)


# ---------------------------------------------------------------- plan parsing

PLAN_DEFAULT = {"symbols": None, "sector": None, "since": None, "until": None,
                "questions": None, "mode": "lookup", "text": None}

def parse_plan(reply, corpus):
    """Parse the filter-extraction model reply into a validated plan.

    Tolerant by design: anything malformed or out-of-vocabulary degrades field by
    field toward PLAN_DEFAULT (plain unscoped lookup) — a bad extraction must
    never make the chat worse than no extraction."""
    plan = dict(PLAN_DEFAULT)
    m = re.search(r"\{.*\}", reply or "", re.S)
    if not m:
        return plan
    try:
        raw = json.loads(m.group(0))
    except (json.JSONDecodeError, ValueError):
        return plan
    if not isinstance(raw, dict):
        return plan
    syms = raw.get("symbols")
    if isinstance(syms, list):
        ok = [s.upper() for s in syms if isinstance(s, str) and re.fullmatch(r"[A-Za-z.\-]{1,6}", s)]
        plan["symbols"] = ok or None
    if raw.get("sector") in corpus["sectors"]:
        plan["sector"] = raw["sector"]
    for k in ("since", "until"):
        v = raw.get(k)
        if isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
            plan[k] = v
    qs = raw.get("questions")
    if isinstance(qs, list):
        ok = [x for x in qs if x in corpus["questions"]]
        plan["questions"] = ok or None
    if raw.get("mode") == "themes":
        plan["mode"] = "themes"
    t = raw.get("text")
    if isinstance(t, str) and t.strip():
        plan["text"] = t.strip()
    return plan


# ---------------------------------------------------------------- CLI

def _val(flag):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else None

if __name__ == "__main__":
    corpus = load()
    common = dict(
        symbols=[s for s in (_val("--symbols") or "").split(",") if s] or None,
        sector=_val("--sector"), since=_val("--since"), until=_val("--until"))
    if "--themes" in sys.argv:
        print(format_themes(theme_digest(corpus, **common, top=int(_val("--top") or 20))))
    else:
        qs = [q for q in (_val("--question") or "").split(",") if q] or None
        frags = select(corpus, **common, questions=qs, text=_val("--text"),
                       k=int(_val("--k") or 28))
        print(format_fragments(frags))
        print(f"\n{len(frags)} fragments (filters: {common}, questions={qs})", file=sys.stderr)
