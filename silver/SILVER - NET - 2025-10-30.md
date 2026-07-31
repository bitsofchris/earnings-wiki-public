---
ticker: NET
call_date: 2025-10-30
report_quarter: 2025-Q4
period_reported: fiscal 2025-Q3
source: bronze/NET/2025-Q4/transcript-2025-10-30.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [ORACLE, OCI, COINBASE, VISA, MASTERCARD, AMERICAN EXPRESS, GOOGLE, CHROME, NETSKOPE, ZSCALER, IETF, NIST, ANTHROPIC, MICROSOFT, CHATGPT]
answers:
  economy: "No macro commentary — the call is framed entirely around company-specific execution and the AI platform shift, not broader demand conditions."
  business: "Revenue grew 30.7% YoY to $562M, accelerating for a second straight quarter; large-customer (>$100K) count up 23% YoY now 73% of revenue; net retention jumped to 119% (+5pp QoQ) as pool-of-funds contracts get consumed. Gross margin held at 75.3%, within the 75-77% long-term range but down 350bp YoY as free/paid traffic mix shifts costs into COGS."
  investing: "Network CapEx ~14% of revenue (guided ~13% for FY25); the buildout philosophy is explicitly demand-following, not demand-anticipating, using a global 'scheduler' that shifts load to wherever idle capacity exists rather than pre-provisioning like hyperscalers."
  scarcity: "Not compute or capacity — CEO explicitly denies being capacity-constrained; the binding constraint is GPU utilization efficiency (still well below the 70-80% they've squeezed from CPUs) and enterprise sales capacity, which they're actively rebuilding after a multi-year revamp."
  forward: "Management believes AI is a full information-consumption platform shift that will replace the 'create content, drive traffic, sell ads' Internet business model with agent-mediated commerce, and that ~80% of leading AI companies already route through Cloudflare's network as a structural moat."
  acting: "Building NET Dollar as an agent-to-agent payment rail while explicitly hedging across other protocols (X402/Coinbase, Visa, Mastercard, Amex, MCP); expanding a Pay Per Crawl program to monetize AI scraping for media/publisher customers; shifting go-to-market from product-led growth to enterprise sales and doubling down on channel/partner selling for SASE after 'forehead-slapping' realization that Netskope does 95% of sales through channel."
  hedges: "CFO declined to confirm CJ Desai's destination company; management said the future business model of agentic commerce is unknown ('I don't know what the future business model of the Internet will look like') and deliberately avoided going all-in on any single payments protocol or standard."
  contradictions: "Claims zero capacity constraint despite last year's stated plan to double network capacity — framed as investment discipline rather than a walk-back, but the tension between 'doubling capacity' and 'never capacity constrained' goes unaddressed."
  street: "Analysts probed RPO acceleration (43% YoY, best since 2022) and pool-of-funds mechanics, sales productivity durability, AI-native customer concentration risk, competitive dynamics in inference/SASE, and the abrupt CEO-level executive departure — with a recurring undertone of 'is this growth durable or one-time catch-up.'"
---

# NET — fiscal 2025-Q3 call (2025-10-30)

**The key idea:** Cloudflare posted a second straight quarter of accelerating growth (30.7% YoY) and is repositioning itself as the toll booth and translator for an "agentic Internet" — new payment rails (NET Dollar), AI crawler monetization (Pay Per Crawl), and a claim that 80% of leading AI companies already sit behind its network. The subtext is a company mid-transition from product-led growth to enterprise sales, losing its product chief to a rival CEO seat mid-call, while insisting none of this changes the trajectory toward $5B run-rate by Q4 2028.

## The read — 3-5 points from the whole transcript
1. **Growth reacceleration is real and enterprise-driven, not macro-driven.** Revenue growth ticked up for the second consecutive quarter to 31% YoY, RPO grew 43% YoY (best since 2022), and net retention jumped 5 points to 119% — CFO Thomas Seifert attributed this explicitly to "customer quality and platform expansion," not any external tailwind. Large customers (>$100K) now drive 73% of revenue.
2. **CJ Desai's exit was announced live on the call**, poached to be CEO of an unnamed public tech company — the second product leader Cloudflare has lost to a CEO role. Prince framed it as validation ("we can't say yet where you're going, but they're lucky to have you") but it's a real leadership gap during a critical go-to-market transformation.
3. **Cloudflare is betting its infrastructure position translates into an AI-commerce toll position.** The NET Dollar initiative, Pay Per Crawl, and "we support every protocol" positioning (MCP, X402, Visa, Mastercard, Amex) reveal a company hedging heavily on which agentic-payment standard wins while trying to sit in the middle of all of them.
4. **The "not capacity constrained" claim sits awkwardly next to last year's promise to double network capacity** — Prince insists Cloudflare invests strictly behind demand via a global workload scheduler that shifts free/low-tier customers to underutilized capacity, reserving prime capacity for large customers, but never squares this with the year-ago capacity-doubling commitment.
5. **Gross margin eroded 350bp YoY** (still within the 75-77% target band) as free-to-paid traffic mix and Workers' relatively lower current margins pull cost allocation — a real trade-off from chasing developer-platform and AI-inference growth that management frames as temporary until Workers "gets better and better over time."

