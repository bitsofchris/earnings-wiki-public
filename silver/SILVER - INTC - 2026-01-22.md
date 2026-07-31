---
ticker: INTC
call_date: 2026-01-22
report_quarter: 2026-Q1
period_reported: fiscal 2025-Q4
source: bronze/INTC/2026-Q1/transcript-2026-01-22.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [NVIDIA, TSMC, SAMSUNG, SOFTBANK, MOBILEYE, ALTERA, SILVER LAKE, IMS]
answers:
  economy: "AI-driven infrastructure demand is outrunning industry-wide supply for CPUs, DRAM, NAND and substrates; Intel calls it \"an intense AI-driven demand environment constrained by supply\" after a tariff-uncertain first half of 2025."
  consumer: "PC TAM grew for a second straight year (>290M units, fastest growth since 2021) off the post-COVID 2023 bottom, with lean client CPU inventory and \"excitement for Series 3\" — but memory pricing pressure could cap client revenue in 2026."
  business: "Fifth straight quarter of beating guidance and Panther Lake (Core Ultra Series 3) shipped ahead of plan on 18A, but the company is turning away revenue it can't supply — DCAI grew 15% sequentially and CFO Dave Zinsner says it \"would have been meaningfully higher if we had more supply.\""
  investing: "2026 CapEx moves from a planned decline to \"flat to down slightly,\" weighted to cleanroom-light tool spend to fix yield/throughput bottlenecks now, while 14A capacity spend stays frozen until customers commit — CEO Lip-Bu Tan: 14A capacity build waits \"until we have customers secured.\""
  scarcity: "Internal wafer supply is the binding constraint — finished-goods inventory buffer is down to ~40% of peak, forcing a hand-to-mouth allocation between client and data center, compounded by external DRAM/NAND/substrate shortages the company doesn't control."
  forward: "Management expects Q1 to be the trough, supply improving \"beginning in Q2 and for each of the remaining quarters,\" a strong DCAI growth year, and gross margin path from 34.5% toward a 40% target and beyond as Panther Lake's cost structure improves."
  acting: "Centralized data center and AI silicon under one leader (Kevork), simplified the server roadmap to focus resources on 16-channel Diamond Rapids, accelerated Coral Rapids (bringing back multithreading), and is prioritizing scarce wafers toward data center over the low end of client."
  hedges: "Won't commit 14A capacity CapEx until firm customer volume commitments land (expected 2H26–1H27); won't give a numeric external foundry success target, deferring specifics to the 2H26 Investor Day; gross margin guidance stayed qualitative (\"not an acceptable level\") rather than quantified beyond Q1."
  contradictions: "Six months ago the company and \"every hyperscaler customer\" it talked to expected core counts to rise but unit volumes to stay flat — unit demand then \"rapidly increased,\" and Intel wasn't managing supply to that scenario, i.e., its own demand planning missed the inflection it now calls durable for \"several years.\""
  street: "Analysts pressed hard on the supply/inventory mismatch (how a company with its own fabs ends up unable to meet demand), CapEx discipline versus TSMC/Samsung's aggressive tool ordering, gross margin bridge precision, foundry success metrics/timeline, and ARM-vs-x86 share risk if Intel can't supply — management repeatedly deferred hard numbers to the 2H26 Analyst Day."
---

# INTC — fiscal 2025-Q4 call (2026-01-22)

**The key idea:** Intel beat guidance for a fifth straight quarter, but the real story is a company leaving money on the table — demand for CPUs (especially data center) is outrunning what its own fabs can ship, and the fix (better yields, more tool spend, mix-shifting wafers to servers) takes until Q2 to bite. Underneath, this is a bet that x86 CPUs become more essential, not less, as AI workloads scale — while the foundry ambition (14A, external customers, advanced packaging) stays deliberately unfunded until customer commitments materialize.

## The read — 3-5 points from the whole transcript
1. **Supply, not demand, is the Q1 story.** Guidance of $12.2B midpoint is "the low end of that range of seasonal" — CFO Dave Zinsner said they'd be "well above seasonal" with adequate supply. Finished-goods inventory buffer that carried them through H2 2025 is now down to ~40% of peak.
2. **Data center demand caught Intel's own planning off guard.** Zinsner admitted that six months ago "core count was absolutely looking like it would increase, but the units were not expected to increase" — and unit demand "rapidly increased" anyway, a miss he now expects to persist "for several years."
3. **The foundry ambition remains capital-disciplined to the point of being hedged.** Lip-Bu Tan: 14A gets R&D/TD spend only — no capacity CapEx — "until we have customers secured." Firm customer decisions aren't expected until 2H26 through 1H27, pushing risk production to late 2027 and volume production to 2028.
4. **Advanced packaging (EMIB-T) is outperforming internal expectations even as wafer foundry lags.** Zinsner: engagements he once sized "in the hundreds of millions" are now tracking "well north of $1 billion," with customers "willing to even prepay" given supply shortages elsewhere.
5. **Server roadmap got deliberately narrowed to move faster.** Diamond Rapids is now focused solely on the 16-channel high end; multithreading — a known gap versus competitors — doesn't return until Coral Rapids, which Intel is actively working to pull forward in response to customer pressure.

