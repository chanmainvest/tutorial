<!-- 此檔案需要翻譯為香港繁體中文 -->
<!-- This file needs translation to HK Traditional Chinese -->

# Week 34: Interest Rate Sensitivity Across Assets

---

## Reading Section

---

### a) Why This Is Important

Most investors think about interest rates as a bond market issue. When rates rise, bond prices fall. Simple enough. But interest rates are far more pervasive than that -- they are the gravitational force of all financial markets. Every single asset class is affected by interest rates, often in ways that are not immediately obvious.

Consider these real-world impacts:

1. **Equities as long-duration assets**: When the Federal Reserve raised rates aggressively in 2022, the Nasdaq-100 fell over 30%. High-growth technology stocks -- companies with earnings far in the future -- were hit hardest. Why? Because equities, especially growth stocks, behave like long-duration bonds. Their value comes from cash flows decades into the future, and higher discount rates crush the present value of those distant cash flows.

2. **Real estate depends on rates**: The housing market slowed dramatically when 30-year mortgage rates went from 3% to 7% in 2022-2023. Commercial real estate suffered even more, with some office buildings losing 40-50% of their value. Real estate is among the most rate-sensitive asset classes because it is heavily financed with debt.

3. **Rate regimes define investment eras**: The period from 1981 to 2020 was a secular bull market in bonds, with rates falling from 15% to near zero. This tailwind lifted all asset prices. Now that rates have normalized, the investment playbook is fundamentally different. Understanding rate sensitivity tells you which assets will thrive and which will struggle in different rate environments.

4. **Corporate behavior changes with rates**: When rates are low, companies borrow cheaply to buy back stock, fund acquisitions, and invest in speculative projects. When rates rise, these activities contract. Leverage that was sustainable at 3% rates can become crushing at 6%. Understanding this dynamic helps you identify which companies are most vulnerable.

5. **Portfolio construction**: If you do not understand rate sensitivity, you cannot build a robust portfolio. You might think you are diversified, but if all your assets are highly rate-sensitive in the same direction, a rate shock can hit your entire portfolio at once.

This lesson connects the dots between interest rates and every major asset class, giving you the framework to anticipate how rate changes will ripple through your portfolio.

---

### b) What You Need to Know

#### 1. Equities as Long-Duration Assets

Most investors do not think of stocks as having "duration," but they absolutely do. In bond math, duration measures how sensitive a bond's price is to interest rate changes. The same concept applies to equities.

**The Duration of an Equity:**

A stock's value equals the present value of all future cash flows (dividends, earnings, free cash flow). These cash flows stretch decades into the future. The discount rate used to calculate present value is directly influenced by interest rates.

```
Stock Value = Sum of [ CF(t) / (1 + r)^t ] for t = 1 to infinity

Where:
  CF(t) = Expected cash flow in year t
  r = Discount rate (risk-free rate + equity risk premium)
  t = Time period

When r increases, the denominator grows, and the present value falls.
The further into the future the cash flow, the more it is discounted.
```

**Illustrative Example -- Impact of a 1% Rate Increase:**

```
Company A: "Value Stock"
  - Earns $10/share today, growing at 3%/year
  - Most value comes from near-term cash flows
  - Duration estimate: ~15 years
  - Price impact of +1% rates: approximately -15%

Company B: "Growth Stock"
  - Earns $1/share today, growing at 25%/year
  - Most value comes from cash flows 10-20 years out
  - Duration estimate: ~35 years
  - Price impact of +1% rates: approximately -35%
```

This explains why growth stocks are far more volatile in response to rate changes than value stocks.

**Equity Duration by Style:**

```
Style/Sector             | Estimated Duration | Rate Sensitivity
-------------------------|-------------------|------------------
Deep Value (banks, etc.) | 8 - 12 years      | Low
Dividend stocks          | 12 - 18 years     | Moderate
Broad market (S&P 500)  | 18 - 25 years     | Moderate-High
Growth stocks            | 25 - 40 years     | High
Unprofitable tech       | 40 - 60+ years    | Very High
Pre-revenue biotech     | 50 - 80+ years    | Extreme
```

**Why did this matter in 2022?**

```
Asset                    | 2022 Return | Rate Sensitivity Explanation
-------------------------|------------|----------------------------------
Profitable value stocks  | -5%        | Short duration, near-term cash flows
S&P 500                  | -18%       | Mix of growth and value
Nasdaq-100               | -33%       | Growth-heavy, longer duration
ARK Innovation ETF (ARKK)| -67%      | Unprofitable growth, extreme duration
30-Year Treasury Bond    | -33%       | Long-duration fixed income

Fed Funds Rate: 0.25% -> 4.50% (425 bps increase)
```

Notice how the most rate-sensitive equities fell as much or more than long-term bonds. This is not a coincidence -- it reflects their similar duration characteristics.

#### 2. Growth vs. Value Duration

The growth-vs.-value debate has a rate sensitivity dimension that many investors miss.

**Why Growth Has Higher Duration:**

Growth companies reinvest most of their earnings into future expansion rather than paying dividends. Their value proposition is: "We will earn enormous profits in the future, even if profits are slim today." This means most of their intrinsic value comes from cash flows 10, 15, or 20+ years into the future.

Value companies, by contrast, are already generating significant cash flows today. They pay dividends, buy back stock, and generate free cash flow now. Their value is concentrated in nearer-term cash flows.

```
Cash Flow Distribution Over Time:

Value Stock:
Year:  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15+
       $$$ $$$ $$  $$  $$  $$  $   $   $   $   .   .   .   .   .
       ^^^^^^^^^^^^^^^
       Most value here (near-term)

Growth Stock:
Year:  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15+
       $   $   $   $   $$  $$  $$  $$$ $$$ $$$ $$$ $$$ $$$ $$$ $$$
                                       ^^^^^^^^^^^^^^^^^^^^^^^
                                       Most value here (far future)
```

