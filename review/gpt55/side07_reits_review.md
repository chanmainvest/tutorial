# Review: course/side07_reits.md

## Overall Assessment

This is a strong, practical lesson. It correctly warns that public REITs behave like public equities with rate sensitivity, not like slow-moving private property. The sector-composition update is especially valuable for viewers who still think REITs mostly mean malls and offices.

The biggest fixes are precision and consistency: REIT sizing sleeve, account-location nuance, duration math, and the interactive's missing horizon control.

## Content Critique

- `REITs are stocks, not real estate` is memorable but a little too absolute. Better: `public REITs are real-estate operating companies priced through the equity-market wrapper`.
- All April 2026 sector weights, AUM, fees, yield, beta, and duration estimates need source/date labels.
- The `199A made permanent in 2025` statement needs a tax-law source/date caveat.
- `REITs belong in the IRA whenever you have room` is directionally right for ordinary-income distributions, but `full stop` is too strong. Taxable REIT distributions can include return of capital/capital gains, 199A applies in taxable, and Traditional IRA withdrawals are eventually ordinary income.
- The 90% distribution rule does not mean REITs cannot retain meaningful cash flow for growth. Taxable income is reduced by depreciation, and REITs may fund growth through retained cash flow, retained 10%, debt, and equity issuance.
- Mortgage REITs are correctly separated from equity REITs, but `blew up in 1998, 2008, and 2020` should be softened to severe dislocations/large drawdowns; not every mREIT permanently failed.
- `EXR` should not be grouped with industrial logistics. It is self-storage; separate it from PLD/industrial warehouses.
- Sector ETFs mentioned (`SRVR`, `VPN`, etc.) should be checked for current existence/liquidity before being suggested.
- Duration math is overstated. A 250 bp rate rise times 7-year duration implies roughly a 17.5% price hit, not 25%. VNQ's 2022 loss also reflected equity risk premia, cap-rate spreads, leverage, and sector stress.
- `Private commercial real estate was roughly flat` in 2022 is too broad. Private marks lagged, but offices and some transaction comps were already impaired.
- §2.3 says REITs belong in the income or stores-of-value sleeve; §2.4 says income, not stores-of-value. Standardize.
- Sizing varies between `5-10% of income sleeve`, `5-10% of equity sleeve`, and interactive percent of total portfolio. Pick one and explain alternatives.
- The direct-property alternative above 15% needs a strong warning: direct real estate adds leverage, tenant risk, maintenance, concentration, illiquidity, local regulation, and operational work.

## Structure And Formatting Issues

- The decimal structure is correct.
- The lesson has a good sequence: wrapper, types, rates, placement.
- Add a small comparison table: public REITs vs private direct property vs mREITs vs real-estate private funds.

## YouTube Script Critique

The mall-vs-data-center opening is strong and visually clean. It immediately updates the viewer's mental model.

Needed fixes:

- The line about managing `a hundred-and-sixty buildings` is wrong. VNQ has roughly 160 holdings/companies, not 160 buildings.
- `Duration math predicted a 25% drop` should be corrected or explained with spreads/equity beta.
- The script says the lab has a horizon control and lets the viewer watch yield compound over 20 years; the current interactive does not have a horizon slider.
- `Default ETF: VNQ` is fine as an educational default, but avoid making it sound like a personal recommendation.

## Chart And Interactive Feedback

`side07_reit_lab.html` is useful as a rate-shock intuition tool, but it is narrower than the script says.

Issues:

- No horizon slider exists, despite the script saying to set the horizon to 20 years.
- The inflation slider mostly subtracts CPI from current yield; it does not actually model multi-year rent resets or compounding.
- The code calculates `yld_5y` but never displays it, so the caption's inflation-growth claim is not visible.
- The 2008 preset uses a negative rate shock, which can make REITs look helped by rates even though 2008 losses came from credit stress, leverage, and equity-market collapse.
- `Real yield` should be labeled `current yield minus CPI`, not a total-return expectation.
- Add an equity-shock/credit-spread slider so 2008 and 2020 can be modeled honestly.
- Add sector mix presets: broad VNQ, towers/data centers, office stress, mREIT carry trade.

## SOUL Consistency Flags

- Good SOUL consistency: REITs are not crisis alpha and should not be mistaken for the stores-of-value sleeve.
- The direct-property-with-fixed-rate-mortgage point aligns with the inflation lesson, but needs risk and leverage caveats.
- The lesson should continue teaching orthodox REIT benefits first, then Horace's caution that public wrappers can fail exactly when retail investors expect private-property behavior.
