---
ticker: ARM
call_date: 2026-02-04
report_quarter: 2026-Q1
period_reported: fiscal 2026-Q3
source: bronze/ARM/2026-Q1/transcript-2026-02-04.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [SOFTBANK, AWS, NVIDIA, MICROSOFT, GOOGLE, ALPHABET, MEDIATEK, RIVIAN, TESLA, QUALCOMM, GROK]
answers:
  economy: "No macro commentary beyond semiconductor-specific dynamics; CEO frames AI infrastructure spend as historically unprecedented, citing Alphabet's $180B CapEx as bigger than what "semiconductor companies used to spend on fabs... times a few.""
  consumer: "Not a direct consumer-facing business, but memory/DRAM supply constraints are expected to compress low-end smartphone unit volumes (MediaTek flagged ~15% next-year reduction); ARM says OEMs are protecting the premium/flagship tier where its highest royalty rates sit."
  business: "Fourth straight >$1B quarter, revenue +26% YoY to $1.24B; royalties hit a record $737M (+27%) on data center strength (>100% YoY growth) and rising smartphone royalty rates; licensing +25% to $505M, boosted by a $200M full-quarter SoftBank contribution (up from $178M pro-rated last quarter)."
  investing: "OpEx +37% YoY to $716M on R&D headcount expansion for next-gen architectures, compute subsystems (CSS), and new chiplet/SoC exploration; CFO signals R&D sequential growth will moderate somewhat after Q1 fiscal '27 versus this year's steep step-ups."
  scarcity: "Memory/DRAM supply chain constraints are the binding near-term constraint on low-end smartphone volumes, but management sizes the royalty impact at just 1-2% company-wide since flagship/CSS-tier devices are insulated; power/battery-life constraints remain the persistent design constraint driving CPU efficiency demand."
  forward: "Data center business expected to become ARM's largest segment (surpassing mobile, currently ~40-45% of revenue) within a few years; CSS could reach ~50% of royalty mix in 2-3 years, up from "into the teens" today; fiscal '27 royalty growth framed as "pretty consistent" with prior 20%+ expectations despite tougher comps."
  acting: "Reorganized into three business units (Edge AI, Physical AI, Cloud AI) to mirror how AI workloads deploy; signed two new CSS licenses and two new Total Access Agreements this quarter; hosting a March 24 product event that management explicitly declined to preview."
  hedges: "Declined to give fiscal '28 guidance ("stay tuned... something we're working through"); dodged whether SoftBank's AI roadmap will yield an ARM custom ASIC ("nothing we can say specific about any products"); would not quantify data center revenue in dollars, only "teens to closer to 20%" of total."
  contradictions: "CEO insists memory/BOM pressure has not slowed CSS/v9 adoption ("we've really not had many discussions with anyone regarding the BOM impact") even as the same call spends multiple answers quantifying memory-driven unit risk — a tension between "no impact on pricing power" and "real impact on volumes.""
  street: "Analysts clustered on three anxieties: (1) memory/DRAM shortage bleeding into smartphone unit and royalty forecasts, (2) whether SoftBank might need to sell ARM shares to fund its AI buildout (flatly denied, quoting Masayoshi Son directly), and (3) parsing why royalty growth decelerates into Q4/FY27 guidance despite record beats — largely a comp/seasonality story, not demand softening."
---

# ARM — fiscal 2026-Q3 call (2026-02-04)

**The key idea:** ARM posted a record quarter almost entirely on the strength of two structural trends — CSS-driven royalty-rate escalation in premium smartphones and explosive, share-gaining growth in data center CPUs tied to agentic AI inference. The tension on the call is that a real near-term headwind (DRAM/memory scarcity hitting low-end smartphone volumes) is being talked down as immaterial, even as management spends several answers carefully quantifying and bounding exactly that risk.

## The read — 3-5 points from the whole transcript
1. **Data center is becoming the company.** Data center royalty revenue "grown more than 100% year on year," and management now expects it to overtake mobile (~40-45% of revenue) as ARM's largest segment within two to three years — a full architectural bet described directly by the CEO: "we expect in a few years our data center business to be our largest business, larger than mobile."
2. **CSS is the royalty-rate engine, not just a licensing product.** 21 CSS licenses across 12 companies, five already shipping, and the top four Android vendors all shipping CSS silicon; CFO expects CSS to reach "upwards of 50%" of royalty mix in a few years, up from "into the teens" now, driven purely by faster time-to-market value, not price cutting.
3. **Memory scarcity is a real but bounded headwind, and management is transparent about the math.** CFO walks through the arithmetic live: a 20% unit reduction translates to "somewhere around a 2% to 4% at worst" hit to smartphone royalties and "1%, maybe 2%" company-wide — because the shortage falls hardest on legacy v8 chips, not the CSS/v9 premium tier ARM actually monetizes.
4. **Agentic AI is reframed as a CPU story, not just a GPU story.** The CEO's core pitch: "agent-based AI requires coordination across many agents running continuously, and... the CPU can only do coordination," which is why hyperscaler core counts are climbing sharply (Graviton5 to 192 cores, Vera to 88 cores, Cobalt 200 to 132 cores) — a genuine architectural shift, not just a marketing frame.
5. **SoftBank concentration is large and now a recurring, defended topic.** SoftBank licensing alone contributed $200M of the $505M license line this quarter (a full-quarter run-rate up from a partial $178M last quarter); CEO directly quotes Masayoshi Son denying any intent to sell "one share... any shares" of ARM stock, addressing dilution/overhang speculation head-on.