**Historical Pattern:**

```
Rate Environment       | Growth vs. Value Performance
-----------------------|-------------------------------
Falling rates          | Growth outperforms value
Rising rates           | Value outperforms growth
Stable low rates       | Growth outperforms value
Stable high rates      | Value outperforms growth (usually)
Rate transition (any)  | Maximum divergence between styles
```

This is not a perfect relationship, but it is a strong tendency. The massive outperformance of growth over value from 2009-2021 coincided with a period of persistently falling and near-zero rates. The value resurgence in 2022 coincided with the fastest rate hiking cycle in decades.

#### 3. The Equity Duration Concept in Depth

Let us formalize the equity duration concept with a simplified model:

**Gordon Growth Model and Duration:**

```
Price = D1 / (r - g)

Where:
  D1 = Next year's dividend (or free cash flow)
  r = Required return (risk-free rate + equity risk premium)
  g = Growth rate

Duration (approximate) = 1 / (r - g)

Example 1: Mature utility
  r = 8%, g = 2%
  Duration = 1 / (0.08 - 0.02) = 1 / 0.06 = 16.7 years
  Price sensitivity to +1% rates: approximately -16.7%

Example 2: High-growth tech
  r = 10%, g = 8%
  Duration = 1 / (0.10 - 0.08) = 1 / 0.02 = 50 years
  Price sensitivity to +1% rates: approximately -50%
```

This simplified model shows why the gap between growth rates and discount rates matters so much. When g is close to r, duration becomes extremely long, and the stock becomes extremely sensitive to rate changes.

**Two-Stage Dividend Discount Model Duration:**

For a more realistic estimate, consider a company with a high-growth phase followed by a mature phase:

```
Stage 1: Years 1-10, growth = 20%/year, payout = 0%
Stage 2: Year 11+, growth = 3%/year, payout = 60%

With r = 9%:
  PV of Stage 1 cash flows: $0 (no payout)
  PV of Stage 2 cash flows: all value comes from year 11+
  Effective duration: ~40 years

With r = 10% (+1%):
  PV of Stage 2 cash flows drops significantly
  Price decline: approximately 30-40%
```

This illustrates why unprofitable growth companies that reinvest everything are so rate-sensitive -- literally 100% of their value comes from the distant future.

#### 4. Real Estate Sensitivity to Interest Rates

Real estate is one of the most interest-rate-sensitive asset classes, for several interconnected reasons:

**Channel 1: Financing Costs**

Most real estate is purchased with significant leverage (debt). A typical commercial property might be financed with 60-70% debt.

```
Impact of Rising Rates on Property Cash Flow:

Scenario: $10 million property, 65% LTV, 10-year loan

At 4% interest rate:
  Loan amount: $6,500,000
  Annual interest: $260,000
  Net Operating Income: $600,000
  Debt Service Coverage Ratio: 2.3x
  Cash flow after debt service: $340,000
  Cash-on-cash return: 9.7% ($340K / $3.5M equity)

At 7% interest rate:
  Loan amount: $6,500,000
  Annual interest: $455,000
  Net Operating Income: $600,000
  Debt Service Coverage Ratio: 1.3x
  Cash flow after debt service: $145,000
  Cash-on-cash return: 4.1% ($145K / $3.5M equity)

The same property's cash flow to equity investors drops 57%
when rates rise from 4% to 7%.
```

**Channel 2: Cap Rate Expansion**

Capitalization rates (cap rates) are the real estate equivalent of earnings yields. They tend to rise when interest rates rise, because investors demand higher yields from real estate when risk-free alternatives become more attractive.

```
Cap Rate = Net Operating Income / Property Value

When cap rates rise, property values fall:

NOI = $600,000

At 5% cap rate: Property value = $600,000 / 0.05 = $12,000,000
At 6% cap rate: Property value = $600,000 / 0.06 = $10,000,000
At 7% cap rate: Property value = $600,000 / 0.07 =  $8,571,429

A 200-basis-point increase in cap rates (5% to 7%)
reduces property value by 29%.
```

**Channel 3: Demand Reduction**

Higher rates reduce housing affordability and business expansion, lowering demand for real estate:

```
Monthly Payment on $400,000 Mortgage (30-year fixed):

  At 3.0%: $1,686/month
  At 4.0%: $1,910/month  (+13%)
  At 5.0%: $2,147/month  (+27%)
  At 6.0%: $2,398/month  (+42%)
  At 7.0%: $2,661/month  (+58%)
  At 8.0%: $2,935/month  (+74%)

Doubling the rate from 3% to 6% increases the monthly
payment by 42%, pricing many buyers out of the market.
```

**Real Estate Sectors by Rate Sensitivity:**

```
Sector              | Rate Sensitivity | Why
--------------------|-----------------|----------------------------------
Office              | Very High       | Long leases, high leverage, secular headwinds
Retail Malls        | High            | Leverage, competition from e-commerce
Multifamily/Apts    | High            | Cap rate sensitive, high leverage
Industrial/Logistics| Moderate        | Strong demand partially offsets rate impact
Data Centers        | Moderate        | Secular growth in demand
Self-Storage        | Moderate        | Short leases allow rent adjustment
Cell Towers         | Lower           | Long contracts, inflation escalators
Healthcare          | Lower           | Demographic demand relatively inelastic
```

**REITs vs. Physical Real Estate:**

