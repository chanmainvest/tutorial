# Review: course/week27_covered_calls.md

## Overall Assessment

Week 27 is a useful covered-call deep dive. It correctly moves beyond the simple "paid limit order" analogy into strike, tenor, IV, rolling, taxes, and buy-write ETF trade-offs. The QYLD discussion is particularly valuable for readers chasing yield.

The lesson has several technical and cross-reference problems that should be fixed before publication: IV-rank is defined incorrectly, some delta/sigma language is wrong, early-assignment mechanics are overstated, JEPI history is likely overclaimed, and the wheel is previewed as Week 30 even though Week 30 is spreads/condors.

## Content Critique

- Strike selection by delta is the right framework.
- The distinction between 30-delta income writing and 16-delta conservative writing is useful.
- The reading correctly says 2.5-delta is roughly two standard deviations, but the script says 10-delta is two standard deviations. That is wrong; 10-delta is closer to a 1.3-sigma one-tailed event, while 2.5-delta is closer to 2-sigma.
- IV-rank is defined incorrectly. IV rank usually means `(current IV - 52-week IV low) / (52-week IV high - 52-week IV low)`. IV percentile measures where current IV sits relative to historical observations. A rank of 50 is not necessarily the median.
- The rule "sell when IV-rank is above 30" is a useful convention, but it should be presented as a rule of thumb rather than a universal law.
- The claim that skipping bottom-quintile IV-rank months improves Sharpe by about 25% needs a source or should be softened.
- The weekly-options early-assignment statement is misleading. A stock briefly piercing the strike midweek and closing below it on Friday does not normally cause assignment by itself. Weeklies have gamma and mark-to-market risk, but early exercise of calls is mostly about dividends and remaining time value.
- The tax section is better than prior lessons and correctly introduces qualified covered-call rules, but it should warn that the exact rules are detailed and jurisdiction-specific.
- The QYLD critique is strong, but the image filename says `week27_qyld_vs_spy.png` while the text compares QYLD to QQQ.
- JEPI launched in 2020, so an "11-year arc" cannot be actual JEPI live history unless it uses a backtest. Clarify.
- The claim that DIY covered calls beat buy-write ETFs over a long horizon is too broad. Skilled, disciplined DIY can do better, but many retail investors will underperform through timing, tax, and execution mistakes.
- The worked SPY example says twelve monthly writes can produce 13% annualized premium layered on top of SPY's normal appreciation and dividend. That overstates the result because assignment, upside caps, and roll losses are part of the strategy.

## Cross-Reference And Consistency Issues

- The wheel is previewed as Week 30, but `course/week30_spreads_condors.md` is Week 30. The wheel appears to be `course/side30_wheel_strategy.md`, or it belongs in Week 28 if that is the cash-secured-put lesson.
- Q&A says XSP is a small-account substitute for covered calls. XSP is cash-settled index options and does not pair cleanly with owned shares as a covered call. Clarify that it is a different defined-risk/index-options structure, not a covered call on an ETF.
- Q&A says covered calls live on the passive-equity end of the barbell, while Week 26 framed them as the L2 income sleeve. Standardize the tranche/barbell language.

## Presentation Improvements

- Add a delta-to-sigma table: 50, 30, 16, 10, 5, 2.5 delta.
- Add a box distinguishing IV rank from IV percentile.
- Add an early-assignment checklist: dividend, time value, ITM depth, borrow/carry.
- Add a source note for BXM methodology and any Sharpe-improvement claims.
- Add live-history versus backtest labels for JEPI/QYLD charts.
- Add a "DIY can beat ETFs only if..." checklist.

## YouTube Script Critique

The QYLD hook should get attention, and the strike-by-delta segment is a good fit for video.

Specific improvements:

- Correct the 10-delta/two-sigma line.
- Explain IV rank correctly or rename the concept to IV percentile.
- Replace "weeklies are awful" with a more precise warning about gamma and management burden.
- Correct the Week 30 wheel preview.
- Add a quick visual showing total return versus distribution yield.

## Chart And Visual Feedback

Existing visuals are useful:

- Premium yield by strike.
- QYLD comparison chart.

Recommended upgrades:

- Add delta/sigma ladder.
- Add IV rank versus IV percentile diagram.
- Add rolling decision tree.
- Add QYLD distribution yield versus NAV/total return chart.
- Add covered-call performance by market regime: flat, grind-up, melt-up, crash, V-recovery.

## Interactive Demo Feedback

The referenced `course/interactive/week27_call_writer.html` is a strong fit for this lesson. Delta, tenor, yield, breakeven, and assignment odds are exactly what the reader should manipulate.

Suggested improvements:

- Add IV rank and IV percentile separately.
- Add ex-dividend early-assignment warning.
- Add after-tax yield toggle.
- Add roll-up-and-out and roll-down-and-out simulation.
- Add total-return comparison versus simply holding the underlying.
- Add a warning when annualized yield is high because delta/assignment risk is high.

## New Interactive Demo Ideas

- Covered-call regime simulator.
- Rolling decision tree calculator.
- QYLD-style ATM buy-write versus DIY 16/30-delta strategy backtest.
- Taxable versus IRA covered-call yield calculator.
- Assignment probability and dividend-risk explorer.

## Make It More Entertaining Without Watering It Down

The QYLD segment is the entertainment engine: show the viewer the yield headline first, then reveal the total-return chart. That "income is not return" reveal is memorable and financially useful.

## Money-Making Usefulness

This lesson is money-useful because it teaches readers not to chase premium mechanically. The best practical guidance is: choose delta intentionally, avoid low-IV months, respect taxes, and accept assignment when the original thesis says assignment is fine.

## SOUL Consistency Flags

- Aligns with SOUL's options-as-expression-tool principle.
- Needs cleaner tranche/barbell placement for covered calls.
- Should avoid implying covered-call overlays are a high-return engine independent of the underlying equity and volatility regime.
