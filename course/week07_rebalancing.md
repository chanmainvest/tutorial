# Week 7: Portfolio Rebalancing

---

## Reading Section

### a) Why This Is Important

Rebalancing is one of the few investment strategies that is both simple to understand and genuinely effective, yet most individual investors either ignore it entirely or do it wrong. It is the discipline of periodically adjusting your portfolio back to your target asset allocation, and it matters far more than most people realize.

Here is the core problem rebalancing solves. Suppose you decide on a 60/40 stock/bond portfolio. After a strong year for stocks, your portfolio drifts to 75/25. You now have significantly more risk than you intended. If the market drops 30%, your 75% stock allocation means a 22.5% portfolio loss instead of the 18% loss you would have experienced at 60/40. That 4.5 percentage point difference on a $500,000 portfolio is $22,500 of additional loss you never signed up for.

But rebalancing is not just about controlling risk. It is a systematic way to buy low and sell high -- the holy grail of investing that most people fail to do because emotions get in the way.

Consider what happens when you rebalance:

1. **You sell winners and buy losers.** After stocks have risen, rebalancing forces you to sell some stocks (which have become relatively expensive) and buy bonds (which have become relatively cheap). After stocks have fallen, rebalancing forces you to buy stocks (now cheaper) and sell bonds (now relatively expensive). This is the opposite of what your emotions tell you to do, and that is precisely why it works.

2. **You maintain your intended risk level.** Without rebalancing, your portfolio's risk profile changes over time as different assets grow at different rates. A portfolio that starts at 60/40 can easily drift to 80/20 during a bull market, exposing you to far more risk than your financial plan assumed.

3. **You impose discipline on an emotional process.** Investing is psychologically brutal. Rebalancing gives you a rules-based framework that removes emotion from the equation. When everyone is panicking and selling stocks, your rebalancing rule says "buy more stocks." When everyone is euphoric and piling into stocks, your rebalancing rule says "take some profits."

4. **You can capture a "rebalancing bonus."** Academic research has demonstrated that in certain market conditions, a rebalanced portfolio can actually outperform its individual components. This rebalancing bonus arises from the mathematical properties of volatile, mean-reverting assets -- and we will explore it in detail in this lesson.

5. **It is one of the few free lunches in investing.** Rebalancing does not require stock-picking skill, market timing ability, or access to special information. It is purely mechanical, yet it improves both risk-adjusted and, in many environments, absolute returns.

The CFA Institute considers portfolio rebalancing a fundamental component of the Investment Policy Statement (IPS) and portfolio management process. At every level of the CFA curriculum, candidates are expected to understand when and how to rebalance, the tradeoffs between different rebalancing strategies, and the tax and transaction cost implications. This is not optional knowledge -- it is foundational.

---

### b) What You Need to Know

#### 1. What Rebalancing Actually Is

Rebalancing is the process of realigning the weights of assets in your portfolio to match your target allocation. When market movements cause your actual allocation to drift from your target, you sell overweight assets and buy underweight ones to restore balance.

```
PORTFOLIO DRIFT AND REBALANCING
================================

Starting Target: 60% Stocks / 40% Bonds

         START            AFTER BULL        AFTER
        (Jan 1)          MARKET            REBALANCING
                         (Dec 31)          (Dec 31)

  100% |                 |                 |
       |                 |########         |
   80% |                 |# Stocks#        |
       |                 |# 75%   #        |
   60% |########         |########         |########
       |# Stocks#        |                 |# Stocks#
   40% |# 60%  #|--------|                 |# 60%  #|--------
       |########|////////|########         |########|////////
   20% |        |/ Bonds/|/ Bonds/         |        |/ Bonds/
       |        |/ 40%  /|/ 25%  /         |        |/ 40%  /
    0% |--------|--------|--------         |--------|--------

       DRIFT happens          REBALANCE restores
       automatically          target allocation
       as markets move        by selling stocks,
                              buying bonds
```

The concept is straightforward, but the execution involves several important decisions: how often to rebalance, what triggers a rebalance, how to handle taxes, and which specific trades to make.

---

#### 2. Why Portfolios Drift

Asset classes have different expected returns and different volatilities. Over time, higher-returning assets grow to dominate the portfolio while lower-returning assets shrink in proportion.

```
DRIFT MECHANICS -- A NUMERICAL EXAMPLE
=========================================

Starting Portfolio: $100,000
Target: 60% Stocks ($60,000) / 40% Bonds ($40,000)

Scenario: Stocks return +25%, Bonds return +3%

Asset       Start       Return      End Value     New Weight
------      -----       ------      ---------     ----------
Stocks      $60,000     +25%        $75,000       64.7%
Bonds       $40,000     +3%         $41,200       35.3%
            --------                --------      ------
Total       $100,000                $116,200      100.0%

Drift from target:
  Stocks:  64.7% vs 60.0% = +4.7% overweight
  Bonds:   35.3% vs 40.0% = -4.7% underweight

To rebalance:
  Target stock value = 60% x $116,200 = $69,720
  Sell $75,000 - $69,720 = $5,280 of stocks
  Buy $5,280 of bonds

After rebalancing:
  Stocks:  $69,720  (60.0%)
  Bonds:   $46,480  (40.0%)
  Total:   $116,200 (100.0%)
```

Notice something important: rebalancing forced you to sell $5,280 of stocks after they rose 25%. You are taking profits systematically. If stocks subsequently decline, you protected some gains. If stocks continue rising, you gave up some upside -- but you maintained your risk target.

---

#### 3. The Buy-Low, Sell-High Mechanism

This is the most powerful and underappreciated aspect of rebalancing. It systematically enforces contrarian behavior.

