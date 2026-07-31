---
ticker: CDNS
call_date: 2026-07-27
report_quarter: 2026-Q3
period_reported: fiscal 2026-Q2
source: bronze/CDNS/2026-Q3/transcript-2026-07-27.md
generated: 2026-07-30 (automated silver pass, schema v2)
mentions: ["INTEL", "SAMSUNG", "TSMC", "RAPIDUS", "NVIDIA", "HEXAGON"]
answers:
  economy: "AI compute demand is shifting toward inferencing-driven memory diversity (SRAM offload, CXL DRAM, flash), pulling more custom/analog/IP work into Cadence's pipeline as customers proliferate bespoke silicon."
  business: "IP grew 40%+ YoY on better leading-node PPA, sharper category focus, and a more fragmented foundry landscape; hardware (Palladium/Protium) had a record quarter but is supply-constrained, not demand-constrained."
  investing: "R&D growth guided to ~19% YoY (vs ~10% prior year) with ~$20-25M set aside for 2H spend on Hexagon D&E integration and Intel-related investment, deliberately compressing 2H margins."
  scarcity: "Hardware systems (Palladium Z3, Protium X3) are being built as fast as possible against backlog — demand exceeds manufacturing capacity, not customer interest."
  forward: "Devgan frames agentic AI as TAM expansion, not disintermediation, via a 'three-layer cake' (compute/data, physics engines, agents); startup formation is picking back up after a lull, signaling fresh capital into new silicon bets."
  acting: "Shipped four AI Super Agents (AuraStack, ChipStack, ViraStack, InnoStack) now in production/engagement with 20-25+ customers each; rebuilt the Intel relationship via a new multi-year 14A deal spanning IP, agentic EDA, and DTCO co-optimization."
  hedges: "Devgan repeatedly declined to quantify agentic AI's revenue contribution or size the agentic TAM, calling it 'early stages' about six months post-launch, and wouldn't size the Intel deal's revenue benefit, saying most is still to come."
  contradictions: "On Kimi autonomously orchestrating chip design without Cadence, Devgan downplayed the example (a small block on 20-year-old tech, 20-30x slower than current) rather than disputing the underlying threat mechanism."
  street: "Analysts pressed on whether agentic AI revenue is real vs. narrative, whether the ~55% bookings surge is chip-cycle beta or genuine AI-seat expansion, what the Intel deal is worth, whether rising R&D signals margin risk into 2027, and repeatedly whether Cadence's moat survives if a frontier LLM eventually orchestrates physical design without a Cadence seat."
---

# CDNS — fiscal 2026-Q2 call (2026-07-27)

**The key idea:** Cadence's pitch is that AI doesn't disintermediate EDA — it multiplies demand for it, because agents "call the underlying physically accurate engines more often" as they explore larger design spaces. The whole call is Devgan defending a "three-layer cake" thesis (compute/data → physics engines → agents) against the obvious threat narrative: that an LLM could eventually generate chip layouts without Cadence in the loop at all.

## Where they're going / what they're building
- **The "three-layer cake" is the entire strategic identity now** — compute/data at bottom, physically accurate solvers in the middle, "AI agents and orchestration" on top — and Devgan repeated it almost verbatim in response to nearly every question, treating agentic AI as a **"long-term TAM expansion opportunity"** rather than a threat to the core license business.
- Four "AI Super Agents" are now shipping: **AuraStack** (PCB/packaging, claimed 15x productivity, 2x faster time-to-market), **ChipStack** (verification, 20+ customer engagements, already in production on multiple chip designs), **ViraStack** (analog/custom, 25+ engagements, 2-10x gains), and **InnoStack** (advanced-node SoC, just picked up by Rapidus). Devgan: "we are pleased by the interest... almost all customers want to engage in our agent stack."
- With NVIDIA at Computex, they introduced a **"fully autonomous virtual AI design engineer"** extending ChipStack — the claimed result is verification cycle time cut from five weeks to under a day (**"more than 40x faster RTL validation"**) on an advanced-node design.
- The **Intel relationship is being rebuilt from scratch** after what Devgan called "a 10 or 20-year-old problem": a new multi-year 14A engagement spanning IP, agentic EDA, and DTCO co-optimization, which he frames as "not a one or two-year-old problem" finally resolving. He was explicit that most of the revenue benefit is still to come, not booked yet.
- IP grew over 40% YoY and management attributes it to three structural shifts: better PPA competitiveness at leading nodes (winning designs they "would not participate in two years ago"), a sharpened focus on five categories (interface, memory, foundation IP for AI/HPC), and a **more fragmented foundry landscape** (Intel, Samsung, Rapidus alongside TSMC) that multiplies the number of IP relationships needed.
- Hardware (Palladium Z3, Protium X3) had another record quarter and is explicitly **supply-constrained, not demand-constrained** — "we're building the systems as quickly as we can to deliver against the backlog."

