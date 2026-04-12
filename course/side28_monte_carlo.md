# Side Lesson 28: Monte Carlo Simulation for Investors

---

## Part 1: Reading Section

---

### Introduction

Traditional financial planning uses straight-line projections: if your portfolio returns 7% per year, here is how much you will have in 30 years. But markets do not deliver smooth, predictable returns. Some years you gain 30%, others you lose 20%. The sequence in which these returns arrive matters enormously, especially in retirement when you are withdrawing money. Monte Carlo simulation addresses this by running thousands of randomized scenarios to model the range of possible outcomes. Instead of a single projection, you get a probability distribution that tells you how likely you are to meet your financial goals. It is one of the most powerful tools available to individual investors, and understanding how it works helps you make better decisions about saving, investing, and spending. Best of all, free tools make Monte Carlo accessible to anyone willing to spend thirty minutes learning the basics.

---

### A) Why Important

**Sequence of returns risk.** Two investors can have identical average returns over 30 years but completely different outcomes depending on when good and bad years occur. An investor who experiences bad returns early in retirement while withdrawing money can run out of money, even if later returns are excellent. Monte Carlo simulation captures this risk in a way that simple average-return projections cannot.

**Realistic planning.** A straight-line 7% annual return projection gives a false sense of precision. In reality, your portfolio might compound at anywhere from 3% to 11% annualized over 30 years, depending on market conditions. Monte Carlo shows you the full range of possible outcomes, helping you plan for realistic scenarios rather than a single guess.

**Decision confidence.** Should you retire at 60 or 65? Can you spend $80,000 per year or only $60,000? Should you keep 60% in stocks or shift to 40%? Monte Carlo provides quantitative answers to these questions by showing how each choice affects your probability of success across thousands of scenarios. This transforms gut feelings into data-driven decisions.

**Risk quantification.** Knowing that your plan has a 90% probability of success is far more useful than knowing that it "should work" based on historical averages. Monte Carlo gives you a specific probability, plus the range of outcomes in the bottom 10% so you can understand worst-case scenarios.

**Adaptive planning.** Monte Carlo is not a one-time exercise. Running simulations periodically, especially after major market moves or life changes, allows you to adjust your plan dynamically. If your probability of success drops below your comfort level, you can take action before it is too late. This iterative approach transforms retirement planning from a one-time event into an ongoing process of adjustment and optimization.

**Spousal coordination.** For couples, Monte Carlo simulation becomes even more valuable. It can model scenarios where one spouse retires before the other, where Social Security claiming strategies differ between spouses, where one spouse has a pension and the other does not, and where the surviving spouse's expenses change after the first spouse's death. These joint-life scenarios are significantly more complex than single-person planning and benefit enormously from the computational power of simulation.

**Communication tool.** For investors working with financial advisors, Monte Carlo results provide a common language for discussing risk, expectations, and tradeoffs. Seeing the probability distribution of outcomes makes abstract concepts concrete and facilitates better conversations about financial planning.

**Stress testing.** Monte Carlo allows you to test extreme scenarios: what if inflation averages 5% instead of 3%? What if stock returns are 4% instead of 7%? What if you live to 100? What if you face a major medical expense at age 75? Each of these scenarios can be modeled and their impact on your probability of success quantified. This stress testing is far more valuable than hoping for the best and assuming average returns.

---

### B) What You Need to Know

#### What Monte Carlo Simulation Actually Is

Monte Carlo simulation is a computational technique that uses random sampling to model uncertain outcomes. Named after the Monte Carlo Casino in Monaco, it was developed in the 1940s by scientists working on nuclear weapons research at Los Alamos National Laboratory. The insight is that when a system is too complex for analytical solutions, you can simulate it thousands of times with randomized inputs and observe the distribution of results.

In financial planning, the "system" is your portfolio growing and being withdrawn from over time. The randomized inputs are annual investment returns, which are drawn from a probability distribution based on historical data or forward-looking assumptions. Each simulation run produces a different sequence of returns, creating a different outcome for your portfolio. Running 10,000 simulations gives you 10,000 possible futures, from which you can calculate probabilities.

A simple example: instead of assuming your portfolio returns 7% every year for 30 years, the simulation might produce Year 1: +22%, Year 2: -8%, Year 3: +15%, Year 4: -3%, and so on. Each run generates a different random sequence. Some sequences lead to portfolio growth; others lead to running out of money. The percentage of runs where your portfolio survives is your "probability of success."

The key insight is that the order of returns matters as much as their average, especially when money is being added or withdrawn. Two investors with identical average returns can end up with vastly different outcomes depending on whether the good years come early or late. This is the essence of what Monte Carlo captures that simple projections miss.

