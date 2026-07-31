---
ticker: DDOG
call_date: 2025-11-06
report_quarter: 2025-Q4
period_reported: fiscal 2025-Q3
source: bronze/DDOG/2025-Q4/transcript-2025-11-06.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [AWS, ORACLE, OCI, HUGGING FACE, OPENAI, ANTHROPIC, CURSOR, GITHUB COPILOT, BLOCK, GOLDMAN SACHS, MORGAN STANLEY, BARCLAYS, JPMORGAN, CITI, KEYBANC, BTIG, BANK OF AMERICA, OPPENHEIMER, TD COWEN, WOLFE RESEARCH, WELLS FARGO, NEEDHAM, UBS, WILLIAM BLAIR]
answers:
  economy: "Demand environment is broadly positive but not surging — Pomel: \"I don't know that we see massive acceleration of cloud migration, but at least the environment is not pushing the other way.\" Growth acceleration was broad-based across enterprise/SMB, all spending bands, and industries."
  consumer: "N/A — DDOG's customers are businesses (developers/ops teams), not end consumers; SMB commentary (companies <1,000 employees) stood in for the smaller-customer read and also showed a strengthening demand cycle even excluding AI names."
  business: "Revenue grew 28% y/y to $886M, beating the top of guidance, with non-AI-native sequential usage growth the strongest in 12 quarters and security ARR growth accelerating to mid-50s% y/y from mid-40s last quarter. Gross/net retention stayed low-90s-churn-stable (mid-to-high 90s GRR, 120% NRR flat) — the flat NRR is a trailing-12-month artifact of a metric that lags the in-quarter acceleration, per CFO."
  investing: "Continued heavy sales-capacity build (new-logo bookings more than doubled y/y to a record) and multiyear comp-plan carve-outs to reward reps for landing new/smaller/harder Fortune 500 accounts instead of only expanding existing ones. R&D dollars concentrated on Bits AI SRE/security agents, LLM Observability GA features, and GPU monitoring — the last of which Pomel flagged as pre-revenue."
  scarcity: "Not compute or capital — the binding constraint is sales-force attention and comp-plan design: land-and-expand economics naturally pull reps toward easy existing-account dollars, so DDOG had to engineer incentives (multiyear plans, carve-outs) to force focus onto new/smaller/upmarket logos."
  forward: "Management expects the digital-transformation/cloud-migration secular growth to persist \"for a very long time\" with normal ebbs and flows, and does not expect AI-native customer classification to remain meaningful as AI usage broadens into every company's stack."
  acting: "Doubling down on Bits AI SRE/security agents (dozens of enthusiastic customer quotes, GA prep, deepening remediation not just detection), expanded channel investment behind the security suite, and built an OCI integration to follow AI-native customers diversifying onto Oracle infrastructure even though Pomel called that near-term opportunity \"remote today.\""
  hedges: "Declined to size the packaging/monetization split between charging for Bits AI directly vs. its halo effect on platform usage — \"I'm not completely sure yet.\" Also refused to give per-customer contribution detail on the 9-figure AI mega-customer renewal (both current CRPO impact and forward quarterly contribution), citing policy against discussing individual contracts."
  contradictions: "The largest AI-native customer's contract expansion was framed as \"better economics\" for DDOG despite carrying a volume-based price discount — Pomel had to clarify this means near-term reported revenue can dip on renewal even as underlying consumption keeps growing, a redefinition worth flagging. Also notable: the non-AI acceleration is explicitly NOT GPU-driven, diverging from the hyperscaler narrative of AI-fueled cloud growth."
  street: "Analysts probed the durability and mechanics of the non-AI-native acceleration (sales capacity vs. demand environment vs. product maturity — asked at least four different ways), monetization of the AI-native cohort (GPU workloads, Bits AI packaging, the mega-customer's true economics), and margin/retention optics (why NRR isn't rising faster, gross margin trajectory). The underlying anxiety, never quite answered: is this quarter's re-acceleration durable secular strength or a temporary alignment of sales investment cycles, easy comps, and one enormous customer's renewal timing?"
