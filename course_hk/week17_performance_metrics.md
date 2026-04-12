<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 17: Performance Metrics - Volatility, Drawdowns, and Risk-Adjusted Returns

---

## Reading Section

### a) Why This Is Important

You just finished a year of investing. Your portfolio went up 15%. Is that good? The honest answer is: you have no idea, unless you know how much risk you took to get there.

Consider two fund managers. Manager A returned 15% while taking wild swings -- her portfolio dropped 40% in March before roaring back. Manager B also returned 15% but with much smoother performance -- the worst monthly decline was 4%. Most investors would strongly prefer Manager B, even though the headline return is identical. The difference is risk-adjusted performance, and it is how professionals actually evaluate investment skill.

This matters for several critical reasons:

1. **Raw returns are meaningless in isolation.** A 20% return sounds great until you learn the market returned 25%, or that you took twice the risk to earn it. Performance metrics give you the context to evaluate whether you are being adequately compensated for the risks you bear.

2. **Drawdowns determine whether you actually capture returns.** A strategy that drops 50% before recovering to earn 12% annually might look good on paper, but most human beings will panic and sell at the bottom. Understanding drawdowns helps you choose strategies you can actually stick with.

3. **You cannot improve what you cannot measure.** If you do not systematically track your performance using proper metrics, you will never know whether your investment decisions are adding or subtracting value compared to simply buying an index fund.

4. **Time-weighted vs. money-weighted returns affect how you evaluate yourself.** The return your portfolio shows depends on how you calculate it. Using the wrong method leads to incorrect conclusions about your investment skill.

5. **Professional credibility demands proper measurement.** If you ever manage money for others, discuss investments with advisors, or even evaluate your own 401(k) options, you need to speak the language of risk-adjusted performance.

This lesson gives you the complete toolkit for evaluating investment performance the way professionals do -- from basic volatility to sophisticated risk-adjusted metrics like the Sharpe and Sortino ratios, through drawdown analysis and the critical distinction between how you measure returns.

---

### b) What You Need to Know

#### 1. Volatility -- The Standard Measure of Risk

Volatility measures how much returns bounce around their average. Technically, it is the standard deviation of returns. A stock that returns 10% every year like clockwork has zero volatility. A stock that swings between -30% and +50% has high volatility.

**The Math (Simplified)**

```
CALCULATING VOLATILITY
======================

Step 1: Collect periodic returns (monthly is standard)
Step 2: Calculate the average return
Step 3: Measure how far each return deviates from the average
Step 4: Square each deviation (to eliminate negatives)
Step 5: Average the squared deviations (this is the variance)
Step 6: Take the square root (this is the standard deviation)

Example with 6 monthly returns:
Returns: +3%, -2%, +5%, -1%, +4%, +3%
Average: +2%

Deviations from average:
+3% - 2% = +1%    -> squared: 0.0001
-2% - 2% = -4%    -> squared: 0.0016
+5% - 2% = +3%    -> squared: 0.0009
-1% - 2% = -3%    -> squared: 0.0009
+4% - 2% = +2%    -> squared: 0.0004
+3% - 2% = +1%    -> squared: 0.0001

Variance = (0.0001+0.0016+0.0009+0.0009+0.0004+0.0001) / 6
         = 0.000667

Monthly Std Dev = sqrt(0.000667) = 2.58%
Annual Std Dev  = 2.58% x sqrt(12) = 8.94%
```

**Key insight:** Volatility is annualized by multiplying monthly standard deviation by the square root of 12 (not by 12). This comes from the mathematical properties of independent random variables.

**Typical Volatility Ranges**

```
ANNUAL VOLATILITY BY ASSET CLASS
==================================

Asset Class              Typical Annual Vol    Range
-----------              ------------------    -----
Money market / T-Bills       0.5 - 1%          Very low
Investment grade bonds       3 - 7%            Low
High yield bonds             8 - 14%           Moderate
Balanced portfolio (60/40)   8 - 12%           Moderate
US large cap stocks         14 - 18%           Moderate-High
US small cap stocks         18 - 25%           High
International developed     15 - 22%           High
Emerging market stocks      20 - 30%           High
Individual stocks           25 - 60%+          Very High
Commodities                 15 - 30%           High
Cryptocurrency              50 - 100%+         Extreme

VOLATILITY SCALE
|---------|---------|---------|---------|---------|
0%        10%       20%       30%       50%      100%
Treasury   Bonds     S&P 500   EM       Crypto
Bills                         Stocks
```

**Why Volatility Is Imperfect as a Risk Measure**

Volatility treats upside and downside moves equally. If a stock jumps 20% in a month, that increases measured volatility -- but no investor considers a big gain to be "risk." This limitation is exactly why metrics like the Sortino ratio exist, which we will cover later.

---

#### 2. Drawdowns -- The Risk Metric That Matters Most to Real Investors

A drawdown measures the decline from a peak to a subsequent trough. It answers the question every investor really cares about: "How much did I lose at the worst point?"

```
DRAWDOWN ANATOMY
================

Portfolio   $100  $110  $105  $95  $80  $85  $90  $100  $115  $108
Value

                   Peak
                   $110
                    |
                    +----+
                         |
                    +----+----+
                              |
                    +---------+----+
                                   |  Maximum Drawdown
                    +--------------+  = ($110-$80)/$110
                              $80  |  = -27.3%
                              Trough
                                   |
                    +--------------+----+
                                        |
                    +-------------------+----+
                                             |
                    +------------------------+----+
                                                   | Recovery!
                                            $110 = | New Peak
                                                   |
                                             +-----+----+
                                                        |
                                                  $115  | New ATH
```

**Key Drawdown Metrics**

