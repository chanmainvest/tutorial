<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 21: Equity Valuation - P/E, P/B, and DCF

---

## Reading Section

### a) Why This Is Important

Valuation is the single most critical skill that separates successful investors from those who simply guess. Every stock you buy has a price -- but does that price reflect what the company is actually worth? Without a framework for answering that question, you are flying blind.

Consider two investors looking at the same company. Investor A sees the stock price has risen 50% in the past year and buys, hoping the trend continues. Investor B calculates that the stock trades at 35 times earnings, well above its historical average and its peers, suggesting the market has already priced in years of optimistic growth. Investor B waits for a better entry point. Over time, Investor B systematically outperforms because she has a valuation discipline.

Valuation matters for several reasons:

1. **It anchors your decisions.** Without valuation, you are reacting to headlines and price movements. With valuation, you have an independent estimate of what a company is worth and can act rationally when markets are irrational.

2. **It helps you compare apples to oranges.** A stock trading at $500 per share is not "more expensive" than one trading at $20. Valuation ratios let you compare companies of different sizes, in different industries, and at different stages of growth on a level playing field.

3. **It protects you from permanent loss of capital.** The most devastating investment losses come from overpaying for assets. A rigorous valuation process serves as your margin of safety -- the gap between the price you pay and the value you receive.

4. **It applies everywhere.** Whether you are buying individual stocks, evaluating an ETF, assessing a private business, or even negotiating the purchase of a house, valuation principles are universal.

This lesson covers the most widely used valuation methods: relative valuation through multiples (P/E, P/B, EV/EBITDA) and absolute valuation through discounted cash flow (DCF) analysis. By the end, you will know when to use each method, how to apply them correctly, and how to avoid the most common traps.

---

### b) What You Need to Know

#### 1. The Two Schools of Valuation

All valuation approaches fall into two broad categories:

**Relative Valuation (Multiples-Based)**
- Asks: "What is this company worth compared to similar companies?"
- Uses ratios like P/E, P/B, EV/EBITDA to compare across peers
- Fast, intuitive, and widely used on Wall Street
- Weakness: if the entire sector is overvalued, relative valuation will not warn you

**Absolute Valuation (Intrinsic Value)**
- Asks: "What is this company worth based on its own cash flows?"
- Uses discounted cash flow (DCF) analysis
- More rigorous and theoretically sound
- Weakness: highly sensitive to assumptions about future growth and discount rates

Neither approach is universally superior. The best analysts use both and look for convergence.

```
VALUATION FRAMEWORK OVERVIEW
============================

                    VALUATION
                   /          \
                  /            \
         RELATIVE              ABSOLUTE
        (Multiples)              (DCF)
        /    |    \                |
      P/E   P/B  EV/EBITDA    Discount
                               Future
                              Cash Flows
                                 |
                            Present Value
                                 |
                          Intrinsic Value
```

---

#### 2. Price-to-Earnings Ratio (P/E)

The P/E ratio is the most commonly cited valuation metric. It tells you how much investors are willing to pay for each dollar of earnings.

**Formula:**

```
P/E Ratio = Stock Price / Earnings Per Share (EPS)
```

Or equivalently for the whole company:

```
P/E Ratio = Market Capitalization / Net Income
```

**Example:**
- Stock price: $150
- Earnings per share: $10
- P/E = $150 / $10 = 15x

This means investors are paying $15 for every $1 of current earnings. Another way to think about it: if earnings stayed flat forever, it would take 15 years for the company to "earn back" its stock price.

**Trailing P/E vs. Forward P/E**

```
TRAILING P/E vs. FORWARD P/E
=============================

Trailing P/E                    Forward P/E
-----------                    -----------
Uses PAST earnings             Uses ESTIMATED future earnings
(last 12 months)               (next 12 months)

Price / Last Year EPS          Price / Expected Next Year EPS

More reliable data             More forward-looking
but backward-looking           but relies on analyst estimates

Example:                       Example:
Price = $150                   Price = $150
Last year EPS = $10            Est. next year EPS = $12
Trailing P/E = 15x             Forward P/E = 12.5x
```

**Key insight:** A company with a trailing P/E of 15x and a forward P/E of 12.5x is expected to grow earnings by 20%. The gap between trailing and forward P/E tells you about growth expectations.

**The PEG Ratio -- Adjusting P/E for Growth**

A stock with a P/E of 30 might look expensive, but if it is growing earnings at 30% per year, the high P/E is justified. The PEG ratio adjusts for this:

```
PEG Ratio = P/E Ratio / Earnings Growth Rate (%)

Example:
P/E = 30, Growth = 30% --> PEG = 30/30 = 1.0 (fairly valued)
P/E = 30, Growth = 15% --> PEG = 30/15 = 2.0 (expensive)
P/E = 15, Growth = 20% --> PEG = 15/20 = 0.75 (cheap)

Rule of thumb:
PEG < 1.0  -->  Potentially undervalued
PEG = 1.0  -->  Fairly valued
PEG > 1.5  -->  Potentially overvalued
```

**Caution:** PEG ratios assume growth is linear and sustainable. For cyclical or early-stage companies, this assumption can be dangerously wrong.

**What is a "normal" P/E?**

