---
ticker: INTC
call_date: 2026-04-23
report_quarter: 2026-Q2
period_reported: fiscal 2026-Q1
source: bronze/INTC/2026-Q2/transcript-2026-04-23.md
generated: 2026-07-30 (automated silver pass, schema v3)
mentions: [GOOGLE, NVIDIA, SPACEX, XAI, TESLA, SAMBANOVA, AMD, ARM, AMAZON, TSMC, MOBILEYE]
answers:
  economy: "Semiconductor TAM is approaching $1T on AI demand; management flags dynamic macro/geopolitical conditions and rising component costs (memory, wafers, substrates) as swing factors on 2H demand."
  consumer: "PC TAM guided down low double-digits for the full year as management 'prudently' plans for 2H weakness, even as Q1 AI PC mix crossed 60% of client CPUs."
  business: "Revenue, gross margin and EPS beat guidance for a sixth straight quarter, with demand outrunning supply across all businesses (\"revenue would have been meaningfully higher\" without supply limits); Foundry still posted a $2.4B operating loss despite improving yields."
  investing: "2026 CapEx moved from 'flat to down' to flat y/y, with tool spend up ~25% while space spend falls — a deliberate shift toward wafer-out capacity; 14A investment stepped up ahead of external customer commitments expected in 2H26/1H27."
  scarcity: "Supply, not demand, is the binding constraint — CFO wouldn't size the shortfall precisely but said the missed revenue 'starts with a B'; rising memory, substrate and T-glass costs are an emerging cost-side constraint into 2H."
  forward: "Management believes CPU-to-accelerator ratios are structurally shifting back toward CPU as AI moves from training to inference to agentic/physical AI, and expects double-digit server CPU unit growth extending into 2027."
  acting: "Signed multi-year LTAs (Google named explicitly) locking in volume/pricing for 3-5 years; repurchased the 49% Fab 34 JV stake for ~$7.7B cash + $6.5B debt; expanded Malaysia advanced-packaging capacity; struck the Terafab partnership with SpaceX/xAI/Tesla to explore new manufacturing economics."
  hedges: "Declined to name most LTA counterparties ('some of them we just didn't announce'), declined to quantify the supply shortfall precisely, declined to detail 18A yield numbers, and would not commit to whether Terafab becomes a standard foundry deal or a licensing-style arrangement ('we would update you as we go')."
  contradictions: "None flagged — the closest tension is Foundry still losing $2.4B while management touts 18A yields beating internal targets; the loss narrative and the yield-inflection narrative are both true but pull in opposite directions on investor confidence."
  street: "Analysts pressed hardest on: how much revenue is being left on the table from supply constraints, what agentic AI actually means for CPU TAM (with one analyst directly testing ARM's $100B TAM claim), gross margin bridge confusion given strong server growth but flat-to-down margins, and Arm/AMD competitive share risk in servers. The compressed worry: is Intel's 'demand exceeds supply' story real structural CPU renaissance, or a temporary supply squeeze that masks margin and competitive fragility once capacity catches up?"
---

# INTC — fiscal 2026-Q1 call (2026-04-23)

**The key idea:** Intel is telling a "good problem to have" story — demand for CPUs (especially Xeon server) is outrunning its own factory output for a sixth straight beat-and-raise quarter, and management is reframing the AI narrative around the CPU as orchestration layer for inference/agentic workloads rather than just the GPU's sidekick. But underneath the beat, Foundry still lost $2.4B, gross margin guidance is flat-to-down on 18A ramp costs, and CapEx discipline is bending ("flat" not "down") to chase supply — the tension between "we're constrained by supply, not demand" and "we still can't make foundry profitable" is the real story.

## The read — 3-5 points from the whole transcript
1. **CPU is being repositioned as AI infrastructure, not legacy compute.** Tan's central pitch: "CPU now serves as the orchestration layer and critical control plane for the entire AI stack," citing a CPU:GPU ratio moving from roughly 1:8 toward 1:4 and potentially toward parity as workloads shift from training to inference to agentic. This is the thesis the whole quarter's narrative hangs on.
2. **Demand exceeds supply, and the gap is not small.** When pressed to quantify under-shipment, Zinsner wouldn't give a percentage but said flatly "it starts with a B" — a multi-billion-dollar unfulfilled demand estimate, a striking admission for a company that spent the prior year in survival mode.
3. **The Google LTA is a template, not a one-off.** Intel signed a 3-5 year volume/pricing agreement with Google (Xeon plus ASIC/IPU business) and says other undisclosed LTAs exist — customers who prefer confidentiality. This is Intel building a backlog of committed demand it can plan supply against, a meaningfully different posture than opportunistic selling.
4. **18A yields are ahead of plan but Foundry economics aren't fixed.** Yields are "running ahead of internal projections" — a year-end target now expected to be hit mid-year — yet Foundry still posted a $2.4B operating loss and Panther Lake margins remain below corporate average even as volume ramps 6-7x quarter over quarter. Fixing yield is necessary but not sufficient for Foundry profitability.
5. **CapEx discipline is loosening under demand pressure.** Guidance moved from "flat to down" to flat y/y over two consecutive quarters, with tool spend up ~25% even as space spend falls — a real signal that management is now willing to spend more to chase committed demand rather than hold the line on capital discipline.

## Economy & consumer
- **Macro framed as a genuine swing factor, not boilerplate.** Zinsner explicitly cited "views on global growth, policy, and trade" alongside rising component costs (memory, wafers, substrates) as forces that "could impact demand for our product at some point in the year."
- **PC TAM guided down despite strong current bookings.** Full-year PC unit TAM is expected down low double-digits, "in line with industry peers," with management "prudently planning for PC demand to weaken in the second half" — a cautious posture layered under near-term order strength.
- **AI PC adoption crossing the halfway mark.** AI PC revenue grew 8% sequentially and now represents over 60% of client CPU mix, with Core Ultra Series 3 called "our strongest product launch in five years."
- **Intel separates industry consumption from its own billings**, arguing pricing and customer inventory replenishment will insulate Intel's client revenue from the full brunt of the industry TAM decline — Q2's run-rate is expected to hold "flattish" the rest of the year.

