# Review: course/side06_inflation.md

## Overall Assessment

This is conceptually strong and very aligned with the course's soul: inflation as a regime risk, stores of value as belief assets, and the danger of assuming the post-2000 stock/bond relationship always holds.

The lesson needs tighter factual precision around CPI/PCE, TIPS mechanics, I-bonds, cash, and several historical claims. The interactive currently contradicts the YouTube demonstration of cash losing purchasing power.

## Content Critique

- The central framing is excellent: inflation is purchasing-power loss that does not show up as an account drawdown.
- The lesson should say the Fed's formal target is PCE inflation; core PCE is a preferred trend signal, not literally the formal target.
- The April 2026 CPI/core PCE/trimmed-mean numbers need source/date labels.
- The CPI/PCE explanation is good but should be slightly softened because basket-update methodology and weights change over time.
- `TIPS are mechanically reliable` is too broad. Individual TIPS held to maturity protect CPI-adjusted principal and real coupon; TIPS funds can lose money when real yields rise, and taxes matter.
- `VTIP has no duration risk` is false. It has low duration risk, not none.
- The asset-ranking section says TIPS are roughly 0% real guaranteed, while Misconception 4 correctly says buying TIPS at a negative real yield locks in a negative real return if held. Reconcile.
- I-bonds are not always `better than TIPS` or usually higher fixed real rate. They have tax deferral, redemption optionality, and purchase limits, but their fixed rate can be zero or below TIPS real yields.
- The 1970s gold explanation is memorable, but `gold got out of jail` should be presented as one major mechanism, not the whole mechanism. Real yields, dollar confidence, and geopolitics also mattered.
- `5% inflation for ten years halves purchasing power` is mathematically wrong. It leaves about 61% purchasing power; halving takes about 14 years at 5%.
- The wage-lag claim should be softened. Wages often lag prices, but `every documented inflation episode` is too universal.
- The Phoenix/San Francisco housing example risks conflating home-price inflation with CPI shelter measurement.
- `The inflation rate that affects your portfolio plan is your local CPI` is a useful idea, but personal inflation is more than geography: housing tenure, medical costs, childcare, tuition, energy, and taxes matter.
- Several performance claims need source/date labels: real S&P 1968-1982 drawdown, 60/40 worst real year, commodities in 2022, gold 2024-2025 catch-up, and average retail capitulation threshold.

## Structure And Formatting Issues

- The decimal section structure is correct.
- The lesson is strong but dense. Consider adding a small `what to actually do` box: short TIPS/I-bonds for inflation-linked bond exposure, small stores-of-value sleeve, avoid excessive long-duration nominal bonds during inflation regimes.
- The `gold is not the answer` section is good storytelling; just avoid replacing one simplistic myth with another simplistic explanation.

## YouTube Script Critique

The grocery-receipt opening is excellent and should stay. It makes inflation visible instantly.

Needed fixes:

- `Core PCE is the one the Fed actually targets` should be changed to `PCE is the target; core PCE is the cleaner trend gauge`.
- The WWI explanation involving the dollar leaving gold needs historical precision.
- The cash interactive demonstration does not match the actual widget behavior.
- `That window is right now` is too market-timing-like and will stale quickly. Replace with an as-of-date real-yield statement.
- The `average retail account drawdown 25%` capitulation claim needs a source or softer wording.

## Chart And Interactive Feedback

`side06_inflation_lab.html` is a useful idea, but its model should be more transparent and internally aligned.

Issues:

- The caption says T-bills track CPI, and the code makes cash earn roughly CPI plus 1.5% real at all inflation settings. That means the script's `100% cash, 4% inflation, thirty years, real wealth shrinks to thirty cents` demonstration is false in the current widget.
- The code models cash nominal return as `0.04 + (inflation - 0.025)`, so cash has a positive real return even at high inflation. If the lesson wants to show bank cash losing value, add a separate `checking account / zero-yield cash` asset.
- TIPS are modeled as a constant positive real return with no mark-to-market duration risk, which contradicts the lesson's 2020-2022 warning about negative real yields and real-yield shocks.
- Asset sensitivities are calibrated assumptions, not historical backtests. Put `model assumption` visibly in the UI, not only the caption.
- The `breakeven inflation` output can be misleading when the model lets nominal returns rise mechanically with CPI. Explain what it means.
- Add presets: 1970s regime, 2022 shock, zero-yield cash, 60/40, TIPS-heavy defensive, stores-of-value sleeve.

## SOUL Consistency Flags

- Strongly aligned with SOUL's stores-of-value-as-belief principle and forty-year regime-change framing.
- Good correction to simplistic `gold always hedges inflation` thinking.
- Needs orthodox-first framing on TIPS before moving into Horace's stores-of-value sleeve. TIPS are contractual CPI instruments; gold/commodities/Bitcoin are belief/regime assets.
