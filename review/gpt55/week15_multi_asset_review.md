# Review: course/week15_multi_asset.md

## Overall Assessment

Week 15 is an important bridge from simple first portfolios to a more robust multi-asset chassis. The four-quadrant framework, 2022 stock-bond correlation break, risk-contribution idea, and retail four-tranche structure are all highly relevant to the course's philosophy.

The lesson needs more mathematical precision and less prescriptive certainty. Risk parity is not simply inverse-vol weighting unless correlations are ignored; the 1928-2024 backtest depends heavily on gold assumptions before 1971; and telling readers that 40/30/20/10 is a defensible IRA default "tomorrow" is too strong without age, jurisdiction, tax, and risk-capacity caveats.

## Content Critique

- The 2022 break is the correct anchor. It explains why 60/40 needs regime-aware caveats.
- The growth/inflation quadrant model is useful and memorable, but "one winning asset per cell" is a simplification. Several assets can win or lose depending on valuation, policy, starting yields, and real-rate path.
- The risk-parity section needs correction. True risk parity equalizes each asset's contribution to total portfolio risk using the covariance matrix. Inverse-vol weighting is only a simplified approximation when correlations are ignored.
- The inverse-vol table appears numerically confusing, especially the T-bill row. With the stated vols, cash dominates the inverse-vol allocation, but the displayed raw/risk-parity weights do not clearly follow the formula.
- The lesson should distinguish Bridgewater-style leveraged all-weather, AQR risk parity, and the course's unlevered four-tranche retail chassis.
- The 2022 risk-parity break is well explained. Add that commodities/energy helped in 2022, while many TIPS funds still suffered because real rates rose.
- The four-tranche structure is helpful, but the labels need consistency with SOUL.md and previous lessons.
- TIPS are described as paying only the inflation print. More precisely, TIPS pay a real coupon on inflation-adjusted principal and return adjusted principal at maturity.
- The pre-1971 gold assumption of 4% real per year is a major backtest assumption. It should be labeled clearly and tested against alternatives.
- "Every decade positive real return" should be treated as backtest output under the stated assumptions, not a timeless property.
- Q&A says 40/30/20/10 is a defensible default in an IRA tomorrow. This is too prescriptive and US-specific. It needs suitability and jurisdiction caveats.
- The international-equity answer is confusing: it says "for a US-domiciled investor" but then invokes withholding taxes, currency hedging, and capital controls in a way that sounds more like non-US investability concerns. Clarify the intended audience.

## Cross-Reference And Consistency Issues

- The lesson says Weeks 16-30 will populate sectors, factors, options strategies, and barbell tilts. Confirm this matches the actual course sequence.
- The four-tranche terminology should be harmonized with Weeks 12-14 and SOUL.md.
- The international-equity stance conflicts with Week 12's VXUS sleeve unless framed as orthodox diversification versus Horace's US-first view.
- The Q&A references a "dashboard at the top of the website." If this dashboard is not a stable public feature, remove or generalize it.

## Presentation Improvements

- Add an "orthodox risk parity versus retail four-tranche" comparison table.
- Add a note explaining why covariance matters in risk parity.
- Add a backtest assumptions box, especially for gold before 1971, rebalancing, taxes, and real-return data.
- Add a suitability grid by investor type: accumulator, pre-retiree, retiree, taxable investor, non-US investor.
- Add a source table for Bridgewater/AQR 2022 drawdown claims.
- Add a warning that all-weather reduces some risks but introduces others: duration, real-rate, leverage, tax, and underperformance risk.

## YouTube Script Critique

The script is lively and well structured. Stella leading the intro is a nice change of rhythm, and the 2022 honesty is good for trust.

Specific improvements:

- When introducing inverse-vol, Horace should say this is a simplified teaching approximation, not full risk parity.
- Add a Stella challenge: "If the backtest earns less than 60/40, why would I use it?" Horace can answer with sequence risk and drawdown tolerance.
- Add a warning that the 1928 gold backfill is an assumption.
- Soften "whatever decision you make on the slider, you cannot screw up Sharpe by very much." That may not hold with extreme weights or real-world taxes/costs.
- Make the homework safer: find the portfolio whose drawdown you can actually hold, not just min drawdown/highest Sharpe.

## Chart And Visual Feedback

Existing visuals are appropriate:

- Growth/inflation quadrant grid is essential.
- Four-tranche donut is clear.
- Backtest table is useful but should be accompanied by assumptions.

Recommended upgrades:

- Add stock-bond correlation rolling chart with 2022 highlighted.
- Add risk-contribution bars for 60/40 versus four-tranche.
- Add covariance-aware risk-parity visual.
- Add drawdown chart for 100% equity, 60/40, and four-tranche.
- Add sensitivity chart for gold pre-1971 assumptions.

## Interactive Demo Feedback

The referenced `course/interactive/week15_allweather_builder.html` is exactly the right interactive shape: sliders, historical wealth, max drawdown, Sharpe, and drawdown duration.

Suggested improvements:

- Add a toggle for nominal versus real returns.
- Add tax drag and expense ratio assumptions.
- Add rolling stock-bond correlation regime markers.
- Add risk-contribution chart, not only dollar weights.
- Add pre-1971 gold assumption controls.
- Add suitability prompts based on horizon and withdrawal status.

## New Interactive Demo Ideas

- Risk-contribution calculator using covariance matrix.
- Stock-bond correlation regime explorer.
- 2022 stress-test dashboard.
- All-weather assumption sensitivity lab.
- Jurisdiction-aware four-tranche implementation map.

## Make It More Entertaining Without Watering It Down

The entertainment is in the 2022 reveal: a portfolio sold as all-weather met weather it was not built for. Use that tension to make the framework trustworthy, not magical.

## Money-Making Usefulness

This lesson helps students make money by teaching them what risk their portfolio is secretly concentrated in. The most useful output is not one fixed allocation; it is the ability to see whether a portfolio is a single-quadrant bet.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #2, #5, #6, #7, #13, and #17.
- Needs cleaner orthodox-first framing for all-weather/risk parity before introducing Horace's four-tranche retail adaptation.
- Needs better alignment with SOUL's US-first global-investability stance while not confusing US and non-US tax concerns.
- Tranche definitions should be standardized across Weeks 12-15.
