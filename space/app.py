"""Earnings Wiki — chat with a structured corpus of earnings-call analyses.

Retrieval mirrors the private earnwiki CLI (see query.py): the model first
extracts filters (symbols / sector / date range / standing-question keys /
lookup-vs-themes mode) from the user's question, query.py runs that scoped
selection locally, and a second model call answers from the scoped context.

Free-tier friendly: retrieval is local; generation uses the HF Inference API
(set HF_TOKEN as a Space secret with Inference Providers permission;
override MODEL_ID to taste).
"""
import json
import os
import re
import traceback

import gradio as gr
from huggingface_hub import InferenceClient

import query as q

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = q.load(HERE)
MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen2.5-7B-Instruct")
client = InferenceClient(token=os.getenv("HF_TOKEN"))

PLAN_PROMPT = f"""You translate a question about public-company earnings calls into search filters.
Reply with ONLY a JSON object, no prose:
{{"symbols": [], "sector": null, "since": null, "until": null, "questions": [], "mode": "lookup", "text": ""}}

- symbols: stock tickers explicitly referenced (company names -> tickers), else []
- sector: exactly one of {json.dumps(CORPUS['sectors'])} or null
- since/until: "YYYY-MM-DD" bounds only if the question names a time range, else null.
  Today is {CORPUS['max_date']}; the corpus spans {CORPUS['quarters'][0]} to {CORPUS['quarters'][-1]}.
  Resolve relative ranges ("since April", "last two quarters") against today's date.
  For "over the last year"-style questions leave since/until null — the corpus is one year.
- questions: matching standing-question keys from {json.dumps(CORPUS['questions'])}, else []
  (economy=macro read, scarcity=binding constraints, street=analyst pressure,
   contradictions=say-vs-do gaps, acting=what they're funding, forward=guidance)
- mode: "themes" if the question is about themes/trends emerging, fading, going quiet,
  changing over time, or what many companies are converging on; else "lookup"
- text: the content words to search for, stripped of filter words

Question: """

SYSTEM = """You answer questions about public-company earnings calls using ONLY the provided context.
Context contains answer fragments tagged [TICKER date question-key] and may contain theme-trend
digests tagged [THEME id] with per-quarter claim counts across companies.
Rules: cite inline as [TICKER date]; ground trend claims in the digest numbers. If the context
doesn't cover the question, say so.
These are AI-generated summaries that may contain errors; they are not investment advice."""


def plan_filters(message):
    """LLM pass 1: extract a validated filter plan; any failure degrades to plain lookup."""
    try:
        out = client.chat_completion(messages=[{"role": "user", "content": PLAN_PROMPT + message}],
                                     model=MODEL_ID, max_tokens=250, temperature=0)
        return q.parse_plan(out.choices[0].message.content, CORPUS)
    except Exception:
        traceback.print_exc()
        return q.parse_plan("", CORPUS)


def build_context(plan, message):
    scope = dict(symbols=plan["symbols"], sector=plan["sector"],
                 since=plan["since"], until=plan["until"])
    text = plan["text"] or message
    if plan["mode"] == "themes":
        themes = q.theme_digest(CORPUS, **scope, top=1000)  # all themes; partition below
        # trend-diverse digest: broadest themes + biggest risers + biggest faders,
        # so both "what's emerging" and "what went quiet" have real material
        broad = themes[:8]
        # late-born themes first (genuinely new), then the sharpest risers
        rising = sorted((t for t in themes if t["trend"] in ("emerging", "rising")),
                        key=lambda t: (t["first_quarter"], t["delta_share"]), reverse=True)[:6]
        fading = sorted((t for t in themes if t["trend"] == "fading"),
                        key=lambda t: t["delta_share"])[:6]
        seen, digest = set(), []
        for t in broad + rising + fading:
            if t["id"] not in seen:
                seen.add(t["id"])
                digest.append(t)
        frags = q.select(CORPUS, **scope, questions=plan["questions"], text=text, k=12)
        q0, qn = CORPUS["quarters"][0], CORPUS["quarters"][-1]
        return (f"Theme trends (cross-company, claims per quarter; corpus spans {q0} to {qn}, "
                f"so a theme born after {q0} is genuinely new — otherwise 'newness' means rising share):\n\n"
                + q.format_themes(digest)
                + "\n\nSupporting fragments:\n" + q.format_fragments(frags))
    frags = q.select(CORPUS, **scope, questions=plan["questions"], text=text, k=28)
    if not frags:  # scope too tight — retry unscoped rather than answering from nothing
        frags = q.select(CORPUS, text=text, k=28)
    return q.format_fragments(frags)


