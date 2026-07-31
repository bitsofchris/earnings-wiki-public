---
ticker: SNOW
call_date: 2025-12-03
report_quarter: 2025-Q4
period_reported: fiscal 2026-Q3
source: bronze/SNOW/2025-Q4/transcript-2025-12-03.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [ANTHROPIC, AWS, SAP, WORKDAY, SALESFORCE, SERVICENOW, ACCENTURE, PALANTIR, SPLUNK, UIPATH, MORGAN STANLEY, PAYPAL, CATERPILLAR, ASTRAZENECA, FANATICS, EVGO, COCA-COLA CONSOLIDATED, GOLDMAN SACHS]
answers:
  economy: "No macro commentary — the call frames demand entirely through enterprise AI/data migration adoption, not broader economic conditions."
  business: "Product revenue up 29% YoY to $1.16B, RPO growth accelerated to 37% ($7.88B), NRR steady at 125%, and a record 615 new customers and four nine-figure deals signed — CFO explicitly downplays the quarterly beat ('only a 2.5% beat') and points to the raised full-year guide as the real signal."
  investing: "Committed $200M as a buy-side spend with Anthropic for model access plus a joint go-to-market motion, alongside tuck-in acquisitions (Datometry, SelectStar) aimed at accelerating legacy migrations and enriching data-catalog context for agentic AI."
  scarcity: "The binding constraint is customer trust/readiness to expose data to AI agents (governance, eval, reliability) rather than compute or headcount — Snowflake positions its data-structuring and eval tooling as solving exactly that bottleneck."
  forward: "Management believes migrations are still 'super early' (citing AWS's own estimate of 15-20% through on-prem migration) and that AI will accelerate both migration pace and Snowflake Intelligence adoption further into FY27."
  acting: "Rolling out coding agents internally, hiring a new CFO (Brian Robbins) explicitly to bring 'discipline' to scaling, and building AI-ready data/agent tooling (OpenFlow, Postgres via Crunchy Data acquisition) rather than just messaging AI readiness."
  hedges: "Declined to guide FY27 or quantify AI revenue growth rate ('we don't really want to guide to it'), and CFO repeatedly warns not to extrapolate from single-quarter beats given the consumption model's lumpiness."
  contradictions: "CFO calls the 4Q operating-margin dip 'nothing to read into,' while simultaneously conceding FY26 margin was intentionally front-loaded — a soft admission that margin trajectory was managed, not organic, even as they reiterate full-year margin targets."
  street: "Analysts pressed repeatedly, in different phrasings, on whether the outsized beat/raise is sustainable core growth or a one-off lumpy-migration effect (echoing last quarter's large-deal timing question) — management's answer stayed consistent: 'look at the full-year guide, not the quarterly beat,' without fully resolving the sustainability question."
---

# SNOW — fiscal 2026-Q3 call (2025-12-03)

**The key idea:** Snowflake hit $100M in AI revenue run-rate a quarter early and used it to justify a raised full-year guide, but nearly every analyst question circled the same tension: is this durable AI-and-migration-driven growth, or a repeat of last quarter's lumpy large-deal timing dressed up in new AI language? Management's answer was consistent and slightly evasive — "look at the annual guide, not the quarterly beat" — which is itself a tell about how much confidence they have in quarter-to-quarter predictability.

## The read — 3-5 points from the whole transcript
1. **AI adoption is real but still "helping hand," not primary driver.** AI influenced roughly 50% of new bookings and 28% of use cases deployed, but CEO Sridhar Ramaswamy is careful to frame it as "a helping hand. It's not the dominant thing" — a more measured claim than the marketing framing around the call implies.
2. **The beat-and-raise pattern is now explicitly managed messaging.** CFO Brian Robbins, in his first quarter, repeatedly steered analysts away from quarterly variance toward the annual guide, and CEO Ramaswamy stated the company calibrates itself to "view a 3% beat as a very good beat" — an admission that guidance is deliberately sandbagged and beats are a managed output, not a surprise.
3. **Large-deal timing continues to muddy the growth signal.** Four nine-figure deals closed this quarter (up from prior records), yet Ramaswamy noted such deals are "slightly negative with respect to revenue" near signing due to discounting — meaning bookings strength and near-term revenue recognition can diverge, which is exactly the ambiguity analysts kept probing.
4. **Migration is framed as "super early" — a genuine long runway if true.** Citing AWS's Matt Garman, management pegs on-prem legacy migration at just 15-20% complete, positioning Snowflake's multi-year growth case on that runway rather than on the current AI narrative.
5. **New CFO's first-sixty-days remarks lean heavily on reassurance.** Robbins spent unusual airtime praising the finance team's "depth of bench" and pledging no change to guidance philosophy — signaling the market's underlying anxiety was less about growth and more about whether a CFO transition changes forecasting discipline.