```
HISTORICAL S&P 500 P/E RANGE
==============================

         Cheap              Fair            Expensive
  |---------|----------------|----------------|---------|
  5x       10x              16x              25x       35x+

  Shiller CAPE long-term average: ~16-17x

  Sector variations (typical ranges):
  - Utilities:        12-18x (low growth, stable)
  - Banks:            8-14x  (cyclical, regulated)
  - Consumer Staples: 18-25x (steady, defensive)
  - Technology:       20-35x (high growth)
  - Biotech:          N/A    (often no earnings)
```

---

#### 3. Price-to-Book Ratio (P/B)

The P/B ratio compares a company's market value to its accounting book value (total assets minus total liabilities).

**Formula:**

```
P/B Ratio = Stock Price / Book Value Per Share

Or: P/B = Market Cap / Total Shareholders' Equity
```

**Example:**
- Stock price: $50
- Book value per share: $25
- P/B = $50 / $25 = 2.0x

This means the market values the company at twice its accounting book value. The premium reflects intangible assets (brand, intellectual property, human capital) that accounting does not capture.

**When P/B Works Best:**

```
P/B IS MOST USEFUL FOR:              P/B IS LEAST USEFUL FOR:
========================              =========================
- Banks and financial firms           - Technology companies
  (assets = loans, securities)          (value is in IP, not assets)
- Insurance companies                 - Service companies
- Real estate companies                 (few tangible assets)
- Asset-heavy industrials             - Pharma/biotech
- Companies in distress                 (value is in pipeline)
  (floor value assessment)
```

**Key insight:** For banks, P/B is the primary valuation metric because a bank's assets (loans) and liabilities (deposits) are already marked close to market value. A bank trading below 1.0x book value is signaling that the market believes its loans are worth less than stated -- a sign of potential trouble.

**Decomposing P/B with ROE:**

There is an elegant relationship between P/B and return on equity (ROE):

```
P/B = ROE x P/E

If ROE = 15% and P/E = 20x:
P/B = 0.15 x 20 = 3.0x

Implication:
- High ROE companies deserve high P/B ratios
- A company with P/B > 1 but low ROE is overvalued
- A company with P/B < 1 and high ROE may be undervalued
```

---

#### 4. Enterprise Value Multiples (EV/EBITDA)

Enterprise value (EV) represents the total value of a company to all capital providers -- both equity holders and debt holders.

**Enterprise Value Formula:**

```
EV = Market Cap + Total Debt - Cash and Cash Equivalents

Example:
Market Cap:    $10 billion
Total Debt:     $3 billion
Cash:           $1 billion
EV = $10B + $3B - $1B = $12 billion
```

**Why EV matters:** Two companies with identical market caps of $10 billion may have very different enterprise values if one carries $5 billion in debt and the other has $5 billion in cash. EV captures the true "acquisition price" -- what you would actually pay to buy the entire business.

**EV/EBITDA Ratio:**

```
EV/EBITDA = Enterprise Value / Earnings Before Interest, Taxes,
            Depreciation, and Amortization
```

**Why EV/EBITDA is often preferred over P/E:**

```
ADVANTAGE OF EV/EBITDA OVER P/E
=================================

1. Capital Structure Neutral
   P/E is affected by how a company finances itself
   EV/EBITDA is not

2. Depreciation Neutral
   Companies with different depreciation policies
   are comparable on EBITDA

3. Tax Neutral
   Companies in different tax jurisdictions
   are comparable

4. Works for Unprofitable Companies
   A company can have negative net income but
   positive EBITDA

Typical EV/EBITDA Ranges:
- Mature industrials:     6-10x
- Consumer brands:        10-14x
- Software/SaaS:          15-25x
- High-growth tech:       25-40x+
```

**EV/EBITDA in Practice -- A Comparison:**

```
COMPANY COMPARISON EXAMPLE
============================

                    Company A       Company B
                    ---------       ---------
Market Cap          $10B            $10B
Debt                $0              $5B
Cash                $2B             $0
Enterprise Value    $8B             $15B

Revenue             $5B             $5B
EBITDA              $1B             $1.5B

P/E                 20x             20x     <-- Look identical!
EV/EBITDA           8.0x            10.0x   <-- Company A is cheaper

Company A is actually cheaper because it has no debt
and significant cash. P/E missed this entirely.
```

---

#### 5. Discounted Cash Flow (DCF) Basics

DCF is the gold standard of absolute valuation. It values a company based on the present value of all future cash flows it will generate.

**The Core Principle:**

A dollar today is worth more than a dollar tomorrow because:
1. You could invest today's dollar and earn a return
2. There is risk that tomorrow's dollar might not materialize
3. Inflation erodes purchasing power

**The DCF Formula:**

```
                   CF_1         CF_2         CF_3               CF_n + TV
Value = --------- + --------- + --------- + ... + ---------
              (1+r)^1     (1+r)^2     (1+r)^3           (1+r)^n

Where:
CF  = Free Cash Flow in each period
r   = Discount rate (WACC)
TV  = Terminal Value
n   = Number of projection years (typically 5-10)
```

**Step-by-Step DCF Process:**

