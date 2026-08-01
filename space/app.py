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
Context contains claims tagged [TICKER date ...] and may contain theme-trend digests tagged [THEME id].

Rules:
- Lead with the signal. Open with the 2-4 strongest cross-company takeaways as short bold
  statements (e.g. "**Memory is the new bottleneck, and it's driving price increases.**"),
  then back each with named-company evidence.
- Be concrete. Every point must name WHO said it, with specifics (numbers, quotes, products),
  cited inline as [TICKER date]. Never present a claim without attribution.
- A theme's "representative claim" is ONE company's wording for a cross-company pattern — never
  restate it as a general fact. Describe the pattern in your own words, then ground it with
  2-3 named company examples from the theme's sample claims.
- Ground any trend statement (emerging/fading/rising) in the digest's per-quarter numbers.
- If the context doesn't cover the question, say so plainly.
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
    frags = q.select(CORPUS, **scope, questions=plan["questions"], text=text, k=18)
    if not frags:  # scope too tight — retry unscoped rather than answering from nothing
        frags = q.select(CORPUS, text=text, k=18)
    atoms = q.select_atoms(CORPUS, **scope, text=text, k=10)
    return (q.format_fragments(frags)
            + "\n\nDetailed claims (richer context for the strongest matches):\n"
            + q.format_atoms(atoms))


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
                                 examples=["Where is the economy heading, according to management teams?",
                                           "What's happening to the consumer right now?",
                                           "What's getting scarce or more expensive?",
                                           "Is anyone actually making money from AI yet?",
                                           "Where is the money actually going — what are companies funding?",
                                           "What are companies saying versus what are they actually doing?"])
    with gr.Tab("About"):
        gr.Markdown("""
**What this is:** 434 earnings calls from 125 large-cap US companies (Nasdaq-100 + Dow 30 + extras),
October 9, 2025 through July 30, 2026, analyzed with the same ten questions per call and turned into a
browsable theme graph and a chat you can query.

**The pipeline:** transcript → one LLM analysis per call answering ten fixed questions (what's scarce,
what they believe vs. what they fund, what analysts pressed on, what they dodged, ...) → every claim
becomes an atom (10,667 of them) → atoms are embedded and clustered into 142 cross-company themes,
each titled and summarized by an LLM.

**What you're looking at:** in the graph, each sphere is a theme; its size is how many *distinct
companies* touch it — one company restating a point five ways counts once per quarter, and a theme
under three companies is dropped. The replay slider shows themes forming over the four quarters.
Click a theme for its summary and the underlying claims. The chat answers from the same corpus: it
extracts your filters (tickers, sector, time range, question lens), runs the scoped query locally,
and cites what it used as [TICKER date].

Transcripts via Yahoo Finance through the open `defeatbeta/yahoo-finance-data` mirror. Raw transcripts
are not republished — only derived analysis with brief quotes. Everything here is AI-generated, can
contain errors, and is not investment advice.
""")

if __name__ == "__main__":
    demo.launch(allowed_paths=[os.path.join(HERE, "graph")])