```
DRAWDOWN METRICS DASHBOARD
============================

Metric                    Definition                          Why It Matters
------                    ----------                          --------------
Maximum Drawdown (MDD)    Largest peak-to-trough decline      Worst-case pain
Recovery Time             Time from trough back to peak       How long you suffer
Drawdown Duration         Peak to peak (includes recovery)    Total disruption
Average Drawdown          Mean of all drawdowns               Typical experience
Drawdown Frequency        How often drawdowns > X% occur      How often it hurts
Calmar Ratio              Ann. Return / Max Drawdown          Return per unit of
                                                              worst-case risk
```

**Historical Maximum Drawdowns -- S&P 500**

```
MAJOR S&P 500 DRAWDOWNS
=========================

Event                    Peak-to-Trough    Duration     Recovery Time
-----                    --------------    --------     -------------
Great Depression         -86.2%            2.8 years    25.2 years
1973-74 Oil Crisis       -48.2%            1.8 years     3.2 years
Black Monday 1987        -33.5%            2 months      1.9 years
Dot-Com Crash            -49.1%            2.5 years     7.0 years
Great Fin. Crisis 2008   -56.8%            1.4 years     5.3 years
COVID Crash 2020         -33.9%            1 month       5 months
2022 Bear Market         -25.4%            9 months      2+ years

KEY INSIGHT: The deeper the drawdown, the more you need
to recover. A 50% loss requires a 100% gain to break even.

LOSS vs. GAIN NEEDED TO RECOVER
================================
Loss     Gain Needed     |  Loss     Gain Needed
-----    -----------     |  -----    -----------
-10%     +11.1%          |  -40%     +66.7%
-20%     +25.0%          |  -50%     +100.0%
-25%     +33.3%          |  -60%     +150.0%
-30%     +42.9%          |  -75%     +300.0%
-33%     +50.0%          |  -90%     +900.0%
```

**Why maximum drawdown matters more than volatility to most investors:** Volatility is an abstract statistical concept. Drawdown is concrete. When your $500,000 retirement portfolio drops to $250,000, you feel that in your gut. The behavioral consequences -- panic selling, sleepless nights, abandoning your strategy at the worst time -- are driven by drawdowns, not standard deviations.

---

#### 3. The Sharpe Ratio -- The Gold Standard of Risk-Adjusted Returns

Named after Nobel laureate William Sharpe, this ratio measures how much excess return you earn per unit of volatility. It is the most widely used risk-adjusted performance metric in finance.

**Formula:**

```
                    Rp - Rf
Sharpe Ratio = ─────────────
                    sigma_p

Where:
  Rp      = Portfolio return (annualized)
  Rf      = Risk-free rate (e.g., T-bill rate)
  sigma_p = Portfolio standard deviation (annualized)
```

**Worked Example:**

```
SHARPE RATIO EXAMPLE
=====================

Portfolio A:
  Return:       12%
  Risk-free:     4%
  Volatility:   16%
  Sharpe = (12% - 4%) / 16% = 0.50

Portfolio B:
  Return:        9%
  Risk-free:     4%
  Volatility:    6%
  Sharpe = (9% - 4%) / 6% = 0.83

Portfolio B has a LOWER return but a HIGHER Sharpe Ratio.
Per unit of risk taken, Portfolio B was more efficient.

VISUAL INTERPRETATION
======================

Return
  ^
14|                    * A (12%, 16% vol)
12|                  /
10|               /
 9|          * B (9%, 6% vol)
  |        /
 6|      /
 4|----*----> Risk-free rate (4%)
 2|
  +-----|-----|-----|-----|------> Volatility
  0     5    10    15    20

The slope of the line from the risk-free rate to each
portfolio IS the Sharpe ratio. Steeper = better.
```

**Interpreting Sharpe Ratios**

```
SHARPE RATIO GUIDELINES
========================

Sharpe Ratio    Interpretation
------------    ---------------
< 0             Worse than risk-free (why bother?)
0.0 - 0.4       Sub-par risk-adjusted returns
0.4 - 0.7       Acceptable (typical for equity markets)
0.7 - 1.0       Very good
1.0 - 1.5       Excellent (top quartile managers)
1.5 - 2.0       Outstanding (rare)
> 2.0           Suspicious (too good -- check for data errors,
                survivorship bias, or hidden risks like tail risk)

Historical Sharpe Ratios (approximate):
  S&P 500 long-term:          0.4 - 0.5
  60/40 balanced:             0.5 - 0.6
  Warren Buffett (Berkshire):  ~0.76
  Renaissance Medallion Fund:  ~2.0+ (but with massive leverage)
```

---

#### 4. The Sortino Ratio -- Fixing the Sharpe Ratio's Biggest Flaw

The Sharpe ratio penalizes all volatility equally. But investors do not mind upside volatility -- they only care about losses. The Sortino ratio fixes this by using only downside deviation in the denominator.

**Formula:**

```
                    Rp - Rf
Sortino Ratio = ─────────────
                 Downside Dev

Where:
  Downside Deviation = Standard deviation of ONLY negative returns
  (returns below the risk-free rate or a target return)
```

**Why It Matters:**

```
SHARPE vs. SORTINO: WHEN THEY DIVERGE
=======================================

                 Portfolio C      Portfolio D
                 -----------      -----------
Return           15%              15%
Volatility       20%              20%
Sharpe Ratio     0.55             0.55   <-- Identical!

But look closer at the return distribution:

Portfolio C (Symmetric returns):
  Positive months:  +4% average, 12 months
  Negative months:  -4% average, 12 months
  Downside Dev:     ~14%
  Sortino:          0.79

Portfolio D (Positive skew):
  Positive months:  +6% average, 14 months
  Negative months:  -2% average, 10 months
  Downside Dev:     ~7%
  Sortino:          1.57   <-- MUCH better!

Portfolio D has the SAME Sharpe but DOUBLE the Sortino
because its volatility comes from upside moves, not losses.

RETURN DISTRIBUTION COMPARISON
================================

Portfolio C (Symmetric):
  Frequency
    |      ***
    |    ***   ***
    |  ***       ***
    | **           **
    |*               *
    +---|----|----|---|--->
    -10  -5   0   5  10   Return %

Portfolio D (Positive Skew):
  Frequency
    |         ***
    |       ***  **
    |     ***      *
    |    **         *
    |  **            *
    +---|----|----|---|--->
    -10  -5   0   5  10   Return %
```

