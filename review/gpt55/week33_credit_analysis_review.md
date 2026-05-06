# Review: course/week33_credit_analysis.md

## Overall Assessment

Week 33 has a strong topic and a clear practical purpose: it teaches students that credit yield is not free income, but compensation for default probability, recovery uncertainty, liquidity, and stress-path risk. The rating ladder, expected-loss formula, and high-yield spread history are all useful.

The lesson needs significant tightening before publication. The largest issue is that the 2008 interactive example appears internally inconsistent: the stated spread, implied YTM, price, and expected return do not line up. The YouTube script also opens with the wrong prior-week reference and previews a different Week 34 than the visible course file.

## Content Critique

- The central question is excellent: will the borrower pay, and what spread compensates for non-payment risk?
- The rating-ladder explanation is clear.
- The expected-loss formula is necessary and well placed.
- The lesson should clarify that annual default rates are not the same as cumulative default probability across a multi-year bond life.
- The spread decomposition formula is a good teaching model, but it should be labeled simplified. Spread also reflects taxes, callability, downgrade/migration risk, index technicals, and risk appetite.
- The line that high-yield spreads are the bond market's volatility index is vivid, but "credit leads equity" is too strong. Credit is often a powerful stress indicator, not a reliable timing signal.
- "HY has delivered 200-300 bps over Treasuries net of defaults, uncorrelated to the equity premium" should be revised. HY is meaningfully equity-correlated in stress regimes.
- The IG/HY cliff is real, but not every investor is forced to sell immediately. Add nuance for fallen-angel mandates, rating-watch periods, and index rules.
- "Don't buy HY at sub-400 bps" is a useful rule of thumb, but the explanation says that level pays less than expected loss for B-rated paper. With the lesson's own B default and 40% recovery assumptions, expected loss is about 246 bps, so sub-400 is thin but not below expected loss.
- "Do buy HY at 800+ bps spreads, with size" is too directive. Change to a sizing-aware opportunity rule, with path, liquidity, recession, and forced-selling caveats.
- The ETF recommendation is directionally right, but should mention ETF discounts/premiums, underlying bond liquidity, fees, and tax/currency issues for non-US readers.
- The April 2026 HY spread comment needs a source/date caption, especially if the chart is generated from live or fixed data.

## Major Numerical Issue

The 2008 credit-pricer example is internally inconsistent across the lesson, script, and interactive.

- Reading section says: 10-year, 6% coupon, 4% Treasury, 1,800 bps spread, 6% PD, 40% recovery; expected return still +9% per year.
- Script says: implied price about 68, credit-adjusted YTM 12%, expected return about 9%.
- Interactive preset uses: Treasury 4%, spread 1,800 bps, so gross YTM = 22%, not 12%.
- A 10-year 6% coupon bond discounted at 22% should price far below 68. A price near 68 is closer to a much lower yield, around the low-teens.

This example needs to be recalculated and made consistent. If the intended YTM is 12%, the spread should be closer to 800 bps over a 4% Treasury, not 1,800 bps. If the intended spread is 1,800 bps, the price and expected return should be very different.

## Cross-Reference And Consistency Issues

- Week 32's outro previews Week 33 as credit spreads, but the actual file is credit analysis. This is close enough topically, but should be named consistently.
- Week 33's script intro says last week covered corporate finance, capital structure, and WACC; the actual prior lesson is Week 32 duration and convexity.
- Week 33's outro previews Week 34 as liquidity risk, but the visible Week 34 file is `week34_rate_sensitivity.md`.
- The phrase "credit spread" needs a one-sentence distinction from options credit spreads because Weeks 26-30 used the same words in a different context.

## Presentation Improvements

- Add a simple waterfall: gross spread -> expected loss -> liquidity premium -> risk premium.
- Add a long-run versus recession-year default-rate table.
- Add a fallen-angel case study.
- Add a "spread is not yield" callout.
- Add a model assumptions box for the interactive.
- Add a stress path example showing how HYG can fall before the expected return arrives.

## YouTube Script Critique

The script has good pacing and clear visuals, but it needs correctness fixes.

Specific improvements:

- Fix the prior-week reference.
- Recalculate the 2008 interactive segment.
- Replace "every single panic was a buying opportunity" with probabilistic language.
- Avoid "always buy HY over 800 bps with size"; that is too close to financial advice without sizing rules.
- Add a Stella challenge: "If the expected return is positive, why do people still lose money in HY?" That opens the path-risk discussion.
- Standardize host labels with the rest of the English scripts if needed.

## Chart And Visual Feedback

Existing visuals are useful:

- Default rates by rating bucket.
- HY OAS history.

Recommended upgrades:

- Add recovery-rate history by seniority.
- Add spread decomposition waterfall.
- Add HYG drawdown versus HY OAS chart.
- Add fallen-angel downgrade timeline.
- Add rate-loss versus spread-loss decomposition for 2022 HY.

## Interactive Demo Feedback

The `week33_credit_pricer.html` interactive is a strong concept but needs model and number cleanup.

Issues and improvements:

- Fix the 2008 preset so spread, YTM, price, and expected return agree.
- Disclose that liquidity and risk premium split is heuristic/arbitrary in the bar chart.
- Clarify that expected return is a simplified one-period approximation, not a full multi-year hazard-rate bond model.
- Add cumulative default probability over maturity.
- Add ETF mode using HYG/JNK/LQD duration, fees, and spread duration.
- Add a scenario path chart: spread widens first, income arrives later.

## New Interactive Demo Ideas

- Fallen-angel forced-selling simulator.
- HY spread entry timing simulator.
- Credit ETF drawdown and recovery path lab.
- Default/recovery Monte Carlo for a diversified HY ETF.
- Spread-duration decomposition for 2022.

## Make It More Entertaining Without Watering It Down

The best hook is the downgrade cliff: one rating notch turns a pension-owned bond into forced-sale junk. Make that a dramatic Stella moment, then show how patient capital can exploit the technical.

## Money-Making Usefulness

This lesson can genuinely help students avoid yield traps and recognize panic opportunities. Its money-making value depends on fixing the numerical model and adding sizing/path-risk rules.

## SOUL Consistency Flags

- Aligns with SOUL's structural alpha sources: illiquidity, behavioral selling, and mandate-driven dislocations.
- Needs less deterministic language around HY entry levels.
- HY belongs in a yield/risk sleeve, not the safety sleeve; that alignment is good.