REITs (Real Estate Investment Trusts) trade on stock exchanges and therefore react to rate changes immediately. Physical real estate reacts more slowly because properties are illiquid and repriced infrequently. This creates a pattern where REITs lead physical real estate by 6-12 months in reflecting rate impacts.

#### 5. Commodity and Interest Rate Relationship

The relationship between commodities and interest rates is complex and works through multiple channels:

**Channel 1: Carrying Cost (Cost of Carry)**

Holding physical commodities requires financing the inventory. Higher rates increase this carrying cost, putting downward pressure on commodity prices (or more precisely, on the futures curve).

```
Cost of Carry = Storage Costs + Financing Costs - Convenience Yield

When rates rise:
  Financing costs increase
  Carrying cost increases
  Futures prices relative to spot prices increase (contango steepens)
  Economic incentive to hold inventory decreases
```

**Channel 2: US Dollar Relationship**

Higher US interest rates typically strengthen the US dollar. Since most commodities are priced in dollars, a stronger dollar makes commodities more expensive for foreign buyers, reducing demand and putting downward pressure on prices.

```
Higher US Rates --> Stronger Dollar --> Commodity Prices Under Pressure

This relationship is strong but not absolute:
  - Correlation between DXY (Dollar Index) and commodity prices: ~-0.5
  - The relationship can break down when supply disruptions dominate
```

**Channel 3: Economic Activity**

Interest rates affect economic growth, which drives commodity demand:

```
Rate Impact Chain:
  Higher rates
    --> Slower economic growth
      --> Lower industrial production
        --> Lower demand for industrial commodities (copper, steel, oil)
          --> Lower commodity prices

But also:
  Higher rates
    --> Reduced investment in new supply (mining, drilling)
      --> Future supply constraints
        --> Eventually higher commodity prices
```

**Channel 4: Gold's Special Relationship with Rates**

Gold has a unique relationship with interest rates because it is a zero-yielding asset:

```
Gold's "Opportunity Cost" Framework:

  Gold yield = 0%
  Real interest rate = Nominal rate - Inflation

  When real rates are negative (rate < inflation):
    Gold's opportunity cost is minimal
    Gold tends to perform well

  When real rates are positive (rate > inflation):
    Gold's opportunity cost is significant
    Gold tends to underperform

  Historical correlation between gold and real rates: approximately -0.7
```

```
Commodity Rate Sensitivity Summary:

  Commodity       | Primary Rate Channel    | Sensitivity
  ----------------|------------------------|------------
  Gold            | Real rates, USD        | High (inverse)
  Oil             | Economic growth, USD   | Moderate
  Copper          | Economic growth        | Moderate-High
  Agricultural    | USD, financing costs   | Low-Moderate
  Natural Gas     | Domestic demand        | Low
  Precious metals | Real rates, USD        | High (inverse)
```

#### 6. Rate Impact on Leverage and Buybacks

Interest rates fundamentally change corporate behavior, especially regarding leverage and capital allocation:

**Leverage Sensitivity:**

```
Company XYZ Financial Profile:

  EBITDA: $500 million
  Total Debt: $2 billion
  Debt/EBITDA: 4.0x

  At 4% average interest rate:
    Interest expense: $80 million
    Interest coverage: 6.3x (comfortable)
    After-tax cost of debt: 3.0% (assuming 25% tax rate)
    Stock buybacks funded by cheap debt: accretive

  At 7% average interest rate:
    Interest expense: $140 million (+75%)
    Interest coverage: 3.6x (tighter)
    After-tax cost of debt: 5.25%
    Stock buybacks funded by expensive debt: often dilutive

  At 10% average interest rate:
    Interest expense: $200 million (+150%)
    Interest coverage: 2.5x (uncomfortable)
    After-tax cost of debt: 7.5%
    Company shifts to deleveraging mode
```

**The Buyback Machine:**

During the low-rate era (2010-2021), US companies bought back over $7 trillion in stock, much of it funded by cheap debt. This leveraged buyback strategy worked as follows:

```
How Debt-Funded Buybacks Work:

  Step 1: Borrow $1 billion at 3% interest ($30M/year after-tax cost: ~$22.5M)
  Step 2: Buy back $1 billion in stock
  Step 3: If earnings yield on stock > after-tax cost of debt, EPS increases
  Step 4: Higher EPS -> higher stock price -> repeat

  Example at low rates:
    Earnings yield: 5%  ($50M earnings from $1B buyback)
    After-tax debt cost: 2.25% ($22.5M)
    Net EPS accretion: 2.75% per $1B buyback
    Verdict: ACCRETIVE -- do more buybacks

  Example at high rates:
    Earnings yield: 5%  ($50M earnings from $1B buyback)
    After-tax debt cost: 5.25% ($52.5M)
    Net EPS accretion: -0.25% per $1B buyback
    Verdict: DILUTIVE -- stop buybacks, start deleveraging
```

**Sectors Most Affected by Rate Changes on Leverage:**

```
Sector                  | Typical Leverage | Rate Impact on Sector
------------------------|-----------------|---------------------------
Utilities               | 3-5x Debt/EBITDA| Moderate (regulated returns)
REITs                   | 4-8x Debt/EBITDA| High (leveraged, rate-sensitive)
Telecoms                | 3-5x Debt/EBITDA| Moderate-High
Private Equity-backed   | 5-8x Debt/EBITDA| Very High
Airlines                | 3-6x Debt/EBITDA| High (lease-heavy)
Banks                   | N/A (asset-based)| Complex (NIM vs. credit risk)
Technology (large cap)  | 0-1x Debt/EBITDA| Low (cash-rich)
Healthcare              | 1-3x Debt/EBITDA| Low-Moderate
```