**When to Use Which:**

- **Sharpe Ratio:** Good general-purpose measure; standard in the industry; comparable across studies and datasets.
- **Sortino Ratio:** Better when comparing strategies with different return distributions, especially those with asymmetric payoffs (options strategies, trend following, etc.).

---

#### 5. Other Important Risk-Adjusted Metrics

```
RISK-ADJUSTED METRICS REFERENCE TABLE
========================================

Metric          Formula                       Best For
------          -------                       --------
Treynor Ratio   (Rp - Rf) / Beta             Diversified portfolios
                                              (uses systematic risk only)

Information     (Rp - Rb) / Tracking Error    Active managers vs.
Ratio                                         benchmark

Calmar Ratio    Ann. Return / Max Drawdown    Evaluating tail risk
                                              exposure

Omega Ratio     Probability-weighted          Complex strategies
                gains / losses                with non-normal returns

Jensen's Alpha  Rp - [Rf + Beta*(Rm - Rf)]   True skill after
                                              adjusting for market risk

M-Squared       Sharpe * Market Vol + Rf      Converts Sharpe to
(M2)                                          an equivalent return %
```

```
CHOOSING THE RIGHT METRIC
============================

Question You're Asking              Use This Metric
-----------------------              ---------------
"Am I being compensated for risk?"   Sharpe Ratio
"Am I being compensated for          Sortino Ratio
 downside risk specifically?"
"Did I beat my benchmark after       Information Ratio
 adjusting for tracking error?"       / Jensen's Alpha
"What is my worst-case scenario?"    Maximum Drawdown
                                      / Calmar Ratio
"How much return per unit of         Treynor Ratio
 market risk (beta) did I earn?"
"Can I compare two strategies        M-Squared
 directly in return terms?"
```

---

#### 6. Time-Weighted vs. Money-Weighted Returns

This is one of the most misunderstood and most consequential distinctions in performance measurement. The method you choose can make the same portfolio look brilliant or mediocre.

**Time-Weighted Return (TWR)**

Time-weighted return eliminates the impact of cash flows (deposits and withdrawals). It measures the return of the strategy itself, as if $1 had been invested for the entire period with no additions or withdrawals.

**Money-Weighted Return (MWR) / Internal Rate of Return (IRR)**

Money-weighted return accounts for the timing and size of cash flows. It measures the return actually experienced by the investor, given when they added or withdrew money.

```
TWR vs. MWR: THE CRITICAL DIFFERENCE
=======================================

Scenario: You invest in a fund over 2 years.

Year 1: Fund returns +30%
Year 2: Fund returns -10%

Case A: You invest $10,000 at the start, add nothing.
                                             TWR     MWR
  Start of Year 1:  $10,000                  
  End of Year 1:    $13,000 (+30%)           
  End of Year 2:    $11,700 (-10%)           
                                             +8.2%   +8.2%
                                             (Same because no
                                              additional flows)

Case B: You invest $10,000 at start, add $50,000
        at start of Year 2 (chasing performance).
                                             TWR     MWR
  Start of Year 1:  $10,000                  
  End of Year 1:    $13,000 (+30%)           
  Add:              $50,000                  
  Start of Year 2:  $63,000                  
  End of Year 2:    $56,700 (-10%)           
                                             +8.2%   -4.6%

SAME fund, SAME returns, but the INVESTOR lost money
because they added capital right before the down year.

Case C: You invest $50,000 at start, withdraw $40,000
        at end of Year 1 (selling after gains).
                                             TWR     MWR
  Start of Year 1:  $50,000                  
  End of Year 1:    $65,000 (+30%)           
  Withdraw:         $40,000                  
  Start of Year 2:  $25,000                  
  End of Year 2:    $22,500 (-10%)           
                                             +8.2%   +20.8%

Now the investor's MWR is HIGH because they were heavily
invested during the good year and lightly invested during
the bad year.
```

```
WHEN TO USE EACH METHOD
=========================

Time-Weighted Return (TWR)         Money-Weighted Return (MWR/IRR)
--------------------------         --------------------------------
Evaluating a fund MANAGER          Evaluating YOUR personal result
  (did the strategy work?)           (how did I actually do?)

Comparing fund to benchmark        Evaluating timing of your
  (apples to apples)                contributions/withdrawals

Industry standard for              Appropriate for private equity,
  mutual fund reporting              real estate (irregular flows)

Removes the effect of              Captures the effect of
  investor behavior                  investor behavior

Used by: Morningstar,              Used by: Personal financial
  fund fact sheets,                  planning, PE/VC funds,
  performance composites             estate valuation

CALCULATION VISUALIZATION
==========================

Time-Weighted (chain-linking sub-period returns):

  Period 1    Period 2    Period 3
  +10%        -5%         +8%
    |           |           |
    v           v           v
  (1.10)  x  (0.95)  x  (1.08)  =  1.1286
                                     = +12.86% TWR

Money-Weighted (finding the rate that equates flows):

  Time 0     Time 1      Time 2      Time 3
  -$1000     -$500       +$200       +$1600
    |          |           |           |
    v          v           v           v
  PV of all cash flows at rate r must = 0
  Solve for r (this IS the IRR / MWR)
```

