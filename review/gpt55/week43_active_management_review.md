# Review: course/week43_active_management.md

## Overall Assessment

Week 43 is a valuable cold-shower lesson. The SPIVA and persistence framing is exactly what students need before taking active-management pitches seriously. It also fits SOUL's view that alpha is rare and must come from structural sources, not from generic stock-picking confidence.

The lesson needs terminology cleanup, source/date verification, and interactive-model caveats. The biggest presentation issue is that the lesson calls active alpha categories "four tranches," which conflicts with the course's existing four-tranche portfolio framework.

## Content Critique

- The opening pitch is excellent: active management sounds reasonable until the base rate is shown.
- SPIVA numbers should be source-labeled and date-checked. "April 2026 scorecard ending December 2024" sounds stale or inconsistent; a 2026 scorecard would normally include more recent periods if available.
- SPIVA methodology description is directionally right but should be precise about fund universes, benchmarks, survivorship adjustment, style consistency, and net-of-fee measurement.
- The statement that active "consistently wins" in liquid hedge funds and illiquid private credit is too broad, especially because the same sentence admits selection bias and mark-to-model issues.
- Persistence discussion is strong, but the 15% top-quartile persistence figure needs a source and vintage range.
- Survivorship bias section is useful and practical.
- The "four tranches that actually generate alpha" should be renamed "four structural alpha categories" or similar. They are not the same as the course's four-tranche portfolio framework.
- The four alpha categories are good: activism, quant/systematic, event-driven, CTA/macro. The lesson should distinguish accessible retail approximations from institutional capacity-limited strategies more sharply.
- The passive-share misconception should be reconciled with SOUL's passive-flow reversal-trigger view. The lesson can default to passive while still explaining the specific conditions under which passive dominance could become fragile.
- The three-year IR cutoff for a DIY active sleeve is sensible as a review discipline, but three years is a noisy sample; use it as a trigger for review, not an automatic verdict.
- DALBAR underperformance claims should carry the same methodology caveat noted in earlier reviews.

## Cross-Reference And Consistency Issues

- Week 42 previewed Week 43 as hedging strategies, but Week 43 is active management.
- Week 43 previews Week 44 as attribution; verify actual Week 44 before publication.
- "Four tranches" conflicts with the course-wide four-tranche framework.
- The passive-flow discussion should align with SOUL's principle that passive dominance can reverse only under specific structural triggers.

## Presentation Improvements

- Add a SPIVA methodology/source box.
- Add a persistence base-rate table: random expectation versus observed persistence.
- Rename alpha "tranches" to "categories" or "sources."
- Add a retail-accessibility column for each alpha source.
- Add a checklist for evaluating an active manager: fees, active share, factor exposure, capacity, team stability, tax drag, downside behavior, and benchmark fit.
- Add a clear distinction between gross alpha and net alpha.

## YouTube Script Critique

The script is watchable and has a clear argument. The "cold-shower week" framing works well.

Specific improvements:

- The interactive walkthrough says expense ratio 1%, gross excess 1.5%, so net 0.5%. The interactive label says excess return is net and the fee slider is not used in the calculation.
- Rephrase "SPIVA tail" as "right tail of active managers" so students do not think SPIVA itself endorses those strategies.
- Add Stella's skeptical question: "If passive keeps growing, doesn't that create alpha for active managers?"
- Add the SOUL-compatible answer: yes, maybe, but only under specific flow/liquidity/concentration triggers, not as a generic active-manager pitch.
- Avoid saying fund-of-funds and advisors mostly chase winners without nuance; it is vivid but broad.

## Chart And Visual Feedback

Existing visuals are useful:

- SPIVA underperformance chart.
- Persistence transition matrix.

Recommended upgrades:

- Add survivorship-bias funnel chart.
- Add fee drag compounding chart.
- Add alpha-source accessibility map.
- Add active manager evaluation checklist visual.

## Interactive Demo Feedback

The `week43_active_evaluator.html` interactive has a good purpose, but it needs fixes to avoid over-interpreting a p-value.

Issues and improvements:

- Expense ratio is not used in the metric calculation even though it is a main input. Either make excess return gross and subtract fees, or remove/rename the fee slider.
- The preset `Renaissance-class` uses fee and excess-return values beyond the slider max, which can create UI/state inconsistency.
- The label `P(luck, not skill)` overstates what a p-value means. It is a one-sided p-value under a zero-alpha null, not the true probability the manager has no skill.
- Add multiple-testing and selection-bias warnings. In a universe of thousands of funds, some will show low p-values by chance.
- Chart title says "5y" even when the years-observed slider changes.
- Add factor exposure / beta adjustment. Raw excess return over a benchmark is not always alpha.
- Add gross versus net toggle and fee compounding.
- Add active share and capacity controls.

## New Interactive Demo Ideas

- SPIVA base-rate simulator: thousands of zero-alpha managers and the right tail of lucky winners.
- Fee drag compounding calculator.
- Active-share and tracking-error map.
- Manager-selection checklist scorer.
- DIY sleeve benchmark tracker with IR and drawdown.

## Make It More Entertaining Without Watering It Down

The best hook is "the manager cemetery." Show 100 funds starting a 15-year race, then remove the closed/merged funds before showing the survivor average. That makes survivorship bias visceral.

## Money-Making Usefulness

This lesson can save students from fee drag and performance chasing. It also gives a useful standard: active sleeves need a structural source of return and honest benchmarking.

## SOUL Consistency Flags

- Strong alignment with SOUL's principle that alpha is rare and must be structural.
- Needs explicit alignment with SOUL's passive-flow reversal triggers.
- Rename the active alpha "four tranches" to avoid conflicting with the SOUL/course four-tranche framework.