## The business — what's working, what's not
- **Sixth consecutive quarter of guidance beats**, with revenue $1.4B above the midpoint of guide and gross margin ~650bps ahead, driven by volume (including selling previously reserved/de-spec'd inventory), mix, pricing, and 18A yield.
- **DCAI (data center) is the clear growth engine**: revenue up 22% y/y, ASIC revenue nearly doubling y/y, and Xeon 6 selected as host CPU for NVIDIA's DGX Rubin NVL8 systems — a notable win validating the CPU-anchor-architecture thesis even inside NVIDIA's own stack.
- **Foundry remains structurally unprofitable**: $2.4B operating loss, improved only $72M q/q, still absorbing "the bulk of the costs associated with the early ramp of Intel 18A" plus a deliberate step-up in 14A investment ahead of any confirmed external customer.
- **The ASIC/custom-silicon business is bigger than disclosed expectations suggested** — Zinsner noted it's already at a run rate "north of $1 billion" and said people "have been surprised about how big the business is already."
- **Q1 gross margin outperformance leaned partly on non-repeatable levers** — selling previously reserved/de-spec'd inventory helped Q1 and Zinsner flagged "I'm not sure we have that benefit in the second quarter," meaning some of the beat was a one-time draw-down, not a run-rate improvement.

## Investing & scarcity
- **CapEx guidance loosened for the second straight quarter**: from "flat to down" (prior call) to "flat to down" to now flat y/y, driven by "the current demand environment" — tool spend specifically up ~25% y/y even as total CapEx holds flat, because space spend (previously built out) is coming down.
- **Supply, not demand, is the binding constraint across every segment** — "demand continued to run ahead of supply for all our businesses," and the CFO's refusal to size the gap more precisely than "starts with a B" underscores how large and persistent the shortfall is.
- **Emerging cost-side scarcity in 2H**: rising memory, substrate, and T-glass costs are called out as a "growing headwind" that could offset gross margin gains from yield and mix improvement later in the year.
- **Wafer capacity allocation is now a strategic lever**: management is running more of Intel's own future products on 14A specifically "to have better control over our supply chain" at a time when "advanced wafer capacity is in short supply" — an explicit hedge against depending on external foundry (TSMC) capacity that is itself tight.
- **Advanced packaging backlog is running far above initial expectations** — Zinsner admitted he "naively" modeled these deals in the hundreds of millions and they're actually landing "in the billions of dollars per year."

## Where they think it's going vs what they're doing about it
- **Belief**: management is confident CPU will be "a meaningful growth engine for the company in the years ahead, not just the quarters ahead," anchored on the CPU:GPU ratio shift and double-digit server CPU unit growth extending into 2027.
- **Action matching the belief**: LTAs with Google (and undisclosed others) locking multi-year volume/pricing, the Fab 34 buyout to capture full economics of a ramping fab, Malaysia packaging expansion, and CapEx tilted harder toward wafer-out tooling.
- **Gap**: despite the conviction on structural CPU demand, Intel is explicitly declining to commit incremental external-foundry CapEx until "customer signals" become "more concrete in the back half of this year and into early next year" — the company is funding its own supply build-out aggressively but staying deliberately non-committal on capacity dedicated to third-party foundry customers, i.e., talking bigger about the AI CPU opportunity than it's currently willing to build capacity for outside customers.
- **Terafab (SpaceX/xAI/Tesla) is high-profile but low-commitment language** — described as "a very broad relationship" to "explore innovative ways to refactor silicon process technology," with no specifics on structure, economics, or whether it becomes a dedicated fab arrangement — more a signaling/partnership announcement than a funded commitment at this stage.

## Hedges — what they wouldn't commit to
- **Refused to name most LTA counterparties**: "some of them we just didn't announce," respecting customer confidentiality — makes the true scale of the committed-demand backlog unverifiable from outside.
- **Refused to quantify the supply/demand gap precisely** beyond "starts with a B," despite direct analyst pressure for a percentage estimate.
- **Declined to disclose 18A yield figures**, calling them "a closely guarded proprietary piece of information."
- **No commitment on Terafab's ultimate structure** — whether it becomes a standard foundry customer relationship or something closer to turning over an entire fab — "we would update you as we go."
- **No specific quantification of agentic-AI CPU TAM** when directly asked whether ARM's $100B figure was reasonable — Tan called it "hard to quantify" and punted to a future update.

## The street — what analysts asked
- Recurring themes: sizing the supply shortfall (repeatedly, from multiple analysts), the mechanics and confidentiality of long-term customer agreements, gross margin bridge confusion given strong DCAI growth without matching margin expansion, and Arm/AMD competitive threats in servers (Amazon Graviton, Google Axion, NVIDIA's Vera CPU rack all cited by name).
- Management's clearest dodge was on quantifying the agentic-AI CPU opportunity — repeated requests for a TAM number or growth framework were met with qualitative color ("hard to quantify," "we will update you") rather than figures.
- Also notable: an analyst directly tested whether Intel's CapEx discipline is being quietly abandoned by the pace of demand ("does structurally CapEx need to go up"), which management answered by pointing to yield/cycle-time efficiency rather than committing to bigger capital spend.
- The compressed worry: is Intel actually solving a structural supply/demand mismatch through disciplined execution, or just riding a temporary shortage that flatters margins and hides how far Foundry still is from profitability?