```
DCF VALUATION STEPS
====================

Step 1: Project Free Cash Flows (5-10 years)
  |
  v
Step 2: Determine the Discount Rate (WACC)
  |
  v
Step 3: Calculate Terminal Value
  |
  v
Step 4: Discount Everything to Present Value
  |
  v
Step 5: Sum Up = Enterprise Value
  |
  v
Step 6: Subtract Debt, Add Cash = Equity Value
  |
  v
Step 7: Divide by Shares Outstanding = Per Share Value
```

**Step 1: Projecting Free Cash Flows**

Free Cash Flow (FCF) is the cash a business generates after accounting for capital expenditures:

```
Free Cash Flow = Operating Cash Flow - Capital Expenditures

Or more detailed:
FCF = Net Income
    + Depreciation & Amortization
    - Changes in Working Capital
    - Capital Expenditures
```

You project FCF for each of the next 5-10 years based on:
- Historical growth rates
- Industry trends
- Management guidance
- Your own analysis of competitive position

**Step 2: The Discount Rate (WACC)**

The Weighted Average Cost of Capital represents the blended cost of a company's debt and equity financing:

```
WACC = (E/V) x Re + (D/V) x Rd x (1 - Tax Rate)

Where:
E/V = Proportion of equity financing
D/V = Proportion of debt financing
Re  = Cost of equity (from CAPM: Rf + Beta x Market Premium)
Rd  = Cost of debt (interest rate on borrowings)

Typical WACC ranges:
- Large, stable company:    7-9%
- Mid-cap growth company:   9-12%
- Small/risky company:      12-18%
- Startup/speculative:      20-30%+
```

**Step 3: Terminal Value**

Since companies can theoretically live forever, you need to estimate value beyond the projection period. This is the terminal value, and it often represents 60-80% of total DCF value.

```
TWO METHODS FOR TERMINAL VALUE
================================

Method 1: Gordon Growth Model (Perpetuity Growth)
-------------------------------------------------
TV = Final Year FCF x (1 + g) / (WACC - g)

Where g = long-term growth rate (typically 2-3%, close to
inflation or GDP growth)

Example:
Final Year FCF = $100M, WACC = 10%, g = 2.5%
TV = $100M x 1.025 / (0.10 - 0.025) = $1,367M


Method 2: Exit Multiple
-------------------------------------------------
TV = Final Year EBITDA x Exit EV/EBITDA Multiple

Example:
Final Year EBITDA = $150M, Exit Multiple = 10x
TV = $150M x 10 = $1,500M
```

**Step 4-7: Putting It All Together**

```
COMPLETE DCF EXAMPLE
=====================

Assumptions:
- Current FCF: $100M, growing 12% for 5 years, then 2.5% forever
- WACC: 10%
- Shares outstanding: 50 million
- Debt: $200M, Cash: $50M

Year        FCF         Discount Factor     Present Value
----        ---         ---------------     -------------
1           $112M       1/(1.10)^1 = 0.909  $101.8M
2           $125M       1/(1.10)^2 = 0.826  $103.3M
3           $140M       1/(1.10)^3 = 0.751  $105.2M
4           $157M       1/(1.10)^4 = 0.683  $107.3M
5           $176M       1/(1.10)^5 = 0.621  $109.3M
                                            ---------
                        PV of Cash Flows:   $526.9M

Terminal Value = $176M x 1.025 / (0.10 - 0.025) = $2,405M
PV of Terminal Value = $2,405M x 0.621 = $1,493M

Enterprise Value = $526.9M + $1,493M = $2,020M
Equity Value = $2,020M - $200M + $50M = $1,870M
Per Share Value = $1,870M / 50M = $37.40

If the stock trades at $30, it may be undervalued.
If the stock trades at $50, it may be overvalued.
```

---

#### 6. Sensitivity Analysis -- Why Assumptions Matter

Small changes in DCF assumptions produce large changes in value. This is why sensitivity analysis is essential.

```
SENSITIVITY TABLE: IMPACT ON PER-SHARE VALUE
==============================================

                    Terminal Growth Rate
                  1.5%    2.0%    2.5%    3.0%    3.5%
              +-------+-------+-------+-------+-------+
    8%    |  $52.10 | $56.80 | $62.70 | $70.30 | $80.40 |
          +-------+-------+-------+-------+-------+
W   9%    |  $42.30 | $45.40 | $49.30 | $54.10 | $60.20 |
A         +-------+-------+-------+-------+-------+
C  10%    |  $34.90 | $37.00 | $39.60 | $42.80 | $46.80 |
C         +-------+-------+-------+-------+-------+
   11%    |  $29.20 | $30.70 | $32.50 | $34.70 | $37.40 |
          +-------+-------+-------+-------+-------+
   12%    |  $24.70 | $25.80 | $27.10 | $28.70 | $30.60 |
          +-------+-------+-------+-------+-------+

Notice: Moving from WACC 10% / Growth 2.5% to
WACC 8% / Growth 3.5% more than DOUBLES the value!
```

**Key takeaway:** Never rely on a single DCF output. Always build a range of values using different assumptions.

---

#### 7. Relative vs. Absolute Valuation -- When to Use Each