```
THE REBALANCING CYCLE -- BUY LOW, SELL HIGH
=============================================

              Stock Price Movement Over Time
     Price
       ^
  $150 |              *
       |            *   *
  $130 |          *       *
       |        *           *
  $110 |      *               *              *
       |    *                   *          *   *
   $90 |  *                       *      *
       |*                           *  *
   $70 |                              *
       +-----|-----|-----|-----|-----|-----|---->
        Jan   Jun   Dec   Jun   Dec   Jun  Time
        Yr1   Yr1   Yr1   Yr2   Yr2   Yr3

  Rebalancing Actions:
  Dec Yr1:  Stock rose   --> SELL stocks, BUY bonds
  Dec Yr2:  Stock fell   --> BUY stocks, SELL bonds
  Jun Yr3:  Stock rose   --> SELL stocks, BUY bonds

  Each time: selling what went UP, buying what went DOWN
  This IS the buy-low, sell-high discipline!
```

Most investors do the opposite. When stocks are soaring, greed kicks in and they want to buy more. When stocks are crashing, fear kicks in and they want to sell. Rebalancing mechanically prevents this emotional trap.

---

#### 4. Calendar Rebalancing vs. Threshold Rebalancing

There are two main approaches to deciding when to rebalance, each with distinct advantages and disadvantages.

**Calendar Rebalancing**

You rebalance on a fixed schedule -- monthly, quarterly, semi-annually, or annually. Regardless of how much or how little the portfolio has drifted, you bring it back to target on the scheduled date.

**Threshold (Percentage-of-Portfolio) Rebalancing**

You rebalance whenever any asset class drifts beyond a predetermined band around its target. For example, if your stock target is 60%, you might set bands of plus or minus 5 percentage points. You only rebalance when stocks exceed 65% or fall below 55%.

```
CALENDAR vs. THRESHOLD REBALANCING
====================================

CALENDAR REBALANCING
--------------------
  Jan 1    Apr 1    Jul 1    Oct 1    Jan 1
    |        |        |        |        |
    R        R        R        R        R
    |        |        |        |        |
    (Quarterly example -- rebalance every 3 months)

  Pros: Simple, predictable, easy to automate
  Cons: May rebalance unnecessarily (small drift)
        May miss needed rebalance (big drift between dates)

THRESHOLD REBALANCING
---------------------
  Target: 60% stocks, Band: +/- 5%

       65% .............. UPPER BAND (trigger: sell stocks)
            \
             \    Actual
              \  Allocation   * <-- Trigger! Rebalance.
       60% ---\-----------/------  TARGET
                \       /
                 \   /
       55% ........*......... LOWER BAND (trigger: buy stocks)
                   ^
                   Trigger! Rebalance.

  Pros: Only rebalances when meaningful drift occurs
        Responds to large market moves immediately
  Cons: More complex to monitor
        May generate more trades in volatile markets

HYBRID APPROACH (MOST RECOMMENDED)
-----------------------------------
  Check allocation on a fixed schedule (e.g., quarterly)
  Only rebalance if drift exceeds threshold (e.g., 5%)

  This combines the simplicity of calendar with the
  efficiency of threshold rebalancing.
```

**What does the research say?**

Academic studies including those by Vanguard and various CFA research papers have found that the specific frequency of rebalancing matters less than the fact that you rebalance at all. Annual rebalancing, semi-annual rebalancing, and threshold-based rebalancing all produce broadly similar long-term results. The biggest difference is between rebalancing and not rebalancing.

That said, a hybrid approach -- checking quarterly but only rebalancing when drift exceeds 5 percentage points -- tends to minimize transaction costs while capturing most of the benefit.

---

#### 5. The Rebalancing Bonus

One of the most fascinating findings in portfolio theory is that a rebalanced portfolio of volatile, negatively correlated (or uncorrelated) assets can outperform each individual asset over time. This phenomenon is called the rebalancing bonus (sometimes called the diversification return or volatility harvesting).

```
THE REBALANCING BONUS -- A SIMPLIFIED EXAMPLE
================================================

Consider two assets that alternate between +30% and -10%,
but in opposite years:

Year    Asset A     Asset B     50/50 Portfolio
                                (Rebalanced Annually)
----    -------     -------     ----------------
  1      +30%        -10%
  2      -10%        +30%
  3      +30%        -10%
  4      -10%        +30%

After 4 years:
  Asset A alone:  $100 x 1.30 x 0.90 x 1.30 x 0.90 = $136.89
  Asset B alone:  $100 x 0.90 x 1.30 x 0.90 x 1.30 = $136.89

  Annualized return each: ~8.17%

  50/50 Rebalanced Portfolio:
  Year 1: A=$65 x 1.30=$84.50, B=$50 x 0.90=$45.00
           Total=$129.50, Rebalance to $64.75 each
  Year 2: A=$64.75 x 0.90=$58.28, B=$64.75 x 1.30=$84.18
           Total=$142.45, Rebalance to $71.23 each
  Year 3: A=$71.23 x 1.30=$92.59, B=$71.23 x 0.90=$64.10
           Total=$156.69, Rebalance to $78.35 each
  Year 4: A=$78.35 x 0.90=$70.51, B=$78.35 x 1.30=$101.85
           Total=$172.36

  Annualized return of rebalanced portfolio: ~14.6%

  REBALANCING BONUS: 14.6% - 8.17% = +6.4% per year!
```

This is a stylized example, but the principle holds in real markets: when assets are volatile and do not move in lockstep, rebalancing systematically harvests the difference. The bonus is largest when:

- Asset volatility is high
- Correlation between assets is low or negative
- Assets tend to mean-revert (what goes down comes back)

In real-world portfolios, the rebalancing bonus is typically 0.5% to 1.5% per year -- modest but meaningful over decades of compounding.

```
WHEN THE REBALANCING BONUS IS LARGEST vs. SMALLEST
=====================================================

  LARGEST BONUS                    SMALLEST BONUS
  +--------------------------+    +--------------------------+
  | High volatility          |    | Low volatility           |
  | Low/negative correlation |    | High positive correlation|
  | Mean-reverting markets   |    | Trending markets         |
  | Multiple asset classes   |    | Few, similar assets      |
  +--------------------------+    +--------------------------+

  Real-world estimates:
  US Stocks + US Bonds:            ~0.2-0.5% per year
  US Stocks + Int'l Stocks:        ~0.3-0.7% per year
  Multi-asset (stocks, bonds,      ~0.5-1.5% per year
    REITs, commodities):
```