**The Behavior Gap**

This distinction reveals one of the most important findings in all of finance: the average investor earns far less than the average fund. DALBAR's annual studies consistently show that while the S&P 500 has averaged roughly 10% per year, the average equity fund investor has earned only about 5-6%. The gap comes from bad timing -- investors add money after gains (buying high) and pull money after losses (selling low).

```
THE BEHAVIOR GAP
=================

       Fund Return (TWR)                  Investor Return (MWR)
       ==================                 =====================
           +10.0%                              +5.8%
              |                                   |
              |    <--- Behavior Gap --->          |
              |          ~4.2% annually            |
              |                                   |

Sources of the gap:
  - Chasing hot funds after big gains
  - Panic selling during drawdowns
  - Market timing attempts
  - Overtrading
  - Moving to cash at wrong times
```

---

#### 7. Putting It All Together -- A Performance Dashboard

When evaluating any investment, strategy, or your own portfolio, you should examine multiple metrics together. No single number tells the full story.

```
SAMPLE PERFORMANCE DASHBOARD
===============================

Metric                  Your       60/40      S&P
                       Portfolio   Benchmark   500
-----                  ---------  ---------   ----
Annualized Return       9.8%       8.2%       10.5%
Annualized Volatility  11.3%       9.4%       15.2%
Sharpe Ratio            0.69       0.60        0.53
Sortino Ratio           1.02       0.85        0.72
Maximum Drawdown       -18.5%     -22.1%      -33.9%
Calmar Ratio            0.53       0.37        0.31
Worst Month            -7.2%      -8.5%      -12.4%
Best Month             +6.8%      +7.1%      +12.7%
% Positive Months       62%        61%         63%
Beta to S&P              0.65       0.58        1.00
Alpha (annualized)      +1.8%      +0.4%       0.0%
Tracking Error           6.2%       7.4%        0.0%
Information Ratio        0.29       0.05        N/A

INTERPRETATION:
Your portfolio earned slightly less than the S&P 500
but with much less risk. On a risk-adjusted basis
(Sharpe, Sortino, Calmar), you outperformed both
benchmarks. The lower drawdown means you were more
likely to stay invested through turbulence.
```

---

#### 8. Rolling Returns and Time-Horizon Analysis

A single performance number can hide tremendous variability depending on the time period chosen. Rolling return analysis solves this by showing performance over every overlapping period of a given length.

```
ROLLING 3-YEAR ANNUALIZED RETURN (CONCEPTUAL)
================================================

Start each new 3-year window one month forward:

Window 1:  Jan 2015 - Dec 2017  ->  Ann. Return: +11.2%
Window 2:  Feb 2015 - Jan 2018  ->  Ann. Return: +10.8%
Window 3:  Mar 2015 - Feb 2018  ->  Ann. Return: +12.1%
...
Window N:  Jan 2021 - Dec 2023  ->  Ann. Return:  +7.3%

Plot all windows:

Return
  20%|                  *
  15%|        * *    *     *
  10%|  *  *       *         *  *    *
   5%|                              *  *
   0%|
  -5%|
     +--|--|--|--|--|--|--|--|--|--|--|---> Time
    2015              2019              2023

This shows the RANGE of experiences investors had,
not just the endpoint-to-endpoint number.
```

---

### c) Common Misconceptions

**Misconception 1: "Higher returns always mean better performance."**

Reality: Returns must always be evaluated relative to the risk taken. A fund that returns 15% with 30% volatility is not superior to one returning 10% with 10% volatility. The second fund has a Sharpe ratio of roughly 0.60 (assuming a 4% risk-free rate) versus about 0.37 for the first. Professionals would choose the lower-return fund and use modest leverage to achieve the same return with less total risk.

**Misconception 2: "Volatility and risk are the same thing."**

Reality: Volatility is one measure of risk, but it misses important dimensions. A stock that steadily loses 2% per month has low volatility but catastrophic risk. Conversely, a stock that is flat for 11 months and then jumps 30% in December has high volatility but would be a wonderful investment. True risk includes the probability of permanent capital loss, liquidity risk, concentration risk, and drawdown severity -- none of which are fully captured by standard deviation.

**Misconception 3: "A Sharpe ratio above 1.0 is easy to achieve."**

Reality: A sustained Sharpe ratio above 1.0 is genuinely exceptional. The long-run Sharpe ratio of the US equity market is roughly 0.4 to 0.5. Warren Buffett's Berkshire Hathaway has achieved approximately 0.76 over decades. If someone claims a Sharpe ratio above 2.0 over a long period, investigate carefully for survivorship bias, data mining, illiquid holdings marked at stale prices, or hidden tail risk.

**Misconception 4: "Maximum drawdown is a one-time event you can just endure."**

Reality: The maximum drawdown you have experienced so far is likely not the worst you will ever experience. Markets regularly produce drawdowns that exceed anything seen in recent history. Furthermore, the psychological impact of living through a drawdown is far more intense than any backtest suggests. Watching your life savings shrink by 40% in real-time, with terrifying headlines every day, is qualitatively different from seeing a -40% number in a table.

**Misconception 5: "My brokerage account return is my actual performance."**

Reality: Most brokerage accounts report time-weighted returns, which ignore the impact of your deposits and withdrawals. Your actual experience (money-weighted return) can be dramatically different. If you added money before a decline or withdrew money before a rally, your personal return is worse than what your account statement shows.

**Misconception 6: "Past Sharpe ratios predict future Sharpe ratios."**

Reality: Risk-adjusted metrics are far more stable than raw returns, but they are not fixed. A strategy's Sharpe ratio can change dramatically when market regimes shift. A strategy designed for low-rate environments may have a terrible Sharpe ratio when rates rise. Always understand why a strategy works, not just that it worked historically.

---