#### 7. Rate Regime Mapping to Asset Allocation

Different interest rate environments favor different asset allocations. Understanding which "regime" we are in helps position portfolios appropriately.

**Four Rate Regimes:**

```
Regime 1: LOW AND FALLING RATES
  (Example: 2010-2020)
  |
  |-- Favored assets:
  |     Growth stocks (long duration benefits)
  |     Long-term bonds (price appreciation)
  |     REITs (declining cap rates, cheap financing)
  |     Private equity (leverage is cheap)
  |     Gold (low opportunity cost)
  |
  |-- Challenged assets:
  |     Bank stocks (compressed NIMs)
  |     Cash (near-zero yields)
  |     Money market funds
  |     Short-term bonds (low yield)
  |     Value stocks (less need for current income)

Regime 2: LOW AND RISING RATES
  (Example: 2022)
  |
  |-- Favored assets:
  |     Value stocks (shorter duration)
  |     Bank stocks (expanding NIMs)
  |     Floating-rate loans
  |     Cash and short-term bonds
  |     Commodities (early cycle)
  |     Energy stocks
  |
  |-- Challenged assets:
  |     Growth stocks (duration pain)
  |     Long-term bonds (price decline)
  |     REITs (cap rate expansion)
  |     Unprofitable companies (funding costs rise)
  |     Highly leveraged companies

Regime 3: HIGH AND STABLE RATES
  (Example: mid-2000s, or potentially current era)
  |
  |-- Favored assets:
  |     High-quality corporate bonds (attractive yields)
  |     Dividend stocks
  |     Short-duration bonds
  |     Cash equivalents (meaningful yield)
  |     Quality factor (strong balance sheets)
  |
  |-- Challenged assets:
  |     Speculative growth
  |     Highly leveraged companies
  |     Rate-sensitive real estate
  |     Long-duration bonds

Regime 4: HIGH AND FALLING RATES
  (Example: early 1980s, or potential future scenario)
  |
  |-- Favored assets:
  |     Long-term bonds (massive price appreciation)
  |     Growth stocks (duration tailwind)
  |     REITs (cap rate compression)
  |     ALL risk assets benefit
  |     Quality growth companies
  |
  |-- Challenged assets:
  |     Cash (yields declining)
  |     Floating-rate instruments (yields declining)
  |     Short-term bonds (less price appreciation)
```

**Rate Regime Identification Checklist:**

```
To identify the current rate regime, assess:

  1. Level: Are rates above or below the long-term average?
     Long-term average 10Y Treasury: ~4-5%
     Below average = "low" rate environment
     Above average = "high" rate environment

  2. Direction: Are rates rising, falling, or stable?
     Look at: Fed policy stance, inflation trajectory, economic growth

  3. Speed: How fast are rates changing?
     Rapid changes cause more dislocation than gradual ones
     2022 was extreme: 425 bps in 9 months

  4. Expectations: What does the market expect going forward?
     Fed funds futures, yield curve shape, TIPS breakevens
     Surprises matter more than anticipated changes

  Current Regime Assessment Framework:
  ┌─────────────────────────────────────────────┐
  │  Are rates above historical average?        │
  │    YES --> Are they rising or falling?       │
  │      Rising  --> Regime 2 (most painful)     │
  │      Falling --> Regime 4 (most bullish)     │
  │      Stable  --> Regime 3                    │
  │    NO  --> Are they rising or falling?       │
  │      Rising  --> Regime 2 (transition)       │
  │      Falling --> Regime 1                    │
  │      Stable  --> Regime 1                    │
  └─────────────────────────────────────────────┘
```

#### 8. Practical Rate Hedging

Investors can manage interest rate sensitivity through various hedging strategies:

**Strategy 1: Duration Management**

```
Reduce portfolio duration when you expect rates to rise:
  - Shorten bond maturities
  - Shift from growth to value stocks
  - Reduce REIT exposure
  - Hold more cash

Increase portfolio duration when you expect rates to fall:
  - Extend bond maturities
  - Increase growth stock allocation
  - Add REIT exposure
  - Reduce cash holdings
```

**Strategy 2: Natural Hedges**

Some assets naturally benefit from rising rates and can offset losses elsewhere:

```
Natural Rate Hedges:
  Asset                         | Benefit from Rising Rates
  ------------------------------|-----------------------------------
  Bank stocks                   | Net interest margins expand
  Insurance companies           | Investment income increases
  Floating-rate bonds/loans     | Coupon payments increase
  Cash and money markets        | Yields increase
  Short positions in bonds      | Profit from bond price declines
  Treasury Inflation Protected  | Protect against inflation-driven
    Securities (TIPS)           |   rate increases
```

**Strategy 3: Derivative Hedges**

```
Interest Rate Derivatives for Hedging:

  Instrument          | How It Hedges                      | Complexity
  --------------------|------------------------------------|-----------
  Treasury futures    | Short futures profit when          | Moderate
    (short)           | rates rise                         |
  Interest rate swaps | Pay fixed/receive floating to      | High
                      | benefit from rising rates          |
  Put options on      | Right to sell bonds at a set       | Moderate
    bond ETFs         | price, limiting downside           |
  Swaptions           | Option to enter an interest        | Very High
                      | rate swap                          |
  Rate caps/floors    | Insurance against rate moves       | High
                      | beyond a threshold                 |
```

**Strategy 4: Sector Rotation**

