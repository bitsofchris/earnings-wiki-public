# Graph & Themes Pipeline

**Description:** How raw earnings-call analyses become the theme graph and chat corpus, and the rules that keep the output meaningful. This is the canonical path — deviations from it have produced every quality failure so far.

**When to use:** rebuilding after a new quarter of silver notes lands, debugging "why does this theme look like mush," or extending the pipeline.

## The distillation ladder

```
transcript (private bronze)
  → silver note                one Claude pass per call, ten standing questions
  → atoms (nodes.json)         one claim per bullet: name + description + facets
  → embeddings (private)       1536-dim, per atom
  → themes (clusters.json)     spherical k-means, silhouette-picked k
  → LLM theme summaries        title + 2-sentence summary per theme
  → UI (graph/index.html)      3D explorer: themes view default, atoms view raw
  → chat (space/app.py)        filter extraction → scoped query → cited answer
```

Every layer below silver is derived and rebuildable; the markdown notes are the truth.

## The three intent rules (why this produces signal, not mush)

1. **Intent at extraction.** The ten standing questions asked of every call make atoms
   *comparable* across companies and quarters. Guideline that matters most (now in the
   private silver prompt, style rule 7): every atom title must be a self-contained
   claim, never a section label — downstream tooling displays titles stripped of
   context. (~10% of pre-rule atoms violate this; `claimText()` in the UI and the
   `substantive()` filter in clustering compensate for history.)

2. **Intent at counting.** A theme carries weight because *multiple companies* converge
   on it: members are deduped to one claim per company per quarter (centroid-nearest
   kept), themes under 3 distinct companies are dropped, and node size = companies,
   not claims. Without this, the biggest "theme" was one company repeating itself.

3. **Intent at description.** A theme is described by an LLM synthesis of its members
   (GraphRAG-style community summary; the private pipeline's RULE TWO) — never by one
   member's text. The medoid atom's name is only a fallback when labeling is skipped.

## Rebuild (each new quarter)

```bash
# 1. after silver notes + export_public.py + embeddings refresh in the private repo:
export HF_TOKEN=$(hf auth token)
uv run --with numpy --with "huggingface_hub>=0.24" graph/build_clusters.py \
    --embeddings ../earnings-wiki/.graph-lab/embeddings.json --label

# 2. sync + test + ship
cp graph/index.html graph/clusters.json space/graph/
python3 -m unittest discover tests
git add -A && git commit && git push   # GitHub Action snapshots the tree to the HF Space
```

`--label` adds the LLM title/summary pass (~150 calls, a few minutes). Without it the
build still works and the UI/chat fall back to flagged medoid labels. `LABEL_MODEL`
overrides the labeling model. Without `--embeddings`, a stdlib label-propagation
fallback runs on the public kNN edges.

## Acceptance test (competency questions)

Before shipping a rebuild, the corpus must answer these well in the chat — they are the
requirements spec, not marketing copy:

- Where is the economy heading, according to management teams?
- What's happening to the consumer right now?
- What's getting scarce or more expensive?
- Is anyone actually making money from AI yet?
- Where is the money actually going — what are companies funding?
- What are companies saying versus what are they actually doing?

If a rebuild makes these answers vaguer or less attributed, the rebuild is wrong.

## Research anchors

- Guidelines at extraction: GoLLIE (arXiv:2310.03668), on-demand IE (arXiv:2310.16040)
- Community summaries & local-vs-global questions: GraphRAG (arXiv:2404.16130),
  RAG vs GraphRAG evaluation (arXiv:2502.11371)
- Competency questions as scope + acceptance test: ontology engineering
  (Grüninger & Fox lineage; survey: arXiv:2409.08820 intro)
