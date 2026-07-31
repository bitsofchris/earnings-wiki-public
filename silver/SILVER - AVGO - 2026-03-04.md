---
ticker: AVGO
call_date: 2026-03-04
report_quarter: 2026-Q1
period_reported: fiscal 2026-Q1
source: bronze/AVGO/2026-Q1/transcript-2026-03-04.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [GOOGLE, ANTHROPIC, META, OPENAI, NVIDIA, VMWARE, GROQ]
answers:
  economy: "No macro commentary — the entire call is a single-thread AI capex/compute buildout story told through 6 named custom-silicon customers."
  business: "Record quarter across the board: revenue $19.3B (+29% y/y), AI semis +106% y/y to $8.4B, EBITDA 68% of revenue; VMware/Infrastructure Software grew only 1% y/y but management frames it as durable, AI-independent annuity, not weakness."
  investing: "Locked multiyear supply of leading-edge wafers, HBM and substrates through 2028 specifically to guarantee XPU delivery to its 6 customers — inventory days rose from 58 to 68 to front-run the ramp."
  scarcity: "Constraint is upstream: leading-edge wafer capacity, HBM, and substrates (T-glass) are the binding inputs, which is why Broadcom raced to lock multiyear agreements ahead of demand rather than compute itself being the limiter."
  forward: "Line of sight to AI chip revenue 'significantly in excess of $100 billion' in 2027, with custom accelerator gigawatt shipments approaching 10GW that year, driven by Google, Anthropic (surging past 3GW), Meta, a newly disclosed OpenAI deal (1GW+ in 2027), and two unnamed customers."
  acting: "Signed a sixth XPU customer (OpenAI, 1GW+ by 2027), added $10B to the buyback, returned $10.9B to shareholders in Q1, and pre-secured 2026-2028 component supply — capital commitments explicitly precede confirmed multiyear demand."
  hedges: "Declined to break out chip-versus-rack dollar mix for the Anthropic deal ('I'd rather not answer that'), and wouldn't confirm precisely how much of the ~$100B 2027 figure is networking versus XPU dollars-per-gigawatt."
  contradictions: "Directly disputed 'recent analyst reports' claiming Meta's MTIA program was dead, and rejected the premise that rack-scale shipments would compress gross margin, calling the suggestion 'a bit hallucinating.'"
  street: "Analysts pressed on hyperscaler ROI/capex-cycle risk, in-house chip (COT) threats to Broadcom's ASIC moat, gross-margin dilution from rack shipments, and reconciling gigawatt math against the $100B 2027 number — Hock dismissed the margin-dilution thesis outright and only partially answered the Anthropic chip-vs-rack ask."
---

# AVGO — fiscal 2026-Q1 call (2026-03-04)

**The key idea:** Broadcom is no longer an AI-supplier-among-many — it has consolidated around 6 strategic, multiyear custom-silicon relationships (Google, Anthropic, Meta, OpenAI, plus two unnamed) and is now the company making the boldest forward claim in the entire AI hardware complex: >$100B of pure chip revenue in 2027, underwritten by supply agreements locked through 2028. The tension is that this is a bet on a handful of customers' continued willingness to build proprietary silicon rather than lean on merchant GPUs — a bet Hock Tan insists is "strategic, not optionality," while simultaneously declining to disclose the granular economics (chip vs. rack, dollars per gigawatt) that would let outsiders verify it.

## The read — 3-5 points from the whole transcript
1. **A sixth customer just surfaced, unprompted.** OpenAI joins the custom-XPU roster with "over 1 gigawatt" of compute in 2027 — a customer disclosure made mid-call, not flagged as a headline event, signaling Broadcom now treats new hyperscaler design wins as routine cadence rather than milestone news.
2. **Broadcom is fighting a media narrative, not just the market.** Hock went out of his way to say "contrary to recent analyst reports, Meta's custom accelerator MTIA road map is alive and well" — an unprompted contradiction of press coverage, suggesting real investor anxiety about in-house chip programs stalling.
3. **Networking, not just XPUs, is becoming a growth leg.** AI networking is guided to jump from ~33% to ~40% of AI revenue in one quarter, driven by exclusivity in 100T Tomahawk 6 switches and 1.6T optical DSPs — Broadcom is monetizing the interconnect layer as aggressively as the compute silicon.
4. **Inference, not training, is now the surprise demand driver.** Hock called out that inference compute needs are "very, very interesting and surprising too to us," reshaping how customers plan capacity — a data point about where AI economics are actually settling, distinct from the training-centric narrative dominant a year ago.
5. **The margin-dilution question got shut down hard, maybe too hard.** When asked whether lower-margin rack shipments would drag gross margin ~500bps, Hock's answer ("you must be a bit hallucinating") and Kirsten's follow-up were emphatic but offered no supporting mechanism — a confident dismissal without much shown work.