The mathematical foundation involves drawing random returns from a specified distribution, typically a normal or lognormal distribution characterized by a mean (expected return) and standard deviation (volatility). More sophisticated simulations incorporate correlations between asset classes, fat tails (extreme events occurring more frequently than a normal distribution predicts), and mean reversion.

The beauty of Monte Carlo is its flexibility. Unlike closed-form mathematical solutions that require simplifying assumptions, Monte Carlo can model arbitrarily complex scenarios: variable spending, changing asset allocations, lumpy expenses, multiple income sources with different start dates, and tax rules. Each scenario is computed independently, and the probability distribution emerges naturally from the aggregate of thousands of trials. This computational brute force approach trades mathematical elegance for practical applicability.

Modern computing makes Monte Carlo trivially fast. A simulation that would have taken hours on a 1990s computer runs in seconds on a modern laptop or smartphone. This accessibility is why Monte Carlo has become the standard tool for retirement planning across the financial advice industry.

#### Key Inputs and Assumptions

The quality of a Monte Carlo simulation depends entirely on the quality of its inputs. Garbage in, garbage out. Here are the critical inputs.

**Expected return.** This is the average annual return you expect from your portfolio. Using historical averages (roughly 10% nominal for US stocks, 5% for bonds) is common but may overstate future returns if current valuations are elevated. Many financial planners use reduced forward-looking estimates, such as 7-8% for stocks and 3-4% for bonds, to be conservative.

**Volatility (standard deviation).** This measures how much returns vary around the average. US large-cap stocks have historically had a standard deviation of approximately 15-16%. Bonds are approximately 4-6%. A portfolio of 60% stocks and 40% bonds has a standard deviation of roughly 10%. Higher volatility means wider dispersion of outcomes.

**Correlation between asset classes.** Stocks and bonds historically have low or negative correlation, which is why combining them reduces portfolio volatility. The simulation should model returns for each asset class separately and combine them using historical correlations. This captures the diversification benefit. Note, however, that correlations are not stable: stocks and bonds were positively correlated in the 1970s and 1990s and negatively correlated in the 2000s and 2010s. Sophisticated simulations allow correlations to vary across scenarios.

**Inflation rate.** All projections should be in real (inflation-adjusted) terms, or inflation should be explicitly modeled. A common assumption is 2-3% annual inflation based on the Federal Reserve's long-term target and historical averages. Failing to account for inflation can make a plan look far more successful than it actually is. A plan showing $2 million at age 90 sounds comfortable, but if inflation averages 3% over 30 years, that $2 million has the purchasing power of only about $825,000 in today's dollars.

**Time horizon.** How many years is the simulation covering? For retirement planning, this is typically from retirement age to age 90 or 95. Longer time horizons increase uncertainty and require more conservative assumptions. Many planners now recommend simulating to age 95 or even 100 due to increasing longevity. For a couple both aged 65, there is roughly a 50% chance that at least one will live past 90 and a 25% chance past 95. Planning only to age 85 creates a significant risk of outliving your money.

**Withdrawal rate and pattern.** How much do you plan to withdraw annually? Is it a fixed dollar amount, a fixed percentage of the portfolio, or a variable strategy? The classic "4% rule" withdraws 4% of the initial portfolio value, adjusted for inflation each year. But actual spending patterns are rarely this smooth, most retirees spend more early in retirement and less later.

Research by David Blanchett of Morningstar found that real spending tends to follow a "smile" pattern: it is higher in early retirement (travel, activities), declines in mid-retirement (settling into routines), and then increases again in late retirement (health care costs). Modeling this more realistic spending pattern, rather than a flat inflation-adjusted amount, can significantly change the simulation results. A plan with front-loaded spending needs more portfolio early on, making sequence-of-returns risk even more important.

**Inflation variability.** Standard simulations use a constant inflation rate, but actual inflation varies significantly from year to year. Running simulations with variable inflation, drawn from a distribution rather than a fixed value, produces more realistic results. Periods of high inflation are particularly dangerous because they simultaneously increase spending needs and can reduce real portfolio returns.

**Tax considerations.** Withdrawals from tax-deferred accounts are taxed as ordinary income. Withdrawals from Roth accounts are tax-free. Taxable accounts generate capital gains. Sophisticated simulations model these differences.

**Social Security and other income.** Fixed income sources like Social Security, pensions, and annuities reduce the amount that must come from the portfolio. Including these sources significantly improves most plans' probability of success. Social Security alone can cover 30-50% of typical retirement spending, dramatically reducing the withdrawal rate from the investment portfolio.

**Sequence of returns sensitivity.** The simulation implicitly tests thousands of different return sequences. Research shows that the first 5-10 years of retirement are the most critical: poor returns in these years combined with withdrawals can permanently impair the portfolio. This is why some retirees consider a "bond tent" strategy, temporarily increasing bond allocation in the years immediately surrounding retirement to protect against sequence risk, then gradually increasing stocks again.