---

# DDOG — fiscal 2025-Q3 call (2025-11-06)

**The key idea:** Datadog beat and re-accelerated on two fronts at once — a mega AI-native customer renewal plus, more surprisingly to management itself, the broadest non-AI enterprise/SMB re-acceleration in three years, explicitly not GPU-driven. The tension: how much of this is durable secular re-acceleration in cloud/digital transformation versus a temporary convergence of two-year-old sales-capacity investments finally clicking, easy prior-year comps, and one very large customer's renewal cadence.

## The read — 3-5 points from the whole transcript

1. **Non-AI growth accelerated broadly, and management can't fully explain why.** Ex-AI-native revenue growth accelerated to 20% y/y from 18% in Q2, and sequential usage growth for non-AI customers was "the highest we have seen going back 12 quarters." Asked directly what's driving it, Pomel gave a shrug-worthy answer: "I don't think there's a lot more to unpack there... it's also the way we've been growing for the past 15 years, really. So that's a — I would call it the usual." That's either quiet confidence or an admission they don't have a crisp causal story.

2. **AI-native concentration risk is real and getting bigger, not smaller.** A single AI-native customer secured a 9-figure annualized expansion with "better economics" (i.e., a price discount) for a higher commitment — CFO declined to disclose deal terms or forward contribution. Excluding that one customer, the broader AI-native cohort (500+ companies, 100+ over $100K ARR, 15+ over $1M) still accelerated, which is the more durable signal, but the single-customer dependency remains a disclosed but unquantified tail risk.

3. **Security is the most underrated growth line on this call.** Security ARR growth jumped to mid-50s% y/y from mid-40s last quarter, driven by Cloud SIEM wins bundled into large enterprise consolidation deals (one customer alone had 93 separate self-hosted open-source instances). Datadog is explicitly using its AI security agents to close 90% of investigation work automatically, which is becoming a wedge to win the SIEM replacement business outright.


5. **Sales-comp engineering, not new demand creation, is doing real work.** Pomel described deliberately restructuring comp plans and carving out multiyear incentive tracks specifically to fight the natural pull of land-and-expand toward easy existing-account dollars, redirecting reps toward harder-to-land new/smaller/Fortune-500 logos. New-logo bookings more than doubled y/y to a record — this is a go-to-market engineering story as much as a market-pull story.

## Economy & consumer

- **Demand environment described as positive but not accelerating on its own** — Pomel: "the demand environment is not... is positive in general. I don't know that we see massive acceleration of cloud migration, but at least the environment is not pushing the other way."
- **Growth was genuinely broad-based**, per CFO Obstler: "it's across the customer base, enterprise SMB... it also is across spending ranges. We're not seeing larger spenders or smaller spenders." SMB here means companies under 1,000 employees, explicitly not micro-business.
- **No direct end-consumer read** — DDOG sells to engineering/ops organizations, so this section functions as a B2B-demand proxy rather than a consumer signal.

## The business — what's working, what's not

