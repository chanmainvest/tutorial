# Review: course/week04_sixty_forty.md

## Overall Assessment

Week 4 is one of the clearest SOUL-aligned lessons so far. It teaches the orthodox 60/40 portfolio as a baseline, explains why it worked, then shows why 2022 exposed the regime dependency. The structure is good: mechanics, history, correlation, 2022, adaptations. This is exactly how the course should handle canonical professional ideas that Horace no longer treats as final answers.

The main issues are cross-reference drift, a mismatch between the promised interactive and the actual interactive, and some claims that need tighter caveats. The lesson is strongest when it says 60/40 is not broken but is no longer default-best. It is weaker when it implies modern replacements like long-vol or trend "pay for themselves" without discussing bleed, manager selection, implementation cost, and tax.

## Content Critique

- The opening gives four strong reasons to understand 60/40 even if the student will not run it. This is pedagogically right.
- The portfolio-volatility formula is appropriate, but beginners need one worked numeric example before the table. Show why 60% stocks + 40% bonds does not equal 60% of stock risk plus 40% of bond risk.
- The lesson correctly identifies correlation as the hidden variable. This should become a recurring course-wide concept.
- The historical growth chart and decade table are useful, but the figures should cite data source and assumptions near the table: annual rebalancing, 10-year Treasuries, Damodaran returns, CPI-adjusted.
- "The 1980s and 1990s are the two decades that built 60/40's reputation" is true but incomplete; the 2000s also reinforced the narrative because bonds saved equity investors during dot-com and GFC drawdowns.
- "Cash earned under inflation" in the 2022 section is unclear. If the meaning is cash lost less than long bonds because duration was near zero, say that directly.
- The 2022 explanation is strong: same rate shock hit both long bonds and equity multiples. This is teachable and concrete.
- Gold discussion needs more nuance. Gold can help in monetary/inflation shocks, but it does not reliably rise in every inflation year, especially when real rates rise sharply.
- Long-volatility and trend-following sleeves need cost caveats. Long vol bleeds; managed futures have manager/model risk and can disappoint outside trend regimes.
- The barbell discussion is SOUL-consistent, but it arrives early. Add a clear warning: the barbell is an advanced migration path, not a Week 4 implementation instruction.
- Q8 mentions crypto as part of asymmetric speculation. That may be fine if intentionally linked to store-of-value / speculation, but "crypto" as a broad bucket is too loose for a beginner allocation lesson. Prefer "Bitcoin or specific asymmetric trades, sized as speculation."

## Cross-Reference And Consistency Issues

- The intro says "the barbell shape we get to in Week 14," but Week 14 is pair trading in the course map. If the barbell is introduced elsewhere, update the reference.
- Q10 says Week 5 covers diversification more deeply, but Week 5 is bonds. The end screen also says "Next: Week 5 — Diversification Done Right," which conflicts with the actual Week 5 title.
- Q10 says Week 13-14 introduce the barbell, but Week 13 is long/short and Week 14 is pair trading. This should be corrected or the related lessons should actually introduce barbell framing.
- The markdown says the interactive lets users adjust rebalance frequency "from monthly to never," but the actual interactive only offers annual rebalance versus never.

## Presentation Improvements

- Add a simple "why 60/40 worked" visual equation: falling inflation + falling rates + negative stock/bond correlation + Fed put = 60/40 golden age.
- Add a "what broke" checklist: inflation shock, rate shock, positive correlation, duration risk, real-return loss.
- Add a table comparing 60/40, 60/30/10, 55/30/10/5, Permanent Portfolio, and barbell preview by expected regime.
- Add a decision box: "If your risk problem is recession, bonds may help; if your risk problem is inflation, bonds may not."
- Add a beginner exercise: pick a stock/bond/cash/gold allocation and write down which macro shock it is designed to survive.

## YouTube Script Critique

The script is concise and has a strong question: "Is it broken or not?" That question should appear in the first five seconds, maybe even before the title card.

Specific improvements:

- Use 2022 as the cold open: show stocks down, bonds down, CPI up, 60/40 real loss. Then ask: "Was the safest portfolio actually safe?"
- Stella should ask: "If 60/40 failed in exactly the year people needed protection, why call it not broken?" This lets Horace define regime specificity.
- The correlation flip should be animated as the central visual moment. Make the line crossing zero feel dramatic.
- Add one concrete investor example: a retiree with $1M in 60/40 losing roughly $180K nominal and more in real terms in 2022.
- The adaptations section needs caveats in-video. "Gold is not magic; long vol bleeds; cash has reinvestment risk; every fix has a cost."
- The end-screen title should match the actual next lesson.

## Chart And Visual Feedback

Existing charts are good and necessary:

- 60/40 growth chart is useful, especially in real terms.
- Stock-bond correlation chart is the most important chart in the lesson.
- Decade table is helpful but should be visually upgraded.

Recommended upgrades:

- Correlation-regime heatmap: inflation-dominant versus growth-dominant regimes, with stock/bond correlation sign.
- 2022 anatomy waterfall: S&P return, Treasury return, inflation, real 60/40 return.
- Portfolio regime matrix: recession shock, inflation shock, liquidity shock, growth boom; show which sleeves help or hurt.
- Duration sensitivity mini-chart: how a rate increase affects long bonds versus T-bills.
- 60/40 versus modified portfolios from 1970s, 2008, 2022, and 2020.

## Interactive Demo Feedback

The existing `course/interactive/week04_sixty_forty.html` is useful: it has a stock-weight slider, annual-vs-never rebalancing, real/nominal toggle, cumulative wealth, drawdown chart, CAGR, volatility, max drawdown, Sharpe, multilingual labels, and theme support.

Suggested fixes and upgrades:

- Align the markdown description with the actual control. Either add monthly / quarterly / annual / never to the interactive, or change the prose to "annual versus never."
- Add cash / T-bill and gold sleeves. The lesson's main thesis is that 60/40 needs modern adaptation; the interactive should let readers test those adaptations.
- Add a correlation slider or regime presets. The lesson says correlation is the key variable, but the interactive only uses historical data and does not let the student manipulate correlation.
- Add scenario buttons: 1970s inflation, 2008 deflationary crisis, 2022 inflation shock, 2020 Fed-put crash/rebound.
- Add tax-aware rebalancing note or toggle. Rebalancing looks clean in pretax data but can be less attractive in taxable accounts.
- Consider finer stock-weight increments than 10% if the chart remains responsive, or keep 10% but label it as a teaching simplification.

## New Interactive Demo Ideas

- 60/40 regime lab: select growth shock, inflation shock, rate shock, liquidity shock, and watch stock, bond, cash, gold, trend, and long-vol sleeves respond.
- Correlation arithmetic sandbox: input asset volatilities, weights, and correlation; output portfolio volatility and diversification benefit.
- Duration shock calculator: choose bond duration and rate move; output approximate price loss.
- Rebalance tax drag simulator: annual rebalancing in taxable versus tax-sheltered accounts.
- Portfolio replacement builder: start from 60/40 and swap bond weight into cash, gold, managed futures, or tail hedge; compare historical scenarios.

## Make It More Entertaining Without Watering It Down

Turn 60/40 into a detective story: the portfolio did not randomly fail; the hidden suspect was correlation. The viewer should feel the reveal when the correlation line flips positive. That is more interesting than saying "2022 was bad" and teaches the real mechanism.

## Money-Making Usefulness

This lesson helps students avoid blindly copying legacy allocations. The practical money skill is regime matching: know what shock your safety sleeve is supposed to hedge. A portfolio that hedges recession may fail in inflation; a portfolio that hedges inflation may bleed in disinflation. Make students state their assumed regime before choosing the allocation.

## SOUL Consistency Flags

- Strong alignment with SOUL principles #2, #8, #14, and #17.
- Good orthodox-first structure: teach 60/40, then explain why Horace no longer treats it as optimal.
- Fix incorrect references to Week 5, Week 13-14, and Week 14 barbell.
- Add caveats that the barbell and long-vol sleeves are advanced, costly to implement, and not beginner defaults.