**Number of simulations.** Most tools run between 1,000 and 10,000 simulations. More simulations produce more stable probability estimates. Results generally stabilize above 5,000 runs.

**Asset allocation glide path.** Many retirees change their asset allocation over time, gradually shifting from stocks to bonds as they age. Sophisticated Monte Carlo tools allow you to model a declining equity allocation over the simulation period, such as starting at 60% stocks at retirement and declining to 40% stocks by age 85. This is more realistic than assuming a static allocation for 30 years.

**Health care costs.** Medical expenses are one of the largest and most variable costs in retirement. Fidelity estimates that an average retired couple will need approximately $315,000 for health care costs in retirement (excluding long-term care). Monte Carlo tools that allow you to model lumpy expenses, such as a major medical event at age 78, provide more realistic planning than smooth annual spending assumptions.

#### Interpreting Results: Probability of Success

The headline output of a Monte Carlo simulation is the probability of success, defined as the percentage of simulations where the portfolio does not run out of money before the end of the time horizon.

**What is a good probability?** There is no universal answer, but common guidelines suggest:
- 90%+ is considered very safe. You can likely spend more or retire earlier.
- 80-90% is a comfortable range for most retirees.
- 70-80% requires monitoring and flexibility to reduce spending if needed.
- Below 70% suggests the plan needs adjustment: save more, spend less, work longer, or take more risk.

**The paradox of 100%.** A plan with 100% probability of success is not optimal; it means you are probably being too conservative and leaving money unspent. If you die with a large portfolio, you could have retired earlier, spent more, or given more to charity. The goal is not to maximize the probability of success but to find the right balance between living well and not running out of money.

**Percentile outcomes.** Beyond the headline probability, examine the distribution of outcomes. The 10th percentile outcome shows what happens in poor scenarios. The 50th percentile (median) shows the most likely outcome. The 90th percentile shows what happens in good scenarios. The spread between the 10th and 90th percentiles shows the range of uncertainty.

For example, a simulation might show:
- 10th percentile: portfolio depleted at age 82
- 25th percentile: $200,000 remaining at age 95
- 50th percentile: $800,000 remaining at age 95
- 75th percentile: $1.8 million remaining at age 95
- 90th percentile: $3.2 million remaining at age 95
- Probability of success: 85%

This tells you much more than a single number. In good scenarios, you leave a substantial estate. In poor scenarios, you run out of money in your early 80s. This information helps you decide whether to take action.

#### The 4% Rule and Monte Carlo

The famous "4% rule" was derived by William Bengen in 1994 using historical US market data. He found that a retiree withdrawing 4% of their initial portfolio value, adjusted for inflation each year, would not have run out of money over any 30-year period in US history.

Monte Carlo simulation adds nuance to this rule. When you simulate using forward-looking return assumptions rather than backward-looking historical data, the safe withdrawal rate may be higher or lower than 4% depending on assumptions.

With historical US equity returns of 10% and volatility of 16%, a 4% withdrawal rate has roughly a 95% probability of success over 30 years. But with more conservative forward-looking assumptions of 7% returns, the probability drops to 80-85%. With international diversification (lower historical returns than the US), it drops further.

Monte Carlo also reveals the sensitivity of the plan to different variables. Small changes in the withdrawal rate have large effects on probability: moving from 4% to 5% might drop success probability from 85% to 65%. This sensitivity analysis is one of the most valuable outputs.

Variable withdrawal strategies, where you reduce spending during market downturns and increase it during booms, significantly improve outcomes compared to fixed withdrawals. Monte Carlo can model these dynamic strategies and show how much flexibility buys you in terms of probability improvement.

Several variable strategies have been tested extensively in the literature. The "guardrails" approach, developed by Jonathan Guyton and William Klinger, adjusts spending up or down by fixed percentages when the withdrawal rate drifts too far from the initial target. The "floor and ceiling" approach sets absolute bounds on annual spending adjustments. The "percent of portfolio" method withdraws a fixed percentage of the current portfolio value each year, automatically adjusting to market conditions but creating income volatility. Monte Carlo simulation can compare all these approaches to find which best suits your tolerance for spending variability versus probability of success.

The Bengen study also assumed a specific asset allocation of 50-75% stocks. Monte Carlo allows you to test different allocations and find the one that maximizes probability of success for your specific withdrawal rate and time horizon. Many simulations suggest that retirees should hold more stocks (60-70%) than conventional wisdom recommends, because the higher expected return offsets the higher volatility over long horizons.

#### Retirement Planning Tools

Several accessible tools bring Monte Carlo simulation to individual investors.

