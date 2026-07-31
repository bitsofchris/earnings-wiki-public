---
ticker: MRVL
call_date: 2025-12-02
report_quarter: 2025-Q4
period_reported: fiscal 2026-Q3
source: bronze/MRVL/2025-Q4/transcript-2025-12-02.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [AMAZON, AWS, INPHI, INNOVIUM, AQUANTIA, AVERA, CELESTIAL AI]
answers:
  economy: "No macro commentary — the entire call is AI-capex-specific; cloud CapEx growth assumption for calendar/fiscal '27 was revised up from 18% to '30%+' since September, and that alone drove Marvell's re-guide."
  business: "Record revenue ($2.075B, +37% y/y) beat guidance on data center strength; custom silicon revenue actually declined sequentially on 'lumpiness,' offset by double-digit sequential growth in optics, storage, and switching."
  investing: "Announced acquisition of Celestial AI (optical/photonic scale-up interconnect) funded via stock and cash, no new debt; management frames it as the next in a string of 'home run' M&A (Inphi, Innovium, Aquantia) after divesting Automotive Ethernet and WiFi to concentrate entirely on data center."
  scarcity: "Reticle-size and die-edge I/O beachfront are the binding physical constraints on next-gen XPU packages — Celestial's pitch is freeing that beachfront for more HBM/bandwidth; secondarily, 'power dissipation savings' are described as the real driver of continued node migration, i.e. power, not raw compute, is the constraint executives orient around."
  forward: "Management now models data center revenue growth accelerating from ~45% this year to 25% next fiscal year to ~40% the year after (fiscal '28), implying a roughly 50% compounded multiyear growth rate since fiscal 2023 — explicitly excluding any Celestial contribution."
  acting: "Fast-tracking in-house scale-up switch silicon (UALink and ESUN standards, sampling 2H fiscal '27), doubling AEC/retimer revenue guidance, and buying Celestial AI outright rather than partnering — CEO said the team 'looked at, could we do it ourselves, could we do it with a partner' and concluded acquisition was the 'home run.'"
  hedges: "Declined to extend forecasting detail past fiscal '28 ('a little far out to go all the way to '29'); repeatedly called the next-gen custom XPU program 'a good safe base case number' rather than a stretch target, explicitly avoiding 'dreaming the dream'; would not name customers behind Celestial's design wins beyond one unnamed Tier-1 hyperscaler."
  contradictions: "CEO ties optics growth to cloud CapEx as 'a proxy' for modeling simplicity, then immediately concedes the metric is wrong — 'the optics business is fundamentally driven by AI acceleration... growing so far above CapEx' — i.e., the framework he just gave analysts to model the business is one he admits understates it."
  street: "Nearly every question was Celestial-AI-specific (revenue scope, customer breadth, timing) or asked management to reconcile a highly unusual 3-year-out revenue framework against Street norms of one-quarter guidance; one question directly noted a competitor (Broadcom) moving to rack-level systems and probed whether Marvell would follow — CEO said rack-level vision exists but no systems revenue is in any current forecast."
---

# MRVL — fiscal 2026-Q3 call (2025-12-02)

**The key idea:** Marvell used a record quarter to launch a multiyear framework — the CEO gave analysts guidance out to fiscal 2028, an explicit break from Marvell's own guide-one-quarter-at-a-time history — while simultaneously announcing the acquisition of Celestial AI, a photonic-interconnect startup, to buy its way into the emerging scale-up optical switching market rather than build it alone. The tension: management is asking the Street to trust multi-year custom-silicon and optics targets from a business that just missed on custom (sequential decline, called "lumpiness") this very quarter.