## Economy & consumer
- **No macro or consumer language appears anywhere in the call** — Broadcom's customer base here is 6 AI platform builders, not end consumers, and management frames the entire narrative through customer capex commitments rather than broader demand conditions.

## The business — what's working, what's not
- **AI semiconductors are the whole story:** revenue **grew 106% y/y to $8.4B**, "way above our outlook," with Q2 guided to accelerate further to **140% y/y growth**.
- **Custom accelerators specifically grew 140% y/y** in Q1, with Hock stating the ramp "across all our 5 customers is progressing very well" (later revised to 6 mid-call).
- **Non-AI semiconductors are flat** ($4.1B, 0% y/y) — enterprise networking, broadband, server storage grew but were offset by seasonal wireless decline; this segment is now a rounding afterthought next to AI.

## Investing & scarcity
- **Multiyear supply lock-in is the single biggest strategic move disclosed:** Broadcom has "fully secured capacity" of leading-edge wafers, HBM, and substrates for **2026 through 2028** — described as being ahead of peers ("probably the first one to secure that up to '28 or beyond," per Charlie Kawwas).
- **Inventory build reflects anticipatory positioning:** days of inventory on hand rose from **58 days in Q4 to 68 days in Q1**, explicitly "to support strong AI demand," despite capex itself staying tiny (**$250M** in Q1 — this is a fabless, supply-agreement-driven capital strategy, not a build-your-own-fabs one).
- **The binding constraint is upstream components, not compute demand itself:** T-glass, substrates, and HBM were called out by name as the scarce inputs Broadcom raced to lock up "early," ahead of the demand surge actually materializing.

## Where they think it's going vs what they're doing about it
- **Stated belief:** >$100B in pure chip AI revenue in 2027, approaching **10 gigawatts** of custom accelerator shipments, with Anthropic alone surging to **"in excess of 3 gigawatts"** by 2027 and OpenAI ramping to 1GW+.
- **Action behind the belief:** multiyear supply agreements locked through 2028, a newly signed sixth customer, and continued network-silicon roadmap investment (Tomahawk 7 at 2x performance slated for 2027) — the capital and contractual commitments plausibly back the growth claim.
- **The gap:** despite the confident 2027 figure, Broadcom declined to disclose the actual mix assumptions (chip vs. rack revenue for Anthropic, dollar-per-gigawatt detail) that would let analysts stress-test the number — the belief is stated with far more precision than the evidence offered to support it.
- **Also notable:** capex remains minimal ($250M) even as $100B+ revenue claims are made — the growth is being funded through supplier commitments and balance-sheet capacity, not Broadcom's own fixed-asset investment, keeping the model asset-light even at this scale.

## Hedges — what they wouldn't commit to
- **Declined to split Anthropic's ~$20B/gigawatt deal into chips vs. racks** when directly asked twice: "I'd rather not answer that, but we're okay... we're good on our dollars and margin" — a specific, repeated dodge on the one number that would validate the content-per-gigawatt math analysts were trying to build.
- **No hard floor given on gross margin** despite being asked directly whether there's a level below which Broadcom wouldn't ship more (lower-margin) racks — the question was deflected as a false premise rather than answered with a number.

## The street — what analysts asked
- **Repeated attempts to reconcile the ">$100B in 2027" claim** with bottoms-up gigawatt math (Stacy Rasgon walked through customer-by-customer gigawatt counts live on the call) — management confirmed directionally correct math ("close to 10 gigawatts") but wouldn't give exact figures.
- **Persistent skepticism about hyperscaler capex sustainability and ROI timing** — one analyst framed it as "the biggest overhang on the group," asking how Broadcom's forecast survives investor fears that hyperscalers need to show AI returns within 1-2 years.
- **Direct challenge on in-house chip competition (COT — customer-owned tooling)** — Hock's answer leaned heavily on Broadcom's execution moat ("can you produce 100,000 of those chips quickly at yields you can afford?") rather than disputing that COT efforts exist at all.
- **Margin-dilution questions on rack-scale shipments** were met with unusually blunt dismissal rather than data.
- **Compressed worry:** the Street's real anxiety is whether Broadcom's >$100B 2027 number is a bottoms-up commitment they can prove, or a confident extrapolation dressed as one.
