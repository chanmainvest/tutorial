# Review: course/week34_rate_sensitivity.md

## Overall Assessment

Week 34 has a powerful course-level idea: many assets that look different can share the same rate driver. The 2022 case study is a strong way to make conditional diversification memorable.

The lesson needs technical cleanup because it mixes strict bond duration with looser empirical equity/rate sensitivity. That makes some tables and rules look more precise than they are. The interactive also appears not to reproduce the 2022 case cleanly because rate and inflation shocks may be double counted for nominal bonds.

## Content Critique

- The core message is excellent: diversify by drivers, not labels.
- The 2022 case study is useful and audience-relevant.
- "Every asset on Earth is priced by discounting cash flows" is too broad unless immediately caveated for commodities, currencies, and stores of value.
- The lesson should distinguish Fed funds shocks, 10-year yield shocks, real-rate shocks, and long-end parallel shocks. It currently uses these somewhat interchangeably.
- The rate-shock table mixes approximate duration and empirical price impact. For example, S&P 500 is listed with duration ~18 but a +100 bps impact of -7%, not -18%. That is not the duration formula; it is an empirical rate beta or scenario estimate.
- The same issue appears for value, growth, REITs, and HYG. Add two columns: cash-flow duration and observed/scenario rate beta.
- The claim that ARKK and TLT moved together mainly because of duration is directionally useful but incomplete. ARKK also reflected earnings revision, liquidity, risk appetite, and unprofitable-growth multiple compression.
- The gold section says 2022 real rates rose only modestly. That should be checked; 10-year real yields moved from deeply negative to meaningfully positive. Gold's resilience needs a richer explanation.
- The dollar section is SOUL-consistent but should be labeled as Horace's US-only view rather than presented as universal advice.
- §2.8 says different drivers include "short volatility." That is likely wrong in this context. A tail-risk diversifier should usually be long volatility, not short volatility.
- Q1's P/E x 0.7 equity-duration shortcut conflicts with the table's equity price impacts. It also risks teaching false precision.
- Q3 says TIPS have lower duration because part of the cash flow comes from CPI accruals. TIPS duration should be framed as real-rate duration; TIPS can still lose when real rates rise.
- Q5 says options are the most tax-efficient way to take leverage in a US taxable account. That needs nuance because ETF options can produce short-term tax treatment; index options and futures have different rules.

## Cross-Reference And Consistency Issues

- Week 33's outro previewed Week 34 as liquidity risk, but Week 34 is rate sensitivity.
- Week 34's outro previews Week 35 as TIPS; this should be checked when Week 35 is reviewed.
- Week 34's long-bond treatment is more nuanced than Week 32's; Week 32 should probably inherit this nuance.
- The lesson should stay consistent with SOUL by saying long volatility/tail hedges are the crisis diversifier, not short volatility.

## Presentation Improvements

- Split strict duration from empirical sensitivity.
- Add a glossary box: rate duration, spread duration, equity duration, real-rate beta, USD beta.
- Add a driver map showing which assets respond to nominal rates, real rates, inflation expectations, credit spreads, and FX.
- Add a 2022 attribution table: nominal rates, real rates, inflation, dollar, credit spreads.
- Add a warning: +100 bps Fed move does not equal +100 bps 10-year move.

## YouTube Script Critique

The script is engaging and accessible. The phrase "one trade in three costumes" is memorable and useful.

Specific improvements:

- Replace "+100bps Fed shock" with the exact curve point being shocked.
- Add a Stella challenge: "But if S&P duration is 18, why does the table say -7%?" That forces the correct distinction between theoretical cash-flow duration and empirical rate beta.
- Avoid making ARKK/TLT equivalence too absolute.
- Label the US-only/dollar argument as Horace's view.
- Correct the Week 33/34 sequence mismatch in the prior lesson, not here.

## Chart And Visual Feedback

Existing visuals are useful:

- Rate-shock grid.
- 2022 cross-asset return bar chart.

Recommended upgrades:

- Add a driver-exposure heatmap.
- Add a two-axis chart: duration estimate versus realized 2022 return.
- Add real-rate versus nominal-rate gold chart.
- Add Fed funds versus 10-year yield shock comparison.
- Add a 60/40 return decomposition for 2022.

## Interactive Demo Feedback

The `week34_shock_lab.html` interactive has a good concept and a helpful disclaimer, but the model needs refinement.

Issues and improvements:

- The 2022 preset may not match the lesson's 2022 case. With rate and inflation shocks both applied to nominal bonds, bond losses can be overstated.
- Clarify whether the rate shock is nominal, real, Fed funds, or 10-year.
- Avoid applying a separate inflation penalty to nominal bonds if the rate shock already embeds nominal yield movement.
- Add HYG, broad S&P 500, and T-bills if the lesson table includes them.
- Add a toggle for nominal-rate shock versus real-rate shock.
- Display the model coefficients so users can see the assumptions.
- Rename 60/40 if it uses value/growth average rather than a real S&P 500 coefficient.

## New Interactive Demo Ideas

- Driver-exposure matrix builder.
- Nominal versus real-rate shock lab.
- 60/40 decomposition replay for 2008, 2020, and 2022.
- Equity duration estimator with growth and ERP inputs.
- Gold real-rate sensitivity lab.

## Make It More Entertaining Without Watering It Down

The best hook is to show a portfolio labeled "diversified" and then recolor every holding by its hidden rate exposure. That reveal would be visual, memorable, and honest.

## Money-Making Usefulness

This lesson can help students avoid hidden concentration in rate-sensitive assets. Its practical value will rise sharply if the model separates precise duration math from rough cross-asset sensitivity.

## SOUL Consistency Flags

- Strongly aligned with SOUL's critique of the 40-year passive/60-40 regime and the need for driver-aware allocation.
- Needs to correct "short volatility" if the intended diversifier is a long-volatility or tail-hedge sleeve.
- US-only/dollar framing should be clearly presented as Horace's view.
