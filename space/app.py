"""Earnings Wiki — chat with a structured corpus of earnings-call analyses.

Free-tier friendly: retrieval is local (pure-python BM25-ish), generation uses the
HF Inference API (set HF_TOKEN as a Space secret; override MODEL_ID to taste).
"""
import json
import math
import os
import re
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
    try:
        out = client.chat_completion(messages=messages, model=MODEL_ID, max_tokens=800, temperature=0.3)
        return out.choices[0].message.content
    except Exception as e:
        return f"Model call failed ({type(e).__name__}) — the free Inference API may be rate-limited; try again shortly."

with gr.Blocks(title="Earnings Wiki") as demo:
    gr.Markdown("# Earnings Wiki\nAsk questions across four quarters of structured earnings-call analyses "
                "(~130 large-cap companies, 10 standing questions per call). "
                "*AI-generated summaries — may contain errors. Not investment advice.*")
    with gr.Tab("Ask the corpus"):
        gr.ChatInterface(chat, type="messages",
                         examples=["What constraints are binding companies right now?",
                                   "What are companies saying about token or inference costs?",
                                   "Compare what the cloud providers say the opportunity is",
                                   "Which companies raised capex guidance and why?"])
    with gr.Tab("3D theme graph"):
        gr.Markdown("Every claim from every call, embedded and linked to its nearest claims across companies. "
                    "Use the replay button to watch four quarters of themes assemble.")
        gr.HTML('<iframe src="/gradio_api/file=graph/index.html" style="width:100%;height:80vh;border:0"></iframe>'
                '<p>If the frame is blank, open <a href="/gradio_api/file=graph/index.html" target="_blank">the graph directly</a>.</p>')

demo.launch(allowed_paths=[os.path.join(HERE, "graph")])