## Economy & consumer
- **No broad macro read** — ARM doesn't comment on the general economy; its closest lens is semiconductor supply chain and end-device demand.
- **Memory scarcity is the proxy for "consumer" here.** MediaTek's flagged ~15% unit reduction next year and ARM's own analysis converge; OEMs are said to be protecting premium/flagship volumes at the expense of the low end, which happens to be where ARM earns the least anyway.
- **CEO ties the AI capex wave to broader market jitters.** Referencing Alphabet's $180B CapEx announcement the same day, Haas frames current equity-market anxiety around software/AI spend as understandable given the scale: "That used to be what semiconductor companies just spent a year on fabs. Times a few. So we're in uncharted waters."

## The business — what's working, what's not
- **Working: royalties at a record $737M (+27% YoY)** on "record units" plus higher per-chip royalty rates — the CSS/v9 pricing escalator compounding with volume.
- **Working: licensing +25% YoY to $505M**, with ACV growth holding at 28% YoY for a third straight quarter, "above our long-term expectation of mid to high single-digit growth."
- **Not working / cost pressure: non-GAAP OpEx +37% YoY to $716M**, outpacing revenue growth, driven by R&D headcount tied to CSS, chiplets, and full-SoC exploration — margin (41% non-GAAP operating margin) held up this quarter but growth is clearly being bought with heavier spend.
- **Licensing lumpiness flagged explicitly by CFO**: the $200M SoftBank contribution this quarter is "just a full quarter impact" of a deal signed prior quarter, not new business — a reminder the license line is deal-timing driven and shouldn't be read as organic acceleration.

## Investing & scarcity
- **R&D investment is the visible capital allocation lever** — engineering headcount expansion into CSS, next-gen architectures, and new chiplet/SoC categories; CFO signals the pace of sequential OpEx step-ups will moderate somewhat after fiscal Q1 '27 versus this year's aggressive ramp.
- **The real constraint is memory supply, not compute demand.** Management is explicit that demand for ARM's IP is not the binding constraint anywhere in the business ("we don't have that problem" of running out of hard problems); DRAM/memory availability constraining device OEMs' unit volumes is the actual scarcity bottleneck this quarter.
- **Power efficiency is the perpetual design constraint**, described by the CEO as something the company addresses "twenty-four seven" — battery life and thermal/power envelopes shape every product decision from smartphones to robotics.

## Where they think it's going vs what they're doing about it
- **Belief: CPUs become more, not less, important as inference goes agentic.** Action backing it: reorganization into Edge/Physical/Cloud AI business units explicitly mirrors this belief, and R&D dollars are flowing into CSS and custom SoC/chiplet capability to capture higher-core-count designs.
- **Belief: data center overtakes mobile as the largest segment within 2-3 years.** Action backing it: heavy R&D reinvestment despite margin compression this quarter — a real financial commitment, not just rhetoric.
- **Belief vs. action gap: fiscal '28 outlook.** Management repeatedly says growth opportunity is expanding ("huge opportunity... in the new areas of physical AI, cloud AI, and edge AI") but explicitly declines to commit to any numbers beyond next fiscal year, and dodges the SoftBank custom-ASIC question entirely — the confidence in the narrative outruns what they'll put a number or specific product commitment behind.

## Hedges — what they wouldn't commit to
- **No fiscal 2028 guidance** — CFO: "we haven't thrown anything out there yet... stay tuned."
- **No details on the March 24 event** despite teasing it themselves — CFO preemptively deflected: "there'll be a million ways of asking what we may or may not be announcing... we won't be providing any details ahead of the event."
- **No confirmation or denial on a SoftBank custom ASIC** despite the $200M/quarter NRE relationship being directly probed.
- **No precise data center dollar figure** — only disclosed once a year, described in ranges ("teens to probably getting closer to 20%") rather than a hard number.

## The street — what analysts asked
- **Memory/DRAM shortage impact on smartphone royalties** dominated multiple questions — analysts pushed for quantification and got a detailed, bounded answer (1-2% company-wide impact) rather than a dodge, one of the more transparent moments on the call.
- **SoftBank overhang and share-sale risk** was asked directly and answered with an unusually direct on-record denial quoting Son personally — signals this is a live investor concern the company felt needed a strong rebuttal.
- **Deceleration in royalty growth guidance despite record beats** drew repeated follow-ups; management's consistent answer was tough comps and one-time prior-year MediaTek timing, not softening demand — plausible, but analysts clearly wanted more conviction than "we'll see if this recent strength continues."
- **Compressed worry:** is ARM's data-center/CSS growth strong enough to keep outrunning a real, if modest, memory-driven mobile volume headwind — and is management's confidence in that outrun backed by anything more than reassurance?