## The read — 3-5 points from the whole transcript
1. **Guidance framework shifted, not just the number.** CEO explicitly departed from Marvell's standard one-quarter-out guidance to lay out a 3-year forward model (fiscal '27 →'28), justifying it as necessary because "these are multiyear cycles" and customers now require Marvell to plan R&D/capacity 6-8 quarters ahead — a genuine business signal (deep customer-Marvell co-planning) but also a rhetorical device to pull the Street's attention off this quarter's custom miss.
2. **Buying rather than building the next interconnect wave.** Celestial AI (photonic scale-up fabric) is bought outright, continuing Marvell's stated playbook (Inphi, Innovium, Aquantia). Meaningful revenue isn't expected until 2H fiscal 2028, with a base case of $500M annualized run-rate by 4Q FY28 doubling to $1B by 4Q FY29 — a bet placed years ahead of any proof of commercial deployment.
3. **Copper is hitting a wall.** "Copper-based interconnects used in today's scale-up systems are approaching their fundamental limits in reach and bandwidth" — stated plainly as the reason optical scale-up interconnect is now a real, near-term TAM (~$10B by the CEO's own math), not a speculative future category.
4. **Custom silicon growth guide (20%) is deliberately conservative.** CEO called it "a good safe base case number," explicitly declining to extrapolate further given "history on this custom business where either people got ahead of themselves or there's a lot of noise in the system" — a candid admission that Street enthusiasm has previously outrun the actual business.
5. **AWS relationship deepens via warrants, not just orders.** An amended warrant agreement adds "photonic fabric" as a new product swim lane alongside AI custom and networking products already covered by a warrant issued only a year prior — a financial-engineering signal of how tightly the hyperscaler and Marvell are now aligning incentives.

## Economy & consumer
- No section — this is a pure-play AI-infrastructure supplier call; there is no direct-consumer or macro-economy commentary. The only "macro" input cited is cloud CapEx growth expectations, revised from 18% to over 30% since September, which management uses purely as a modeling proxy, not an economic read.

## The business — what's working, what's not
- **Record top line, beat on data center.** Revenue of $2.075B (+37% y/y, +3% sequentially) beat the guided midpoint on "stronger than forecasted demand" in data center; non-GAAP EPS of $0.76 beat by $0.02.
- **Optics/switching/storage all posted double-digit sequential growth** on a percentage basis — the interconnect and switch businesses are the current engine.
- **Custom silicon declined sequentially** this quarter "due to lumpiness in demand," the one soft spot in an otherwise record quarter; management frames it as a timing issue tied to a next-gen XPU transition, not demand loss, but it's the crack in an otherwise clean beat.
- **Enterprise networking normalized** — inventory digestion in that segment is "complete," reaching a ~$1B annualized run-rate, while carrier is recovering toward "almost double" its year-ago level.
- **Operating leverage is real:** non-GAAP EPS grew 77% y/y, "more than double the pace of revenue growth."

## Investing & scarcity
- **Celestial AI acquisition** (~$50M in added annual opex post-close, funded by stock/cash, no incremental debt) is the headline capital allocation move — a bet on photonic scale-up fabric years before revenue materializes.
- **Reticle size and die-edge beachfront are the physical constraint** shaping XPU package design: Celestial's pitch is that its 3D co-packaged photonics frees up die-edge area "which can be repurposed to significantly increase the amount of HBM within the XPU package" — a direct memory/bandwidth-scarcity workaround, not a compute one.
- **Power, not raw compute, is what's described as scarce and monetizable:** the CEO ties node migration (2nm) explicitly to "power savings are worth real OpEx dollars" for customers — reframing Moore's Law progress as a power economics story.
- **Executing a $1B accelerated buyback plus $300M ongoing repurchase** this quarter while still funding the acquisition — signals confidence cash flow ($582M op cash flow, a record) can support both.

## Where they think it's going vs what they're doing about it
- **Belief:** Data center revenue growth accelerates from ~45% this year to 25% next year, then re-accelerates to ~40% in fiscal '28, driven by custom XPU transitions, XPU-attach (NIC/CXL), and optics outgrowing CapEx.
- **Action backing it:** Purchase orders already in hand "for the entirety of next fiscal year's" current custom forecast; UALink/ESUN scale-up switch silicon sampling committed for 2H fiscal '27; AEC/retimer design wins already secured at 2 Tier-1 hyperscalers plus "more than 10 sockets" for retimers.
- **The gap:** the acceleration to 40% growth in fiscal '28 depends heavily on a "new meaningful XPU socket" and Celestial revenue that hasn't shipped yet and whose customer base is, by the CEO's own admission, narrow today ("we have one Tier 1 hyperscaler... pulling us through the first wave"). The multi-year framework is being sold with more certainty than the underlying customer concentration supports.

## Hedges — what they wouldn't commit to
- Refused to extend detailed guidance beyond fiscal 2028 ("it's a little far out to go all the way to '29").
- Called the 20% custom growth guide a deliberately conservative "safe base case," explicitly resisting pressure to raise it despite acknowledging "a lot of good things happening."
- Declined to name any Celestial AI hyperscaler customers beyond the one confirmed (implicitly AWS, per the warrant 8-K) — "in the spirit of customer confidentiality... I can't go into too much."
- No system/rack-level revenue is included in any forecast despite stating a "rack-scale vision" — deliberately keeping that optionality out of the model for now.

## The street — what analysts asked
- The overwhelming theme was **Celestial AI**: its revenue scope (chiplet-only vs. broader memory business), customer breadth/concentration, and credibility of the fiscal '28-'29 targets.
- A second cluster probed **the unusual multi-year guidance itself** — analysts pushed on why Marvell broke from single-quarter guidance and how confident management really is in numbers 2-3 years out.
- One question directly raised **competitive pressure to move to rack/system-level solutions** (a clear reference to Broadcom), testing whether Marvell's point-solution model is at risk of commoditization — management insisted on a "rack-scale vision" while conceding no systems revenue is currently modeled.
- Compressed worry: **the Street is being asked to underwrite a three-year growth curve built substantially on unproven, narrow-customer optical technology and a custom-silicon program that just missed this quarter.**
