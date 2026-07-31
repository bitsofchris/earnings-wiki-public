---
ticker: ARM
call_date: 2026-07-29
report_quarter: 2026-Q3
period_reported: fiscal 2027-Q1
source: bronze/ARM/2026-Q3/transcript-2026-07-29.md
generated: 2026-07-30 (automated silver pass, schema v2)
mentions: ["CEREBRAS", "OPENAI", "META", "CLOUDFLARE", "ORACLE", "GOOGLE", "NVIDIA", "AWS", "MICROSOFT", "QUALCOMM", "SOFTBANK"]
answers:
  economy: "Demand for the AGI CPU has more than doubled to over $2B in three months, but supply chain capacity (wafers, substrates, test, memory) — not demand — is the binding constraint."
  consumer: "Smartphone royalty growth guidance was quietly cut from ~20% to high-teens (Q2 guided low-to-mid teens), driven by memory-price BOM inflation now hitting mid/upper-tier phones, not just the low end."
  business: "Neoverse and data-center royalties are accelerating sharply, and Arm-based server platforms now outspend x86 per IDC; but AGI CPU margins are stuck high-30s/low-40s for years and smartphone royalty growth is decelerating."
  investing: "Strategic pivot from pure IP licensing to selling silicon (Arm AGI CPU, launched March); next lever is raising core count above today's 128 (vs. Graviton5's 192) to improve agentic throughput."
  scarcity: "Wafers, substrates, test capacity, and memory gate AGI CPU output, not demand; management raised confidence in beating the original $1B supply commitment but wouldn't name the specific bottleneck or resolution date."
  forward: "Management believes agentic inference is fundamentally CPU-throughput-constrained, positioning the AGI CPU as a durable buy attached to every hyperscaler's accelerator build-out; TAM framing has moved from $100B+ to peer estimates of $200-220B."
  acting: "Shipped the AGI CPU to multiple customers across head-node, agentic-server, and cloud-infra segments (Cerebras, OpenAI, Meta, Cloudflare, Oracle OCI); building NVLink Fusion and Google Axion paths to stay accelerator-agnostic rather than NVIDIA-dependent."
  hedges: "When pressed on why $1B of supply can't just be bought for a claimed $50B market, Haas reframed it as an industry-wide constraint rather than naming a specific bottleneck component or resolution timeline; margin-dilution and customer-concentration questions went undiscussed."
  street: "Analysts pressed on the specific source of new supply confidence, whether a single-point-of-failure component exists, whether CPU-only positioning gets squeezed out as hyperscalers co-design accelerators in-house, and whether the smartphone royalty cut and SoftBank-dependent licensing revenue signal a durable trend or a one-quarter blip."
---

# ARM — fiscal 2027-Q1 call (2026-07-29)

**The key idea:** ARM is betting its next act on selling actual silicon (the "Arm AGI CPU"), not just IP licenses — and the pitch is that agentic inference is fundamentally CPU-throughput-constrained, so every hyperscaler's accelerator buildout drags a CPU buy along with it. The tension: demand has **doubled to over $2 billion** in three months, but the company is candid that supply chain (wafers, substrates, test capacity, memory) — not demand — is the binding constraint, and margins on the first-generation product are stuck in the high-30s/low-40s for years.