```
DECISION MATRIX: WHICH METHOD TO USE
======================================

Situation                           Best Method(s)
---------                           --------------
Quick screening of many stocks      P/E, EV/EBITDA
Comparing within an industry        EV/EBITDA, P/E
Banks and financials                P/B, P/E
Asset-heavy businesses              P/B, EV/EBITDA
High-growth companies               Forward P/E, PEG, DCF
Pre-revenue startups                DCF (revenue-based)
M&A / buyout analysis               EV/EBITDA, DCF
Deep fundamental analysis           DCF with multiples check
Cyclical businesses at trough       Normalized P/E, P/B, DCF
Companies with lots of debt         EV/EBITDA (NOT P/E)
REITs and MLPs                      P/FFO, Dividend Yield
```

---

#### 8. Common Valuation Traps

**Trap 1: Value Traps**
A stock looks cheap on every metric (low P/E, low P/B) but stays cheap or gets cheaper because the business is in structural decline.

```
VALUE TRAP WARNING SIGNS
========================
- Revenue declining for 3+ years
- Market share loss to new competitors
- Industry disruption (think: newspapers, video rental)
- Low P/E but also low or declining ROE
- Management unable to articulate a turnaround plan
- "Cheap for a reason" -- the market is not always wrong
```

**Trap 2: Growth Traps**
Overpaying for growth that never materializes or that compresses margins.

**Trap 3: Accounting Manipulation**
Earnings can be manipulated. Cash flow is harder to fake. Always cross-check P/E with cash flow multiples (P/FCF).

**Trap 4: Comparing Unlike Companies**
A software company's P/E cannot be meaningfully compared to a bank's P/E. Always compare within the same industry or business model.

**Trap 5: Ignoring the Balance Sheet**
P/E ignores debt entirely. A company with a P/E of 10x and massive debt is not necessarily cheaper than one with a P/E of 15x and no debt. Use EV/EBITDA for a cleaner picture.

**Trap 6: Terminal Value Dominance in DCF**
When terminal value represents more than 80% of your DCF output, your valuation is essentially a guess about perpetual growth rates. Be skeptical.

```
HEALTHY DCF STRUCTURE
=====================

              Terminal Value
              as % of Total
              ===============
Reasonable:   50-70%
Caution:      70-80%
Dangerous:    80%+    <-- You are not valuing cash flows,
                          you are guessing about eternity
```

---

### c) Common Misconceptions

**Misconception 1: "A low P/E means the stock is cheap."**

Reality: A low P/E might mean the market expects earnings to decline. A company earning $5/share today trading at 8x P/E ($40) might see earnings drop to $2/share next year, making the forward P/E actually 20x. Always look at forward estimates and the trajectory of earnings.

**Misconception 2: "A high P/E means the stock is expensive."**

Reality: A high P/E can be perfectly justified by high growth. Amazon traded at enormous P/E ratios for years because it was reinvesting all profits into growth. Investors who avoided it due to "high P/E" missed one of the greatest wealth-creation stories in market history. Context matters.

**Misconception 3: "DCF gives you the 'true' value of a stock."**

Reality: DCF gives you an estimate that is only as good as your assumptions. Garbage in, garbage out. Two analysts can run a DCF on the same company and get values that differ by 100%. DCF is a framework for thinking, not a crystal ball.

**Misconception 4: "Book value represents what a company is actually worth."**

Reality: Book value is an accounting concept, not a market concept. It reflects historical cost minus depreciation, not current market value. A factory bought for $100 million twenty years ago might be worth $200 million or $10 million today -- book value tells you neither.

**Misconception 5: "You can value any company with any metric."**

