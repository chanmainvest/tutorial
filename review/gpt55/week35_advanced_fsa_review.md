# Review: course/week35_advanced_fsa.md

## Overall Assessment

Week 35 is a strong return to financial statement analysis. The "negative-alpha filter" framing is excellent and fits the course's practical philosophy: these tools may not find the next winner, but they can help students avoid obvious disasters.

The lesson needs important corrections around model applicability. The biggest issue is using Altman Z-score on Lehman or implying it knew what the market did not; the original Altman model is not appropriate for banks, insurers, or broker-dealers. The interactive also appears to have slider-range issues that may clamp some large Z-score inputs.

## Content Critique

- The lesson is well motivated and connects cleanly to Weeks 8, 19, 20, and 21.
- The DuPont explanation is clear.
- The Apple buyback/ROE example is strong, but should say buybacks can make ROE less meaningful, not that the equity multiplier is simply "not leverage in the bad sense."
- JPMorgan in a DuPont comparison needs caution. Bank revenue, asset turnover, and leverage are structurally different from non-financial firms.
- CCC formulas should use average balances and, ideally, credit sales for DSO. The simple formulas are fine for teaching but should be labeled approximations.
- The accruals ratio formula appears too simplified and may repeat the Week 20 Sloan/accruals issue. Use the standard balance-sheet accrual formula or clearly label this as a rough proxy.
- The Sloan quintile-spread claim should be softened; the accrual anomaly has decayed and varies by implementation.
- Beneish M-score coverage is good, but claims about Enron, WorldCom, and Valeant should be source-labeled.
- M-score and Altman Z should both carry stronger sector-applicability caveats. Financials, insurers, banks, REITs, and some asset-light firms need different tools.
- The GE timeline should be checked. GE's dividend cuts happened before/around 2017-2018, while the breakup was announced in 2021.
- The Horace-view section is excellent philosophically, but the statement that orthodox CFA framing treats these tools mainly as alpha generation is too broad. CFA material also frames them as risk and quality diagnostics.
- The Q&A tranche mapping may conflict with earlier four-tranche wording. It should be reconciled with SOUL terminology.

## Major Accuracy Issues

- The YouTube script says Ford "did file for bankruptcy" near GM's crisis years. Ford did not file for bankruptcy in 2009; GM and Chrysler did.
- The YouTube script says Lehman 2007 had Z under 1 and "the market did not know; the model did." This is not valid. Altman Z is not designed for broker-dealers/financial institutions, and market credit/equity signals were visible.
- The interactive includes a Lehman 2007 Z-score preset. That preset should either be removed or explicitly labeled as an invalid demonstration of using the wrong model.

## Cross-Reference And Consistency Issues

- Week 34 previewed Week 35 as TIPS, but the actual Week 35 file is advanced FSA.
- Week 35's outro previews Week 36 as industry analysis; this should be checked when Week 36 is reviewed.
- Week 20 accruals formula issues appear to carry forward into Week 35.
- The lesson should keep bank/financial-company caveats consistent across DuPont, M-score, and Z-score.

## Presentation Improvements

- Add a model-applicability table: industrials, retailers, banks, insurers, REITs, software, cyclicals.
- Add "do not use this model here" warnings for Altman Z and Beneish.
- Add a compact two-page checklist template as an image or downloadable markdown table.
- Add a real example of CCC deterioration with source data.
- Add a side-by-side: Apple ROE versus Apple ROIC.

## YouTube Script Critique

The script is clear and practical, but several lines should be corrected.

Specific improvements:

- Remove the Lehman Z-score claim.
- Correct the Ford bankruptcy line.
- Replace technical implementation text about locales/theme switcher with a viewer-facing lab walkthrough.
- Add a Stella challenge: "Can I use Z-score on banks?" The answer should be no, and that would prevent misuse.
- The "negative-alpha filter" outro is strong and should stay.

## Chart And Visual Feedback

Existing visuals are useful:

- DuPont comparison chart.
- Altman Z-score time series.

Recommended upgrades:

- Add model-applicability warning badges on charts.
- Add CCC trend chart for a real company.
- Add Beneish component radar chart.
- Add ROE versus ROIC comparison for Apple.
- Add an FSA dashboard mockup for one company.

## Interactive Demo Feedback

The `week35_fsa_lab.html` interactive is useful but needs fixes.

Issues and improvements:

- Remove or relabel Lehman 2007 because Altman Z is invalid for broker-dealers.
- The Z-score `D: MVE / TL` slider max is 8.0, but presets include AAPL 9.50 and MSFT 12.00. Browser range inputs may clamp those values, causing wrong displayed Z-scores.
- Add a warning when a preset is outside slider bounds.
- Add model-applicability notes next to presets.
- Add five-factor DuPont mode.
- Add Beneish M-score panel or a CCC panel so the lab covers more than Z-score and three-factor DuPont.

## New Interactive Demo Ideas

- FSA two-page health-check builder.
- Beneish M-score component lab.
- CCC trend and peer comparison lab.
- ROE versus ROIC decomposition lab.
- Model applicability selector by industry.

## Make It More Entertaining Without Watering It Down

The most entertaining version is a "forensic dashboard" episode: Stella brings a stock with beautiful ROE, and Horace pulls the company apart with DuPont, CCC, M-score, and Z-score until the hidden risk reveals itself.

## Money-Making Usefulness

This lesson is very useful as a loss-avoidance tool. That is real money: avoiding one Valeant-sized mistake can matter more than finding several small winners.

## SOUL Consistency Flags

- Strong alignment with SOUL's humility about stock-picking alpha.
- Good emphasis on avoiding negative alpha rather than pretending ratio work creates systematic edge.
- Needs tranche terminology cleanup so the four-tranche map is consistent with the rest of the course.
