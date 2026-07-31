---
ticker: DDOG
call_date: 2026-05-07
report_quarter: 2026-Q2
period_reported: fiscal 2026-Q1
source: bronze/DDOG/2026-Q2/transcript-2026-05-07.md
generated: 2026-07-30 (automated silver pass, schema v3)
mentions: [AWS, GRAVITON, TRAINIUM, GOOGLE, TPU, MICROSOFT, MAIA, CLAUDE CODE, CODEX, CURSOR]
answers:
  economy: "No visible macro drag: SMB strong, e-commerce/retail/travel 'similar to other industries,' no geopolitical or consumer-discretionary effect seen yet, though CFO says they 'watch it and look at analytics.'"
  business: "Revenue crossed $1B for the first time, growing 32% (accelerating from 29%, 25% prior quarters) with acceleration broad-based across AI-native and non-AI cohorts; non-AI revenue growth alone hit mid-20s%, record new-logo bookings more than doubled YoY, and gross retention held mid-to-high 90s."
  investing: "Heavy R&D and go-to-market capacity investment (OpEx +31% YoY) funding platform breadth (26 products, 18 still sub-$100M ARR) and new AI products (GPU Monitoring, Bits AI Security Analyst, MCP Server GA); CapEx stays deliberately low since nearly all workloads run on public cloud, not owned infrastructure."
  scarcity: "Sales capacity and engineering headcount to keep building/selling 18 immature products, plus certification/geographic build-out (UK datacenter, FedRAMP High) — not compute or capital, which they explicitly said isn't constrained."
  forward: "Management believes training workloads are 'turning into production' and could democratize beyond the handful of labs that do it today, becoming a durable new demand category alongside inference; they also expect AI agent usage and human console usage to keep growing side by side, not substitute."
  acting: "Landed 7-and-8-figure deals with two frontier AI labs' training divisions, shipped GPU Monitoring and MCP Server GA, is investing 'heavily' in Bring Your Own Cloud / CloudPrem for data-residency-sensitive workloads, and is expanding FedRAMP High certifications and channel partnerships ahead of actual federal bookings."
  hedges: "Declined to call training a proven, durable revenue line yet ('too early... to call definitive victory'), applied deliberately higher guidance conservatism specifically to their largest customer, and wouldn't speculate on where agent-vs-human usage settles in four to five years."
  contradictions: "Argues hyperscalers — who have unlimited staffing and a build-it-themselves culture — are nonetheless coming to Datadog for AI/training workloads because 'the equation... has often been slightly different' under AI-race urgency; a notable reversal from a year ago when management said training 'is not really a market for us yet.'"
  street: "Analysts probed whether code-gen tools are inflating production complexity/telemetry volume, whether heterogeneous AI silicon (Trainium, TPU, Maia) is a tailwind, why capital intensity stays low despite telemetry growth, and pressed twice on the specific wording of 'higher conservatism' applied to the largest customer — a proxy for concentration-risk anxiety the company kept batting down."
---

# DDOG — fiscal 2026-Q1 call (2026-05-07)

**The key idea:** Datadog crossed $1B in quarterly revenue for the first time and reported accelerating growth in *both* its AI-native and non-AI cohorts — the more interesting story is the pivot from "training isn't our market" a year ago to landing two frontier-lab training deals and hyperscaler customers now, even though management is careful not to declare training a durable revenue category yet.

## The read — 3-5 points from the whole transcript
1. **Growth accelerated everywhere, not just in AI.** Revenue grew 32% YoY (up from 29%, up from 25% a year ago), and non-AI customer revenue growth alone accelerated to mid-20s% from 23% and 19% — Olivier Pomel frames this as "strong continued cloud migration" plus AI adoption spreading into the broader base, not an AI-only story.
2. **Training is now a real market for Datadog — a stated reversal.** "Last year when we reported earnings, we said we're mostly interested in inference workloads and training is not really a market for us yet. Now we actually see training becoming a market," Pomel said, citing two new land deals with "the world's biggest AI research teams" in Q1.
3. **Even hyperscalers with unlimited engineering capacity are buying, not building.** Pomel's explanation was urgency, not capability: "the equation for hyperscalers has often been slightly different because they have... unlimited access to staffings... I think the situation is a little bit different with AI race maybe" — a tacit admission that AI-race pressure is overriding their normal build-vs-buy calculus.
4. **CapEx stays deliberately thin despite exploding telemetry.** MCP Server tool calls quadrupled quarter-over-quarter, LLM Observability spans nearly tripled, Bits Assistant messages rose 12x — yet CapEx/capitalized software guided to just 4-5% of revenue for the year, because "we run most of our workloads on clouds, meaning you'll see all of that in OpEx, not in CapEx."
5. **Concentration risk lingers under the surface.** CFO David Obstler again flagged "a higher degree of conservatism" applied specifically to their largest customer in guidance — the same language as last quarter — and an analyst pressed twice to confirm nothing had changed methodologically, suggesting the Street is still nervous about single-customer dependence even amid record broad-based ARR adds.

