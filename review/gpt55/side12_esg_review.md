# Review: course/side12_esg.md

## Overall Assessment

This is one of the better side lessons conceptually. It treats ESG as neither magic alpha nor nonsense, but as a values expression with measurable cost, tracking error, and rating uncertainty. That is the right adult framing.

The lesson needs stronger source/date labels, one major compounding-cost correction, and tighter alignment between the script and interactive.

## Content Critique

- The opening `$50T+` ESG/sustainable/responsible-assets claim needs a source and definition. ESG integration, sustainable funds, responsible-investment mandates, and labelled retail funds are not the same category.
- `Every prospectus now includes a sustainability paragraph` is too broad.
- The ratings-disagreement section is strong, but noisy ESG ratings do not prove zero alpha by themselves. A noisy signal can still have weak predictive value; the better claim is that composite ESG scores are unreliable as a clean standalone alpha signal.
- The credit-rating comparison needs source/definition. `0.99` may be too precise depending on whether ratings are mapped ordinally, by notch, or by default-implied spread.
- ETF expense ratios, AUM, index names, and April 2026 figures need source/date labels.
- Product methodology descriptions are too compressed. `ESGV`, `SUSL`, `DSI`, `EFIV`, and `SUSA` do not all use the same exclusion and best-in-class logic.
- ESGV vs VTI performance numbers need exact source/date methodology: total return, dividend reinvestment, start/end dates, and whether returns are NAV or market price.
- The Q&A math is materially wrong. A `40 bp` annual return gap on `$500k` over 30 years is far larger than `$60-90k` under normal equity-return assumptions. Recalculate and state the assumed base return.
- `Most retail ESG ETFs are pure divestment products` should be softened. They are passive-screened products, but their sponsors still exercise proxy voting/stewardship.
- `Vanguard, BlackRock and State Street collectively control about 20% of the S&P 500 vote` needs source/date and should distinguish ownership, voting power, and pass-through/client-directed voting trends.
- The greenwashing discussion is useful, but SEC Names Rule compliance dates/enforcement examples need source/date labels.
- The `fossil-fuel-free` holdings check is good, but not every ESG fund claims to be fossil-fuel-free. Distinguish broad ESG, fossil-fuel-free, climate-transition, and thematic clean-energy products.
- ESG bond discussion should note green bonds, use-of-proceeds risk, issuer-level versus project-level ESG, and greenium/liquidity issues.
- `Gold and Treasuries are not ESG-screenable` is directionally practical, but sovereign ESG and mining-company ESG screens exist. Phrase as `not cleanly screenable in the same way as equity funds`.

## Structure And Formatting Issues

- The section numbering is correct.
- The lesson has a clean arc: ratings, products, performance, greenwashing, engagement, portfolio placement.
- Add a quick `ESG due diligence checklist`: fee, active share/tracking error, exclusions, top holdings, rating provider, proxy-voting policy, tax wrapper, and source-date.
- Add a small `values budget` example: how many basis points or dollars per year the student is consciously willing to pay for exclusions.

## YouTube Script Critique

The script is more watchable than many side lessons because it starts with a controversy and gives the answer early. It is clear, calm, and likely to avoid alienating both ESG believers and skeptics.

Needed fixes:

- Add a stronger cold-open contrast: `Tesla can be a climate hero in one ESG model and a governance failure in another.`
- Correct the `eight years` wording if the window is September 2018 to April 2026; it is closer to 7.5 years.
- The script says the lab default has `neutral expected drag`, but the interactive default is `+0.40%` drag.
- The lab walkthrough says default settings produce about `50 bps tracking error`; verify against the interactive's model output.
- The outro says ESG costs `15-25 bps in fees and another 50 in tracking error`; tracking error is not the same as expected annual return cost. Say tracking-error risk separately from fee/return drag.

## Chart And Interactive Feedback

`side12_esg_lab.html` is a useful teaching sandbox, but it must be more visibly stylized.

Issues:

- The lab only models energy and utility exclusions, while the lesson discusses tobacco, weapons, governance, fossil fuels, clean-energy themes, and broad ESG index methodology.
- The KPI label `Expected return shortfall` appears to show a negative number when ESG underperforms because the code displays `-rs`. Either relabel it as `ESG expected excess return` or display shortfall as a positive drag.
- The caption says tracking error uses sector covariance with market `0.65`, but the code uses a simplified sum of squared active weights times idiosyncratic sector vol and does not use that covariance term.
- Sector weights and expected sector returns are hardcoded as April 2026 assumptions. They need source/date labels and a visible `model, not forecast` warning.
- The lab's expected-return assumptions are deterministic sector-return forecasts. Students may read them as investment forecasts unless the UI warns them.
- Add presets for `ESGV-like`, `SUSL-like`, `fossil-fuel-free`, `clean-energy thematic`, and `market`.
- Add a tracking-error versus expected-drag scatter/heatmap. That would better show the non-linear cost of aggressive exclusion.

## SOUL Consistency Flags

- Strong SOUL alignment: alpha is rare, fees are certain, and portfolio design should separate return maximization from values expression.
- The Horace personal-position answer is clear and consistent with the course's US-market core.
- Keep the orthodox ESG impact case visible before Horace's critique: engagement, cost-of-capital effects, and values expression are real even if they are not reliable alpha.
