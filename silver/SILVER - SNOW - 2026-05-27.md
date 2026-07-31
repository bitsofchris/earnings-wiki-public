---
ticker: SNOW
call_date: 2026-05-27
report_quarter: 2026-Q2
period_reported: fiscal 2027-Q1
source: bronze/SNOW/2026-Q2/transcript-2026-05-27.md
generated: 2026-07-30 (automated silver pass, schema v3)
mentions: [AWS, OPENAI, ANTHROPIC, DATABRICKS, SAP, NATOMA, OBSERVE, TERADATA, NESTLE, THOMSON REUTERS, PROVIDENCE, DTCC, GLOBAL PAYMENTS, BLUE YONDER, HOLIDAY INN CLUB VACATIONS, HOUZZ, MISTRAL]
answers:
  economy: "No macro commentary beyond an AI-adoption tailwind; management frames urgency to migrate to cloud/Snowflake as accelerating rather than any demand softness."
  business: "Product revenue growth accelerated to 34% YoY (from 30%, from 26% a year ago) — 'strongest sequential dollar growth in company history' — with NRR up to 126% and non-GAAP operating margin up 300bps to 12%; net new customers up 38% YoY and use-cases-won-per-AE up 86% YoY."
  investing: "Signed a $6B five-year AWS agreement (more than doubling the FY2023 deal) and a $200M OpenAI partnership; announced intent to acquire Natoma to extend the agentic control plane into SaaS actions (email, Slack, Jira); hiring stayed disciplined — 190 net adds, but 173 came from the Observe acquisition, leaving only 17 organic hires."
  scarcity: "AI/agent cost governance is the binding constraint as usage scales — CFO Brian Robins confirmed Cortex Code carries lower gross margin than core, offset by AWS bandwidth savings; engineering headcount is being deliberately throttled (17 organic hires) in favor of AI-driven productivity."
  forward: "Raised FY2027 product revenue growth guidance from 27% to 31% and full-year operating margin from 12.5% to 13.5%, citing 'a step function change in our AI revenue opportunity, led by Cortex Code.'"
  acting: "Extending Snowflake Intelligence/Cortex Code (CoCo) into an 'agentic control plane' via the Natoma acquisition, building account/agent-level token cost controls, and routing internal support/SRE/services work through CoCo (25%+ faster case resolution, ~40% less engineering time per ticket)."
  hedges: "CFO repeatedly stressed guidance methodology is unchanged — 'we only forecast observed behavior' — meaning the raise reflects one quarter of CoCo data, not a forward bet on continued acceleration; declined to give specifics on per-customer CoCo revenue uplift beyond qualitative examples."
  contradictions: "Management frames a lower-margin AI product line (Cortex Code) as gross-margin-neutral to the full-year 75% guide only via an offsetting AWS bandwidth-cost deal — a favorable vendor deal propping up a metric that would otherwise show AI-driven margin dilution."
  street: "Analysts converged almost entirely on Cortex Code: what's driving the guidance inflection, whether usage-based AI pricing risks customer throttling, gross-margin drag from AI products, and whether CoCo changes the competitive moat against hyperscalers/Databricks. One analyst asked directly why sales & marketing hiring wasn't scaling with demand — management's answer leaned on AI-driven productivity rather than committing to more S&M headcount."
---

# SNOW — fiscal 2027-Q1 call (2026-05-27)

**The key idea:** A single quarter of Cortex Code (CoCo) — Snowflake's coding/agent product that only went GA February 5 — was enough data for management to raise full-year growth guidance from 27% to 31% and operating margin from 12.5% to 13.5%. The bet is a flywheel: AI products drive more core-platform consumption, core consumption funds the AI investment, and a new $6B AWS deal plus a Natoma acquisition extend the platform from data into SaaS "actions." The tension: guidance philosophy is explicitly built on one quarter of observed behavior for a product still in its infancy, and the AI product line is conceded to run at lower gross margin, papered over by a vendor bandwidth deal.

