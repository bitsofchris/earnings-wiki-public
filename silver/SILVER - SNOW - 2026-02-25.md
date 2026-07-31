---
ticker: SNOW
call_date: 2026-02-25
report_quarter: 2026-Q1
period_reported: fiscal 2026-Q4
source: bronze/SNOW/2026-Q1/transcript-2026-02-25.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [SEAGATE, CAPITAL ONE, TOYOTA MOTOR EUROPE, UNITED RENTALS, EVOLV CONSULTING, SAP, EXPAND ENERGY, ANTHROPIC, INTERCOM, OPENAI, GOOGLE CLOUD, SANOFI, ELEMENTUM, OBSERVE]
answers:
  economy: "No macro commentary — consumption is described as resilient and predictable enough that Snowflake claims deviation of roughly 0.5% between forecast and actual, a level of confidence CFO Brian Robins calls near-total in guidance-setting."
  business: "Product revenue grew 30% y/y to $1.23B with RPO accelerating to 42% y/y growth for a second straight quarter; NRR held flat at 125%, and the company signed its largest deal ever (>$400M TCV, an existing customer) plus 7 nine-figure deals vs. 2 a year ago."
  investing: "Closed the ~$600M Observe acquisition (cash+stock) to push into the $50B observability/ITOps market, expanding from 'platform you analyze with' toward 'platform you build AI-native apps on' via Postgres, OpenFlow, Cortex Code; also committed $200M to an expanded OpenAI partnership for native model access."
  scarcity: "Constraint is less compute/capital and more headcount-per-output: Q4 included a ~200-person RIF and net adds of only 37 despite record bookings, with management explicit that 'AI has really changed the framework for investing in growth — it's no longer tied to headcount.'"
  forward: "Guiding FY27 product revenue to ~$5.66B (27% y/y, sustained rather than decelerating through the year), non-GAAP operating margin to 12.5% (up from 10.5%), with Observe adding ~1pt of growth and a ~150bp drag on free cash flow margin (guided 23%)."
  acting: "Building consumption guardrails (per-user caps on Snowflake Intelligence) ahead of scaled agent rollout to avoid 'sticker shock,' and redeploying AI-driven productivity gains (free-pool optimization, storage tiering, a services team running 5x faster) directly into margin rather than reinvesting in headcount."
  hedges: "Declined to attribute FY27 guidance upside specifically to AI/Cortex Code, repeatedly stressing the guide is built purely on 'existing patterns of consumption' and historical data — CEO Sridhar Ramaswamy admits 'there's no way that they can take into account the impact of Cortex Code because the historical data simply is not there,' effectively banking upside it isn't formally guiding to."
  contradictions: "Management frames itself as data-neutral on monetization ('slightly indifferent about whether we get more... revenue from running a query or from running the model') even while gross margin ticked down ~1pt this year specifically because new AI products carry lower margins than the core — an acknowledged trade-off management calls temporary but doesn't fully explain."
  street: "Analysts probed bookings sustainability (is the record RPO one-time or structural?), gross margin durability in the mid-70s as AI products scale, whether AI-lab-native stacks threaten the SaaS layer, and usage predictability — Snowflake gave confident, data-driven answers on predictability but was noticeably light on giving any hard AI-specific revenue or ARR figure when directly asked."
---

# SNOW — fiscal 2026-Q4 call (2026-02-25)

**The key idea:** Snowflake closed FY26 with re-accelerating bookings (record $400M+ deal, 42% RPO growth) and is pivoting its self-description from "data platform" to "control plane for the agentic era," anchored by Cortex Code (an AI coding/ops agent already used by 4,400 customers) and Snowflake Intelligence (2,500 accounts, nearly doubled quarter-over-quarter). The tension: management insists FY27 guidance is built purely on historical consumption data and explicitly excludes any credit for Cortex Code's impact — yet nearly every anecdote offered on the call is about Cortex Code's outsized internal and customer impact, suggesting real upside is being deliberately kept off the guided number.

## The read — 3-5 points from the whole transcript
1. **Bookings inflected sharply, and it's durable, not one-off.** RPO growth accelerated for a second consecutive quarter to 42% y/y ($9.77B), with the largest deal in company history (>$400M TCV, an existing financial-services customer) and 7 nine-figure deals versus 2 a year prior. CFO Brian Robins called this "really a buy-in from our customers on our product roadmap and AI strategy."
2. **AI is substituting for headcount, not just adding revenue.** Q4 saw a ~200-person reduction in force alongside net headcount adds of just 37, with Robins stating plainly: "AI has really changed the framework for investing in growth. It's no longer tied to headcount." Internal use cases (free-pool compute optimization, storage lifecycle policies, a 90-FTE-equivalent sales productivity gain) are cited as direct margin drivers, not efficiency theater.
3. **Cortex Code is described in almost breathless terms but deliberately excluded from guidance math.** Ramaswamy repeatedly says the model can't capture Cortex Code's impact because "the historical data simply is not there" — a partner quote ("we just gave them bulldozers") and a services team running "up to 5x faster" both point to real operating leverage that isn't in the guide. This is a explicit hedge-to-upside setup for FY27.
5. **Consumption pricing is being actively re-engineered to avoid enterprise sticker shock as agents scale.** Snowflake is adding per-user spend caps atop Snowflake Intelligence specifically to give budget owners predictability, explicitly contrasting itself with subscription-bundled agent competitors — an acknowledgment that unconstrained consumption pricing on agentic workloads is a real adoption risk, not a hypothetical.