**Important caveat:** In strongly trending markets (where one asset consistently outperforms), rebalancing will reduce returns because you keep selling the winner. The rebalancing bonus is most evident in range-bound or mean-reverting markets. This does not mean you should stop rebalancing in trending markets -- risk control remains the primary purpose.

---

#### 6. Tax Considerations in Rebalancing

In taxable accounts, every rebalancing trade is a potential tax event. Selling appreciated assets generates capital gains taxes, which can significantly erode the benefit of rebalancing if not managed carefully.

```
TAX IMPACT OF REBALANCING
===========================

Scenario: Sell $10,000 of stocks that have $4,000 of gains

  If Short-Term Gains (held < 1 year):
    Tax rate: up to 37% (ordinary income)
    Tax bill: $4,000 x 0.37 = $1,480
    Net proceeds: $10,000 - $1,480 = $8,520

  If Long-Term Gains (held > 1 year):
    Tax rate: 15% or 20% for most investors
    Tax bill: $4,000 x 0.15 = $600
    Net proceeds: $10,000 - $600 = $9,400

  Difference: $880 -- just from holding period!
```

**Tax-efficient rebalancing strategies:**

```
TAX-EFFICIENT REBALANCING METHODS
===================================

METHOD 1: USE NEW CONTRIBUTIONS
--------------------------------
Instead of selling overweight assets, direct new
contributions to underweight asset classes.

  Portfolio: 65% stocks / 35% bonds (target: 60/40)
  Monthly contribution: $2,000

  --> Put entire $2,000 into bonds until balance restores
  --> No selling = no taxes!

  Best for: Accumulation phase, regular contributors

METHOD 2: USE WITHDRAWALS STRATEGICALLY
-----------------------------------------
In retirement, withdraw from overweight asset classes.

  Portfolio: 65% stocks / 35% bonds (target: 60/40)
  Monthly withdrawal: $3,000

  --> Withdraw from stocks until balance restores
  --> You were going to sell anyway!

  Best for: Distribution phase, retirees

METHOD 3: REBALANCE IN TAX-ADVANTAGED ACCOUNTS
------------------------------------------------
Keep the most tax-inefficient rebalancing in IRAs and 401(k)s,
where there are no capital gains taxes.

  Taxable Account: Hold and rarely sell
  IRA / 401(k):    Rebalance freely

  Best for: Investors with assets in both account types

METHOD 4: TAX-LOSS HARVESTING DURING REBALANCING
--------------------------------------------------
When selling, prioritize lots with losses to offset gains.

  Lot 1: 100 shares bought at $50, now $60 (gain $1,000)
  Lot 2: 100 shares bought at $70, now $60 (loss $1,000)

  --> Sell Lot 2 first to realize loss
  --> Loss offsets gains from other rebalancing trades

  Best for: Volatile markets with mixed gains/losses

METHOD 5: USE DIVIDENDS AND INTEREST
--------------------------------------
Direct dividends and interest payments to underweight
asset classes instead of reinvesting in the same fund.

  Stock dividends --> Purchase bonds
  Bond interest   --> Purchase stocks (if stocks underweight)

  Best for: Income-generating portfolios
```

**The tax-efficiency hierarchy for rebalancing:**

```
MOST TAX-EFFICIENT (try these first)
  |
  |  1. Direct new contributions to underweight assets
  |  2. Reinvest dividends/interest into underweight assets
  |  3. Rebalance within tax-advantaged accounts (IRA, 401k)
  |  4. Sell assets with losses (tax-loss harvesting)
  |  5. Sell assets with long-term gains (lower tax rate)
  |  6. Sell assets with short-term gains (highest tax rate)
  |
LEAST TAX-EFFICIENT (avoid if possible)
```

---

#### 7. Rebalancing Across Multiple Asset Classes

Real portfolios often have more than two asset classes. Rebalancing becomes more nuanced but follows the same principles.

```
MULTI-ASSET PORTFOLIO REBALANCING
===================================

Target Allocation:
  US Stocks:        35%    |============================|
  Int'l Stocks:     20%    |================|
  Bonds:            25%    |====================|
  REITs:            10%    |========|
  Commodities:       5%    |====|
  Cash:              5%    |====|
                   -----
                   100%

After One Year of Drift:
  US Stocks:        42%    |=================================|  +7%
  Int'l Stocks:     18%    |==============|                     -2%
  Bonds:            22%    |=================|                  -3%
  REITs:            11%    |=========|                          +1%
  Commodities:       3%    |==|                                 -2%
  Cash:              4%    |===|                                -1%
                   -----
                   100%

Rebalancing Trades (on $200,000 portfolio):
  SELL US Stocks:         -$14,000  (42% --> 35%)
  BUY Int'l Stocks:       +$4,000  (18% --> 20%)
  BUY Bonds:              +$6,000  (22% --> 25%)
  SELL REITs:             -$2,000   (11% --> 10%)
  BUY Commodities:        +$4,000  (3%  --> 5%)
  BUY Cash:               +$2,000  (4%  --> 5%)
```

With multiple asset classes, you can often net trades against each other: sell the overweight assets and use the proceeds to buy the underweight ones. This minimizes the total number and size of transactions.

---

#### 8. Implementation: A Step-by-Step Rebalancing Process

