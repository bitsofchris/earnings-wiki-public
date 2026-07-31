---
ticker: IBM
call_date: 2026-04-22
report_quarter: 2026-Q2
period_reported: fiscal 2026-Q1
source: bronze/IBM/2026-Q2/transcript-2026-04-22.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [RED HAT, CONFLUENT, DATASTAX, HASHICORP, WATSONX, NVIDIA, ARM, SERVICENOW, VISA, NESTLÉ, NATWEST, RBC, CLEVELAND CLINIC]
answers:
  economy: "Middle East saw strongest growth in decades; Europe strong with no deal slowdown observed. Only flagged risk is a speculative energy impact from Straits closures, not yet materializing."
  business: "Software +8% (Data +16%, Red Hat accelerated to 10%), infrastructure +12% with Z up 48% on z17 momentum, consulting a soft +1% though signings returned to growth (+6%). Segment margins expanded broadly except consulting, which dipped on currency and reinvestment."
  investing: "$10.5B deployed on acquisitions (mainly closing Confluent), CapEx stepping up, and Arvind says richer M&A appetite is opening once Confluent is integrated and cash rebuilds — \"maybe we can do something in the second half.\""
  scarcity: "Memory/supply-chain cost inflation is hitting storage and distributed infrastructure and being watched in RHEL (tied to hardware placements), though Jim calls the overall impact \"de minimis\" given IBM's mainframe-weighted, human-capital/IP-heavy mix."
  forward: "Management believes AI value concentrates in data/orchestration/governance layers, not the interaction layer, and expects mainframe to gain a durable \"third\" AI-inferencing workload alongside classic MIPS and Linux MIPS."
  acting: "Reaffirmed guidance (5%+ revenue, ~$1B FCF growth) despite a beat, upgraded software guide to 10%+ on early Confluent close, and shipped concrete AI infrastructure (Spyre Accelerator, Sovereign Core, Bob GA, AI editions of Db2/Cognos/MQ) rather than just messaging AI."
  hedges: "Explicitly declined to raise full-year guidance despite a strong beat — Jim invoked last year's pattern of building confidence early then \"blowing through\" free cash flow targets by Q4, and Arvind called the Middle East/Europe strength real but flagged Strait-closure energy risk as unconfirmed and speculative."
  contradictions: "Reported software deceleration (11%→8% headline growth) is framed as a mix artifact of transactional revenue timing, not weakening — annuity ARR growth is said to be accelerating underneath the same print, an assertion investors were visibly skeptical of given the string of pointed questions on it."
  street: "Recurring theme: is the software deceleration real or a mix illusion (asked twice, in different words); is macro deterioration behind the guidance conservatism; how memory/supply-chain inflation bites margins; how mainframe AI inferencing actually monetizes. Compressed worry: are IBM's growth numbers as clean as management insists, or is caution about guidance itself the tell."
---

# IBM — fiscal 2026-Q1 call (2026-04-22)

**The key idea:** IBM posted its strongest Q1 in over a decade — 6% revenue growth, double-digit software, record Z mainframe growth — while conspicuously refusing to raise full-year guidance. The tension of the call is credibility: management insists the beat is durable (mix-driven, annuity-backed, AI-tailwind-fueled) even as the reported software growth rate ticked down and Jim Kavanaugh openly cited last year's pattern of early-year confidence evaporating into a Q4 free-cash-flow miss.

## The read — 3-5 points from the whole transcript
1. **Mainframe is becoming an AI inference platform, not just a transaction engine.** Arvind describes a "third kind of compute capacity" beyond classic and Linux MIPS: running 20-30B parameter models in-line on every transaction instead of sampling 10% off-platform for fraud checks. A fully populated system can do "about 450 billion inferences a day," and clients using watsonx Code Assistant for Z are "growing MIPS capacity 3x faster."
2. **Guidance conservatism is deliberate, not a demand signal.** Despite a beat, IBM held guidance flat. Jim's own framing invites scrutiny: "dial back a year ago, same call, same question... we executed well. We took up free cash flow throughout the year, and then we blew through it in the fourth quarter." That's a candid admission that Q1 optimism has historically not held.
3. **Software's growth optics are mix, not deceleration, per management.** The 11%→8% headline drop is attributed entirely to the transactional-vs-annuity mix shifting quarter to quarter (Q4 ~30% transactional vs Q1 ~10%), with annuity ARR "approaching $25 billion... up 10%" said to be accelerating underneath. Two separate analysts pressed on this almost identically — a sign the street isn't fully buying the explanation on the surface print alone.
5. **M&A appetite is reopening post-Confluent.** Arvind: valuations are attractive but sellers haven't accepted the new baseline yet; IBM wants Confluent fully integrated first, but "second half, if things stay where they are... maybe we can do something."