## Where they're going / what they're building
- The **Arm AGI CPU**, launched in March, is the strategic pivot from pure IP licensor to silicon vendor: initial product has already shipped to multiple customers, and demand has **more than doubled from $2 billion to "north of $2 billion"** in one quarter, with **confidence in beating the original $1 billion supply commitment increasing** over the past 90 days.
- Management is framing the addressable market aggressively upward: the TAM guidance given in March (**$100 billion+**) is now being dwarfed by peer estimates running to **$200-220 billion**, and Rene Haas argues this isn't hype — "agentic workloads are essentially capacity constrained in terms of throughput by the number of CPUs you have."
- The customer list spans all three sub-segments of the AI compute stack — head nodes (Cerebras, OpenAI), agentic/general-purpose server (Meta, Cloudflare), and cloud infrastructure (Oracle OCI) — with Haas stating plainly the AGI CPU "is a good fit for all of those."
- **Core count is the next product lever**: today's AGI CPU ships at 128 cores versus Graviton5's 192, and Haas signals more cores are coming because "for running agentic workloads, more cores is a better outcome" — fewer virtual machines per core, better throughput.
- Silicon revenue will get its own disclosure line once it clears 10% of total revenue, which Jason Child now expects to land in **fiscal 2028** — a tacit admission this business is about to become material enough to matter to the model.

## What's changing
- **Neoverse's growth curve is inflecting, not just growing**: it took six years to ship the first billion cores; the most recent 500 million shipped in nine months. Data center royalties **more than doubled year-over-year again**.
- IDC data cited by ARM shows spending on Arm-based accelerated server platforms has **nearly doubled in two quarters and now exceeds x86 platforms** — a genuine architecture shift in AI infra, not just a share-gain story.
- Every major hyperscaler is now visibly on the Arm compute path: NVIDIA's Vera in production (**50% higher CPU performance, 2x energy efficiency** vs. comparable x86), AWS deploying "tens of millions" of Graviton5 cores for agentic workloads, Microsoft's Azure Cobalt 200, and Qualcomm entering AI data center CPUs with Dragonfly C1000 — even a merchant-silicon company is now building Arm-based server chips.
- The licensing side is quietly propping up the headline growth number: **$193 million of the $574 million in license revenue this quarter came from a single SoftBank technology-licensing/design-services agreement**, expected to run at roughly $200 million/quarter going forward — a related-party, non-market revenue stream doing real work on the topline.

## What's NOT working (or being talked around)
- **Smartphone royalty guidance was quietly cut mid-call**: full-year royalty growth guidance moved from "around 20%" down to "high teens," and Q2 royalty growth is guided to just **low-to-mid teens** — a real deceleration Child attributes to memory-price-driven BOM inflation now hitting "even upper and mid-tier" phones, not just the low end as originally expected.
- **Gross margin on the AGI CPU stays weak for years**: high-30s to low-40s through fiscal 2028, with a path to 50% only after ARM brings in-house work currently done by an outside ASIC partner — "that'll probably take a couple of years." This is a low-margin hardware business layered onto a historically ~90%+-margin IP licensor, and management didn't dodge that math, just deferred the detail to Q3.
- When directly asked why ARM can't just secure supply for "only" $1 billion in a "$50 billion market," Haas didn't really answer the capacity question — he reframed it as "everyone" being supply constrained, including CPU makers with their own fabs, without naming a specific bottleneck component or a date it resolves.
- **Notably absent**: no mention of margin dilution's effect on consolidated non-GAAP operating margin as AGI CPU silicon revenue scales, no discussion of customer concentration risk in the AGI CPU pipeline (how much of that $2B+ is a handful of hyperscalers vs. broad-based), and no commentary on China export/geopolitical risk despite explicitly claiming "multiple customers in the U.S. and China."

## Street anxiety (compressed)
Where exactly is the incremental AGI CPU supply confidence coming from — wafers, substrates, memory, or something specific? · why can't a company with a "$50 billion" opportunity just buy more capacity, and is there a single-point-of-failure "golden screw" risk in the supply chain at the 11th hour? · does the CPU-only (no proprietary accelerator) position get squeezed out as NVIDIA/Google/Amazon increasingly co-design silicon in-house? · will the smartphone royalty guidance cut be a one-quarter blip or the start of a trend, and is licensing revenue (increasingly SoftBank-dependent) really a durable offset? · underlying worry: that the AGI CPU story is being sold on demand-side enthusiasm while the actual gating factor — supply, margin structure, and customer concentration — remains vague and pushed to "an update next quarter."