```
REBALANCING WORKFLOW
=====================

  +-------------------+
  | 1. SET TARGET     |    Define your target allocation
  |    ALLOCATION     |    based on goals, risk tolerance,
  +--------+----------+    and time horizon
           |
           v
  +-------------------+
  | 2. SET BANDS      |    Determine rebalancing thresholds
  |    (e.g., +/-5%)  |    (e.g., rebalance if any asset
  +--------+----------+    drifts more than 5% from target)
           |
           v
  +-------------------+
  | 3. SET SCHEDULE   |    Choose review frequency
  |    (e.g., Qtrly)  |    (monthly, quarterly, annually)
  +--------+----------+
           |
           v
  +-------------------+
  | 4. REVIEW         |    On schedule date, compare
  |    CURRENT vs.    |    actual vs. target allocation
  |    TARGET         |
  +--------+----------+
           |
           v
  +-------------------+     NO
  | 5. DRIFT EXCEEDS  |---------> Do nothing.
  |    THRESHOLD?     |           Wait for next review.
  +--------+----------+
           | YES
           v
  +-------------------+
  | 6. CALCULATE      |    Determine exact dollar amounts
  |    TRADES         |    to sell/buy for each asset
  +--------+----------+
           |
           v
  +-------------------+
  | 7. CONSIDER       |    Can you use contributions,
  |    TAX IMPACT     |    dividends, or tax-advantaged
  +--------+----------+    accounts instead of selling?
           |
           v
  +-------------------+
  | 8. EXECUTE        |    Place trades, preferably all
  |    TRADES         |    on the same day to avoid
  +--------+----------+    interim drift
           |
           v
  +-------------------+
  | 9. DOCUMENT       |    Log what you did and why
  |    AND RECORD     |    (for tax records and review)
  +-------------------+
```

**Practical tips:**

- **Batch your trades.** Execute all rebalancing trades on the same day to avoid interim drift between selling one asset and buying another.
- **Use limit orders for individual stocks.** For ETFs and mutual funds in broad markets, market orders are generally fine.
- **Mind the settlement dates.** Stock and ETF trades settle in T+1 (one business day). Ensure you have settled cash before buying.
- **Automate if possible.** Many 401(k) plans and robo-advisors offer automatic rebalancing. Use it.
- **Keep records.** Track every rebalancing trade for tax purposes, including the date, amount, cost basis, and whether the gain or loss was short-term or long-term.

---

#### 9. How Often Should You Rebalance? The Research

```
REBALANCING FREQUENCY COMPARISON (Historical Backtests)
=========================================================

Frequency      Avg Annual    Volatility   Turnover   Tax
               Return                     (Annual)   Efficiency
----------     ----------    ----------   --------   ----------
Never          9.2%          14.8%        0%         Highest
(drift to 90/10)

Annually       9.1%          11.2%        8%         Good

Semi-Annual    9.1%          11.1%        12%        Moderate

Quarterly      9.0%          11.0%        18%        Lower

Monthly        9.0%          10.9%        25%        Lowest

Daily          8.9%          10.9%        High       Very Low

Note: Based on 60/40 US stock/bond portfolio, 1926-2023.
Actual results vary by period. Returns before taxes and
transaction costs.

KEY FINDINGS:
  - Annual or semi-annual is the sweet spot for most investors
  - More frequent rebalancing reduces volatility slightly
    but increases costs
  - Never rebalancing maximizes raw return but dramatically
    increases risk
  - The benefit of rebalancing is primarily risk reduction,
    not return enhancement
```

For most individual investors, **annual or semi-annual rebalancing with a 5% threshold** is the recommended approach. It captures the vast majority of the risk-reduction benefit while minimizing transaction costs and tax drag.

---

#### 10. Rebalancing in Different Market Environments

```
HOW REBALANCING BEHAVES IN DIFFERENT MARKETS
===============================================

BULL MARKET (stocks steadily rising)
-------------------------------------
  Rebalancing REDUCES returns vs. buy-and-hold
  Because: you keep trimming the winning asset
  But: you maintain risk discipline for when the
       bull market inevitably ends

BEAR MARKET (stocks falling sharply)
--------------------------------------
  Rebalancing FORCES you to buy stocks at lower prices
  This is psychologically the hardest time to rebalance
  But: it is historically the MOST valuable time
  Example: Investors who rebalanced in March 2009
  bought stocks near the bottom

SIDEWAYS/VOLATILE MARKET (choppy, no trend)
---------------------------------------------
  Rebalancing captures the HIGHEST bonus here
  Because: you are systematically buying dips and
  selling rallies within the range
  This is where rebalancing truly shines

CRASH AND RECOVERY (V-shaped market)
---------------------------------------
  Rebalancing during the crash (buying stocks)
  followed by recovery produces the best outcomes
  The deeper the crash, the more you buy
  The stronger the recovery, the more you benefit

  2008-2009 Example:
  Investor who rebalanced quarterly through the
  crisis recovered to breakeven ~1 year faster
  than the investor who froze and did nothing
```

---

### c) Common Misconceptions

**Misconception 1: "Rebalancing is just about maximizing returns."**

Reality: The primary purpose of rebalancing is risk management, not return maximization. In strongly trending markets, rebalancing will actually reduce returns because you sell the winning asset. The value of rebalancing is that it keeps your portfolio's risk level consistent with your financial plan. Over a complete market cycle (including both bull and bear phases), rebalancing tends to improve risk-adjusted returns, but raw returns depend heavily on the specific time period.

**Misconception 2: "I should rebalance as frequently as possible."**

Reality: More frequent rebalancing does not necessarily produce better results. Research consistently shows that annual rebalancing captures most of the benefit. Excessive rebalancing increases transaction costs, generates more taxable events, and rarely improves returns or risk reduction by a meaningful amount. The diminishing returns set in quickly after quarterly frequency.

**Misconception 3: "Rebalancing means selling all my winners."**

Reality: Rebalancing means trimming overweight positions, not eliminating them. If your stock target is 60% and stocks have drifted to 65%, you sell 5 percentage points worth -- not all your stocks. You are still heavily invested in the winning asset class; you are just maintaining your intended exposure level.

**Misconception 4: "I do not need to rebalance because I am in index funds."**

Reality: Index funds are internally rebalanced (stocks entering or leaving the index are automatically adjusted), but your allocation across different index funds still drifts. If you own a US stock index fund and a bond index fund, the relative balance between them changes as markets move. That inter-fund drift is what you need to rebalance.

**Misconception 5: "Rebalancing does not matter if I am decades from retirement."**

Reality: Rebalancing matters at every investment horizon. Young investors with aggressive allocations still benefit from rebalancing between, say, US stocks, international stocks, and small-cap stocks. The rebalancing bonus from uncorrelated volatile assets can add meaningful returns over decades. Additionally, the discipline of rebalancing during your accumulation years builds the habits you will need when the stakes are higher closer to retirement.

**Misconception 6: "I should rebalance during a crash by selling stocks to buy bonds."**

