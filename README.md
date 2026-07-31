# earnings-wiki (public dataset + explorer)

A structured, longitudinal corpus of large-cap earnings calls — four quarters (2025-Q4 → 2026-Q3), ~130 companies (Nasdaq-100 + Dow 30 + extras), one analysis note per call, every note answering the same ten standing questions.

**⚠️ Everything here is AI-generated analysis of public earnings-call transcripts. It may contain errors. It is not investment advice, and quotes should be verified against primary transcripts before use.**

## What's here

- **`silver/`** — 434 per-call analysis notes (markdown + YAML frontmatter). Each answers: economy · consumer · business · investing · scarcity · forward (beliefs) · acting (commitments) · hedges (what they wouldn't commit to) · contradictions · street (what analysts pressed on). Style: numbers only as deltas, verbatim quotes attributed to executives, honesty about spin.
- **`graph/`** — every claim as an atom (10.7k nodes), embedded (OpenAI text-embedding-3-small) and linked to its nearest claims across companies (63k cosine k-NN edges). `index.html` is a self-contained 3D explorer (three.js via 3d-force-graph) with a time-replay slider — open it over any static server.
- **`space/`** — a Hugging Face Space app (Gradio) to chat with the corpus using a free hosted LLM: local BM25 retrieval over 4.5k question-aligned fragments + HF Inference API generation.

## Provenance

Company webcasts → Yahoo Finance transcripts → the open [`defeatbeta/yahoo-finance-data`](https://huggingface.co/datasets/defeatbeta/yahoo-finance-data) mirror → duckdb → per-call analysis by an isolated LLM session with a fixed question schema. Raw transcripts are **not** republished here — only derived analysis with brief quotes.

## Run the Space

Create a Space (Gradio SDK), upload `space/*` and `graph/`, set an `HF_TOKEN` secret (any free account token) and optionally `MODEL_ID`. Default model: `Qwen/Qwen2.5-7B-Instruct` via the serverless Inference API.

## Schema, briefly

Partition = calendar quarter of the call date. Silver filenames: `SILVER - <TICKER> - <call-date>.md`. The ten questions are the fixed frame; answers are free text; themes are meant to be *discovered* (cluster the graph, or ask the Space) — there is deliberately no tag taxonomy.

## License

Analysis notes and code: MIT. Underlying transcript content remains the property of its owners; this repository contains derived commentary only.
