---
ticker: DDOG
call_date: 2026-02-10
report_quarter: 2026-Q1
period_reported: fiscal 2025-Q4
source: bronze/DDOG/2026-Q1/transcript-2026-02-10.md
generated: 2026-07-31 (automated silver pass, schema v3)
mentions: [AWS, MICROSOFT, GOOGLE, OPENAI, ANTHROPIC, MORGAN STANLEY, BARCLAYS, GOLDMAN SACHS, OPPENHEIMER, CIBC, JPMORGAN, RBC, BANK OF AMERICA, BERNSTEIN, JEFFERIES, STIFEL, GUGGENHEIM]
answers:
  economy: "Broad-based cloud migration demand accelerated across the whole customer base, not just AI-native names — David Obstler: ex-AI-native revenue growth accelerated to 23% y/y from 20% in Q3, with strength 'across customer size, spending bands, and industries,' and the trend continued into January."
  consumer: "No direct end-consumer read (B2B infrastructure vendor); the closest proxy is enterprise IT/engineering budget health, which looks robust — record $1.63B bookings, up 37% y/y, with 18 deals over $10M TCV."
  business: "Revenue hit $953M (+29% y/y, above guide high end), NRR ~120%, GRR mid-to-high 90s, and platform attach keeps deepening (18% of customers on 8+ products, up from 12% a year ago); APM reaccelerated into the mid-30s% range as its fastest-growing core pillar."
  investing: "OpEx grew 29% y/y as Datadog keeps scaling go-to-market headcount and R&D (400+ features shipped in 2025); capex/capitalized software guided to 4-5% of revenue for 2026, mostly funding platform build-out rather than new infrastructure categories."
  scarcity: "The binding constraint is go-to-market coverage and engineering velocity, not compute or capital — Olivier Pomel: the team is 'not at the scale we need to be in every single marketing segment... right now,' so 2026 investment is aimed at scaling GTM headcount while holding productivity, not chasing a supply-side bottleneck."
  forward: "Management believes AI-driven app proliferation will multiply system complexity and eventually push observability from post-hoc incident analysis to real-time, in-stream, preemptive detection — Pomel: a few years out, the winning model 'need[s] to be embedded into the data plane,' running specialized detection models on data as it flows, not summarizing after the fact."
  acting: "2026 guide bakes in continued heavy R&D and GTM investment (AI SRE agent, DevAgent, Security agent, MCP server, AI Agents console) and explicit go-to-market scaling ('you should expect more scaling from us on the go-to-market side'), but full-year revenue guide of 18-20% is a deceleration from Q4's 29%, reflecting stated conservatism rather than a demand read."
  hedges: "David Obstler declined to give AI-cohort revenue as a % of total ('we definitely haven't put it in there') and built the FY26 guide on an explicitly conservative assumption that the single largest customer's growth trails the 20%+ core — management repeatedly stressed they 'don't control' that customer's consumption trajectory."
  contradictions: "Management argues LLM-native anomaly detection (e.g., Anthropic's push into security/anomaly tooling) won't disintermediate Datadog because post-hoc LLM summarization can't match in-stream, data-plane-embedded detection — a bet against the crowd narrative that general-purpose LLMs erode specialized observability moats, made explicitly against a competitor (Anthropic) whose model they otherwise praise and expect to keep improving."
  street: "Analysts converged hard on one anxiety cluster: does agentic AI/LLM advancement erode Datadog's moat (build-it-yourself risk, LLMs as generic anomaly detectors, competitive share shifts from AI-native entrants) — plus a secondary thread on large-customer concentration and margin durability given aggressive reinvestment. Management's answer to nearly every AI-disruption question was the same pivot: LLMs are accelerants that grow the addressable surface, not substitutes, because value lives in context-assembly and in-stream data-plane execution — a well-rehearsed answer, but analysts kept re-asking it in different forms, suggesting they aren't fully bought in."
---

# DDOG — fiscal 2025-Q4 call (2026-02-10)

**The key idea:** Datadog closed 2025 with an inflection — the "boring" non-AI-native core business (23% growth) reaccelerating alongside continued AI-native outperformance, on the back of record bookings and the largest deals in company history. The real tension on the call wasn't growth, it was moat: can Datadog's value survive a world where LLMs get "significantly better every few months" and can plausibly do anomaly detection themselves? Management's answer — value shifts from writing code to validating it in production, and real-time in-stream detection beats post-hoc LLM summarization — was consistent but untested, and analysts kept probing it from different angles rather than accepting it at face value.

## The read — 3-5 points from the whole transcript
1. **The core business, not AI, drove the acceleration.** Ex-AI-native revenue growth went from 20% to 23% q/q with "broad-based strength across customer size, spending bands, and industries" — this is a real-economy signal about enterprise cloud/IT spend recovering broadly, not just an AI story.
2. **AI-native customers are now paying full freight, not experimenting.** An 8-figure land with "a leading AI model company" and a prior 8-figure deal with another major AI lab show frontier AI companies moving off homegrown/open-source observability once they hit production scale — Pomel: "the idea that it's cheaper to do it yourself is usually not the case."
3. **Consolidation is the dominant expansion motion.** Nearly every named deal (7 cited) involved replacing 5-30+ legacy/open-source tools with Datadog, several landing 17-19 products per account — this is a company winning via platform breadth and vendor fatigue, not point-product superiority.
4. **APM's reacceleration to mid-30s% growth is a genuine inflection**, driven by faster onboarding, DEM differentiation, and expanded go-to-market coverage — notable since APM had been "steady Eddie" historically.
5. **Guidance conservatism is structural, not a demand signal.** FY26 revenue guide of 18-20% sits well below Q4's 29% print and January's continued acceleration — David Obstler was explicit that this reflects discounting observed trends plus an unusually conservative assumption on their single largest (unnamed) customer's growth.

