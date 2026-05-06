# Review: course/side04_tax_efficiency.md

## Overall Assessment

This is an ambitious and useful tax-efficiency lesson. It covers the right map: rate schedules, asset location, TLH, Roth conversions, HSA, account-filling order, withdrawal sequencing, and advanced tax-aware exposure tools.

It needs stronger caveats because tax is jurisdiction-specific and rule-sensitive. Several claims are too universal, and there is a direct internal contradiction on whether HSA comes before the 401(k) match.

## Content Critique

- The lesson's practical value is high. Asset location and TLH are exactly where retail investors can improve after-tax returns.
- Add visible `US tax law, as of 2026 assumptions` language. This lesson will become stale faster than most.
- The opening `taxes are almost always the largest line item` is plausible for high earners, but it mixes wage/lifetime taxes with investment-specific tax drag. Clarify the comparison.
- The 2026 rates and limits need source/date labels and a warning that law changes can invalidate them.
- The lesson says HSA is the first dollar, even before the 401(k) match, but §2.6 correctly puts the 401(k) match first. Standard rule: capture employer match before HSA unless there is a special vesting/liquidity issue.
- Treasury tax-equivalent-yield examples need recalculation/clarification, especially high-state examples such as California.
- `High-growth assets and crypto belong in Roth` needs risk caveats. Roth space is scarce; a high-volatility asset that goes to zero wastes tax-free space. The better rule is highest expected after-tax, risk-adjusted, conviction-weighted growth.
- RMD age should be birth-year-specific under SECURE 2.0, not simply `currently age 75` for everyone.
- Mega-backdoor Roth discussion should mention plan rules, nondiscrimination testing, after-tax subaccount availability, in-plan conversion, and earnings treatment.
- Backdoor Roth guidance should emphasize the pro-rata rule, aggregation across pre-tax IRAs, and Form 8606.
- TLH alpha numbers (`30-60 bps`, `$100k`) need model/source labels and should stress that the benefit is path-dependent and mostly tax deferral unless gains are offset in low-bracket years or eliminated by step-up/charity.
- Section 1256 rate math should include NIIT/state caveats and specify qualifying index options/futures only.
- Covered calls and collars against appreciated stock need qualified-covered-call, straddle, constructive-sale, and holding-period caveats. Too-tight collars can create tax problems.
- Box spreads and portfolio-margin loans are not reliably `sub-Treasury`; rates, margin-call risk, interest deductibility, and estate-tax/step-up assumptions matter.
- `Options and margin capture the remaining 20%` is unsupported and should be softened.

## Structure And Formatting Issues

- The lesson follows the correct Part 1 / Part 2 and decimal section structure.
- It is dense. Add a `safe beginner path` before advanced options/margin: match, HSA, 401(k), Roth/backdoor, taxable ETF placement, TLH checklist.
- Consider splitting advanced tax-via-options into a separate side lesson or add a strong warning box.

## YouTube Script Critique

The script has good practical energy and a clear Monday-morning call to action.

Specific issues:

- It repeats the HSA-before-401(k)-match contradiction.
- `You should have a plan you can implement on Monday` is motivating but should say `review` or `start implementing`, because Roth conversions, MLP moves, TLH, and option overlays may require professional advice.
- The Roth example (`$50k at 12% becomes $1.5M`) is compelling but should also show the risk of putting speculative assets in scarce Roth space.
- The optimizer does not truly `tell you what to do`; keep Stella's line but have Horace immediately say it is a rough educational model.

## Chart And Interactive Feedback

`side04_tax_optimizer.html` is useful but too recommendation-like for a simplified model.

Issues:

- The model uses 7% nominal gross return, while the lesson opening discusses 7% real return. Harmonize.
- Traditional IRA after-tax value is simplified as balance times `(1 - federal bracket)`, ignoring progressive brackets, state tax, RMDs, Social Security taxation, IRMAA, and filing status.
- The `After-tax wealth at 65 vs naive single-account` baseline is not clearly defined and may compare unlike tax wrappers.
- The `Suggested Roth conversion` is rule-of-thumb only; label it `illustrative bracket-fill estimate`, not a recommendation.
- The optimizer does not actually allocate user-entered assets across accounts; it displays a static grid and grows account balances. The script overstates what it computes.
- Add filing status, current taxable income, retirement income estimate, tax-rate-on-withdrawal, and expected return by asset class if this is meant to be more than a toy model.

## SOUL Consistency Flags

- Strong alignment with SOUL principle 15: after-tax return management via options and margin.
- The SOUL-aligned advanced section needs more warnings because options/margin can turn tax management into leverage risk.
- The lesson should make clear that tax optimization never outranks survival, liquidity, diversification, or legal compliance.
