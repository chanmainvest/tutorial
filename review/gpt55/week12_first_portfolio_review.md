# Review: course/week12_first_portfolio.md

## Overall Assessment

Week 12 is the right Level 1 capstone. It turns concepts into action: open account, choose allocation, pick ETFs, set contributions, schedule rebalancing. This is exactly the kind of lesson that can change student behavior.

The biggest weakness is audience mismatch. The account hierarchy is US-taxpayer-specific, while the course repeatedly speaks to Hong Kong/Mainland/Taiwan readers. A non-US reader following this blindly could make poor wrapper and tax decisions, especially around US-listed ETFs, withholding tax, and estate tax. The lesson also contains several course-map inconsistencies and a few allocation table/script mismatches.

## Content Critique

- The "build the thing" framing is excellent and gives Level 1 a concrete payoff.
- The six-step build is clear and should become a reusable checklist.
- The account-type section is useful for US investors but needs a prominent jurisdiction warning. 401(k), HSA, Roth IRA, backdoor Roth, and US taxable brokerage do not apply globally.
- For Hong Kong, Mainland, Taiwan, Singapore, or other non-US readers, the lesson needs a separate implementation path: local broker access, US withholding tax, estate tax, Irish-domiciled UCITS alternatives where appropriate, FX conversion, local retirement wrappers, and account safety.
- "Tax-advantaged before taxable, every time" is not universally true outside the US. In Hong Kong, for example, taxable brokerage treatment is very different from US taxable brokerage.
- The five archetypes are useful, but the ex-US sleeve needs to be reconciled with SOUL's US-first investable-universe stance. Teach the orthodox global-diversification case first, then Horace's caveat.
- The FIRE/barbell-curious row is interesting but should be clearly labeled advanced/experimental, not a standard beginner allocation.
- The ETF list is concrete and useful, but "US-listed only" should be paired with a non-US-tax warning.
- GLD is expensive relative to IAU/GLDM. If cost minimization is a theme, lead with the cheaper gold ETF unless liquidity/option-chain reasons justify GLD.
- The lump-sum versus DCA section is strong and honest: mathematically lump sum usually wins; behaviorally DCA may be worth the expected-return cost.
- The monitoring cadence is excellent: quarterly check, annual rebalance, life-event review.

## Cross-Reference And Consistency Issues

- The opening says the first eleven weeks covered valuation and fees, but detailed valuation is later and fees were a side lesson, not a core Week 1-11 topic.
- The L2 preview says "weeks 26 onward" but the next core week is Week 13 and Level 2 begins there in the visible course map.
- §2.7 references Weeks 23, 26, 31, 35, 47, 50 in ways that do not match the actual core sequence described nearby.
- Q12 says Weeks 13-25 layer factor tilts, tax management, and asset-location optimization, but Week 13 is long/short, Week 14 pair trading, and tax management appears elsewhere.
- Q5 says the early-career archetype has 5% bond + 5% TIPS, but the table has 5% intermediate bonds, 0% TIPS, 5% gold, and 5% cash.
- The script says Level 2 starts with factor tilts, tax management, and options overlays; the actual Week 13 is long/short.

## Presentation Improvements

- Add two tracks: "US taxpayer implementation" and "non-US investor implementation." The current lesson should not pretend one account stack fits all readers.
- Add a first-portfolio worksheet: goal, horizon, risk capacity, risk willingness, account type, allocation, ETFs, contribution date, rebalance date.
- Add an account hierarchy flowchart by jurisdiction.
- Add a risk-capacity quiz before the archetype table.
- Add a "do this by Friday" checklist at the end.
- Add a non-US ETF caveat box before recommending US-listed ETFs.
- Add an ETF selection rubric: expense ratio, domicile/tax, liquidity, spread, tracking error, securities lending, currency.

## YouTube Script Critique

The script is clean, practical, and watchable. The promise of a real portfolio by Friday is a strong retention hook.

Specific improvements:

- Make Stella the implementation proxy: she should ask, "I live in Hong Kong/Taiwan/Mainland. Do I still use this account order?" That forces the course to address the global audience.
- Add a visual checklist that fills in as the episode progresses.
- Do not say "By Friday" without adding a suitability caveat for emergency funds, debt, tax status, and jurisdiction.
- Replace "Level 2: factor tilts, tax management, options overlays" with the actual next-week/next-level sequence.
- Add a closing assignment: choose one archetype, write the target weights, and schedule the first contribution.

## Chart And Visual Feedback

Existing visuals are useful:

- Archetype allocation stacked bars are exactly right.
- Archetype outcome lines make risk/return trade-offs visible.

Recommended upgrades:

- Add a drawdown chart for each archetype, not only wealth lines.
- Add a contribution-growth chart showing why habit matters more than starting amount.
- Add a fee/tax drag chart comparing 0.05%, 0.50%, and 1.00% cost over 30 years.
- Add a country-specific account flowchart.
- Add a one-screen implementation checklist.

## Interactive Demo Feedback

The referenced `course/interactive/week12_portfolio_builder.html` sounds like the right capstone tool: sliders for US, ex-US, bonds, gold, cash remainder, archetype presets, and real wealth outcomes with return/drawdown/Sharpe.

Suggested improvements:

- Add a jurisdiction selector that changes warnings and account/ETF suggestions.
- Add expense ratio and tax-drag assumptions.
- Add emergency-fund and debt gates before recommending investment deployment.
- Add a contribution schedule simulator, not only starting allocation.
- Add a stress-test panel: 1932, 1973-74, 2008, 2022.
- Add "can you hold this?" prompts based on max drawdown.

## New Interactive Demo Ideas

- First portfolio checklist generator: outputs target allocation, ETFs, contribution schedule, rebalance date, and IPS summary.
- Account wrapper decision tree by country.
- DCA versus lump-sum simulator with regret and drawdown views.
- Tax location simulator: taxable versus tax-advantaged asset placement.
- ETF comparison tool: VTI/VOO/SPY, VXUS/IXUS, BND/AGG, IAU/GLDM.

## Make It More Entertaining Without Watering It Down

The entertainment is the action challenge: the viewer can finish the episode with a portfolio. Use a progress meter and Stella's actual example account. Let the audience watch the boring portfolio become real step by step.

## Money-Making Usefulness

This is one of the highest money-usefulness lessons because it turns education into execution. The key upgrade is preventing jurisdiction-specific tax mistakes. A technically good US portfolio can be a poor non-US implementation if withholding, estate tax, account rules, or FX costs are ignored.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #1, #2, #3, #12, #13, and #17.
- Needs cleaner orthodox-first framing around ex-US diversification versus Horace's US-first investable-universe view.
- Needs careful handling of barbell language so FIRE/barbell-curious does not look like a beginner default.
- Must fix course-map references before publication.