## Economy & consumer
- **Broad-based enterprise demand, not concentrated.** Diversification cited by industry, geography, and company size; 48% of Fortune 500 are now customers, yet median Fortune 500 ARR is still under $500K — "a very large opportunity for us to grow."
- **No consumer read** — Datadog sells to engineering orgs, not end consumers; omit from consumer lens.
- **Record bookings signal healthy IT capex appetite**: $1.63B in bookings, +37% y/y, with two deals over $100M TCV.

## The business — what's working, what's not
- **Three core pillars all crossed major thresholds**: infra monitoring >$1.6B ARR, logs >$1B ARR (FlexLogs nearing $100M ARR), APM/DEM >$1B ARR — all growing, with APM the standout at mid-30s%.
- **Platform depth keeps compounding**: 18% of customers now use 8+ products (up from 12%), 9% use 10+ (up from 6%) — but "about half of our customers do not buy all three pillars from us," still a large expansion runway.
- **Retention is rock-solid but not improving**: NRR flat at ~120% q/q, GRR "stable in the mid to high nineties" — a mature-but-healthy retention profile, not a growth lever.
- **What's not addressed**: no color on churn drivers, no update on gross margin trajectory beyond "plus or minus the 80% mark," and management wouldn't quantify AI-cohort revenue mix at all.

## Investing & scarcity
- **GTM headcount scaling is the primary 2026 investment**, not infrastructure or compute — Pomel: "we're still scaling the go-to-market team... not at the scale we need to be in every single marketing segment... right now."
- **R&D output stayed extremely high** (400+ features in 2025) while OpEx growth (29% y/y) roughly tracked revenue growth — indicating disciplined, not runaway, investment.
- **Capex/capitalized software guided to just 4-5% of revenue for 2026** — a light capital footprint relative to hyperscaler AI capex discussed on the call ($500B+ combined), underscoring Datadog's asset-light, software-margin model even as it rides the AI infrastructure wave.

## Where they think it's going vs what they're doing about it
- **Belief**: observability will move from human-driven post-hoc incident analysis to AI-agent-driven, real-time, in-stream, preemptive detection — Pomel: "you'll need to be proactive... you'll need to run detection and resolution before you have outages materialize."
- **Action**: AI SRE agent already GA (2,000+ customers ran investigations in one month), DevAgent and Security agent in development, MCP server in preview with explosive growth, AI Agents console "coming soon" — real product shipped, not just roadmap talk.
- **Gap flagged**: Pomel himself admits "we're not quite there yet" on the in-stream, data-plane-embedded vision — the flagship products (SRE agent) are still largely diagnostic/post-hoc rather than the preemptive, streaming architecture he describes as the multi-year differentiator. The rhetoric is ahead of the shipped capability.
- **Guidance mismatch as its own tell**: if management truly believed the AI-driven complexity wave was compounding as described, the FY26 guide (18-20%) sitting well below the trailing quarter (29%) and January trend reads as pure conservatism layered on top of genuine bullishness, not a change in belief.

## Hedges — what they wouldn't commit to
- **Declined to size the AI-native cohort as % of revenue** despite disclosing customer counts (650 AI-native customers, 19 spending $1M+) — a real disclosure gap given how much airtime AI-native growth got.
- **Explicitly conservative on largest customer's 2026 trajectory**, stating plainly "we essentially don't control that" in their consumption-based model — an acknowledged blind spot in their own guide.
- **No committed timeline for the in-stream/data-plane detection vision** — described as "a few years from now" with no product milestone attached.
- **Declined to frame hyperscaler CapEx ($500B+) as translating into a predictable observability revenue ramp** — Pomel called it "reductive" to map CapEx directly to LLM observability revenue, an unusually humble non-answer from a management team that otherwise leans bullish.

## The street — what analysts asked
- **Dominant anxiety: does agentic AI erode Datadog's moat?** Multiple analysts (Morgan Stanley, Goldman Sachs, CIBC, Bernstein) asked variations of whether LLMs enable customers to build homegrown observability, whether general-purpose models become anomaly-detection substitutes, and how competition shifts as AI-native entrants and even Anthropic push into adjacent territory.
- **Secondary theme: customer concentration risk.** Analysts pressed on the size and growth durability of the largest AI customer and whether AI-cohort revenue is dangerously concentrated — management repeatedly stressed diversification (650 names, 14 of top 20 AI-native companies as customers) without giving the underlying revenue number.
- **Tertiary theme: margin durability under reinvestment.** Questions on whether AI-native customers dilute gross margin and whether the mid-20s historical operating margin returns — management held the line at "plus or minus 80%" gross margin and framed margin as growth-first, investment-second.
- **What got dodged**: the AI-cohort % of revenue (twice asked, twice declined) and any firm timeline for translating hyperscaler CapEx into Datadog revenue. Compressed worry: *analysts aren't worried about current growth — they're worried that Datadog's AI moat story is a promise about 2028, resting on 2026 evidence that's still mostly qualitative.*