Reality: This is the opposite of what rebalancing requires. During a crash, stocks have fallen and are now underweight relative to your target. Rebalancing means buying more stocks and selling bonds. If your emotional instinct is to sell stocks during a crash, you are not rebalancing -- you are panic-selling. True rebalancing is counter-emotional by design.

---

### d) Common Questions and Answers

**Q1: What is the difference between rebalancing and reallocating?**

A: Rebalancing means restoring your existing target allocation after market drift -- for example, bringing a drifted 65/35 portfolio back to 60/40. Reallocating means changing the target itself -- for example, shifting from 60/40 to 50/50 because you are closer to retirement or your risk tolerance has changed. Rebalancing is tactical maintenance; reallocation is a strategic decision. Both are important, but they serve different purposes.

**Q2: Should I rebalance my 401(k) and IRA separately, or look at my total portfolio?**

A: Ideally, you should view all your accounts as one combined portfolio and rebalance holistically. You might hold all your bonds in your IRA (for tax efficiency) and all your stocks in your taxable account. The individual accounts would look unbalanced, but the total portfolio would be on target. This approach, called asset location, optimizes for tax efficiency. However, if managing multiple accounts feels overwhelming, rebalancing each account individually to its own target is a reasonable simplification.

**Q3: What should my rebalancing bands be?**

A: The most common recommendation is 5 percentage points absolute (e.g., rebalance when stocks hit 65% or 55% against a 60% target) or 25% relative (e.g., rebalance when stocks exceed 75% of their target weight or fall below 45%). For smaller asset class allocations (like a 5% commodities position), tighter bands such as plus or minus 2 percentage points are appropriate because even small absolute changes represent large relative swings.

**Q4: Does rebalancing work with individual stocks, or only with asset classes?**

A: Rebalancing is primarily an asset class concept. You rebalance between stocks and bonds, between US and international, between large-cap and small-cap. While you can rebalance among individual stocks, this is more akin to portfolio management and requires fundamental analysis of each position. Selling a stock that has risen does not make sense if the company's value has genuinely increased -- unlike asset classes, individual stocks do not necessarily mean-revert. Stick to rebalancing at the asset class level.

**Q5: What about rebalancing costs eating into the benefit?**

A: With modern commission-free brokerages and low-cost ETFs, direct transaction costs for rebalancing are minimal. The more significant cost is taxes in taxable accounts. Use tax-efficient rebalancing strategies (new contributions, tax-advantaged accounts, tax-loss harvesting) to minimize this drag. In tax-advantaged accounts like IRAs and 401(k)s, the cost of rebalancing is essentially zero.

**Q6: Should I rebalance after a major market event, even if it is not my scheduled date?**

A: If you use threshold-based rebalancing, yes -- that is exactly what the threshold is for. A major market crash that pushes stocks well below your target should trigger a rebalance. However, resist the urge to rebalance in the middle of a fast-moving event. Wait for markets to stabilize somewhat (a few days to a week) so your trades execute at reasonable prices and you are not whipsawed by intraday volatility.

**Q7: Is there a difference between rebalancing a taxable account versus a retirement account?**

A: The mechanics are the same, but the tax implications are completely different. In a retirement account (IRA, 401(k), Roth IRA), you can rebalance freely without tax consequences -- there are no capital gains taxes on trades within these accounts. In a taxable account, every sale is a potential tax event, so you need to be more deliberate and use the tax-efficient strategies described above.

**Q8: What does the CFA curriculum say about rebalancing?**

A: The CFA curriculum covers rebalancing extensively in the Portfolio Management and Wealth Planning section. Key topics include calendar rebalancing versus percentage-of-portfolio (threshold) rebalancing, the costs and benefits of different rebalancing strategies, the tradeoff between transaction costs and tracking error, and optimal corridor width. The curriculum emphasizes that the appropriate rebalancing strategy depends on risk tolerance, transaction costs, asset class correlations, and tax considerations. Level III in particular expects candidates to recommend and justify specific rebalancing approaches within an Investment Policy Statement.

**Q9: Can rebalancing ever hurt my portfolio?**

A: Yes, in specific circumstances. In a strong, sustained bull market for one asset class, rebalancing will reduce total returns because you keep trimming the winner. If an asset class is in structural decline (not just cyclical), rebalancing into it destroys value. And if rebalancing generates large tax bills in a taxable account, the tax drag can exceed the benefit. These are reasons to be thoughtful about rebalancing, not reasons to avoid it entirely. Over complete market cycles, the risk-management benefits generally outweigh these costs.

**Q10: What tools or platforms can help automate rebalancing?**

A: Many options exist. Robo-advisors like Betterment and Wealthfront automatically rebalance portfolios and handle tax-loss harvesting. Target-date funds automatically rebalance and gradually shift allocation over time. Most 401(k) plans offer an automatic rebalancing feature. For self-directed investors, tools like Personal Capital, Morningstar Portfolio X-Ray, or a simple spreadsheet can track drift and signal when rebalancing is needed.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 7: Portfolio Rebalancing -- The Discipline That Pays"]

**Horace:** Welcome back everyone. Today we are covering a topic that might sound boring but is genuinely one of the most important things you can do as an investor. We are talking about portfolio rebalancing. And by the end of this video, you will understand why it is a systematic way to buy low and sell high without needing any market-timing skill.

**Stella:** Okay, I will be honest, Horace. When I hear "rebalancing," I think of someone checking a spreadsheet and moving tiny amounts of money around. How much difference can it really make?

**Horace:** Let me give you a real example that will change how you think about this. Imagine it is January 2008. You have a $500,000 portfolio, split 60/40 between stocks and bonds. By September 2008, the financial crisis has hammered stocks. Your portfolio has drifted to something like 45% stocks and 55% bonds because stocks have fallen so much.

**Stella:** That sounds terrifying. I think most people would want to sell their remaining stocks at that point.

**Horace:** Exactly -- and that is what millions of investors did. They panicked and sold. But what does the rebalancing rule tell you to do?

[VISUAL: Split screen showing a panicking investor on one side and a calm investor checking their allocation spreadsheet on the other]

