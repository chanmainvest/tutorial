<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Side Lesson 19: Correlation, Covariance, and Portfolio Mathematics

---

## Reading Section

Diversification is the closest thing to a free lunch in investing -- but the reason it works is mathematical, not magical. At its core, portfolio diversification reduces risk because different assets do not move perfectly together. The mathematical concepts that describe this phenomenon -- correlation, covariance, and portfolio variance -- are the foundation of modern portfolio theory. Understanding these concepts does not require advanced mathematics, but it does require careful thinking about how assets interact within a portfolio. This lesson walks through the math of diversification, explains why correlations matter so much for portfolio construction, and addresses the uncomfortable reality that correlations tend to increase during market crises -- precisely when diversification is needed most.

---

### a) Why This Is Important

**Diversification Is Not Just "Owning More Stuff."** Many investors believe they are diversified because they own many different stocks or funds. But if all those holdings are highly correlated -- they move up and down together -- the portfolio is not truly diversified. Understanding correlation helps you build portfolios where the components genuinely offset each other's risks.

**Risk Is Not Additive.** If you invest 50% in Stock A (which has 20% volatility) and 50% in Stock B (which also has 20% volatility), the portfolio's volatility is NOT 20%. It is less -- sometimes significantly less -- depending on the correlation between A and B. This non-additive property of risk is the fundamental reason diversification works, and understanding the math behind it changes how you think about portfolio construction.

**Asset Allocation Decisions.** The covariance matrix -- the full set of correlations and volatilities for all assets in a portfolio -- is the primary input to mean-variance optimization, the framework used by institutional investors to determine optimal asset allocations. While you do not need to solve optimization problems yourself, understanding the inputs helps you evaluate whether your portfolio is efficiently constructed.

**Crisis Awareness.** One of the most important practical lessons from portfolio mathematics is that correlations are not stable. They increase during market crises, a phenomenon called "correlation breakdown" (or more accurately, correlation convergence). The diversification you thought you had can partially evaporate at the worst possible moment. Knowing this helps you build portfolios that account for stressed correlations, not just normal conditions.

**Evaluating Diversifiers.** When someone recommends adding an asset to your portfolio for "diversification," correlation is how you evaluate that claim. If the proposed asset has a correlation of 0.95 with your existing holdings, it adds almost no diversification benefit. If the correlation is 0.2, it adds a great deal. The math gives you an objective framework for these decisions.

---

### b) What You Need to Know

#### Understanding Correlation

The correlation coefficient measures the strength and direction of the linear relationship between two variables. In investing, it measures how two assets' returns tend to move together.

**Correlation ranges from -1 to +1:**

- **+1.0 (Perfect Positive Correlation):** The two assets always move in the same direction by proportional amounts. There is no diversification benefit from combining them. Example: Two index funds tracking the same index.

- **0 (Zero Correlation):** The assets' movements are completely independent. Combining them provides significant diversification. Example: Historically, gold returns have had near-zero correlation with stock returns over long periods.

- **-1.0 (Perfect Negative Correlation):** The assets always move in exactly opposite directions. A portfolio of two perfectly negatively correlated assets could theoretically have zero volatility. In practice, perfect negative correlation is virtually nonexistent among real assets.

**Typical Correlation Values in Practice:**

| Asset Pair | Approximate Correlation |
|---|---|
| U.S. Large Cap vs. U.S. Small Cap | 0.85-0.90 |
| U.S. Stocks vs. International Developed | 0.75-0.85 |
| U.S. Stocks vs. Emerging Markets | 0.65-0.75 |
| U.S. Stocks vs. U.S. Aggregate Bonds | 0.0 to -0.30 |
| U.S. Stocks vs. Long-Term Treasuries | -0.20 to -0.40 |
| U.S. Stocks vs. Gold | -0.05 to 0.10 |
| U.S. Stocks vs. REITs | 0.55-0.70 |
| U.S. Stocks vs. Commodities | 0.15-0.35 |

