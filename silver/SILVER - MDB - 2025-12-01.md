---
ticker: MDB
call_date: 2025-12-01
report_quarter: 2025-Q4
period_reported: fiscal 2026-Q3
source: bronze/MDB/2025-Q4/transcript-2025-12-01.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [POSTGRES, ELASTICSEARCH, REDIS, VOYAGE AI, MERCOR, AWS, HUGGING FACE]
answers:
  economy: "No macro commentary — the call is entirely company- and workload-specific; enterprise modernization spend appears undisturbed by any broader demand caution."
  business: "Atlas revenue accelerated to 30% YoY (from 29% Q2, 26% Q1) on 75% of revenue; total revenue $628.3M beat guide; non-GAAP operating margin hit 20% vs 19% a year ago; net ARR expansion rose to 120%. Non-Atlas grew ARR only 8%, with two-thirds of its guide-beat coming from multiyear deal timing, not underlying demand."
  investing: "New CEO CJ Desai (28 days in) is redirecting go-to-market energy toward Fortune 500/Global 2000 penetration and Silicon Valley AI-native accounts, leveraging his personal network in both; sales-capacity and engineering investment that was planned for FY26 slipped into Q4 and FY27."
  scarcity: "Not compute or capital — it's proof: CFO Berry says non-Atlas multiyear pipeline requires 'very clear visibility' before being included in guidance, and Desai repeatedly says enterprises have pilots and '10, 15, 20' agents but almost none in true production, meaning the binding constraint is enterprise trust/governance, not technology capability."
  forward: "Management guided Atlas to ~27% Q4 growth (up from a prior mid-20s expectation) and non-Atlas to upper-single-digit growth, while flagging historically 'unpredictable' holiday seasonality as a reason for caution; FY27 non-Atlas is expected to land in low-single-digit growth once multiyear pull-forward normalizes."
  acting: "CEO transition just executed (Ittycheria to board, Desai now CEO); MongoDB is relaunching its .local developer conference in San Francisco Jan 15 and continuing the 'Reclaim the Bay' investment in AI-native startups/VCs; sales capacity hires pushed into Q4/FY27 rather than cut."
  hedges: "CFO explicitly declined to give FY27 guidance ('we will guide '27 on the next call'), repeatedly stressed 'prudent' Q4 forecasting given seasonal unpredictability, and would not commit to whether new-customer Atlas revenue ramp speed is materially changing ('hasn't changed materially... pretty small number')."
  contradictions: "Desai insists core-business strength is happening 'before any AI tailwinds' have hit, yet in the same breath argues AI modernization pressure and core-platform agility are 'not mutually exclusive' and that sluggish core teams frustrate AI teams — effectively conceding the two are already intertwined, undercutting the clean before/after framing."
  street: "Analysts probed (1) how the brand-new CEO's strategy will differ operationally, (2) whether newly precise Atlas guidance reflects real predictability or just a new CFO's transparency preference, (3) FY27 margin trajectory given op margin still ~200bps below the long-term model, and (4) whether new-customer ramp speed is actually accelerating. Management gave process answers (transparency, prudence) rather than hard commitments on any forward number, and deferred all FY27 specifics to the next call."
---

# MDB — fiscal 2026-Q3 call (2025-12-01)

**The key idea:** MongoDB delivered its third straight quarter of Atlas acceleration (30% YoY) and margin outperformance under a brand-new CEO, CJ Desai, just 28 days into the job — with the entire call built around convincing investors that this strength is durable core-business execution, not an AI mirage, even while management's own commentary shows the two are already blurring together. The real story underneath the beat is a company mid-transition: leadership handoff, guidance-philosophy overhaul, and a non-Atlas segment whose growth is increasingly a multiyear-deal-timing artifact rather than organic demand.

## The read — 3-5 points from the whole transcript
1. **Atlas is genuinely accelerating, non-Atlas is not.** Atlas grew 30% YoY (up from 29%, 26% the two prior quarters) and now carries 75% of revenue, but non-Atlas ARR — the cleaner measure — grew just 8%, and CFO Berry admitted "approximately 2/3 of the non-Atlas revenue outperformance versus the high end of guidance was attributable to multiyear outperformance," not new demand.
2. **New CEO frames the opportunity as "once in a lifetime" but the evidence he cites is still anecdotal.** Desai's specifics — one AI-native company migrating off Postgres, one enterprise starting with Voyage embeddings — read as promising vignettes from 28 days of customer calls, not a demand inflection visible in the numbers yet.
3. **Enterprise AI remains stuck in pilot purgatory.** Desai's own words are the clearest data point on the call: "what I have not seen is truly AI agents running in production that fundamentally transform the business or serve customers better... they may have 10, 15, 20, but not that many compared to thousands of applications they run."
4. **Guidance philosophy just changed, and management was candid about why.** CFO Berry now gives explicit quarterly Atlas growth guidance (27% for Q4) instead of vaguer ranges, attributing it to both a desire for transparency from new leadership and Atlas's scale (nearly $2B) making it more forecastable — a genuine process improvement worth tracking for consistency next quarter.
5. **Margin expansion this year is a timing gift, not a structural win.** Op margin beat guidance because "planned investments have taken longer to implement than expected and have shifted into the fourth quarter... and fiscal '27" — meaning FY26's margin outperformance borrows against FY27 opex.