def chat(message, history):
    if not os.getenv("HF_TOKEN"):
        return "HF_TOKEN is not set on this Space, so the model call can't authenticate."
    plan = plan_filters(message)
    context = build_context(plan, message)
    messages = [{"role": "system", "content": SYSTEM}]
    for h in history[-4:]:
        messages.append({"role": h["role"], "content": h["content"]})
    messages.append({"role": "user", "content": f"Context:\n{context}\n\nQuestion: {message}"})
    try:
        out = client.chat_completion(messages=messages, model=MODEL_ID, max_tokens=800, temperature=0.3)
        return out.choices[0].message.content
    except Exception as e:
        traceback.print_exc()  # full detail in the Space logs
        status = getattr(getattr(e, "response", None), "status_code", None)
        if status in (401, 403):
            return ("Model call rejected (HTTP %s): the Space's HF_TOKEN is invalid or lacks the "
                    "'Inference Providers' permission." % status)
        if status == 402:
            return "Model call rejected (HTTP 402): the account is out of inference credits for this billing period."
        detail = str(e).split("\n")[0][:200]
        return f"Model call failed ({type(e).__name__}{': ' + str(status) if status else ''}) — {detail}"


with gr.Blocks(title="Earnings Wiki") as demo:
    gr.Markdown("# Earnings Wiki — talk to four quarters of earnings calls\n"
                "*AI-generated analysis — may contain errors. Not investment advice.*")
    with gr.Tab("Graph + chat"):
        with gr.Row():
            with gr.Column(scale=3):
                GRAPH_URL = f"/gradio_api/file={os.path.join(HERE, 'graph', 'index.html')}"
                gr.HTML(f'<iframe src="{GRAPH_URL}" style="width:100%;height:82vh;border:0;border-radius:8px"></iframe>'
                        f'<p style="margin:4px 0 0">Hit ▶ replay to watch themes assemble over four quarters · '
                        f'<a href="{GRAPH_URL}" target="_blank">open full-screen</a></p>')
            with gr.Column(scale=2):
                gr.ChatInterface(chat, type="messages", chatbot=gr.Chatbot(height=560, type="messages"),
                                 examples=["What new themes emerged over the last year?",
                                           "Which themes have gone quiet?",
                                           "What constraint is binding each cloud provider?",
                                           "Who raised capex guidance, and what reason did they give?",
                                           "What did analysts press Apple on, and what got dodged?",
                                           "Where do managements' beliefs diverge from what they're actually funding?"])
    with gr.Tab("About"):
        gr.Markdown("""
Earnings calls are the most information-dense public statements companies make — executives on the record,
grilled by professionals who are paid to be skeptical.

This project reads a set of them (~130 big caps, every quarter) and **extracts specific ideas through fixed
lenses** — what's scarce, what they believe vs. what they fund, what they dodged, what analysts pressed on —
instead of summarizing. Intent-based extraction beats generic LLM summaries: the same questions asked of every
company every quarter produce *comparable atoms*.

Those atoms become a **knowledge graph** (embeddings + k-means themes). A theme only counts when **multiple
companies** converge on it — one company restating a point five ways is deduped to one claim per quarter.
The replay slider shows themes forming over four quarters. The chat answers from the same corpus: it first
extracts your filters (tickers, sector, time range, question lens), runs the scoped query locally, and cites
what it used.

Things to try: *what new themes emerged this year? · which themes went quiet? · what's the most common thing
analysts asked about? · which companies contradict each other? · what does everyone say is scarce?*

Transcripts via Yahoo Finance through the open `defeatbeta/yahoo-finance-data` mirror. Everything here is
AI-generated, can contain errors, and is not investment advice.
""")

if __name__ == "__main__":
    demo.launch(allowed_paths=[os.path.join(HERE, "graph")])
