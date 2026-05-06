# Review: course/week41_risk_management.md

## Overall Assessment

Week 41 is one of the most important behavioral and practical lessons in the course. The central message is excellent: most blowups come from size, not direction. The Kelly/fractional Kelly/1-2% risk framework is exactly the kind of discipline the course should teach.

The lesson needs several math and model fixes before publication. The leverage drawdown formula is wrong as written, the variance wording is imprecise, and the interactive's default outputs do not appear to match the script.

## Content Critique

- The opening is strong and memorable: being right about direction is useless if size destroys the bankroll.
- "Staying solvent longer than the market stays irrational" is important, but the sentence in §1 has a grammar break and should be cleaned up.
- The Kelly formula and coin-flip example are clear.
- The "above 2x Kelly" statement should be softened to expected log-growth/wealth tending toward ruin rather than a casual guarantee unless assumptions are stated.
- Fractional Kelly is well framed. However, claims like quarter-Kelly keeping drawdowns under 25% need model assumptions or softer wording.
- The 1-2% rule section is practical and clear.
- The stop-loss versus hedge distinction is very useful. Add a note that stops may be inappropriate for long-term index allocations where the plan is rebalancing, not thesis invalidation.
- The correlation bucket framework is strong and appropriately simple for retail investors.
- The leverage drawdown formula is wrong as written: `DD_lev ≈ (1 + L) × DD_unlev` conflicts with the examples. If `L` means total leverage, it should be approximately `L × DD_unlev` before financing/path effects.
- The lesson says 2x leverage doubles return and variance. It doubles expected return and volatility/exposure; variance scales roughly with `L^2`.
- The chart assumptions for leverage/drawdown should disclose simulation method, return distribution, financing drag, and rebalancing assumptions.
- The bankroll rules are useful, but "income position size = yield target / asset yield" in Q11 is dangerous if not capped by credit, duration, liquidity, and concentration risk.

## Cross-Reference And Consistency Issues

- Week 40 previewed Week 41 as macro positioning, but Week 41 is risk management.
- Week 41 should explicitly tie back to Weeks 37-40 because options, futures, and vol products are where sizing errors become fatal.
- The four-tranche language in Q11 uses Growth/Income/Stores/Opt; make sure this matches the course-wide tranche naming and SOUL terminology.
- The lesson should reinforce the futures margin warning from Week 39 and vol-convexity warning from Week 40.

## Presentation Improvements

- Add a one-page sizing checklist before any leveraged trade.
- Add a table comparing stop, hedge, size reduction, and diversification.
- Fix the leverage formula and show a simple numeric example.
- Add "risk per trade" versus "notional position size" diagrams.
- Add a crash-correlation illustration showing ten 1% tech risks becoming one 8-10% bucket risk.

## YouTube Script Critique

The script has good teaching energy and makes sizing feel dramatic rather than administrative. It needs a few alignment fixes.

Specific improvements:

- The opening comparison says Investor B uses 50% with full Kelly. That can confuse students because full Kelly depends on edge; say "oversized relative to Kelly" unless the example provides inputs.
- The script's interactive walkthrough says defaults should produce about $10,000 per position and ten simultaneous positions. The actual interactive appears to output a much smaller Kelly-capped position and 8 max simultaneous positions at a sector cap of 8%.
- Add a Stella challenge: "If my stop is tighter, why isn't that always safer?" This lets Horace explain noise stops and gap risk.
- Add a short futures example: one /MES contract can be a small margin line but a large notional risk.
- Keep the final rules, but make the four-tranche connection explicit.

## Chart And Visual Feedback

Existing visuals are valuable:

- Kelly curve.
- Leverage drawdown curve.

Recommended upgrades:

- Add fractional Kelly growth/drawdown curve.
- Add drawdown recovery table.
- Add correlation bucket heatmap.
- Add gap-risk illustration for stop losses.
- Add notional-versus-risk sizing chart for options/futures.

## Interactive Demo Feedback

The `week41_position_sizer.html` interactive is useful, but its model needs clearer labels and alignment with the script.

Issues and improvements:

- The default output described in the script does not appear to match the code. With default settings, the Kelly cap is likely far below $10,000 and the sector-cap position count is 8, not 10.
- The model converts edge/vol into a binary win probability with `Phi(edge / vol)` and assumes `b = 1`. That is a stylized proxy, not the same as normal-return Kelly (`mu / sigma^2`). Explain or replace.
- `Max loss / trade` is implemented as dollar risk divided by per-trade volatility, effectively a one-sigma sizing proxy, not a true stop-defined max loss.
- Blowup probability is labeled as drawdown ruin, but the code flags paths down 50% from starting wealth, not necessarily peak-to-trough drawdown.
- Add a stop distance input for stock trades and a max-loss input for option spreads.
- Add a correlation slider or bucket count.
- Add a futures/notional mode.
- Fix CJK translation strings that appear to use `回撚` where `回撤` or `回檔` is intended.

## New Interactive Demo Ideas

- Stop-distance position calculator.
- Fractional Kelly simulator with estimation error.
- Correlation bucket allocator.
- Leverage drawdown stress tester.
- Options/futures max-loss sizing calculator.

## Make It More Entertaining Without Watering It Down

This lesson can use a "same thesis, different size" cold open. Show two investors both right about a stock, then reveal one survives because the losing streak was sized and the other fails because the same streak hits at 5x the risk.

## Money-Making Usefulness

This is mostly a save-money and stay-alive lesson, but that is exactly what lets students make money over decades. The practical sizing rules are more valuable than another stock-picking framework.

## SOUL Consistency Flags

- Strong alignment with SOUL's "market can stay irrational longer than you can stay solvent" constraint.
- Needs explicit application to the options/futures/volatility tools introduced in Weeks 37-40.
- Four-tranche naming should be standardized.
