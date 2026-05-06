# Review: course/week14_pair_trading.md

## Overall Assessment

Week 14 is a strong continuation of Week 13. It makes the key conceptual move: pair trading is not "two stocks that seem related," but a relative-value bet on a mean-reverting spread. The correlation-versus-cointegration section is essential and well explained.

The lesson needs technical cleanup around hedge ratios, equal-dollar sizing, and the source/precision of the 2007 quant-quake claims. It also has a major next-week mismatch in the YouTube outro.

## Content Critique

- The opening connects well to Week 13 and clearly positions pair trading as education before production use.
- The regime-change warning is excellent. KO/PEP is a useful example because PEP's snack business makes the pair less clean than it looks.
- The 2007 quant-quake case study is highly relevant and entertaining, but it should be sourced and phrased carefully. Claims like "some funds halved in a week" need precision.
- The log-spread construction assumes a 1:1 hedge ratio. Real pair trading usually estimates a hedge ratio through regression or cointegration testing. Add this before teaching Z-scores.
- The example "long 1,000 KO and short 1,000 PEP" conflicts with equal-dollar sizing because KO and PEP have different prices. Use dollar amounts or hedge-ratio-adjusted share counts.
- "Correlation is not cointegration" is the best technical section. Keep it and make it a recurring warning in factor/stat-arb material.
- Pair trading as "structural alpha" is partly true but a little too broad. Many pairs are statistical mean-reversion trades; the structural-alpha argument applies when the dislocation is tied to forced flows, liquidity provision, or crowding.
- GLD/SLV is a less stable pair than KO/PEP or V/MA because silver has large industrial-demand shifts and the gold/silver ratio can exceed the stated range. Present it as a noisier pair.
- The barbell positioning section introduces deep-ITM long-dated calls as part of the safety end, which is conceptually confusing. Deep-ITM calls are still option exposure and should not be grouped with cash, Treasuries, and gold as safety.
- The lesson wisely says one-pair retail trading is education, not alpha. That should be highlighted even more.

## Cross-Reference And Consistency Issues

- The YouTube outro says Week 15 is volatility as an asset class, but the course map shows Week 15 as multi-asset allocation.
- The barbell/tranche language should be checked against SOUL.md and Week 13. Pair trading is described as opportunistic, edge-end, and third tranche; make sure the labels stay consistent.
- If Week 15 is multi-asset, this lesson should preview how relative-value thinking helps multi-asset allocation, not volatility.

## Presentation Improvements

- Add a hedge-ratio mini-section before Z-score construction.
- Add a simple table: correlation, cointegration, hedge ratio, Z-score, entry/exit, stop.
- Add an equal-dollar sizing example with actual prices.
- Add a "pair viability checklist": same sector, similar business model, stable spread, plausible fundamental link, cheap borrow, low crowding, clear break condition.
- Add a "regime break versus dislocation" decision tree.
- Add a warning that a pretty backtest with one pair is usually overfit.

## YouTube Script Critique

The script is engaging and clear. The quant-quake story is a good retention device, and the "correlation is not cointegration" takeaway is memorable.

Specific improvements:

- Let Stella make the naive mistake: "KO and PEP are correlated, so I trade them." Horace can correct her with cointegration.
- Add a 30-second hedge-ratio explanation using dollar amounts.
- Add a stronger retail warning: one pair is tuition, not income.
- State that the 2007 quant-quake numbers are historical estimates and vary by fund/source.
- Fix the next-week preview.

## Chart And Visual Feedback

Existing visuals are good:

- KO/PEP spread chart is the right teaching chart.
- Pair P&L chart is useful because it shows small wins and occasional regime breaks.

Recommended upgrades:

- Add hedge-ratio visual: raw prices, ratio, regression residual spread.
- Add regime-break annotation on KO/PEP when business mix diverged.
- Add a 2007 quant-quake timeline.
- Add a parameter-sensitivity heatmap for entry Z-score and lookback window.
- Add a borrow/dividend cost overlay.

## Interactive Demo Feedback

The referenced `course/interactive/week14_pair_lab.html` is exactly the right interactive for this lesson: pick a pair, change entry/exit Z-score and lookback, watch P&L, trade count, win rate, and Sharpe.

Suggested improvements:

- Add hedge-ratio selection: 1:1, equal-dollar, beta-adjusted, regression-estimated.
- Add transaction cost, borrow cost, dividend cost, and tax drag toggles.
- Add out-of-sample split: calibrate on one window, test on another.
- Add parameter-stability heatmap to reveal overfitting.
- Add a "regime break" marker where the pair relationship structurally changes.

## New Interactive Demo Ideas

- Correlation versus cointegration simulator using two random walks.
- Pair sizing calculator: dollar-neutral, beta-neutral, hedge-ratio-neutral.
- Quant-quake crowding simulator.
- Pair viability screener checklist.
- Regime-break diagnostic: is the spread wide because of noise or a changed business model?

## Make It More Entertaining Without Watering It Down

The entertainment is in the detective story: two companies look alike until one quiet business-model difference makes the pair stop working. Pair trading should feel like forensic investing, not button-click stat magic.

## Money-Making Usefulness

For most students, the money-making value is not running a pair book. It is learning relative valuation, hedge discipline, overfitting detection, and crowding risk. Those skills transfer to factor investing, sector rotation, and portfolio construction.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #4, #5, #7, #8, and #13.
- Needs cleaner tranche/barbell terminology, especially around safety versus option exposure.
- Needs a more precise distinction between structural alpha and statistical mean reversion.
- Fix Week 15 preview mismatch.