**Stella:** If your target is 60/40 and you have drifted to 45/55... your rebalancing rule says to sell bonds and buy more stocks.

**Horace:** Right. Buy stocks in the middle of a financial crisis. Sell bonds when they feel like the only safe place. That is absolutely gut-wrenching. But here is what happened to the investor who followed the rebalancing discipline: they bought stocks near the bottom. When the market recovered, those cheap shares produced enormous gains. The rebalancing investor recovered to their pre-crisis portfolio value roughly a year faster than the investor who froze.

**Stella:** A full year faster? Just from following a mechanical rule?

**Horace:** Just from following a mechanical rule. No genius required. No market-timing required. Just the discipline to do what your rebalancing policy tells you, especially when it feels wrong.

[ANIMATION: animation/week07_rebalancing_demo.py - Animated visualization showing two portfolio bars side by side over time. The "rebalanced" portfolio periodically adjusts back to 60/40, while the "drifted" portfolio gradually becomes dominated by whatever asset class performed best. The animation runs through a simulated market cycle showing how the rebalanced portfolio recovers faster after a crash because it bought stocks at lower prices.]

**Stella:** Okay, you have my attention. Let us start from the basics. What exactly is rebalancing?

**Horace:** At its simplest, rebalancing is bringing your portfolio back to its target allocation. You start with a plan -- say 60% stocks, 40% bonds. Over time, as stocks and bonds earn different returns, the actual percentages drift. Rebalancing means selling some of what went up and buying some of what went down to restore your original targets.

**Stella:** So if stocks have a great year and I drift to 70% stocks, I sell stocks and buy bonds to get back to 60/40?

**Horace:** Exactly.

[VISUAL: Animated pie chart morphing from 60/40 to 70/30 as stocks rise, then snapping back to 60/40 when "rebalance" button is pressed]

**Stella:** But am I not selling my winners? That seems counterintuitive.

**Horace:** It does, and that is precisely why it works. Think about what you are doing mechanically. After stocks have risen a lot, they are relatively expensive. After bonds have lagged, they are relatively cheap. By selling stocks and buying bonds, you are selling high and buying low. You are taking profits on the expensive asset and deploying them into the cheap one.

**Stella:** That is the holy grail of investing -- buy low, sell high. And you are telling me there is a mechanical rule that does it automatically?

**Horace:** That is exactly what I am telling you. And it works in reverse too. When stocks crash, they become cheap. Bonds, which usually hold up during crashes, become the expensive asset. Rebalancing forces you to sell the expensive bonds and buy the cheap stocks. Again -- buy low, sell high.

**Stella:** But that sounds psychologically really hard. Buying stocks when they are crashing?

**Horace:** It is extremely hard. And that is why having a written rebalancing policy is so important. You make the rule when you are calm and rational. Then when markets are in chaos, you follow the rule instead of your emotions. The rule does not have emotions. The rule does not watch CNBC. The rule just does math.

[VISUAL: A "rebalancing policy" document with key terms highlighted: target allocation, rebalancing bands, review frequency]

**Stella:** Makes sense. So how often should I actually rebalance?

**Horace:** This is one of the most commonly asked questions, and the good news is that the research shows it does not matter that much. What matters far more is that you rebalance at all. But let me walk you through the main approaches.

[VISUAL: Three columns labeled "Calendar," "Threshold," and "Hybrid," each with bullet points appearing as Horace describes them]

**Horace:** The first approach is calendar rebalancing. You pick a schedule -- monthly, quarterly, annually -- and on that date, you check your allocation and rebalance if needed. Annual rebalancing is the simplest and works surprisingly well.

**Stella:** Why not monthly? Would not more frequent be better?

**Horace:** Intuitively you would think so, but no. Vanguard did a comprehensive study and found that the difference between monthly, quarterly, and annual rebalancing is tiny -- maybe a few hundredths of a percent in return, and slightly lower volatility. But monthly rebalancing generates far more transactions and tax events, especially in taxable accounts. You are paying a real cost for an almost invisible benefit.

**Stella:** So annual is the sweet spot?

**Horace:** Annual is great for simplicity. But the second approach is threshold rebalancing, which many professionals prefer. Instead of rebalancing on a fixed date, you rebalance whenever any asset class drifts beyond a set band -- typically 5 percentage points from target.

**Stella:** So if my stock target is 60%, I would rebalance whenever stocks hit 65% or drop to 55%?

**Horace:** Exactly. The advantage is that you only rebalance when it actually matters. If the market barely moves for six months, you do not bother. But if there is a sudden crash or a big rally, the threshold catches it right away.

**Stella:** What about doing both?

**Horace:** Now you are thinking like a portfolio manager. The hybrid approach -- and this is what I recommend for most people -- is to check your allocation on a fixed schedule, say quarterly, but only rebalance if the drift exceeds your threshold. You get the efficiency of threshold rebalancing with the simplicity of a regular calendar reminder.

[VISUAL: Calendar showing quarterly check dates, with only two of four dates triggering a rebalance because the other two had drift below threshold]

**Stella:** That makes a lot of sense. Can you walk me through the actual math of a rebalancing trade?

**Horace:** Sure. Let us say you have $200,000 and your target is 60% stocks, 40% bonds. That means $120,000 in stocks and $80,000 in bonds. After a good year for stocks, your portfolio is worth $220,000, but now it is 68% stocks and 32% bonds -- meaning $149,600 in stocks and $70,400 in bonds.

[VISUAL: Two-column layout showing "Current" versus "Target" allocation with exact dollar amounts]

**Stella:** How do I calculate the trades?

**Horace:** Take the new total -- $220,000 -- and apply your target percentages. 60% of $220,000 is $132,000 for stocks. 40% of $220,000 is $88,000 for bonds. So you sell $149,600 minus $132,000 equals $17,600 of stocks, and buy $17,600 of bonds.

**Stella:** That is more than I expected. Almost $18,000 in trades.

**Horace:** Because the drift was significant -- 8 percentage points. That is why a 5% threshold is reasonable. If you had rebalanced when stocks first hit 65%, the trade would have been much smaller.

