# Review: course/week42_var_risk_models.md

## Overall Assessment

Week 42 is conceptually strong and well placed after position sizing. It teaches the right hierarchy: VaR is a threshold, CVaR/Expected Shortfall is more useful, and explicit stress tests matter more than model elegance.

The lesson needs a few important accuracy fixes. The "good enough VaR at home" Q&A has percentile errors, the historical-window example claims to include COVID when the stated window likely does not, and the interactive's historical data/date labeling needs verification.

## Content Critique

- The opening does a good job connecting Week 41's sizing discipline to formal risk models.
- Basel/FRTB discussion should be slightly more precise: Expected Shortfall was introduced through FRTB with phased implementation, not simply "required since 2016" in all practical bank reporting.
- The definition of VaR is clear, but the translation of "one day in every hundred" should be framed probabilistically, not as a calendar guarantee.
- Parametric VaR section is vivid and useful. The 1987 example is memorable.
- Historical simulation section says the last 1,000 SPY trading days in April 2026 "knows about COVID." A 1,000-trading-day window in April 2026 likely starts around 2022, so it does not include the March 2020 crash.
- The Monte Carlo section is balanced and warns against false precision.
- CVaR/coherence explanation is excellent for advanced students.
- The kurtosis section is strong, but any live claims through April 2026 should be source-labeled.
- The "VaR is institutional theatre" Horace view is philosophically aligned, but should remain clearly separated from the orthodox framework so students learn both the institutional language and Horace's critique.
- The final Q&A says to read the 5th percentile as 99% VaR and the 25th percentile as 95% VaR. That is wrong. For 500 daily returns, 99% VaR is around the 1st percentile / 5th worst return, and 95% VaR is around the 5th percentile / 25th worst return.

## Cross-Reference And Consistency Issues

- Week 41 correctly leads into Week 42, so this transition is better than several prior chapters.
- Week 42 previews Week 43 as hedging strategies; verify actual Week 43 before publication.
- The lesson should explicitly link back to Week 40's VIX/volatility convexity and Week 41's leverage sizing.
- The barbell/tail-hedge language aligns with SOUL but should use the same tranche naming as prior chapters.

## Presentation Improvements

- Add a VaR/CVaR percentile cheat sheet.
- Add a "sample-size problem" box: how many observations exist at 95%, 99%, 99.9% for 250, 500, 1,000 days.
- Add a table distinguishing VaR, CVaR, stress test, max drawdown, and liquidity risk.
- Add a concrete home spreadsheet example with correct percentile math.
- Add source labels for S&P return data, Damodaran annual returns, and Basel/FRTB references.

## YouTube Script Critique

The script is strong and has a memorable tone. It should work well because it translates an institutional risk concept into practical survival rules.

Specific improvements:

- Clarify that VaR is wrong in the tail because of assumptions, not because the concept is useless.
- In the historical-method section, avoid saying a window "remembers COVID" unless the window actually includes it.
- Add one line explaining why a 99.9% historical VaR from 1,000 days is almost meaningless.
- The interactive walkthrough should mention the square-root-of-time caveat because the lesson itself criticizes that assumption.
- Keep "VaR is institutional theatre" as Horace's view, after the orthodox explanation.

## Chart And Visual Feedback

Existing visuals are useful:

- VaR methods distribution chart.
- Rolling kurtosis history chart.

Recommended upgrades:

- Add percentile/sample-size chart.
- Add VaR versus CVaR tail-shading visual.
- Add model comparison table for the same portfolio: Normal, historical, Student-t, stress test.
- Add a "two portfolios with same VaR but different CVaR" payoff diagram.

## Interactive Demo Feedback

The `week42_var_lab.html` interactive is useful, but several assumptions need clearer labels.

Issues and improvements:

- The embedded historical data is labeled as SPY daily returns since April 2021, but some extreme-looking values appear inconsistent with that window. Verify source/date range.
- Historical VaR ignores the annual-volatility slider, while Normal and Student-t use it. That is valid only if clearly explained.
- Student-t VaR uses 5,000 simulated samples. At 99.9%, that leaves only about five tail observations, so the displayed value can be noisy. Use analytic quantiles or a much larger deterministic sample.
- 1-month VaR is square-root scaled for all methods; add a warning that this assumes IID returns and can fail under volatility clustering.
- Historical 99.9% VaR from a ~1,274-day sample is based on about one observation. The UI should warn about estimator instability.
- Add CVaR tail shading, not only VaR threshold shading.
- Add stress-test buttons: 1987, 2008, Mar 2020, 2022 stock/bond shock.

## New Interactive Demo Ideas

- VaR sample-size instability simulator.
- Same-VaR/different-CVaR payoff comparator.
- Stress-test dashboard with historical scenarios.
- VaR backtest breach counter.
- Tail-hedge sizing overlay that turns model risk into premium budget.

## Make It More Entertaining Without Watering It Down

The best hook is a courtroom-style reveal: "The model said this was a once-in-the-universe event. It happened on a Monday." Then use 1987 as the anchor for why model shape matters.

## Money-Making Usefulness

This lesson makes students less likely to trust thin-tail risk numbers and more likely to size for stress. That is directly money-saving and survival-enhancing, especially for options and futures users.

## SOUL Consistency Flags

- Strong alignment with SOUL's skepticism toward model-only risk management.
- Strong alignment with tail-hedge/barbell thinking.
- Needs standardized tranche language and explicit connection to the course's vol-on/vol-off regime framing.
