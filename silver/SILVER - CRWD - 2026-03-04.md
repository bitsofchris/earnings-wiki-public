---
ticker: CRWD
call_date: 2026-03-04
report_quarter: 2026-Q1
period_reported: fiscal 2026-Q4
source: bronze/CRWD/2026-Q1/transcript-2026-03-04.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [NVIDIA, AMD, INTEL, DELL, HPE, SUPER MICRO, VAST DATA, AWS, OCI, GCP, AZURE, COREWEAVE, NEBIUS, CRUSOE, ANTHROPIC, OPENAI, GOOGLE, MICROSOFT, SGNL.AI, SERAPHIC, PANGEA, ONUM, ADAPTIVE SHIELD, EY, ACCENTURE, DELOITTE, HCL, WIPRO, KPMG, INFOSYS, KROLL, PAX8, NINJAONE]
answers:
  economy: "No macro commentary — the framing is entirely AI-adoption-driven demand, not cyclical spend. Kurtz explicitly says the AI security tailwind is \"not cyclical, it is structural.\""
  business: "Record quarter across nearly every metric: $331M net new ARR (+47% YoY), $5.25B ending ARR (+24%), 25% operating margin, 29% FCF margin, third straight quarter of net new ARR acceleration. Endpoint accelerated for a second consecutive quarter and Next-Gen SIEM grew 75%+ YoY — the legacy core and the new bets are both firing simultaneously."
  investing: "Closed three bolt-on AI-security acquisitions (SGNL.ai for identity/zero standing privilege, Seraphic for browser security, Pangea for AIDR) and is deliberately holding back go-to-market scaling on them until native platform integration is done, per Podbere's \"minimal organic contribution\" guidance for the rest of FY27."
  scarcity: "Not compute or capital — it's trust and data exclusivity. Kurtz frames the moat as proprietary breach telemetry (\"cyber RLHF at scale,\" 1 trillion events/day) that no LLM provider can replicate; the binding constraint on rivals is data access, not model quality."
  forward: "Management believes AI adoption bifurcates software into 'existentially vulnerable' point products versus 'thriving' mission-critical infrastructure, with CrowdStrike in the latter camp and set to capture new spend as agents multiply (\"90 AI agents per knowledge worker\")."
  acting: "Backing the belief with product launches (AIDR grew 5x quarter-over-quarter in weeks), M&A closed and integrated under Flex (SGNL, Seraphic, Pangea, Onum), a new Microsoft Azure marketplace deal, and a commission-amortization change (4→5 years) that itself signals a bet on longer customer lifetimes."
  hedges: "Guidance explicitly assumes near-zero organic ARR contribution from the four recent acquisitions through the rest of FY27 — management is not yet willing to underwrite them scaling ahead of integration despite the strong early usage data."
  contradictions: "Kurtz directly rebuts the 'hyperscalers will own security' thesis he says he heard for a decade, pointing to $1.5B in AWS marketplace TCV (+50% YoY) and the new Azure consumption-commitment deal as evidence hyperscaler partnership, not competition, is what materialized."
  street: "Analysts converged on one anxiety across nearly every question: does frontier-model progress (explicitly Anthropic/Claude) commoditize CrowdStrike's SIEM/SOC and endpoint franchises. Secondary threads were identity/CCP renewal mix, cloud security competitive durability, and agent/seat pricing under AI-driven headcount shifts. Management's answer was consistent and largely unchallenged: telemetry and real-time enforcement beat LLM text generation for breach-stopping — the crowd's worry was never really tested with a hard follow-up."
---

# CRWD — fiscal 2026-Q4 call (2026-03-04)

**The key idea:** CrowdStrike posted its best quarter ever (record net new ARR, record margins, record FCF) while spending the entire call rebutting a market narrative it clearly feels threatened by — that frontier AI labs will commoditize security software. The tension: the numbers say AI is a tailwind today, but the guide explicitly excludes any near-term payoff from the four acquisitions built to prove that thesis, and management's moat argument rests on trust and proprietary telemetry rather than anything defensible in a pure product-feature sense.

## The read — 3-5 points from the whole transcript
1. **Acceleration, not deceleration, in the "AI eats software" narrative window.** Net new ARR grew 47% YoY in Q4, the third straight quarter of acceleration, and endpoint — the business AI was supposed to cannibalize — accelerated for a second consecutive quarter. Kurtz: "Amidst today's AI backdrop, our endpoint business accelerated for the second consecutive quarter."
2. **Flex is now effectively the entire go-to-market motion.** $1.69B in ending ARR sits in Flex accounts (+120% YoY), re-Flex rate rose from 5% to 23% of the Flex base in a year, and repeat re-Flexers now post a 48% average ARR lift. One account expanded from one module and low six figures to 25 modules and $86M in total Flex contract value — the model is doing real expansion work, not just a pricing wrapper.
3. **The AI-moat argument is about data provenance, not model quality.** Kurtz repeatedly draws the line that LLMs can "summarize alerts, draft queries, speed up triage" but "it's not stopping any breaches in real time" — the differentiator claimed is closed-loop expert-labeled telemetry from real incident response, which he calls "cyber RLHF at scale."
4. **Four acquisitions in rapid succession, all deliberately throttled.** SGNL.ai (zero standing privilege identity), Seraphic (browser security), Pangea (AIDR), and Onum closed within the quarter, but guidance assumes "minimal organic contribution... for the remaining quarters of FY27" as management prioritizes native integration over go-to-market scaling — a discipline call that trades near-term ARR optics for platform coherence.
5. **A five-year commission amortization change adds $85–95M to operating income** — a GAAP-adjacent accounting choice justified by "longer customer relationship periods," worth noting as a margin tailwind that isn't organic operating leverage.