## Economy & consumer
- **No macro drag detected yet.** Asked directly about geopolitical tensions and consumer-discretionary risk in SMB/e-commerce/retail, Obstler said: "We haven't seen any particular effect in the consumer businesses or e-commerce businesses yet... travels and things like that are very similar to... the other industries."
- **SMB was a standout, not a weak spot.** Obstler called out SMB as "very strong" within an otherwise "multi-industry, multi-geography type of quarter."

## The business — what's working, what's not
- **First $1B revenue quarter, on a record sequential add.** Revenue hit $1.01B, up 32% YoY, with the highest Q1 sequential revenue growth since 2022 and "the highest ever" absolute Q1 dollar add.
- **New logo bookings more than doubled YoY** and set an all-time record, including wins in newer products like security, Data Observability, and Flex Logs — platform breadth is translating into bigger initial lands, not just expansion.
- **Product depth keeps deepening within the base.** Customers using 6+ products rose to 35% (from 28% a year ago) and 8+ products to 20% (from 13%) — but of 26 total products, only 5 exceed $100M ARR and 18 remain early-stage, meaning most of the platform bet is still unproven at scale.
- **Gross margin drifted down sequentially** (80.2% vs 81.4% prior quarter) as innovation investment outpaced efficiency gains — flagged as normal quarter-to-quarter variability, not a trend.

## Investing & scarcity
- **Investment is going into people and product breadth, not infrastructure.** OpEx grew 31% YoY (vs 29% prior quarters), explicitly tied to hiring plan execution; CapEx stays capped at 4-5% of revenue because the company runs on public cloud rather than owned GPU/datacenter infrastructure.
- **Certification and geographic build-out is the visible constraint.** UK datacenter launch and FedRAMP High certification required investing "ahead of the certifications because... in this sector, building pipeline... takes time," per Obstler — public-sector revenue is gated by sales/channel readiness, not product readiness.
- **CloudPrem (Bring Your Own Cloud) is a hedge against a structural shift**, letting Datadog run inside customer environments for data-residency-sensitive workloads — Pomel called it a potential path into "extremely large scale workloads where customers would not have considered a SaaS offering before."

## Where they think it's going vs what they're doing about it
- **Belief:** training could "democratize quite a bit more" beyond the 2-5 companies doing it at scale today, becoming a recurring category like inference. **Action:** landed two frontier-lab training deals and shipped GPU Monitoring for GPU fleet utilization/thermal/interconnect visibility — but Obstler explicitly declined to size the attach rate, calling it "early days for the training... I would sort of look at the larger attachment at this point as the evidence of inference but also some training." The belief is running ahead of the proof.
- **Belief:** agent-driven usage (MCP Server, Bits AI SRE, Bits Assistant) will keep scaling alongside human usage. **Action:** usage-based pricing model is left unchanged deliberately — "we don't care whether most of the usage is humans, most of the usage is agents... it doesn't really matter where the usage is coming from" — no new agent-specific pricing tier is being built despite Bits Assistant messages growing 12x quarter-over-quarter.
- **Belief:** heterogeneous AI silicon (Trainium, TPUs, Maia) increases the need for a third-party unifier. **Action:** GPU Monitoring product built and already landing with hyperscalers, though Pomel conceded the pool of companies actually running heterogeneous fleets today "is still a very small number."

## Hedges — what they wouldn't commit to
- **No definitive claim on training as a durable revenue line yet:** "It's too early in the product life cycle and the customer life cycle for these specific customers to call definitive victory there."
- **Extra guidance conservatism reserved for the single largest customer**, applied identically to last quarter's methodology — management repeatedly stressed no change, seemingly trying to defuse concentration-risk speculation rather than resolve it.
- **No prediction on agent-vs-human usage mix in the long run:** "it's hard to tell where we're gonna be in four or five years... if you had told me two years ago that most engineers would go back to coding in the console, I would not believe you."
- **No CapEx model change disclosed even hypothetically committed to:** "If it changes, we'll tell you" — twice repeated, functioning as a placeholder rather than a forecast.

## The street — what analysts asked
- **Telemetry-volume-from-code-gen and silicon-heterogeneity tailwinds** dominated the early questions — analysts wanted confirmation that AI coding tools (Claude Code, Codex, Cursor) are driving real production complexity Datadog can monetize, and Pomel confirmed "a move to production that is very real."
- **Capital intensity and margin durability** came up directly — an analyst pushed on whether exploding telemetry volume would eventually force more CapEx or compress gross margins; the company held the line that it's an OpEx, cloud-native cost structure.
- **Concentration risk via the largest-customer conservatism language** was asked about twice in different forms — the underlying anxiety is that a large chunk of the ARR beat is customer-concentrated and could reverse or plateau.
- **Hyperscaler build-vs-buy logic** got pressed hard — why would companies with "unlimited access to staffing" outsource observability to Datadog — and Pomel's answer (AI-race urgency overriding normal build economics) was more candid than a fully confident answer would need to be, worth flagging as a soft spot in the thesis.
- Compressed worry: **is the acceleration durable and broad, or is it one or two whale customers and a training narrative still too young to underwrite?**
