# Review: course/week36_income_portfolio.md

## Overall Assessment

Week 36 is practical and important. The focus on after-tax yield, account location, sequence risk, and distribution-side portfolio design is exactly the kind of material that can help students make better real-world decisions.

The lesson needs tax precision and consistency fixes. The largest issue is that the taxable model portfolio relies on municipal bonds, but the interactive groups bond exposure into a taxable corporate sleeve, so the lab may not reproduce the lesson's central after-tax point. The four-tranche mapping also conflicts with earlier tranche language.

## Content Critique

- The accumulation-to-distribution shift is well explained.
- The "pre-tax yield is marketing; after-tax yield is spent" message is strong and memorable.
- Tax treatment is too simplified in several places. Add caveats for NIIT, state differences, qualified-dividend holding-period rules, return of capital, 1256 contracts, and fund-specific tax character.
- The lesson says equity-option premium is almost always short-term income. This is too broad. Index options, Section 1256 products, ELNs, and funds like SPYI/PUTW may have different tax treatment.
- SPYI is listed in dividend equity but described as inheriting the option-premium tax problem. That should be verified because some S&P index option strategies may use 1256 treatment or other tax-managed distributions.
- REIT taxation needs more precision. The 199A deduction applies to qualified REIT dividends, and REIT distributions can include ordinary income, capital gains, and return of capital.
- The 4% rule update is useful, but "variable spending has essentially no behavioural cost" is too optimistic. Spending cuts are behaviorally meaningful.
- Safe-withdrawal-rate figures for April 2026 need source labels and should be framed as estimates, not a settled number.
- The distribution-side four-tranche table conflicts with prior tranche descriptions in Weeks 34-35 and likely with SOUL terminology.
- The statement that intermediate Treasuries are the least useful distribution sleeve is too strong. Intermediate bonds still provide liquidity, income, and recession hedge properties in some regimes.
- Model B says after-tax equals pre-tax inside an IRA. That is true inside the account, but traditional IRA withdrawals are later taxed as ordinary income. Distinguish Roth from traditional.
- JAAA/JBBB in Q10 are CLO ETFs, not broad retirement-income fund-of-funds substitutes. They need a stronger complexity/risk caveat.

## Cross-Reference And Consistency Issues

- Week 35 previewed Week 36 as industry analysis, but Week 36 is income portfolio construction.
- Week 36's outro previews Week 37 as dynamic withdrawals, but the visible Week 37 file is `week37_options_leverage.md`.
- Week 36 references Weeks 26-28 for options; those earlier option tax caveats should be fixed before this capstone relies on them.
- Four-tranche terminology differs across Weeks 34, 35, and 36.

## Presentation Improvements

- Add a tax-character table by product: Treasury ETF, muni ETF, corporate bond ETF, REIT ETF, covered-call ETF, index-option ETF, ELN fund.
- Add a Roth versus traditional IRA caveat.
- Add a "not all option income is taxed the same" box.
- Add a source note for all April 2026 yields.
- Add a model-portfolio assumption box: taxes, state, expenses, volatility, drawdown method.
- Add a distribution-flow diagram: cash sleeve, bond sleeve, equity refill, bad-year draw rules.

## YouTube Script Critique

The script is engaging and the after-tax flip is a strong visual moment.

Specific improvements:

- Avoid saying JEPI's taxable advantage is definitely negative across all investors and regimes; frame it as often much smaller after tax and total-return drag.
- Clarify that 199A is a deduction, not a direct discount.
- Add a Stella question about Roth versus traditional IRA taxation.
- Correct the Week 37 preview once the sequence is reconciled.
- Add a warning that product tax character must be checked on the fund's tax documents.

## Chart And Visual Feedback

Existing visuals are useful:

- Pre-tax yield hierarchy.
- After-tax yield chart.

Recommended upgrades:

- Add product tax-character heatmap.
- Add account-location matrix.
- Add 4% rule success-rate chart by starting yield.
- Add sequence-of-returns path comparison.
- Add model portfolio drawdown simulation.

## Interactive Demo Feedback

The `week36_income_builder.html` interactive is useful, but it does not fully match the lesson's taxable model.

Issues and improvements:

- Add a municipal bond sleeve or a tax-exempt toggle. Model A uses VTEB, but the interactive's corporate sleeve is taxed like ordinary corporate income.
- Add after-tax income contribution chart, not only pre-tax contribution.
- Show Roth versus traditional IRA distinction.
- Add NIIT and state-tax customization beyond 0/5/10.
- Add fund-specific tax character overrides for option-premium products.
- Explain that volatility/drawdown estimates are heuristic and not retirement-safe-withdrawal simulations.

## New Interactive Demo Ideas

- Account-location optimizer.
- 4% rule and variable-withdrawal simulator.
- Roth versus traditional IRA after-tax withdrawal lab.
- Product tax-character comparison tool.
- Bad-decade sequence-risk simulator.

## Make It More Entertaining Without Watering It Down

The strongest video moment is to show JEPI winning the pre-tax chart, then watch it shrink after tax and total-return drag. That gives viewers a clean "brokerage yield is not spendable yield" lesson.

## Money-Making Usefulness

This lesson has high money-making usefulness because tax location and withdrawal rules can improve spendable cash without requiring stock-picking skill. The usefulness depends on fixing product-specific tax details.

## SOUL Consistency Flags

- Aligns with SOUL's emphasis on after-tax return management and income/options as tools.
- Needs tranche terminology cleanup to match the course-wide four-tranche framework.
- The barbell/distribution language should distinguish Horace's preferred construction from universal retirement planning advice.
