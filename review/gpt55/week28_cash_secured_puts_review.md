# Review: course/week28_cash_secured_puts.md

## Overall Assessment

Week 28 has the right moral center: cash-secured puts should be used to bid on securities the investor already wants to own, not as yield farming. The warning against influencer-style annualized-yield marketing is excellent, and the PUTW comparison gives needed humility.

The lesson needs technical corrections around the limit-order analogy, collateral yield, historical rate context, PUTW methodology, and next-week references. It should also stop calling CSPs "safe-end" activity without clarifying that they are still equity downside and short-vol exposure.

## Content Critique

- The opening is clear and practical.
- The phrase "premium is not your edge; the discount to where you wanted to buy is your edge" is excellent.
- The lesson correctly warns that high premium is compensation for volatility and assignment risk.
- The text says the CSP buys the stock if it "ever trades" at the strike during the next 30 days. That is not how assignment normally works. A put is not a limit order triggered by an intraperiod print; assignment usually happens at expiry, with early exercise possible mainly when deep ITM/carry makes it rational.
- The comparison to a day limit order is too narrow. Limit orders can be good-till-canceled and can be canceled/modified without buying back an option.
- Delta-as-assignment-probability should repeat the risk-neutral-probability caveat from Week 27.
- Collateral yield is broker/account-specific. Some brokers pay little on cash sweeps, some allow Treasury/MMF collateral, and IRA rules vary. Do not assume every CSP collateral account earns T-bill yield.
- The statement that T-bills paid 0% in the 1990s is wrong. That sounds like the 2010s, not the 1990s.
- Assignment psychology is useful, but "the only loss scenario is panic-selling" is too strong. The stock can keep falling after assignment; the loss is real even if the investor behaves well.
- CSPs on index ETFs and quality stocks are conservative equity-entry trades, not true safe-end assets like T-bills. Calling them safe-end activity needs a clear distinction from cash/bonds.
- The PUTW methodology appears wrong. The CBOE S&P 500 PutWrite Index is commonly described as selling monthly at-the-money SPX puts against T-bill collateral, not ~2% OTM puts. Verify and correct.
- The PUTW discussion should distinguish "does not own upside" from "cap on upside"; put-write funds are not covered-call funds.

## Cross-Reference And Consistency Issues

- The YouTube outro says next week is spreads/bull-put credit spreads, but the visible course sequence has Week 29 as option Greeks and Week 30 as spreads/condors.
- Week 28 should connect to Week 27 covered calls and likely to `side30_wheel_strategy.md` if the wheel is not a core Week 30 lesson.
- The safe-end/barbell language needs alignment with the SOUL tranche structure and prior lessons.

## Presentation Improvements

- Add a limit order versus CSP table covering intraperiod fills, expiry, cancelability, assignment, taxes, and collateral.
- Add a broker-collateral note: cash sweep, Treasury bills, MMFs, and account restrictions vary.
- Add a rate-history correction: 1990s versus 2010s.
- Add a PUTW methodology footnote with index rules.
- Add a post-assignment plan: hold, covered call, sell because thesis changed, tax considerations.
- Add a concentration rule: one assignment should not dominate the portfolio.

## YouTube Script Critique

The script has a strong anti-hype opening. It should work well because it pushes against bad options content.

Specific improvements:

- Correct the "if it trades there" implication.
- Replace the next-week preview with Week 29 Greeks if that is the actual sequence.
- Add a clear example where the stock trades below the strike and recovers before expiry, showing why CSP is not exactly a limit order.
- Add a brief broker-collateral caveat.
- Avoid saying the wheel breaks only if the investor panic-sells; it also breaks if the underlying thesis was wrong.

## Chart And Visual Feedback

Existing visuals are useful:

- CSP yield curve by delta.
- PUTW versus SPY chart.

Recommended upgrades:

- Add path-dependency chart comparing GTC limit buy and CSP.
- Add assignment probability versus premium chart.
- Add collateral-yield decomposition chart.
- Add PUTW methodology diagram.
- Add post-assignment wheel flowchart.

## Interactive Demo Feedback

The referenced `course/interactive/week28_put_writer.html` is a strong tool. It should help readers compare delta, DTE, premium, breakeven, and assignment odds.

Suggested improvements:

- Add broker cash-yield input.
- Add taxable versus IRA/Roth mode.
- Add path simulation, not only terminal outcomes.
- Add assignment concentration warning.
- Add earnings/event-risk toggle for single names.
- Add PUTW-style systematic preset versus targeted CSP preset.

## New Interactive Demo Ideas

- CSP versus GTC limit-order path simulator.
- Put assignment concentration stress test.
- CSP after-tax yield calculator.
- Wheel lifecycle simulator.
- PUTW methodology explorer.

## Make It More Entertaining Without Watering It Down

The influencer-yield-farming takedown is already a strong video hook. Add a "headline yield versus actual account value" reveal: show premium collected, then show assignment loss and tax drag.

## Money-Making Usefulness

Very useful if tightened. CSPs can improve entry discipline and monetize patience, but only when used on names the student wants to own and in accounts where tax and collateral treatment make sense.

## SOUL Consistency Flags

- Aligns with SOUL's options-as-execution-tool and tax-wrapper philosophy.
- Needs clearer separation between safe-end cash/T-bills and conservative equity-entry CSPs.
- Reinforces the course's view that options are expression tools, not automatic alpha.
