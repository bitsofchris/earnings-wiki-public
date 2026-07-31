---
ticker: MRVL
call_date: 2026-05-27
report_quarter: 2026-Q2
period_reported: fiscal 2027-Q1
source: bronze/MRVL/2026-Q2/transcript-2026-05-27.md
generated: 2026-07-30 (automated silver pass, schema v3)
mentions: [NVIDIA, TSMC, GROQ, CELESTIAL AI, XCONN, POLARITON, INNOVIUM, AVERA, GLOBALFOUNDRIES, IBM]
answers:
  economy: "No macro commentary — the call is entirely about AI infrastructure capex, which management frames as still accelerating, not cooling: cloud capex growth is expected to moderate to '30%+' in fiscal 2028 even as Marvell's own growth accelerates."
  consumer: "Not applicable — Marvell sells to hyperscalers and telecom operators, not consumers. Communications/carrier/enterprise segment is described as having 'largely recovered from inventory corrections.'"
  business: "Record revenue of $2.418B (+9% seq, +28% YoY), data center now 76% of revenue and reaccelerating; guide raised repeatedly with Q3 now expected to hit $3B a full quarter earlier than prior guidance. Communications remains the small, low-growth (~10%) segment by comparison."
  investing: "~$1B in supplier prepayments this fiscal year to lock capacity, plus two fresh acquisitions (Polariton for plasmonic silicon photonics, on top of Celestial AI and XConn closed this quarter) — capital is going almost entirely into securing supply and buying scale-up/optical interconnect technology."
  forward: "Management now expects ~50% data center growth in fiscal 2027 accelerating to ~55% in fiscal 2028, custom silicon to 'more than double' next year, and reiterates the >$10B custom revenue target for fiscal 2029 — guidance has been raised multiple quarters running."
  acting: "Committing ~$1B in prepayments to suppliers, closing three acquisitions in one year (Celestial AI, XConn, Polariton) to buy scale-up optics and switch IP, and expanding R&D specifically into scale-up NVLink/UALink/ESUN switching and silicon photonics ahead of confirmed revenue."
  hedges: "Declined to name the new Tier-1 custom XPU customer or give specifics on other design wins ('no additional details at this time'); called the possibility of entering the broader custom-compute TAM an 'insurance policy,' explicitly not required for the guided numbers; scale-up switching/optics upside is called 'not really in any numbers' — deliberately excluded from guidance despite being highlighted at length."
  contradictions: "Interconnect growth guidance has gone 30%→50%→70%+ YoY in successive quarters — management frames this as 'where we are right now' with 'upward bias' rather than admitting the pattern of systematic prior under-forecasting."
  street: "Analysts pressed repeatedly for the same thing from different angles — magnitude/timing of the new Tier-1 XPU ramp, breadth of the custom customer base, and whether scale-up networking upside is already baked into guidance. Management consistently declined specifics on customer identity while reiterating that scale-up/switching upside sits entirely outside current numbers. Compressed worry: is Marvell's guidance still lagging the real demand curve, and how much of the future growth depends on one unnamed customer executing on schedule."
---

# MRVL — fiscal 2027-Q1 call (2026-05-27)

**The key idea:** Marvell delivered a record quarter and raised guidance again — fiscal 2027 up ~$500M, fiscal 2028 up ~$1.5B versus last quarter's outlook — driven almost entirely by AI data center networking, where interconnect growth guidance has now been revised upward from 30% to 50% to 70%+ YoY across consecutive quarters. The real story is optionality: scale-up networking (NVLink/UALink/ESUN switches, CPO/NPO optics) is described at length as a "massive new TAM" but management insists it's barely in the numbers yet, making this a bet that today's guide is once again conservative relative to what ships.

## The read — 3-5 points from the whole transcript
1. **Guidance keeps getting raised, and management keeps calling the increases "upward bias," not correction.** Interconnect growth went from 30% to 50% to 70%+ YoY across three quarters; CEO Matt Murphy says fiscal 2028 growth "could" run higher too, but frames this as newly discovered demand rather than a pattern of underestimating it.
2. **The NVIDIA partnership is a hedge on architecture, not a bet on one winner.** The deal spans optics (silicon photonics collaboration), NVLink Fusion (letting hyperscalers mix custom and merchant silicon), and AI-RAN (OCTEON base stations paired with NVIDIA GPUs) — Marvell explicitly positions itself as "the bridge" between custom and merchant architectures rather than picking a side.
4. **Three acquisitions in one year (Celestial AI, XConn, Polariton) are building an end-to-end scale-up optics and switching stack from scratch**, with a new Plasmonics-based photonics technology (>1 THz modulator bandwidth, "up to 10x higher" than current silicon photonics) meant to extend Marvell's roadmap to 3.2T and beyond.
5. **The single largest unquantified swing factor is the unnamed new Tier-1 custom XPU program**, which is "about 1/3" of next year's custom growth and remains undisclosed by customer or details despite five separate analyst attempts to get color on it.

