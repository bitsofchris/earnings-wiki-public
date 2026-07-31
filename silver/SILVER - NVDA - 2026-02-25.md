---
ticker: NVDA
call_date: 2026-02-25
report_quarter: 2026-Q1
period_reported: fiscal 2026-Q4
source: bronze/NVDA/2026-Q1/transcript-2026-02-25.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [OPENAI, ANTHROPIC, META, XAI, GROK, AWS, WAYMO, TESLA, UBER, WERIDE, ZOOX, MERCEDES-BENZ, BOSTON DYNAMICS, CATERPILLAR, LG ELECTRONICS, DASSAULT SYSTEMES, SIEMENS, SYNOPSYS, INTEL, NOKIA, COREWEAVE, HUGGING FACE, CURSOR]
answers:
  economy: "Management frames the entire economy as mid-regime-shift: ~$300-400B/year of historical classical-compute CapEx is being replaced by AI CapEx that is already approaching $700B among top-5 hyperscalers, up ~$120B since January alone. Jensen calls this 'a new industrial revolution' rather than a cyclical upswing."
  business: "Record quarter: $68B revenue (+73% YoY), data center +75% YoY/+22% sequentially to $62B, networking +3.5x YoY to $11B; gross margin held ~75% despite fast Blackwell ramp. Weak spots: gaming faces supply-constrained headwinds into Q1+ despite strong demand, and China compute revenue remains zero with no visibility on whether H200 shipments will ever be allowed in."
  investing: "$10B direct equity investment in Anthropic plus a nonexclusive licensing deal absorbing Grok's engineering team (à la Mellanox) — NVIDIA is now investing across the entire model-maker ecosystem (OpenAI, Anthropic, Meta, xAI) rather than just selling into it. Purchase commitments and inventory were built out 'further out in time than usual,' now covering visibility into calendar 2027."
  scarcity: "Power, not chips, is the explicit binding constraint: 'every data center is power-constrained,' so performance-per-watt is described as directly dollarized into customer revenue. Memory/component supply is the secondary constraint, openly blamed for the gaming segment's headwind and clouding gaming's ability to grow YoY in fiscal '27."
  forward: "Jensen expects sequential data-center growth through all of calendar 2026, exceeding the $500B Blackwell+Rubin opportunity previously guided, with 'every single customer' expected to purchase Vera Rubin once available. He reiterates the $3-4T 2030 data-center CapEx envelope and calls agentic AI a just-crossed 'inflection point,' with physical AI/robotics as the next wave."
  acting: "Actually building: shipped first Vera Rubin samples, on track for 2H production; deployed ~9GW of Blackwell already consumed by hyperscalers; started including stock-based comp in non-GAAP metrics (a genuine transparency move Reitzes flagged approvingly); locked purchase commitments into 2027; returned $41B (43% of FCF) via buybacks/dividends even while ramping."
  hedges: "Colette repeatedly declined to size the Vera Rubin second-half ramp ('too early yet to determine how much') or commit to gaming returning to YoY growth in fiscal '27 pending memory supply. On the OpenAI 'partnership agreement,' Jensen says only 'we believe we are close' — a deal still not finalized despite being touted on the call. No answer given on China revenue timing beyond 'we do not know whether any imports will be allowed.'"
  contradictions: "NVIDIA leans on a third-party 'Inference King' SemiAnalysis benchmark and Meta's ad-click/conversion stats to validate ROI it has every incentive to overstate; Jensen's blanket claim that customer cash flow will keep growing because 'compute equals revenue' is asserted as near-tautology rather than demonstrated with hyperscaler free-cash-flow data, which is exactly what the analyst asking the question was worried about."
  street: "Analysts converged on one anxiety cluster: is $700B+ of hyperscaler CapEx sustainable if their own cash flow is compressing, and can NVIDIA still grow if it isn't? Secondary threads covered custom-silicon/decode competition (Grok/CPX), capital-return philosophy given ~$100B annual FCF and a flat stock, chiplet/architecture roadmap, and non-hyperscaler revenue mix. Management answered CapEx-sustainability with philosophy ('compute equals revenue') rather than hyperscaler balance-sheet specifics — the dodge itself is the tell."
---

# NVDA — fiscal 2026-Q4 call (2026-02-25)

**The key idea:** NVIDIA posted a record quarter and reframed its entire growth story around a single equation Jensen repeats like a mantra: "compute equals revenue." The tension underneath the record numbers is that this framing shifts the risk entirely onto customers' willingness (and ability) to keep funding ~$700B of CapEx on faith that inference tokens monetize — a bet NVIDIA is now backing directly with $10B in Anthropic and absorbed Grok engineers rather than just selling into.