The most valuable diversifiers are assets with low or negative correlation to your core holdings. For equity-heavy portfolios, bonds (especially Treasuries) and gold have historically been the most reliable diversifiers.

#### Covariance: The Building Block

While correlation gets more attention, covariance is the mathematical building block of portfolio risk calculations. Covariance measures how two assets' returns move together in absolute terms.

**The formula for covariance between assets A and B:**

Cov(A,B) = (1/n) * Sum of [(R_A,i - Mean_A) * (R_B,i - Mean_B)]

Where R_A,i and R_B,i are the returns for assets A and B in period i, and Mean_A and Mean_B are their average returns.

**Interpreting Covariance:**
- Positive covariance: Assets tend to move in the same direction.
- Negative covariance: Assets tend to move in opposite directions.
- Zero covariance: No systematic relationship.

**The relationship between covariance and correlation:**

Correlation(A,B) = Cov(A,B) / (StdDev_A * StdDev_B)

Correlation is simply covariance normalized by the standard deviations (volatilities) of both assets. This normalization is why correlation is bounded between -1 and +1, making it easier to interpret than raw covariance values.

#### Portfolio Variance: The Key Formula

The variance (and therefore the volatility) of a two-asset portfolio is where the diversification benefit becomes concrete.

**Two-Asset Portfolio Variance Formula:**

Var(P) = w_A^2 * Var(A) + w_B^2 * Var(B) + 2 * w_A * w_B * Cov(A,B)

Where:
- w_A and w_B are the portfolio weights of assets A and B.
- Var(A) and Var(B) are the variances of assets A and B.
- Cov(A,B) is the covariance between A and B.

Or equivalently, using correlation:

Var(P) = w_A^2 * sigma_A^2 + w_B^2 * sigma_B^2 + 2 * w_A * w_B * sigma_A * sigma_B * rho(A,B)

Where sigma_A and sigma_B are the standard deviations and rho(A,B) is the correlation.

**The portfolio's standard deviation (volatility)** is the square root of the variance.

**A Concrete Example:**

Suppose you have two assets:
- Asset A: Expected return 10%, volatility 15%.
- Asset B: Expected return 8%, volatility 12%.
- Correlation between A and B: 0.3.

For a 60/40 portfolio (60% A, 40% B):

Var(P) = (0.6)^2 * (0.15)^2 + (0.4)^2 * (0.12)^2 + 2 * 0.6 * 0.4 * 0.15 * 0.12 * 0.3

Var(P) = 0.36 * 0.0225 + 0.16 * 0.0144 + 2 * 0.6 * 0.4 * 0.15 * 0.12 * 0.3

Var(P) = 0.0081 + 0.002304 + 0.002592

Var(P) = 0.012996

Portfolio Volatility = sqrt(0.012996) = 0.114 = 11.4%

Notice: The portfolio volatility (11.4%) is lower than either asset's individual volatility (15% and 12%). This is the power of diversification -- by combining two imperfectly correlated assets, the portfolio achieves lower risk than either component alone.

If the correlation were 1.0 (perfect positive correlation), the portfolio volatility would be:
0.6 * 15% + 0.4 * 12% = 13.8% -- a simple weighted average with no diversification benefit.

If the correlation were 0 (uncorrelated), the portfolio volatility would be:
sqrt(0.0081 + 0.002304) = sqrt(0.010404) = 10.2% -- even lower.

If the correlation were -1.0 (perfect negative correlation), you could theoretically achieve zero volatility with the right weights.

#### The Covariance Matrix