## Economy & consumer
- **AI infrastructure buildout is the demand engine across every segment** — AI PC, traditional server, and networking revenue were all up double digits both sequentially and year-over-year in Q4.
- **PC market is in genuine recovery**, not just AI-PC hype: client consumption TAM exceeded 290M units in 2025, the fastest TAM growth since 2021 and a second consecutive year of growth off the 2023 trough.
- **Memory (DRAM/NAND) and substrate scarcity is now an external tax on Intel's plans** — Zinsner flagged "rising component pricing" as a dynamic that "could limit our revenue opportunity this year," particularly in client, where memory is packaged in and directly dilutes margin.

## The business — what's working, what's not
- **Working:** Panther Lake (Core Ultra Series 3) shipped 3 SKUs by end of 2025 versus a committed 1, powering 200+ notebook designs at CES, with benchmarks Intel claims are "50% to 100% better than peers."
- **Working:** Custom ASIC revenue grew over 50% in 2025, +26% sequentially, crossing a $1B annualized run rate — chasing what Zinsner sizes as a $100B TAM.
- **Not working:** CCG (client) revenue fell 4% quarter-over-quarter even as AI PC units grew 16%, because Intel is deliberately starving the low end of client to feed data center.
- **Not working:** Intel Foundry posted a $2.5B operating loss in Q4, worsening $188M sequentially on the early 18A ramp — the foundry bet is still expensive with limited external revenue ($222M, largely U.S. government and Altera deconsolidation effects).
- **Yields are "in line with our internal plans" but Tan says they're "still below what I want them to be,"** improving roughly 7-8% per month but "not quite to the industry-leading standard yet."

## Investing & scarcity
- **CapEx guidance flipped** from "down" to "flat to down slightly," weighted toward the first half, with the incremental dollars going almost entirely to tools rather than new cleanroom space — a bet that throughput/yield fixes have better ROI than adding capacity.
- **14A capacity spend stays gated on customer commitments** — a deliberate scarcity-of-capital discipline Tan attributes to his own experience at Cadence, wanting confirmed volume before deploying capacity CapEx.
- **The binding constraint is internal wafer supply plus external component scarcity (memory, substrates)**, not demand, not capital access — Intel's own fabs give it a lever (yield/throughput improvement) competitors sourcing from TSMC don't have, but they're using it defensively, not offensively.
- **People/leadership scarcity is being addressed directly**: DCAI and AI silicon were centralized under a newly recruited leader (Kevork) specifically to tighten CPU/GPU/platform coordination.

## Where they think it's going vs what they're doing about it
- **Belief:** Supply improves steadily starting Q2 through the rest of 2026, DCAI has "a strong year of growth" ahead, and x86 server demand is structural, not cyclical, due to AI's compute-coordination role.
- **Action backing it:** Ramping wafer starts "pretty much across the board" on Intel 7, Intel 3, and 18A every quarter; simplifying the server roadmap (16-channel Diamond Rapids focus, accelerated Coral Rapids) to get differentiated products out faster.
- **Belief without matching action (the gap):** Tan describes the AI-accelerator/ASIC opportunity as one where "Intel can truly disrupt and differentiate," and foundry as reaching "trust and consistency" — but capacity dollars for both 14A external foundry and the broader accelerator strategy remain explicitly withheld pending 2H26 customer commitments. The rhetoric of urgency (rebuild "this iconic American company") is paired with capital discipline that pushes real foundry scale to 2027-2028.
- **Gross margin target (40%+) is stated as a goal but Q1 guide is 34.5%, called "by no means an acceptable level"** — the bridge is entirely dependent on execution (yield, Panther Lake cost curve) rather than any near-term revenue or pricing action disclosed on the call.

## Hedges — what they wouldn't commit to
- **No numeric target for external foundry success** — Tan and Zinsner both deferred specificity (revenue level, timeline of "'27? '28? later?") to the planned 2H26 Investor Day.
- **No firm 14A capacity buildout** until customer volume commitments are secured — explicitly held back even amid competitive pressure to match TSMC/Samsung's aggressive tool-ordering pace.
- **Declined to give precise full-year gross margin guidance**, offering only qualitative direction ("should benefit us," "mix can go in any different direction") beyond the Q1 number.
- **Wouldn't say supply constraints fully resolve in 2026** — Zinsner: "we won't be completely out of the woods."

## The street — what analysts asked
- Analysts converged on one anxiety: **how does a company with its own fabs end up supply-constrained and holding $11.6B of inventory in the wrong place?** Zinsner's answer — a demand-planning miss on data center unit growth, not a manufacturing capacity failure — was pressed twice and didn't fully satisfy the skepticism.
- Recurring theme: **CapEx discipline versus competitive urgency** — why isn't Intel ordering tools more aggressively given TSMC/Samsung are, and could waiting for 2H26 customer commitments cost them lead-time on 14A equipment.
- Secondary cluster: **foundry business definition of success and timeline** — analysts wanted numeric external-revenue targets and got deferred to the Investor Day instead.
- Also asked: **server roadmap execution risk** (Diamond Rapids' lack of multithreading, Coral Rapids timing), memory cost pass-through to client margins, and whether ARM-based servers gain share while Intel can't supply x86 demand.
- Compressed worry: **is Intel's supply shortfall a temporary execution problem it can fix with yield gains, or a sign it under-invested in capacity just as AI-driven CPU demand structurally re-accelerated?**