## The read — 3-5 points from the whole transcript
1. **The power constraint has replaced the chip constraint as the real story.** Jensen states flatly "every data center is power-constrained," and the entire performance-per-watt marketing (50x on GB300 NVL72, 35x lower cost per token) is really an argument about maximizing revenue per megawatt, not raw compute — this is NVIDIA's honest acknowledgment that the ceiling is now electrons, not silicon.
2. **NVIDIA is becoming a strategic investor in its own demand, not just a vendor.** The $10B Anthropic stake plus the Grok engineer/IP absorption ("as we did with Mellanox") extends a pattern where NVIDIA funds the customers who buy its chips — a flywheel that inflates both revenue and reported CapEx-driven demand, worth watching for circularity risk.
3. **Gaming and China are the two segments management can't spin positive.** Gaming faces open-ended "tight for a couple of quarters" supply constraints with no YoY growth commitment for fiscal '27; China compute revenue is explicitly $0 in guidance with "we do not know whether any imports will be allowed" — rare unhedged admissions of uncertainty on an otherwise triumphant call.
4. **The OpenAI "partnership" is still not signed.** Despite being showcased alongside Anthropic/Meta/xAI as evidence of ecosystem depth, Jensen says only "we continue to work with OpenAI toward a partnership agreement and believe we are close" — a materially unfinished deal presented in the same breath as completed ones.

## Economy & consumer
- **No traditional consumer segment**, but the macro read is stark: classical computing CapEx (~$300-400B/year historically) is being displaced wholesale by AI CapEx now nearing $700B among the top 5 hyperscalers, up ~$120B in analyst estimates since January.
- Jensen positions this as **structural, not cyclical**: "AI is here, AI is not going to go back. AI is going to only get better from here."

## The business — what's working, what's not
- **Working:** Data center revenue +75% YoY to $62B; networking +3.5x YoY to $11B on NVLink/Spectrum-X/InfiniBand demand; gross margin held at 75% even as Blackwell Ultra ramps; professional visualization crossed $1B for the first time (+159% YoY).
- **Not working:** Gaming growth (+47% YoY) is now capped by **supply, not demand** — "we expect supply constraints to be the headwind to Gaming in Q1 and beyond." China data-center compute revenue remains **zero**, with small H200 approvals generating no actual revenue yet.
- Even legacy hardware is oversubscribed: "even Hopper and much of the 6-year-old Ampere based products are sold out in the cloud" — a proof point for how tight the whole install base is, not just Blackwell.

## Investing & scarcity
- **R&D approaching $20B annually**, funding "extreme co-design" across chips, systems, networking, and software to keep outrunning Moore's Law on performance-per-watt.
- **Scarcity is power first, memory/component supply second.** Every architectural claim on the call — NVLink 72's 50x perf/watt, Rubin's promised 10x lower inference token cost — is justified in terms of maximizing revenue per fixed power budget, not raw throughput.
- Inventory grew 8% quarter-over-quarter with purchase commitments "further out in time than usual," extending into calendar 2027 — a bet that current demand visibility is durable, not a one-quarter spike.

## Where they think it's going vs what they're doing about it
- **Believes:** sequential growth through all of calendar 2026 exceeding the prior $500B Blackwell+Rubin opportunity; a $3-4T data-center CapEx envelope by 2030; agentic AI has "reached an inflection point" in just the last 2-3 months, with physical AI/robotics next.
- **Is doing:** shipped first Vera Rubin samples this week, on track for second-half production; deployed ~9GW of Blackwell capacity already; committed $10B to Anthropic and absorbed Grok's team; built purchase commitments out to 2027.
- **The gap:** the stated $3-4T 2030 vision and "every customer will deploy Vera Rubin" confidence sit ahead of concrete commitments — Colette repeatedly declines to quantify how much of Rubin's ramp lands in the second half ("too early yet to determine"), so the boldest forward claims outrun what's actually locked in.

## Hedges — what they wouldn't commit to
- **Vera Rubin ramp sizing:** "It's too early yet to determine how much... that beginning ramp will start in the second half."
- **Gaming YoY growth for fiscal '27:** contingent on memory supply improving, explicitly "too early for us to know at this time."
- **China revenue timing:** "We do not know whether any imports will be allowed into China" — no forecast given despite naming it as a live variable.
- **OpenAI deal terms:** "we believe we are close" to a partnership agreement — not yet signed, despite being presented alongside finalized deals.
- Declined to commit to a large one-time buyback despite ~$100B expected annual free cash flow and a flat stock price, instead reiterating a "strategic and disciplined" ongoing capital-return process.

## The street — what analysts asked
- The dominant anxiety, raised directly and revisited implicitly across multiple questions: **can hyperscaler CapEx (~$700B, up sharply) keep growing when those customers' own cash flow is compressing, and does NVIDIA's growth story break if it doesn't?** Management's answer was philosophical ("compute equals revenue") rather than balance-sheet-specific.
- Secondary clusters: the strategic logic of NVIDIA's ecosystem investments (Anthropic, OpenAI, Grok, CoreWeave, Intel, Nokia, Synopsys) as more than financial engineering; competitive/architecture questions on custom silicon and Grok's decode technology; sustainability of mid-70s gross margins into the Rubin transition; capital-return posture given a flat stock despite blowout results; and customer-mix diversification beyond the top-5 hyperscalers.
- Compressed worry: **is $700B+ of AI CapEx actually self-funding, or is NVIDIA's own balance sheet (via Anthropic, Grok, and friends) now propping up the demand it reports?**
