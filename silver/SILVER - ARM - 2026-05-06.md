---
ticker: ARM
call_date: 2026-05-06
report_quarter: 2026-Q2
period_reported: fiscal 2026-Q4
source: bronze/ARM/2026-Q2/transcript-2026-05-06.md
generated: 2026-07-30 (automated silver pass, schema v3)
mentions: [META, SAP, CLOUDFLARE, F5, SK TELECOM, NVIDIA, AMAZON, AWS, GOOGLE, GOOGLE CLOUD, MICROSOFT, AZURE, CEREBRAS, OPENAI, REBELLIONS, POSITRON, SOFTBANK, MEDIATEK, SUPERMICRO, LENOVO, ASROCK, SAMSUNG, TSMC, SYNOPSYS, CADENCE, AMD, INTEL]
answers:
  economy: "No macro discussion beyond chip-cycle framing; management describes an 'AI investment super cycle' now three years running with no visible end, and separately flags flattish-to-slightly-negative mobile unit growth as the one soft spot."
  business: "Record quarter ($1.49B, +20% YoY) and record fiscal year ($4.92B, +23%); royalty growth (+11%) was held back by a tough mobile comp while licensing (+29%) and ACV (+22%) stayed strong — CFO Jason Child: 'we had a particularly strong ramp of MediaTek's Snapdragon 400 a year ago... you saw a bit of a slowdown in royalty revenue' as a result."
  investing: "R&D/OpEx up 30% YoY to fund the new Arm AGI CPU silicon product line launched six weeks prior, while keeping the $1B FY27-28 revenue guide unchanged even as demand doubled — the incremental spend is explicitly framed as small ('a team... in the dozens of people, not hundreds')."
  scarcity: "Supply chain capacity — not demand — is now the gating factor for the AGI CPU ramp: CEO Rene Haas says demand is over $2B for FY27-28 (2x prior) but they are only guiding to $1B 'while we pursue supply chain capacity,' citing wafers, memory, packaging, and test equipment access."
  forward: "Management projects data center CPU TAM exceeding $100B by 2030 (rivals now citing even higher, e.g. AMD's $120B) driven by 4x+ CPU capacity growth for agentic workloads, and reiterates the FY2031 target of $15B AGI CPU + $10B IP revenue = $25B total, >$9 EPS."
  acting: "Despite doubled customer demand, Arm is deliberately NOT raising the $1B FY27-28 revenue guide until supply is secured, and is expanding through partner-built finished racks (Supermicro, Lenovo, ASRock) to lower deployment friction rather than building its own manufacturing capacity."
  hedges: "Child declined to give a firmer FY28 number now ('in Q3, we'll give you a much firmer estimate'), Haas wouldn't commit to precise CPU-core-count or CPU:GPU ratio math ('ratios are a tough way to look at it'), and management repeatedly said the extra $1B+ of demand is real but supply-constrained rather than committed revenue."
  contradictions: "Haas claims Arm, AMD, and Intel all separately claim ~50% data-center CPU share ('you add up to some crazy number') — an implicit admission that vendor share claims in this market are not mutually consistent — while still asserting Arm will hold 'the largest market share by CPU type' by decade end."
  street: "Analysts converged on three anxieties: (1) is the AGI CPU cannibalizing IP/licensing customers who also build Arm chips (answered with an ecosystem-endorsement narrative, not hard commitments); (2) can Arm actually secure enough wafer/memory/packaging supply to convert the doubled demand into revenue; (3) how to model CPU-to-GPU/core ratios and OpEx-to-revenue timing for the new silicon business. The unspoken worry: guidance is being held flat precisely because supply, not demand, is now the constraint — a good problem, but still a constraint management can't yet quantify."
---

# ARM — fiscal 2026-Q4 call (2026-05-06)

**The key idea:** Arm just doubled its own six-week-old demand forecast for its first-ever silicon product (the Arm AGI CPU) but refused to raise revenue guidance, because the constraint moved from "will customers buy this" to "can we get wafers, memory, and packaging capacity." Layered on top is a genuine strategic tension — Arm is now selling finished chips that compete, at the margin, with the same hyperscaler and vendor customers who license its IP — and management's answer amounts to "everyone we asked said yes," not a structural resolution of channel conflict.

## The read — 3-5 points from the whole transcript
1. **Demand outran supply within six weeks.** The AGI CPU launched at the March "Arm Everywhere" event with $1B of stated demand; by this call it's "more than $2 billion... more than double what we stated at launch" — yet guidance stayed at $1B because, per Child, "we are maintaining our outlook of $1 billion while we pursue supply chain capacity."
2. **Two growth engines, deliberately decoupled.** Haas frames IP/royalty (Neoverse/CSS, doubling YoY again) and AGI CPU silicon ($15B by FY2031) as parallel, non-cannibalizing vectors — "don't cannibalize each other. They're going to run in tandem" — a claim investors should watch given it's asserted, not yet proven at scale.
3. **Mobile is quietly going negative and it doesn't matter.** Child expects mobile *unit* growth to "flip to negative" this past quarter, offset entirely by data-center royalty that "more than doubled year-over-year" — Arm's royalty mix is being reshaped by cloud AI, not phones, even as phones remain the volume base.
4. **The ecosystem-conflict question got a PR answer, not a mechanism.** Asked directly whether IP licensees (AWS, Google, NVIDIA, Microsoft) feel threatened by Arm now selling finished silicon, Haas cites unanimous partner "endorsement" videos and quotes from the March launch — no discussion of pricing, allocation, or design-win conflicts between Arm's own chips and licensee chips built on the same IP.
5. **Core-count math is doing more work than the CPU:GPU ratio.** Haas repeatedly redirects "will CPUs approach 1:1 with GPUs" questions toward core-count growth (136 cores in the AGI CPU today, "could I see those core counts doubling or quadrupling" ) as the real TAM driver — a subtle but important reframe of how the $100B+ data-center CPU TAM gets built.