## The read — 3-5 points from the whole transcript
1. **An unusually clean beat-and-raise, attributed almost entirely to one new product.** Product revenue growth accelerated ~400bps sequentially to 34% YoY, the "strongest sequential dollar growth in company history," and CFO Brian Robins said plainly: "CoCo had the largest driver to the increase in our forecast."
3. **Natoma acquisition is a governance play as much as a feature play.** Extending CoCo/Snowflake Intelligence into Slack, email, Jira and calendar actions is framed less as convenience and more as "control" — governed, audited agent actions across SaaS, explicitly positioned as a moat against looser competitors.
4. **Margin math on AI is being managed, not solved.** CFO conceded Cortex Code runs at lower gross margin than the core platform but held the 75% full-year product gross margin guide by citing "lower bandwidth costs" from the new AWS contract — an accounting offset from a vendor deal, not underlying AI-product economics improving.
5. **Renewal timing risk building toward Q4.** RPO grew 38% YoY, but management flagged that customers increasingly favor Q4 renewals, meaning bookings — and the read-through to future growth — will be more concentrated and less visible earlier in the year.

## Economy & consumer
No discrete macro or consumer commentary; SNOW is enterprise infrastructure and doesn't touch a consumer directly. The only environmental read is customers moving to cloud/Snowflake "with increasing urgency" under an AI-first mindset — read as tailwind, not caution.

## The business — what's working, what's not
- **Core platform reaccelerating alongside AI, not despite it:** product revenue growth of 34% YoY, NRR up to 126%, 64 customers now over $10M TTM revenue (8 crossed the threshold this quarter), 79 customers over $1M TTM.
- **Customer land-grab accelerating:** 616 net new customers (+38% YoY), 13 new Global 2000 logos vs. 4 a year ago — "the most net new customer adds that we had in company history" per Robins.
- **What's not emphasized:** no update on churn, downsell, or any customer segment showing weakness — the note is one-sided toward strength, which is itself worth flagging as an omission for a bull-case-heavy call.

## Investing & scarcity
- **$6B AWS deal, more than doubling the FY2023 contract**, explicitly built into guidance; **$200M OpenAI partnership** and existing Anthropic model access underpin a stated "model choice" strategy rather than single-vendor dependence.
- **Natoma acquisition** (20 employees) extends the control plane into third-party SaaS actions with built-in governance/audit — CEO Sridhar Ramaswamy: "The important point is not just convenience, it is control."
- **Binding constraint is agent/token cost governance at scale**, not compute or talent: Ramaswamy described building "cost limits at an account level, or at a particular agent level" as usage scales toward 10,000-user rollouts, with model-tiering (small models like Mistral for simple tasks, frontier models reserved for complex ones) as the mechanism to keep economics sane.

## Where they think it's going vs what they're doing about it
- **Belief:** AI compounds Snowflake's core data advantage rather than disintermediating it — "AI is compounding Snowflake's advantage in data."
- **Action backing it:** Guidance raised on a single quarter of CoCo data; Natoma acquisition signed same-day as the call to broaden the control plane; internal teams (support, SRE, services) pushed to 95%+ CoCo adoption as proof-of-concept before further external rollout.
- **Gap:** The guidance raise is explicitly a one-quarter extrapolation ("we didn't have any observed behavior for guidance for CoCo" until now) — a materially thinner data basis than the size of the raise (27%→31% full-year) might suggest to investors expecting steady-state visibility.

## Hedges — what they wouldn't commit to
- CFO repeatedly anchored expectations to "no change in guidance philosophy" and reiterated a 3% beat is "a really strong beat" — deliberately tempering expectations that this quarter's magnitude of beat becomes the new normal.
- No specific dollar or percentage disclosure of CoCo's standalone revenue contribution or per-customer spend uplift — only qualitative anecdotes (Infinite Lambda, Providence, Thomson Reuters).
- Declined to commit to accelerating S&M hiring despite record customer adds, instead attributing go-to-market strength to AI-driven productivity gains from the existing team.

## The street — what analysts asked
Nearly every question centered on Cortex Code: what specifically inflected this quarter, whether usage-based AI pricing invites customer throttling, whether CoCo drags gross margin, and how the Natoma acquisition and coding-agent economics reshape the competitive landscape against hyperscalers and Databricks. One question pressed on why sales & marketing headcount hadn't scaled with demand, getting an AI-productivity answer rather than a commitment to add reps. The underlying anxiety, compressed: is this quarter's AI-driven beat a durable new growth rate, or a one-time step-change being guided off a single data point?