**Stella:** Got it. Now let me ask about something that was really fascinating in the reading -- the rebalancing bonus. Can a rebalanced portfolio actually outperform both of its components?

**Horace:** This is one of the most counterintuitive results in portfolio theory, and it is real. Let me walk you through the math.

[ANIMATION: animation/week07_rebalancing_demo.py - Animated simulation showing two assets that alternate between good and bad years (Asset A: +30%, -10%, +30%, -10% vs. Asset B: -10%, +30%, -10%, +30%). Three lines plotted simultaneously: Asset A alone, Asset B alone, and a 50/50 rebalanced portfolio. The rebalanced portfolio line steadily outperforms both individual assets, with annotations showing the rebalancing trades at each period.]

**Horace:** Imagine two assets. Asset A goes up 30% one year and down 10% the next. Asset B does the opposite -- down 10% then up 30%. Over four years, each asset individually turns $100 into about $137. That is about 8.2% annualized.

**Stella:** Okay, same return for both assets individually.

**Horace:** Now watch what happens with a 50/50 portfolio that rebalances annually. After year one, Asset A is up 30% and Asset B is down 10%. You rebalance -- selling some of the winner and buying some of the loser. Next year, the assets flip. The one you just bought more of goes up 30%, and the one you trimmed goes down 10%. You rebalance again.

**Stella:** You keep buying the one that is about to go up and selling the one that is about to go down!

**Horace:** Exactly. And after four years, the rebalanced portfolio turns $100 into about $172. That is over 14% annualized -- almost double the return of either asset individually!

**Stella:** That is incredible. Is this too good to be true?

**Horace:** In this stylized example, the bonus is exaggerated because the assets perfectly alternate. In real markets, the bonus is smaller -- typically half a percent to one and a half percent per year. But over twenty or thirty years of compounding, even half a percent per year adds up to a significant amount of additional wealth.

**Stella:** When is the bonus biggest?

**Horace:** Three conditions. First, the assets need to be volatile -- calm, steady assets do not produce much of a bonus. Second, the correlation between them should be low or negative -- they should not move in lockstep. Third, the assets should tend to mean-revert -- what goes down should eventually come back up.

**Stella:** Stocks and bonds fit that pretty well, right?

**Horace:** They fit reasonably well, especially during stress periods when bonds usually go up while stocks fall. The bonus is even larger for more diverse portfolios that include REITs, international stocks, and commodities, because you have more uncorrelated volatile asset pairs.

[VISUAL: Grid showing correlation matrix between major asset classes, with color coding from dark green (low/negative correlation = high rebalancing bonus) to red (high positive correlation = low rebalancing bonus)]

**Stella:** There has to be a catch though.

**Horace:** Good instinct. The rebalancing bonus disappears -- and rebalancing actually hurts you -- in strongly trending markets. If stocks go up every year for ten years straight, rebalancing means you keep selling stocks and buying bonds, giving up returns the whole way. You still maintained your risk level, which was the right thing to do from a risk management perspective, but the raw return was lower than if you had simply let stocks run.

**Stella:** So it is a tradeoff -- better risk management in exchange for potentially lower returns in one-directional markets.

**Horace:** Exactly. And since nobody knows in advance whether the next decade will be trending or choppy, maintaining the discipline is the right approach. You are optimizing for the full range of possible market environments, not just one scenario.

**Stella:** Let us talk about taxes. I have heard that rebalancing can create big tax bills. How do you handle that?

[VISUAL: Tax form with capital gains highlighted, transitioning to a list of tax-efficient strategies]

**Horace:** This is critical, especially for taxable accounts. Every time you sell an asset that has gained value, you owe capital gains tax. If you held it less than a year, the gains are taxed at your ordinary income rate -- up to 37%. If you held it more than a year, you get the lower long-term capital gains rate of 15% or 20%.

**Stella:** So rebalancing can mean paying taxes every year on my gains?

**Horace:** In a taxable account, yes. But there are several strategies to minimize this. Strategy number one, and the best option: use new contributions. Instead of selling stocks to buy bonds, just direct your new money entirely into the underweight asset class. No selling means no taxes.

**Stella:** That is brilliant. What if my contributions are not enough to close the gap?

**Horace:** Strategy two: rebalance inside your tax-advantaged accounts. If you have an IRA or 401(k), trades inside those accounts are tax-free. Do your aggressive rebalancing there and leave your taxable account alone as much as possible.

**Stella:** What if I do not have enough in retirement accounts to rebalance?

**Horace:** Strategy three: tax-loss harvesting. When you sell assets at a loss, those losses offset your gains. So if you are selling some winning stocks and some losing stocks as part of rebalancing, the losses cancel out the gains and you may owe little or no tax.

**Stella:** And strategy four?

**Horace:** Use dividends and interest. Instead of automatically reinvesting stock dividends back into stocks, direct them to your underweight asset class. If bonds are underweight, let your stock dividends flow into bonds. It is a slow form of rebalancing, but it is tax-efficient because you are redirecting income, not selling positions.

[VISUAL: Flowchart showing the tax-efficiency hierarchy -- try contributions first, then retirement accounts, then tax-loss harvesting, then dividends, and only as a last resort sell assets with gains]

**Stella:** What about this idea of holding the whole bond allocation in your IRA and the whole stock allocation in your taxable account?

**Horace:** That is asset location, and it is a separate but related topic. The idea is to hold the most tax-inefficient assets -- like bonds, which generate ordinary income from interest -- in tax-sheltered accounts. And hold the most tax-efficient assets -- like stock index funds, which generate mostly long-term capital gains -- in taxable accounts. When you combine smart asset location with smart rebalancing, you can significantly reduce your lifetime tax bill.

**Stella:** This is getting sophisticated. Let me ask a practical question: what about a more complex portfolio? I do not just hold stocks and bonds. I have US stocks, international stocks, bonds, and a small REIT position.

**Horace:** Great. The process is exactly the same, just with more line items. You compare each asset class's actual weight to its target weight, identify which are overweight and which are underweight, and then calculate trades. The nice thing about multi-asset rebalancing is that the sells fund the buys -- it is a closed system.

