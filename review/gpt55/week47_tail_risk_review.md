# Review: course/week47_tail_risk.md

## Overall Assessment

Week 47 is conceptually strong and very relevant to SOUL. It teaches the core lesson that normal-distribution risk is inadequate, that convex hedges are expensive but valuable in crashes, and that CTAs can behave differently from static stock/bond diversification.

The lesson needs significant precision around option sizing, hedge cost, tax treatment, and CTA claims. The biggest issue is that several examples imply a 1% annual put budget can make a -30% drawdown roughly flat; the math does not support that under the stated SPY/strike assumptions.

## Content Critique

- The fat-tail opening is memorable and appropriate, but extreme sigma claims should state the volatility assumption and sample window.
- Volmageddon is described as a `-115%` one-day VIX-product implosion. A product price cannot lose more than 100%; clarify whether this refers to an inverse-vol strategy, NAV destruction, or a short-vol position.
- The lesson says tail hedges are the only `negatively-convex` sleeve that becomes more negatively correlated. Put hedges are positively convex and negatively correlated to equities. This is a major terminology correction.
- The mirror comparison to selling premium says the option seller collects small premium for a `known small risk and one big tail`; the seller's tail risk is not known or small.
- The market-tail count section is useful, but the observed 3-sigma/5-sigma frequencies need source and definition.
- `VaR, Sharpe ratios, CAPM-based pricing` should not all be grouped as normal-pricing models in the same way. VaR can be historical or parametric; Sharpe is a summary statistic, not a pricing model.
- The put quote table is useful, but it should distinguish gross intrinsic payout from net profit after premium.
- The Universa section is compelling but should be carefully sourced. The +4,144% hedge-sleeve return and 3.3/96.7 portfolio framing should include caveats about public claims and implementation details.
- The chart/lesson alternates between 25-35% OTM, 15% OTM, and 5-10% OTM strikes. Standardize the architecture or explain the regimes.
- The `$1,000 quarterly tail-hedge budget` on a `$100,000` portfolio is 4% of NAV per year, not 1%. This conflicts with the later cap-carry rule and the interactive default.
- A 1% annual budget buying 15% OTM 90-day SPY puts does not make a -30% drawdown roughly flat for a $100k SPY portfolio. The payoff needs recalculation using contract count and notional coverage.
- CTAs are rightly introduced as long-realized-vol/trend diversifiers, but the lesson should avoid saying they have `no carry cost`. They have fees, whipsaw costs, margin/cash collateral returns, and regime-specific drawdowns.
- CTA comments on March 2020 and 2022-23 need more nuance. Many trend-following programs did well in 2022 and some did well in Q1 2020 before later whipsaw.
- Put upside is described as `unbounded`; index put payoff is large and convex but bounded by the strike times notional.
- The Section 1256 tax claim is wrong for SPY ETF options. SPX/XSP index options generally receive 60/40 treatment; SPY options generally do not.
- Q9 says tail hedges enable leverage and bound drawdown roughly by strike distance plus hedge cost. This is too simplified because option maturity, delta/gamma, basis risk, margin rules, and mark-to-market path can still create liquidation risk.

## Cross-Reference And Consistency Issues

- Week 46 previews Week 47 as tail risk, and this one matches.
- Week 47 previews Week 48 as capital efficiency; verify actual Week 48 before publication.
- Week 47 should align with Week 40 VIX caveats and Week 42 VaR caveats.
- The lesson should harmonize the CTA language with Week 43's active-management discussion of CTA/macro strategies.
- Q2 uses `retail traders`; use `retail investors` or `retail options users`.

## Presentation Improvements

- Add a hedge-sizing table by portfolio size, contracts bought, annual premium, notional covered, and -30% payoff.
- Add a clear SPY vs SPX/XSP implementation box: liquidity, contract size, tax treatment, settlement, assignment, and account suitability.
- Add a `what goes wrong` table: no crash for 10 years, vol spike after purchase, crash after expiry, V-shaped recovery, contract count under-hedging, tax mismatch.
- Add a CTA failure-mode visual: clean trend vs whipsaw.
- Make the Universa example a sourced case study, not an implementation promise.

## YouTube Script Critique

The script is dramatic and watchable. It has a strong hook and the CTA pairing explanation is accessible.

Specific issues:

- Speaker labels use all caps again (`HORACE`, `STELLA`) instead of the course's usual script style.
- The script says a `$1,000` quarterly budget on `$100k` has net drag closer to 1% of NAV. The actual annual premium budget is 4% of NAV unless much of the budget is not spent.
- The claim that a 1% budget and 15% OTM put makes a -30% crash land roughly flat is mathematically inconsistent with the interactive.
- "Deep-OTM puts are 0.2 to 1% per year drag" conflicts with 90-day put examples where quarterly roll costs can annualize much higher depending on strike.
- The retail-vehicle section should mention that CTA ETFs are not pure tail hedges and can lag badly in snapback regimes.
- Add Stella asking: "What if the crash comes one week after my puts expire?" That is the practical retail fear.

## Chart And Visual Feedback

Existing visuals are useful:

- Tail-hedge payoff chart.
- 2008 CTA comparison chart.

Recommended upgrades:

- Add a contract-count-aware payoff chart.
- Add a premium-burn timeline across 10 quiet years.
- Add a CTA trend-versus-whipsaw sequence.
- Add a SPY puts versus VIX calls payoff/monetization window comparison.

## Interactive Demo Feedback

The `week47_tail_lab.html` interactive is a good structure, but several assumptions need correction or disclosure.

Issues and improvements:

- The default 1% annual budget likely buys only about one 15% OTM 90-day SPY put on a $100k portfolio, so a -30% crash remains heavily negative. The script should match this.
- Annual drag is displayed as the budget percent even when the whole-contract floor means actual spend is lower. Use actual spend × rolls / NAV.
- Rolls are fixed at four per year even when DTE changes. If DTE is adjustable, annualized drag should use roughly `365 / DTE` rolls or clearly state quarterly rolling regardless of DTE.
- Add implied volatility/VIX and skew controls. A flat Black-Scholes sigma misses the expensive put skew that dominates deep-OTM hedging.
- Add SPY versus SPX/XSP toggle for contract size, settlement, and tax treatment.
- Add a mark-to-market before expiry mode; crash hedges are often monetized before expiration after implied volatility spikes.
- Add warning when contract count is zero or notional coverage is far below the portfolio beta being hedged.
- CJK labels contain likely mistranslations/errors such as `回撚`; this should be reviewed carefully.

## New Interactive Demo Ideas

- Contract-count hedge planner.
- Quiet-decade premium bleed simulator.
- SPY versus SPX/XSP implementation comparison.
- CTA trend-following path simulator.
- VIX-call monetization-window simulator.

## Make It More Entertaining Without Watering It Down

The best viewer hook is "the insurance receipt." Show the same $100k portfolio over 10 calm years, with premium receipts piling up, then one crash month where the receipt stack finally pays. That makes the emotional challenge clear: the strategy is easy to understand and hard to keep funding.

## Money-Making Usefulness

This lesson can help students avoid catastrophic drawdown and understand why defensive convexity has a cost. But because the math is sensitive to contract count, tax treatment, and strike selection, precision matters more here than in most lessons.

## SOUL Consistency Flags

- Strong alignment with SOUL's tail-hedge/Dragon-portfolio shape.
- Needs correction from `negative convexity` to positive convexity.
- Needs SPY/SPX tax precision before recommending implementation.
- Needs explicit warning that tail hedges are for sizing and solvency, not crash prediction or leverage permission by default.
