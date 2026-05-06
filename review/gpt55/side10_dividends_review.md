# Review: course/side10_dividends.md

## Overall Assessment

This is a good income-sleeve lesson. It balances Modigliani-Miller theory with real-world taxes, behavior, and dividend-growth quality screens. The SCHD/VYM/DGRO/NOBL/SPYI comparison is useful for retail investors.

The lesson needs tax-bracket reconciliation, source labels, and more precision around covered-call ETF distributions and foreign withholding.

## Content Critique

- The opening dividend-return statistics need source labels and should distinguish income share of total return from reinvested-dividend contribution to terminal wealth.
- Qualified-dividend rules are mostly right, but option hedging should reference reduced-risk/holding-period rules and qualified-covered-call nuances, not only constructive-sale rules.
- The 2026 qualified-dividend/LTCG bracket thresholds conflict with Side Lesson 04. Side 04 says single 0% up to `$48,350`; this lesson says `$49,450`. Reconcile all 2026 tax tables.
- The VNQ/SCHD tax example appears wrong. If REIT ordinary income is taxed at `32% x 80% + 5% state`, the after-tax cash on `$4,000` is about `$2,776`, not `$2,624`. If state tax also interacts differently, show the exact formula.
- The 0% qualified-dividend statement should be based on total taxable income and filing status, not just being a `12% bracket investor`.
- VYM does not screen the top half of the S&P 500 by yield; it tracks a FTSE high-dividend-yield universe excluding REITs. Fix the index description.
- SPYI likely does not have a full 5-year history if the product launched after 2021. A 5-year chart/table including SPYI needs a proxy/backfill label or should use a shorter common window.
- SPYI tax treatment is oversimplified. Covered-call ETF distributions can include option gains, ordinary dividends, qualified dividends from underlying holdings, capital gains, and return of capital depending on structure and reporting.
- The Aristocrats dividend-growth chart needs methodology/source labels because index membership changes create survivorship/reconstitution effects.
- Foreign withholding section is useful but oversimplified. Canada has special treaty treatment for many US retirement accounts, so Canadian dividend payers are not always worse in an IRA.
- Shell B-share language is stale after Shell's share unification. Update examples.
- Foreign tax credit is not always dead forever if current US tax owed is zero; carryback/carryforward can matter.
- Q11 income-sleeve sizing by age needs suitability/source caveats.
- Q7's `5-10 bp/year` location-loss estimate for SCHD in Traditional IRA needs calculation support.

## Structure And Formatting Issues

- The section numbering is correct.
- The lesson is well sequenced: tax, rates, ETF landscape, theory, foreign withholding.
- Add a compact `dividend ETF comparison` table with: index methodology, launch date, expense ratio, yield, qualified-dividend percentage, distribution tax character, and sector biases.
- The YouTube outro says the next side lesson is foreign-listed ETFs/PFIC rules, but the actual next file is `side11_retirement_accounts.md`.

## YouTube Script Critique

The script is tight and watchable. Stella's opening gives the audience the exact promise.

Needed fixes:

- Use the standard Horace/Stella script style consistently; current labels are all caps rather than the two-host format used elsewhere.
- Correct the `most households making over about 200 grand single` wording. It is too broad and casual for tax brackets.
- Correct the VNQ/REIT 199A tax math.
- Soften `SPYI is taxed at short-term cap gains` into a distribution-character explanation.
- Correct the next-side-lesson preview.

## Chart And Interactive Feedback

`side10_div_lab.html` supports the lesson nicely, especially the yield-on-cost intuition.

Issues:

- The tax model ignores NIIT, filing status, actual taxable-income thresholds, state-specific treatment, and foreign withholding.
- The qualified-dividend tax calculation is inferred from marginal bracket buttons, but actual qualified-dividend rates depend on taxable income after deductions.
- Ordinary dividends are modeled as full bracket plus state, which is fine for generic ordinary dividends but not REIT distributions after 199A, MLP return of capital, or bond-interest state exemptions.
- The chart assumes no reinvestment and flat share price; the caption says this, but the UI should make it visible near the KPI cards.
- Add presets for SCHD, VYM, DGRO, NOBL, SPYI, REIT ordinary income, and foreign dividend with withholding.
- Add a `total-return reminder` panel so yield-on-cost does not become the whole story.

## SOUL Consistency Flags

- Good alignment with the income tranche and behavior-first retirement framing.
- The lesson should make clear that dividend income is an implementation choice, not alpha by itself.
- Strong SOUL-compatible distinction between dividend growth income, premium-write income, REIT income, and stores-of-value assets.
