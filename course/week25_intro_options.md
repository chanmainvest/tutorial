# Week 25: Introduction to Options

## Reading Section

### a) Why This Is Important

Options are one of the most powerful and versatile financial instruments available to individual investors. Yet they are also one of the most misunderstood. Many investors avoid options entirely because they seem complex or risky. Others dive in without proper understanding and suffer painful losses. Neither approach is optimal.

Understanding options is important for several reasons:

**Risk Management (Hedging):** Options were originally created as insurance contracts. Just as you buy home insurance to protect against catastrophic loss, you can buy options to protect your investment portfolio. A long-term investor holding $500,000 in stocks can purchase protective puts for a fraction of that amount, ensuring they will never lose more than a predetermined percentage even in a market crash. Without options knowledge, you are essentially driving without insurance.

**Income Generation:** Options can generate consistent income on stocks you already own or stocks you would like to own. Covered calls and cash-secured puts (which we will explore in Weeks 27 and 28) can produce yields of 8-15% annually, often 2-3 times what dividends alone would provide. In a flat or mildly bullish market, this income can make a significant difference in your total returns.

**Capital Efficiency:** Options allow you to control a large amount of stock with a relatively small capital outlay. One options contract controls 100 shares. This leverage can be used responsibly to enhance returns or irresponsibly to blow up an account. Understanding the mechanics helps you stay on the right side of that line.

**Market Insight:** Even if you never trade a single option, understanding how the options market works gives you valuable insight into market sentiment. The VIX (Volatility Index), implied volatility, put/call ratios, and unusual options activity all provide signals about what large, sophisticated investors expect the market to do. This information is hiding in plain sight for those who understand how to read it.

**Better Stock Investing:** Options knowledge makes you a better stock investor. When you understand concepts like time decay and implied volatility, you gain a deeper appreciation for the role that time and uncertainty play in all investments, not just options. You begin to think probabilistically, which is how the best investors in the world approach markets.

In this course, we focus on four specific, conservative options strategies that complement a long-term investment approach. We are not teaching you to be a day trader or a speculative options gambler. We are teaching you to use options as tools that enhance your existing investment strategy.

---

### b) What You Need to Know

#### What Is an Option?

An option is a contract that gives the buyer the **right, but not the obligation**, to buy or sell a specific stock at a specific price on or before a specific date. This is the single most important sentence in options education. Read it again.

The key word is **right**. The buyer of an option has a choice. They can exercise the option if it benefits them, or they can let it expire worthless if it does not. The seller (also called the writer) of an option has an **obligation**. If the buyer chooses to exercise, the seller must fulfill the contract.

This asymmetry between rights and obligations is what makes options unique and is the foundation of everything that follows.

#### The Two Types: Calls and Puts

There are only two types of options:

**Call Option:** Gives the buyer the right to **buy** a stock at a specific price.
- You buy a call when you think the stock will go UP.
- Think of it as a "reservation to buy."

**Put Option:** Gives the buyer the right to **sell** a stock at a specific price.
- You buy a put when you think the stock will go DOWN (or want to protect against it).
- Think of it as an "insurance policy."

Every option contract has four essential components:

```
+----------------------------------------------------------+
|                    OPTION CONTRACT                        |
|                                                          |
|  1. UNDERLYING ASSET:  The stock (e.g., AAPL, MSFT)     |
|  2. STRIKE PRICE:      The agreed upon price             |
|  3. EXPIRATION DATE:   When the contract expires         |
|  4. TYPE:              Call or Put                        |
|                                                          |
|  Example: "AAPL Jan 17 2026 $200 Call"                   |
|  = Right to BUY 100 shares of AAPL at $200/share        |
|    on or before January 17, 2026                         |
+----------------------------------------------------------+
```

#### Contract Size

One options contract controls **100 shares** of the underlying stock. This is standard across U.S. equity options. When you see an option quoted at $3.50, you pay $3.50 per share, meaning $350 per contract ($3.50 x 100 shares).

```
Option Price (Premium):   $3.50 per share
Shares per Contract:      x 100
Total Cost per Contract:  = $350.00
```

#### Rights vs. Obligations

This table clarifies who has rights and who has obligations:

```
+------------------+------------------------+------------------------+
|                  |     CALL OPTION        |     PUT OPTION         |
+------------------+------------------------+------------------------+
|  BUYER (Long)    | Right to BUY stock     | Right to SELL stock    |
|                  | at strike price        | at strike price        |
|                  | Pays premium           | Pays premium           |
|                  | Max loss = premium     | Max loss = premium     |
+------------------+------------------------+------------------------+
|  SELLER (Short)  | Obligation to SELL     | Obligation to BUY      |
|                  | stock at strike price  | stock at strike price  |
|                  | Receives premium       | Receives premium       |
|                  | Max loss = unlimited*  | Max loss = large**     |
+------------------+------------------------+------------------------+

*  For naked calls, loss is theoretically unlimited as stock can rise infinitely.
** For naked puts, max loss = strike price x 100 (if stock goes to $0).
```

#### Strike Price and Moneyness

The **strike price** (also called the exercise price) is the price at which the option holder can buy (for calls) or sell (for puts) the underlying stock.

The relationship between the strike price and the current stock price determines the option's **moneyness**:

**For Call Options:**

```
Stock Price = $150

  In-The-Money (ITM)     At-The-Money (ATM)    Out-of-The-Money (OTM)
  Strike < Stock Price    Strike = Stock Price   Strike > Stock Price
  Strike = $140           Strike = $150          Strike = $160
  Intrinsic Value = $10   Intrinsic Value = $0   Intrinsic Value = $0
       |                       |                       |
       v                       v                       v
  [====|==========]       [=========|=]           [==========|====]
  $130  $140  $150        $140  $150  $160        $150  $160  $170
       Higher Value            Some Value              Lower Value
       Higher Premium          Moderate Premium        Lower Premium
```

