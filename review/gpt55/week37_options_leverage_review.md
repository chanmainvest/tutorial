# Review: course/week37_options_leverage.md

## Overall Assessment

Week 37 teaches a valuable advanced concept: deep-ITM calls can be used as capital-efficient stock replacement rather than lottery-ticket speculation. The core distinction between OTM gambling and deep-ITM leverage is useful and fits the options arc.

The lesson needs stronger leverage, tax, and interactive-model caveats. The largest issue is that the interactive appears to size option rows by notional share exposure rather than delta-adjusted exposure while claiming equal target equity exposure. The tax section also contains a capital-loss wording error.

## Content Critique

- The deep-ITM versus lottery-ticket contrast is strong.
- The capital-efficiency framing is useful, but should repeatedly say this is leverage and can still lose 100% of premium.
- The statement that freed cash is "all incremental return" is too strong. Option prices already embed rates, dividends, and financing through put-call parity. The cash yield is real, but not a free arbitrage.
- The tax section says a loss is an "ordinary capital loss." It should say capital loss; only limited amounts can offset ordinary income after netting against capital gains.
- The claim that LEAPS have no financing drag should be reframed. They do not create a separate margin-interest statement, but the option premium embeds interest rates, dividends, and volatility.
- "Options are the most tax-efficient leverage" needs caveats by option type, account type, holding period, exercise, wash sales, and short-leg combinations.
- The leveraged ETF comparison is useful, but the SSO/frictionless 2x calculation should disclose methodology and data source.
- Saying LEAPS have no volatility-decay problem is directionally true versus daily-reset ETFs, but LEAPS still have theta, vega, bid/ask, and roll risk.
- The four-tranche statement that stock replacement frees 75% of capital to fund other sleeves needs a portfolio-risk warning. If the freed cash goes into risky sleeves while beta exposure remains, total portfolio risk rises.
- Q9 says PMCC is covered in Week 30, but Week 30 is spreads/condors/butterflies. The next-week script previews poor-man's covered call, while the visible Week 38 file is `week38_leaps.md`.

## Cross-Reference And Consistency Issues

- Week 36 previewed Week 37 as dynamic withdrawals, but Week 37 is options leverage.
- Week 37 previews poor-man's covered call next week, but the visible Week 38 file is `week38_leaps.md`.
- Tax caveats should align with Weeks 25-28 and Week 36.
- Tranche language again needs alignment with the course-wide SOUL framework.

## Presentation Improvements

- Add a put-call parity box: stock replacement is not free leverage.
- Add a total-portfolio exposure example: beta exposure plus freed-cash redeployment.
- Add a tax decision tree: sell, expire, exercise, roll, combine with short leg.
- Add a liquidity checklist: open interest, bid/ask, midpoint fills, LEAPS chain depth.
- Add a rolling calendar diagram.

## YouTube Script Critique

The script is lively and the charts should hold attention. It needs a few corrections.

Specific improvements:

- Replace "LEAPS don't decay" with "LEAPS do not suffer daily-reset variance drag, but they still have theta and vega risk."
- Remove implementation details like theme observer, four-locale, and postMessage from the script. Viewers need the trading lesson, not website plumbing.
- Clarify that the LEAPS tax advantage applies only if holding-period and transaction rules are respected.
- Add a Stella challenge: "If I invest the freed cash into risky strategies, am I now overlevered?" That would make the barbell risk honest.
- Use consistent branding: the script says "Chan Investing" instead of Chanmainvest.

## Chart And Visual Feedback

Existing visuals are useful:

- Replacement capital chart.
- Leveraged ETF decay chart.

Recommended upgrades:

- Add put-call parity balance sheet.
- Add delta-adjusted exposure chart.
- Add LEAPS P&L surface by underlying move and IV change.
- Add roll-timing chart showing theta acceleration.
- Add total portfolio exposure before/after stock replacement.

## Interactive Demo Feedback

The `week37_replacement_lab.html` interactive is a strong idea but needs material fixes.

Issues and improvements:

- The option rows appear scaled by `target exposure / spot`, not by `target exposure / (spot × delta)`. If so, a 0.92 delta LEAPS controls only about 92% of the target delta exposure, not the same target exposure.
- Row labels use fixed deltas (0.90D, 0.70D, 0.30D), but strikes are fixed at 80%, 92%, and 106% of spot. Actual delta changes with IV, rates, dividends, and expiry. Display actual delta or solve strikes for target deltas.
- The 6-month and 3-month rows use half/quarter annual moves while the chart says 1-year P&L. That makes comparisons confusing.
- Add tax mode and roll assumptions.
- Add bid/ask and slippage assumptions.
- Add a warning when option liquidity would be poor.
- Show net portfolio exposure if freed cash is redeployed into risky sleeves.

## New Interactive Demo Ideas

- Put-call parity stock-replacement explainer.
- Delta-adjusted contract count calculator.
- LEAPS roll calendar and theta decay lab.
- IV-crush sensitivity simulator.
- Total portfolio leverage dashboard.

## Make It More Entertaining Without Watering It Down

The best hook is to put two accounts side by side: one buys 100 SPY shares, the other buys a deep-ITM LEAPS plus T-bills. Then reveal how similar the exposure is and where the hidden risks differ.

## Money-Making Usefulness

This lesson can be genuinely useful for sophisticated students, but only if sizing is disciplined. Used badly, stock replacement becomes hidden leverage rather than capital efficiency.

## SOUL Consistency Flags

- Aligns with SOUL's options-as-expression-tool and after-tax leverage themes.
- Needs more explicit total-risk control when freed capital is redeployed.
- Needs tranche-language consistency with the rest of the course.
