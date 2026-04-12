<!-- 此檔案需要翻譯為台灣繁體中文 -->
<!-- This file needs translation to TW Traditional Chinese -->

# Week 15: Multi-Asset Allocation

---

## Reading Section

### a) Why This Is Important

Most beginning investors think of investing as choosing between stocks and bonds. This two-asset mental model is dangerously incomplete. The investment universe is vast -- it includes real estate, commodities, private equity, infrastructure, hedge fund strategies, and more. Each asset class has its own return profile, risk characteristics, and sensitivity to economic conditions. By limiting yourself to two ingredients, you are cooking with one hand tied behind your back.

Multi-asset allocation matters for three fundamental reasons:

1. **Diversification is the only free lunch in finance.** Nobel laureate Harry Markowitz said this, and decades of evidence support it. By combining assets that do not move in lockstep, you can earn higher returns per unit of risk than any single asset can deliver alone. A portfolio of five uncorrelated return streams is categorically different from a portfolio of one.

2. **The 60/40 portfolio is not a law of nature.** The traditional 60% stocks / 40% bonds split served investors well for decades, but it was a product of a specific interest rate environment. When rates were high and falling, bonds provided both income and diversification. In a low-rate or rising-rate world, the 60/40 portfolio may not work as advertised. You need alternatives.

3. **Asset allocation drives the vast majority of portfolio returns.** Landmark studies by Brinson, Hood, and Beebower found that over 90% of the variation in portfolio returns over time is explained by the asset allocation decision -- not stock picking, not market timing. Getting the big picture right matters more than getting any single holding right.

4. **Different assets protect you in different environments.** Stocks do well during economic growth. Bonds do well when growth slows and rates fall. Commodities do well during inflation. Real estate provides income and inflation protection. Gold protects against extreme uncertainty. No single asset handles every scenario. A multi-asset portfolio gives you coverage across multiple economic regimes.

5. **Institutional investors already know this.** Endowments like Yale and Harvard, sovereign wealth funds, and pension funds have long used multi-asset approaches. David Swensen's Yale Model famously emphasized alternative assets and earned extraordinary risk-adjusted returns over decades. Individual investors can apply the same principles on a smaller scale using ETFs and low-cost funds.

This lesson will teach you the major asset classes, how they interact through correlation, how to build an efficient portfolio using modern portfolio theory, and how more advanced approaches like risk parity attempt to improve on traditional allocation methods.

---

### b) What You Need to Know

#### 1. The Major Asset Classes

An asset class is a broad category of investments that share similar characteristics, behave similarly in the market, and are subject to the same laws and regulations. Here are the primary asset classes available to individual investors:

**Equities (Stocks)**
- Ownership stakes in companies
- Highest long-term expected returns (~7-10% real historically)
- Highest volatility (~15-20% annual standard deviation)
- Sensitive to economic growth and corporate earnings
- Sub-categories: domestic large-cap, small-cap, international developed, emerging markets

**Fixed Income (Bonds)**
- Loans to governments or corporations
- Lower expected returns (~1-4% real historically)
- Lower volatility (~4-8% annual standard deviation)
- Sensitive to interest rates and inflation expectations
- Sub-categories: government, investment-grade corporate, high-yield, TIPS, international

**Real Estate (REITs)**
- Ownership of physical property or property-related securities
- Returns between stocks and bonds (~5-7% real historically)
- Moderate volatility
- Provides income through rents and inflation protection
- Accessible through publicly traded REITs and REIT ETFs

**Commodities**
- Physical goods: energy, metals, agriculture
- Low long-term real returns (~0-2%) but valuable diversifier
- High volatility, low correlation with stocks and bonds
- Strong inflation hedge
- Accessible through commodity futures ETFs and commodity-producing company stocks

**Gold and Precious Metals**
- Store of value for thousands of years
- Low long-term real returns (~0-1%)
- Valuable as a crisis hedge and inflation hedge
- Tends to do well when confidence in governments and currencies declines
- Accessible through gold ETFs (GLD, IAU) and mining stocks

**Cash and Cash Equivalents**
- Treasury bills, money market funds, savings accounts
- Lowest returns but zero volatility in nominal terms
- Provides optionality -- the ability to buy assets during crashes
- Often overlooked as a strategic allocation

```
ASSET CLASS RISK-RETURN SPECTRUM
================================

Expected                                              Emerging
Real Return                                           Markets
(%)                                                     *
  10 |                                               *
     |                                          Small-Cap
   8 |                                        *
     |                                  Large-Cap US
   6 |                                *
     |                          REITs
   5 |                        *
     |                  Corp Bonds
   4 |                *
     |          Gov Bonds
   3 |        *
     |    TIPS
   2 |  *
     | * Gold
   1 |* Commodities
     |
   0 +--*--+-----+-----+-----+-----+-----+-----+---
     Cash  5    10    15    20    25    30    35
                Volatility (Std Dev %)

Higher return generally requires accepting higher risk.
Multi-asset allocation tries to find the best trade-off.
```

---

#### 2. Correlation -- The Key to Diversification

The power of multi-asset investing comes not from individual asset class returns but from how assets move relative to each other. Correlation measures this co-movement on a scale from -1 to +1.

- **Correlation = +1.0:** Assets move in perfect lockstep. No diversification benefit.
- **Correlation = 0.0:** Assets move independently. Good diversification.
- **Correlation = -1.0:** Assets move in opposite directions. Maximum diversification.

The lower the correlation between two assets, the more they reduce each other's risk when combined. Even a correlation of +0.3 provides meaningful diversification -- the assets are related but far from identical.

