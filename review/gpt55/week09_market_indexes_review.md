# Review: course/week09_market_indexes.md

## Overall Assessment

Week 9 is timely and important. It connects directly to what students actually own after Week 2: index ETFs. The "index as recipe, not market" framing is excellent, and the lesson does a good job explaining weighting schemes, Mag-7 concentration, float adjustment, index reconstitution, and passive-flow plumbing.

The lesson should tighten survivorship-bias language and fix several cross-reference errors. It also has a chance to connect more explicitly to SOUL principle #2: passive indexing is a flow machine, and once price-insensitive flow dominates marginal trading, price discovery can weaken.

## Content Critique

- The opening is strong: indexes are recipes. Keep this as the core metaphor.
- The three weighting schemes are explained clearly. Price-weighting as a Dow artifact is especially well handled.
- The cap-weighting section should say concentration is both feature and risk: it lets winners run but makes the index momentum-sensitive.
- The Mag-7 concentration section is highly relevant. Add a time-series chart of top-10 concentration, not only a current snapshot.
- "Equal-weight is now the obvious diversifier" is directionally useful, but specify whether this means replacing VOO with RSP or adding RSP alongside VOO. RSP alone cuts top-10 concentration much more than VOO+RSP blended.
- The Russell reconstitution section is useful and entertaining. Add a warning that retail investors should understand the plumbing but generally should not try to trade it.
- The survivorship-bias section needs precision. The historical S&P 500 index return is the return of the index methodology, including deletions and replacements. That is not the same as a backtest of today's constituents, which is the more severe survivorship error. Avoid implying that the index return is invalid merely because the index replaced dead names; replacement is part of the product an index investor actually owns.
- The claim that Damodaran's dataset corrects broad-market survivorship should be sourced or softened.
- The MSCI ACWI caveat is strongly SOUL-aligned, but it should separate orthodox global diversification from Horace's investability/political-risk objection.
- The futures section is useful but advanced. Add a warning that futures are leverage instruments and can liquidate an undercapitalized retail account quickly.

## Cross-Reference And Consistency Issues

- The reading section says the default move is to own the index, hold the four tranches "lesson 13," and spend decision budget on tax structure "lesson 15." In the course map, Week 13 is long/short and Week 15 is multi-asset, not those topics.
- The YouTube outro says next week is bonds, but bonds were Week 5 and Week 10 is economic cycles.
- The "four tranches" language may be confusing here because SOUL principle #13 is a precious-metals/sector-cycle tranche model, not a generic index allocation step.

## Presentation Improvements

- Add a simple recipe card for each index: universe, selection rule, weighting rule, rebalance rule, hidden tilt.
- Add a Mag-7 concentration timeline from 2014 to 2026.
- Add a "same stocks, different index" table showing cap-weight, equal-weight, and price-weight weights for a few familiar companies.
- Add a "what can go wrong" box for each index: S&P concentration, Russell low quality, Nasdaq listing bias, Dow price-weight distortion, ACWI political/FX/tax complexity.
- Add an index-plumbing flow diagram: committee/rules -> index changes -> passive fund flows -> price impact -> arbitrage/front-running.

## YouTube Script Critique

The script is engaging and clearer than many index explainers. Stella's confession that she owned VOO before knowing what was inside it is relatable and should stay.

Specific improvements:

- Use the recipe metaphor visually: same ingredients, three dishes.
- Make the Mag-7 reveal a retention beat: show "500 stocks" first, then reveal one-third in top ten.
- Give Stella a stronger challenge: "If equal-weight beat long term, why not use only RSP?" That lets Horace discuss turnover, taxes, and regime underperformance.
- Add a SOUL-flavored line: passive is not neutral; it is a mechanical buyer and seller based on flows.
- Fix the next-week outro.
- Add one short viewer action: open your ETF holdings page and find the top-10 concentration.

## Chart And Visual Feedback

Existing visuals are relevant:

- Cap versus equal-weight chart is important.
- Top-10 concentration chart is the visual center of the lesson.

Recommended upgrades:

- Top-10 S&P 500 concentration over time with Nifty Fifty, dot-com, and Mag-7 annotations.
- S&P 500 inclusion/deletion event study chart.
- Russell reconstitution calendar with flow timeline.
- Survivorship-bias visual contrasting actual historical index membership versus today's-constituents backtest.
- ACWI country/region weight map with "orthodox" versus "Horace investability" overlay.

## Interactive Demo Feedback

The existing `course/interactive/week09_index_builder.html` works well for the core lesson. It lets students toggle cap-weighted, equal-weighted, and price-weighted recipes over 30 representative stocks, then shows composition, contribution to return, 12-month index return, and top-5 concentration. It is a good teaching sandbox.

Suggested improvements:

- Add sector labels and sector exposure by weighting scheme.
- Add a top-10 concentration metric in addition to top-5, to match the lesson's Mag-7/top-10 framing.
- Add a toggle for "current year" versus "bad mega-cap year" so students see equal-weight diversification in a drawdown.
- Add a reconstitution event mode: add/remove a stock and show forced-flow impact.
- Add a note that data is representative/pedagogical, not live market data.
- Add mobile simplification for the pie chart; many labels may become crowded.

## New Interactive Demo Ideas

- ETF concentration checker: enter VOO, VTI, QQQ, RSP, ACWI, VXUS; see top holdings, overlap, sector, country, and effective top-10 concentration.
- Passive flow simulator: payroll contributions and retiree withdrawals drive index buying/selling; user changes demographics and sees flow pressure.
- Index addition/deletion simulator: passive assets benchmarked to an index, stock float, and required buy/sell volume -> estimated price pressure.
- Survivorship backtest trap: compare today's S&P constituents backtest against actual historical membership.
- Global investability map: orthodox ACWI weights versus Horace-adjusted investable universe.

## Make It More Entertaining Without Watering It Down

The strongest entertainment device is the reveal that "passive" is not neutral. It is a machine with rules. Show the machine. Make the viewer feel the surprise that the index they thought was a market is actually a recipe maintained by committees, calendars, float rules, and forced flows.

## Money-Making Usefulness

This lesson helps students avoid hidden concentration, bad benchmarks, false diversification, and naive global allocation. The most actionable addition is a required "look-through" exercise: list your ETF's top 10 holdings, top sector, country exposure, and weighting rule.

## SOUL Consistency Flags

- Strong alignment with SOUL principle #2 on passive flows, but the lesson should more explicitly connect index plumbing to price-discovery risk.
- Strong alignment with SOUL principle #16 in the ACWI caveat, but teach orthodox global diversification first.
- Fix the lesson 13/15 and Week 10 cross-reference errors.
- Clarify "four tranches" usage so it does not confuse SOUL's sector-cycle tranche model with general index allocation.