### d) Common Questions and Answers

**Q1: How many months of data do I need before performance metrics are meaningful?**

A: At minimum, you want 36 months (3 years) for basic statistics like Sharpe ratio and volatility to be somewhat reliable. For drawdown analysis, you ideally want data covering at least one full market cycle (bull and bear), which typically means 7-10 years. For very high confidence, 15-20 years of data is preferred. Be deeply skeptical of any strategy that shows only 12 months of performance.

**Q2: Should I use daily, weekly, or monthly returns to calculate volatility and Sharpe?**

A: Monthly returns are the standard for most performance analysis. Daily returns can be noisy and may overstate volatility due to bid-ask spreads and microstructure effects. Weekly returns are a reasonable middle ground. For comparability with published statistics and benchmarks, use monthly data and annualize. If using daily data, annualize by multiplying daily standard deviation by the square root of 252 (trading days per year).

**Q3: My portfolio has a negative Sharpe ratio. What does that mean?**

A: It means your portfolio returned less than the risk-free rate. You would have been better off in Treasury bills. This is not uncommon during bear markets -- even the S&P 500 has negative Sharpe ratios over certain multi-year periods. If your Sharpe ratio is consistently negative over a full market cycle (5+ years), you should seriously reconsider your strategy.

**Q4: What is a good maximum drawdown to target?**

A: This depends entirely on your risk tolerance, but a useful rule of thumb: your maximum acceptable drawdown should be roughly twice the return you expect. If you target 8% annual returns, be prepared for drawdowns of 15-20%. If you target 12% annual returns, be prepared for drawdowns of 25-30% or more. The key is to set this threshold before you invest, not during a drawdown when emotions dominate.

**Q5: Why do financial advisors show time-weighted returns instead of money-weighted?**

A: Time-weighted returns are used because they isolate manager skill from client behavior. If an advisor's strategy returned 10% (TWR) but a particular client earned only 3% (MWR) because they panicked and sold during a dip, the advisor's strategy still performed well -- the client's behavior was the problem. TWR is fair to the manager; MWR is fair to the client. You should demand to see both.

**Q6: How do hedge funds report such high Sharpe ratios?**

A: Several factors inflate hedge fund Sharpe ratios: (1) Survivorship bias -- failed funds are removed from databases, leaving only winners. (2) Illiquid holdings are often marked at stale or manager-estimated prices, artificially smoothing returns and reducing measured volatility. (3) Some strategies involve selling insurance-like instruments that generate steady small gains but occasional catastrophic losses (hidden tail risk). (4) Leverage can boost returns without appearing in standard Sharpe calculations if not properly accounted for. Always look at the Sharpe ratio with skepticism for any strategy that involves illiquid assets or option-like payoffs.

**Q7: What is the Calmar ratio and why do some people prefer it?**

A: The Calmar ratio is annualized return divided by maximum drawdown. Some investors prefer it because maximum drawdown is a more tangible risk measure than standard deviation. A Calmar ratio above 1.0 means your annualized return exceeds your worst drawdown -- a good sign. Below 0.5 suggests you endured significant pain for modest returns. However, maximum drawdown is a single observation and is sample-dependent, which makes Calmar less statistically robust than Sharpe.

**Q8: How do I calculate my personal money-weighted return?**

A: You need a record of every deposit and withdrawal with dates. Then you solve for the internal rate of return (IRR) -- the discount rate that makes the present value of all cash flows (including the ending portfolio value) equal to zero. Most spreadsheet software has an IRR or XIRR function that does this automatically. XIRR is preferred because it handles irregular dates. Simply input negative values for money invested, positive values for money withdrawn or your ending balance, and the corresponding dates.

**Q9: Does rebalancing affect performance metrics?**

A: Yes, rebalancing affects all performance metrics. Regular rebalancing tends to reduce volatility (by keeping allocations from drifting toward riskier assets) and can improve the Sharpe ratio, particularly in sideways or mean-reverting markets. However, in strong trending markets, rebalancing sells winners and buys losers, which can reduce raw returns. The impact on drawdown is generally positive -- rebalanced portfolios typically experience smaller maximum drawdowns because they maintain diversification.

**Q10: Can two investors in the same fund have wildly different money-weighted returns?**

A: Absolutely. If Investor A put in $100,000 at inception and never touched it, and Investor B started with $10,000 but added $200,000 right before a 30% crash, their money-weighted returns would be vastly different despite owning the same fund. This is precisely why the distinction between TWR and MWR matters. The fund's performance (TWR) is the same for everyone. Each investor's experience (MWR) is unique.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 17: Performance Metrics - Volatility, Drawdowns, and Risk-Adjusted Returns"]

**Alex:** Welcome back everyone. Today we are talking about something that is absolutely critical for your success as an investor, but that most people get completely wrong. We are talking about how to actually measure investment performance.

**Sam:** This seems pretty straightforward, Alex. I look at my portfolio, I see it went up 15% this year, that is my performance, right?

**Alex:** And that right there is the mistake almost everyone makes. Let me ask you something. If I told you I made 15% last year, would you be impressed?

**Sam:** I mean, 15% sounds pretty good.

**Alex:** What if I told you that to make that 15%, my portfolio dropped 45% in the spring, I could not sleep for three months, and I nearly sold everything at the bottom?

**Sam:** That sounds terrifying. Okay, so the 15% does not tell the whole story.

**Alex:** Not even close. Today we are going to learn the metrics that professionals use to evaluate performance properly. We will cover volatility, drawdowns, the Sharpe ratio, the Sortino ratio, and one of the most misunderstood concepts in all of finance -- the difference between time-weighted and money-weighted returns.

[VISUAL: Agenda slide showing the five main topics with icons: a zigzag line for volatility, a falling arrow for drawdowns, a scale/balance for Sharpe, a half-scale for Sortino, and a clock vs. money bag for TWR vs. MWR]

