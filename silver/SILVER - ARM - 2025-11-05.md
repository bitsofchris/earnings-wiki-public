---
ticker: ARM
call_date: 2025-11-05
report_quarter: 2025-Q4
period_reported: fiscal 2026-Q2
source: bronze/ARM/2025-Q4/transcript-2025-11-05.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [NVIDIA, AWS, GOOGLE, MICROSOFT, TESLA, META, SOFTBANK, OPENAI, SAMSUNG, OPPO, VIVO, DREAMBIG, MELLANOX, ARISTA, ORACLE]
answers:
  economy: "No macro commentary; the call frames the environment entirely around an AI compute build-out that management says is accelerating, not slowing — 'the demand picture for compute is greater than it was' 11 months after Stargate was announced."
  business: "Third straight billion-dollar quarter, revenue up 34% YoY; royalty revenue hit a record $620M (up 21%, above mid-teens guide) and licensing rose 56% to $515M, with data-center Neoverse royalties more than doubling YoY."
  investing: "R&D spend is being accelerated to fund exploration 'beyond our current platform into additional compute subsystems, chiplets or complex SoCs,' plus the announced acquisition of DreamBig Semiconductor for Ethernet/networking IP for scale-up/scale-out data-center networking."
  scarcity: "Power, not chips, is the binding constraint: 'power has become the bottleneck for everyone,' pulling demand toward Arm's ~50%-more-efficient compute as the fix — not a compute-availability story but an energy-infrastructure one."
  forward: "Management expects training to keep dominating compute today but to 'flip' toward inference over time, pushing workloads to the edge, and expects the cloud/networking royalty mix (~10% of royalties) to climb to 15-20% this fiscal year."
  acting: "Signed 3 new CSS licenses (19 total across 11 companies), launched Lumex CSS with royalties already flowing from an early licensee within months, deepened the SoftBank/Stargate relationship (related-party revenue jumped from ~$126M to ~$178M quarter-over-quarter), and moved to acquire DreamBig."
  hedges: "Declined to give any timeline, product name, or technology detail on the chiplet/SoC expansion — CFO explicitly said they'll only speak up once there's tape-out, samples back, AND noncancelable customer orders; also declined multi-year Stargate revenue framing and any specifics on which partner is driving early Lumex royalties."
  contradictions: "CFO frames the SoftBank related-party design-services revenue as durable and non-anomalous ('if SoftBank wasn't a related party, we'd just be booking license and design services... the numbers would be pretty similar'), while simultaneously calling it lower-margin funded R&D that could later cannibalize the license line it's currently inflating."
  street: "Analysts clustered on three things: how durable/large the SoftBank-Stargate revenue relationship is, when and how the chiplet/SoC pivot becomes a real product, and whether new AI silicon spend is genuinely incremental Arm content or share-shift. The underlying worry compressed: is this quarter's growth structural royalty/share gain, or a related-party/one-time-deal sugar high that could reverse once SoftBank's own products ship."
---

# ARM — fiscal 2026-Q2 call (2025-11-05)

**The key idea:** Arm posted its best Q2 ever on the back of a data-center AI buildout it says is now gated by power, not silicon — positioning its efficiency advantage as the natural beneficiary. But underneath the headline growth is a related-party SoftBank/Stargate revenue stream that expanded fast and unexplained, plus a still-secret bet to move beyond IP licensing into chiplets or full SoCs that management refuses to detail until it's a fait accompli.

## The read — 3-5 points from the whole transcript
1. **Power is the new bottleneck, and Arm is positioning as the fix.** Rene Haas: "power has become the bottleneck for everyone... Arm is about 50% more efficient than competitive solutions." This reframes Arm's pitch from pure performance to power-constrained economics — a durable structural argument if power buildout stays slow.
2. **Data center Neoverse is now the growth engine, not smartphones.** Neoverse royalties more than doubled YoY, cloud/networking royalty mix is tracking toward 15-20% of royalties from ~10% a year ago, and management says this trend is "going faster than we expected a year ago."
3. **The SoftBank relationship is opaque and growing fast.** Related-party revenue jumped ~$52M quarter-over-quarter to $178M (design services + licensing), described as durable but explicitly acknowledged as "lower margin" and potentially cannibalistic of future license revenue once SoftBank products ship.
4. **Arm is quietly funding a strategic pivot it won't name.** CFO confirmed R&D is accelerating specifically to explore chiplets/complex SoCs — a categorical departure from pure IP licensing — but set a high, deliberately opaque bar (tape-out + samples + noncancelable orders) before disclosing anything.
5. **CSS is becoming the default entry point and pricing lever.** All top 4 Android vendors now ship CSS-powered devices; Lumex CSS already generating royalties from an early licensee within months of a September launch — CSS is compressing customers' time-to-market and lifting Arm's per-chip royalty rate.

