# Review: course/week07_rebalancing.md

## Overall Assessment

Week 7 is a strong behavioral and operational lesson. It correctly frames rebalancing as risk control first and return enhancement second. The opening is memorable: rebalancing is boring, mechanical, and exactly why it works. The lesson also does a good job making the tax-aware implementation hierarchy practical.

The main problems are recurring cross-reference drift, some overprecision around the rebalancing premium formula, and the need for clearer limits on when rebalancing works. The lesson is best when it says: pick an allocation, pick a rule, and let the rule protect you from yourself.

## Content Critique

- The drift section is excellent. Showing a 60/40 becoming 78/22 is a concrete risk lesson.
- The calendar versus threshold section is practical and appropriately says the differences are small. This prevents overengineering.
- The rebalancing premium discussion is useful, but the formula should be clearly labeled as an approximation under simplifying assumptions. Beginners should not think the premium is mechanically guaranteed.
- The word "lagniappe" is charming but may be too obscure for a beginner lesson; define it or replace with "bonus."
- The tax hierarchy is one of the most valuable parts of the lesson. It should include explicit jurisdiction labeling because capital-gains treatment varies outside the US.
- The March 2009 example is emotionally strong, but clarify whether the rule is calendar or threshold. A January-only rule may not buy exactly at March 2009; a threshold rule could.
- The December 2021 example is good, but again should specify whether it is annual January rebalancing, year-end rebalancing, or threshold rebalancing.
- The 2022 discussion is honest: rebalancing cannot create a premium when both assets fall together. Good continuation from Week 4.
- The broader-asset-menu conclusion is correct, but be careful saying a barbell has more cross-asset variance to harvest. Long options, tail hedges, and asymmetric sleeves do not rebalance like simple mean-reverting asset classes.
- The lesson should distinguish rebalancing a passive allocation from trimming a high-conviction active position. It does this in Misconception 5 and Q7; those ideas deserve earlier placement.

## Cross-Reference And Consistency Issues

- Q11 says "diversified mixes (Week 5)," but Week 5 is bonds.
- Q11 and the YouTube script again refer to the barbell as Week 14 material, while Week 14 is pair trading in the course map.
- The YouTube end screen says "Next: Week 8 — Asset Location and Tax Optimisation," but Week 8 is Reading Financial Statements - Basics.
- The script says "We cover that in Week 14" for the broader barbell response; this should be corrected or the pair-trading lesson should explicitly include that connection.

## Presentation Improvements

- Add a "Rebalancing is for risk, not alpha" callout near the start.
- Add a worked household example: taxable brokerage + IRA + 401(k), and show where trades should happen.
- Add a "rebalance with contributions" flowchart: new cash -> underweight sleeve -> no sale -> no tax.
- Add a visual distinction between passive sleeves and active conviction sleeves.
- Add a mini checklist: target allocation, band, date, tax location, contribution rule, exception policy.
- Use a one-page summary: annual is fine, 5% band is fine, monthly is usually too much, never is hidden risk drift.

## YouTube Script Critique

The script is clear and has a strong promise: boring discipline beats emotional trading. It should be more visual and more story-driven, because rebalancing can otherwise feel like a spreadsheet chore.

Specific improvements:

- Cold open with Stella's portfolio drifting from 60/40 to 78/22 and then facing COVID. Show the dollar drawdown difference.
- Make the 2009 example more cinematic: headlines, portfolio down, rule says buy, human wants to sell.
- Add a tax segment visual with three buckets: taxable, IRA/401(k), new contributions.
- Give Stella the obvious objection: "Why sell my winner if the thesis is still right?" Use that to introduce passive sleeve versus conviction sleeve.
- The 2022 segment should say: the rule did not fail; the asset menu was too narrow.
- Fix the next-week end screen and Week 14 reference.

## Chart And Visual Feedback

Existing visuals are useful:

- Drift chart is the right anchor visual.
- Method comparison chart supports the conclusion that rule choice matters less than rule-following.

Recommended upgrades:

- Tax-aware rebalancing flowchart.
- Rebalance event markers on a historical wealth path, especially 2008-2009 and 2020.
- Contribution-only rebalancing example over time.
- Passive sleeve versus active sleeve diagram.
- 2022 no-winner case study with stock, bond, cash, gold side-by-side.

## Interactive Demo Feedback

The existing `course/interactive/week07_rebalance_lab.html` matches the lesson well. It includes target stock weight, threshold band, calendar-only toggle, start-year slider, stock-weight drift chart, wealth path, rebalance events, turnover, CAGR, and max drawdown. It also supports multilingual labels and theme changes.

Suggested improvements:

- Add transaction cost and tax drag toggles. The lesson emphasizes taxes, but the interactive is pretax/frictionless.
- Add contribution-based rebalancing mode. This is the practical default for accumulators.
- Add annual / semiannual / quarterly calendar choices, not just calendar-only as a single annual rule.
- Add a comparison overlay: selected rule versus never rebalance versus annual 60/40.
- Add a 2022 scenario preset and a 2008-2009 preset.
- Add a turnover warning when a tight band creates many trades.

## New Interactive Demo Ideas

- Household asset-location rebalancer: enter balances in taxable, IRA, 401(k), target allocation, and current holdings; output which account should trade first.
- Tax-aware band optimizer: choose tax rate, transaction cost, and band width; see turnover and after-tax return.
- Behavioral panic simulator: choose whether to follow the rule or pause rebalancing in 2008/2020; compare outcomes.
- Active-position trim calculator: if one stock becomes 30% of net worth, show concentration risk and staged trimming options.

## Make It More Entertaining Without Watering It Down

The entertainment angle is that rebalancing is a robot that does the emotionally impossible trade. Personify the rule lightly: it has no ego, no FOMO, no CNBC, no neighbor with a sports car. It just restores the target.

## Money-Making Usefulness

This lesson helps students make money by preventing hidden risk creep and panic-driven timing mistakes. The highest-value practical addition would be a rebalancing policy template students can fill in once and reuse for decades.

## SOUL Consistency Flags

- Strong alignment with SOUL principle #12: survival and solvency beat being right.
- Good connection to tax-aware exposure management, though Week 7 only covers basic rebalancing.
- Needs corrected references to Week 5, Week 8, and Week 14.
- Be cautious when applying simple rebalancing-premium logic to barbell and option-based sleeves.