**Free tools.**
FireCalc (firecalc.com) uses historical return sequences rather than random sampling. It runs your plan through every possible historical starting year. This is technically not Monte Carlo but provides similar insights using actual market history.

cFIREsim is similar to FireCalc but with more customization options. It allows variable spending rules, Social Security timing, and different asset allocations.

Portfolio Visualizer (portfoliovisualizer.com) offers Monte Carlo simulation with customizable return assumptions, multiple asset classes, and various withdrawal strategies. The free version provides substantial functionality.

**Paid tools and advisor platforms.**
Financial planning software like MoneyGuidePro, eMoney, and RightCapital offer sophisticated Monte Carlo engines used by financial advisors. These incorporate taxes, Social Security optimization, Roth conversion strategies, and estate planning.

New Retirement (newretirement.com) provides a detailed DIY planning tool with Monte Carlo for a modest subscription fee. It is widely regarded as the best consumer-grade retirement planning tool.

**Brokerage tools.** Fidelity, Vanguard, and Schwab all offer retirement planning calculators with Monte Carlo components. These are convenient if you already hold your accounts there but may be less flexible than dedicated tools.

**Spreadsheet DIY.** For the technically inclined, Monte Carlo simulations can be built in Excel or Google Sheets using random number generation functions. The basic structure requires: a random return generator for each year (using NORMINV with RAND to create normally distributed returns), a portfolio value accumulator that applies returns and subtracts withdrawals, and a macro or iteration tool to run thousands of trials. While more effort than using a dedicated tool, building your own simulation deepens your understanding of the underlying mechanics and gives you complete control over assumptions.

**Important: validate your tool.** Whichever tool you use, validate it by running a known scenario. For example, a portfolio of 100% US stocks with 4% withdrawals over 30 years starting from 1926 should show approximately 95% historical success rate. If your tool produces a significantly different result, something may be misconfigured. Cross-referencing results across two different tools provides additional confidence.

#### Limitations of Monte Carlo Simulation

**Distribution assumptions.** Most Monte Carlo tools assume returns follow a normal distribution. In reality, markets exhibit "fat tails," meaning extreme events (crashes and booms) occur more frequently than a normal distribution predicts. Simulations based on normal distributions may understate the probability of catastrophic outcomes and overstate the probability of average outcomes.

**Stationarity assumption.** Standard Monte Carlo assumes that the statistical properties of returns (mean, volatility, correlations) remain constant over time. In reality, these properties change. Expected returns are lower when valuations are high. Correlations spike during crises. This assumption can lead to overly optimistic results during expensive markets and overly pessimistic results during cheap markets.

**Model risk.** The simulation is only as good as its assumptions. If you input overly optimistic returns, the results will look better than reality. If you use inappropriate volatility estimates, the range of outcomes will be wrong. Sensitivity analysis (running the simulation with different assumptions) helps identify how much the results depend on specific inputs.

**Behavioral factors.** Monte Carlo assumes you will follow your stated plan regardless of market conditions. In reality, many investors panic and sell during crashes, lock in losses, and then miss the recovery. The simulation cannot model the emotional decisions that often derail otherwise sound plans.

**Spending flexibility.** Most tools model spending as either fixed or following a simple rule. Real spending is lumpy: health care costs spike in your 70s and 80s, travel spending decreases as you age, and unexpected expenses arise. More realistic spending models improve the simulation's usefulness.

**Single-period assumptions.** Returns are typically modeled on an annual basis, ignoring intra-year volatility. A year where the market drops 30% and then recovers 30% looks identical to a year with a small net change, but the experience and behavioral impact are very different.

#### Practical Tips for Running Your Own Simulation

**Start simple.** Use one of the free tools mentioned above with your current portfolio value, target retirement age, expected spending, and a balanced asset allocation. Do not try to model every nuance on your first attempt. Get a baseline probability of success and then refine from there.

**Run multiple scenarios.** Do not rely on a single set of assumptions. Run a "base case" with moderate assumptions, a "conservative case" with lower returns and higher spending, and an "optimistic case" with favorable assumptions. The range of probabilities across these scenarios tells you how sensitive your plan is to assumptions.

**Test specific decisions.** Monte Carlo is most valuable when it helps you compare specific choices. Should you take Social Security at 62 or 67? Run both and compare probabilities. Should you convert some traditional IRA assets to Roth? Model the tax impact and see how it affects long-term outcomes. Should you downsize your home and invest the equity? Quantify the impact.

**Document your assumptions.** Write down the return, volatility, inflation, and spending assumptions you used. When you revisit the simulation in a year, you will want to know what changed and why the probability shifted.

**Do not over-optimize.** A plan that requires a specific sequence of actions over 30 years to achieve a 95% success rate is fragile. Prefer robust plans that work across a range of scenarios. A plan with 85% success and significant spending flexibility is often better than a rigid plan with 93% success.

