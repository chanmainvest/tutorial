# Review: course/week29_option_greeks.md

## Overall Assessment

Week 29 is a strong bridge from basic option mechanics to spreads. The worked Black-Scholes example is clear, the Greek intuition is mostly sound, and the strategy signatures for long calls, puts, covered calls, CSPs, and condors are very useful.

The lesson needs several technical corrections: the Greek/input framing is imprecise, the 1-day gamma claim is too high under the stated assumptions, the theta-decay interpretation contradicts the chart values, the Q&A delta-estimation shortcut appears wrong, and second-order-Greek references point to the wrong side lesson.

## Content Critique

- The opening motivation is excellent: Greeks explain pre-expiration behavior.
- The worked $100 ATM 30-day call example is well chosen and the headline values are plausible.
- The delta section correctly distinguishes delta from true risk-neutral probability ITM.
- The statement "five inputs matter ... so there are five Greeks" is imprecise. Strike is an input but not a moving market input in position management, and gamma is a second derivative with respect to spot, not a separate input.
- "The Greeks have closed-form answers" is true for Black-Scholes European options, but not generally for American equity options with discrete dividends. Add a model caveat.
- The claim that a 1-day ATM call can have gamma north of 1.0 does not match the lesson's own $100, 20% vol assumptions. It is closer to ~0.38 per $1 under Black-Scholes. Gamma can get very large, but quantify accurately.
- The theta-decay text says roughly two-thirds of a 90-day ATM call's premium is gone by 30 DTE. The chart numbers show the opposite: from $4.05 at 90 DTE to $2.45 at 30 DTE is about 40% gone, with most of the remaining value burning in the final 30 days.
- The Q&A shortcut for estimating delta shifts by `$0.05 / (sigma sqrt T)` appears badly wrong. It gives an impossible ~0.88 delta change per $1 for the worked example. A gamma-based approximation would be more accurate.
- The long-call strategy description says "theta and rho-bleed." Rho is rate sensitivity, not daily bleed.
- Vega discussion is strong, but avoid mixing IV rank and IV percentile language after Week 27/28 issues.
- The covered-call and CSP Greek equivalence is useful and should stay.

## Cross-Reference And Consistency Issues

- The intro references `side25` as second-order Greeks, but the visible side lesson list has `side20_greeks_deep_dive.md`; `side25` appears to be hedge funds.
- Week 29 correctly previews Week 30 spreads/condors.
- References to LEAPS Week 38 and VIX Week 40 should be verified when those files are reviewed.

## Presentation Improvements

- Add a model-caveat box: European/no-dividend Black-Scholes versus American equity options.
- Add a units table: per share, per contract, per day, per vol point, per 1% rate.
- Add a corrected theta-decay decomposition: value lost from 90 to 30 DTE versus 30 to expiry.
- Add a gamma-by-DTE table with exact values under the same assumptions.
- Add a Greek-sign table for long/short calls/puts.
- Add a Greek P&L attribution example: delta + gamma + theta + vega.

## YouTube Script Critique

The script is clear and probably the best format for this lesson because Greeks are visual. The analogy stack is useful without being childish.

Specific improvements:

- Correct the gamma magnitude.
- Correct the theta-decay interpretation.
- Add one concrete P&L decomposition: stock up $2, IV down 1 point, one day passes.
- Mention that Greeks are local approximations, not guarantees over large moves.
- Keep the "without calculus" title, but include the formulas in the reading for credibility.

## Chart And Visual Feedback

Existing visuals are useful:

- Greeks versus spot chart.
- Theta-decay chart.

Recommended upgrades:

- Add Greek P&L waterfall.
- Add gamma versus DTE heatmap.
- Add vega versus DTE heatmap.
- Add covered-call/CSP Greek signature chart.
- Add long-gamma versus short-gamma payoff-path visual.

## Interactive Demo Feedback

The referenced `course/interactive/week29_greeks_lab.html` is exactly the right tool. Sliders for spot, strike, DTE, IV, and rates should make local sensitivity concrete.

Suggested improvements:

- Add per-share/per-contract toggle.
- Add P&L attribution for a user-specified scenario.
- Add warning that Greeks are local and change after the move.
- Add call/put parity comparison.
- Add dividend-yield input or a note explaining the simplified no-dividend model.
- Add gamma and vega heatmaps by DTE and moneyness.

## New Interactive Demo Ideas

- Greeks P&L attribution lab.
- Delta-hedging simulator.
- Gamma risk into expiry simulator.
- Earnings vol-crush simulator.
- Covered-call versus CSP Greek equivalence visualizer.

## Make It More Entertaining Without Watering It Down

The best entertaining segment is "why my correct call lost money." Give Stella a long call, the stock moves up, IV collapses, and the P&L still loses. Then decompose the loss with Greeks. That is memorable and saves real money.

## Money-Making Usefulness

This lesson helps students make money mainly by avoiding naive option trades. Greeks turn option P&L into accountable risk, which should reduce oversized short-gamma and long-vega mistakes.

## SOUL Consistency Flags

- Strongly aligned with SOUL's options-as-expression-tool requirement.
- Good foundation for vol-surface-aware technical analysis and post-COVID option-market mechanics.
- Needs exact cross-references to the actual second-order Greeks side lesson.