```
Rate-Based Sector Rotation Framework:

  Rates Rising:
    Overweight --> Financials, Energy, Industrials, Materials
    Underweight --> Utilities, REITs, Consumer Staples, High-Growth Tech

  Rates Falling:
    Overweight --> Utilities, REITs, Growth Tech, Consumer Staples
    Underweight --> Financials (short-term), Cyclicals

  Rates Stable (High):
    Overweight --> Quality, Dividends, Value
    Underweight --> Speculative Growth, Leveraged Companies

  Rates Stable (Low):
    Overweight --> Growth, Innovation, Leverage plays
    Underweight --> Cash, Short-duration fixed income
```

**Strategy 5: Multi-Asset Rate Sensitivity Dashboard**

```
Asset Class          | Duration | Direction | Magnitude of
                     | Estimate | of Impact | Rate Sensitivity
---------------------|----------|-----------|------------------
Cash                 | 0        | Positive  | Zero price risk
T-Bills (3-month)    | 0.25     | Positive  | Negligible
2-Year Treasury      | 2        | Negative  | Low
10-Year Treasury     | 8        | Negative  | Moderate
30-Year Treasury     | 20       | Negative  | High
IG Corporate Bonds   | 7        | Negative  | Moderate
HY Corporate Bonds   | 4        | Negative  | Low-Moderate
TIPS                 | 7        | Mixed     | Depends on type of rate move
Value Stocks         | 12       | Negative  | Low
S&P 500              | 20       | Negative  | Moderate
Growth Stocks        | 35       | Negative  | High
REITs                | 15       | Negative  | High
Gold                 | 15       | Negative  | Moderate (real rates)
Commodities (ex-gold)| N/A      | Mixed     | Moderate
Bank Stocks          | -5       | Positive  | Moderate (benefit)
Floating-Rate Loans  | 0.25     | Positive  | Low (benefit)
```

---

### c) Common Misconceptions

**Misconception 1: "Only bonds are affected by interest rates."**

This is the most dangerous misconception. As we have shown, equities, real estate, commodities, and even private investments are all profoundly affected by interest rates. The 2022 experience should have dispelled this myth permanently: the Nasdaq fell 33%, the S&P 500 fell 18%, REITs fell 25%, and long-term bonds fell 30% -- all driven primarily by rising interest rates. Understanding rate sensitivity across all asset classes is essential for portfolio construction.

**Misconception 2: "Growth stocks always outperform value stocks."**

Growth stocks outperformed value from roughly 2007 to 2021, leading many investors to believe this was a permanent state. But this outperformance coincided with a secular decline in interest rates. When rates rose sharply in 2022, value outperformed growth by the widest margin in decades. The growth-value cycle is heavily influenced by the rate cycle. Neither style is permanently superior; it depends on the rate environment.

**Misconception 3: "Rising rates are always bad for stocks."**

This is an oversimplification. The reason rates are rising matters enormously. If rates rise because the economy is booming and corporate profits are surging, stocks can do well despite higher rates. The rate increase is offset by higher earnings. If rates rise because inflation is out of control and the Fed is slamming on the brakes, stocks suffer because higher rates coincide with deteriorating earnings. Context matters more than direction.

**Misconception 4: "REITs are just like bonds."**

REITs and bonds both produce income, but REITs also offer growth potential through rent increases and property appreciation. During periods of moderate inflation and stable rates, REITs can perform well because rents adjust upward. REITs suffer most during rapid rate increases (like 2022) but can recover when rates stabilize, even at higher levels. Treating REITs as bond substitutes misses their growth dimension.

**Misconception 5: "Gold is an inflation hedge."**

Gold's relationship with inflation is indirect. Gold is better described as a hedge against negative real interest rates. When real rates are deeply negative (inflation is much higher than interest rates), gold shines. When real rates are positive and rising, gold struggles -- even if inflation itself is elevated. In 2022, inflation was running at 8-9%, but gold fell slightly because real rates were rising rapidly.

**Misconception 6: "You can hedge rate risk perfectly."**

While derivative instruments can hedge specific rate exposures, perfectly hedging an entire portfolio's rate sensitivity is extremely difficult and expensive. Different assets respond to different parts of the yield curve (short rates vs. long rates), different types of rate moves (nominal vs. real), and with different timing. Over-hedging can be as costly as under-hedging if rates move in your favor and you have eliminated that upside.

**Misconception 7: "Low rates are good for everyone."**

Low rates help borrowers but hurt savers. They boost asset prices but also inflate speculative bubbles. They make pensions and insurance companies' liabilities more expensive to fund. They encourage excessive risk-taking and malinvestment. The "everything bubble" thesis argues that persistently low rates inflated all asset prices to unsustainable levels, creating fragility that was revealed when rates normalized.

---

### d) Common Questions and Answers

**Q1: How do I calculate the duration of my stock portfolio?**

A: There is no standard calculation for equity duration like there is for bond duration. However, you can approximate it using sensitivity analysis. Look at how your portfolio (or similar portfolios) performed during the 2022 rate hiking cycle. If your portfolio fell 25% while rates rose 3%, your portfolio's effective duration is approximately 25/3 = 8.3 "years" of duration. More sophisticated approaches use dividend discount models to estimate the weighted-average timing of expected cash flows.

**Q2: Should I move entirely to value stocks when rates are rising?**

A: Dramatic style shifts are usually a mistake. Rate environments change, and if you are wrong about the direction of rates, you will underperform. A better approach is to tilt your portfolio modestly toward lower-duration assets when you expect rates to rise. Instead of a 60/40 growth/value split, you might shift to 45/55. This captures some of the rate-driven outperformance without making a concentrated bet.

**Q3: How do banks benefit from rising rates?**

A: Banks profit from the "net interest margin" (NIM) -- the difference between what they earn on loans and what they pay on deposits. When rates rise, banks can often increase lending rates faster than deposit rates, expanding their NIM. However, this benefit has limits. If rates rise too fast or too far, loan defaults increase, deposit competition intensifies, and bond portfolios (which banks hold) lose value. The optimal environment for banks is gradually rising rates with a steep yield curve.