**Sam:** Let us start from the beginning. When people talk about volatility, what exactly do they mean?

**Alex:** Volatility is simply a measure of how much returns bounce around. Technically, it is the standard deviation of returns. Think of it this way. Imagine you have two roads to get to the same destination, and both take the same time. Road A is a smooth highway. Road B is a roller coaster with huge hills and sharp turns. They get you to the same place, but the experience is very different.

**Sam:** I would definitely prefer Road A.

**Alex:** Most investors would. And in investing, the smooth road has low volatility and the roller coaster has high volatility. The S&P 500 typically has an annual volatility of about 15 to 16 percent. That means in a normal year, you should expect the market to fluctuate within a range of about 15% above or below the average return.

[ANIMATION: animation/week17_volatility.py - Two animated portfolio lines growing over the same 5-year period to the same ending value. Line A is smooth with gentle undulations. Line B zigzags wildly with large swings. Both reach the same final point. Labels show "Low Volatility: 8%" and "High Volatility: 25%". A final annotation appears: "Same return. Very different experience."]

**Sam:** So if the average return is 10% and volatility is 15%, the range of typical outcomes in a year would be negative 5% to positive 25%?

**Alex:** Roughly, yes. That is one standard deviation in each direction, which covers about two thirds of outcomes. Two standard deviations -- covering about 95% of outcomes -- would be negative 20% to positive 40%. That is why even in a normal environment, without any crisis, you can see the market drop 20% and it is completely within the realm of normal.

**Sam:** That is actually useful to know. So when the market drops 15%, that is just normal volatility, not necessarily a crisis.

**Alex:** Exactly. And this is where many investors go wrong. They see a 10 or 15 percent decline and they panic, thinking something is fundamentally broken. In reality, the market drops 10% or more roughly once every 18 months on average. It drops 20% or more about once every 4 to 5 years. These are features of equity investing, not bugs.

[VISUAL: Timeline from 1980 to present showing all S&P 500 corrections (10%+) and bear markets (20%+) plotted as vertical bars below the x-axis, demonstrating how frequent these events are. A rising line above shows the long-term upward trend despite the corrections.]

**Sam:** Okay, so volatility tells me about the bumpiness of the ride. But you mentioned something about volatility being an imperfect measure of risk?

**Alex:** Yes, and this is crucial. Volatility treats upside and downside moves identically. If your stock jumps 20% in a month, that increases its measured volatility. But nobody thinks of a big gain as risk, right?

**Sam:** No, that sounds great.

**Alex:** Exactly. This is the fundamental limitation of volatility as a risk measure. It penalizes you for good outcomes as much as bad ones. We will come back to this when we talk about the Sortino ratio, which fixes this problem. But first, let us talk about the risk metric that matters most to real human beings -- drawdowns.

**Sam:** What exactly is a drawdown?

**Alex:** A drawdown is the decline from a portfolio's peak value to its subsequent trough. It answers the question every investor actually cares about: how much did I lose from the top?

[VISUAL: Large animated chart showing a portfolio growing from $100,000. The line rises to a peak of $150,000, then drops to $105,000 (a 30% drawdown), then recovers to $160,000. Red shading fills the area between the peak and the trough, labeled "Maximum Drawdown: -30%". The recovery period is highlighted in yellow. Clear labels show "Peak", "Trough", "Drawdown Period", and "Recovery Period".]

**Alex:** There is a mathematical reality about drawdowns that most people do not intuitively grasp. If your portfolio drops 50%, you need a 100% gain just to get back to even. Not 50% -- 100%.

**Sam:** Wait, why 100%?

**Alex:** Because if you start with $100 and lose 50%, you have $50. Now you need to double from $50 to get back to $100. And doubling your money is a 100% gain. This asymmetry is devastating at large drawdown levels.

[ANIMATION: animation/week17_drawdown_recovery.py - Animated bar chart showing loss percentages on the left and required recovery gains on the right. Starts with small losses (-10% needs +11.1%) and progressively shows larger losses up to -90% needs +900%. The bars on the right grow exponentially while the bars on the left grow linearly, visually demonstrating the asymmetry. Each pair of bars animates in sequence with the recovery bar "growing" up dramatically.]

**Sam:** So a 75% loss needs a 300% gain to recover? That could take decades!

**Alex:** It can. The S&P 500 after the Great Depression did not recover to its 1929 peak until 1954 -- twenty-five years later. That is why Warren Buffett's first rule of investing is "never lose money" and the second rule is "never forget rule number one." He is not speaking literally -- all investors experience losses. He means that avoiding catastrophic drawdowns is the single most important thing you can do.

**Sam:** This is making me think differently about risk already. Okay, so how do we combine return and risk into a single number?

**Alex:** That brings us to the Sharpe ratio, which is arguably the most important metric in all of performance analysis. It was created by William Sharpe, who won the Nobel Prize in Economics.

[VISUAL: Photo of William Sharpe with the formula displayed prominently: Sharpe = (Rp - Rf) / sigma_p, with each component labeled: "Portfolio return minus Risk-free rate, divided by Portfolio volatility"]

**Alex:** The Sharpe ratio measures excess return per unit of risk. The numerator is your portfolio return minus the risk-free rate -- this is the extra return you earned for taking risk. The denominator is your volatility. The higher the ratio, the more efficiently you converted risk into return.

**Sam:** Can you walk me through a real example?

**Alex:** Of course. Let us say Portfolio A returned 14% with a volatility of 20%, and the risk-free rate is 4%. The Sharpe ratio is 14 minus 4, divided by 20, which equals 0.50. Now Portfolio B returned only 9% with a volatility of 8%. Its Sharpe is 9 minus 4 divided by 8, which equals 0.625.