## Economy & consumer
- **No macro read beyond the AI cycle itself.** Management offers no view on rates, employment, or general demand — the only "cycle" referenced is the AI capex cycle, which Child calls a "super cycle" now in its third year, adding "who knows how much longer it goes, but it's at least gonna happen for the next year."
- **Consumer/mobile is soft but not alarming.** Child: mobile unit growth likely "flip to negative," concentrated in "the lower end of the market," which "doesn't have too much impact on us" given Arm's growth is now driven by royalty-rate mix shift (Armv9, CSS penetration) rather than unit volume.

## The business — what's working, what's not
- **Record top line, mixed royalty story.** $1.49B revenue (+20% YoY, above guidance midpoint); royalty +11% held back by a hard MediaTek Snapdragon 400 comp from a year prior — a genuine, disclosed comp headwind rather than spin.
- **Licensing is the current growth engine.** License revenue +29% YoY to $819M, ACV +22% YoY — Child explicitly steers investors to ACV "as it's a key indicator of the underlying licensing trend" over lumpy quarterly license revenue, which is reasonable given SoftBank's flat $200M contribution this quarter shows genuine lumpiness.
- **Data center royalty is the standout.** "Data center royalty has more than doubled year-over-year," attributed to hyperscaler server-chip ramps plus near-100%-share DPU/SmartNIC attach — a clean, credible growth story with less spin than most segments on this call.
- **Margin discipline intact despite R&D surge.** Non-GAAP OpEx +30% YoY yet came in ~$10M under guidance; operating margin held near 49% — management is investing heavily in the new product line without yet sacrificing profitability.

## Investing & scarcity
- **Supply chain, not demand, is now the binding constraint.** Haas: "the number that we talked about end of March was supply in place to support $1 billion of demand, and that includes memory, that includes wafers, that includes packaging, that includes access to test equipment. For the $2 billion, we are now in the process of securing supply" — an unusually candid statement that a hardware business is chasing components, not customers.
- **R&D investment is scaling but the chip-business overhead is framed as small.** Child on incremental AGI CPU OpEx: "It's a team that's in the... probably in the dozens of people, not hundreds" — because most of the expensive engineering work (the compute die) is shared with the existing CSS/IP business, making the new silicon line inherently higher-margin than a standalone chip startup would be.

## Where they think it's going vs what they're doing about it
- **Belief: TAM keeps expanding past their own forecast.** Haas: "$100 billion TAM on March 24th... we were the first company to talk about numbers in that magnitude... Could the number be $120 billion out in that timeframe? Certainly." Action: still holding the $1B FY27-28 guide flat despite 2x demand — belief in market size is racing ahead of committed, supply-backed revenue.
- **Belief: Arm CPUs become "100% attach" alongside every major accelerator (Trainium, TPU, NVIDIA's line).** Action: no new fab/supply capacity announced this call beyond "teams are working around the clock" — the commitment is organizational effort, not yet contracted capacity, wafer allocation, or capex disclosure.
- **Belief: IP and silicon businesses won't cannibalize each other.** Action: no structural separation disclosed (pricing walls, allocation priority, licensee protections) — just ecosystem buy-in gathered ahead of the March launch. The gap between the confident claim and the thin evidentiary base here is the largest talk-vs-action divergence on the call.

## Hedges — what they wouldn't commit to
- **No firmer FY28 number yet.** Child: "in Q3, we'll give you a much firmer estimate of what we expect to deliver in Q4" — declining to convert doubled demand into raised guidance now.
- **Declined to quantify CPU:GPU ratio or per-token orchestration math.** When pushed for a bottom-up core-per-agent or instructions-per-token model, Haas demurred: "I think the latter is a little too complicated to think about it... Ratios are a tough way to look at it."
- **No commitment on long-term license growth rate beyond a floor.** Child: "at least, you know, at least 10% year-on-year growth for the long term is probably being the floor" — explicitly hedging above the near-term 20% guide without giving a real ceiling.

## The street — what analysts asked
- **Supply-chain execution risk dominated.** Multiple questions probed how Arm secures the incremental wafer/memory/packaging capacity behind the $2B demand figure, with management repeatedly deferring firm numbers to Q3.
- **Channel-conflict anxiety surfaced directly.** One question named the tension plainly — Arm's own silicon competing with IP customers who build Arm-based chips — and got an ecosystem-endorsement answer rather than a structural one.
- **Modeling questions on ratios and margin timing.** Analysts pushed on CPU:GPU ratios, core-count economics, and when the new chip business becomes accretive to earnings (answered: "operating profit positive next year," ~35% margin by 2031 vs. ~65% for IP).
- **Compressed worry:** Arm has more demand than it can supply for a brand-new, unproven silicon business, and is asking investors to trust that this won't cannibalize the IP licensees whose goodwill it depends on — with no hard mechanism offered for either problem.