**For Put Options (opposite direction):**

```
Stock Price = $150

  In-The-Money (ITM)     At-The-Money (ATM)    Out-of-The-Money (OTM)
  Strike > Stock Price    Strike = Stock Price   Strike < Stock Price
  Strike = $160           Strike = $150          Strike = $140
  Intrinsic Value = $10   Intrinsic Value = $0   Intrinsic Value = $0
```

The moneyness of an option directly affects its price and behavior. ITM options are more expensive, move more closely with the stock, and have higher probability of being exercised. OTM options are cheaper, move less with the stock, and usually expire worthless.

#### Intrinsic Value vs. Extrinsic Value

Every option's price (called the **premium**) is composed of two parts:

**Intrinsic Value** = The amount the option is in the money. This is the value the option would have if exercised right now.
- For calls: max(0, Stock Price - Strike Price)
- For puts: max(0, Strike Price - Stock Price)

**Extrinsic Value** (also called Time Value) = Everything else. This is the extra premium above intrinsic value that reflects the possibility of the option becoming more valuable before expiration.

```
Option Premium = Intrinsic Value + Extrinsic Value

Example: AAPL trading at $155
AAPL $150 Call trading at $8.50

Intrinsic Value  = $155 - $150 = $5.00  (the option is $5 in the money)
Extrinsic Value  = $8.50 - $5.00 = $3.50 (time value, volatility premium)
Total Premium    = $5.00 + $3.50 = $8.50

+---------------------------------------------------+
|              OPTION PREMIUM: $8.50                 |
|                                                    |
|  [===== INTRINSIC: $5.00 =====][== EXTRINSIC ==]  |
|  [===== (In the Money) =======][== $3.50 ======]  |
|                                                    |
|  Intrinsic: Real, tangible     Extrinsic: Hope,   |
|  value right now.              time, uncertainty.  |
|  Cannot be negative.           Decays over time.   |
+---------------------------------------------------+
```

An out-of-the-money option has **zero intrinsic value**. Its entire premium is extrinsic value, meaning it is purely a bet on future movement.

#### The Option Chain

An **option chain** is the full listing of all available options for a particular stock. It shows every available combination of strike price, expiration date, and type (call/put). Here is a simplified representation:

```
                    AAPL Option Chain - Stock Price: $155.00
                    Expiration: March 21, 2026

    ====================== CALLS ======================  ====== PUTS ======
    Bid    Ask    Last   Volume  OI    Strike   Bid    Ask    Last   Volume  OI
    -----------------------------------------------------------------------
    17.20  17.50  17.35   1,205  8,432  $140    1.85   1.95   1.90    892  5,210
    12.40  12.70  12.55   2,847  12,105 $145    3.10   3.25   3.15  1,540  7,890
     8.30   8.55   8.42   5,120  18,760 $150    5.20   5.40   5.30  3,210  11,450
     5.10   5.30   5.20   8,450  22,340 $155    7.80   8.05   7.90  2,870  9,870
     2.85   3.00   2.92   6,780  19,540 $160   11.50  11.80  11.65  1,650  6,540
     1.40   1.55   1.47   4,320  14,890 $165   16.20  16.50  16.35    780  3,210
     0.55   0.65   0.60   2,150   9,870 $170   21.30  21.60  21.45    340  1,890

    ITM calls are above this line    <--- ATM ($155) --->    ITM puts are above
    OTM calls are below this line                            OTM puts are below

    Key:  Bid = highest price buyers will pay
          Ask = lowest price sellers will accept
          OI  = Open Interest (number of existing contracts)
```

Notice several important patterns:
- As you move away from ATM in either direction, premiums decrease.
- ITM options have higher premiums because they contain intrinsic value.
- ATM options typically have the highest volume and open interest (most liquid).
- The bid-ask spread is tightest for ATM options and widens for deep ITM/OTM.

#### Expiration Dates

Options do not last forever. Every option has an **expiration date**, which is the last day the option can be exercised. After this date, the option ceases to exist.

Common expiration cycles:

```
+-------------------------------------------------------------------+
|  TYPE              | EXPIRATION          | TYPICAL USE             |
+-------------------------------------------------------------------+
|  Weekly Options    | Every Friday        | Short-term trading      |
|  Monthly Options   | 3rd Friday of month | Most common, liquid     |
|  Quarterly Options | End of quarter      | Index options           |
|  LEAPS             | 1-3 years out       | Long-term strategies    |
+-------------------------------------------------------------------+

Timeline Example (from today):

  Today          2 weeks       1 month        3 months       1 year
    |               |             |               |             |
    v               v             v               v             v
  [NOW]---[Weekly]---[Monthly]---[Quarterly]------[LEAPS]-------->

  Higher Theta <--------------------------------> Lower Theta
  (faster decay)                                  (slower decay)
  Lower Premium <--------------------------------> Higher Premium
```

**LEAPS** (Long-Term Equity Anticipation Securities) are options with expiration dates more than one year in the future. They are particularly useful for long-term investors because they allow you to take positions with less time decay pressure.

#### American vs. European Style Options

**American-Style Options:** Can be exercised at any time before expiration. Most individual stock options in the U.S. are American-style.

**European-Style Options:** Can only be exercised on the expiration date itself. Most index options (SPX, NDX) are European-style.

```
American Style:
  [Purchase]=====[Can Exercise Any Time]=====[Expiration]
       |                                          |
       +------ Exercise window is OPEN -----------+

European Style:
  [Purchase]=====[Cannot Exercise]=====[Expiration]
       |                                    |
       +-- Can ONLY exercise on this day ---+
```

For our purposes in this course, we will focus on American-style options on individual stocks. The practical difference matters primarily for early assignment risk, which we will address in the covered calls lesson (Week 27).

#### Time Decay (Theta)