Reality: Different business models require different valuation approaches. Trying to value a pre-revenue biotech on P/E is meaningless. Trying to value a bank on EV/EBITDA is misleading (banks' debt is their raw material, not their financing). Match the method to the business.

**Misconception 6: "The market always gets valuation right."**

Reality: In the short run, markets can deviate wildly from fundamental value. The dot-com bubble saw companies with no revenue trading at billions of dollars. The 2008 crisis saw bank stocks trading at fractions of book value. Valuation is your anchor when the market goes to extremes.

---

### d) Common Questions and Answers

**Q1: If a company has negative earnings, how do I calculate P/E?**

A: You cannot calculate a meaningful P/E for a company with negative earnings. Instead, use alternative metrics: Price-to-Sales (P/S), EV/EBITDA (if EBITDA is positive), EV/Revenue, or a DCF based on projected future profitability. For pre-revenue companies, you may need to use scenario-based DCF or comparable transaction analysis.

**Q2: What discount rate should I use in a DCF?**

A: The theoretically correct discount rate is the Weighted Average Cost of Capital (WACC), which typically ranges from 7-12% for most public companies. In practice, many individual investors use a simpler approach: a flat 10% discount rate for average-risk companies, higher for riskier ones. Warren Buffett reportedly uses the 10-year Treasury rate as his discount rate, arguing that if an investment cannot beat risk-free returns, it is not worth making.

**Q3: How do I know if a sector is overvalued, not just individual stocks?**

A: Compare the sector's current average P/E or EV/EBITDA to its own historical average. If the technology sector historically trades at 22x earnings and currently trades at 35x, the entire sector may be overvalued. Also compare the earnings yield (1/P/E) to bond yields. If stocks yield less than bonds, the equity risk premium has compressed, which is typically a warning sign.

**Q4: What is the Shiller CAPE ratio and why does it matter?**

A: The Cyclically Adjusted Price-to-Earnings ratio (CAPE) divides the current price by the average of inflation-adjusted earnings over the past 10 years. This smooths out the business cycle so you do not mistakenly think stocks are cheap at cyclical earnings peaks or expensive at cyclical troughs. The historical average CAPE for the S&P 500 is about 16-17x. When CAPE is significantly above this, subsequent 10-year returns have historically been below average.

**Q5: Should I use trailing or forward P/E?**

A: Use both and compare them. Trailing P/E uses verified historical data, so it is more reliable but backward-looking. Forward P/E uses analyst estimates, which are forward-looking but can be wrong. The relationship between the two tells you about growth expectations. A wide gap (forward much lower than trailing) implies high expected growth, but verify whether that growth is realistic.

**Q6: How accurate are DCF models in practice?**

A: Individual DCF outputs are frequently wrong because assumptions about growth rates, margins, and discount rates are uncertain. However, the DCF framework is extremely valuable as a thinking tool. It forces you to explicitly state your assumptions, which you can then debate and stress-test. The sensitivity table (showing value under different assumption combinations) is often more useful than any single number.

**Q7: Why do some value investors prefer EV/EBITDA over P/E?**

A: EV/EBITDA is capital-structure neutral (it does not penalize companies for having debt or reward them for having cash in misleading ways), it removes the effect of different depreciation policies and tax rates, and it better approximates operating cash flow. It is particularly useful for comparing companies that might be acquisition targets, since an acquirer buys the entire enterprise, not just the equity.

**Q8: Can I use these valuation techniques for ETFs?**

A: Yes. Most ETF providers publish the weighted average P/E, P/B, and other valuation metrics for their funds. You can compare the S&P 500 ETF's current P/E to its historical average to assess whether the broad market is cheap or expensive. For sector ETFs, compare the current multiples to sector historical averages. You generally would not run a DCF on an ETF, but the concept of discounting future cash flows applies to any asset.

**Q9: What is the difference between equity value and enterprise value?**

A: Equity value (market cap) is what belongs to shareholders. Enterprise value is what belongs to all capital providers (shareholders plus debt holders, minus cash). Think of it this way: if you buy a house for $500,000 with a $400,000 mortgage and $100,000 of equity, the enterprise value of the house is $500,000 (what it costs to own the whole thing) while the equity value is $100,000 (your stake). Always match the numerator to the denominator: equity value goes with earnings (P/E), enterprise value goes with EBITDA (EV/EBITDA).

**Q10: How do professional analysts actually value stocks?**

A: Most professional analysts use a combination: a primary valuation based on EV/EBITDA or P/E relative to peers, a DCF as a cross-check, and potentially a sum-of-the-parts analysis for diversified companies. They then triangulate between these methods. If all methods suggest the stock is undervalued, the conviction is high. If the methods disagree, further investigation is needed to understand why.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 21: Equity Valuation - P/E, P/B, and DCF"]

**Alex:** Welcome back everyone. Today we are tackling one of the most important topics in all of investing -- how to actually figure out what a stock is worth. This is equity valuation, and I promise you, once you understand this, you will look at the stock market completely differently.

**Sam:** I have to admit, Alex, this is something I have been confused about for a while. When I look at stock prices, I see numbers like $150 for one company and $30 for another. Does that mean the $30 stock is cheaper?

**Alex:** That is one of the biggest beginner mistakes, and I am glad you brought it up right away. The stock price alone tells you absolutely nothing about whether a stock is cheap or expensive. Think of it this way -- if I told you a slice of pizza costs $5, is that expensive?

**Sam:** I guess it depends on how big the slice is?

**Alex:** Exactly! A tiny sliver for $5 is outrageous, but a massive New York-style slice for $5 is a bargain. The stock price is the $5 -- the valuation metrics we are going to learn today are how you measure the size of the slice.

[VISUAL: Side-by-side comparison showing two pizza slices of different sizes, both labeled $5, transitioning to two stocks at different prices with their earnings highlighted]

**Sam:** Okay, that makes sense. So where do we start?

**Alex:** Let us start with the most famous valuation metric in the world -- the price-to-earnings ratio, or P/E.

[VISUAL: Large text showing "P/E = Price / Earnings Per Share"]

**Alex:** The P/E ratio tells you how many dollars investors are willing to pay for each dollar of earnings. If a stock trades at $150 and earns $10 per share, the P/E is 15. That means investors are paying $15 for every $1 of profit.

**Sam:** So a lower P/E is better, right? It means you are paying less for each dollar of earnings?

**Alex:** That is the intuition, but it is not that simple. And this is where most people go wrong. A low P/E can mean the stock is cheap, yes. But it can also mean the market expects earnings to fall. If a company earned $10 this year but the market thinks it will earn only $5 next year, the trailing P/E looks low, but the forward P/E is actually double.

**Sam:** Wait, what is the difference between trailing and forward P/E?

**Alex:** Great question. Trailing P/E uses earnings from the past twelve months -- it is based on actual, reported numbers. Forward P/E uses estimated earnings for the next twelve months -- it is based on analyst forecasts.

[ANIMATION: animation/week21_dcf_model.py - Animated bar chart showing a company's trailing earnings vs. forward estimated earnings, with P/E ratios calculated dynamically as the bars change height. The animation shows how the same stock price produces different P/E ratios depending on which earnings figure you use.]

**Sam:** So you need to look at both?

**Alex:** Absolutely. And pay attention to the gap between them. If trailing P/E is 20 and forward P/E is 15, the market expects about 33% earnings growth. But if trailing is 15 and forward is 20, the market expects earnings to decline. That gap tells a story.

**Sam:** This is already more nuanced than I expected. What about when people say "the market P/E is 22" -- what does that mean?

**Alex:** They are talking about the weighted average P/E of the entire S&P 500 index. Historically, the S&P 500 has traded at an average P/E of about 16 to 17 times. When it gets much higher than that, say above 25, it tends to mean stocks are getting expensive relative to historical norms.

[VISUAL: Historical chart of S&P 500 P/E ratio from 1950 to present, with bands showing "cheap" (below 12), "fair" (12-20), and "expensive" (above 20) zones, with notable market events labeled]

**Sam:** But tech companies trade at way higher P/Es than that, right?

**Alex:** They do, and that is because P/E comparisons only work within similar categories. A technology company growing revenues at 30% per year deserves a higher P/E than a utility growing at 3%. This is where the PEG ratio comes in -- you divide the P/E by the earnings growth rate. A PEG of 1.0 suggests the stock is fairly priced for its growth. Below 1.0, it may be a bargain. Above 1.5, you are probably overpaying for the growth.

**Sam:** Okay, so P/E is useful but has limitations. What about P/B -- the price-to-book ratio?

**Alex:** Price-to-book compares the stock price to the company's book value, which is essentially what the accountants say the company is worth on paper -- total assets minus total liabilities.

[VISUAL: Balance sheet diagram showing Assets on one side, Liabilities + Equity on the other, with Book Value highlighted as the equity portion]

**Alex:** If a company has a P/B of 2.0, it means the market values it at twice its book value. The premium reflects things that do not show up on the balance sheet -- brand value, intellectual property, talented employees, growth prospects.

**Sam:** When would I use P/B instead of P/E?

**Alex:** P/B is most useful for financial companies -- banks, insurance companies -- because their assets are mostly financial instruments that are already close to market value. For a bank, book value is a pretty good approximation of what its assets are actually worth. A bank trading below 1.0 times book is basically the market saying "we think some of those loans on your books are not going to be repaid."

**Sam:** That is a red flag then?

**Alex:** It can be an opportunity or a red flag, depending on whether the market is right or overreacting. During the 2008 financial crisis, many solid banks traded well below book value. Investors who bought them made enormous returns. But some banks that traded below book really did have terrible loan portfolios and went bankrupt. That is the art of investing -- figuring out which situation you are in.

[VISUAL: Chart showing major bank stock P/B ratios during 2008-2009, with banks that recovered versus banks that failed highlighted in different colors]

**Sam:** This is getting really interesting. You mentioned EV/EBITDA earlier -- that sounds more complicated.

**Alex:** It sounds complicated, but it is actually more straightforward than P/E in many ways. Let me break it down. First, enterprise value. Think of buying a house. The house costs $500,000, but you have a $400,000 mortgage. Your equity -- your stake -- is $100,000. The enterprise value of the house is $500,000, because that is what it costs to own the whole thing free and clear.

**Sam:** So enterprise value is like the total price tag of the company?

**Alex:** Exactly. It is market cap plus debt minus cash. It represents what it would actually cost an acquirer to buy the entire business -- they buy the equity, assume the debt, but get the cash.

[VISUAL: Animated diagram showing Enterprise Value as a stack: Market Cap on top, plus Debt, minus Cash, equals Enterprise Value. Two companies side by side with same market cap but different EVs due to different debt and cash levels.]

**Alex:** Now, EBITDA stands for Earnings Before Interest, Taxes, Depreciation, and Amortization. It is a rough proxy for operating cash flow. When you divide EV by EBITDA, you get a cleaner valuation metric than P/E because it strips out the effects of how a company is financed, how it is taxed, and how it depreciates its assets.

**Sam:** Why is that better?

**Alex:** Let me give you an example. Imagine two identical restaurant chains. Both generate the same revenue and the same operating profit. But Company A financed its expansion with debt, so it pays a lot of interest, which reduces net income and makes P/E look high. Company B used equity financing, so no interest expense, and P/E looks low. On P/E, Company B looks cheaper. But on EV/EBITDA, they look the same -- because EV/EBITDA ignores the financing decision. It just looks at the operations.

**Sam:** That makes so much sense. So EV/EBITDA is better for comparing companies with different amounts of debt.

**Alex:** Exactly. And it is the metric most commonly used in mergers and acquisitions, because when a company buys another company, they are buying the enterprise.

[VISUAL: Comparison table showing two companies with identical operations but different capital structures, demonstrating how P/E gives misleading signals while EV/EBITDA shows they are equivalent]

**Sam:** Okay, these are all relative valuation methods -- comparing one company to another. What about figuring out what a company is worth on its own?

**Alex:** Now we get to the grand daddy of valuation methods: the discounted cash flow, or DCF.

[VISUAL: Title card "Discounted Cash Flow Analysis" with dramatic music]

**Alex:** The DCF is based on a simple but powerful idea: a company is worth the sum of all the cash it will generate in the future, discounted back to today's value.

**Sam:** Discounted? Why would you discount future cash?

**Alex:** Because a dollar today is worth more than a dollar tomorrow. If I offered you $100 today or $100 in a year, which would you take?

**Sam:** Today, obviously.

**Alex:** Why?

**Sam:** Because I could invest that $100 and have maybe $108 or $110 by next year.

**Alex:** Exactly. So $100 next year is really only worth about $91 to $93 today, assuming you could earn 8-10% on your money. That is discounting. You are adjusting future cash flows to reflect their present value.

[ANIMATION: animation/week21_dcf_model.py - Animated visualization showing future cash flow bars stretching into the future, each one getting slightly larger (growth), but then showing the "discounting" effect where each bar shrinks as it is brought back to present value. The sum of the discounted bars builds up to show the total present value. The terminal value appears as a large block at the end.]

**Sam:** So in a DCF, you project out future cash flows and discount them back?

**Alex:** Right. There are basically four steps. First, you estimate free cash flow for the next five to ten years. Second, you calculate a terminal value to capture all cash flows beyond that period. Third, you discount everything back to the present using a rate called WACC -- the weighted average cost of capital. Fourth, you add it all up, subtract debt, add cash, and divide by shares to get a per-share value.

**Sam:** What is this terminal value? It sounds important.

**Alex:** It is incredibly important -- and also the most dangerous part of a DCF. Since a company can theoretically live forever, you cannot project cash flows for eternity. So after your projection period -- say ten years -- you estimate what all remaining future cash flows are worth using a simple formula. The problem is that terminal value often represents 60 to 80 percent of the total value.

**Sam:** Whoa, so most of the value comes from a single estimate about the distant future?

**Alex:** Yes, and this is why DCF has its critics. You are essentially making a guess about growth rates decades from now. A small change in assumptions can swing the value by 50% or more.

[VISUAL: Pie chart showing typical DCF breakdown -- 30% from projected cash flows, 70% from terminal value, with annotation "This is why sensitivity analysis matters!"]

**Sam:** That sounds scary. How do you deal with that uncertainty?

**Alex:** You build a sensitivity table. Instead of producing one number, you produce a range. You show what the stock is worth under different combinations of growth rates and discount rates. If the stock looks undervalued under most reasonable scenarios, you have a compelling case. If it only looks cheap under the most optimistic assumptions, be careful.

[VISUAL: Interactive sensitivity table with WACC on one axis and growth rate on the other, showing how value changes across different assumption combinations, with cells color-coded green (undervalued) to red (overvalued)]

**Sam:** Can you walk me through a quick example?

**Alex:** Sure. Let us say a company generates $100 million in free cash flow this year and we expect it to grow at 12% per year for five years. After that, we assume it grows at 2.5% forever. Our discount rate is 10%.

**Sam:** Those seem like reasonable numbers.

**Alex:** Year one cash flow is $112 million. Year two, $125 million. And so on up to $176 million in year five. You discount each of those back. Then the terminal value is $176 million times 1.025, divided by the difference between 10% and 2.5%, which gives you about $2.4 billion. Discount that back five years and it is about $1.5 billion. Add up the projected cash flows and the discounted terminal value, and you get about $2 billion in enterprise value. Subtract $200 million in debt, add $50 million in cash, divide by 50 million shares, and you get $37.40 per share.

**Sam:** So if the stock is trading at $30, it is undervalued?

**Alex:** According to this model, yes. But remember -- change the growth rate from 12% to 8%, and the value might drop to $28. Change the discount rate from 10% to 12%, and it might drop further. The DCF does not tell you the answer; it tells you what the answer would be if your assumptions are correct.

[VISUAL: The DCF example numbers building step by step on screen, with the final per-share value highlighted]

**Sam:** This is really helpful. But I am curious -- when should I use P/E versus EV/EBITDA versus DCF? When does each one shine?

**Alex:** Great question. For quick screening when you are looking at many stocks, use P/E and EV/EBITDA. They are fast and easy to compare. For financial companies -- banks, insurance -- use P/B because their balance sheets are the business. For companies with a lot of debt, use EV/EBITDA instead of P/E because it accounts for leverage. For a deep dive where you want your own independent estimate of value, build a DCF. For high-growth companies with no current earnings, you might need a revenue-based DCF or EV/Revenue.

**Sam:** And you mentioned using multiple methods together?

**Alex:** Always. If P/E says a stock is cheap, EV/EBITDA says it is cheap, and your DCF says it is cheap under most reasonable assumptions -- now you really have something. If they disagree, you need to figure out why. The disagreement itself is informative.

[VISUAL: Venn diagram showing the three valuation methods overlapping, with "High Conviction Buy" in the center where all three agree]

**Sam:** Before we wrap up, can we talk about traps? Where do people go wrong with valuation?

**Alex:** The biggest trap is the value trap. You find a stock with a low P/E, low P/B, looks cheap on every metric. You buy it, and it keeps going down. Why? Because the business is in structural decline. The market was not wrong to price it cheaply -- it was right. Think about Kodak when digital photography was taking over, or traditional taxi companies when ridesharing arrived.

**Sam:** So how do you avoid that?

**Alex:** Ask yourself: is the business cheap because the market is overreacting to temporary bad news, or cheap because the business model is dying? If revenue has been declining for years, market share is shrinking, and management has no credible plan to turn things around -- that is probably a value trap, not a value opportunity.

[VISUAL: Two paths diverging -- one labeled "Genuine Value Opportunity" showing a stock recovering, the other labeled "Value Trap" showing a stock continuing to decline despite low multiples]

**Alex:** The second big trap is overpaying for growth. Just because a company is growing fast does not mean any price is justified. At some point, the P/E is so high that the company would need to grow at 40% for twenty years to justify it. That almost never happens.

**Sam:** What is the reality check for that?

**Alex:** Use the PEG ratio as a starting point, and always ask: what growth rate is currently baked into the stock price? If a stock trades at 50 times earnings, the market is expecting massive growth. Is that realistic? How many companies in history have sustained 30% earnings growth for more than a few years? Very, very few.

**Sam:** And the accounting trap?

**Alex:** Yes -- earnings can be manipulated through accounting choices. Aggressive revenue recognition, capitalizing expenses, one-time charges that happen every year. Always cross-check earnings-based metrics with cash flow-based metrics. If a company reports strong earnings but weak cash flow, something might be off.

[VISUAL: Side-by-side comparison showing "Reported Earnings" vs. "Free Cash Flow" for a hypothetical company, with divergence highlighted as a warning sign]

**Sam:** Can we do a quick practice exercise? Give me a real-world-style scenario.

**Alex:** Absolutely. Let us say you are looking at two companies in the same industry -- consumer packaged goods. Company A has a P/E of 12, P/B of 1.5, and EV/EBITDA of 8. Company B has a P/E of 28, P/B of 6.0, and EV/EBITDA of 18. Which is cheaper?

**Sam:** Company A, obviously. Every metric is lower.

**Alex:** Not so fast. What if I told you Company A's revenue has been declining 5% per year, its market share is shrinking, and management just cut the dividend? Meanwhile, Company B has been growing revenue 15% per year, has a dominant brand, and generates enormous free cash flow.

**Sam:** Then Company A might be a value trap.

**Alex:** Exactly. Now let us say you run a DCF on both. Company A, even with declining revenues, has a DCF value of $45 and trades at $35 -- a 22% discount. Company B's DCF value is $120 and it trades at $115 -- only a 4% discount. Which do you buy?

**Sam:** It is tempting to say Company A because the discount is bigger, but if the business is deteriorating, the DCF inputs might be too optimistic.

**Alex:** Now you are thinking like a real analyst. The answer is: you need to stress-test both DCFs. If Company A's DCF value drops to $30 under pessimistic assumptions, it is overvalued at $35. If Company B's DCF holds up at $100 or above under most scenarios, it might actually be the better buy at $115 despite the smaller discount.

[VISUAL: Decision tree showing the analytical process: screen with multiples, then dig deeper with fundamentals, then validate with DCF, then stress-test assumptions]

**Sam:** So valuation is not about finding the lowest number -- it is about finding the best risk-adjusted opportunity.

**Alex:** Perfectly said. And that requires combining quantitative metrics with qualitative judgment about the business. The numbers are the starting point, not the conclusion.

**Sam:** What about sector-specific tricks? You mentioned banks use P/B. Are there other sector-specific metrics I should know?

**Alex:** Great question. REITs use Price-to-FFO -- funds from operations -- because traditional earnings do not capture real estate economics well. Airlines and industrials sometimes use EV/EBITDAR, adding back rent expenses. Software companies often use EV/Revenue or a "Rule of 40" -- growth rate plus profit margin should exceed 40. Insurance companies use Price-to-Book and combined ratios. Each industry has its own language, and speaking that language is essential for accurate valuation.

[VISUAL: Table showing industry-specific valuation metrics: Banks (P/B, P/TBV), REITs (P/FFO, P/AFFO), Software (EV/Revenue, Rule of 40), Insurance (P/B, Combined Ratio), Airlines (EV/EBITDAR), Pharma (Pipeline Value, EV/Revenue)]

**Sam:** This course keeps expanding my toolkit. Okay, if I had to remember just three things from today, what would they be?

**Alex:** First, no single valuation metric tells the whole story -- use multiple methods and look for convergence. Second, context matters enormously -- always compare within the same industry and consider the growth profile. Third, a valuation model is only as good as its assumptions -- focus more on understanding the range of possible values than on finding a single "right" number.

**Sam:** Valuation is not a science -- it is a framework for thinking.

**Alex:** That is exactly right. And the more you practice, the better your intuition becomes for what "cheap" and "expensive" really mean.

[VISUAL: Summary card with the three key takeaways, plus a preview of next week's lesson on currency and international diversification]

**Alex:** Next week, we are going global. We will talk about international diversification, currency risk, and why most investors have too much of their money in their home country. See you then.

**Sam:** Can not wait. Thanks everyone for watching!

[VISUAL: End screen with subscribe button and links to previous lessons]

---
