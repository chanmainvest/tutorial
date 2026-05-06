# Review: course/week26_options_as_orders.md

## Overall Assessment

Week 26 has a strong teaching hook: a sold option as a limit order that pays you to wait. That mental model will help beginners understand cash-secured puts and covered calls without fear. The payoff diagrams, anchored $50k example, and yield-on-capital caveats are useful.

The lesson overstates the equivalence. Options are not strict upgrades over limit orders because path, expiry, assignment, tax, and opportunity cost all matter. That needs correction before readers use the lesson as an implementation guide.

## Content Critique

- The limit-order analogy is powerful and should stay.
- The reference account makes the examples easy to follow.
- The payoff diagrams are well chosen.
- The yield-on-cash section correctly warns that annualized option yields are upper bounds, not realized returns.
- The statement that a cash-secured put "never does worse than a limit order at the same strike" is too strong and can be false once path is considered. If the stock dips below the limit price, the limit order fills, then the stock recovers above the strike by expiry, the limit-order buyer owns the rebound while the put seller may only keep the premium.
- A covered call is also not identical to a limit sell order. A limit sell can execute intraperiod when the stock touches the price; a short call usually assigns at expiry or around ex-dividend mechanics. If the stock spikes above the strike and falls back, the limit seller exits, while the covered-call writer may remain long and only keep premium.
- The analogy should be reframed as "similar terminal payoff at expiry under specific assumptions," not a universal replacement.
- The claim that option overlays can turn a 7% expected return into 9-12% is too optimistic unless supported with backtests and risk adjustments. Premium is compensation for taking risk and capping upside, not free extra return.
- The 30-45 DTE and 5-10% OTM rule should be framed as a convention. Many practitioners choose by delta, IV rank, liquidity, and event calendar instead of percentage OTM.
- Tax handling is better than Week 25, but covered-call tax treatment still needs qualified-covered-call and assignment caveats.

## Cross-Reference And Consistency Issues

- Links to image scripts and the interactive use `course/image/...` and `course/interactive/...` from inside a `course/` markdown file. These may be broken relative paths; they likely should be `image/...` and `interactive/...` if meant to work from the lesson.
- The YouTube outro says Week 29 closes the arc with protective puts/collars, but Week 30 also appears to be part of the options arc.
- Script host labels use normal `Stella`/`Horace` this time, which is better than the all-caps issue in Weeks 22/25.

## Presentation Improvements

- Add a table: limit order versus CSP/CC, including expiry, intraperiod fill, cancellation, tax, assignment, and gap risk.
- Add a path-dependency example where the stock dips and recovers.
- Add a delta-based strike-selection note.
- Add an event-risk warning: earnings, ex-dividend dates, macro events.
- Add after-tax yield examples for taxable versus IRA/Roth.
- Add a "close early" decision tree.

## YouTube Script Critique

The script is clear and likely engaging. The "cheque attached" framing is sticky, but it risks overselling the strategy as strictly better than ordinary orders.

Specific improvements:

- Replace "strict upgrade" with a more precise formulation.
- Add Stella asking: "What if the stock hits my limit mid-month and then rebounds?"
- Show the path-dependency example visually.
- Add a one-sentence tax caveat in the main explanation, not only later.
- Avoid implying that weekly monitoring is always enough around earnings or ex-dividend dates.

## Chart And Visual Feedback

Existing visuals are useful:

- Cash-secured put payoff.
- Covered-call payoff.

Recommended upgrades:

- Add path-dependency chart comparing limit order and CSP.
- Add limit-order versus option timeline.
- Add annualized-yield decomposition: premium, assignment loss, taxes, cash yield.
- Add covered-call upside-cap comparison.
- Add assignment flowchart.

## Interactive Demo Feedback

The referenced `course/interactive/week26_orders_lab.html` is a strong concept. It should make payoffs and annualized yield tangible.

Suggested improvements:

- Add a path simulator, not only terminal price sliders.
- Let users compare limit order, CSP, covered call, and no trade on the same price path.
- Add tax drag and cash-sweep yield inputs.
- Add delta, probability ITM, and IV rank if possible.
- Add warnings when annualized yield is high because assignment risk is high.

## New Interactive Demo Ideas

- Limit order versus short put path simulator.
- Covered call versus limit sell path simulator.
- Wheel assignment loop simulator.
- After-tax premium-yield calculator.
- Strike selector using target delta and target annualized return.

## Make It More Entertaining Without Watering It Down

The best entertaining moment is the path-dependency trap. Let Stella think the CSP is always better, then show the stock dipping to $90, rallying to $105, and the ordinary limit order beating the option. That makes the lesson sharper and more trustworthy.

## Money-Making Usefulness

Very useful if corrected. This lesson can teach students to monetize planned entries/exits. The money-making edge is discipline and selectivity, not selling options mechanically every month.

## SOUL Consistency Flags

- Aligns with SOUL's use of options as execution and tax-expression tools.
- Needs stronger caveats so the options overlay is not portrayed as free structural alpha.
- Good fit with tranche discipline if the strategy is limited to quality names and predefined action prices.