## What's changing
- Management explicitly reframed AI compute demand as shifting toward **inferencing-driven memory architecture diversity** — SRAM offload, CXL-based DRAM offload, flash-based memory — which Devgan says is pulling more analog, custom, and memory-IP work into Cadence's pipeline as customers proliferate bespoke silicon rather than converging on standard parts.
- A notable admission on competitive posture: **"a few years ago we were weak at Intel and Samsung, and that definitely has changed."** The company is openly narrating a multi-year turnaround in accounts where TSMC had been the strong relationship.
- **Startup formation is picking back up** after a lull — Devgan: "startups were kind of dormant. In the last six months there are some very high-profile startups... not just in AI, but in networking and even CPU" — a tell that capital is flowing into new silicon bets beyond the hyperscalers.
- The full-year revenue guide was raised to ~19% growth — described by Devgan as **"the highest we ever had"** in a single quarterly raise — with management repeatedly stressing the raise is broad-based (core EDA, IP, hardware, SDA) rather than driven by agentic AI or any single customer, seemingly pre-empting the obvious follow-up question about how much of the raise is AI-hype versus organic.

## What's NOT working (or being talked around)
- **Second-half margins are being deliberately compressed** to fund integration and expansion spend — R&D growth guided to ~19% YoY versus ~10% last year — with John Wall careful to frame this as "deliberate investments, not a deterioration in the underlying model." Specific line items: Hexagon D&E integration and Intel-related investment, with **~$20-25 million** set aside for second-half spend.
- Devgan was **notably non-committal on quantifying agentic AI's actual revenue contribution**, repeatedly deflecting to "we'll see how it progresses" and stressing "we are still in early stages," "roughly six months" into the launch — a soft admission that the productivity claims (2x-40x) are anecdotal wins, not yet a monetization pattern management will forecast.
- On the existential question — Kimi (an open-source model) autonomously orchestrating chip design tools without Cadence — Devgan's rebuttal leaned on minimizing the example rather than disputing the mechanism: the chip in question was **"a small block... about technology that is 20 years old... 20, 30 times slower than current frequency."** That's a real caveat, but it sidesteps the trajectory question of whether such agents scale up over time.
- **Nobody quantified the agentic TAM** despite being asked directly (Joe Quatrochi's question went unanswered numerically) — Devgan pivoted to qualitative "the interest is amazing" language rather than any sizing.
- Hexagon's D&E integration is still "progressing well" language, not "done" language, three-plus quarters after acquisition — suggesting integration friction that management isn't detailing.

## Street anxiety (compressed)
Analysts pushed hard and repeatedly on whether agentic AI revenue is real and sizeable versus narrative · whether the ~55% bookings surge is chip-cycle beta or genuine AI-tool-driven seat expansion · what the Intel deal is actually worth and over what timeframe, with management declining to size it · whether elevated R&D spend (19% growth vs. 10% prior year) signals margin structure risk into 2027 · and underneath all of it, the same question asked six different ways: is Cadence's moat durable if a frontier LLM can eventually orchestrate physical design without a Cadence seat, or is management's three-layer-cake answer a rehearsed deflection rather than a real technical defense.
