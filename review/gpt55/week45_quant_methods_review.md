# Review: course/week45_quant_methods.md

## Overall Assessment

Week 45 is one of the most important advanced lessons. It teaches students how to evaluate alpha claims, factor exposure, overfitting, ML pitches, and backtest credibility. The lesson is highly aligned with SOUL's view that alpha is rare and expression/toolkit matters.

It needs equation consistency, a few statistical corrections, and script/lab alignment. The biggest issues are the inconsistent factor model, the broken duplicate sentence in §2.4, and the YouTube script's incorrect statement about how much data is needed to prove 2% alpha.

## Content Critique

- The opening is strong and useful: quantitative methods are the language of skill claims.
- The phrase "alpha is what is left over after a regression on the right factors" is good, but should acknowledge factor-model choice risk and factor-zoo overfitting.
- The factor model is inconsistent. The opening lists MKT/SMB/HML/UMD/RMW; the equation includes MKT/SMB/HML/UMD only; Q11 references FF5 + UMD. Standardize on CAPM, Fama-French 3, Carhart 4, or FF5 + UMD and name each correctly.
- UMD is not part of original Fama-French 3 or FF5; it is the Carhart momentum factor when added to FF3.
- The t-stat explanation in §2.2 is excellent and should be preserved.
- The 25-year proof-of-skill point is one of the lesson's best moments.
- Cross-sectional regression is useful, but the statement that this is inside every smart-beta ETF is too broad. Many smart-beta products use ranking/weighting heuristics rather than monthly Fama-MacBeth estimation.
- The AR(1) section is useful, but "where phi is zero, no model that takes only past prices as input can win" is too strong. It is true for linear lag-one autocorrelation, but nonlinear effects, volatility state, and cross-sectional signals complicate the statement.
- §2.4 has a broken duplicate sentence: "You return dog — gets a lot of its leverage..." This needs deletion/repair.
- VIX/volatility persistence should distinguish VIX levels, realized volatility, log-volatility, and mean reversion.
- Parameter-stability examples need sourcing, especially the claim that HML market beta shifted sign around 2007.
- The multiple-testing section is valuable, but misconception #2 says in-sample Sharpe bias scales by roughly `sqrt(N)` standard deviations. That should be closer to extreme-value / `sqrt(2 log N)` logic, not `sqrt(N)`.
- The signal-to-noise/R-squared claim in §2.8 needs precision. `0.05 R-squared per month` could mean 5%, which is high for equity-return prediction; if the intent is 0.05%, say that.
- §2.8 repeats `expensive. expensive.`
- Q4's "arbitrage it away" explanation should mention limits to arbitrage, transaction costs, risk premia, and crowdedness.
- Q8's "linear regression first, always" is a good teaching default, but the claim that ML cannot find a same-feature signal if linear regression cannot is too strong. Nonlinear interactions can exist, but should be treated skeptically.

## Cross-Reference And Consistency Issues

- Week 44 previews Week 45 as regulation/securities law, but Week 45 is quantitative methods.
- Week 45 script previews Week 46 as a real hedge-fund track-record dissection; verify actual Week 46 before publication.
- The lesson says it has leaned on intuition for forty-three weeks, but this is Week 45 after Week 44 microstructure; update count or remove exact count.
- Course terminology should distinguish SOUL structural-alpha lanes from statistical factor alpha.

## Presentation Improvements

- Add a small factor-model taxonomy table: CAPM, FF3, Carhart 4, FF5, FF5 + momentum.
- Add a "what this statistic does not prove" box for alpha, beta, R-squared, p-value, and Sharpe.
- Add a toy example of multiple testing: 1,000 random strategies and the best lucky Sharpe.
- Add a clean equation for t-stat using annual alpha and annual residual volatility.
- Add a regression checklist: excess returns, matching dates, correct benchmark, robust standard errors, residual diagnostics, multiple-testing correction.

## YouTube Script Critique

The script is lively and useful, especially the three bubble-popping questions: holdout, how chosen, t-stat.

Specific issues:

- The script says 60 months with 2% alpha and the shown residual volatility barely gives a t-stat of 2.0. This conflicts with the reading, which correctly says roughly 25 years are needed for 2% alpha at 5% residual vol.
- The lab walkthrough says 200 bps alpha and 4% noise with 60 points lands within about 30 bps of true alpha. That understates sampling error; the annual alpha confidence interval is much wider.
- The script uses "five-factor regression" after showing a four-factor equation. Standardize.
- The next-week preview likely drifts if Week 46 is not a hedge-fund track-record lesson.
- Add a Stella challenge: "Isn't this just math that quants use to justify anything?" This would let Horace explain why the method is useful but not magic.

## Chart And Visual Feedback

Existing visuals are useful:

- Regression alpha chart.
- Overfitting curve.

Recommended upgrades:

- Factor-model ladder chart.
- Multiple-testing false-positive simulator visual.
- Walk-forward timeline diagram with train/validation/test/test-is-consumed labels.
- Alpha confidence interval chart showing why 5 years is rarely enough.

## Interactive Demo Feedback

The `week45_regression_lab.html` interactive is well structured and directly supports the regression lesson.

Issues and improvements:

- It uses a normal 1.96 threshold for alpha significance; for small sample sizes, use Student-t critical values or label it as an approximation.
- It simulates raw market returns rather than excess returns over a risk-free rate; this is acceptable for a toy lab but should be labeled.
- The true line is visible, which is educational, but remind students that real investors never know the true line.
- The preset highlight does not clear when sliders are changed, which can mislead users into thinking the preset still applies.
- Add an option to turn alpha off and repeatedly resample so students can see false positives.
- Add multi-factor mode to show alpha disappearing after adding SMB/HML/UMD/RMW/CMA.
- Add multiple-testing mode that runs many zero-alpha managers and highlights the best lucky result.

## New Interactive Demo Ideas

- Factor attribution lab: CAPM alpha versus FF5 + UMD alpha.
- False-alpha mill: generate 1,000 random strategies and show the best in-sample Sharpe.
- Walk-forward validation simulator.
- ML overfitting slider: features/depth versus in-sample and out-of-sample Sharpe.
- Autocorrelation explorer for momentum versus mean reversion.

## Make It More Entertaining Without Watering It Down

The best story is "the courtroom trial of alpha." Regression is the cross-examination; t-stat is the evidence threshold; multiple testing is the discovery file showing all the failed strategies the manager did not show you.

## Money-Making Usefulness

This lesson can save students from paying high fees for factor beta, noisy alpha, and overfit backtests. It also teaches a practical habit: do not buy a performance pitch until the alpha survives the right benchmark and a clean holdout.

## SOUL Consistency Flags

- Strongly aligned with SOUL: alpha is rare, structural edge matters, and toolkits determine whether a view can be expressed honestly.
- Needs clearer distinction between structural alpha lanes and statistical residual alpha.
- Should not let ML language make information-alpha sound cheaply accessible to ordinary retail investors.
