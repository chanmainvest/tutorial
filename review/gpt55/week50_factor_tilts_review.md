# Review: course/week50_factor_tilts.md

## Overall Assessment

Week 50 is a useful implementation-focused factor lesson. It correctly separates academic long-short factor premia from retail ETF products, and its honest expected-uplift estimate is one of the better student-protection moments in the course.

The lesson needs several corrections before publication. The largest issues are a cost-haircut math error, contradictory value-ETF guidance, questionable low-vol drawdown claims, and an interactive that uses synthetic monthly data while the prose presents it as historical backtest evidence.

## Content Critique

- The opening is excellent: Week 23 was the factor theory; Week 50 is the ETF implementation bill.
- McLean-Pontiff and Hou-Xue-Zhang are the right references, but all statistics should be source/date labeled.
- The cost arithmetic in §1 is wrong: 24 bps expense ratio plus 30 bps turnover cost equals 54 bps. On a 7% gross premium, that is about 7.7%, not a 25% haircut. On a 2% premium, it is about 27%.
- The statement that markets have eaten roughly half of every published premium since 2015 is too broad; keep it as a default haircut, not a universal law.
- The ETF AUM values are future/current as of Apr 2026 and need source labels.
- The `VTV vs. VBR` note says owning both is mostly redundant, but the misconceptions and Q&A correctly say they are not interchangeable. These should be reconciled.
- The MTUM discussion references 2009 even though MTUM launched in 2013. Clarify whether that refers to the academic momentum factor, not the ETF.
- The USMV claim that March 2020 peak-to-trough was actually worse than VTI should be verified. It is likely false or at least sensitive to date definitions.
- The implementation-gap table lists VTV universe as Russell 1000 / MSCI USA, but VTV uses a CRSP large-cap value index.
- The expected uplift framing of 30-50 bps per year is good and realistic.
- The five-year stop rule needs nuance. It conflicts with the warning not to sell factors after underperformance unless framed as thesis-risk reduction, not performance chasing.
- The phrase `markets stay irrational longer than you stay solvent` is less appropriate for unlevered ETF tilts; use `longer than your discipline lasts`.
- The barbell section is useful, but should clarify that factor tilts are optional intermediate-risk sleeves, not central to the SOUL barbell.

## Cross-Reference And Consistency Issues

- Week 50 should explicitly link back to Week 23 and update any assumptions from Week 23's academic factor discussion.
- Week 49 previews Week 50 correctly as factor tilts.
- Week 50's outro says `Week 51 was managed futures` and `See you in Week 51's review section`; this is awkward and should be corrected after checking Week 51.
- `VTV and VBR are redundant` conflicts with `VTV and VBR are not interchangeable`.
- The reading says the interactive shows 2014-2024/2026 historical monthly backtest results, but the interactive creates synthetic monthly returns from annual return inputs.

## Presentation Improvements

- Add a clear `academic factor vs retail ETF` bridge diagram.
- Add a source/date footnote for every ETF stat: ER, AUM, launch date, methodology, turnover.
- Add a corrected cost-haircut table with gross premium, live premium, expense ratio, turnover, tax drag, and net expected alpha.
- Add a factor-drought table: value 2007-2019, momentum crashes, low-vol underperformance in bull markets.
- Separate three levels of recommendation: no tilt, simple 80/20 tilt, diversified 70/30 core+tilt.

## YouTube Script Critique

The script is clean, viewer-friendly, and has a strong message: factors are real but smaller than marketing says.

Specific issues:

- It repeats source-heavy statistics without visible source/date cues.
- The AVUV edge over VBR should be framed as short-sample evidence, not proof.
- `The best blend beat VTI on Sharpe by maybe 10 to 15 basis points` does not match the stated grid values of 0.60 versus 0.56, which is a 0.04 Sharpe difference.
- The five-year stop explanation is good, but it should be tied to thesis review rather than mechanical performance chasing.
- The outro needs cleanup: `Week 51 was managed futures` is tense-confused, and `review section` sounds like an internal artifact rather than a lesson.

## Chart And Visual Feedback

Existing visuals are useful:

- Factor ETF cumulative-return chart.
- Core+tilt grid.

Recommended upgrades:

- Add launch-date markers, especially for AVUV.
- Add a drawdown/underperformance-duration chart versus VTI.
- Add factor-correlation heatmap.
- Add implementation-gap waterfall from academic premium to net ETF expectation.
- Add taxable-versus-IRA after-tax return comparison.

## Interactive Demo Feedback

The `week50_tilt_builder.html` interactive is visually useful but analytically risky.

Issues and improvements:

- It uses hardcoded annual returns expanded into synthetic monthly returns. Volatility, drawdown, Sharpe, and path shape are therefore synthetic, not historical.
- The reading and script present the grid/lab as a 2014-2024/April 2026 monthly historical backtest, which overstates what the interactive actually does.
- AVUV pre-Sep-2019 is filled with VBR, which should be clearly surfaced in the UI and the lesson text.
- The interactive rebalances monthly, while the lesson recommends annual rebalance.
- Sharpe uses a fixed 4% risk-free rate for the entire 2014-2024 sample. Use historical T-bill returns or label it as a simplified excess-return proxy.
- If weights do not sum to 100%, the backtest still runs using those weights. Either normalize automatically, add an explicit cash/leverage sleeve, or block the stats until weights equal 100%.
- CJK strings include `回撚` for max drawdown in HK/CN; this needs correction.
- Replace synthetic monthly paths with actual monthly total-return data if the chart is meant to support investment claims.

## New Interactive Demo Ideas

- Factor implementation gap waterfall.
- Factor drought simulator showing 10-year tracking-error pain.
- Tax-location optimizer for factor sleeves.
- Factor correlation and diversification explorer.
- Expected-alpha haircut calculator using academic premium, decay, implementation exposure, fees, turnover, and tax drag.

## Make It More Entertaining Without Watering It Down

The best hook is Stella buying the ETF with the same name as the academic factor, then discovering the `nutrition label` is different: long-only, cap-weighted, slower rebalance, fees, taxes, and tracking error.

## Money-Making Usefulness

The lesson is genuinely useful because it prevents overpaying for factor marketing. It also gives a realistic target: 30-50 bps of expected uplift, not fantasy alpha. The charts and interactive must be tightened so students do not mistake synthetic backtests for hard evidence.

## SOUL Consistency Flags

- Good alignment with SOUL's view that alpha is rare and must survive implementation.
- Factor sleeves should be framed as optional Level-4 expression tools, not replacements for the barbell's asymmetric core.
- US-only implementation is aligned with SOUL, but any international factor section should be clearly orthodox context rather than a recommended allocation.
