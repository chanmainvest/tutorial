# Review: course/week22_currency_international.md

## Overall Assessment

Week 22 is energetic, opinionated, and very aligned with the course's US-listed-investable-universe philosophy. The DXY explanation is valuable, and the lesson does a good job showing that international equity exposure is really equity plus FX.

The biggest issue is the FX hedging/carry explanation. The lesson is internally inconsistent about whether hedging developed-market currency exposure costs or earns the interest-rate differential when US rates are higher than foreign rates. This must be corrected before publication because it changes the practical conclusion. The lesson also needs a slightly stronger orthodox-first setup before rejecting the global-market-cap textbook allocation.

## Content Critique

- The DXY section is excellent. It teaches the composition and limitations clearly.
- The "international ETF is two bets" framing is exactly the right mental model.
- The lesson is appropriately skeptical of broad EXUS allocation for a US-based retail investor.
- The FX hedge-cost section has a major sign/definition problem. The formula, quote convention, and written explanation need to be reconciled. If `S` is quoted as USD per foreign currency, covered interest parity is typically `F = S * (1 + r_US) / (1 + r_foreign)`. The current text uses the inverse and then mixes cost/carry language.
- The intro says hedging EUR exposure costs roughly 2% per year when Fed funds exceed ECB rates; §2.3 says the hedger is paid the differential. Those cannot both be true under the same quote convention.
- Operational drag and bid-ask spreads should not be described as offsetting most of a 2% developed-market rate differential unless the lesson has data proving it. ETF expense ratios/tracking error are much smaller than that in normal conditions.
- The Japan example should verify the claim that yen weakness worsened the USD investor's 1989-2024 experience by roughly 30%. The USD/JPY endpoint depends heavily on the exact start/end dates and may not support that wording.
- The lesson should teach the orthodox global market-cap argument first: global market portfolio, lower single-country risk, valuation dispersion, sector diversification. Then Horace can reject it based on governance, currency, liabilities, and US-listed quality.
- "Currency leg routinely overwhelms the equity leg over any horizon you actually care about" is memorable but a little too absolute. It should say it can dominate over multi-year horizons.
- The S&P 500 global-revenue argument is good but should distinguish revenue exposure from listing/legal/governance exposure.

## Cross-Reference And Consistency Issues

- The YouTube outro previews Week 23 as bonds/duration/convexity/yield curve, but the visible course sequence has Week 23 as factor investing.
- The lesson is strongly SOUL-aligned on US-listed equities, but it should explicitly acknowledge the orthodox global diversification case before giving Horace's course-specific conclusion.
- Script host labels use all-caps `STELLA`/`HORACE`, while most English scripts use `Stella`/`Horace`. Standardize for consistency.

## Presentation Improvements

- Add a small quote-convention box: `S` as USD per EUR versus EUR per USD changes the formula orientation.
- Add a table showing hedge carry by currency using the same convention throughout.
- Add a DXY versus broad trade-weighted dollar comparison chart.
- Add a clear decision tree: unhedged, hedged, or no international exposure.
- Add an orthodox-vs-Horace allocation comparison: global cap-weight, Bogleheads-style, and Chanma/SOUL version.
- Add source notes for SPY/EFA/HEFA return claims.

## YouTube Script Critique

The script has a strong hook and a clear contrarian stance. It should perform well because it challenges a familiar textbook belief.

Specific improvements:

- Correct the hedge-cost/carry section before recording.
- Make Stella challenge Horace: "Isn't the global market portfolio the neutral answer?" Then Horace can explain why the course deviates.
- Replace the Week 23 preview.
- Avoid saying the textbook is simply outdated; explain which assumptions changed.
- Add one simple numerical hedge example with spot, forward, and resulting USD return.

## Chart And Visual Feedback

Existing charts are useful:

- DXY long-history chart.
- SPY versus EFA versus HEFA cumulative wealth chart.

Recommended upgrades:

- Add DXY versus Fed broad trade-weighted dollar.
- Add hedged-versus-unhedged return decomposition.
- Add FX carry/cost table by currency.
- Add Japan local-currency versus USD investor experience chart.
- Add global revenue exposure chart for S&P 500.

## Interactive Demo Feedback

The referenced `course/interactive/week22_fx_lab.html` is the right concept. Sliders for local equity return and USD strength should make the FX overlay obvious.

Suggested improvements:

- Add interest-rate differential and hedge-cost/carry slider.
- Show exact formula and quote convention used.
- Add historical presets with dates and data sources.
- Add a toggle for USD-based versus non-USD-based investor.
- Add a broad trade-weighted-dollar option, not only DXY.

## New Interactive Demo Ideas

- Global allocation allocator: US, hedged developed, unhedged developed, EM.
- DXY basket explainer with draggable weights.
- Hedging carry calculator using two interest rates and spot/forward quotes.
- International return decomposer: local equity return, FX return, hedge carry, fees.
- Home-liability currency stress test.

## Make It More Entertaining Without Watering It Down

The lesson already has a strong contrarian energy. The best entertainment would be a "textbook says / brokerage statement says" split-screen where the same EFA investment looks diversified in theory and disappointing in USD reality.

## Money-Making Usefulness

Very useful if corrected. The lesson can prevent students from buying international ETFs without realizing they bought an FX position. The practical allocation guidance is valuable, but the hedge mechanics must be technically clean.

## SOUL Consistency Flags

- Strongly aligned with SOUL's US-listed-equities-only stance and skepticism toward HK/CN/EM governance.
- Needs orthodox-first presentation to satisfy the SOUL application workflow.
- Emerging-market "sized for total loss" language fits the risk philosophy but should be framed as tranche-4 speculation, not a default investment pillar.