## Economy & consumer
- **Middle East hit a multi-decade high**, per Arvind: "the strongest growth we have seen in decades, not years, decades" — enterprises and governments there are moving deliberately on tech investment, not retrenching.
- **Europe strong with zero observed deal slippage**: "There is nothing in what has already transpired. There has been no slowdown in deals."
- **The one flagged macro risk is speculative, not observed**: prolonged Strait closures could bring European energy impacts, but "that is not what we are seeing" today.
- No direct consumer-facing exposure — IBM sells to enterprises and governments, so this section is enterprise-IT-capex proxy rather than end-consumer read.

## The business — what's working, what's not
- **Z mainframe had a record quarter, up 48%**, with new MIPS shipments over 100% growth for four straight quarters — Jim ties this to a 3x-4x software/services "stack multiplier" per hardware dollar landed.
- **Data (+16%) and Red Hat (accelerated to 10%)** are the clear software winners; OpenShift crossed **$2 billion ARR**, virtualization has booked **over $600 million** in contracts since 2024.
- **RHEL is the one soft spot flagged inside software** — deceleration tied to "the federal lack of signings and the closure of the government" plus a "dislocated hardware supply chain market," an area Jim says they're actively monitoring.
- **Consulting remains the laggard at +1% revenue**, though signings snapped back (+6%) and GenAI now represents **about 30% of backlog**, with **400 new clients** captured in the quarter — a leading indicator management leans on to justify the "low to mid-single digit" full-year consulting guide.
- **Free cash flow hit $2.2B, up 13%, the best Q1 in a decade** by both absolute and margin measures — but management is careful to frame this as "less than 15% of what's required for the year."

## Investing & scarcity
- **Confluent closed early (~2 months ahead of plan)**, absorbing **~$600M of dilution** in 2026 from stock comp and interest expense, but data segment guidance was raised to "low 20%+" for the year on the back of it.
- **CapEx and net interest expense are rising as expected headwinds** to free cash flow, alongside higher cash taxes — all previously flagged, none new.
- **Memory and supply-chain cost inflation is real but contained**: Jim calls it "de minimis" at the IBM level given the mix (75-80% human-capital/IP business), though it touches storage, distributed infrastructure, and indirectly RHEL through hardware placement cycles. No mention of GPU scarcity specifically — notable, since IBM sells adjacent AI infrastructure (Spyre, Nvidia-accelerated watsonx.data) without describing any compute constraint of its own.

## Where they think it's going vs what they're doing about it
- **Belief**: value in the AI stack settles in data/governance/orchestration, not the "interaction layer," because agents will interact with underlying data and business logic more than with people. **Action**: Confluent acquisition (real-time governed data streaming), watsonx Orchestrate, AI editions of Db2/Cognos/MQ — concrete product bets matching the thesis, not just messaging.
- **Belief**: sovereignty and workload-control will matter increasingly given geopolitics ("infrastructure no one can turn off or tamper with"). **Action**: launched Sovereign Core this quarter — a direct, dated product response.
- **Belief**: mainframe inferencing is a large new monetization vector. **Action**: quantified capacity (450B inferences/day) and cited financial-services fraud-detection savings "in the tens of millions," but full monetization is still described as multi-year ("play out 2026 and 2027") — the action is shipped (Spyre, Z17 capacity) but the revenue realization is forward-looking, not yet booked at scale.
- **Gap to flag**: management professes confidence in accelerating trends across every segment, yet explicitly won't raise guidance — the strongest visible gap between stated belief ("strong start," "more optimistic than 90 days ago") and committed action (holding numbers flat).

## Hedges — what they wouldn't commit to
- **Declined to raise full-year guidance** despite a clear beat on revenue, EPS, and free cash flow — citing only "three months of the year" and explicitly recalling last year's pattern of early strength giving way to a Q4 free-cash-flow shortfall.
- **Wouldn't commit to a Strait-closure macro call** either way — framed as speculative optionality ("if the Straits stay closed for another few weeks... but that is not what we are seeing") rather than a forecast.
- **M&A appetite is stated as directional, not committed** — "maybe we can do something in the second half," explicitly conditioned on valuations holding and cash rebuilding.

## The street — what analysts asked
- **Software growth optics dominated**: two separate questioners pushed on the 11%→8% sequential deceleration, wanting to know if it's mix or a real slowdown — management's mix explanation was consistent but repetition of the question suggests it wasn't fully landing.
- **Guidance conservatism given the beat**: pointed questions on whether Europe or Straits-related macro risk is the real reason IBM won't raise numbers; management answered with reassurance but no new data beyond "no slowdown in deals."
- **Mainframe AI monetization mechanics**: detailed questions on how inferencing workloads translate into dollars, answered with hardware/software stack-multiplier math (3x-4x) and shipped-MIPS growth stats.
- **Supply chain/memory cost exposure**: asked directly, answered as contained/de minimis with RHEL flagged as the one watch item.
- Compressed one-sentence worry: **is IBM's growth as clean and durable as management insists, or is the refusal to raise guidance itself the most honest number on the call.**