## Economy & consumer
No discussion of the broader macro or end-consumer environment — CRWD sells to enterprise IT/security buyers, and the entire demand narrative is framed as AI-adoption-driven rather than cyclical. This is itself notable: unlike consumer- or SMB-facing companies, there's zero hedge language about budget scrutiny or elongated sales cycles.

## The business — what's working, what's not
- **Broad-based record quarter:** $331M net new ARR (+47% YoY), $5.25B ending ARR crossing $5B (+24% YoY, "fastest and only pure-play cybersecurity software company" to hit the mark), record $326M operating income (25% margin), record $376M FCF (29% of revenue).
- **Platform consolidation stats point to genuine stickiness:** 50% of subscription customers now use 6+ modules, 24% use 8+; gross retention held at 97%, net retention rose to 115%.
- **Next-Gen SIEM is the standout growth line:** >75% YoY growth to $585M+ ending ARR, cited as displacing legacy SIEM vendors with an "expected 80% faster query performance."
- **What's not emphasized:** no mention of any underperforming segment — an unusually clean quarter across every disclosed metric, which itself warrants skepticism about what's not being surfaced (e.g., no color on down-market/SMB churn dynamics beyond aggregate gross retention).

## Investing & scarcity
- **M&A cadence accelerated sharply:** SGNL.ai, Seraphic, Pangea, and Onum all closed within the quarter, each targeting a specific layer of the "AI attack surface" (identity, browser, AI usage detection, data pipelines).
- **Capex guide: 7-8% of revenue for FY27**, weighted to the first half — modest relative to hyperscaler-scale AI infrastructure spend, reflecting CRWD's asset-light SaaS model even as it rides the AI wave.
- **The constraint that actually binds is trust/compliance positioning, not compute:** Kurtz frames cybersecurity as uniquely intolerant of AI failure modes — "you simply cannot have a hallucination... it's first time final" — positioning data exclusivity and vendor trust, not GPUs, as the scarce resource.

## Where they think it's going vs what they're doing about it
- **Belief:** AI adoption will require an entirely new security layer (AIDR) at every stack tier — GPU foundation, infrastructure OEMs, neoclouds/hyperscalers, model providers, and AI applications/agents — and CrowdStrike claims coverage of all five.
- **Action backing it up:** AIDR (from the Pangea acquisition) grew "5x versus last quarter despite having only been available for a few weeks" — real, fast-moving product traction.
- **Gap:** despite that momentum, FY27 guidance explicitly assumes near-zero organic contribution from AIDR, SGNL, and Seraphic beyond a modeled $5-8M in Q1 acquired ARR — management's own numbers don't yet bet on the belief they're evangelizing, a conservatism worth flagging against the confident rhetoric.
- **Belief on agent economics:** "each knowledge worker will have 90 AI agents," framed as a tailwind even if human seat counts shrink — but no concrete agent-based pricing model was announced; Flex is the only pricing mechanism doing the work today.

## Hedges — what they wouldn't commit to
- **No organic ARR ramp assumed from the four recent acquisitions for the rest of FY27** — despite touting explosive early usage (5x AIDR growth, 300%+ YoY Falcon Shield growth), guidance holds back until integration is complete.
- **No specific agent-based pricing model articulated** when directly asked about consumption-based pricing for AI agents — Kurtz redirected to the existing Flex framework rather than committing to a new pricing primitive.
- **No hard numbers given on identity growth attribution** (renewal of prior CCP/Flex deals vs. net-new product) when asked directly — Kurtz answered with qualitative "extremely high percentage" renewal language rather than a disclosed split.

## The street — what analysts asked
Nearly every question, across seven of nine analysts, circled back to one core worry dressed in different framings: cloud security competitiveness, next-gen SIEM durability, endpoint acceleration drivers, browser security categorization — all were proxies for "does a frontier LLM (Anthropic/Claude named explicitly) eventually commoditize what CrowdStrike sells." Secondary clusters: identity growth composition (CCP renewal vs. net-new) and how Flex/pricing holds up if AI shrinks knowledge-worker seat counts. Management's rebuttal was consistent (telemetry and real-time enforcement beat LLM inference for breach-stopping) and went largely unchallenged — no analyst pushed on whether that moat argument holds if a frontier lab builds its own security-specific fine-tuned model with comparable data access. The compressed worry: **is CrowdStrike's data moat durable, or is the market about to find out LLMs can do "good enough" security triage at a fraction of the cost?**
