# Review: course/week30_spreads_condors.md

## Overall Assessment

Week 30 is a useful introduction to defined-risk structures. It explains verticals, condors, and butterflies with clear payoff formulas and shows why spreads solve the capital-intensity problem of cash-secured puts and naked short options.

The lesson needs important corrections before publication. It overstates the safety and barbell role of spreads, has several volatility/Greek inaccuracies, contains likely broken relative links, has a typo in iron-condor capital requirement, and previews the wrong Week 31 topic.

## Content Critique

- The motivation is strong: single-leg options are blunt and capital-heavy.
- The four vertical-spread definitions are clear.
- The bull-call worked example is accessible.
- The statement that a $50k account can run "fifty" spreads in parallel is dangerous without correlation and aggregate max-loss caveats. Defined risk per trade can still become portfolio-level overleverage.
- "Defined-risk options ARE the barbell" is too absolute. Spreads are tools for the asymmetric sleeve, not the whole barbell.
- The claim that iron condors monetize markets mean-reverting inside their range about 70% of the time is misleading. The 68% figure comes from a one-standard-deviation model assumption, not necessarily from real-world mean reversion.
- The text says debit spreads are short-vega and parenthetically says "you bought volatility." That is internally contradictory and generally wrong. Debit spreads can be net long or short vega depending strikes and spot; they often reduce vega versus a naked long option but are not automatically short-vega.
- The iron-condor capital line says "Capital required: $500 minus credit" when it should be $5 width minus credit, or $500 per contract before credit.
- The condor POP/expected-value statement should add that model POP is not edge by itself; transaction costs, skew, gap risk, and realized-versus-implied vol determine expectancy.
- The condor chart caption says tighter shorts give wider profit zones "in theta terms"; the price profit zone is narrower. Rephrase.
- The butterfly section uses "gamma-scalping a butterfly" loosely. A long butterfly near the body is typically short gamma/short vega and positive theta; gamma scalping usually refers to long-gamma hedging.
- The butterfly discussion around earnings/catalysts needs more IV nuance. Long butterflies can benefit from IV crush near the body but can be harmed by IV expansion before an event.
- The capital-efficiency comparison table is too loose. Long stock does not have max profit of ~$1,000 carry, and a short straddle does not have the same kind of bounded range thesis as a condor.
- Yield-on-capital for butterflies at peak is not comparable to monthly yield on other structures and may encourage bad sizing.
- The 1256 section should say the advantage is roughly a 10 percentage-point tax-rate difference, not necessarily 10 percentage points of after-tax return.

## Cross-Reference And Consistency Issues

- Links to `course/image/week30_*.py` and `course/interactive/week30_spread_builder.html` may be broken from inside a `course/` markdown file; use `image/...` and `interactive/...` if those are intended relative links.
- The lesson and YouTube outro preview Week 31 as IV rank/vol regimes, but the visible file is `course/week31_yield_curves.md`.
- Week 30 should inherit the Week 29 Greek corrections before relying on gamma/vega/theta claims.

## Presentation Improvements

- Add a warning box: defined risk does not mean small risk, and many defined-risk trades can still lose the portfolio.
- Add a per-trade and portfolio-level max-loss sizing example.
- Add a Greek-sign table for each spread type.
- Add a model-risk box for POP: risk-neutral model, skew, event risk, gap risk, transaction costs.
- Add an assignment/pin-risk checklist for spreads near expiry.
- Add a tax note distinguishing SPX/NDX/RUT from SPY/QQQ/IWM and explaining notional size.

## YouTube Script Critique

The script is engaging and practical. The transition from single-leg collateral to spreads is a strong hook.

Specific improvements:

- Avoid saying spreads have "same edge" as single legs; they have different Greeks, costs, and payoff caps.
- Correct the Week 31 preview.
- Add a pin-risk example: short strike at expiry, one leg assigned, long leg not automatically exercised as expected.
- Add a sizing rule: max loss per structure and aggregate correlated max loss.
- Make the condor section say "model win rate" rather than implying a natural win-rate edge.

## Chart And Visual Feedback

Existing visuals are useful:

- Spread payoff diagrams.
- Condor POP bar chart.

Recommended upgrades:

- Add spread Greek profile chart.
- Add payoff-plus-probability overlay.
- Add defined-risk portfolio overleverage example.
- Add assignment/pin-risk timeline.
- Add tax comparison: SPX versus SPY condor.

## Interactive Demo Feedback

The referenced `course/interactive/week30_spread_builder.html` is the right tool. It should be especially useful if it shows max profit/loss, POP, breakevens, and payoff diagrams live.

Suggested improvements:

- Add portfolio-level max-loss tracker.
- Add commission and bid/ask slippage assumptions.
- Add Greek profile outputs for each structure.
- Add event-risk/IV-skew adjustment warning.
- Add pin-risk warning when short strikes are near spot close to expiry.
- Add SPX/SPY tax and notional-size toggle.

## New Interactive Demo Ideas

- Spread structure selector by view: direction, vol, range, catalyst.
- Condor model-risk simulator using realized vol above/below IV.
- Butterfly path simulator with early exit targets.
- Pin-risk assignment simulator.
- Portfolio spread max-loss aggregator.

## Make It More Entertaining Without Watering It Down

The best dramatic reveal is that a $320 max-loss condor can feel safe until the student opens 50 of them and realizes the book has $16,000 of correlated max loss. That makes defined-risk sizing unforgettable.

## Money-Making Usefulness

The lesson is useful because it teaches students to cap tail risk and use capital efficiently. The money-making edge, however, is not the structure itself; it is correct sizing, good liquidity, fair vol pricing, and disciplined exits.

## SOUL Consistency Flags

- Aligns with SOUL's options-as-expression-tool requirement and asymmetric sleeve architecture.
- Needs more caution that spreads are not the barbell itself.
- Supports the vol-aware worldview but must correct vega/gamma language before becoming canonical.
