# Review: course/week17_performance_metrics.md

## Overall Assessment

Week 17 is a necessary and useful lesson. It teaches students to stop judging portfolios by raw return and to ask what pain, beta, drawdown, and benchmark deviation produced that return. The taxonomy of Sharpe, Sortino, Calmar, IR, Treynor, alpha, and beta is well chosen.

The lesson needs a few precision fixes. Some rules of thumb are too strong, the S&P drawdown figure conflicts with earlier lessons, and the YouTube outro previews the wrong Week 18 topic.

## Content Critique

- The opening is excellent: return alone is not evaluation.
- The Sharpe section is strong, especially the frequency-rescaling trap.
- The warning about hidden tail risk is important and SOUL-aligned.
- The Sortino section should be more cautious. A high Sortino relative to Sharpe can indicate positive skew or downside control, but it can also reflect a benign sample window with few downside observations.
- The Sortino downside-deviation formula should clarify whether the denominator divides by all observations or only downside observations; both variants exist.
- Calmar is well explained, but the S&P 500 max drawdown number should be harmonized with other lessons. Week 15 uses -75% real max drawdown for 1929-32, while this lesson cites roughly -86%.
- The Information Ratio section is useful for active-manager evaluation.
- Treynor is correctly framed as inappropriate for market-neutral or near-zero-beta portfolios.
- The CAPM alpha/beta section is strong, especially the warning that omitted factors can masquerade as alpha.
- The metrics-disagree section is the lesson's best teaching move. Keep the idea that disagreement is signal, not confusion.
- Rolling Sharpe by regime is useful, but state clearly that a 10-year Sharpe computed from annual data is noisy.

## Cross-Reference And Consistency Issues

- The S&P 500 drawdown figure differs from Week 15's backtest table. Decide whether the course uses nominal price, nominal total return, real total return, or annual versus daily data, then label consistently.
- The YouTube outro says Week 18 will cover what to do with metrics in portfolio construction, but Week 18 is interest rates and market returns.
- The script uses uppercase speaker labels (`HORACE`, `STELLA`), while many prior scripts use title-case markdown labels. Standardize script formatting across the course.

## Presentation Improvements

- Add a "metric answers this question" table.
- Add a "metric can be gamed by" column: Sharpe by short vol, Calmar by short sample, IR by closet indexing, alpha by omitted factors.
- Add a distribution-shape visual: symmetric, positive skew, negative skew.
- Add a common-window warning: compare metrics over the same dates.
- Add confidence intervals or sample-size warnings for Sharpe and alpha.

## YouTube Script Critique

The title "Sharpe Is Lying to You" is clickable and appropriate, but the video should avoid making Sharpe sound useless. Sharpe is useful; it lies when used alone or when the distribution has hidden tails.

Specific improvements:

- Change "picking the right metric is all of the battle" to "picking the right metric is half the battle; reading the sample window is the other half."
- Avoid saying S&P Sharpe varies by a "factor of fifteen" when one endpoint is near zero.
- Add a Stella question: "Can a high Sharpe be dangerous?" Then show short-vol/illiquid-credit examples.
- Fix the Week 18 preview.
- Add one concrete fund-tearsheet reading exercise.

## Chart And Visual Feedback

Existing visuals are useful:

- Metric comparison grid is essential.
- Rolling Sharpe chart makes regime dependence visible.

Recommended upgrades:

- Add drawdown chart beside Calmar.
- Add a CAPM scatter static image for the reading section, not only the interactive.
- Add a sample-size/uncertainty visual for Sharpe estimates.
- Add a skewness visual showing why Sharpe and Sortino disagree.
- Add a metric-selection decision tree.

## Interactive Demo Feedback

The referenced `course/interactive/week17_metrics_lab.html` is the right interactive: sliders/weights, start year, metrics, and CAPM scatter.

Suggested improvements:

- Add benchmark selection for IR and beta, not only S&P 500.
- Add confidence bands for alpha and beta.
- Add daily/monthly/annual frequency mode to show annualization pitfalls.
- Add hidden-tail examples such as short-vol synthetic strategy.
- Add common-window comparison mode for multiple portfolios.

## New Interactive Demo Ideas

- Fund tearsheet grader: enter return, volatility, drawdown, tracking error, beta; get metric interpretation.
- Sharpe annualization trap quiz.
- Alpha significance calculator.
- Metric gaming simulator: smooth illiquid returns, short-vol returns, levered beta returns.
- Drawdown pain simulator tied to Calmar.

## Make It More Entertaining Without Watering It Down

The entertaining hook is fraud detection: how ratios flatter strategies that later blow up. Use examples like LTCM, short-vol funds, and smooth private-credit marks carefully, with the lesson that metrics are tools, not verdicts.

## Money-Making Usefulness

This lesson helps students make money by preventing them from paying active fees for beta, closet indexing, or hidden tail risk. The practical output should be a three-metric minimum: Sharpe, max drawdown/Calmar, and IR or alpha versus the correct benchmark.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #1, #5, #7, #8, and #12.
- The lesson supports SOUL's skepticism toward naive alpha claims.
- Needs consistency in drawdown data definitions across the course.
