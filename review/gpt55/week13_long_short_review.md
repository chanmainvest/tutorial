# Review: course/week13_long_short.md

## Overall Assessment

Week 13 is strong. It teaches shorting as a professional toolkit rather than a retail action plan, and it repeatedly tells beginners not to naked short casually. The mechanics, payoff asymmetry, borrow-cost explanation, squeeze discussion, and gross/net/beta-neutral vocabulary are valuable.

The lesson should tighten a few technical claims, especially tax treatment, option substitutes, and the synthetic market-neutral chart. It should also soften the claim that alpha mostly lives on the short side, because SOUL's alpha taxonomy is broader and because many readers should still default to long-only compounding.

## Content Critique

- The opening does the right thing: long-only remains the default, and shorting is introduced as a toolkit.
- The short mechanics are clear and practical. Borrow, sale proceeds, cover, return, borrow fee, and dividend obligations are explained well.
- The asymmetric loss section is the best part of the lesson. It protects students from thinking a short is just an upside-down long.
- GameStop is a good case study because it connects short interest, options flow, dealer hedging, margin calls, and forced covering.
- The gross/net/beta-neutral vocabulary is essential and well placed before pair trading.
- The borrow-cost section is useful and should be retained.
- "Alpha mostly lives on the short side or in the spread" is too strong. Structural and relative-value alpha often require shorting, but SOUL also emphasizes liquidity, time horizon, sector rotation, passive abandonment, and regime awareness. Do not make long-only sound alpha-less.
- The options-as-constructive-shorts section is directionally right, but it should remind readers that options introduce implied-volatility, timing, liquidity, spread, and theta risks.
- The tax paragraph is oversimplified. A naked short is not generally marked to market continuously for a typical retail account; tax treatment depends on jurisdiction, holding period, constructive sale rules, Section 1256 status for some instruments, and product type.
- The market-neutral comparison chart is synthetic. It should be visually and verbally labeled as a model, not evidence that market-neutral strategies deliver a smooth 4% real return.
- The lesson should add operational broker risk: margin rules can change, borrow availability can vanish, and broker liquidation can happen at bad prices.

## Cross-Reference And Consistency Issues

- The lesson references later Weeks 47 and 49. Confirm those week topics match the final course map before publication.
- Q10 says long Coke / short Pepsi has roughly zero net beta by construction. A dollar-neutral pair only has zero beta if the beta exposure is matched; the pair should be beta-adjusted if beta neutrality is the goal.
- Q11 introduces a four-tranche breakdown that may not match the exact SOUL tranche definitions. Define the tranche taxonomy consistently across the course.

## Presentation Improvements

- Add a warning box: "For most readers, use puts or cash, not naked shorts."
- Add a short-sale cash-flow diagram: borrow -> sell -> collateral -> borrow fee/dividends -> cover -> return.
- Add a margin-call example with numbers as the stock rises.
- Add a borrow-cost calculator example: correct thesis, wrong economics.
- Add a table comparing naked short, long put, put spread, inverse ETF, and cash reduction.
- Add a checklist before any short: liquidity, borrow, short interest, options activity, catalyst, max loss, stop, position size.

## YouTube Script Critique

The script is engaging and appropriately scary. The repeated "do not naked short illiquid squeeze names" message is good pedagogy.

Specific improvements:

- Make Stella ask whether buying a put is "free safety" so Horace can explain theta and implied volatility.
- When discussing the synthetic market-neutral chart, explicitly say: "This is a model, not a fund return series."
- Add one real math example: short at $100, stock goes to $180, margin requirement rises, borrow cost accrues.
- Reduce the phrase "alpha lives on the short side" to "some alpha streams require a short leg."
- Mention that a stop order does not guarantee the exit price in a gap or squeeze.

## Chart And Visual Feedback

Existing visuals are useful:

- Payoff diagrams are essential and should stay.
- Market-neutral versus 60/40 chart is conceptually useful but should be clearly synthetic.

Recommended upgrades:

- Add a GameStop squeeze flowchart.
- Add a borrow-cost drag chart.
- Add a margin-call ladder.
- Add a long put versus naked short payoff/cost comparison.
- Add a gross/net/beta-neutral exposure diagram.

## Interactive Demo Feedback

The referenced `course/interactive/week13_long_short_lab.html` is the right kind of tool. Sliders for long beta, short beta, idiosyncratic alpha, net beta, gross exposure, Sharpe, and drawdown should make neutrality intuitive.

Suggested improvements:

- Add borrow cost and trading-cost sliders.
- Add a short-squeeze shock button.
- Add a beta-adjusted pair mode.
- Add an option substitute mode: naked short versus long put versus put spread.
- Add warnings when short exposure exceeds a beginner-safe threshold.

## New Interactive Demo Ideas

- Short squeeze simulator: short interest, float, borrow rate, call buying, dealer gamma, margin call threshold.
- Borrow-cost breakeven calculator.
- Pair beta-adjustment calculator.
- Naked short versus put payoff explorer.
- L/S exposure dashboard for gross, net, beta, factor, borrow, and liquidity risk.

## Make It More Entertaining Without Watering It Down

The GameStop segment is naturally dramatic. Use it as the emotional center, but make the takeaway sober: the student should feel that shorts are powerful tools with sharp edges, not forbidden magic.

## Money-Making Usefulness

This lesson helps students make money mostly by preventing catastrophic losses. The most profitable lesson for many retail investors will be: do not short obvious bubbles naked; use capped-loss structures or do nothing.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #1, #4, #5, #8, #12, and #13.
- Needs cleaner wording around alpha sources so it does not overstate short-side alpha versus SOUL's broader structural-alpha list.
- Tranche terminology should be harmonized with SOUL.md.
- Reinforce that retail investors have a solvency advantage only if they avoid leverage and margin traps.
