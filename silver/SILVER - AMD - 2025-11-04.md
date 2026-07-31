---
ticker: AMD
call_date: 2025-11-04
report_quarter: 2025-Q4
period_reported: fiscal 2025-Q3
source: bronze/AMD/2025-Q4/transcript-2025-11-04.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [OPENAI, ORACLE, OCI, MICROSOFT, GOOGLE, ALIBABA, HPE, DELL, LENOVO, SUPER MICRO, SANMINA, ZT SYSTEMS, IBM, ZYPHRA, COHERE, CHARACTER.AI, LUMA AI, HUGGING FACE, VLLM, SGLANG, META, CISCO, G42, DEPARTMENT OF ENERGY, OAK RIDGE NATIONAL LABS, SONY, MICROSOFT XBOX, CRUSOE, DIGITALOCEAN, TENSORWAVE, VULTR, NVIDIA]
answers:
  economy: "Management describes a broad-based, accelerating compute buildout — 'the demand for compute has never been greater' — spanning cloud, enterprise, and sovereign AI, not a narrow AI-only pocket."
  business: "Record quarter across every segment: revenue up 36% YoY to $9.2B, data center up 22% to a record $4.3B, client and gaming up 73% to $4B; embedded remained the lone weak spot, down 8% YoY though up sequentially."
  investing: "Opex jumped 42% YoY to fund R&D and go-to-market for the AI ramp; the quarter also closed the ZT manufacturing sale to Sanmina, converting AMD from a systems-manufacturing owner into a partner reliant on Sanmina to build Helios racks."
  scarcity: "Su frames 2026 as a coordinated ecosystem constraint — power, silicon, memory, and packaging capacity all tight simultaneously — requiring multiyear planning with customers and suppliers rather than a single binding bottleneck."
  forward: "AMD guides Data Center AI to 'tens of billions in annual revenue in 2027' and reiterates the OpenAI deal could be 'well over $100 billion in revenue over the next few years,' with MI450/Helios ramping second half of 2026."
  acting: "AMD signed a multiyear, 6-gigawatt Instinct deal with OpenAI (first gigawatt of MI450 online 2H26) including warrants tied to share-price milestones, sold ZT's manufacturing arm to Sanmina to secure lead rack-build capacity, and is dimensioning its supply chain explicitly to serve multiple hyperscale-scale customers, not just OpenAI."
  hedges: "AMD declined to guide FY2026 or give 2026 gross-margin framework ('we're not guiding into 2026 yet'), gave no MI308-China revenue in Q4 guidance despite having received some licenses, and repeatedly deferred detailed AI-TAM and customer-mix specifics to next week's Analyst Day."
  contradictions: "None stated outright, but Su's insistence AMD is 'dimensioning the supply chain... to have multiple customers at similar scale' sits in tension with analyst math implying OpenAI could be roughly half of data-center GPU revenue by 2027-28 — a concentration risk management downplays rather than directly refutes."
  street: "Analysts converged on three anxieties: OpenAI customer-concentration risk and deal structure (warrants), whether power/component supply becomes the binding constraint on 2026 rack-scale deployments, and precise CPU-vs-GPU growth attribution — Su and Hu visibly parried Stacy Rasgon's repeated attempts to pin down exact server-vs-Instinct growth splits."
---

# AMD — fiscal 2025-Q3 call (2025-11-04)

**The key idea:** This is the OpenAI-deal victory-lap call — record results across every segment, but the real story is AMD converting a single customer relationship (6 GW, potentially $100B+) into proof-of-concept for a much bigger rack-scale AI bet (Helios/MI450) landing in the second half of 2026. Management is confident, but visibly protecting two things under questioning: customer concentration risk and any specifics that would preempt next week's Analyst Day.

## The read — 3-5 points from the whole transcript
1. **CPU is back as a genuine AI story, not just a hedge.** Server CPU revenue hit an all-time high, with Su saying the CPU demand signal is "not a short-term thing... it is a multi-quarter phenomenon" because AI workloads are "spawning more traditional compute." Hyperscalers are now planning "substantially larger CPU build-outs" specifically to support AI serving — a second, less-hyped AI beneficiary line.
2. **The OpenAI deal is the pivot, and AMD knows it.** Su calls it a partnership that could generate "well over $100 billion in revenue over the next few years," with warrants structured so "everybody wins." That's an aggressive framing for a single-customer agreement, and the unusual equity structure (warrants vesting on share-price milestones) is itself a tell of how much AMD needed this signed logo.
3. **Concentration risk is real and management's answer is deflection, not denial.** Asked directly whether OpenAI could be ~half of data-center GPU revenue by 2027-28, Su pivoted to "a very key foundation for us... is to have a broad set of customers" without disputing the math — an evasion worth flagging.
4. **ZT Systems divestiture to Sanmina outsources manufacturing risk right as Helios complexity peaks.** AMD sold the ZT manufacturing business the week before this call, making Sanmina "lead manufacturing partner for Helios" — a bet that a partner can execute rack-scale builds AMD itself chose not to own.
5. **MI308-China remains an unresolved swing factor.** AMD "received some licenses" but excluded any China MI308 revenue from Q4 guidance, calling the situation "still pretty dynamic" — real revenue upside sitting entirely outside guided numbers.

