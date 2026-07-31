---
ticker: SMCI
call_date: 2025-11-04
report_quarter: 2025-Q4
period_reported: fiscal 2026-Q1
source: bronze/SMCI/2025-Q4/transcript-2025-11-04.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [NVIDIA, AMD, XAI, DCBBS]
answers:
  economy: "No macro commentary — the call is entirely about company-specific AI-buildout capacity and order flow, treated as effectively unconstrained by demand."
  consumer: ""
  business: "Revenue fell 15% y/y and 13% q/q to $5B as ~$1.5B shifted out of the quarter on last-minute GB300 rack reconfiguration; gross margin held flat at 9.5% versus 9.6%, well below the old 14-17% long-term target, and management now frames double-digit margins as 'a little longer' out."
  investing: "Aggressive global capacity build — new/expanding sites in San Jose, Taiwan, Netherlands, Malaysia, and soon the Middle East — targeting 6,000 racks/month (3,000 DLC) this fiscal year; a $1.8B AR factoring facility was put in place specifically because doubling revenue outstripped normal working capital."
  scarcity: "Working capital and cash flow, not chips: Q1 burned $918M in operating cash flow, inventory jumped to $5.7B (105 days, up 30 days q/q), and the company moved to net debt of $575M from net cash of $412M to fund the ramp."
  forward: "Management raised full-year guidance to 'at least $36 billion' (from $33B) and guided Q2 to at least $10.5B, calling both numbers conservative, with CEO Liang projecting theoretical capacity near $100B annualized if fully utilized."
  acting: "Building DCBBS (full rack/data-center building-block solution spanning cooling, power, networking, software) as the stated path to >20% margins, and standing up a new federal program to chase U.S. government contracts — both are real headcount/facility commitments, not just talk."
  hedges: "Refused to give backlog figures, declined margin guidance beyond one quarter out, would not name customers behind the $13B GB300/B300 order book, and repeatedly said revenue growth will be 'controlled' by cash flow rather than capacity."
  contradictions: "CFO admitted Q2 guidance implies roughly 0% incremental contribution margin on the added revenue, yet CEO simultaneously called $36B 'a very conservative number' — the growth story and the margin story are pulling in opposite directions on the same guide."
  street: "Analysts pressed hard on gross margin trajectory, the mechanics and durability of the $13B order book, capacity utilization economics, and whether this is a repeat of the low-margin xAI Colossus 'lighthouse customer' playbook; management dodged backlog detail and long-term margin targets each time."
---

# SMCI — fiscal 2026-Q1 call (2025-11-04)

**The key idea:** SMCI is scaling from a $5-6B/quarter business to a $10B+/quarter business almost overnight, chasing the largest GB300/Blackwell Ultra deals in company history — but doing so at what its own CFO conceded is roughly zero incremental gross margin, funded by newly-tapped receivables factoring rather than operating cash flow. The bet is that scale, DCBBS attach, and manufacturing diversification eventually convert volume into margin; for now, the company is explicitly prioritizing market share and "total profit" over margin percentage.

## The read — 3-5 points from the whole transcript
1. **A $1.5B shipment slip, not a demand problem.** Revenue missed guidance because GB300 rack configurations required "intricate integration, testing and validation" that pushed ~$1.5B into the December quarter — management frames this as pure execution timing against a record $13B+ order book, not softening orders.
2. **Margin is the tension of the call.** Non-GAAP gross margin was flat at 9.5%, guided down another 300bps next quarter, and an analyst bluntly noted the guide "implies 0% contribution margin" on the incremental revenue — a sharp downgrade from the 2021-vintage 14-17% long-term target, which CFO Weigand now says the company will "give guidance when we can see it clearly."
3. **This is Colossus 2.0.** Two separate analysts drew the parallel to the low-margin xAI Colossus buildout from 18 months ago as a "lighthouse customer" play; management confirmed it's repeating the pattern with an even larger unnamed customer's GB300 mega-cluster, calling it their "first GIGA project."
4. **Working capital, not chips, is the real constraint.** Operating cash flow was -$918M, inventory ballooned to $5.7B (cash conversion cycle stretched from 96 to 123 days), and the company flipped from net cash to net debt — prompting a new $1.8B accounts-receivable factoring facility explicitly to fund the ramp.
5. **DCBBS is the stated margin escape hatch.** CEO Liang repeatedly pitches the full-stack Data Center Building Block Solution (racks, liquid cooling, power, networking, software) as carrying >20% margins versus commodity server assembly — but it's early-stage ("we have begun shipping DCBBS orders to some key customers") and unquantified in the model.

