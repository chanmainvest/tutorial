# Review: course/side08_fund_fees.md

## Overall Assessment

This is a highly useful lesson and the topic belongs in the course. Fees are one of the few variables retail investors can directly control, and the Bogle framing is exactly right.

However, the headline number is wrong/inconsistent. The lesson says a 1% fee costs about `$400,000` versus a 5 bp ETF on a `$100,000`, 30-year, 8% example, but the same lesson's own math shows a gap around `$226,000`.

## Content Critique

- The central message is correct: fees compound against the investor and are a strong predictor of net fund outcomes.
- The opening `$400,000` / `40% of terminal wealth` claim for 1% versus 5 bp is not supported by the table. With `$100,000`, 30 years, 8% gross, 0.05% ends near `$987k`; 1.00% ends near `$761k`; the gap is about `$226k`.
- The chart caption repeats the incorrect `$400,000` gap for 0.05% versus 1.00%.
- `8% gross` is called close to long-run real US equity return. It is closer to a nominal long-run assumption; if using real wealth, inflation assumptions must be explicit.
- `1.0% extra fee on top of 5 bp ... closer to $400k` is still not correct under the stated assumptions.
- Transaction costs do not show up as `acquired fund fees and expenses`; AFFE is for fees of underlying funds. Transaction costs generally show up through performance and filings, not the headline ER.
- Q1 references Form N-Q, which has been replaced for funds by modern N-PORT/N-CEN reporting. Update the filing language.
- The target-date section overstates sameness. Active target-date funds may use active underlying funds and different glidepaths. Say `similar asset-class exposures`, not `the same passive ETFs`.
- The script says Fidelity Freedom 2050 holds the same Vanguard Total Stock Market underneath; that is false.
- `Fire the advisor and buy the five ETFs` is too glib. Some advisors add value through planning, tax coordination, estate work, behavioral coaching, and complex situations; the better critique is fee transparency and value delivered.
- Q8's advisor-cost dollar estimate should be recalculated. A 2% all-in drag on a `$500k` portfolio for 30 years is much more than `$700k` under an 8% gross assumption.
- The hedge-fund section has a typo/logic issue: `despite a positive gross alpha of 0%` should be `despite matching the index gross` or similar.
- The +30/-10/+30/-10 hedge-fund example should be recalculated with high-water marks and management-fee timing; the current `closer to flat` claim likely overstates the damage.
- Renaissance/Citadel comparison should be handled carefully. Medallion is the classic closed-to-outside-capital example; Citadel's investor-access situation is not the same.

## Structure And Formatting Issues

- The lesson structure is clean and follows the course format.
- It would benefit from a simple `fee audit checklist`: ER, 12b-1, load, AFFE, advisor fee, transaction cost, tax-cost ratio, bid/ask spread, performance fee.
- Add source labels to Morningstar, SPIVA, target-date fund fees, hedge-fund fee-capture studies, and AUM/fee examples.

## YouTube Script Critique

The video hook is excellent but currently built on the wrong number.

Needed fixes:

- Change the headline from `$400,000` to the correct gap under the chosen assumptions, or change assumptions so `$400,000` is true.
- The script says `Four hundred thousand. Forty percent of your terminal wealth`; under the displayed chart, 1% versus 5 bp is about 23% of terminal wealth.
- The target-date line claiming Fidelity Freedom holds the same Vanguard Total Stock Market underneath must be corrected.
- The hedge-fund example is engaging but should use a cleaner `gross return / hurdle / performance fee / net return` table.
- The Bogle table should avoid unsupported claims like `10% annuity wrapper` unless a separate annuity lesson/source backs it.

## Chart And Interactive Feedback

`side08_fee_calculator.html` is useful and directly supports the lesson, but it only models expense ratio.

Issues:

- The interactive correctly computes about `$226k` gap for the Bogle preset, contradicting the lesson's `$400k` headline.
- `Total fees paid` is only fee dollars deducted, not total foregone wealth from fee drag. Keep both metrics visible: dollars deducted and terminal wealth gap.
- `Fees as % of gross gain` uses deducted fee dollars as numerator; it does not include lost compounding on fees. Rename or add a second KPI.
- The hedge-fund preset uses only 2% management fee and ignores the 20% performance fee, hurdle, and high-water mark.
- Add controls or presets for loads, advisor AUM fees, AFFE/fund-of-funds, transaction-cost drag, tax-cost ratio, and performance fees.
- Add a `target-date comparison` preset showing 0.08%, 0.12%, 0.75%, and 1.09% side by side.

## SOUL Consistency Flags

- Strongly aligned with the alpha-is-rare/passive-default principle.
- The lesson should keep the orthodox Bogle rule first, then explain where Horace would pay higher fees only for genuine scarce exposure, structural alpha, or tax/option implementation that earns its keep.