**Integrate with your broader financial plan.** Monte Carlo should not exist in isolation. It should be part of a comprehensive financial plan that includes estate planning, insurance coverage, tax strategy, and contingency plans for major life events. The simulation answers the investment and spending question, but other planning elements determine whether you can actually execute the plan in practice.

**Consider using multiple tools.** Running your scenario through two or three different Monte Carlo tools provides a range of results that accounts for differences in methodology, assumptions, and calculation approaches. If all tools show probabilities in the 80-90% range, you can have higher confidence than if one shows 75% and another shows 95%. The disagreement between tools highlights sensitivity to methodology choices.

**Update after major market events.** When the stock market drops 20% or more, re-run your simulation immediately. A portfolio that had a 90% probability before a bear market might now show 75%. This early warning allows you to adjust spending or allocation before the situation worsens. Conversely, a strong bull market might push your probability above 95%, signaling that you can afford to relax spending constraints or consider early retirement.

---

### C) Common Misconceptions

**Misconception 1: "Monte Carlo tells me exactly what will happen."**
Monte Carlo shows the range of what could happen and the probability of different outcomes. It is not a prediction but a probability distribution. The actual future will be one specific path through the distribution, influenced by factors the model cannot anticipate (geopolitical events, pandemics, technological breakthroughs). Use the results as a planning guide, not a guarantee.

**Misconception 2: "A 90% probability of success means I am safe."**
A 90% probability means that in 10% of simulated scenarios, your plan fails. Over 10,000 simulations, that is 1,000 scenarios where you run out of money. Whether you are comfortable with a 1-in-10 chance of financial ruin depends on your risk tolerance and ability to adjust. Some retirees need 95%+ to sleep at night; others are comfortable with 80% because they have flexibility to reduce spending.

**Misconception 3: "I only need to run the simulation once."**
Your financial situation changes over time. Market returns, spending needs, health status, and income sources all evolve. Run the simulation at least annually, and after any major life event or market dislocation. A plan that had an 85% probability five years ago might now be at 75% or 95% depending on what has happened.

**Misconception 4: "Higher return assumptions make my plan better."**
Inputting higher expected returns increases the probability of success on paper but does not change reality. If the market delivers lower returns than assumed, your plan will fail faster than the simulation predicted. It is better to use conservative assumptions and be pleasantly surprised than to use optimistic assumptions and be devastated.

**Misconception 5: "Monte Carlo accounts for all risks."**
Monte Carlo models investment return uncertainty but typically ignores inflation spikes, health care cost surges, longevity beyond age 95, tax law changes, and political risks. These factors can derail a plan that Monte Carlo says is safe. Use the simulation as one input into your planning, not the only input.

**Misconception 6: "The 4% rule makes Monte Carlo unnecessary."**
The 4% rule is a historical observation based on US market data. It does not account for your specific situation: your asset allocation, your other income sources, your tax situation, your spending flexibility, or your life expectancy. Monte Carlo customizes the analysis to your circumstances and provides probability-based answers rather than a one-size-fits-all rule.

**Misconception 7: "I can ignore inflation in my simulation."**
Inflation is one of the most destructive forces for retirees. At 3% annual inflation, the purchasing power of a dollar halves in about 24 years. A retirement plan that looks solid in nominal terms may be deeply inadequate in real terms. Always run simulations using real (inflation-adjusted) returns or explicitly model inflation as a separate variable. Periods of high inflation, like the 1970s or 2021-2022, are particularly dangerous for retirees with fixed spending plans because both their purchasing power and their portfolio values decline simultaneously.

**Misconception 8: "Monte Carlo is only for people near retirement."**
Monte Carlo is valuable at any stage of wealth accumulation. A 30-year-old can use it to estimate the probability of reaching their target retirement portfolio by age 55 or 60 under different savings rates and investment assumptions. A 40-year-old can model whether paying off the mortgage or investing the money produces a better probability of meeting retirement goals. The earlier you start running simulations, the more time you have to adjust your plan.

---

### D) Q&A Section

**Q1: What return and volatility assumptions should I use?**
A1: For a diversified stock portfolio, conservative forward-looking assumptions might be 6-8% nominal return with 15-16% standard deviation. For bonds, 3-4% nominal with 5-6% standard deviation. For a 60/40 portfolio, roughly 5-6% nominal with 10% standard deviation. Use real (after-inflation) returns if your spending is in real terms. When in doubt, use lower return assumptions; it is better to over-save than to under-save.

**Q2: How many simulations do I need to run?**
A2: Results become stable around 5,000 to 10,000 simulations. Below 1,000, the probability estimates can vary meaningfully depending on the random draws. Most modern tools run 10,000 by default, which is more than sufficient. Running more than 10,000 provides negligible additional precision for retirement planning purposes.