For portfolios with more than two assets, the math extends using a covariance matrix. For n assets, the covariance matrix is an n-by-n table where each cell contains the covariance between two assets (and the diagonal contains each asset's variance).

For a three-asset portfolio with assets A, B, and C:

|  | A | B | C |
|--|--|--|--|
| A | Var(A) | Cov(A,B) | Cov(A,C) |
| B | Cov(B,A) | Var(B) | Cov(B,C) |
| C | Cov(C,A) | Cov(C,B) | Var(C) |

The portfolio variance is:

Var(P) = Sum over all i,j of: w_i * w_j * Cov(i,j)

As the number of assets grows, the number of covariance terms grows quadratically (n^2 terms for n assets). In a 10-asset portfolio, there are 45 unique covariance pairs. In a 100-asset portfolio, there are 4,950. This is why institutional portfolio managers rely on software and simplified models (factor models) to estimate covariance matrices rather than calculating every pair individually.

#### The Efficient Frontier

Harry Markowitz's 1952 paper "Portfolio Selection" introduced the concept of the efficient frontier -- the set of portfolios that offer the highest expected return for each level of risk (standard deviation).

**Key Insights from the Efficient Frontier:**

- **No Rational Investor Should Hold an Inefficient Portfolio.** For any portfolio below the efficient frontier, there exists another portfolio with the same risk but higher return (or the same return but lower risk). The efficient frontier represents the best achievable trade-offs.

- **Diversification Creates the Frontier.** Without the ability to combine assets, investors would simply choose individual assets based on their risk-return characteristics. The efficient frontier exists because combining imperfectly correlated assets creates portfolios with risk-return profiles superior to any individual asset.

- **The Minimum Variance Portfolio.** The leftmost point on the efficient frontier is the portfolio with the lowest possible volatility. This portfolio often has counterintuitive weights because it maximizes the diversification benefit by heavily weighting low-correlation assets.

- **Adding the Risk-Free Asset.** When a risk-free asset (like Treasury bills) is available, the optimal portfolio lies on the Capital Market Line -- a straight line from the risk-free rate to the tangent point on the efficient frontier. This tangent portfolio is the "optimal risky portfolio," and all investors should hold some combination of this portfolio and the risk-free asset, varying only the proportions based on their risk tolerance.

#### Correlation Breakdown in Crises

Perhaps the most important practical lesson from portfolio mathematics is that historical correlations can be misleading, particularly during market crises.

**What Happens During Crises:**

During severe market stress, correlations between risky assets tend to increase sharply. Assets that had moderate correlations during normal times suddenly move in lockstep during crashes. This phenomenon has been documented in every major market crisis:

- During the 2008 financial crisis, correlations between U.S. stocks, international stocks, REITs, and corporate bonds all spiked toward 1.0. Assets that investors believed provided diversification offered far less protection than expected.

- During the COVID-19 crash in March 2020, even gold initially declined alongside stocks as investors sold everything to raise cash.

**Why Correlation Breakdown Occurs:**

- **Contagion.** Financial institutions hold diverse portfolios. When they face losses in one area, they sell assets across all areas to raise cash, creating correlated selling pressure.

- **Leverage Unwinds.** Leveraged investors facing margin calls must sell whatever they can, regardless of fundamentals, pushing all liquid assets down simultaneously.

- **Risk-Off Behavior.** During crises, investors' appetite for risk decreases across the board. They flee all risky assets simultaneously, driving correlations toward 1.0.

- **Funding Liquidity.** When credit markets freeze, all assets that depend on financing become correlated through the common channel of funding availability.

**Implications for Portfolio Construction:**

- Do not rely solely on normal-period correlations for risk management. Stress-test your portfolio using crisis-period correlations.
- Assets that maintain low or negative correlation during crises -- primarily high-quality government bonds and cash -- provide the most reliable diversification when it is needed most.
- Diversification helps in moderate downturns but provides less protection in extreme crises. Position sizing and overall risk budgeting are essential complements to diversification.
- Consider tail-risk hedging (such as put options or managed futures) as additional protection for scenarios where traditional diversification breaks down.

---

### c) Common Misconceptions

**"A correlation of 0.7 means the assets move together 70% of the time."** Correlation does not measure the percentage of time assets move in the same direction. A correlation of 0.7 means that 49% (0.7^2 = 0.49) of the variance in one asset's returns is explained by the other asset's returns. Two assets with a correlation of 0.7 can still move in opposite directions on many individual days.

**"Adding more assets always improves diversification."** Adding a 50th stock to a portfolio of 49 stocks provides almost no marginal diversification benefit if all 50 stocks are highly correlated. The quality of diversification (low correlation between components) matters more than the quantity of holdings.

**"Historical correlation predicts future correlation."** While correlations tend to be somewhat persistent, they change over time and can shift dramatically during crises. A correlation estimated from the past five years of calm markets may be a poor predictor of behavior during the next crash.

**"You need to calculate these formulas manually."** While understanding the math is important for building intuition, modern portfolio tools (Portfolio Visualizer, Excel, Python) handle the calculations. Your job is to understand what the inputs mean and how changes in correlation affect your portfolio's risk profile.

**"Negative correlation means an asset always goes up when stocks go down."** Even Treasuries, which have had negative correlation with stocks over recent decades, do not always rise when stocks fall. The negative correlation describes a tendency over many periods, not a guarantee in any single period. In 2022, both stocks and bonds declined significantly -- a painful reminder.

---

### d) Q&A

**Q: How do I calculate the correlation between two assets?**
A: You need a time series of returns for both assets (daily, weekly, or monthly). In Excel, use the CORREL function on the two return series. In Google Sheets, the same CORREL function works. Portfolio Visualizer and other online tools calculate correlations automatically when you input tickers. Use at least three to five years of data for stable estimates, and be aware that the time period you choose can significantly affect the result.

**Q: What is the optimal correlation for a portfolio diversifier?**
A: The lower (or more negative) the correlation with your core holdings, the better the diversification benefit. For equity portfolios, the ideal diversifier has a correlation near zero or negative with stocks, while still providing a positive expected return. Long-term Treasury bonds (correlation typically -0.2 to -0.4 with stocks) and gold (correlation near zero) are the most commonly used diversifiers. An asset with perfect negative correlation would be ideal mathematically but does not exist in practice among real investable assets.

**Q: Does diversification eliminate risk?**
A: Diversification eliminates idiosyncratic (company-specific) risk but not systematic (market-wide) risk. Even a perfectly diversified portfolio is exposed to recessions, interest rate changes, pandemics, and other events that affect all assets. Academic research suggests that most idiosyncratic risk can be eliminated with as few as 20-30 well-chosen, lowly correlated stocks, but systematic risk -- also called market risk -- cannot be diversified away.

**Q: Why did the 60/40 portfolio fail in 2022?**
A: The 60/40 portfolio (60% stocks, 40% bonds) depends on negative or low correlation between stocks and bonds. In 2022, both stocks and bonds declined because the Fed was raising interest rates aggressively to fight inflation. Rising rates are bad for both bond prices (directly) and stock valuations (by reducing the present value of future cash flows). The negative stock-bond correlation that prevailed from roughly 2000 to 2021 was not a law of nature -- it was driven by a specific macroeconomic environment of low and falling inflation. When the inflation regime changed, the correlation changed with it.

**Q: How can I stress-test my portfolio for correlation breakdown?**
A: Use the correlation matrix from a specific crisis period (2008, 2020) rather than a long-term average. Portfolio Visualizer allows you to set custom date ranges for correlation calculations. Alternatively, assume all equity-like assets have a correlation of 0.9 with each other during a crisis and see how your portfolio performs. If your portfolio cannot survive a scenario where all risky assets fall together, you may need more allocation to truly uncorrelated assets like Treasury bonds and cash.

**Q: What is the role of covariance in factor models?**
A: Factor models (like the Fama-French model) simplify the covariance estimation problem by assuming that the correlations between stocks are driven by common factors (market, size, value, etc.). Instead of estimating thousands of individual covariance pairs, you estimate each stock's exposure (beta) to a small number of factors and use the factor covariance matrix. This dramatically reduces estimation error and is the standard approach in institutional portfolio management.

---

## YouTube Script

[INTRO - 0:00]

[VISUAL: Two bouncing balls on screen, one representing Stock A and one representing Stock B, moving independently]

**Alex:** We have talked a lot about diversification in this series. Do not put all your eggs in one basket, spread your risk across different assets, blah blah blah. But have you ever wondered WHY diversification actually works? What is the math behind it?

**Sam:** Today we are going under the hood. We are going to look at the actual mathematics that makes diversification one of the most powerful concepts in investing. And I promise -- it is more intuitive than you think.

[VISUAL: Title card "The Math of Diversification: Correlation, Covariance, and Portfolio Risk"]

---

[SECTION 1 - WHAT IS CORRELATION - 1:30]

[ANIMATION: Two stock charts side by side. First showing them moving in perfect lockstep (correlation +1), then independently (correlation 0), then in opposite directions (correlation -1)]

**Alex:** Let us start with correlation. It is a number between negative one and positive one that tells you how much two investments tend to move together.

**Sam:** If two stocks have a correlation of positive one, they move in perfect lockstep. When one goes up 2 percent, the other goes up 2 percent. There is zero diversification benefit from holding both -- they behave like the same investment.

**Alex:** If the correlation is zero, the stocks move completely independently. One might go up while the other goes down, or both might go up, or both might go down. There is no consistent relationship.

[VISUAL: Scatter plots showing return pairs for different correlation levels: +1.0, +0.5, 0, -0.5, -1.0]

**Sam:** And if the correlation is negative one -- perfect negative correlation -- they always move in exactly opposite directions. If you could find two investments with correlation of negative one, you could theoretically build a portfolio with zero risk. But in the real world, nothing has perfect negative correlation.

**Alex:** Most stock pairs have correlations between 0.5 and 0.9. Stocks and bonds have correlations that typically range from 0 to negative 0.3. Gold has near-zero correlation with stocks. The lower the correlation between your portfolio components, the more diversification benefit you get.

---

[SECTION 2 - THE MAGIC OF PORTFOLIO MATH - 3:30]

[ANIMATION: Building blocks showing how two volatile assets can combine into a less volatile portfolio]

**Sam:** Here is where it gets really interesting. Let us say you have two investments. Stock A has 15 percent volatility. Stock B has 12 percent volatility. Their correlation is 0.3.

**Alex:** If you put 60 percent in A and 40 percent in B, what is the portfolio's volatility? If you just take a weighted average, you would expect about 13.8 percent.

[VISUAL: Calculation showing weighted average: 0.6 * 15% + 0.4 * 12% = 13.8%]

**Sam:** But the actual portfolio volatility is only 11.4 percent. That is lower than EITHER individual investment. You combined two risky things and got something less risky than both. That is the magic of diversification.

[ANIMATION: Visual showing 15% and 12% combining to create 11.4%, with "Diversification Benefit" labeled as the difference]

**Alex:** The reason is that third term in the portfolio variance formula -- the covariance term. When the correlation is less than one, that term reduces the total portfolio variance. The lower the correlation, the bigger the reduction.

**Sam:** Let me put it simply. When Stock A has a bad day but Stock B does not -- because they are not perfectly correlated -- the loss in A is partially offset by B holding steady or even going up. That offsetting effect is what reduces portfolio risk below the weighted average.

[VISUAL: Daily returns calendar showing days where A is down but B is up, partially offsetting each other]

---

[SECTION 3 - THE EFFICIENT FRONTIER - 6:00]

[ANIMATION: Graph with Risk (x-axis) and Return (y-axis). Individual assets plotted as dots. Curved line (efficient frontier) appearing above and to the left of most dots]

**Alex:** In 1952, a graduate student named Harry Markowitz published a paper that would eventually win him the Nobel Prize. He showed that by combining assets with different correlations, you can trace out what he called the "efficient frontier."

**Sam:** The efficient frontier is the set of portfolios that give you the highest possible return for each level of risk. Every point on this curve is optimal -- you cannot get more return without taking more risk, and you cannot reduce risk without giving up some return.

[ANIMATION: Arrow showing that portfolios below the frontier are "inefficient" -- same risk but lower return, or same return but higher risk]

**Alex:** Any portfolio that falls below the efficient frontier is inefficient. There exists a better portfolio -- one with the same risk but higher return, or the same return but less risk. The math proves it.

**Sam:** And here is the key insight: individual assets almost never sit on the efficient frontier. It is only by combining assets that you can reach the frontier. This is the mathematical proof that diversification works -- it literally creates better risk-return combinations than any individual investment.

[VISUAL: Animated GIF showing how adding a low-correlation asset to a portfolio shifts the frontier up and to the left]

**Alex:** When you add an asset with low correlation to your portfolio, the efficient frontier shifts up and to the left -- meaning you get more return for the same risk or less risk for the same return. This is why financial advisors emphasize diversification so strongly. The math demands it.

---

[SECTION 4 - WHEN DIVERSIFICATION FAILS - 8:30]

[VISUAL: Correlation matrix that starts with normal values, then shifts to all-high values during a crisis, visualized with color coding]

**Sam:** Now for the uncomfortable truth. Everything we just discussed works beautifully during normal times. But during market crises, correlations change. And they change in the worst possible direction.

**Alex:** During the 2008 financial crisis, correlations between stocks, international stocks, REITs, corporate bonds, and commodities all spiked toward one. Assets that were supposed to diversify your portfolio suddenly all fell together.

[ANIMATION: Network diagram showing assets with moderate connections during normal times, then connections all turning red and thickening during a crisis]

**Sam:** This is what people call correlation breakdown, though it is really correlation convergence. In a crisis, everything becomes correlated because of contagion, leverage unwinds, and panicked selling across all asset classes.

**Alex:** Even gold, which normally has near-zero correlation with stocks, briefly declined alongside stocks during the worst days of the March 2020 crash, as investors sold everything to raise cash.

[VISUAL: Chart showing gold declining alongside stocks in mid-March 2020 before recovering and rising]

**Sam:** So what actually works as a diversifier during crises? Historically, two things have been most reliable: high-quality government bonds -- especially long-term Treasuries -- and cash. These maintained their negative or low correlation with stocks even during severe stress.

**Alex:** The 2022 experience was a notable exception. Both stocks and bonds fell because rising interest rates and inflation hit both asset classes simultaneously. This shows that even the stock-bond negative correlation is not guaranteed -- it depends on the macroeconomic regime.

---

[SECTION 5 - PRACTICAL APPLICATIONS - 11:00]

[VISUAL: "Building Your Portfolio: Correlation in Practice" header]

**Sam:** Let us bring this back to practical portfolio construction. Here are the key takeaways.

**Alex:** First, when evaluating whether to add an asset to your portfolio, check its correlation with your existing holdings. An asset with high expected returns but a correlation of 0.95 with what you already own adds almost no diversification value. An asset with moderate returns but a correlation of 0.2 might actually improve your portfolio's risk-adjusted returns dramatically.

[VISUAL: Before/after portfolio comparison showing how adding a low-correlation asset improves the efficient frontier position]

**Sam:** Second, do not confuse the number of holdings with diversification quality. Owning 100 U.S. large-cap stocks gives you roughly the same diversification as owning 30, because they are all highly correlated with each other. True diversification comes from combining asset classes with genuinely different return drivers -- stocks, bonds, real estate, commodities, international equities.

**Alex:** Third, stress-test your portfolio. Do not just look at average correlations. Look at crisis-period correlations. How would your portfolio have performed in 2008 or 2020 if correlations spiked to 0.9 among all your equity holdings?

[VISUAL: Side-by-side portfolio performance: "Normal Correlations" vs "Crisis Correlations" showing the difference]

**Sam:** Fourth, keep some assets that historically maintain their diversification benefit during crises. Treasury bonds and cash are boring, but they are the most reliable portfolio insurance available.

**Alex:** And fifth, remember that the math is a framework, not a crystal ball. Correlations change, expected returns are uncertain, and no model perfectly predicts the future. Use the math to build better portfolios, but maintain humility about its limitations.

[VISUAL: End card with channel logo and "Next: Options Greeks Deep Dive"]

**Sam:** In our next lesson, we are diving deep into the world of options Greeks -- gamma, rho, and the second-order sensitivities that separate beginners from advanced options traders. See you there.

[END - 13:30]