## Economy & consumer
No consumer-facing commentary; Cloudflare is B2B infrastructure. No macro-demand framing was offered anywhere in the call — an absence worth flagging, since most infra vendors give at least a line on enterprise IT budget conditions and Cloudflare gave none, instead attributing all momentum to internal go-to-market execution.

## The business — what's working, what's not
- **Working:** Sales productivity rose for a seventh consecutive quarter, close rates "ticked up notably," partner-initiated bookings **doubled YoY**, and the largest customer cohorts (>$1M, >$5M annual spend) hit **record net adds for the fourth consecutive quarter**.
- **Working:** Paying customers hit a **record net add of ~30,000 in a single quarter**, up 33% YoY, boosted by free-to-paid graduation around AI Week and Birthday Week product launches.
- **Not working / cost pressure:** Gross margin down 100bp sequentially and 350bp YoY to 75.3%, driven by rising paid-vs-free traffic mix pushing more cost into COGS — Seifert calls the "unit economic margin... very consistent" but the headline number is still eroding.

## Investing & scarcity
- **CapEx stays lean and reactive:** Network CapEx ran ~14% of revenue this quarter, guided to ~13% for full-year 2025 — Prince explicitly contrasts Cloudflare's model ("invest behind demand, not ahead of demand") against hyperscalers' pre-provisioning economics, using off-the-shelf hardware to deploy fast in Tier 1 cities "even before we start to pay for the equipment" (Seifert).
- **The real scarce resource is GPU utilization, not GPU count:** CPUs already run at 70-80% utilization after 15 years of optimization; GPUs are "well below" that today, and management describes "speed running" the same multi-tenancy and model-swap efficiency work Cloudflare did for CPUs — implying GPU economics, not GPU supply, is the current bottleneck.
- **AI-native customer concentration is explicitly capped and disclosed:** Seifert clarified "de minimis" means **no single customer exceeds 2% of revenue** — a direct, quantified answer to a concentration-risk question that's unusually transparent for this stage of an AI capex cycle.

## Where they think it's going vs what they're doing about it
- **Belief:** Prince argues AI is a platform shift on the order of desktop→mobile→social, that "human eyeball traffic is unlikely to be the currency of the Internet's future," and Cloudflare will "help shape" the rules of an agentic Internet because most AI traffic already routes through it.
- **Action backing the belief:** Concrete signed deals point at monetizing exactly this thesis — a **$22.8M** media-platform contract explicitly won on Pay Per Crawl positioning, a **14-month $1.2M** AI Crawl Control/Bot Management deal, and active NET Dollar / X402 / card-network partnerships.
- **The gap:** Despite the sweeping "agentic Internet" rhetoric, Prince repeatedly declines to commit to any single protocol or currency ("we're not all in on any one of these things"), and the actual dollar contribution from AI-specific products remains, by their own description, "relatively de minimis" — the vision is far ahead of the current revenue reality, which management itself acknowledges.

## Hedges — what they wouldn't commit to
- **Would not name CJ Desai's destination company**, despite reporters clearly knowing enough to ask — "We can't say yet where you're going."
- **Would not pick a winning agentic-payments standard**, spreading bets across NET Dollar, X402/Coinbase, and the major card networks simultaneously rather than committing capital to one rail.
- **Would not forecast the future Internet business model**, with Prince stating plainly: "I don't know what the future business model of the Internet will look like, who the winners and losers will be" — an unusually direct admission of uncertainty embedded inside otherwise bullish framing.

## The street — what analysts asked
Analyst questions clustered around three anxieties: (1) **durability of the growth reacceleration** — RPO's 43% YoY jump, pool-of-funds consumption mechanics, and whether sales-productivity gains are a one-time catch-up or a sustainable trend; (2) **AI exposure and risk** — customer concentration in AI-native accounts, capacity strategy versus stated capacity-doubling plans, and competitive dynamics for inference workloads against hyperscalers; (3) **leadership continuity** after the CJ Desai departure was dropped live on the call. Nothing was overtly dodged, but the capacity-constraint question got a philosophy lecture rather than a hard capacity-utilization number, and the "de minimis" AI concentration answer was volunteered only after direct probing. Compressed worry: **is this quarter's acceleration structural, or is Cloudflare front-loading a sales/product cycle right before losing the executive who built its product-engineering credibility?**