**Q3: Should I use historical returns or forward-looking estimates?**
A3: Both have merit. Historical returns reflect what actually happened but may not represent the future, especially if current conditions (valuations, interest rates, demographics) differ from historical averages. Forward-looking estimates incorporate current conditions but are inherently uncertain. Many advisors recommend running simulations with both sets of assumptions and basing decisions on the more conservative results.

**Q4: How do I account for Social Security in the simulation?**
A4: Enter Social Security as a fixed income stream starting at your planned claiming age. This reduces the amount your portfolio needs to fund, significantly improving the probability of success. For planning purposes, some conservative planners reduce the expected Social Security benefit by 20-25% to account for potential future benefit cuts. Run the simulation both with and without Social Security to understand your dependence on it.

**Q5: What withdrawal strategy works best in Monte Carlo simulations?**
A5: Variable strategies consistently outperform fixed withdrawal rates. The "guardrails" approach is particularly effective: set a target withdrawal rate (say 4%), but reduce spending by 10% if your portfolio drops below a lower guardrail, and allow spending increases of 10% if the portfolio rises above an upper guardrail. This flexibility dramatically improves the probability of success compared to a rigid fixed withdrawal.

**Q6: Can Monte Carlo help with the decision to retire early?**
A6: Absolutely. Run the simulation for different retirement ages and compare the probabilities. Retiring at 55 instead of 65 adds 10 years of withdrawals and eliminates 10 years of contributions, which can dramatically change the probability of success. The simulation quantifies exactly how much each additional year of work improves your odds, helping you find the earliest retirement age that still maintains an acceptable probability.

**Q7: How do I handle a pension or annuity in the simulation?**
A7: Enter these as fixed income streams, similar to Social Security. Pensions and annuities provide guaranteed income that reduces portfolio withdrawal needs. If the pension has a cost-of-living adjustment (COLA), model the income as growing with inflation. If it is a fixed nominal payment, model it as a flat dollar amount that loses purchasing power over time. The guaranteed income floor from pensions, annuities, and Social Security is one of the most powerful ways to improve Monte Carlo outcomes.

**Q8: What should I do if my Monte Carlo probability is too low?**
A8: You have several levers to improve the probability. Save more now. Reduce planned spending. Delay retirement by one or two years (this has an outsized impact because it adds contributions and shortens the withdrawal period). Adjust your asset allocation. Consider part-time work in early retirement. Optimize Social Security claiming strategy. Reduce housing costs. Each of these changes can be modeled individually to see which has the largest impact on your specific situation.

**Q9: How do Monte Carlo results differ from historical backtests like FireCalc?**
A9: Historical backtesting (FireCalc-style) uses actual historical return sequences: starting in 1926, 1927, 1928, and so on. It tells you how your plan would have performed in every historical period. Monte Carlo generates random sequences based on statistical properties. Historical backtests are limited to about 100 starting years, so you only get roughly 100 scenarios. Monte Carlo generates 10,000+. Historical backtests assume the future will resemble the past. Monte Carlo allows you to change assumptions about future returns. Both approaches are valuable, and ideally you should use both. If your plan passes both historical backtests and Monte Carlo with conservative assumptions, you can have higher confidence.

**Q10: Can I use Monte Carlo for goals other than retirement?**
A10: Absolutely. Monte Carlo works for any financial goal with uncertain returns and a specific time horizon. Saving for a child's college education in 15 years, building a down payment fund over 5 years, or accumulating a target portfolio value by a specific date can all be modeled. The inputs change (no withdrawals during accumulation, different time horizons, different target amounts), but the methodology is identical. Some tools even model multiple goals simultaneously, showing the probability of achieving each one given your total resources.

---

## Part 2: YouTube Script

---

**TITLE: Monte Carlo Simulation: The Retirement Planning Tool You Need**

**LENGTH: Approximately 17 minutes**

---

**[VISUAL: Casino roulette wheel spinning, then morphing into a retirement portfolio graph with thousands of lines fanning out]**

**Alex:** Sam, I have heard that Monte Carlo simulation can tell me whether I will run out of money in retirement. That sounds both amazing and intimidating. What is it, and do I need a math degree to use it?

**Sam:** You absolutely do not need a math degree. The concept is intuitive once you see it in action.

**Sam:** It is actually simpler than it sounds. Instead of assuming your portfolio grows at a nice, steady seven percent every year, Monte Carlo asks: what if returns are random?

**[ANIMATION: Single straight line showing 7% annual growth. Then the line shatters into thousands of squiggly lines, some going up dramatically, some going down to zero]**

**Sam:** Each of those lines represents one possible future. In some futures, the market booms and you end up wealthy. In others, a crash early in retirement devastates your portfolio. Monte Carlo runs thousands of these scenarios and counts how many times your money lasts.