**Sam:** So Portfolio B has a lower return but a higher Sharpe ratio?

**Alex:** Exactly. Portfolio B was more efficient with its risk. And here is the key insight. If Portfolio B used a little bit of leverage -- say borrowed at the risk-free rate and scaled up to the same volatility as Portfolio A -- it would produce a higher return than A. The Sharpe ratio tells you which strategy is fundamentally better, regardless of how much risk you choose to take.

[ANIMATION: animation/week17_sharpe_visual.py - A coordinate plane with volatility on x-axis and return on y-axis. The risk-free rate is marked at 4% on the y-axis. Two dots represent Portfolio A (20%, 14%) and Portfolio B (8%, 9%). Lines are drawn from the risk-free rate through each dot. Portfolio B's line is steeper (higher slope = higher Sharpe). An animated leverage slider shows Portfolio B sliding along its line to higher risk/return levels, eventually surpassing Portfolio A's return at the same risk level.]

**Sam:** That is elegant. So when comparing any two investments, the one with the higher Sharpe ratio is always better?

**Alex:** In theory, yes, assuming the returns are normally distributed and you can use leverage freely. In practice, there are complications. Returns are not always normally distributed -- they can have fat tails and skewness. And not everyone can use leverage. But as a general ranking tool, the Sharpe ratio is the industry standard.

**Sam:** What is a good Sharpe ratio?

**Alex:** The long-run Sharpe ratio of the US stock market is about 0.4 to 0.5. A 60/40 balanced portfolio is typically around 0.5 to 0.6. Anything above 0.7 is quite good. Above 1.0 is excellent -- you are in the top tier. And if someone tells you they have a Sharpe ratio above 2.0 over any extended period, be very, very skeptical.

**Sam:** Why skeptical?

**Alex:** Because sustained Sharpe ratios above 2.0 are almost unheard of in liquid markets. When you see them, it is usually because of one of a few things. The returns are calculated on illiquid assets marked at stale prices, which artificially smooths volatility. Or there is survivorship bias -- you are only seeing the fund that survived while the other 99 that used the same strategy blew up. Or the strategy is selling tail risk -- collecting small premiums that look like steady income until a catastrophe hits and wipes out years of gains in a week.

**Sam:** Like picking up pennies in front of a steamroller.

**Alex:** That is the classic metaphor, and it is perfect. The Sharpe ratio of picking up pennies in front of a steamroller looks amazing right up until the steamroller catches you.

[VISUAL: Illustrated metaphor showing someone picking up coins on a road with a steamroller approaching in the background, with a P&L chart below showing steady gains followed by a sudden catastrophic loss]

**Sam:** You mentioned earlier that the Sharpe ratio has a flaw because it treats upside volatility the same as downside volatility. How does the Sortino ratio fix this?

**Alex:** The Sortino ratio uses the same basic structure as the Sharpe -- excess return in the numerator -- but in the denominator, instead of total standard deviation, it uses only the downside deviation. That is, it only counts the volatility that comes from returns below your target, usually the risk-free rate.

**Sam:** So it ignores the good kind of volatility.

**Alex:** Exactly. Imagine two hedge funds. Both return 12% per year with the same Sharpe ratio. But Fund X achieves this with symmetric returns -- gains and losses are roughly equal in size. Fund Y achieves it by having many small gains and very few but slightly larger losses -- most of its volatility comes from the upside. The Sortino ratio would rate Fund Y much higher than Fund X, even though the Sharpe ratio says they are equal.

[VISUAL: Two return distribution histograms side by side. Fund X shows a symmetric bell curve. Fund Y shows a right-skewed distribution with a higher peak. Both have the same Sharpe ratio labeled, but Fund Y shows a much higher Sortino ratio. The downside portion of each distribution is highlighted in red, showing that Fund Y has much less downside area.]

**Sam:** When should I use the Sortino versus the Sharpe?

**Alex:** Use the Sharpe as your default -- it is the standard, everyone calculates it, and it is easy to compare across studies. Use the Sortino when you are comparing strategies that have very different return distributions. This is especially important for options strategies, trend following, and anything with asymmetric payoffs. A covered call strategy, for example, will look different on Sharpe versus Sortino because the distribution is truncated on the upside.

**Sam:** This brings up a question. What other metrics should I know about?

**Alex:** There are a few more worth knowing. The Calmar ratio divides annualized return by maximum drawdown -- it tells you how much return you earned per unit of worst-case pain. The Information ratio measures excess return over a benchmark divided by tracking error -- it is how active managers are evaluated. And Jensen's Alpha measures whether a portfolio beat what the Capital Asset Pricing Model predicted it should earn, given its level of market risk.

**Sam:** That is a lot of metrics. Do professionals really look at all of these?

**Alex:** Not all of them, but they typically look at a dashboard of metrics, not just one number. The standard professional analysis would include annualized return, volatility, Sharpe ratio, maximum drawdown, and sometimes Sortino and Calmar. Looking at multiple metrics gives you a three-dimensional picture of performance instead of a flat snapshot.

[VISUAL: Mock-up of a professional performance dashboard showing a portfolio vs. benchmark with all key metrics: return, volatility, Sharpe, Sortino, max drawdown, Calmar, beta, alpha, Information ratio. Color-coded green/red to show where the portfolio outperforms/underperforms.]

**Sam:** Alright, let us move to the last topic, which you said is one of the most misunderstood concepts in finance -- time-weighted versus money-weighted returns. What is the difference?

**Alex:** This is where it gets really interesting. Let me set up a scenario. Imagine a fund that returns plus 30% in Year 1 and minus 10% in Year 2.

**Sam:** Okay, so a great year followed by a bad year.

