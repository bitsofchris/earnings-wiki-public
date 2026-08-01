"""Earnings Wiki — chat with a structured corpus of earnings-call analyses.

Free-tier friendly: retrieval is local (pure-python BM25-ish), generation uses the
HF Inference API (set HF_TOKEN as a Space secret; override MODEL_ID to taste).
"""
import json
import math
import os
import re
import traceback
from collections import Counter

import gradio as gr
from huggingface_hub import InferenceClient

HERE = os.path.dirname(os.path.abspath(__file__))
FRAGS = json.load(open(os.path.join(HERE, "fragments.json")))
MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen2.5-7B-Instruct")
client = InferenceClient(token=os.getenv("HF_TOKEN"))

def toks(s):
    return re.findall(r"[a-z0-9]{2,}", s.lower())

DF = Counter()
for f in FRAGS:
    f["_toks"] = Counter(toks(f["ticker"] + " " + f["question"] + " " + f["text"]))
    DF.update(f["_toks"].keys())
N = len(FRAGS)

def retrieve(query, k=28):
    q = toks(query)
    scored = []
    for f in FRAGS:
        s = sum(f["_toks"][t] * math.log(1 + N / (1 + DF[t])) for t in q if t in f["_toks"])
        if s > 0:
            scored.append((s, f))
    scored.sort(key=lambda x: -x[0])
    return [f for _, f in scored[:k]]

SYSTEM = """You answer questions about public-company earnings calls using ONLY the provided context fragments.
Each fragment is an AI-generated analysis of one call, tagged [TICKER date question-type].
Rules: cite fragments inline as [TICKER date]. If the context doesn't cover the question, say so.
These are AI-generated summaries that may contain errors; they are not investment advice."""

def chat(message, history):
    ctx = retrieve(message)
    context = "\n".join(f"[{f['ticker']} {f['date']} {f['question']}] {f['text']}" for f in ctx)
    messages = [{"role": "system", "content": SYSTEM}]
    for h in history[-4:]:
        messages.append({"role": h["role"], "content": h["content"]})
    messages.append({"role": "user", "content": f"Context fragments:\n{context}\n\nQuestion: {message}"})
    if not os.getenv("HF_TOKEN"):
        return "HF_TOKEN is not set on this Space, so the model call can't authenticate."
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

Those atoms become a **knowledge graph** (embeddings + nearest-neighbor edges). No taxonomy is defined up
front — clusters emerge from the data, and the replay slider shows them forming over four quarters. The chat
answers from the same atoms, with citations.

Things to try: *what new themes emerged this year? · which themes went quiet? · what's the most common thing
analysts asked about? · which companies contradict each other? · what does everyone say is scarce?*

Transcripts via Yahoo Finance through the open `defeatbeta/yahoo-finance-data` mirror. Everything here is
AI-generated, can contain errors, and is not investment advice.
""")

demo.launch(allowed_paths=[os.path.join(HERE, "graph")])