[VISUAL: Multi-asset portfolio dashboard showing target weights, actual weights, drift amounts, and required trades for each of six asset classes]

**Stella:** Do I need to get each asset class exactly to its target?

**Horace:** No, and this is an important practical point. Getting within a percentage point or two of target is good enough. Do not agonize over getting 60.00% versus 59.73%. The trading costs and effort of perfect precision are not worth the negligible difference in outcomes.

**Stella:** That is reassuring. What about people who say they do not need to rebalance because they have a target-date fund?

**Horace:** Target-date funds do rebalance internally -- that is one of their key features. If all your money is in a single target-date fund, you do not need to do anything. The fund company handles it. But if you have a target-date fund in your 401(k) plus individual accounts elsewhere, you need to think about rebalancing across all your accounts as a whole portfolio.

**Stella:** Makes sense. Can we talk about the psychological side? You mentioned that rebalancing after a crash is the hardest thing to do.

**Horace:** It is, and I want to be honest about how hard it is. In March 2020, when COVID crashed the market 34% in about a month, rebalancing meant buying stocks when it felt like the world was ending. Nobody knew if it was going to get worse. The news was terrifying. And yet, investors who mechanically rebalanced -- buying stocks with the proceeds from selling bonds that had risen in value -- made an enormous amount of money over the next twelve months.

[VISUAL: Timeline of March 2020 crash showing S&P 500 levels, with rebalancing trade points marked and subsequent recovery highlighted]

**Stella:** And people who panicked and sold?

**Horace:** Many of them locked in their losses. They sold stocks at the bottom, waited for things to "calm down," and by the time they felt comfortable buying again, the market had already recovered most of the loss. They sold low and bought high -- the exact opposite of what rebalancing does.

**Stella:** So the rebalancing rule protects you from yourself.

**Horace:** That might be its single most valuable property. The math is nice, the rebalancing bonus is real, but the behavioral protection -- preventing emotional decisions at the worst possible time -- that is worth its weight in gold.

[VISUAL: Two investor journeys plotted on the same chart -- the rebalancer who follows the rules through the crash and recovery, versus the emotional investor who sells at the bottom and buys back higher]

**Stella:** Let me ask about a scenario that I think would trip people up. What if one asset class keeps going up year after year? Like the 2010s when US stocks dominated. Are you just constantly selling your best performer?

**Horace:** Yes, and this is the one situation where rebalancing demonstrably costs you return. From 2010 to 2020, US stocks massively outperformed international stocks and bonds. An investor who rebalanced out of US stocks into international stocks and bonds every year earned less than an investor who simply held 100% US stocks.

**Stella:** So rebalancing hurt them?

**Horace:** It reduced their return compared to a concentrated stock portfolio, yes. But here is what you have to remember: nobody knew in advance that US stocks would dominate for a decade. And the investor who held 100% US stocks took on enormous risk. In 2018, the S&P 500 dropped almost 20%. In 2020, it dropped 34%. If that investor was 100% in stocks and panicked during one of those drops, they would have been far worse off than the rebalanced investor who had bonds cushioning the fall.

**Stella:** So it is an insurance cost.

**Horace:** Exactly. You might "overpay" for that insurance in hindsight during a strong bull market. But when the bear market hits -- and it always eventually does -- you are incredibly glad you paid the premium.

**Stella:** Let me try to summarize the practical steps someone should take.

**Horace:** Go for it.

**Stella:** First, define your target allocation based on your goals and risk tolerance. Second, set a rebalancing threshold -- something like 5 percentage points. Third, put a quarterly reminder in your calendar to check your allocation. Fourth, when you check, if anything is more than 5 points off target, calculate the trades needed. Fifth, try to do it tax-efficiently -- use contributions, tax-advantaged accounts, or tax-loss harvesting first. Sixth, execute the trades. Seventh, log what you did.

**Horace:** That is a perfect summary. I would add one thing: write this down as a formal policy before you need it. The Investor Policy Statement should include your target allocation, your rebalancing bands, your review frequency, and the priority order of tax-efficient methods. That way, when markets are panicking and you are tempted to deviate, you can pull out the document and follow the plan.

[VISUAL: Template of a simple Investment Policy Statement with the rebalancing section highlighted, showing sample text for target allocation, bands, and review frequency]

**Stella:** One more question. Is there a level of drift that should be an automatic emergency rebalance? Like if we have a 2008-style crash?

**Horace:** Some investors use a two-tier system. Normal bands at plus or minus 5 percentage points, reviewed quarterly. But if any asset class drifts by more than 10 percentage points in either direction -- whether due to a crash or a massive rally -- they rebalance immediately regardless of the calendar. That 10-point trigger catches rare but extreme events and ensures you are buying into crashes and selling into euphoria at exactly the moments when it matters most.

**Stella:** I love that. A normal rule and an emergency rule.

**Horace:** Exactly. And the beauty is, once you have these rules in place, investing becomes a lot less stressful. You do not have to agonize over "should I buy or sell right now?" The rules tell you. You just follow them.

[VISUAL: Summary card with five key takeaways:
1. Rebalancing is a systematic way to buy low and sell high
2. Annual or quarterly with a 5% threshold works for most investors
3. The rebalancing bonus adds 0.5-1.5% per year in volatile markets
4. Use tax-efficient methods: contributions first, tax-advantaged accounts second
5. Write down your rebalancing policy before you need it]

**Stella:** To summarize today's lesson. Rebalancing is not optional, it is fundamental. It keeps your risk on target, forces you to buy low and sell high, and protects you from your own emotions. The specific frequency matters less than the commitment to doing it at all.

**Horace:** Perfectly said. And if you only remember one thing from today: your rebalancing rule is most valuable at exactly the moments when it is hardest to follow. That is not a bug -- that is the feature.

**Stella:** Next week, we are going to learn how to read financial statements -- the building blocks of understanding any company. If you want to know whether a business is actually making money or just pretending to, you will not want to miss it.

**Horace:** See you then.

[VISUAL: End screen with subscribe button and links to previous lessons]

---