One of the most important concepts in options is **time decay**, also known as **theta**. Extrinsic value decays as the option approaches expiration. This decay is not linear; it accelerates as expiration nears.

```
  Extrinsic
  Value ($)
    |
  8 |*
    |  *
  7 |    *
    |      *
  6 |        *
    |          *
  5 |            *
    |              *
  4 |                *
    |                  *
  3 |                    *
    |                      **
  2 |                        **
    |                          ***
  1 |                             ****
    |                                 *******
  0 |____________________________________*****__
    90   75   60   45   30   15    5    0
                Days to Expiration

  Key observation: Most time decay occurs in the LAST 30 days.
  The curve accelerates dramatically in the final 2 weeks.
```

This decay curve has enormous practical implications:

- **Option buyers** are fighting against time. Every day that passes, their option loses value, all else being equal. They need the stock to move enough, fast enough, to overcome this decay.
- **Option sellers** benefit from time decay. They collect premium upfront and profit as that premium erodes. Time is literally on their side.

This is why, in this course, we focus primarily on **option selling strategies** (covered calls and cash-secured puts). As conservative investors, we want time working for us, not against us.

#### Why Options Exist: Three Primary Purposes

**1. Hedging (Insurance)**

A portfolio manager holding $10 million in stocks can buy put options as insurance against a market crash. If the market drops 30%, the puts increase in value, offsetting the stock losses. The cost of this insurance (the put premium) is the price of sleeping well at night.

```
Without Hedging:                    With Protective Puts:
Portfolio: $10M                     Portfolio: $10M
                                    Put Cost: $200K (2%)

Market drops 30%:                   Market drops 30%:
Portfolio: $7M                      Stocks: $7M
Loss: -$3M (-30%)                   Puts gain: +$2.8M
                                    Net: $9.8M - $0.2M = $9.6M
                                    Loss: -$400K (-4%)
```

**2. Speculation (Leverage)**

A trader who believes AAPL will rise from $155 to $175 in the next month could:
- Buy 100 shares at $155 = $15,500 investment, $2,000 profit (+12.9%)
- Buy 1 ATM call for $5.20 = $520 investment, ~$1,480 profit (+284.6%)

The option provides much higher percentage returns but also much higher risk of total loss if the stock does not move as expected.

**3. Income Generation**

An investor holding 500 shares of AAPL at $155 ($77,500 in stock) can sell 5 covered call contracts at the $165 strike for $1.47 each, collecting $735 in premium. If the stock stays below $165, they keep the shares and the $735. Repeating this monthly could generate $8,820 per year, an 11.4% annual yield on top of dividends.

```
Income Comparison (on $77,500 portfolio):

  Dividends Only:          Dividends + Covered Calls:
  AAPL dividend ~0.65%     AAPL dividend ~0.65%
  Annual: ~$504            Covered call income: ~$8,820
                           Annual: ~$9,324
                           Yield: ~12.0%
```

#### Option Pricing: What Determines the Premium?

Six factors affect an option's price:

```
+----------------------------------------------------------------+
| FACTOR               | CALL EFFECT      | PUT EFFECT           |
+----------------------------------------------------------------+
| Stock price UP       | Premium UP       | Premium DOWN         |
| Stock price DOWN     | Premium DOWN     | Premium UP           |
| Strike price (high)  | Premium DOWN     | Premium UP           |
| Time to expiration+  | Premium UP       | Premium UP           |
| Volatility UP        | Premium UP       | Premium UP           |
| Interest rates UP    | Premium UP       | Premium DOWN (minor) |
| Dividends UP         | Premium DOWN     | Premium UP           |
+----------------------------------------------------------------+

Most Important Factors (in order):
1. Stock price relative to strike (intrinsic value)
2. Time to expiration (time value)
3. Implied volatility (market's expected movement)
```

**Implied Volatility (IV)** deserves special attention. IV represents the market's expectation of how much the stock will move in the future. High IV means the market expects large moves (perhaps before an earnings report), so options are expensive. Low IV means the market expects calm conditions, so options are cheap.

```
Implied Volatility and Option Prices:

  Low IV (15-20%):                    High IV (40-50%):
  Stock is expected to be calm.       Stock is expected to be volatile.
  Options are CHEAP.                  Options are EXPENSIVE.
  
  Example: AAPL $155, ATM Call        Example: AAPL $155, ATM Call
  30 days, IV = 18%                   30 days, IV = 45%
  Premium: ~$3.20                     Premium: ~$7.80

  Good time to BUY options.           Good time to SELL options.
```

#### The Greeks: A Practical Introduction

While a deep mathematical understanding of the Greeks is not necessary for the strategies in this course, a working knowledge of the four main Greeks helps you make better decisions.

```
THE FOUR MAIN GREEKS:

+-------------------------------------------------------------------+
| GREEK  | MEASURES                  | PRACTICAL MEANING             |
+-------------------------------------------------------------------+
| DELTA  | Price sensitivity to      | How much the option moves     |
|  (Δ)   | stock price movement      | per $1 stock price change     |
|        | Range: 0 to 1.0 (calls)   | Delta 0.50 = moves $0.50      |
|        | Range: 0 to -1.0 (puts)   | per $1 stock move             |
+-------------------------------------------------------------------+
| GAMMA  | Rate of change of delta   | How much delta changes        |
|  (Γ)   |                           | per $1 stock price change     |
|        |                           | Highest for ATM options       |
+-------------------------------------------------------------------+
| THETA  | Time decay per day        | How much value the option     |
|  (Θ)   | Always negative for       | loses each day from time      |
|        | long options              | decay alone                   |
+-------------------------------------------------------------------+
| VEGA   | Sensitivity to implied    | How much the option price     |
|  (V)   | volatility changes        | changes per 1% change in IV   |
+-------------------------------------------------------------------+
```

**Delta in Practice:**

Delta serves double duty. It tells you how much your option price will change and it gives you an approximate probability that the option will be in the money at expiration.