**Q4: Why do utility stocks act like bonds?**

A: Utilities have several bond-like characteristics: stable and predictable cash flows, high dividend payouts, regulated returns on capital, and significant leverage. Because their earnings are stable and regulated, investors value utilities primarily for their dividends. When rates rise, the relative attractiveness of utility dividends declines (why take equity risk for a 3.5% yield when Treasuries yield 5%?), and their stock prices fall. When rates fall, utility stocks rally as their yields become more attractive.

**Q5: How does the yield curve shape affect asset allocation?**

A: The yield curve (the difference between long-term and short-term rates) provides important signals. A steep curve (long rates much higher than short rates) favors banks and financial stocks. A flat curve suggests the economy is slowing. An inverted curve (short rates above long rates) has preceded every US recession since 1970. When the curve inverts, consider shifting to defensive assets. When it steepens from inversion, the recession is usually either underway or imminent -- but the subsequent recovery often favors cyclical assets.

**Q6: Should I avoid real estate when rates are rising?**

A: Not necessarily. Location, property type, and lease structure matter enormously. Properties with short-term leases (like hotels or self-storage) can adjust rents upward to offset higher financing costs. Properties in supply-constrained markets may hold value despite higher rates. And if you are buying (not already owning), higher rates often create buying opportunities as sellers capitulate. The key is understanding how much leverage is involved and whether cash flows can support higher financing costs.

**Q7: How do negative interest rates affect these frameworks?**

A: Negative rates (which existed in Europe and Japan) push these dynamics to extremes. With negative rates, all asset durations effectively increase because the discount rate is lower. Cash becomes costly to hold (you pay the bank to store it). Asset prices are supported by the extreme cheapness of financing. When rates eventually normalize from negative levels, the adjustment can be violent -- as European bond markets experienced in 2022 when the ECB began raising rates from -0.5%.

**Q8: How do TIPS (Treasury Inflation-Protected Securities) fit into this framework?**

A: TIPS are unique because they are sensitive to real interest rates, not nominal rates. If nominal rates rise because inflation expectations increase, TIPS are relatively protected (their principal adjusts for inflation). If nominal rates rise because real rates increase (tighter monetary policy), TIPS decline like regular bonds. TIPS are most valuable when you expect inflation to exceed market expectations but real rates to remain stable or decline.

**Q9: How quickly do different asset classes react to rate changes?**

A: Publicly traded assets (stocks, REITs, publicly traded bonds) react within minutes to hours. Private real estate takes months to reprice because appraisals lag market conditions. Private equity valuations adjust quarterly. Bank deposit rates are "sticky" -- they move slowly even when market rates change rapidly. Understanding these timing differences helps you anticipate which assets will be affected first and which will follow with a lag.

**Q10: What is the single most important thing to monitor regarding rates?**

A: The real interest rate -- the nominal rate minus inflation expectations. This is the true cost of capital for the economy. Most asset classes respond more to real rates than nominal rates. You can approximate real rates by looking at TIPS yields (which directly reflect real rates) or by subtracting breakeven inflation expectations from nominal Treasury yields. When real rates are rising, almost all asset classes face headwinds. When real rates are falling, almost all asset classes get a tailwind.

---

## YouTube Script

---

**[VISUAL: Title card -- "Week 34: Interest Rate Sensitivity Across Assets" with a rising interest rate curve superimposed over various asset icons: stocks, bonds, houses, gold bars]**

**Alex:** Welcome back. Last week, we covered credit analysis. Today, we are going even broader. We are going to talk about the gravitational force of all financial markets -- interest rates. And I do not just mean how rates affect bonds. I mean how rates affect everything.

**Sam:** Everything? I know higher rates make bond prices go down, but are stocks and real estate really that connected to rates?

**Alex:** Let me answer with a question. What was the worst-performing major asset class in 2022?

**Sam:** I would guess long-term bonds? Or maybe the Nasdaq?

**Alex:** Trick question -- they performed almost identically. The 30-year Treasury fell about 33%. The Nasdaq-100 fell about 33%. And the reason was the same: interest rates went from near zero to over 4% in just nine months.

**[VISUAL: Side-by-side chart showing 2022 performance of 30-year Treasuries and Nasdaq-100, both declining roughly 33%]**

**Sam:** Wait, the same percentage? That cannot be a coincidence.

**Alex:** It is not. And this is the key insight of today's lesson: stocks have duration, just like bonds. Duration measures how sensitive an asset's price is to changes in interest rates. Growth stocks, especially unprofitable growth stocks, have extremely long duration -- sometimes 40 to 60 years.

**Sam:** How can a stock have "duration"? That is a bond concept.

**Alex:** Think about what determines a stock's value. It is the present value of all future cash flows -- dividends, earnings, free cash flow stretching decades into the future. You discount those cash flows back to today using a discount rate that includes the risk-free interest rate. When rates go up, that discount rate goes up, and the present value goes down.