## Economy & consumer
No macro or consumer-demand commentary appears anywhere in the call — MongoDB is an infrastructure layer once removed from end consumers, and management's entire frame is enterprise IT modernization budgets, which show no sign of pulling back.

## The business — what's working, what's not
- **Atlas outperformance is broad and structural.** 30% YoY growth was "driven by continued strength with our largest customers in the U.S. and broad-based strength in EMEA," from both new workloads and expansion of existing ones, and total net ARR expansion rose to 120% from 119%.
- **Customer-add momentum is real but skews small.** MongoDB added 2,600 customers in the quarter (65% YoY growth in additions), driven by self-serve — but CFO Berry noted new-customer revenue "hasn't changed materially... it's still, keep in mind, a pretty small number when they first onboard."
- **Gross margin is eroding as the mix shifts.** Gross margin fell to 74% from 77% a year ago "primarily driven by Atlas growing as a percent of the overall business," since Atlas carries a lower gross margin than non-Atlas even as it improves YoY.
- **Non-Atlas is a legacy book being managed for orderly decline into low-single-digit growth**, per CFO Berry's own FY27 framing — "somewhere in that mid kind of low single digits is probably a good range to think about for next year."

## Investing & scarcity
- **The scarce resource is enterprise production-readiness, not technology.** Desai: "in regulated industries... the requirement for an AI agent to be in production versus prototype are vastly different, and they are looking for governance, auditability... The churn for some of these AI companies that deliver these tools is also very real."
- **Sales and engineering capacity investment slipped a quarter**, benefiting FY26 margins opportunistically rather than by design — a real signal that the org couldn't hire/build as fast as planned.
- **Capital allocation stayed conventional**: $145M spent on buybacks this quarter under a $1B authorization, plus a shift to cash-settling RSU taxes instead of issuing shares — capital discipline moves, not AI infrastructure land-grab spending (notably, no GPU/compute capex commentary at all, consistent with MongoDB's software-only, cloud-hosted model).

## Where they think it's going vs what they're doing about it
- **Believes**: AI agents at enterprise scale are coming and will need real-time operational data plus retrieval — "MongoDB has the potential to become the generational modern data platform of this evolving era."
- **Doing**: Relaunching the .local developer conference in San Francisco (Jan 15) and continuing "Reclaim the Bay" investment in the AI-native startup/VC ecosystem — concrete but modest, marketing-and-mindshare-scale actions, not R&D or headcount commitments sized to match the "generational" rhetoric.
- **Gap**: the acquisition that actually matters for the AI thesis, Voyage AI, closed under the prior CEO in February; nothing announced this quarter represents new capital committed specifically to the AI opportunity beyond conference/marketing spend and Desai's personal network-building.

## Hedges — what they wouldn't commit to
- **FY27 guidance flatly deferred**: "we will guide '27 on the next call" — repeated verbatim when pressed twice on margin trajectory and non-Atlas trends.
- **Q4 Atlas guidance framed defensively**: despite giving a specific 27% number, Berry stressed being "prudent" multiple times given "seasonal holiday patterns that can be somewhat unpredictable... we've seen that play out in the past Q4s" — setting up room to underdeliver against the headline number.
- **Would not attribute core strength to AI or separate it from AI**, calling the relationship "possible but not deterministic" when asked directly — a carefully hedged non-answer to a direct causal question.

## The street — what analysts asked
Analyst questions clustered almost entirely around the CEO transition: what a 28-day-old CEO's early read reveals, whether new granular Atlas guidance signals real predictability or just a stylistic change, and whether FY27 margin expansion is credible given the current 200bp gap to the long-term model. A secondary thread pushed on new-customer ramp speed and the durability of non-Atlas post-multiyear-headwind. Management answered nearly every forward-looking question with a variant of "we'll guide that next quarter" or "we're being prudent" — the compressed worry: is this quarter's beat a real inflection or a soft-landing quarter dressed up by a new CEO's honeymoon narrative and a CFO's favorable expense-timing luck.