## Economy & consumer
- **Compute demand described as broad-based and durable**, not narrowly AI-driven: "the demand for compute has never been greater as every major breakthrough in business, science and society now relies on access to more powerful, efficient and intelligent computing" (Su).
- No direct consumer-facing exposure; PC/gaming commentary reflects channel and enterprise demand rather than end-consumer health — Ryzen commercial sell-through was up over 30% YoY, suggesting enterprise refresh strength more than consumer spending signal.

## The business — what's working, what's not
- **Every reporting segment grew except embedded.** Data center revenue hit a record $4.3B (+22% YoY); client and gaming surged 73% YoY to $4B on record Ryzen desktop sales and console semi-custom strength ahead of the holidays.
- **Embedded is the one segment still shrinking**, down 8% YoY to $857M, with operating margin compressing from 40% to 33% — end-market softness (test/emulation, industrial) not yet resolved, though sequential improvement and record year-to-date design wins ($14B+) suggest a lagged recovery is coming.
- **Data center AI segment operating margin actually declined** YoY (25% vs 29%) despite record revenue, "driven by higher revenue partially offset by higher R&D investment" — margin dilution from scaling the AI business is an explicit, acknowledged trade-off, not spin.
- **ROCm 7 marks a credible software-stack inflection**: "up to 4.6x higher inference and 3x higher training performance compared to ROCm 6," with day-zero framework support and direct contributions from Hugging Face, vLLM, and SGLang — relevant validation for anyone tracking whether CUDA's moat is eroding.

## Investing & scarcity
- **Opex up 42% YoY** to fund AI R&D and go-to-market, a deliberate margin trade for share gain — Hu frames the data-center GPU priority explicitly as "expand the top line revenue growth and the gross margin dollars" ahead of margin percentage.
- **Constraint is systemic, not singular**: Su describes the binding limits as power, silicon, memory, and packaging capacity all simultaneously tight across the industry, requiring 2-year joint planning with customers and suppliers rather than one clear bottleneck AMD can solve alone.
- **ZT manufacturing sale to Sanmina** converts a prior acquisition (owned manufacturing capability) into an outsourced dependency at the exact moment Helios rack-scale complexity is ramping — a capital-allocation reversal worth watching for execution risk.

## Where they think it's going vs what they're doing about it
- **Belief:** Data center AI reaches "tens of billions in annual revenue in 2027," MI450/Helios ramp sharply in 2H26, and the AI silicon TAM (previously pegged at $500B) is "going up" per Su, with updated figures reserved for Analyst Day.
- **Action:** Signed OpenAI (6 GW multiyear, first GW online 2H26), landed Oracle as MI450 launch partner, secured sovereign-AI wins (UAE/G42, DOE/Oak Ridge "Discovery" supercomputer, "Lux AI" facility), and structured warrants to lock in the OpenAI relationship — these are the closest things to money-and-people-backed commitments matching the stated growth story.
- **Gap:** The tens-of-billions-in-2027 target and TAM-expansion claims are asserted with far more confidence than the concrete guidance behind them — AMD explicitly declined to guide any 2026 numbers on this call, meaning the boldest forward claims currently rest on qualitative "customer pull" language rather than committed backlog disclosed here.

## Hedges — what they wouldn't commit to
- **No FY2026 revenue or gross-margin guidance** given at all ("we're not guiding into 2026 yet"); C.J. Muse's gross-margin framework question got a directional non-answer deferring to "the past" pattern of margin normalizing after a ramp.
- **MI308 China revenue excluded entirely from guidance** despite having received export licenses — Su called the demand environment still being sorted out with customers.
- **Declined to break out server vs. Instinct GPU growth in dollar terms** even under repeated, specific pressure — Hu would only concede "server is a little bit better" directionally.

## The street — what analysts asked
- Two dominant anxieties: **OpenAI concentration risk** (multiple analysts, from Arcuri to Seymore, probed how unique/risky the single-customer scale is) and **2026 supply/power constraints** on the MI450/Helios ramp.
- A secondary thread was **CPU-vs-GPU attribution** — Stacy Rasgon pushed hardest for a clean split between server and Instinct growth and was met with vague "directionally" language rather than numbers, a clear instance of management declining to give the precision requested.
- Compressed worry: **can AMD's supply chain and a still-forming rack-scale ecosystem actually deliver at the scale the OpenAI headline number implies, without becoming dangerously dependent on that one customer?**