```
CORRELATION MATRIX (APPROXIMATE HISTORICAL VALUES)
====================================================

              US      Intl    EM     US     Corp   Commod  Gold   REITs
             Stocks  Stocks  Stocks  Bonds  Bonds  -ities
US Stocks    1.00
Intl Stocks  0.75    1.00
EM Stocks    0.65    0.70    1.00
US Bonds    -0.10    0.00    0.05   1.00
Corp Bonds   0.25    0.15    0.20   0.75   1.00
Commodities  0.15    0.20    0.30  -0.10   0.00   1.00
Gold        -0.05    0.05    0.05   0.30   0.10   0.25   1.00
REITs        0.55    0.40    0.40   0.15   0.25   0.10   0.05   1.00

Key insights from this matrix:
- US and Intl stocks are highly correlated (0.75) -- limited diversification
- US Bonds are negatively correlated with stocks -- strong diversifier
- Commodities have low correlation with almost everything -- valuable addition
- Gold is near-zero with stocks -- crisis hedge
- REITs are moderately correlated with stocks -- some diversification
```

**Critical warning: correlations are not constant.** During market crises, correlations tend to spike. Assets that seemed uncorrelated during calm periods may suddenly move together during a panic. This is called "correlation breakdown" and it is one of the biggest risks in portfolio construction. The 2008 financial crisis demonstrated this vividly -- almost everything except Treasury bonds and gold fell together.

```
CORRELATION BEHAVIOR DURING STRESS
====================================

Normal Markets:              Crisis Markets:
                              (Correlations Spike)

  Stock A     Bond            Stock A     Bond
    \        /                  \          |
     \      /                    \         |  (still some
      \    /                      \        |   diversification)
       \/                          \       |
    Low/Negative                    --------
    Correlation                     Moderate
                                    Correlation

  Stock A     Gold            Stock A     Gold
    \        /                  |         /
     \      /  Near-zero        |        /  Negative
      \    /   Correlation      |       /   (Gold rises
       \/                       |      /    when stocks crash)
                                ------

Lesson: Build portfolios for the storm, not just fair weather.
```

---

#### 3. Modern Portfolio Theory and the Efficient Frontier

In 1952, Harry Markowitz published a paper that would earn him a Nobel Prize. The core insight was revolutionary in its simplicity: investors should not evaluate assets in isolation. What matters is how each asset contributes to the overall portfolio's risk and return.

**The key idea:** For any given level of risk, there exists an optimal combination of assets that maximizes expected return. The set of all such optimal portfolios forms a curve called the efficient frontier.

```
THE EFFICIENT FRONTIER
=======================

Expected
Return (%)
    |                                          * Aggressive
    |                                       *    (90/10 stocks/bonds)
 12 |                                    *
    |                                 *
 10 |                              *   <-- EFFICIENT FRONTIER
    |                           *        (Best risk/return trade-off)
  8 |                        *
    |                    *  * Balanced (60/40)
  6 |                 *
    |              *
  5 |           * Conservative (30/70)
    |        *
  4 |     *
    |  * 100% Bonds
  3 |*
    |
  2 |
    +----+----+----+----+----+----+----+----+----+---
    0    2    4    6    8   10   12   14   16   18
              Portfolio Risk (Std Dev %)

          x                      x
          Portfolios below       Individual assets
          the frontier are       typically fall below
          INEFFICIENT            the frontier

Any portfolio BELOW the curve is sub-optimal: you could earn more
return for the same risk, or take less risk for the same return,
by moving to the frontier.
```

**How to read the efficient frontier:**

1. Every point ON the curve represents the best possible portfolio for that level of risk
2. Points BELOW the curve are inefficient -- they take on unnecessary risk for their return level
3. There is no way to get ABOVE the curve without adding leverage or finding a new asset class
4. Moving along the curve represents the trade-off between risk and return
5. The leftmost point is the minimum variance portfolio -- lowest possible risk

**Building a portfolio on the efficient frontier requires three inputs:**

1. Expected returns for each asset class
2. Expected volatility (standard deviation) for each asset class
3. Expected correlations between all pairs of asset classes

The mathematics of portfolio optimization then finds the weights that maximize return for each level of risk. The formula for a two-asset portfolio's risk illustrates why diversification works:

```
PORTFOLIO RISK FORMULA (TWO ASSETS)
====================================

Portfolio_Variance = w1^2 * var1 + w2^2 * var2 + 2 * w1 * w2 * cov(1,2)

Where:
  w1, w2     = portfolio weights (must sum to 1.0)
  var1, var2 = variance of each asset
  cov(1,2)   = covariance = correlation * stddev1 * stddev2

EXAMPLE:
  Asset A: weight = 60%, stddev = 15%
  Asset B: weight = 40%, stddev = 5%
  Correlation = -0.10

  Portfolio Variance = (0.60)^2 * (0.15)^2
                     + (0.40)^2 * (0.05)^2
                     + 2 * (0.60) * (0.40) * (-0.10) * (0.15) * (0.05)

                     = 0.0081 + 0.0004 + (-0.00036)

                     = 0.00814

  Portfolio StdDev   = sqrt(0.00814) = 9.02%

Notice: 60% in a 15% volatility asset and 40% in a 5% volatility asset
gives a portfolio with only 9.02% volatility -- LESS than the weighted
average of 11% (0.60*15 + 0.40*5). This is diversification at work!
The negative correlation term SUBTRACTS from total risk.
```

---

#### 4. Beyond Mean-Variance: Risk Parity

Modern Portfolio Theory has a well-known weakness: it is extremely sensitive to the inputs. Small changes in expected returns can produce wildly different portfolio allocations. And estimating expected returns is very difficult.

Risk parity takes a different approach. Instead of optimizing for returns, it focuses entirely on risk. The idea: equalize the risk contribution from each asset class so that no single asset dominates the portfolio's risk profile.

**The problem with 60/40:**

```
60/40 PORTFOLIO: RISK CONTRIBUTION ANALYSIS
=============================================

               Allocation    Risk Contribution
               (by weight)   (by variance)
              +-----------+  +-----------------+
  Stocks      |           |  |                              |
  60%         |   60%     |  |         ~90%                 |
              |           |  |                              |
              +-----------+  +-----------------+
  Bonds       |           |  |    |
  40%         |   40%     |  |~10%|
              +-----------+  +----+

Despite being 40% of the portfolio by weight, bonds contribute
only ~10% of the portfolio's risk. The portfolio is essentially
a leveraged bet on stocks.

When stocks crash, the 60/40 portfolio crashes too -- the bonds
barely cushion the blow because their risk contribution is tiny.
```