**Alex:** So it is like running my retirement plan through ten thousand alternate realities?

**Sam:** Exactly. And the percentage of realities where you do not run out of money is your "probability of success."

**[VISUAL: Counter showing "10,000 simulations" with a success/failure tally. Final result: "8,500 success / 1,500 failure = 85% probability of success"]**

**Alex:** Why can I not just use the average return and call it a day?

**Sam:** Because of something called sequence of returns risk. Let me show you why it matters so much.

**[ANIMATION: Two investors, both getting the same set of annual returns over 20 years, but in different orders. Investor A gets bad returns early and good returns late. Investor B gets good returns early and bad returns late. Both withdrawing the same amount annually]**

**Sam:** Both investors have the same average return over twenty years: seven percent. But Investor A, who got the bad years early while withdrawing money, runs out at age seventy-eight. Investor B, who got the good years early, has over a million dollars left.

**Alex:** Same average return, completely different outcomes. That is terrifying.

**Sam:** This is why straight-line projections are dangerous. They hide the single biggest risk retirees face: getting unlucky with the sequence of returns in the early years.

**[VISUAL: Side-by-side portfolio value charts for Investor A and B, diverging dramatically despite identical average returns]**

**Alex:** So what goes into a Monte Carlo simulation? What are the inputs?

**Sam:** There are several key inputs. Let me walk through them.

**[ANIMATION: Input form appearing with fields being filled in one by one]**

**Sam:** First, your starting portfolio value. Say one million dollars. Second, your expected return and volatility for each asset class. For stocks, maybe seven percent return with fifteen percent volatility. For bonds, four percent with five percent volatility.

**Alex:** Where do those numbers come from?

**Sam:** Historical data adjusted for current conditions. US stocks have historically returned about ten percent, but with today's higher valuations, many planners use seven to eight percent as a more realistic forward-looking estimate.

**[VISUAL: Historical return distribution bell curve for stocks, with the mean and standard deviation labeled]**

**Sam:** Third, your asset allocation. Sixty percent stocks, forty percent bonds. Fourth, your annual withdrawal amount, say forty thousand dollars, adjusted for inflation at three percent per year.

**Alex:** And then the computer runs random scenarios?

**Sam:** Right. In each simulation, the computer randomly generates annual returns from the specified distribution. Year one might be plus twenty-two percent. Year two might be minus fourteen percent. Year three might be plus nine percent. Each simulation creates a different random sequence.

**[ANIMATION: Random number generator spinning, producing annual returns that feed into a portfolio growth model. Portfolio balance rising and falling over 30 simulated years]**

**Sam:** After running ten thousand of these sequences, you get a distribution of outcomes.

**[VISUAL: Fan chart showing the 10th, 25th, 50th, 75th, and 90th percentile portfolio trajectories over 30 years, with a horizontal red line at zero]**

**Alex:** What am I looking at here?

**Sam:** The dark middle line is the median outcome, the fiftieth percentile. The shaded bands show different probability ranges. The key is the bottom band, the tenth percentile. That is what happens in the worst ten percent of scenarios.

**Alex:** And if that bottom line hits zero, I have run out of money in those bad scenarios.

**Sam:** Exactly. In this example, the bottom ten percent of scenarios run out of money around year twenty-five. The median scenario ends with over a million dollars. The top ten percent ends with over three million. Same starting conditions, vastly different outcomes.

**Alex:** So what is a good probability of success? Should I aim for a hundred percent?

**Sam:** Here is where people get confused. Many people think a hundred percent is the goal, but it is actually a signal of a different problem.

**[ANIMATION: Probability gauge showing different zones: Below 70% = "Needs Work" (red), 70-80% = "Caution" (yellow), 80-90% = "Comfortable" (light green), 90%+ = "Very Safe" (dark green), 100% = "Probably Too Conservative" (blue)]**

**Sam:** A hundred percent probability means you are being extremely conservative. You are probably spending too little and will leave a fortune behind. That is not the goal unless leaving a large inheritance is your primary objective.

**Alex:** So what is the sweet spot?

**Sam:** For most people, eighty to ninety percent. That means you have a high likelihood of success but are not so conservative that you sacrifice quality of life. The key is having flexibility to adjust if things go poorly.

**Alex:** What about the famous four percent rule? How does it hold up in Monte Carlo?

**Sam:** The four percent rule says you can withdraw four percent of your initial portfolio, adjusted for inflation, for thirty years. Let me show you what Monte Carlo says about it.

**[VISUAL: Monte Carlo results for the 4% rule at different return assumptions. Historical returns: 95% success. Conservative forward returns: 80-85% success. Very conservative: 70% success]**