## Economy & consumer
No discussion of macro conditions or end consumers — Snowflake's customers are enterprises, and this call stayed entirely within enterprise IT/data-migration and AI-adoption framing.

## The business — what's working, what's not
- **Working:** Product revenue +29% YoY, RPO growth accelerated to 37%, NRR flat but healthy at 125%, and a record 615 new logos — broad-based strength across acquisition and retention.
- **Working:** Snowflake Intelligence (GA'd this quarter) called "the fastest ramp in product adoption in our company history," already at 1,200 customers.
- **Not working / friction:** A hyperscaler outage this quarter cost an estimated $1-2M in revenue — a reminder that Snowflake's business still depends on third-party cloud infrastructure reliability, even as it markets its own disaster-recovery capability (300+ workloads failed over) as a selling point.
- **Not working / soft spot:** Non-GAAP operating margin guide for Q4 (7%) stepped down from Q3's 11%, which CFO dismissed as an artifact of "front-loading" the year rather than deteriorating unit economics — plausible, but unverified by any breakdown.

## Investing & scarcity
- **$200M committed to Anthropic** as a buy-side model spend plus a joint go-to-market motion — a direct financial bet that native access to leading third-party models drives Cortex/Snowflake Intelligence consumption.
- **Tuck-in M&A aimed squarely at migration and catalog depth:** Datometry (legacy warehouse migration tooling) and SelectStar (Horizon catalog enrichment) — both framed as removing friction for customers moving onto Snowflake and for agentic AI to "understand" enterprise data.
- **Crunchy Data-driven Postgres support** still a couple months from GA — an admission this OLTP push, positioned as essential "for agentic solutions that need an OLTP store," is not yet shipped.
- **The real constraint is trust and readiness, not infrastructure:** Ramaswamy describes customers who tried to "string together agentic systems" themselves and failed, positioning Snowflake's governance/eval tooling as the actual bottleneck-breaker — a scarcity of reliable agent infrastructure, not compute.

## Where they think it's going vs what they're doing about it
- **Belief:** Migrations are only 15-20% complete industry-wide, implying years of runway. **Action:** acquiring migration-acceleration tech (Datometry) and using AI/coding agents internally to speed migrations — money and product behind the belief, a real gap-closer.
- **Belief:** Every dataset in Snowflake should eventually be "AI-ready" and shareable as an agent, not a raw dataset. **Action:** SelectStar acquisition for catalog context, but this is still an early-stage integration, not yet a shipped capability at scale — the belief runs ahead of the build.
- **Belief:** AI revenue growth will "continue to grow quite well." **Action:** No rate or milestone commitment given — the stated confidence isn't backed by any quantified target, a soft spot between rhetoric and commitment.

## Hedges — what they wouldn't commit to
- **Refused to guide FY27** even directionally, deferring entirely to the next earnings call and citing post-holiday consumption data as the needed input.
- **Declined to quantify AI revenue growth rate,** despite volunteering the $100M run-rate milestone unprompted — cherry-picking the flattering absolute number while withholding the trend.
- **CFO deflected the Q4 margin-guide question** ("don't read too much into that... nothing intended") without giving a substantive driver beyond "Q4 guide and annual guide happen together" — a non-answer to a direct question about sequential margin compression.

## The street — what analysts asked
Q&A repeatedly circled one anxiety from multiple angles: is the growth acceleration organic and durable, or an artifact of lumpy, hard-to-predict large-deal and migration timing? Analysts pushed on the gap between the "best sequential guide in years" and a below-average beat, on whether Q3's four nine-figure deals were pulled-forward from Q2's unusually strong migration quarter, and on how the $100M AI milestone breaks down by product. Management's answers consistently redirected toward the full-year guide as the only meaningful signal and declined to give granular attribution — leaving the underlying question only partially resolved: **is Snowflake's growth engine now AI-and-migration-durable, or still fundamentally lumpy and hard to forecast quarter to quarter?**