```
DELTA AS A PROBABILITY GUIDE:

  Delta    Approximate Probability    Moneyness
  =====    ========================   ===========
  0.80     ~80% chance ITM at expiry  Deep ITM
  0.60     ~60% chance ITM at expiry  Slightly ITM
  0.50     ~50% chance ITM at expiry  ATM
  0.30     ~30% chance ITM at expiry  Slightly OTM
  0.15     ~15% chance ITM at expiry  OTM
  0.05     ~5% chance ITM at expiry   Far OTM

  For COVERED CALLS: Sell calls with delta 0.20-0.30
    (20-30% chance of being called away)
  
  For CASH-SECURED PUTS: Sell puts with delta -0.20 to -0.30
    (20-30% chance of being assigned)
```

**Theta in Practice:**

Theta tells you the daily "rent" you pay for holding an option (if you are a buyer) or the daily "rent" you collect (if you are a seller).

```
THETA EXAMPLE:

  AAPL $155 Call, 30 days to expiration
  Price: $4.20
  Theta: -$0.08

  This means:
  - The option loses $0.08 per share per day from time decay
  - Per contract: $0.08 x 100 = $8.00 per day
  - Over a week: $56 in decay (all else equal)
  - Over the full 30 days: Not $240 (because theta accelerates)
    but rather about $350-$400 (since theta increases daily)

  FOR SELLERS: You earn this theta every day. Weekends too.
  FOR BUYERS: You lose this theta every day. The clock never stops.
```

#### Reading an Options Quote

When you look at an option on your brokerage platform, you will see a standardized format. Let us learn to read it:

```
OPTION QUOTE BREAKDOWN:

  AAPL  Mar 21 2026  $160  Call

  |       |            |     |
  |       |            |     +-- Type: Call option
  |       |            +-------- Strike: $160 per share
  |       +--------------------- Expiry: March 21, 2026
  +----------------------------- Underlying: Apple Inc.

  Bid:     $3.20     (price buyers will pay you)
  Ask:     $3.40     (price you must pay to buy)
  Last:    $3.30     (most recent trade price)
  Volume:  2,847     (contracts traded today)
  Open Interest: 18,760  (total existing contracts)
  
  Greeks:
  Delta:   0.35      (moves $0.35 per $1 AAPL move)
  Gamma:   0.025     (delta changes 0.025 per $1 move)
  Theta:   -0.065    (loses $0.065/share per day)
  Vega:    0.18      (changes $0.18 per 1% IV change)
  IV:      24.3%     (implied volatility)
```

#### The VIX: The Market's Fear Gauge

The **VIX** (CBOE Volatility Index) measures the implied volatility of S&P 500 options. It is often called the "fear gauge" because it rises when investors are nervous and drops when they are calm.

```
VIX LEVELS AND WHAT THEY MEAN:

  VIX Level    Market Mood         Options Implication
  =========    ===========         ==================
  10-15        Very calm/complacent Options are CHEAP
  15-20        Normal               Options are fairly priced
  20-25        Elevated concern     Options are getting expensive
  25-30        Fearful              Options are expensive (good for sellers)
  30-40        Very fearful         Options are very expensive
  40+          Panic                Options are extremely expensive
                                    (rare: 2008, 2020 COVID crash)

  KEY INSIGHT FOR OPTION SELLERS:
  When VIX is high (25+), premiums are fat.
  This is the BEST time to sell covered calls and cash-secured puts.
  You get paid more for the same obligation.

  When VIX is low (12-15), premiums are thin.
  You may want to reduce option selling or use tighter strikes.
```

Understanding the VIX gives you an edge in timing your options trades. You do not need to predict market direction, but knowing whether options are cheap or expensive helps you decide how aggressively to sell premium.

#### A Complete Example

Let us walk through a complete, practical example to tie all these concepts together.

**Scenario:** AAPL is trading at $155. You believe it will rise to $170 within 60 days.

**Option chosen:** AAPL $160 Call, expiring in 60 days, trading at $3.50.

```
Analysis:
  Type:              Call (right to buy)
  Strike:            $160
  Current Stock:     $155
  Moneyness:         Out-of-the-money ($5 OTM)
  Intrinsic Value:   $0 (OTM, no intrinsic value)
  Extrinsic Value:   $3.50 (entire premium is time value)
  Cost:              $3.50 x 100 = $350 per contract
  Breakeven:         $160 + $3.50 = $163.50

Possible Outcomes at Expiration:

  Stock at $170:  Option worth $10.00  -> Profit: $650 (+185.7%)
  Stock at $165:  Option worth $5.00   -> Profit: $150 (+42.9%)
  Stock at $163.50: Option worth $3.50 -> Breakeven ($0)
  Stock at $160:  Option worth $0.00   -> Loss: -$350 (-100%)
  Stock at $155:  Option worth $0.00   -> Loss: -$350 (-100%)
  Stock at $150:  Option worth $0.00   -> Loss: -$350 (-100%)

Payoff Diagram:

  Profit
  ($)
    |
 +650|                                          *****
    |                                      ****
 +300|                                 ****
    |                            ****
    0|----------------------*****----- Stock Price ($) --->
    |                  *
 -350|*****************    <-- Max loss = premium paid
    |
    +---|---|---|---|---|---|---|---|---
       140  145  150  155  160  165  170  175

  Breakeven at $163.50 (Strike + Premium)
```

---

### c) Common Misconceptions

**Misconception 1: "Options are always risky and speculative."**

This is perhaps the most damaging misconception. Options themselves are neither inherently risky nor safe. They are tools, and like any tool, their risk depends entirely on how you use them. Buying far out-of-the-money weekly options with your entire account is extremely risky. Selling covered calls on stocks you already own is one of the most conservative strategies in investing. A chain saw is dangerous in the hands of a child, but a lumberjack uses one safely every day. The same principle applies to options.