**Alex:** Right. Now imagine three different investors. Investor A puts in $10,000 at the start and does not touch it. Investor B puts in $10,000 at the start, but then adds $50,000 at the start of Year 2 because she was impressed by the 30% gain. Investor C starts with $50,000 and withdraws $40,000 at the end of Year 1 because she wanted to lock in profits.

**Sam:** They are all in the same fund, so they should have the same return, right?

**Alex:** The fund has the same return, yes. The time-weighted return, which ignores cash flows, is about 8.2% annualized for all three investors. But the money-weighted returns -- the actual returns these investors experienced -- are wildly different.

[ANIMATION: animation/week17_twr_mwr.py - Three animated portfolio simulations running simultaneously. Investor A shows a simple line growing 30% then declining 10%. Investor B shows a small line growing 30%, then a large cash deposit animates in, and the combined portfolio drops 10% on a much larger base -- ending animation shows the dollar loss prominently. Investor C shows a large line growing 30%, then a large cash withdrawal animates out, and the small remaining portfolio drops 10% on a small base -- ending animation shows the dollar gain prominently. Final screen shows all three money-weighted returns side by side with the identical time-weighted return.]

**Alex:** Investor A has the same TWR and MWR because she made no additional moves. Investor B, who added money before the decline, has a money-weighted return of roughly negative 4.6%. She actually lost money despite being in a fund that gained.

**Sam:** That is shocking.

**Alex:** And Investor C, who pulled money before the decline, has a money-weighted return of roughly positive 20.8%. She did phenomenally despite being in the same fund. Same fund, same performance, but three totally different investor experiences.

**Sam:** So the timing of when you add and remove money completely changes your result.

**Alex:** Completely. And this is not a contrived example. There is extensive academic research showing that the average investor earns substantially less than the funds they invest in. The DALBAR studies show that while the S&P 500 has averaged roughly 10% per year over the past 30 years, the average equity fund investor has earned only about 5 to 6%. That 4 percentage point gap is the "behavior gap."

[VISUAL: Bar chart showing "Fund Return" at approximately 10% next to "Investor Return" at approximately 5.5%, with the gap between them labeled "The Behavior Gap: ~4.2% per year lost to bad timing"]

**Sam:** Because people buy after things go up and sell after things go down.

**Alex:** Exactly. Fear and greed dominate investor behavior. When markets are roaring, everyone wants in -- they add money at the peaks. When markets crash, everyone wants out -- they pull money at the troughs. This is literally the opposite of buy low, sell high.

**Sam:** So when my brokerage account shows me my return, which one is it using?

**Alex:** Most brokerage accounts report time-weighted returns. This means the return number you see may not reflect your actual experience if you have been making deposits and withdrawals. If you want to know your true personal return, you need to calculate the money-weighted return using the XIRR function in a spreadsheet.

**Sam:** Which one is "right?"

**Alex:** Neither is right or wrong -- they answer different questions. Time-weighted return answers "did the investment strategy work?" Money-weighted return answers "did I personally make money?" For evaluating a fund manager, use TWR -- it is not fair to penalize them for when you chose to invest. For evaluating your own financial progress, use MWR -- it captures the reality of your decisions.

**Sam:** This has been incredibly eye-opening. So to summarize, I should not just look at returns -- I need to look at volatility, drawdowns, and risk-adjusted ratios like the Sharpe and Sortino. And I need to understand the difference between how well my strategy performed and how well I personally performed.

**Alex:** That is a perfect summary. Let me give you a practical takeaway. After every year, sit down and calculate these five things for your portfolio. One, your total return. Two, your portfolio's volatility. Three, your Sharpe ratio. Four, your maximum drawdown during the year. Five, your money-weighted return using XIRR.

[VISUAL: Checklist graphic showing "Annual Performance Review - 5 Must-Calculate Metrics" with the five items listed cleanly]

**Alex:** Compare your Sharpe ratio to a simple 60/40 benchmark. If your Sharpe is lower, your added complexity is not being rewarded. Compare your money-weighted return to your time-weighted return. If there is a big gap, your timing of deposits and withdrawals is hurting you, and you should consider automating contributions.

**Sam:** What if my Sharpe ratio is lower than the benchmark?

**Alex:** Then you need to honestly ask yourself whether your active decisions are adding value. Many investors discover that despite spending hours researching stocks, they would have been better off in a simple index fund. That is not a failure -- that is valuable self-knowledge. You can redirect that energy toward the aspects of financial planning that matter more, like saving rate, tax optimization, and staying invested during downturns.

**Sam:** This is the most practical episode we have done yet. Thank you for walking through all of this.

**Alex:** Before we wrap up, I want to emphasize one final point. These metrics are tools for learning and improving. Do not obsess over short-term Sharpe ratios or panic over a bad quarter's drawdown. Calculate these annually, look at trends over time, and use them to gradually refine your approach. The best investors are the ones who treat their portfolio as a continuous learning experiment, and these metrics are how you keep score honestly.

[VISUAL: End screen with key takeaways in bullet points:
- Returns without risk context are meaningless
- Drawdowns matter more than volatility for real investors
- Sharpe ratio: excess return per unit of total risk
- Sortino ratio: excess return per unit of downside risk
- TWR measures the strategy; MWR measures your experience
- Calculate these annually to track your improvement]

**Sam:** Same time next week?

**Alex:** Same time next week. We will be talking about interest rates and how the Federal Reserve affects everything from bond prices to stock valuations. You will not want to miss it.

[VISUAL: Preview card for Week 18 with "Interest Rates and Central Bank Policy" and an animated Federal Reserve building icon]

**Alex:** Thanks for watching everyone. If this episode helped you think differently about performance measurement, share it with a friend who is just looking at returns and thinking they have the whole picture. See you next week.

[VISUAL: Outro animation with subscribe button and links to previous episodes]