## Economy & consumer
- No macro or consumer commentary — this is a pure-play AI infrastructure supplier call to hyperscalers and telecom carriers.
- The only "recovery" language is for the small communications/carrier/enterprise segment, which has "largely recovered from inventory corrections" and is expected to track underlying enterprise/carrier/consumer trends going forward at low-single-digit to ~10% growth — a rounding error next to the AI data center business.

## The business — what's working, what's not
- **Data center is now 76% of revenue** and reaccelerating: $1.83B (+11% seq, +27% YoY) this quarter, guided to mid-to-high-teens sequential and mid-40s% YoY growth next quarter.
- **Interconnect (DSPs, TIAs/drivers, coherent, DCI) is "the star of the show,"** now guided to >70% YoY growth in fiscal 2027, with TIAs/drivers alone approaching a $1B annualized run rate "in the next few quarters."
- **Custom silicon remains on plan** (>20% YoY this year, "more than double" next year) but GAAP EPS this quarter ($0.04) came in below guidance due to purchase-accounting drag from the Celestial AI/XConn deals and their earn-out obligations — a real, if temporary, cost of the acquisition spree.
- **Scale-out switching is doubling this year** to >$600M with line of sight to >$1B annualized in fiscal 2028, but Murphy is candid that Marvell remains a small-share "emerging company" in a large, already-established market.

## Investing & scarcity
- **~$1B in cash prepayments to suppliers this fiscal year**, funded from balance sheet and operating cash flow, explicitly to lock capacity rather than hope for allocation.
- **Polariton acquisition adds plasmonic photonics IP** aimed at pushing DCI/coherent-lite roadmaps to 3.2T; layered on top of Celestial AI (photonic fabric/EAM modulators, already design-won at a Tier-1 hyperscaler for scale-up XPU networks) and XConn (PCIe/CXL switching, now scale-up switch capability).
- **Scarcity is structural, not cyclical**: Koopmans says the company hasn't seen an unconstrained AI supply environment since 2020-2021, and the fix — tight, forecast-backed relationships with "a small number of key suppliers" — is the same playbook run at larger scale, not a new strategy.

## Where they think it's going vs what they're doing about it
- **Belief:** cloud capex growth moderates to "30%+" in fiscal 2028, yet Marvell's own data center revenue growth *accelerates* (50%→55%) because networking content per dollar of capex keeps rising as agentic AI, reasoning models, and MoE architectures drive more east-west traffic, more CPUs, more memory, and more scale-up bandwidth.
- **Action:** three acquisitions and a broadened NVIDIA partnership within the fiscal year, all aimed squarely at scale-up interconnect and switching — a market Murphy repeatedly says generates **zero revenue in the current $16.5B fiscal 2028 guide**. That's the clearest talk-vs-action gap on the call: the technology investment is already made and described in detail, but management refuses to put a dollar figure on it until it ships, calling it explicit "upside" rather than baseline.

## Hedges — what they wouldn't commit to
- **Refused to name the new Tier-1 custom XPU customer** or give any programmatic detail, across at least three separate analyst attempts, only confirming the program is "on track" and hitting milestones.
- **Called potential entry into the broader custom-compute TAM an "insurance policy,"** explicitly stated as unnecessary for hitting the >$10B fiscal 2029 custom target — a deliberate underpromise.
- **Scale-up switching/NVLink-UALink-ESUN opportunity is explicitly excluded from all guidance numbers** ("very little, nothing in the $16.5 billion"), despite being one of the most detailed topics on the call — pure optionality management won't yet price in.

## The street — what analysts asked
- Multiple questions converged on the same anxiety from different angles: how big and how real is the new, unnamed Tier-1 custom XPU program, and how much of next year's growth depends on it landing on schedule.
- Analysts also pushed on whether the repeatedly-raised interconnect and data center guidance reflects genuine incremental demand or previously-known customer forecasts management was simply slow to bake in — a question Murphy answered by crediting supply-chain execution rather than directly addressing prior conservatism.
- One-sentence worry: **how much of Marvell's accelerating growth trajectory rests on one still-unnamed customer's XPU program executing exactly as planned.**