**Misconception 2: "Most options expire worthless, so selling options is free money."**

While it is true that a significant percentage of options expire worthless (roughly 60-70% of options that are held to expiration), this statistic is misleading. Many options are closed before expiration for a profit. Additionally, when an option seller loses, the loss can be much larger than the premium collected. Selling options is not free money; it is accepting a high probability of small gains in exchange for a low probability of large losses. Responsible position sizing is essential.

**Misconception 3: "Options are too complicated for regular investors."**

The basic strategies we cover in this course (covered calls and cash-secured puts) are straightforward once you understand the fundamentals. You do not need to understand the Black-Scholes model, Greek calculations, or complex multi-leg strategies to use options effectively. A 30-year-old learning to drive does not need to understand internal combustion engineering. Similarly, you can use basic options strategies effectively with a solid understanding of the concepts in this lesson.

**Misconception 4: "If I buy a call option, I have to buy the stock."**

No. The buyer of an option has the **right**, not the obligation. If the option is profitable at expiration, you can either exercise it (buy the stock at the strike price) or simply sell the option to close your position and pocket the profit. Most options traders never exercise; they simply trade the options themselves. If the option is not profitable, you simply let it expire and lose only the premium you paid.

**Misconception 5: "Implied volatility is the same as historical volatility."**

Historical volatility measures how much the stock has actually moved in the past. Implied volatility is the market's expectation of how much it will move in the future. They are related but different. Before earnings announcements, implied volatility can spike well above historical volatility because the market expects a large move. After the announcement, IV typically collapses (known as "IV crush"), even if the stock moves significantly. Understanding this difference is crucial for timing options trades.

**Misconception 6: "A stock option is the same as an employee stock option."**

Exchange-traded options (what we discuss in this course) are standardized contracts traded on public exchanges. Employee stock options (ESOs) are compensation grants from employers with different rules regarding exercise, expiration, taxation, and transferability. While they share the same underlying concept, the mechanics and strategies differ significantly.

---

### d) Common Questions and Answers

**Q1: How much money do I need to start trading options?**

A: The capital requirement depends on the strategy. Buying a single option contract might cost as little as $50-$500. Selling cash-secured puts requires enough cash to buy 100 shares at the strike price (e.g., a $150 strike put requires $15,000 in cash). Covered calls require owning 100 shares of the underlying stock. For most investors starting with conservative options strategies, $10,000-$25,000 is a reasonable starting point, though some brokers allow smaller accounts.

**Q2: What happens if I just let an option expire?**

A: If the option is out of the money at expiration, it expires worthless. You lose the premium you paid (if you bought it) or keep the premium (if you sold it). If the option is in the money at expiration, most brokers will automatically exercise it (known as "auto-exercise"). If you bought an ITM call, you will end up buying 100 shares at the strike price. If you cannot afford this, close the position before expiration.

**Q3: Can I lose more than the premium I paid when buying an option?**

A: No. When you buy an option (long call or long put), your maximum loss is always limited to the premium you paid. This is one of the key advantages of buying options. However, when you sell options (short call or short put), your potential losses can be much larger than the premium received.

**Q4: What is the difference between "open interest" and "volume"?**

A: Volume is the number of contracts traded on a particular day. Open interest is the total number of contracts that currently exist and have not been closed or exercised. High open interest indicates a liquid option with tight bid-ask spreads. Increasing open interest suggests new money is flowing into that option. Volume can exceed open interest if there is heavy day trading.

**Q5: Why should I care about the bid-ask spread?**

A: The bid-ask spread is the difference between the price buyers are willing to pay (bid) and the price sellers are asking (ask). A wide spread means higher transaction costs and makes it harder to enter and exit positions profitably. For example, an option with a bid of $2.00 and ask of $2.50 has a $0.50 spread, meaning you immediately lose $50 per contract when you buy. Always look for options with tight spreads, typically found in high-volume, liquid stocks.

**Q6: Do I need to understand the Greeks to trade options?**

A: For the basic strategies in this course, a deep understanding of the Greeks is not required, but a conceptual understanding of two key Greeks is helpful:
- **Delta:** How much the option price moves when the stock moves $1. A delta of 0.50 means the option gains $0.50 for every $1 the stock rises (for calls).
- **Theta:** How much value the option loses each day from time decay. A theta of -0.05 means the option loses $5 per day ($0.05 x 100 shares).
Understanding delta helps you select appropriate strike prices, and understanding theta helps you appreciate why time works for sellers and against buyers.

**Q7: What stocks are best for options trading?**

A: Look for stocks with: (1) high trading volume and open interest for tight bid-ask spreads, (2) moderate implied volatility for reasonable premiums, (3) stocks you are willing to own long-term (for put selling and covered call strategies), and (4) stocks in the $50-$300 range for manageable position sizes. Popular options-friendly stocks include large-cap names like AAPL, MSFT, AMZN, GOOGL, JPM, and broad ETFs like SPY, QQQ, and IWM.

**Q8: Is there a difference between closing an option and exercising it?**

A: Yes, and this distinction is important. Closing an option means selling it back in the market (if you bought it) or buying it back (if you sold it). Exercising means using the right the option gives you to buy or sell the underlying stock. In most cases, closing is preferable to exercising because closing captures the remaining extrinsic value, while exercising only captures intrinsic value. The only common reason to exercise early is to capture a dividend on an ITM call option.

**Q9: What is assignment, and should I be worried about it?**

A: Assignment occurs when an option seller is required to fulfill their obligation because the option buyer exercised their right. If you sold a call and get assigned, you must sell 100 shares at the strike price. If you sold a put and get assigned, you must buy 100 shares at the strike price. Early assignment is possible with American-style options but is uncommon except when (a) the option is deep in the money near expiration, or (b) there is an upcoming dividend. For the covered call and cash-secured put strategies we teach, assignment is not a disaster; it simply means you sold your stock at your target price (for calls) or bought stock at your target price (for puts).

