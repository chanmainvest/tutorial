# Review: course/week21_equity_valuation.md

## Overall Assessment

Week 21 has the right philosophical stance: valuation is a structured argument, not a precise measurement. The DCF/multiples/CAPE/Fed-model combination is a good toolkit, and the reverse-DCF framing is especially useful for retail investors who otherwise get trapped in false precision.

The lesson inherits Week 20's FCF-definition issue, has likely Markdown rendering problems in the sensitivity table, and contains a few cross-reference mismatches. It should also be careful with date-specific CAPE/Fed-model claims and with using banks inside a standard DCF lab.

## Content Critique

- The opening is excellent. "Valuation is not a measurement; it is a structured argument" should stay.
- Absolute versus relative valuation is explained clearly.
- The warning that most valuation alpha is regime/multiple risk is strongly aligned with the course philosophy.
- The DCF mechanics are clear, but "free cash flow" is defined as `OCF - Capex`, inheriting the Week 20 issue. If discounting firm-level cash flows using WACC, use true FCFF or explain the simplification.
- The terminal-value warning is important and should be emphasized visually.
- The sensitivity table appears likely to render incorrectly because dollar values such as `$238` are not escaped or closed as math. Use `\$238`, plain numbers, or code formatting.
- The claim that price targets cluster because analysts gravitate to similar WACC/growth assumptions is plausible and useful.
- The multiples field guide is good, especially the EV/EBITDA capex warning.
- CAPE is presented correctly as a long-horizon temperature gauge rather than a short-term timing signal.
- Date-specific claims about April 2026 CAPE, Fed-model readings, and implied returns need source/date labels.
- The Fed model section is thoughtful because it explicitly calls out the real/nominal mismatch.
- The DCF lab includes JPM, but the Q&A correctly says banks do not fit standard DCF well. Either remove JPM from the standard DCF lab or switch it to residual income/P/B-vs-ROE mode.
- The 2014 CAPE example says the subsequent decade gave roughly 9% nominal CAGR. Verify this number with a total-return series; it may understate the actual 2014-2024 return depending on date window.

## Cross-Reference And Consistency Issues

- Q6 references the four-tranche framework from Week 14, but Week 15 is the multi-asset/four-tranche lesson.
- The YouTube outro says next week is macroeconomic indicators, but Week 22 is currency and international diversification.
- The lesson's DCF section relies on Week 20 cash-flow definitions, which need correction before Week 21 is finalized.
- If Week 20 links to a nonexistent `week21_valuation_dcf.md`, update those references to this file.

## Presentation Improvements

- Add a DCF definition box: FCFF cash flows use WACC; FCFE cash flows use cost of equity.
- Add a terminal-value share-of-DCF visual.
- Add a sensitivity heatmap instead of a plain table.
- Add a reverse-DCF checklist: current price, starting FCF, WACC, terminal growth, implied explicit growth, plausibility.
- Add a bank-valuation sidebar: residual income, P/B, ROE/ROTCE.
- Add source notes for CAPE and Fed-model data.

## YouTube Script Critique

The script is strong and appropriately humble. The slider demonstration should be compelling because it makes assumption sensitivity visceral.

Specific improvements:

- Correct the next-week preview.
- Add one line explaining why JPM is different if it remains in the lab.
- Replace "DCF you can drive" with a clear warning that the sliders teach sensitivity, not a price target.
- Add a Stella pushback: "If everything changes with WACC, why model at all?" Horace can answer: to reveal the bet.
- Make the April 2026 CAPE/Fed-model section explicitly date-stamped.

## Chart And Visual Feedback

Existing visuals are useful:

- CAPE history chart.
- Fed-model spread chart.

Recommended upgrades:

- Add DCF sensitivity heatmap.
- Add terminal-value contribution chart.
- Add multiple-selection guide by industry.
- Add reverse-DCF implied-growth chart for preset stocks.
- Add CAPE versus 10-year forward real return scatter.

## Interactive Demo Feedback

The referenced `course/interactive/week21_dcf_lab.html` is a strong idea. Sliders for WACC, growth, terminal growth, and reverse DCF can teach humility quickly.

Suggested improvements:

- Add FCFF versus FCFE mode.
- Add bank/residual-income mode or remove bank presets from standard DCF.
- Add guardrails when terminal growth approaches WACC.
- Add sensitivity heatmap and not just a single output.
- Add uncertainty bands instead of one intrinsic-value number.
- Add data/source/date notes for preset assumptions.

## New Interactive Demo Ideas

- Reverse DCF sanity-check tool for any ticker.
- CAPE expected-return explorer.
- Fed-model cross-asset thermometer.
- Multiples peer-comparison builder.
- Terminal-value dependency visualizer.

## Make It More Entertaining Without Watering It Down

The entertainment is the reveal that tiny assumption changes move hundreds of billions of dollars. Let Stella turn one slider and accidentally create or destroy a trillion dollars of market cap; that is both funny and educational.

## Money-Making Usefulness

This lesson helps students make money by preventing overpayment and by forcing explicit assumptions. The reverse DCF is the most actionable tool: it asks whether the current price requires a miracle.

## SOUL Consistency Flags

- Strong alignment with SOUL principle #1: alpha is rare, and valuation should not be confused with magic.
- Good connection to SOUL's regime-awareness through CAPE and rate sensitivity.
- Needs clean cash-flow/discount-rate matching to avoid technical contradiction with Week 20.