**Risk parity solution:** Allocate so that each asset class contributes equally to portfolio risk. Since bonds are less volatile than stocks, this means holding more bonds (and often using leverage to achieve competitive returns).

```
RISK PARITY PORTFOLIO CONCEPT
==============================

Traditional 60/40:              Risk Parity:

Weight:  Risk:                  Weight:      Risk:
+------+--------+              +-----------+------+
|Stock | Stock  |              |   Bonds   |Bond  |
| 60%  |  90%   |              |   ~55%    | ~33% |
+------+--------+              +-----------+------+
|Bond  |Bond    |              |Stock ~25% |Stock |
| 40%  | 10%    |              |           | ~33% |
+------+--------+              +-----+-----+------+
                               |Commod ~20%|Commod|
                               |           | ~33% |
                               +-----------+------+

Risk parity allocates MORE to low-vol assets (bonds)
and LESS to high-vol assets (stocks), then may use
leverage to scale up the total return.

Result: each asset class contributes ~33% of risk,
so no single asset class can dominate portfolio losses.
```

**Advantages of risk parity:**
- More balanced risk exposure across economic environments
- Less sensitive to expected return estimates
- Performed well historically during both growth and recession
- Used by major hedge funds (Bridgewater's All Weather fund)

**Disadvantages of risk parity:**
- Often requires leverage to achieve target returns
- Heavy bond allocation can suffer in rising rate environments
- Leverage introduces its own risks and costs
- More complex to implement than traditional allocation

---

#### 5. Sample Multi-Asset Portfolios

Here are several well-known multi-asset portfolio templates, ranging from simple to sophisticated:

```
SAMPLE MULTI-ASSET PORTFOLIOS
==============================

1. THREE-FUND PORTFOLIO (Bogle/Boglehead Classic)
   Simple, effective, low-cost
   +------------------------------------------+
   | US Total Stock Market          |   50%    |
   | International Stock Market     |   30%    |
   | US Total Bond Market           |   20%    |
   +------------------------------------------+
   Total: 100%   Expense ratio: ~0.03-0.05%

2. FOUR-FUND WITH REAL ASSETS
   Adds inflation protection
   +------------------------------------------+
   | US Total Stock Market          |   40%    |
   | International Stocks           |   20%    |
   | US Total Bond Market           |   25%    |
   | REITs                          |   15%    |
   +------------------------------------------+
   Total: 100%   Expense ratio: ~0.05-0.08%

3. ALL-WEATHER INSPIRED (Simplified Ray Dalio)
   Designed for all economic environments
   +------------------------------------------+
   | US Stocks                      |   30%    |
   | Long-Term Treasury Bonds       |   40%    |
   | Intermediate Treasury Bonds    |   15%    |
   | Gold                           |    7.5%  |
   | Commodities                    |    7.5%  |
   +------------------------------------------+
   Total: 100%   Expense ratio: ~0.10-0.20%

4. YALE ENDOWMENT INSPIRED (Simplified Swensen)
   Emphasizes alternatives and diversification
   +------------------------------------------+
   | US Stocks                      |   30%    |
   | International Developed        |   15%    |
   | Emerging Markets               |   10%    |
   | REITs                          |   15%    |
   | TIPS (Inflation-Protected)     |   15%    |
   | Nominal Bonds                  |   15%    |
   +------------------------------------------+
   Total: 100%   Expense ratio: ~0.08-0.15%

5. RISK PARITY LITE (No Leverage)
   Equal risk contribution without leverage
   +------------------------------------------+
   | US Stocks                      |   20%    |
   | International Stocks           |   10%    |
   | Long-Term Treasuries           |   30%    |
   | TIPS                           |   15%    |
   | Gold                           |   10%    |
   | Commodities                    |   10%    |
   | REITs                          |    5%    |
   +------------------------------------------+
   Total: 100%   Expense ratio: ~0.10-0.20%
```

```
ECONOMIC REGIME COVERAGE MAP
==============================

Economic        | Growth | Growth | Recession | Recession
Environment:    | + Low  | + High | + Low     | + High
                | Inflat | Inflat | Inflation | Inflation
                | (Boom) |(Overheat)|(Deflation)|(Stagflat)
----------------+--------+--------+-----------+----------
Stocks          |  +++   |   +    |   ---     |   --
Bonds           |   +    |   --   |   +++     |   --
Commodities     |   +    |  +++   |    -      |   ++
Gold            |   -    |   ++   |    +      |  +++
REITs           |  +++   |   +    |   --      |    -
TIPS            |   +    |   ++   |    +      |   ++
Cash            |   -    |    -   |    +      |    +
----------------+--------+--------+-----------+----------

+++ = strong performance    + = modest positive
 -  = modest negative     --- = poor performance

A multi-asset portfolio has SOME assets performing well
in EVERY economic environment. That is the whole point.
```

---

#### 6. Rebalancing a Multi-Asset Portfolio

Once you have set your target allocation, markets will move your actual weights away from those targets. Rebalancing is the process of bringing your portfolio back to its target weights.

**Calendar rebalancing:** Check and rebalance at fixed intervals (quarterly, semi-annually, annually). Simple to implement but may rebalance unnecessarily or too late.

**Threshold rebalancing:** Rebalance whenever any asset class drifts more than a set amount (e.g., 5 percentage points) from its target. More responsive but requires monitoring.

**Cost-aware rebalancing:** Factor in transaction costs and tax implications. Use new contributions to buy underweight assets rather than selling overweight ones. Direct dividends to underweight positions.

```
REBALANCING ILLUSTRATION
=========================

Target Allocation:           After Market Movement:
US Stocks   40%              US Stocks   48%  (+8)  --> SELL
Intl Stocks 20%              Intl Stocks 17%  (-3)  --> BUY
Bonds       25%              Bonds       22%  (-3)  --> BUY
Gold        10%              Gold         8%  (-2)  --> BUY
REITs        5%              REITs        5%  ( 0)  --> HOLD

Rebalancing means selling winners and buying losers.
This feels counterintuitive but it enforces "buy low, sell high."

Rebalancing bonus: historically adds 0.3-0.5% per year in return
through this systematic contrarian behavior.
```

---

#### 7. Implementation with ETFs

The practical beauty of multi-asset investing is that you can implement sophisticated institutional-quality portfolios using low-cost ETFs. Here is a reference table:

```
ASSET CLASS TO ETF MAPPING
============================

Asset Class              | Popular ETFs      | Expense Ratio
-------------------------+-------------------+--------------
US Total Stock Market    | VTI, ITOT, SPTM   | 0.03%
US Large-Cap             | VOO, IVV, SPY     | 0.03-0.09%
US Small-Cap             | VB, IJR, SCHA     | 0.04-0.06%
International Developed  | VXUS, IXUS, EFA   | 0.05-0.07%
Emerging Markets         | VWO, IEMG, EEM    | 0.08-0.11%
US Total Bond Market     | BND, AGG, SCHZ    | 0.03-0.04%
Long-Term Treasuries     | TLT, VGLT, SPTL   | 0.04-0.06%
TIPS                     | TIP, SCHP, VTIP   | 0.03-0.05%
Corporate Bonds          | LQD, VCIT, IGIB   | 0.04-0.06%
REITs                    | VNQ, SCHH, IYR    | 0.07-0.12%
Gold                     | GLD, IAU, GLDM    | 0.10-0.40%
Broad Commodities        | DJP, GSG, PDBC    | 0.45-0.75%
```

---

### c) Common Misconceptions

**Misconception 1: "More asset classes always means better diversification."**

Not true. Adding a tenth asset class that is 90% correlated with assets already in your portfolio adds complexity without meaningful diversification. What matters is the correlation structure, not the number of line items. A five-asset portfolio with low correlations can be far better diversified than a ten-asset portfolio with high cross-correlations.

**Misconception 2: "International stocks provide significant diversification from US stocks."**

Less true than it used to be. Globalization has increased correlations among developed equity markets. US and international developed stocks now have a correlation of roughly 0.75 to 0.85, which provides only modest diversification. Emerging markets and non-equity asset classes (commodities, gold, bonds) provide more meaningful diversification benefits.

**Misconception 3: "The efficient frontier tells you the optimal portfolio."**

The efficient frontier tells you the set of optimal portfolios, but only if your inputs are correct. In practice, expected returns, volatilities, and correlations are estimated with error. Small estimation errors can produce wildly different "optimal" portfolios -- a phenomenon called estimation risk. This is why many practitioners prefer simpler approaches like equal weighting or risk parity over unconstrained mean-variance optimization.

**Misconception 4: "Risk parity is always better than 60/40."**

Risk parity outperformed during the three-decade bond bull market from 1981 to 2020 because its heavy bond allocation benefited from steadily falling interest rates. In a rising rate environment, the large bond allocation becomes a liability. No allocation strategy is universally superior -- each has environments where it shines and environments where it struggles.

**Misconception 5: "Gold is a bad investment because it does not produce cash flow."**

Gold is not meant to be a return engine. It is a portfolio insurance policy. It tends to rise sharply during exactly the environments when everything else is falling -- financial crises, geopolitical turmoil, loss of confidence in fiat currencies. A small allocation (5-10%) can meaningfully reduce portfolio drawdowns without significantly dragging on long-term returns.

**Misconception 6: "I can just use a target-date fund and not worry about this."**

Target-date funds are a reasonable default, but they typically use only stocks and bonds, missing asset classes like commodities, gold, and REITs that can improve diversification. They also use a one-size-fits-all glide path that may not match your specific risk tolerance, financial situation, or views on the economy. Understanding multi-asset allocation empowers you to evaluate and improve upon these defaults.

---

### d) Questions and Answers

**Q1: How many asset classes should I include in my portfolio?**

For most individual investors, four to seven asset classes is the sweet spot. This provides meaningful diversification without excessive complexity. A core portfolio of US stocks, international stocks, bonds, and one or two real assets (REITs, gold, or commodities) captures most of the diversification benefit. Beyond seven or eight asset classes, each additional one provides diminishing marginal benefit and adds rebalancing complexity.

**Q2: How do I estimate expected returns for building an efficient frontier?**

This is the hardest part of portfolio construction. Common approaches include: (a) using long-term historical averages (simple but backward-looking), (b) using current yields and valuations as starting points (e.g., bond yield as expected bond return, earnings yield plus growth as expected stock return), (c) using the approach of building blocks -- start with risk-free rate and add risk premiums for each asset class. Approach (b) tends to produce the most reliable forward-looking estimates.

**Q3: Should I use leverage in a risk parity portfolio?**

For most individual investors, no. Leverage introduces additional risks including margin calls, borrowing costs, and the risk of forced liquidation at the worst possible time. The simplified "risk parity lite" portfolios that tilt toward bonds and include multiple asset classes can capture much of the benefit without leverage. Leave leveraged risk parity to institutional investors with stable capital bases.

**Q4: How often should I rebalance my multi-asset portfolio?**

Research suggests that annual or semi-annual rebalancing captures most of the benefit. More frequent rebalancing increases transaction costs without significantly improving risk-adjusted returns. The exception is during extreme market events -- if an asset class has moved 10+ percentage points from its target, rebalancing sooner may be warranted. Using new contributions to buy underweight assets is the most tax-efficient rebalancing method.

**Q5: Correlations seem to change over time. How do I account for that?**

Use longer historical windows (10-20 years) to estimate baseline correlations, but be aware that crises tend to increase correlations across risky assets. Build your portfolio assuming correlations will be higher than historical averages during bad times. This means holding genuinely different asset classes -- bonds, gold, commodities -- rather than relying on diversification among different types of equities, which tends to disappear when you need it most.

**Q6: What is the difference between strategic and tactical asset allocation?**

Strategic allocation sets long-term target weights based on your risk tolerance, time horizon, and return objectives. You stick to these weights through rebalancing regardless of market conditions. Tactical allocation makes short-term deviations from strategic weights based on market outlook -- for example, overweighting stocks when valuations are low or underweighting bonds when rates are about to rise. Most investors should focus on strategic allocation and leave tactical moves, if any, to small tilts rather than wholesale changes.

**Q7: Is there an easy way to tell if my portfolio is well-diversified?**

Look at the maximum drawdown during past crises. A well-diversified portfolio should have a significantly smaller drawdown than a 100% stock portfolio during events like 2008 or 2020. You can also calculate the portfolio's effective number of independent bets -- if it is close to 1, you are not diversified regardless of how many funds you own. If it is 3 or higher, you have meaningful diversification.

---

## YouTube Script

[VISUAL: Channel intro animation with upbeat music. Title card reads "Week 15: Multi-Asset Allocation -- Beyond Stocks and Bonds"]

**Alex:** Welcome back, everyone. Today we are tackling one of the most important topics in all of investing: multi-asset allocation. Sam, pop quiz. What does your portfolio look like right now?

**Sam:** Um, I have got some US stock index funds, a little international stocks, and some bonds. Basically the classic three-fund portfolio.

**Alex:** That is a great start, and honestly better than most people. But today we are going to explore why limiting yourself to just stocks and bonds is like painting with only two colors. The investment universe has a much richer palette.

[VISUAL: An artist's palette with two colors labeled "Stocks" and "Bonds" transforming into a full palette with labels for Stocks, Bonds, REITs, Commodities, Gold, TIPS, and Alternatives]

**Sam:** Okay, but I have heard that keeping things simple is the best approach. Why complicate things?

**Alex:** Simplicity is great, but there is a difference between simplicity and incompleteness. Harry Markowitz -- the father of modern portfolio theory -- said that diversification is the only free lunch in finance. And you cannot get a truly diversified meal with just two ingredients.

**Sam:** Free lunch? In finance? That sounds suspicious.

**Alex:** I know, right? But the math backs it up. When you combine assets that do not move in lockstep, the portfolio's risk decreases without a proportional decrease in return. You literally get a better risk-return trade-off from mixing than from holding any single asset alone.

[VISUAL: Two wave patterns slightly out of phase, showing how their combination produces a smoother wave. Labels: "Asset A returns (volatile)", "Asset B returns (volatile)", "Combined portfolio (smoother)"]

**Sam:** Okay, let us start at the beginning. What are all the asset classes we should know about?

**Alex:** Let me walk through the major ones. First, you already know equities -- stocks. They have the highest long-term expected returns, roughly 7 to 10 percent per year after inflation historically. But they are also the most volatile, with annual swings of 15 to 20 percent being normal.

**Sam:** Right, stocks are the growth engine.

**Alex:** Exactly. Then you have fixed income -- bonds. Lower expected returns, maybe 1 to 4 percent after inflation, but much less volatile. They serve as ballast in your portfolio and tend to do well when the economy slows down.

[VISUAL: Bar chart showing historical real returns for each major asset class over 1926-2025, with error bars showing the range of outcomes]

**Sam:** Stocks for growth, bonds for stability. What else?

**Alex:** Real estate, which you can access through REITs -- Real Estate Investment Trusts. These are companies that own properties and are required by law to pay out most of their income as dividends. Returns have been between stocks and bonds historically, roughly 5 to 7 percent real. They also provide inflation protection because rents tend to rise with inflation.

**Sam:** I like the idea of owning real estate without being a landlord.

**Alex:** Same. Then you have commodities -- physical goods like oil, copper, wheat, and natural gas. Commodities have low long-term real returns, maybe 0 to 2 percent. So why own them? Because they have very low correlation with stocks and bonds, and they tend to surge during inflationary periods -- exactly when your stocks and bonds are struggling.

[VISUAL: Timeline showing commodity performance during major inflationary periods: 1970s oil crisis, 2003-2008 commodity boom, 2021-2022 post-COVID inflation, with stock/bond returns shown for comparison]

**Sam:** So commodities are like insurance against inflation?

**Alex:** Precisely. And then there is gold, which deserves its own category. Gold has been a store of value for thousands of years. It has very low real returns over the long run, but it tends to spike during financial crises, geopolitical turmoil, and loss of confidence in governments and currencies.

**Sam:** So gold is crisis insurance?

**Alex:** That is a perfect way to think about it. In 2008, when stocks fell roughly 50 percent, gold rose about 5 percent. During the early COVID panic in March 2020, gold held its value while stocks plunged. A small allocation to gold -- 5 to 10 percent -- can meaningfully reduce your portfolio's worst-case drawdown.

**Sam:** And the last one -- TIPS?

**Alex:** Treasury Inflation-Protected Securities. These are government bonds whose principal adjusts with inflation. So if inflation runs at 5 percent, your bond's face value increases by 5 percent. They are a direct hedge against unexpected inflation, which is one of the biggest risks to a traditional stock-bond portfolio.

[VISUAL: Comparison of a regular Treasury bond vs. TIPS during an inflationary period, showing how the TIPS principal grows while the regular bond's real value shrinks]

**Sam:** Alright, so we have got stocks, bonds, REITs, commodities, gold, and TIPS. How do we know which ones to combine and in what proportions?

**Alex:** And that brings us to one of the most important concepts in all of investing: correlation.

[VISUAL: Title card "Correlation: The Secret Sauce of Diversification"]

**Sam:** Correlation -- how assets move relative to each other?

**Alex:** Right. It is measured on a scale from negative one to positive one. A correlation of positive one means two assets move in perfect lockstep -- if one goes up 10 percent, the other goes up 10 percent. No diversification benefit at all. A correlation of zero means they move independently -- knowing what one did tells you nothing about the other. And negative one means they move in exactly opposite directions.

**Sam:** And we want low or negative correlations in our portfolio?

**Alex:** Exactly. The lower the correlation, the more two assets reduce each other's risk when combined. Let me show you a real-world correlation matrix.

[VISUAL: Full correlation matrix displayed as a heat map, with dark red for high positive correlation, white for zero, and dark blue for negative. Each cell shows the numerical value]

**Alex:** Look at a few key relationships. US stocks and international stocks have a correlation of about 0.75. That is pretty high -- they move mostly together. Not much diversification there.

**Sam:** So owning international stocks does not help as much as people think?

**Alex:** For diversification purposes, much less than it used to. Globalization has linked equity markets together. But look at US stocks versus US government bonds: about negative 0.10. They tend to move in opposite directions. When stocks crash, investors flee to Treasuries, pushing bond prices up. That is powerful diversification.

**Sam:** What about commodities and gold?

**Alex:** Commodities have a correlation of about 0.15 with stocks -- nearly independent. Gold is roughly negative 0.05 to zero. These are the kinds of assets that provide genuine diversification, because they respond to different economic forces than stocks do.

[ANIMATION: animation/week15_efficient_frontier.py - Animated visualization showing how adding each new asset class to a portfolio shifts and extends the efficient frontier upward and to the left. Start with stocks only (a single dot), add bonds (a curve forms), add REITs (curve shifts up), add commodities (curve shifts left), add gold (curve shifts further left). Each addition is highlighted with a label showing the new asset class being incorporated.]

**Sam:** That animation is incredible. Every time we add a new low-correlation asset, the curve moves up and to the left -- meaning more return for less risk.

**Alex:** Exactly. And that curve is called the efficient frontier, which brings us to modern portfolio theory.

[VISUAL: Title card "Modern Portfolio Theory: The Efficient Frontier"]

**Alex:** In 1952, a young economist named Harry Markowitz published a paper that would eventually win the Nobel Prize. The core idea was deceptively simple: do not evaluate investments in isolation. What matters is how each investment contributes to the total portfolio.

**Sam:** Makes sense. A stock that is risky on its own might actually reduce portfolio risk if it has low correlation with everything else.

**Alex:** Exactly right. Markowitz showed that for any given level of risk, there exists an optimal combination of assets that maximizes expected return. Plot all these optimal portfolios on a chart with risk on the x-axis and return on the y-axis, and you get a curve called the efficient frontier.

[VISUAL: Clean diagram of the efficient frontier with clearly labeled axes, showing several portfolio points along the curve and a few sub-optimal portfolios below it]

**Sam:** So any portfolio ON the curve is optimal, and anything below it is leaving money on the table?

**Alex:** Correct. If your portfolio is below the efficient frontier, you could either earn more return for the same risk, or take less risk for the same return, by moving to the frontier. That is what portfolio optimization does -- it finds the weights that get you onto the frontier.

**Sam:** How does the math actually work? Can you give me an intuitive example?

**Alex:** Sure. Let us take two assets. Asset A has an expected return of 10 percent and volatility of 15 percent -- think stocks. Asset B has an expected return of 4 percent and volatility of 5 percent -- think bonds. And they have a correlation of negative 0.10.

**Sam:** Classic stocks and bonds.

**Alex:** Now, if you put 60 percent in A and 40 percent in B, your expected return is simply the weighted average: 0.60 times 10 plus 0.40 times 4 equals 7.6 percent. Easy.

**Sam:** Right, that is just a weighted average.

**Alex:** But here is where the magic happens. The portfolio's risk is NOT the weighted average. The weighted average risk would be 0.60 times 15 plus 0.40 times 5 equals 11 percent. But because of the negative correlation, the actual portfolio risk is only about 9 percent.

[VISUAL: Two side-by-side calculations. Left: "Expected Return = Weighted Average = 7.6%". Right: "Expected Risk =/= Weighted Average. Weighted Avg = 11%. Actual = 9.0%. Diversification benefit = 2 percentage points of FREE risk reduction"]

**Sam:** Two full percentage points of risk just disappear?

**Alex:** They do not disappear -- they cancel out. When stocks zig down, bonds tend to zag up. The negative correlation term in the formula literally subtracts from total portfolio risk. This is the free lunch Markowitz was talking about.

**Sam:** That is genuinely amazing. But I have heard there are problems with this approach?

**Alex:** Yes, and this is important. The efficient frontier is only as good as the inputs you feed it. You need three inputs: expected returns, expected volatilities, and expected correlations for every asset class. The problem is that expected returns are notoriously difficult to estimate. Small changes in your return assumptions can produce wildly different "optimal" portfolios.

**Sam:** So the theory is elegant but the practice is messy?

**Alex:** Exactly. This is called estimation risk, and it is a serious problem. Run an optimizer with slightly different return estimates and you might get an allocation of 70 percent stocks and 5 percent gold one day, then 20 percent stocks and 40 percent gold the next. That kind of instability is not useful.

[VISUAL: Three different efficient frontiers generated with slightly different return assumptions, showing how the optimal portfolio point shifts dramatically]

**Sam:** So what do practitioners do about this?

**Alex:** Several things. First, many add constraints -- maximum and minimum weights for each asset class. You might say no single asset class can be more than 40 percent or less than 5 percent. Second, some use more robust estimation techniques. And third -- and this leads to our next topic -- some abandon return optimization entirely and focus on risk alone.

[VISUAL: Title card "Risk Parity: A Different Philosophy"]

**Sam:** Risk parity. I have heard this term but never really understood it.

**Alex:** Let me start with a simple observation about the traditional 60/40 portfolio. Stocks are allocated 60 percent of the weight. Bonds get 40 percent. Seems balanced, right?

**Sam:** Sure, 60/40 sounds balanced.

**Alex:** But now look at the risk side. Stocks have roughly three times the volatility of bonds. So even though stocks are 60 percent of the portfolio by weight, they contribute about 90 percent of the portfolio's risk. The 60/40 portfolio is not balanced at all -- it is essentially a stock portfolio with a small bond buffer.

[VISUAL: Two pie charts side by side. Left: "Weight Allocation" showing 60% stocks, 40% bonds. Right: "Risk Allocation" showing 90% stocks, 10% bonds. The contrast is dramatic and highlighted with color coding]

**Sam:** Wait, 90 percent? So when stocks crash, the bonds can barely soften the blow?

**Alex:** Exactly. In 2008, the 60/40 portfolio fell about 30 to 35 percent. That is not what most people expect from a "balanced" portfolio. Risk parity says: instead of balancing by weight, balance by risk. Make each asset class contribute equally to portfolio risk.

**Sam:** How do you do that?

**Alex:** Since bonds are less volatile than stocks, you need to hold more bonds per dollar of risk contribution. A simplified risk parity portfolio might look like 25 percent stocks, 55 percent bonds, and 20 percent commodities -- with each contributing roughly one-third of the portfolio's risk.

**Sam:** But that is a lot of bonds. Will not the returns be too low?

**Alex:** In the pure risk parity approach, you use leverage to scale up the overall return. If the unlevered risk parity portfolio returns 5 percent with 6 percent volatility, you might lever it 1.5 times to get 7.5 percent return with 9 percent volatility -- similar return to 60/40 but with genuinely balanced risk.

[VISUAL: Bar chart comparing three portfolios: 60/40 (unlevered), Risk Parity (unlevered, low return), and Risk Parity (levered, comparable return). Show both return and risk metrics]

**Sam:** Leverage sounds scary though. Is that safe?

**Alex:** That is the right concern. For most individual investors, I would not recommend levered risk parity. The good news is that even without leverage, a risk-parity-inspired portfolio -- one that tilts toward bonds and includes commodities, gold, and TIPS -- can provide better diversification than a traditional 60/40.

**Sam:** Like a "risk parity lite"?

**Alex:** Exactly. Something like 20 percent stocks, 30 percent long-term Treasuries, 15 percent TIPS, 10 percent gold, 10 percent commodities, 10 percent international stocks, and 5 percent REITs. No leverage needed, but much more balanced risk exposure than 60/40.

[VISUAL: The Risk Parity Lite allocation displayed as a bar chart with risk contribution percentages shown for each asset class, demonstrating more balanced risk than 60/40]

**Sam:** Let us talk about some complete portfolios people actually use. I have heard of things like the All-Weather portfolio and the Yale Model.

**Alex:** Great idea. Let me walk through several famous multi-asset portfolios that real investors use.

[VISUAL: Title card "Portfolio Models: From Simple to Sophisticated"]

**Alex:** First, the Three-Fund Portfolio, popularized by Bogleheads. Just US stocks, international stocks, and US bonds. Something like 50-30-20. It is beautifully simple, incredibly low cost, and captures the basic diversification between equities and fixed income.

**Sam:** That is what I started with.

**Alex:** And it is a perfectly reasonable portfolio for many people. But we can improve on it. The Four-Fund Portfolio adds REITs as a fourth asset class. Something like 40 percent US stocks, 20 percent international stocks, 25 percent bonds, and 15 percent REITs. This adds real estate exposure and a bit more diversification.

[VISUAL: Side-by-side comparison of the three-fund and four-fund portfolios, showing allocations and historical risk-return metrics]

**Sam:** What about Ray Dalio's All-Weather portfolio? That is the one Bridgewater runs, right?

**Alex:** The simplified version for individual investors is roughly 30 percent US stocks, 40 percent long-term Treasuries, 15 percent intermediate Treasuries, 7.5 percent gold, and 7.5 percent commodities. It is designed to perform reasonably well in all four economic environments: rising growth, falling growth, rising inflation, and falling inflation.

**Sam:** Why so many bonds? 55 percent seems like a lot.

**Alex:** Because it is risk-parity-inspired. Bonds are less volatile, so you need more of them to balance the risk contribution of stocks. The gold and commodities provide inflation protection that bonds lack. The result is a portfolio that had remarkably small drawdowns historically.

**Sam:** How did it actually perform?

**Alex:** During the 2008 crisis, the All-Weather portfolio lost only about 3 to 4 percent while the S&P 500 fell nearly 40 percent. Over long periods, it returned about 7 to 8 percent per year with much smaller drawdowns than a stock-heavy portfolio. The trade-off is that it lags stocks during strong bull markets.

[VISUAL: Growth of $10,000 chart from 2005 to 2025 comparing All-Weather, 60/40, and 100% stocks. Show the 2008 drawdown, the 2020 COVID crash, and the 2022 rate-rising environment. All-Weather has the smoothest line but ends lower than 100% stocks]

**Sam:** What about the Yale Model? I have heard David Swensen was a genius.

**Alex:** Swensen ran the Yale endowment for decades and pioneered the use of alternative assets in institutional portfolios. The simplified version for individual investors is something like 30 percent US stocks, 15 percent international developed, 10 percent emerging markets, 15 percent REITs, 15 percent TIPS, and 15 percent nominal bonds.

**Sam:** That is more stock-heavy than All-Weather.

**Alex:** It is, and the real Yale portfolio also included private equity, venture capital, and hedge funds that are not available to individual investors. The key insight Swensen emphasized was that individual investors should stick to low-cost index funds for each asset class rather than trying to pick active managers.

[VISUAL: Table comparing all five portfolio models with columns for allocation, historical return, historical volatility, maximum drawdown, and Sharpe ratio]

**Sam:** How do I choose between all these models?

**Alex:** It depends on your risk tolerance and your beliefs about the future economic environment. If you believe the future will look like the past 40 years -- falling interest rates, strong stock markets, low inflation -- then a stock-heavy portfolio like the Three-Fund or Yale Model will likely do best. If you are worried about inflation, rising rates, or economic uncertainty, the All-Weather or Risk Parity Lite approaches provide more protection.

**Sam:** What about just mixing approaches?

**Alex:** Totally valid. You could start with the Three-Fund Portfolio as your core and then add 10 to 15 percent in real assets like gold, commodities, and TIPS as a satellite allocation. That gives you the simplicity of the core with some additional diversification on the edges.

[VISUAL: Diagram showing Core-Satellite approach: a large circle labeled "Core: Three-Fund Portfolio (70-80%)" surrounded by smaller circles labeled "Gold (5%)", "Commodities (5%)", "TIPS (5%)", "REITs (5%)"]

**Sam:** Let me ask about something practical. I am going to set my allocation and then what? Just leave it alone?

**Alex:** Not quite. Over time, market movements will push your portfolio away from its target weights. If stocks have a great year, they might drift from 40 percent to 48 percent of your portfolio. You need to rebalance -- bring the weights back to targets.

[VISUAL: Title card "Rebalancing: The Discipline That Pays"]

**Sam:** How often should I rebalance?

**Alex:** Research shows that annual or semi-annual rebalancing captures most of the benefit. More frequent rebalancing just adds transaction costs. Some people use threshold-based rebalancing instead -- you rebalance whenever any asset class has drifted more than 5 percentage points from its target.

**Sam:** Is not rebalancing just selling your winners and buying your losers? That feels wrong.

**Alex:** It does feel wrong, and that is exactly why it works. Rebalancing is a systematic way to buy low and sell high. When stocks surge, you trim them. When they crash, you buy more. Studies show this disciplined contrarian behavior has added roughly 0.3 to 0.5 percent per year in return historically.

[VISUAL: Chart showing a portfolio that drifts away from target, gets rebalanced, drifts again, gets rebalanced again -- with annotations showing "Sell high" and "Buy low" at each rebalancing event]

**Sam:** And the tax-efficient way to do this?

**Alex:** Great point. In taxable accounts, the best approach is to use new contributions to buy underweight assets rather than selling overweight ones. Direct your monthly investment to whatever has drifted furthest below its target. Also, if you receive dividends, reinvest them into the underweight asset classes. This way you rebalance over time without triggering capital gains taxes.

**Sam:** Clever. Let us talk about one more thing -- the practical implementation. How do I actually build a multi-asset portfolio with ETFs?

**Alex:** The amazing thing is that you can build an institutional-quality multi-asset portfolio with just five to seven low-cost ETFs. For US stocks, VTI at 0.03 percent expense ratio. For international stocks, VXUS at 0.07 percent. For bonds, BND at 0.03 percent. For long-term Treasuries, TLT at 0.15 percent. For TIPS, SCHP at 0.03 percent. For gold, GLDM at 0.10 percent. For commodities, PDBC at 0.59 percent.

[VISUAL: A "shopping list" graphic showing each ETF with its ticker, name, asset class, and expense ratio, organized as a checklist]

**Sam:** So total portfolio cost would be what, maybe 0.10 to 0.15 percent per year?

**Alex:** Something in that range, depending on the weights. Institutional investors pay tens of millions in management fees for similar strategies. You can do it for pennies on the dollar with ETFs.

**Sam:** That is incredible.

**Alex:** One important note on commodities ETFs. Most commodity ETFs use futures contracts, not physical commodities. Futures-based ETFs can suffer from something called "roll cost" or "contango" -- they lose money when they sell expiring contracts and buy new ones. This can drag on returns over time. Make sure you understand this before adding a commodity ETF.

[VISUAL: Diagram showing how futures-based commodity ETFs work, with the "roll" process illustrated and the contango cost highlighted]

**Sam:** Good warning. Let me make sure I understand the big picture. I should think about which economic environments I want to be protected against, then choose asset classes that perform well in those environments, then combine them with low correlations, and rebalance periodically?

**Alex:** That is a perfect summary. And remember the economic regime coverage map we discussed. Growth with low inflation favors stocks and REITs. Growth with high inflation favors commodities and TIPS. Recession with low inflation favors bonds. Recession with high inflation -- stagflation -- favors gold and commodities. A good multi-asset portfolio has some assets performing well in every one of those environments.

[VISUAL: Four-quadrant economic regime grid with Growth/Recession on one axis and High/Low Inflation on the other, with each quadrant showing the best-performing asset classes]

**Sam:** Before we wrap up, let me ask about a common concern I hear: "Is not this all just over-complicating things? Warren Buffett says just buy an S&P 500 index fund."

**Alex:** Buffett's advice is specifically for his estate after he dies -- for money his wife will not need for decades. And he is not wrong for that specific situation. A 100 percent stock portfolio has the highest expected long-term return. But most real people cannot stomach a 40 to 50 percent drawdown, which stocks have delivered multiple times. They panic-sell at the bottom and lock in losses. A multi-asset portfolio with smaller drawdowns is easier to hold through crises, and the portfolio you actually hold is infinitely better than the one you abandon.

**Sam:** So it is about matching the portfolio to the investor, not just chasing the highest return.

**Alex:** Exactly. The best portfolio is the one you can stick with for decades. Multi-asset allocation helps you find that portfolio by offering better risk-adjusted returns and smaller worst-case scenarios.

[VISUAL: Split-screen showing two investors during a market crash. Left: "100% Stocks" investor panics and sells at the bottom. Right: "Multi-Asset" investor stays calm because the portfolio only fell 15% instead of 40%]

**Sam:** That makes a lot of sense. Three key takeaways from today?

**Alex:** First, diversification beyond stocks and bonds is not complication -- it is completion. Asset classes like commodities, gold, REITs, and TIPS provide genuine diversification that different types of stocks do not. Second, what matters is not how many assets you own but how they correlate with each other. Focus on adding assets with low correlations to your existing portfolio. Third, the efficient frontier shows the optimal risk-return trade-off, but your inputs matter enormously -- consider simpler approaches like equal risk contribution if you are unsure about expected returns.

**Sam:** And maybe a bonus takeaway: rebalance regularly. That systematic buy-low, sell-high discipline adds real value over time.

**Alex:** Great addition. Next week, we are going to talk about how the business cycle affects which sectors of the economy perform best, and how you can tilt your portfolio to take advantage of that cycle. It is called sector rotation, and it is fascinating.

**Sam:** Can not wait. See everyone next week!

[VISUAL: End screen with subscribe button, links to previous lessons, and a preview thumbnail for Week 16: Business Cycles and Sector Rotation]

---