**Q10: How are options taxed?**

A: Options taxation depends on the strategy and holding period. Generally, option premiums received from selling options are treated as short-term capital gains. If you are assigned on a covered call, the premium is added to your selling price. If you are assigned on a cash-secured put, the premium reduces your cost basis. LEAPS held for more than one year may qualify for long-term capital gains rates. Consult a tax professional for your specific situation, as options taxation can be complex.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 25: Introduction to Options - Level 3: Advanced"]

**Horace:** Welcome back, everyone. Today we are stepping into what I consider one of the most important topics in this entire course. We are talking about options.

**Stella:** Options. I have to be honest, Horace, this is the topic I have been both excited about and a little nervous about. I hear people talk about options and it sounds like gambling.

**Horace:** And that is exactly the misconception we need to address right at the start. Options are tools. A hammer can build a house or break a window. Options can protect your portfolio like insurance, or they can blow up your account like a casino bet. It all depends on how you use them.

[VISUAL: Split screen showing two scenarios - Left: "Options as Insurance" with a shield icon and a portfolio being protected, Right: "Options as Gambling" with dice and a portfolio going to zero]

**Stella:** OK so let us start from the very beginning. What actually IS an option?

**Horace:** An option is a contract. It gives the buyer the right, but not the obligation, to buy or sell a specific stock at a specific price on or before a specific date. Let me repeat that because it is the single most important definition you will learn today. The right, but not the obligation.

**Stella:** So it is like a choice. I have the option to do something, but I do not have to.

**Horace:** Exactly. And this is what separates options from other financial instruments. When you buy stock, you own it, period. When you buy a futures contract, you are obligated to fulfill it. But when you buy an option, you have a choice. You will only exercise it if it benefits you.

[VISUAL: Three boxes side by side: "Stock = You OWN it", "Futures = You MUST fulfill", "Option = You CHOOSE"]

**Stella:** Got it. So there are two types, right? Calls and puts?

**Horace:** Right. A call option gives you the right to BUY a stock at a specific price. A put option gives you the right to SELL a stock at a specific price. That is it. Those are the only two building blocks. Every options strategy in existence is built from some combination of calls and puts.

**Stella:** Let me make sure I have this straight. If I think a stock is going up, I want a call because that gives me the right to buy at a lower price?

**Horace:** Exactly right. And if you think a stock is going down, or if you want to protect against a drop, you want a put because that gives you the right to sell at a higher price.

[VISUAL: Two cards appear - "CALL: Right to BUY - Bullish bet" and "PUT: Right to SELL - Bearish bet / Insurance"]

**Stella:** Now I have heard the terms "strike price" and "expiration date." Can you explain those?

**Horace:** Sure. Every option has four essential components. The underlying stock, like Apple or Microsoft. The type, call or put. The strike price, which is the agreed-upon price for the transaction. And the expiration date, which is when the contract expires.

[ANIMATION: Reference animation/week25_option_payoff.py - Animation showing an option contract being assembled piece by piece. First the stock ticker appears, then the type (call/put), then the strike price slides in, then the expiration date stamps on. The assembled contract then shows a payoff diagram that builds as the stock price moves along the x-axis.]

**Horace:** Let me give you a concrete example. Let us say Apple is trading at $155. You buy an "AAPL January 17, 2026, $160 Call." That means you have the right to buy 100 shares of Apple at $160 per share, any time before January 17, 2026.

**Stella:** Wait, did you say 100 shares? Why 100?

**Horace:** Every standard options contract controls 100 shares. This is important because it affects your calculations. If the option is quoted at $3.50, you are not paying $3.50. You are paying $3.50 per share times 100 shares, which equals $350 per contract.

**Stella:** Oh, that is something I could see tripping people up.

**Horace:** Absolutely. It trips up beginners all the time. Always multiply by 100 to get your actual cost.

[VISUAL: Calculator animation: "$3.50 per share x 100 shares = $350 per contract"]

**Stella:** OK, so I have heard the phrase "in the money" thrown around a lot. What does that mean?

**Horace:** Great question. This is about the relationship between the strike price and the current stock price. We call it "moneyness." There are three states. In the money means the option has intrinsic value right now. At the money means the strike price equals the stock price. Out of the money means the option has no intrinsic value.

**Stella:** Can you give me an example?

**Horace:** Sure. Apple is at $155. If you have a call option with a $140 strike, that is in the money because you could buy the stock at $140 and it is worth $155. That is $15 of intrinsic value. If your call has a $155 strike, it is at the money. And if your call has a $170 strike, it is out of the money because it would not make sense to exercise the right to buy at $170 when the stock is only at $155.

[VISUAL: A number line showing stock price at $155, with markers at different strike prices. $140 labeled "ITM - $15 intrinsic value", $155 labeled "ATM", $170 labeled "OTM - no intrinsic value". Color coding: green for ITM, yellow for ATM, red for OTM]

**Stella:** And for puts it is the opposite?

**Horace:** Exactly. A put with a $170 strike is in the money when the stock is at $155, because you could sell at $170 when it is only worth $155. A put with a $140 strike is out of the money.

**Stella:** This brings up another question. You mentioned intrinsic value. What is the other part of the option's price?

**Horace:** Every option's price, which we call the premium, has two components. Intrinsic value, which is the real tangible value, and extrinsic value, which is everything else. Extrinsic value is also called time value, though that is slightly imprecise because it also includes volatility premium.

**Stella:** Can you break that down with numbers?

**Horace:** Let us say Apple is at $155 and the $150 call is trading at $8.50. The intrinsic value is $5, because the stock is $5 above the strike price. The extrinsic value is $8.50 minus $5, which is $3.50. That $3.50 represents the market's assessment of the possibility that the option could become even more valuable before it expires.

[VISUAL: A stacked bar chart showing the option premium of $8.50 broken into two segments: $5.00 intrinsic (solid green) and $3.50 extrinsic (striped blue)]