**[ANIMATION: Reference animation/week34_rate_sensitivity.py -- Animated visualization showing a timeline of future cash flows for two companies: a value stock with large near-term cash flows that taper off, and a growth stock with small near-term cash flows that grow much larger over time. As the discount rate slider increases, both bars shrink, but the growth stock's bars shrink dramatically more because its cash flows are further in the future.]**

**Alex:** Here is the critical difference between a value stock and a growth stock. A value stock generates most of its cash flows in the next few years. A growth stock generates most of its cash flows 10, 15, 20 years from now. When you raise the discount rate, those distant cash flows get crushed.

**Sam:** So a growth stock is like a long-term bond, and a value stock is like a short-term bond?

**Alex:** Exactly. A mature utility company paying a 4% dividend with slow growth might have an effective duration of 15 years. A high-growth tech company reinvesting all its profits might have a duration of 40 years or more. An unprofitable biotech company? Its duration could be 60 to 80 years.

**[VISUAL: Table showing equity duration by style -- Deep Value (8-12 years), Dividend stocks (12-18), S&P 500 (18-25), Growth (25-40), Unprofitable Growth (40-60+)]**

**Sam:** That explains why the ARK Innovation ETF fell 67% in 2022 while the S&P only fell 18%.

**Alex:** Precisely. ARK was loaded with unprofitable, high-growth companies -- the longest-duration equities you can buy. When rates went up 4 percentage points, those stocks were devastated. Meanwhile, bank stocks and energy stocks -- short-duration assets -- actually went up.

**Sam:** So the whole growth-versus-value debate is really about interest rates?

**Alex:** To a large degree, yes. Growth massively outperformed value from 2009 to 2021. But that period saw rates falling from about 3% to near zero. It was a 12-year tailwind for long-duration assets. In 2022, when rates reversed sharply, value outperformed growth by the widest margin in decades.

**[VISUAL: 20-year chart showing growth vs. value performance with the 10-year Treasury yield overlaid, showing the inverse relationship]**

**Alex:** This does not mean growth is bad or value is good. It means the rate environment determines which style has the wind at its back. Neither is permanently superior.

**Sam:** OK, what about real estate? I know mortgage rates matter, but how big is the impact?

**Alex:** Real estate might be the single most interest-rate-sensitive major asset class, and for three distinct reasons.

**[VISUAL: Three-pillar graphic -- "Financing Costs," "Cap Rates," "Demand" -- each connected to interest rates]**

**Alex:** Pillar one: financing costs. Most real estate is bought with 60 to 70 percent debt. When the interest rate on that debt goes from 4% to 7%, the annual interest expense nearly doubles. For our example of a ten-million-dollar property with 65% leverage, the cash flow to the equity investor drops by 57%.

**Sam:** 57%? From a 3-percentage-point rate increase?

**Alex:** Yes, because leverage amplifies the impact. This is the double-edged sword of leverage -- it magnifies returns on the way up and magnifies losses on the way down.

**[VISUAL: Before/after comparison showing the same property's cash flow at 4% vs 7% interest rates, with the equity investor's cash flow highlighted]**

**Alex:** Pillar two: cap rate expansion. The cap rate is real estate's version of the earnings yield. When interest rates rise, investors demand higher cap rates. And when cap rates rise, property values fall. A 200-basis-point increase in cap rates can reduce a property's value by nearly 30%.

**Sam:** That is enormous. And what is the third pillar?

**Alex:** Demand reduction. Consider residential housing. A 30-year mortgage at 3% on a $400,000 loan costs $1,686 per month. At 7%, the same loan costs $2,661 per month -- that is 58% more. Many potential buyers simply cannot afford that, so demand drops, inventory builds, and prices soften.

**[ANIMATION: Reference animation/week34_rate_sensitivity.py -- Animated bar chart showing monthly mortgage payments at different interest rates from 3% to 8% on a $400,000 loan, with each bar growing taller and a "buyer affordability threshold" line showing fewer and fewer buyers can afford the payment as rates rise.]**

**Sam:** What about commercial real estate? I have heard the office market is in trouble.

**Alex:** Office is facing a double whammy -- higher rates plus the secular shift to remote work. Some office buildings have lost 40 to 50 percent of their value. But not all real estate is equally affected. Industrial properties like warehouses and data centers have strong secular demand that partially offsets rate headwinds. Self-storage has short-term leases that allow quick rent adjustments.

**[VISUAL: Table showing real estate sectors by rate sensitivity, from "Very High" (Office) to "Lower" (Cell Towers, Healthcare)]**

**Sam:** Let us talk about commodities. Gold went up a lot recently, but I have also heard gold does poorly when rates rise?

**Alex:** This is where the misconceptions run deep. People say gold is an inflation hedge. But that is imprecise. Gold is really a hedge against negative real interest rates.

**Sam:** What are real interest rates?

**Alex:** The real rate is the nominal interest rate minus inflation. If the nominal rate is 5% and inflation is 3%, the real rate is 2%. If the nominal rate is 2% and inflation is 5%, the real rate is negative 3%.

**[VISUAL: Simple equation graphic -- "Real Rate = Nominal Rate - Inflation" with examples showing positive and negative real rates]**

**Alex:** Gold does not generate any income -- no dividends, no coupons, no rent. So when real rates are positive and rising, holding gold means you are giving up meaningful yield to own a non-yielding asset. The opportunity cost is high, and gold tends to decline.

**Sam:** But when real rates are negative?

**Alex:** When real rates are negative, cash is losing purchasing power even in a savings account. In that environment, gold's zero yield does not look so bad compared to a guaranteed real loss. That is when gold tends to shine.

**[VISUAL: Scatter plot showing gold price changes vs. real interest rate changes, demonstrating the inverse relationship with ~-0.7 correlation]**

**Sam:** What about other commodities like oil and copper?

**Alex:** They work through different channels. Higher rates strengthen the dollar, and since commodities are priced in dollars, a stronger dollar puts downward pressure on commodity prices. Higher rates also slow economic growth, reducing demand for industrial commodities. But the supply side matters too -- if rates are high enough to discourage new mining or drilling, future supply constraints can eventually push prices higher.

**Sam:** So commodity analysis is complicated.

**Alex:** It is. There is no single clean relationship like there is for bonds. You have to think about which channel dominates in each specific situation.

**Sam:** Let us talk about corporate behavior. You mentioned that rates affect how companies use leverage and buybacks.

**Alex:** This is hugely important and often overlooked. During the low-rate era from 2010 to 2021, US companies bought back over seven trillion dollars in stock. A large portion was funded by cheap debt.

**[VISUAL: Chart showing cumulative stock buybacks by US companies over the past 15 years, with the Fed Funds rate overlaid]**

**Alex:** The math was simple. Borrow at 3%, buy back stock with a 5% earnings yield, and you create 2% of value for remaining shareholders. But when borrowing costs go to 6 or 7 percent, the math flips. Now buybacks destroy value. The company would be better off paying down debt.

**Sam:** So do buybacks stop when rates rise?

**Alex:** They slow dramatically. Companies shift from "buy back stock and increase leverage" mode to "pay down debt and strengthen the balance sheet" mode. This matters for equity investors because a significant portion of equity returns over the past decade came from buyback-driven EPS growth. Remove that tailwind, and equity returns may be more modest going forward.

**[VISUAL: Two-scenario comparison showing how the same $1B buyback is EPS-accretive at 3% rates but EPS-dilutive at 7% rates]**

**Sam:** Which sectors are most vulnerable to this?

**Alex:** Any sector with high leverage is vulnerable. Utilities, REITs, telecoms, and especially private-equity-backed companies, which often carry 5 to 8 times debt-to-EBITDA. When rates rise 3 percentage points on that much debt, it can turn a comfortable situation into a crisis.

**Sam:** So how do I put all of this together for my portfolio?

**Alex:** That is where rate regime mapping comes in. I think about four distinct rate environments, and each one favors a different mix of assets.

**[ANIMATION: Reference animation/week34_rate_sensitivity.py -- Four-quadrant animated diagram showing rate regimes (Low/Falling, Low/Rising, High/Stable, High/Falling) with asset class performance indicators rotating into each quadrant. For each regime, favored assets light up green and challenged assets turn red.]**

**Alex:** Regime one: low and falling rates. Think 2010 to 2020. Growth stocks, long bonds, REITs, and gold all benefited. Regime two: low and rising rates. Think 2022. Value stocks, bank stocks, floating-rate instruments, and cash were the winners. Regime three: high and stable rates. Think the mid-2000s. High-quality bonds, dividend stocks, and quality companies do well. Regime four: high and falling rates. Think the early 1980s. Everything rallies because the starting yields are high and rates are declining.

**Sam:** Which regime are we in now?

**Alex:** That is the critical question every investor needs to answer for themselves. Look at the level of rates relative to history, the direction they are heading, the speed of change, and what the market expects. The answers to these questions should drive your asset allocation.

**[VISUAL: Rate regime identification decision tree/flowchart]**

**Sam:** What if I am wrong about the direction of rates?

**Alex:** That is why hedging matters. There are several approaches. The simplest is duration management -- if you think rates are rising, shorten your portfolio's duration by owning more value stocks, shorter-term bonds, and less real estate. If you think rates are falling, extend duration.

**Sam:** What about using derivatives to hedge?

**Alex:** You can use Treasury futures, interest rate swaps, or options on bond ETFs to hedge rate exposure. But for most individual investors, the simpler approach is more practical: use asset allocation and sector rotation to manage rate sensitivity. Tilt toward financials and value when you expect rising rates. Tilt toward growth and REITs when you expect falling rates.

**Sam:** Are there any natural hedges -- assets that benefit from rising rates?

**Alex:** Yes. Bank stocks tend to benefit because their net interest margins expand. Insurance companies earn more on their investment portfolios. Floating-rate loans and bonds see their coupon payments increase. Cash and money market funds start yielding more. These can serve as natural offsets to the rate sensitivity in the rest of your portfolio.

**[VISUAL: "Natural Rate Hedges" table showing assets that benefit from rising rates with explanations of why]**

**Sam:** What is the single most important rate metric I should watch?

**Alex:** The real interest rate. Not the nominal rate, not the Fed Funds rate, but the real rate -- the nominal rate minus inflation expectations. You can see this directly by looking at TIPS yields. When real rates are rising, almost every asset class faces headwinds. When real rates are falling, almost everything gets a boost. Real rates are the true gravitational force of financial markets.

**[VISUAL: 20-year chart of real interest rates (TIPS yields) with annotations showing how different asset classes performed during different real rate regimes]**

**Sam:** This has been eye-opening. Let me try to summarize. Stocks have duration just like bonds -- growth stocks have long duration and are very rate-sensitive, while value stocks have shorter duration. Real estate is extremely rate-sensitive because of leverage, cap rates, and demand effects. Gold responds to real rates, not nominal rates. And I should map the rate regime to my asset allocation.

**Alex:** That is an excellent summary. And remember -- the reason rates are changing matters as much as the direction. Rising rates driven by strong economic growth are very different from rising rates driven by inflation and Fed tightening. Context is king.

**Sam:** Thanks Alex. Next week we dive into advanced financial statement analysis. I am looking forward to getting into the weeds on earnings quality.

**Alex:** It will be a great one. We will cover some of my favorite tools for detecting accounting manipulation. See you next week.

**[VISUAL: End card with key takeaways:
1. Equities have duration -- growth stocks are long-duration, value stocks are short-duration
2. Real estate is among the most rate-sensitive asset classes due to leverage and cap rate effects
3. Gold responds to real interest rates, not nominal rates or inflation directly
4. Rate regimes (level + direction) should drive asset allocation decisions
5. The real interest rate is the single most important rate metric to monitor]**

---

*End of Week 34*
