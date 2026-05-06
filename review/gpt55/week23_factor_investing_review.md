# Review: course/week23_factor_investing.md

## Overall Assessment

Week 23 is one of the more advanced and useful lessons so far. It teaches factors as long-short portfolios, explains factor decay, covers the 2007 quant quake, and gives retail investors a practical ETF implementation path. The tone is appropriately skeptical: factors are real, but crowded and smaller than advertised.

The lesson should soften a few overclaims, tighten academic definitions, verify ETF expense ratios/data claims, and fix the next-week preview. It also needs to align the "passive core" language with the course's SOUL/tranche framing.

## Content Critique

- The CAPM-to-Fama-French opening is strong and accessible.
- The distinction between academic long-short factors and retail long-only factor ETFs is essential and well placed.
- The factor-premium and factor-decay sections are valuable.
- The phrase "explains roughly 90% of the cross-section of US equity returns" should be tightened. Factor models often explain a high share of time-series variance for diversified portfolios, but the wording "cross-section" is too broad.
- The example definition of HML as top-decile minus bottom-decile book-to-market is a useful teaching simplification, but the actual Fama-French HML construction uses size/book-to-market portfolio sorts. Add a note distinguishing simplified intuition from exact academic construction.
- The claim that factors "scale infinitely" is false as written. Factors are scalable compared with idiosyncratic active management, but small-cap, value, momentum, and short legs have capacity/crowding limits.
- The claim that ETF fee compression makes the net premium roughly the same as old leveraged hedge-fund factor premia is interesting but unsupported. It should be framed as a rough intuition, not a factual equivalence.
- The script says market is the biggest premium at 6.6% and then immediately says momentum is 7.5%, bigger than market. Fix the contradiction.
- ETF expense ratios should be checked. VLUE may not be 0.08% depending on current fee data.
- "Morningstar Direct ... for free" is likely wrong; Morningstar Direct is generally paid software. Portfolio Visualizer may offer limited free factor tools, but verify.
- The central-bank-liquidity explanation says "nothing trades on fundamentals" too absolutely. Make it a regime pressure, not a total claim.

## Cross-Reference And Consistency Issues

- The YouTube outro previews style boxes/Morningstar grid next week, but the course sequence shows Week 24 as multi-strategy.
- Week 23 says factors belong in the passive core. The course/SOUL framing should call this tranche one or tranche two, because the broader SOUL architecture replaces a naive passive core with a barbell/tranche framework.
- The script references `course/interactive/week23_factor_blender.html`; most lesson references use `interactive/...`. Standardize if needed.

## Presentation Improvements

- Add a table: academic factor construction versus retail ETF proxy.
- Add a factor crash table: HML 2007-2020, UMD 2009, low-vol melt-up underperformance.
- Add a capacity/crowding sidebar.
- Add a tax/turnover warning, especially for momentum ETFs.
- Add a short note on factor timing using valuation spreads, and warn that timing factors can become another overfit strategy.
- Add a glossary box for HML, SMB, RMW, CMA, UMD.

## YouTube Script Critique

The script should be attractive to viewers because it reveals that many expensive active strategies are just factor tilts in costume. The factor-decay hook is strong.

Specific improvements:

- Fix the market-versus-momentum premium contradiction.
- Add a simple visual analogy: "factor ETF is not the pure academic factor; it is market beta with a tilt."
- Add one real retail mistake: replacing the whole core with MTUM after a good run.
- Add a Stella challenge: "If everyone knows this, why should it still work?"
- Correct the next-week preview.

## Chart And Visual Feedback

Existing visuals are useful:

- Factor premia 1963-2024.
- Rolling HML/UMD factor decay chart.

Recommended upgrades:

- Add long-short construction diagram.
- Add factor ETF proxy map.
- Add HML drawdown and UMD drawdown charts.
- Add factor-correlation matrix.
- Add after-fee/after-tax comparison for retail ETFs.

## Interactive Demo Feedback

The referenced `course/interactive/week23_factor_blender.html` is a strong concept. A factor blender with historical Fama-French data can teach diversification, drawdown, and factor regret better than prose.

Suggested improvements:

- Include a toggle for academic long-short factors versus long-only ETF proxies.
- Add transaction-cost and tax-drag assumptions.
- Add annual versus monthly rebalance options.
- Add maximum factor weight constraints.
- Add a warning when a portfolio is concentrated in a single crash-prone factor.
- Show rolling 10-year underperformance versus the market, not just cumulative wealth.

## New Interactive Demo Ideas

- Factor-regression explainer for a sample active fund.
- Factor crowding simulation with leverage and redemptions.
- Factor regret simulator showing how long a factor can underperform.
- ETF factor-exposure map: VTI, QUAL, MTUM, USMV, AVUV, VLUE.
- Taxable-account rebalancing drag calculator.

## Make It More Entertaining Without Watering It Down

The entertaining version is a "wealth-manager X-ray" segment: take a fancy fund pitch, regress it, and reveal that the expensive alpha is mostly value, quality, and momentum exposure in a nicer suit.

## Money-Making Usefulness

Very useful if the implementation is restrained. The best money-making advice here is not "buy factors aggressively" but "tilt modestly, understand the drawdown, and stop paying active fees for factor exposure."

## SOUL Consistency Flags

- Aligns with SOUL's structural-alpha framework and skepticism toward easy, crowded alpha.
- Needs to avoid implying factors are a magic passive core. In SOUL terms, factors are modest tranche-one/two tilts inside a broader barbell/tranche architecture.
- Good fit with the principle that discomfort and structural mispricing, not consensus labels, are where persistent edge remains.