**Stella:** And an out-of-the-money option has no intrinsic value?

**Horace:** Correct. An out-of-the-money option's entire premium is extrinsic value. It is all hope and time. That is why OTM options are cheaper, and it is also why they lose value faster as expiration approaches.

**Stella:** That leads perfectly into time decay, which I keep hearing about. Can you explain that?

**Horace:** Time decay, technically called theta, is the rate at which an option loses extrinsic value as it approaches expiration. And here is the critical thing: it is not linear. The decay accelerates as you get closer to expiration.

[ANIMATION: Reference animation/week25_option_payoff.py - A second animation sequence showing a time decay curve. An option starts with 90 days to expiration and $8 of extrinsic value. As a clock ticks and days count down, the extrinsic value decreases slowly at first, then the curve steepens dramatically in the last 30 days, with the last week showing the fastest decay. Numbers update in real-time. A "days remaining" counter ticks down alongside.]

**Horace:** Imagine you have 90 days until expiration. In the first 30 days, the option might lose about 15% of its time value. In the middle 30 days, maybe another 25%. But in the last 30 days, it loses the remaining 60%. And in the final week, the decay is brutal.

**Stella:** So if you are buying options, time is your enemy.

**Horace:** Precisely. Every single day, your option loses a little value, and that loss accelerates. You need the stock to move enough, in the right direction, fast enough, to overcome this natural erosion.

**Stella:** And if you are selling options?

**Horace:** Then time is your best friend. You collect premium upfront and profit as it decays. This is why, in this course, we focus heavily on option selling strategies. We want time on our side.

[VISUAL: Two panels - Left: "Option Buyer" with a melting ice cream cone labeled "Time Value" and text "Time is your ENEMY". Right: "Option Seller" with a piggy bank getting larger as coins drop in, text "Time is your FRIEND"]

**Stella:** Speaking of buying and selling, can we talk about the difference between the buyer and the seller? Because I know one has rights and the other has obligations.

**Horace:** This is crucial. The buyer of an option pays the premium and gets a right. The seller of an option collects the premium and takes on an obligation. Let me walk through each scenario.

**Horace:** If you buy a call, you have the right to buy stock at the strike price. Your maximum loss is the premium you paid. If you sell a call, you have the obligation to sell stock at the strike price if the buyer exercises. Your maximum loss is theoretically unlimited because the stock could keep going up forever.

**Stella:** Unlimited loss? That sounds terrifying.

**Horace:** It is, for a naked call. But a covered call, where you already own the stock, caps your risk. The stock gets called away at the strike price, and you miss out on gains above that price, but you never actually lose money on the option itself. That is why we only teach covered calls in this course, never naked calls.

[VISUAL: Risk comparison chart: "Naked Call = Unlimited Risk" (red, warning sign), "Covered Call = Limited, Defined Risk" (green, checkmark)]

**Stella:** What about puts?

**Horace:** If you buy a put, you have the right to sell stock at the strike price. Max loss is the premium. If you sell a put, you have the obligation to buy stock at the strike price. Your max loss is the strike price times 100 minus the premium, which would happen if the stock went to zero. That sounds scary, but if it is a stock you actually want to own, then getting assigned on a put just means you bought the stock at a discount.

**Stella:** That is actually a really nice way to think about it. You are getting paid to promise to buy a stock you already want.

**Horace:** Exactly. And that is the philosophy behind the cash-secured put strategy we will cover in Week 28.

**Stella:** Let us talk about the option chain. When I look at my brokerage account, I see this huge grid of numbers. It is overwhelming.

**Horace:** The option chain is just a listing of all available options for a particular stock. It shows you every available strike price for each expiration date, separated into calls on one side and puts on the other.

[VISUAL: A real-looking option chain table for AAPL, with columns labeled: Bid, Ask, Last, Volume, Open Interest, Strike, and the same columns repeated for puts. The ATM strike is highlighted. ITM options have a shaded background.]

**Horace:** The key things to look at are the bid and ask prices, which tell you what you can buy and sell for. The volume, which tells you how active that specific option is today. And the open interest, which tells you how many existing contracts are out there. High open interest means the option is liquid and you will get better pricing.

**Stella:** What about the bid-ask spread?

**Horace:** The bid-ask spread is the difference between the bid and ask. A tight spread, like $0.05, means low transaction costs. A wide spread, like $0.50, means expensive. On a $3.00 option, a $0.50 spread means you are paying about 17% just to get into the trade. Always check the spread.

**Stella:** Now I want to ask about American versus European options. Does that matter?

**Horace:** For most individual investors trading stock options, you are dealing with American-style options, which means they can be exercised at any time before expiration. European-style options can only be exercised on the expiration date. Most index options like SPX and NDX are European-style.

**Stella:** When would someone exercise early?

**Horace:** Early exercise is rare but it happens most commonly when there is a dividend coming. If you own a deep in-the-money call on a stock that is about to go ex-dividend, you might exercise early to capture the dividend. Otherwise, it is almost always better to sell the option rather than exercise it, because selling captures both intrinsic and extrinsic value.

[VISUAL: Timeline showing American vs European exercise windows, with American having a full bar across the entire period and European having only a marker at expiration]

**Stella:** Let us talk about why options exist in the first place. What is the purpose?

**Horace:** Three main purposes. First, hedging. Options were originally created so farmers could lock in prices for their crops. Today, portfolio managers use options to protect against market crashes. It is insurance.

**Stella:** Like buying a put on your portfolio?

**Horace:** Exactly. If you own $500,000 in stocks and you are worried about a crash, you can buy puts on SPY or on your individual holdings. If the market drops 30%, your puts gain value and offset your stock losses. The cost of the puts is your insurance premium.

