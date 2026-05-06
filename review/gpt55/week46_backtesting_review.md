# Review: course/week46_backtesting.md

## Overall Assessment

Week 46 is a strong and necessary lesson. It gives students the right instinct: most backtests are optimistic, and the burden of proof belongs to the strategy seller. The survivorship, look-ahead, cost, multiple-testing, walk-forward, and regime sections fit naturally after Week 45.

The lesson needs terminology consistency around deflated Sharpe, several source/factual checks, and alignment between the reading, script, and interactive. The largest issue is that "deflated Sharpe" is used sometimes as a probability and sometimes as a Sharpe point estimate.

## Content Critique

- The opening is engaging and correctly skeptical.
- The claim that median published in-sample Sharpe roughly halves out of sample should be sourced.
- "Deflated Sharpe is now the institutional standard" is too broad. It is respected and useful, but not universally required by allocators.
- Survivorship-bias explanation is good, but "any data terminal" is too broad; professional platforms can provide historical constituents if configured correctly.
- The AAPL restatement example has a likely date error. Apple's FY2024 10-K would not normally be filed in November 2025; this should be corrected or replaced with a real restatement example.
- The cost arithmetic is clear and valuable.
- Cost estimates should be harmonized with Week 44. Week 46 table says SPY/QQQ are 1-3 bps, but the script later says 10 bps is realistic for SPY.
- The multiple-testing example is useful, but the expected count above Sharpe 3 in 1 year of daily zero-edge data should be checked. Under a standard normal approximation, 1000 trials gives about 1-2 above 3, not 3.
- The DSR formula is presented as a probability, but later Q&A uses "deflated Sharpe below 0.7" as if it were a Sharpe point estimate. Pick one convention.
- The simplified expected-max formula should be explicitly labeled as an approximation.
- Walk-forward is correctly emphasized, but "kills overfitting" should be softened to "reveals or reduces overfitting." The misconception section already says it does not eliminate it.
- The rule "walk-forward Sharpe less than half in-sample Sharpe means overfit" is useful as a warning, but too absolute as a diagnosis. Regime change, cost errors, or genuine decay can also explain it.
- Q3 uses "retail traders" instead of repository-preferred "retail investors."
- Q12's `L4 opportunity sleeve` should match the course's established terminology exactly, likely `opportunistic sleeve` if that is the canonical wording.

## Cross-Reference And Consistency Issues

- Week 45 script previews Week 46 as a hedge-fund track-record dissection, but Week 46 is backtesting.
- Week 46 previews Week 47 as tail risk; verify actual Week 47 before publication.
- Week 44 and Week 46 transaction-cost assumptions need to be reconciled.
- Week 45 and Week 46 should use the same multiple-testing/deflated-Sharpe definitions.

## Presentation Improvements

- Add a compact "backtest error budget" table: survivorship, look-ahead, costs, multiple testing, regime selection, implementation gap.
- Add source notes for survivorship bias magnitude, OOS Sharpe haircut, cost assumptions, and DSR formula.
- Add a terminology box: raw Sharpe, probabilistic Sharpe ratio, deflated Sharpe ratio, deflated Sharpe point estimate.
- Replace hard deployment thresholds with decision bands and sizing guidance.
- Add a point-in-time data checklist.

## YouTube Script Critique

The script is energetic and should hold attention. The topic is naturally dramatic, and the "single most persuasive / overrated document" hook works.

Specific issues:

- Speaker labels use all caps (`HORACE`, `STELLA`) rather than the usual `**Horace:**` / `**Stella:**` style.
- The script says 10 bps is realistic for SPY; the reading says SPY/QQQ/top mega-caps are 1-3 bps.
- "Every retail quant influencer's daily algorithm is a scam" is too inflammatory. Keep the edge, but let the arithmetic do the work.
- The script says a one-year Sharpe 2 strategy has `t-stat three`; annualized Sharpe 2 over one year is closer to t-stat 2.
- The interactive examples should be recalculated from the actual code. The "good case" likely produces a probability much higher than 90% under the current model.
- The deployment threshold `deflated Sharpe above 0.7 OOS` should be clarified as either a Sharpe value or a probability.

## Chart And Visual Feedback

Existing visuals are strong:

- Cost drag chart.
- Random-strategy Sharpe histogram.

Recommended upgrades:

- Add a survivorship-bias before/after universe visual.
- Add a look-ahead timeline for signal date, data availability date, and execution date.
- Add a walk-forward train/test rolling window diagram.
- Add a regime robustness heatmap.

## Interactive Demo Feedback

The `week46_backtest_validator.html` interactive is useful but needs clearer statistical labeling.

Issues and improvements:

- The KPI labeled `Deflated Sharpe` is a point-estimate haircut (`observed SR - expected null max`), while the lesson formula defines DSR as a probability. Rename it or compute the formula shown.
- `Probability strategy is real` overstates what the normal calculation proves. It is a model-implied probability under assumptions, not a true Bayesian probability of skill.
- `Sharpe after costs` subtracts costs from raw in-sample Sharpe, not from deflated/OOS Sharpe. This can make the displayed cost-adjusted Sharpe look too generous.
- `Expected OOS Sharpe` equals the multiple-testing-deflated point estimate, while the reading says empirical OOS Sharpe often halves. Add an explicit OOS-haircut control or label the output more carefully.
- Cost drag assumes 15% volatility. Add a volatility slider or make the assumption prominent in the KPI area.
- The chart approximates the maximum-of-N Sharpe distribution with a normal curve centered at the expected max; label this as a visualization approximation.
- The interactive ignores skewness and kurtosis despite the lesson formula including them.
- Add serial correlation / block-bootstrap caveat for high-turnover strategies.

## New Interactive Demo Ideas

- Survivorship-bias universe simulator.
- Look-ahead-bias timeline checker.
- Strategy search-space simulator where users create false Sharpe by trying more variants.
- Walk-forward builder with rolling windows.
- Regime robustness heatmap.

## Make It More Entertaining Without Watering It Down

The strongest entertainment frame is "backtest court." Stella presents the beautiful equity curve; Horace cross-examines it: dead tickers, data timestamp, fills, costs, trial count, regime sample. Each question knocks a chunk off the Sharpe.

## Money-Making Usefulness

This lesson can prevent students from deploying fragile systems and buying overfit strategy products. The most practical habit is: no point-in-time data, no realistic costs, no honest trial count, no capital.

## SOUL Consistency Flags

- Strong alignment with SOUL's skepticism toward easy alpha and emphasis on small opportunity-sleeve sizing.
- Needs terminology consistency around the opportunity/opportunistic sleeve.
- The lesson should keep the message focused on defensive validation for retail investors, not on encouraging frequent system trading.