**Sam:** With historical return assumptions, the four percent rule has about a ninety-five percent success rate. But with more conservative forward-looking assumptions, it drops to eighty to eighty-five percent. If the next thirty years deliver lower returns than history, the four percent rule might be too aggressive.

**Alex:** That is eye-opening. What improves the numbers?

**Sam:** Flexibility is the single most powerful improvement. Instead of withdrawing a fixed amount regardless of market conditions, adjust your spending.

**[ANIMATION: "Guardrails Strategy" showing a corridor. Upper guardrail: "Portfolio up 20%+ from plan -> increase spending 10%." Lower guardrail: "Portfolio down 20%+ from plan -> decrease spending 10%."]**

**Sam:** The guardrails approach sets an upper and lower boundary. If your portfolio surges well above plan, you give yourself a raise. If it drops significantly, you tighten the belt. This flexibility can improve your probability of success from eighty percent to over ninety percent without changing your starting withdrawal rate.

**Alex:** Where can I actually run these simulations?

**Sam:** Several free tools are available.

**[VISUAL: Screenshots of three tools side by side: Portfolio Visualizer, FireCalc, and cFIREsim with brief descriptions]**

**Sam:** Portfolio Visualizer has a great Monte Carlo tool with customizable assumptions. FireCalc runs your plan through every historical period, which is technically not Monte Carlo but gives similar insights. And cFIREsim offers the most customization options for free.

**Alex:** What are the limitations I should know about?

**Sam:** Three big ones. First, most tools assume returns follow a normal bell curve distribution. But real markets have fat tails, meaning crashes happen more often than the models predict.

**[ANIMATION: Normal bell curve overlaid with actual market return distribution showing fatter tails, with the excess highlighted]**

**Sam:** Second, the simulation assumes you will stick to your plan no matter what. In reality, people panic and sell at the worst times. No model can account for behavioral mistakes.

**Alex:** And the third?

**Sam:** The inputs are assumptions, not facts. If you assume eight percent returns and the market only delivers five percent, your ninety percent success plan might actually be a sixty percent success plan. Always run simulations with conservative assumptions and see how sensitive the results are to changes.

**[VISUAL: Sensitivity analysis table showing probability of success at different return/withdrawal rate combinations. Returns across the top (5%, 6%, 7%, 8%), withdrawal rates down the side (3%, 3.5%, 4%, 4.5%, 5%). Each cell shows probability of success]**

**Alex:** That sensitivity table is really useful. I can see exactly how each variable affects my odds.

**Sam:** That is the power of Monte Carlo. It turns vague anxiety about retirement into specific, quantifiable probabilities. You can see exactly how much saving one more year, or cutting spending by ten percent, or adjusting your allocation, changes your odds of success.

**[VISUAL: Three scenario comparisons: "Retire at 62" (75% success), "Retire at 64" (87% success), "Retire at 62 but reduce spending 15%" (88% success)]**

**Alex:** So the bottom line is: run the simulation, aim for eighty to ninety percent, build in flexibility, and check back regularly?

**Sam:** Exactly. And remember, Monte Carlo is a planning tool, not a crystal ball. Use it to inform your decisions, not to dictate them. The real value is understanding the range of outcomes so you can prepare for both the good scenarios and the bad ones.

**[VISUAL: Summary card showing key takeaways: Sequence of returns matters, Aim for 80-90% success, Use conservative assumptions, Flexibility is your superpower, Check annually, 4% rule is a starting point not a law]**

**Alex:** Thanks Sam. I feel much more confident about planning for retirement now.

**Sam:** The best part is you can do this yourself tonight with free tools. Run the numbers, see where you stand, and start making informed decisions.

**Alex:** One last thing. If I run the simulation and I am at seventy-five percent, should I panic?

**Sam:** No. Seventy-five percent means you need to make some adjustments but you are not in crisis. Small changes compound into big probability improvements. Saving an extra five hundred dollars per month, delaying retirement by one year, or reducing planned spending by ten percent could each push you above eighty-five percent. The simulation tells you precisely how much each lever moves the needle.

**[VISUAL: Before/after comparison showing 75% success improving to 88% with three small adjustments: $500/month more savings, 1 year later retirement, 8% less spending. Each adjustment shown with its individual probability improvement]**

**Alex:** That is incredibly empowering. Instead of worrying vaguely about retirement, I can quantify exactly where I stand and what to do about it.

**Sam:** That is the whole point. Turn anxiety into arithmetic. Then take action on the specific levers that matter most for your situation.

**[VISUAL: End screen with channel subscribe button and links to related lessons on retirement planning and withdrawal strategies]**

---

*End of Side Lesson 28*

---

*Supplementary Resource: Try running your first Monte Carlo simulation at portfoliovisualizer.com/monte-carlo-simulation with your own portfolio data to see where you stand.*