## Economy & consumer
- No explicit macro or consumer-demand commentary — Arm is a pure upstream IP supplier and the call frames everything through AI capex and semiconductor design cycles, not end-consumer spending.
- China called out as "as strong as we've ever seen," with the region driving one of the largest license deals in the quarter — the only geography/demand color offered.

## The business — what's working, what's not
- **Working:** Royalty revenue at a record $620M (+21% YoY, above mid-teens guide), licensing up 56% to $515M, ACV growth of 28% YoY for a second straight quarter — "well above our usual run rate" and above long-term mid-to-high-single-digit targets.
- **Working:** Non-GAAP operating margin expanded to 41.1% from 38.6% a year ago even while R&D ramps, meaning revenue growth is outpacing OpEx growth.
- **Watch item:** Licensing revenue is inherently lumpy ("varies quarter-to-quarter due to timing and size of high-value deals") — the 56% growth print is partly deal-timing, not pure trend, which is why management steers to ACV instead.

## Investing & scarcity
- R&D (non-GAAP OpEx) up 31% YoY to $648M, guided to ~$720M next quarter — explicitly funding exploration of subsystems, chiplets, and complete SoCs beyond Arm's traditional IP-licensing model.
- Lumex CSS alone took roughly 1,000 engineer-years and a peak team of 450+ engineers over four years and "hundreds of millions of dollars" — a concrete data point on how capital-intensive Arm's compute-subsystem strategy has become.
- Announced acquisition of DreamBig Semiconductor for Ethernet/networking IP to broaden data-center scale-up/scale-out offerings — a direct extension into a component Arm didn't previously address.
- The binding scarcity constraint, per management, sits outside Arm entirely: power generation and grid/transformer infrastructure for hyperscale data centers, which they argue accelerates (not delays) adoption of Arm's efficiency advantage.

## Where they think it's going vs what they're doing about it
- **Belief:** Training will keep dominating compute today but inevitably "flip" toward inference, pushing AI workloads to edge devices and batteries. **Action:** heavy investment in scalable matrix extensions in Lumex/CSS and a joint architecture push with Meta (announced October) to let developers port models seamlessly between cloud and edge — a real product commitment behind the inference-at-the-edge thesis.
- **Belief:** Chiplets/SoCs represent a large incremental opportunity. **Action:** R&D dollars are already flowing there, but there's no committed product, timeline, or customer disclosed — the money is moving before the strategy is public, which is itself a signal of confidence but leaves investors without a way to size the bet.
- **Belief:** Cloud/networking royalty mix will keep climbing toward 15-20% of royalties. **Action:** DreamBig acquisition and continued Neoverse/CSS penetration in DPUs, switches (Mellanox BlueField, Broadcom Tomahawk, Arista) directly support this, so belief and action are well aligned here — a rare case with no gap.

## Hedges — what they wouldn't commit to
- Refused any timeline or product detail on the SoC/chiplet expansion: "there's nothing I can talk to you about today in terms of time line, about products or technologies" — disclosure gated behind tape-out, samples, AND noncancelable orders, a bar set high enough to defer accountability for quarters.
- Declined a multi-year (1/3/5-year) revenue framing for the Stargate opportunity when directly asked, instead reframing the question around overall demand growth since the original Stargate announcement.
- Would not name the customer generating early Lumex CSS royalties, only characterizing it as a repeat (second-generation) CSS licensee.
- Would not forecast Q4 licensing revenue, citing 6-9 month deal cycles and dependence on customer timing — deferred specificity to "next quarter."

## The street — what analysts asked
- Heavy clustering on the AI data-center buildout and Arm's positioning within it (power constraints, Neoverse penetration, networking/DPU content) — analysts are trying to size how much of the trillion-dollar capex wave actually flows to Arm royalties versus just hyperscaler capex headlines.
- Multiple questions probed the SoftBank/Stargate related-party revenue specifically — magnitude, run-rate durability, and whether a future chiplet/SoC product would cannibalize the current license-plus-design-services stream. Management's answer conceded the cannibalization risk directly.
- Questions on the chiplet/SoC strategy repeatedly got redirected to "we'll tell you when there's tape-out" — a topic clearly probed hard but consistently dodged with the same scripted milestone answer.
- Compressed worry: how much of this quarter's blowout growth is structural royalty/share gain across the AI stack, and how much is a related-party SoftBank relationship and lumpy license deals that could unwind once SoftBank's own downstream products materialize.