- **Revenue beat guidance at $886M, +28% y/y**, with Q4 guide of 24% y/y growth (a deceleration baked into guidance, consistent with DDOG's stated conservative-guidance philosophy).
- **Platform depth is compounding**: customers using 8+ products rose to 16% from 12% a year ago; digital experience products (RUM, synthetics, product analytics) crossed $300M ARR with product analytics adopted by 1,000+ customers in a fast ramp.
- **Gross margin held flat-to-up at 81.2%**, credited to ongoing "cloud efficiency project" cost engineering — a working lever, not a one-time item, per CFO's multi-year framing of the 80% target band.
- **Net revenue retention stayed flat at 120%**, which CFO attributed to the metric's trailing-12-month lag rather than any underlying weakness — worth watching next quarter for whether it actually moves.
- **New-logo bookings more than doubled y/y to a record**, with new customers contributing 25% of y/y revenue growth, up from 20% in Q2 — an inflection in a business that has historically been dominated by expansion revenue.

## Investing & scarcity

- **Sales capacity expansion is the primary investment**, with OpEx growth decelerating to 32% y/y from 36% even as hiring continues — a sign of operating leverage kicking in alongside continued investment.
- **R&D dollars are concentrated on Bits AI agents** (SRE and security variants), LLM Observability (LLM spans sent to Datadog "more than quadrupled" in a few months), and MCP server integrations bridging Datadog into Codex, Claude, Cursor, GitHub Copilot, and Goose.
- **The actual constraint is sales-force attention allocation, not capital or compute.** Pomel was candid: "it is more work to get an extra dollar for a smaller customer or for a new one [than] from an existing one that they already have at scale" — hence the comp-plan re-engineering and multiyear carve-outs for harder Fortune 500 targets.
- **Capex/capitalized software guided at just 4% of revenue for FY2025** — Datadog is not itself a heavy AI-infrastructure capex story; it's a software layer riding on top of others' buildouts.

## Where they think it's going vs what they're doing about it

- **Belief: digital transformation and cloud migration remain a durable, multi-year secular driver.** Pomel: "we feel very confident about the motion in general for digital transformation and cloud migration is steady... we see that keep going on for a very long time."
- **Action backing that belief: continued sales-capacity scaling and product breadth investment**, which management credits for both the enterprise wins and the SMB reacceleration — a case where stated belief and actual spend are well aligned.
- **Belief: agentic AI will fundamentally change observability and incident response**, with Bits AI SRE catching root causes "3 minutes into the outage" versus 2 hours and 20 engineers manually. **Action: heavy multi-team R&D investment** into deepening remediation (not just detection) and broadening data-source training — genuine follow-through, not just messaging.
- **Gap worth flagging:** management is *not yet* committing meaningfully to GPU/AI-infrastructure monitoring as a product priority, despite repeatedly touting AI-native growth — the belief that "AI adoption... has grown faster than we thought" is not yet matched by disclosed GPU-specific product investment or revenue plan.

## Hedges — what they wouldn't commit to

- **Refused to quantify the AI mega-customer's forward revenue contribution or contract term** ("we don't provide that kind of information on individual customers"), despite three separate analyst attempts to triangulate it via CRPO math.
- **Declined to specify how Bits AI will be packaged/priced** — direct product monetization versus a platform-wide usage halo effect — Pomel: "I'm not completely sure yet."
- **No committed timeline or magnitude for GPU monitoring revenue** — flagged as a future opportunity with zero current contribution, an explicit non-commitment rather than a soft dodge.
- **Oracle/OCI/Stargate opportunity explicitly downplayed as "remote today"** given the highly custom nature of those AI training-cluster buildouts, versus optimism voiced for standard cloud integration demand.

## The street — what analysts asked

- **Durability of the non-AI reacceleration dominated the Q&A** — asked from at least four angles (sales capacity vs. demand backdrop vs. product maturity vs. holiday-calendar guidance risk), and management's answers converged on "a bit of everything," never isolating a single driver.
- **AI-native monetization mechanics were probed hard**: GPU workload revenue potential, the mega-customer's true economics under "better pricing," and whether independent AI/agentic vendors bundling their own observability threaten Datadog's wedge — Pomel's answer leaned on the platform-consolidation thesis (too many tools to manage separately) rather than a competitive rebuttal.
- **Sales execution and comp design got unusually detailed scrutiny** — quota attainment rates, comp-plan changes for 2026 — suggesting analysts see the go-to-market engine, not just product, as the marginal driver of the beat and want to know if it's repeatable.
- **Compressed worry: is Datadog's re-acceleration a durable inflection in enterprise digital transformation, or a favorable one-time alignment of sales-investment payoff timing, easy prior-year comps, and one whale customer's renewal — and how much of next year's growth quietly depends on that whale staying happy?**