## Economy & consumer
- **No macro or consumer commentary appears at all** — Snowflake is a B2B infrastructure layer and the call contains zero discussion of end-consumer demand or broader economic conditions; the only "demand" signal offered is enterprise data/AI consumption trends.
- **Forecasting is treated as a competency, not a market signal.** Ramaswamy claims "something like a 0.5% deviation is one part in 200" in consumption prediction accuracy, presented as evidence of platform maturity rather than commentary on the environment.

## The business — what's working, what's not
- **Core metrics are strong across the board:** product revenue +30% y/y to $1.23B, NRR steady at 125%, 740 net new customers (+40% y/y), 733 customers now over $1M trailing-12-month spend (+27% y/y), and a record 56 customers over $10M spend (+56% y/y).
- **Gross margin is quietly eroding as AI products scale.** FY26 non-GAAP product gross margin came in at 75.8%, described as down about a point for the year; CFO Robins conceded new AI products "aren't as high" margin as the core business and are being offset by core-business efficiencies rather than fixed outright — guided to 75% for FY27.
- **Stock-based compensation is being deliberately wound down**, from 41% of revenue in FY25 to 34% in FY26, guided to 27% in FY27 — a real dilution-discipline shift, not just an efficiency talking point.
- **Sales incentive structure reverted to rewarding bookings** (not just consumption) in FY26, which Ramaswamy frames as "business as usual" and a return to a two-year-old comp philosophy, likely contributing to the RPO acceleration.

## Investing & scarcity
- **Capital is flowing into agentic/AI infrastructure and observability, not core-warehouse capacity.** The $600M Observe deal, the $200M OpenAI partnership expansion, and continued Postgres/OpenFlow GA rollouts show investment shifting toward "build and run AI-native applications," per Ramaswamy's stated platform evolution.
- **The binding constraint is people-per-dollar-of-growth, and it's loosening via AI, not hiring.** Management explicitly decoupled growth from headcount this quarter (RIF + minimal net adds against record bookings), a scarcity story that inverts the usual "we need more engineers" framing seen elsewhere in tech.
- **$4.8B cash position and $1.1B remaining buyback authorization** (after $150M repurchased in Q4) signal no capital scarcity — the constraint is organizational leverage, not funding.

## Where they think it's going vs what they're doing about it
- **Stated belief:** Snowflake will become "the control plane for the agentic era," where enterprises need a single source of truth, governed metrics, and interoperability across model providers (OpenAI, Anthropic, Gemini all natively available).
- **Action behind it:** GA launches of Cortex Code CLI, Snowflake Postgres, and OpenFlow; the Observe acquisition; a $200M OpenAI commitment; and explicit multi-model neutrality ("we work with all of them") rather than betting on one lab.
- **Gap to flag:** Despite calling Cortex Code a "massive accelerant" and the "real game changer," guidance explicitly excludes its impact, and management declined to give any hard AI-specific ARR number when directly asked (Zukin's question on "Snowflake AI ARR" was answered with free-cash-flow commentary instead) — the enthusiasm in prepared remarks and Q&A anecdotes is meaningfully ahead of what's quantified in guidance or disclosed metrics.

## Hedges — what they wouldn't commit to
- **No AI-specific ARR or revenue figure was disclosed**, despite a direct analyst question about "Snowflake AI ARR" — the CFO pivoted to free cash flow margin mechanics instead.
- **Management repeatedly declined to attribute forward guidance strength to AI/Cortex Code specifically**, insisting the FY27 guide reflects only "existing patterns of consumption" — a deliberately conservative framing that preserves optionality to beat guidance on AI-driven upside later.
- **On gross margin trajectory, Robins would not commit to a stable long-term mid-70s range**, saying only that the sequence is "build great products, make it easy to use, then drive revenue, then optimize margins" — margin optimization is explicitly deferred, not promised.

## The street — what analysts asked
- **Durability of the reaccelerated guide.** Multiple analysts (Sanjit Singh, Alex Zukin) pushed on whether 27% growth is sustainable through FY27 or a sugar high off one quarter's mega-deals; answers leaned on "high stable core growth" plus AI contribution without much new specificity.
- **The nature and repeatability of the $400M+ mega-deal.** Analysts wanted to know if it signals a new class of bookings behavior; management confirmed it's an existing customer already in the run rate and pointed to comp-plan changes (bookings-weighted incentives) as a structural, repeatable driver rather than a one-off.
- **Competitive threat from AI labs disintermediating the SaaS stack.** Brent Thill's question about "SaaS names selling off on the big AI labs taking the stack" got a defensive answer centered on Snowflake's multi-model neutrality and governance moat rather than a direct rebuttal of the disintermediation risk.
- **Gross margin durability as AI products scale** — got a candid, unresolved answer (new AI products carry lower margins, offset elsewhere, no firm target given).
- **Compressed one-sentence worry:** analysts are effectively asking whether Snowflake's blockbuster bookings quarter and AI enthusiasm reflect a durable structural inflection or a guidance-conservative company sandbagging against one very large, non-repeatable enterprise deal — and management's refusal to quantify AI ARR leaves that question unresolved.