**Horace:** Second purpose is speculation. Options provide leverage. Instead of buying 100 shares of Apple for $15,500, you can buy one call option for maybe $350 and control those same 100 shares. If Apple goes up 10%, the stock investor makes about $1,550, or 10%. But the option might go up 200% or more.

**Stella:** But if Apple stays flat or goes down?

**Horace:** The stock investor still has their shares and might only be down temporarily. The option buyer could lose their entire $350. Leverage cuts both ways. That is why speculation with options requires discipline and proper position sizing.

[VISUAL: Side-by-side comparison: Stock buyer puts in $15,500, options buyer puts in $350. Three scenarios shown: stock up 10%, flat, and down 10%, showing both dollar and percentage returns for each]

**Horace:** The third purpose is income generation. This is what we will focus on most. If you own stocks, you can sell covered calls against them. If you have cash and a list of stocks you want to buy, you can sell cash-secured puts. Both strategies generate regular income.

**Stella:** And the income from options can be significant, right?

**Horace:** It can be. A well-executed covered call strategy on a diversified portfolio can generate 8 to 15 percent annually. Compare that to the average dividend yield of the S&P 500, which is around 1.3 percent. We are talking about potentially 6 to 10 times the income from dividends alone.

**Stella:** That is remarkable. Why does not everyone do it?

**Horace:** Because there are tradeoffs. Covered calls cap your upside. If the stock rockets higher, you miss out on gains above the strike price. Cash-secured puts require you to buy the stock if it drops, which means you take on the downside risk. There is no free lunch. But for investors with the right temperament and the right portfolio, these strategies can significantly enhance returns.

[VISUAL: Bar chart comparing income sources: "Dividends Only: ~1.3%/year" vs "Dividends + Options Income: ~9-16%/year"]

**Stella:** Before we wrap up, can we talk about what makes option pricing work? Like, why does an option cost what it costs?

**Horace:** Six main factors. The stock price relative to the strike, which determines intrinsic value. The time to expiration, more time means more premium. Implied volatility, which is the market's expectation of how much the stock will move. Interest rates, which have a minor effect. Dividends, which affect calls and puts differently. And the strike price itself.

**Stella:** Implied volatility sounds important. Can you explain it simply?

**Horace:** Think of it this way. If a stock has been moving 1% per day on average, options will be priced for that level of movement. But if the company has earnings coming up next week and everyone expects a big move, the options will get more expensive because the market expects 3-4% movement. That higher expected movement is reflected in higher implied volatility.

**Stella:** So options before earnings are expensive?

**Horace:** Very expensive. And right after earnings, implied volatility collapses, a phenomenon called IV crush. This is why buying options before earnings is generally a losing strategy. Even if you are right about the direction, the IV crush can eat up your profits.

[VISUAL: Graph showing implied volatility building up before an earnings date, then sharply dropping. Label: "IV Crush" at the drop point. Shows option price declining despite stock moving in the right direction]

**Stella:** That is a trap a lot of beginners fall into, I bet.

**Horace:** One of the most common traps. We will teach you how to be on the right side of that trade.

**Stella:** So to summarize today's lesson: options are contracts that give buyers rights and sellers obligations. There are calls for bullish bets and puts for bearish bets or protection. Every option has a strike price, expiration date, and type. Options are priced based on intrinsic value and extrinsic value, and extrinsic value decays over time. And the three main uses are hedging, speculation, and income generation.

**Horace:** Perfect summary. And the key takeaway for our course is that we will focus on selling options for income, specifically covered calls and cash-secured puts. These are conservative strategies where time decay works in our favor.

**Stella:** I am actually excited about this. It seems much less scary than I expected.

**Horace:** That is the goal. In the next lesson, we are going to look at one of my favorite mental models: options as conditional orders. It will change the way you think about selling puts and calls forever.

[VISUAL: Preview slide for Week 26 with text "Next Week: Options as Conditional Orders - Rethinking How You Buy and Sell Stocks"]

**Stella:** Before we go, can we do a quick lightning round? I have a few rapid-fire questions from viewers.

**Horace:** Let us do it.

**Stella:** First question: can you trade options after hours?

**Horace:** No. Options trade during regular market hours only, 9:30 AM to 4:00 PM Eastern. Some index options have extended hours, but for stock options, it is regular hours only.

**Stella:** Can I buy one option and sell a different one at the same time?

**Horace:** Yes, those are called spreads. Bull call spreads, bear put spreads, iron condors, those are all multi-leg strategies. We will not cover those in this course because they are more complex, but they are common intermediate strategies.

**Stella:** What is the minimum account size for options trading?

**Horace:** There is no universal minimum, but most brokers require $2,000-$5,000 for a basic options account. For selling cash-secured puts, you need enough to cover 100 shares at the strike price. For buying options, you just need enough to pay the premium. I recommend at least $10,000 to start with covered calls or cash-secured puts.

**Stella:** Can I use options on any stock?

**Horace:** Not every stock has options. The stock needs to be listed on an exchange, meet minimum requirements for price, trading volume, and float. Most large-cap stocks have options. Many small-cap stocks do not. Your broker will show you which stocks have options available.

**Stella:** And finally: what is the single most important thing a beginner should know about options?

**Horace:** Know your maximum loss before you enter any trade. If you are buying options, your max loss is the premium. If you are selling options, calculate the worst case and make sure you can live with it. Position sizing and risk management are more important than any strategy.

**Stella:** Great advice. Thanks, everyone. See you next week.

**Horace:** Thanks for watching. If you found this helpful, please like and subscribe. We will see you in Week 26.

[VISUAL: End screen with subscribe button, playlist link to Level 3: Options series, and social media handles]

---

*Animation Reference: animation/week25_option_payoff.py - This animation builds an interactive payoff diagram for call and put options. Users can adjust the strike price and premium to see how the payoff profile changes. The animation also includes a time decay visualization showing how extrinsic value erodes as expiration approaches, with the decay curve accelerating in the final 30 days.*