## Economy & consumer
- No macro or consumer commentary at all — this is a pure AI-capex supply-chain story where demand is treated as given and the entire discussion is about SMCI's ability to build, staff, and finance capacity to meet it.

## The business — what's working, what's not
- **Working:** AI GPU platforms were **over 75% of Q1 revenue**, and the OEM/large-datacenter segment grew 25% y/y to 68% of revenue even as the enterprise channel fell 51% y/y — the business is increasingly a hyperscale/neocloud pure-play.
- **Not working:** Gross margin has been **flat to declining for two straight quarters** (9.6% → 9.5%, guided down 300bps more) even as revenue guidance was raised — the classic "growing into losses on the margin line" pattern.
- **10%+ customer concentration is falling, not the risk it sounds:** SMCI had 2 customers over 10% of revenue this quarter versus 4 a year ago — David Weigand called this "some of the best customers in the world" but declined to name them or give backlog composition.
- **Geographic mix flipped hard toward Asia:** Asia revenue grew 143% y/y (a U.S. customer opened a data center there) while U.S. revenue fell 57% y/y — a single customer's geography choice is materially reshaping SMCI's reported regional mix.

## Investing & scarcity
- **Global manufacturing sprint:** new or expanding facilities in San Jose, Taiwan, Netherlands, Malaysia, and "soon the Middle East," targeting **6,000 racks/month including 3,000 DLC racks** within the fiscal year, on 52MW of power capacity already in place.
- **Theoretical capacity dwarfs current run rate:** Liang did the math live on the call — 3,000 liquid-cooling racks/month × 12 months × ~$3M/rack — landing near **"more than $100 billion"** in annualized capacity, versus a $36B full-year guide, implying deliberate conservatism/burn-in caution on a brand-new GB300 platform.
- **Cash, not silicon, is the binding constraint:** CFO stated plainly they "will control our revenue based on our cash flow" — a striking admission that order intake already exceeds what they're willing/able to finance without new instruments like the AR factoring facility.
- **CapEx is comparatively tiny** ($32M in Q1, guided $60-80M in Q2) relative to the working-capital swing — this is an inventory/receivables-funded ramp, not a heavy owned-asset buildout.

## Where they think it's going vs what they're doing about it
- **Belief:** Liang called $36B for the year "a very conservative number" and said growth will continue "through the balance of the calendar year," with double-digit gross margins "not too far away."
- **Action backing it:** Real capacity investment (new facilities, 6,000 racks/month target, DCBBS product buildout, a new federal sales program) is underway — this isn't purely rhetorical.
- **The gap:** None of the near-term guidance (Q2 margin down 300bps, "0% contribution margin" per analyst math) actually supports the "conservative guide, margins improving soon" narrative — management is asking investors to trust a margin inflection that isn't visible in a single forward quarter of guidance, and explicitly won't commit to when it arrives ("we'll give guidance when we can see it clearly").

## Hedges — what they wouldn't commit to
- **No backlog disclosure, ever:** "it's been our practice not to talk about backlog" — even as they tout a record $13B+ in new orders, the stock (order book minus shipments) remains opaque.
- **No customer names** behind the $13B order book or the "largest deal in our 32-year history" — repeatedly described only as "high-profile, high-value" partners.
- **No margin guidance beyond one quarter:** explicitly declined to reaffirm or replace the old 14-17% long-term gross margin target, saying only it's "still in our plan, it just take a little bit longer."
- **Declined to size total manufacturing capacity** in revenue terms when directly asked, before Liang later volunteered a rough "$100 billion" ceiling unprompted.

## The street — what analysts asked
- **Margin sustainability dominated the Q&A** — three separate analysts pushed on whether the current low-margin, mega-deal-driven growth is a repeatable pattern (the xAI Colossus comparison came up twice) or a one-off cost of landing lighthouse customers, and whether follow-on orders from previously-discounted customers actually carry better pricing.
- **Order book opacity was a recurring friction point** — analysts wanted backlog size, order composition, and customer concentration; management gave order-intake figures but stonewalled on backlog and names.
- **Working capital and financing came up directly** — one analyst asked when SMCI would need to tap capital markets, prompting disclosure of the new $1.8B AR factoring facility.
- **Compressed worry:** analysts are converging on one question — is SMCI buying revenue and market share at a margin cost it can't yet prove it will recover, funded by increasingly stretched working capital?
