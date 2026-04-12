<!-- 此檔案需要翻譯為台灣繁體中文 -->
<!-- This file needs translation to TW Traditional Chinese -->

# Week 39: Futures Markets Introduction

---

## Reading Section

### a) Why This Is Important

Futures markets are among the oldest and most liquid financial markets in the world, yet most retail investors never learn how they work. This is a significant gap in financial literacy because:

- **Futures drive price discovery**: Many assets -- oil, gold, interest rates, stock index levels -- are priced in the futures markets first and then reflected in spot markets. Understanding futures helps you understand how global prices are set.
- **Futures are the backbone of institutional trading**: Pension funds, hedge funds, and commodity producers all use futures extensively. When you hear that "institutional money is flowing into equities," much of that flow occurs through futures markets.
- **Micro futures have opened the door for retail**: Since 2019, the CME has offered micro futures contracts that are one-tenth the size of standard contracts. This makes futures accessible to individual investors for the first time in a practical way.
- **Futures offer unique advantages**: Nearly 24-hour trading, tax advantages (60/40 rule), no pattern day trader restrictions, and efficient leverage make futures a powerful tool for certain strategies.
- **Understanding contango and backwardation**: These concepts from futures markets explain why many popular ETFs (commodity ETFs, volatility ETFs) chronically underperform their underlying assets. Without understanding futures mechanics, you cannot properly evaluate these products.

This lesson provides a comprehensive introduction to futures markets -- how contracts work, how margin functions, how prices relate to spot markets, and how you can use futures as part of a sophisticated investment toolkit.

---

### b) What You Need to Know

#### 1. Futures Contract Basics

A futures contract is a legally binding agreement to buy or sell a specific asset at a predetermined price on a specific future date. Both parties are obligated to fulfill the contract (unlike options, where the buyer has a choice).

```
ANATOMY OF A FUTURES CONTRACT

┌─────────────────────────────────────────────────────┐
│                FUTURES CONTRACT                      │
│                                                      │
│  Underlying Asset:  S&P 500 Index                   │
│  Contract Symbol:   ES (E-mini S&P 500)             │
│  Contract Size:     $50 x Index Level               │
│  Tick Size:         0.25 index points ($12.50)      │
│  Expiration:        3rd Friday of contract month     │
│  Settlement:        Cash-settled                     │
│  Trading Hours:     Sun 6pm - Fri 5pm ET (nearly    │
│                     24 hours)                        │
│  Exchange:          CME (Chicago Mercantile Exchange)│
│                                                      │
│  If S&P 500 is at 5,000:                            │
│  Contract Value = $50 x 5,000 = $250,000            │
│  Initial Margin = ~$12,500 (5% of value)            │
│  Leverage = 20:1                                     │
└─────────────────────────────────────────────────────┘
```

**Key terminology:**

- **Long position**: Agree to buy at the contract price. Profits when price rises.
- **Short position**: Agree to sell at the contract price. Profits when price falls.
- **Contract month**: The month the contract expires (March, June, September, December for most financial futures).
- **Front month**: The nearest expiration contract (most liquid).
- **Back months**: Contracts with later expirations.
- **Open interest**: The total number of outstanding contracts.
- **Settlement**: How the contract is resolved at expiration -- either by physical delivery of the asset or by cash payment of the difference.

**Physical vs. Cash Settlement:**

```
Physical Settlement (e.g., Crude Oil futures - CL):
  At expiration, the short delivers the physical commodity
  and the long pays the contract price.
  
  WARNING: If you hold a physically-settled contract to
  expiration, you may be obligated to take delivery of
  1,000 barrels of oil! Always close before expiration.

Cash Settlement (e.g., S&P 500 futures - ES):
  At expiration, the difference between the contract price
  and the settlement price is paid in cash.
  
  Example: You are long ES at 5,000. Settlement price is 5,050.
  You receive: (5,050 - 5,000) x $50 = $2,500
  No physical delivery occurs.
```

#### 2. Futures Margin: Initial, Maintenance, and Variation

Futures margin is fundamentally different from stock margin. In stocks, margin is a loan from your broker. In futures, margin is a **performance bond** -- a good-faith deposit ensuring you can meet your obligations.

```
FUTURES MARGIN STRUCTURE

                    ┌──────────────────────────┐
                    │    Initial Margin         │
                    │    ($12,500 for ES)       │
                    │                           │
                    │    This is what you       │
                    │    deposit to open        │
                    │    a position             │
                    ├───────────────────────────┤
                    │    Maintenance Margin     │
                    │    ($11,300 for ES)       │
                    │                           │
                    │    If your account drops  │
                    │    below this level, you  │
                    │    get a margin call      │
                    ├───────────────────────────┤
                    │                           │
                    │    Buffer zone:           │
                    │    $1,200 before          │
                    │    margin call            │
                    │                           │
                    └───────────────────────────┘

How much can the market move before margin call?
  Buffer: $12,500 - $11,300 = $1,200
  ES point value: $50
  Points before margin call: $1,200 / $50 = 24 points
  S&P 500 at 5,000: 24/5,000 = 0.48% move

  A 0.48% adverse move triggers a margin call.
  This illustrates the extreme leverage of futures.
```

**Variation Margin (Mark-to-Market):**

Futures positions are marked to market daily. This means gains and losses are settled in cash at the end of each trading day, not when you close the position.

```
DAILY MARK-TO-MARKET EXAMPLE

Day 0: Open long 1 ES at 5,000. Deposit $12,500 initial margin.

Day 1: ES closes at 5,020 (+20 points)
  Daily P&L: +20 x $50 = +$1,000
  Account balance: $12,500 + $1,000 = $13,500

Day 2: ES closes at 4,980 (-40 points from Day 1)
  Daily P&L: -40 x $50 = -$2,000
  Account balance: $13,500 - $2,000 = $11,500
  
  $11,500 > $11,300 maintenance margin: NO margin call

Day 3: ES closes at 4,960 (-20 points from Day 2)
  Daily P&L: -20 x $50 = -$1,000
  Account balance: $11,500 - $1,000 = $10,500
  
  $10,500 < $11,300 maintenance margin: MARGIN CALL!
  Must deposit $2,000 to restore to initial margin ($12,500)
  If you do not deposit by deadline: position is liquidated

Day 4: You deposit $2,000. Account balance: $12,500
  ES closes at 5,010 (+50 points)
  Daily P&L: +50 x $50 = $2,500
  Account balance: $12,500 + $2,500 = $15,000

Total P&L from entry (5,000) to Day 4 close (5,010):
  +10 x $50 = +$500
  Account balance confirms: $12,500 initial + $2,000 added + $500 = $15,000
  But you had to deposit extra capital to survive the drawdown.
```

#### 3. Contango vs. Backwardation

The relationship between futures prices and the current spot price reveals crucial information about market expectations, carrying costs, and supply/demand dynamics.

```
CONTANGO (Normal Market Structure)
Futures price > Spot price

Price
  ^
  |                                    * Contract 6
  |                              * Contract 5
  |                        * Contract 4
  |                  * Contract 3
  |            * Contract 2
  |      * Contract 1
  | * Spot
  +--+----+----+----+----+----+----+----> Time
   Now  1mo  2mo  3mo  4mo  5mo  6mo

Reasons for contango:
  - Cost of carry (storage, insurance, financing)
  - Time value of money (opportunity cost)
  - Convenience yield is low (ample supply)

Examples: Gold, most equity indices, most commodities
in normal conditions.

Cost of carry formula:
  Futures Price = Spot x e^((r - d + s) x t)
  Where: r = risk-free rate
         d = dividend/convenience yield
         s = storage costs
         t = time to expiration
```

```
BACKWARDATION (Inverted Market Structure)
Futures price < Spot price

Price
  ^
  | * Spot
  |      * Contract 1
  |            * Contract 2
  |                  * Contract 3
  |                        * Contract 4
  |                              * Contract 5
  |                                    * Contract 6
  +--+----+----+----+----+----+----+----> Time
   Now  1mo  2mo  3mo  4mo  5mo  6mo

Reasons for backwardation:
  - Strong immediate demand (supply shortage)
  - High convenience yield (owning the physical
    commodity has significant value)
  - Market expects future prices to decline

Examples: Oil during supply disruptions, agricultural
commodities during droughts, VIX during market panics.
```

**Why this matters for investors:**

```
CONTANGO DRAG ON ROLLING FUTURES POSITIONS

Suppose you want to maintain continuous exposure to crude oil
using futures. Oil spot is at $70. The front-month contract
(expiring in 30 days) is at $70.50 and the next month is at $71.

Month 1: Buy front-month at $70.50
  At expiration, spot is still $70
  You sell at $70, losing $0.50 (contango loss)
  You buy next month at $71

Month 2: Holding at $71
  At expiration, spot is still $70
  You sell at $70, losing $1.00
  Buy next month at $71.50

After 12 months of this:
  Oil spot: unchanged at $70
  Your cumulative loss: approximately $6-8 per barrel (8-11%)
  
  This is called "negative roll yield" or "contango drag"
  and it is why commodity ETFs often underperform spot prices.
```

#### 4. Major Futures Markets

```
EQUITY INDEX FUTURES
─────────────────────────────────────────────────────────
Contract        Symbol   Multiplier   Margin*   Contract Value*
E-mini S&P 500  ES       $50          $12,500   $250,000
Micro S&P 500   MES      $5           $1,250    $25,000
E-mini Nasdaq   NQ       $20          $17,600   $360,000
Micro Nasdaq    MNQ      $2           $1,760    $36,000
E-mini Dow      YM       $5           $9,500    $195,000
E-mini Russell  RTY      $50          $7,000    $110,000

*Approximate, subject to change

TREASURY FUTURES
─────────────────────────────────────────────────────────
Contract        Symbol   Multiplier   Duration  Contract Value*
30-Year Bond    ZB       $1,000       ~17 yrs   $120,000
10-Year Note    ZN       $1,000       ~7 yrs    $110,000
5-Year Note     ZF       $1,000       ~4 yrs    $108,000
2-Year Note     ZT       $2,000       ~2 yrs    $205,000
Micro 10-Year   10Y      $1           varies    $1,100

COMMODITY FUTURES
─────────────────────────────────────────────────────────
Contract        Symbol   Size           Contract Value*
Crude Oil       CL       1,000 bbl      $70,000
Gold            GC       100 oz         $220,000
Silver          SI       5,000 oz       $140,000
Natural Gas     NG       10,000 MMBtu   $30,000
Corn            ZC       5,000 bu       $24,000
Micro Gold      MGC      10 oz          $22,000
Micro Crude     MCL      100 bbl        $7,000

CURRENCY FUTURES
─────────────────────────────────────────────────────────
Contract        Symbol   Size           Contract Value*
Euro            6E       125,000 EUR    $135,000
Japanese Yen    6J       12,500,000 JPY $82,000
British Pound   6B       62,500 GBP     $79,000

*Values are approximate based on recent prices
```

#### 5. Micro Futures for Retail Investors

Micro futures, introduced by the CME in 2019, are game-changers for retail investors. They are one-tenth the size of their E-mini counterparts, making them accessible to smaller accounts.

```
MICRO FUTURES: MAKING FUTURES ACCESSIBLE

Micro E-mini S&P 500 (MES):
  Contract value: ~$25,000 (at S&P 500 = 5,000)
  Margin: ~$1,250
  Tick size: 0.25 points = $1.25
  
  Comparison to other ways to get S&P 500 exposure:
  
  100 shares of SPY:       $50,000 capital
  1 SPY ATM call option:   ~$1,200 premium (2 months)
  1 MES futures contract:  ~$1,250 margin
  
  MES advantages over SPY stock:
    - 20x leverage vs 1x
    - Nearly 24-hour trading
    - Tax advantages (60/40 rule)
    - No PDT restrictions
    
  MES advantages over SPY options:
    - No time decay
    - Linear P&L (not affected by Greeks)
    - Better for short-term trading
    - No extrinsic value cost
    
  MES disadvantages:
    - Margin calls possible
    - Leverage can cause rapid losses
    - Must roll contracts quarterly
    - No defined risk (losses can exceed margin)
```

**Account size recommendations:**

```
MINIMUM ACCOUNT SIZE FOR MICRO FUTURES

Conservative (can withstand 5% S&P move):
  MES point value: $5
  5% move on S&P 5,000 = 250 points
  Dollar risk: 250 x $5 = $1,250
  Plus margin: $1,250
  Minimum account: $2,500 per contract
  
  For 1 MES contract: $2,500 minimum
  For 2 MES contracts: $5,000 minimum

Prudent (can withstand 10% S&P move):
  250 points x 2 = 500 points
  Dollar risk: 500 x $5 = $2,500
  Plus margin: $1,250
  Minimum account: $3,750 per contract
  
  For 1 MES contract: $3,750 minimum
  For 2 MES contracts: $7,500 minimum

Professional (can withstand 20% S&P move):
  1,000 points
  Dollar risk: 1,000 x $5 = $5,000
  Plus margin: $1,250
  Minimum account: $6,250 per contract

RECOMMENDATION: $5,000 minimum per MES contract
for most retail traders. This provides adequate
buffer for normal market volatility.
```

#### 6. Futures vs. ETFs

Many investors use ETFs to access asset classes that are primarily traded in futures markets (commodities, volatility, etc.). Understanding the differences is crucial.

```
FUTURES vs. ETF COMPARISON

EQUITY INDEX EXPOSURE (S&P 500)
─────────────────────────────────────────────────
Feature          MES Futures      SPY ETF
─────────────────────────────────────────────────
Expense ratio    None             0.09%
Trading hours    ~23 hours/day    Market hours
Leverage         ~20x             1x (2x w/margin)
Dividends        Priced in*       Paid quarterly
Tax treatment    60/40 rule**     Standard CG
Minimum size     ~$1,250 margin   ~$500 (1 share)
Roll required    Yes (quarterly)  No
Counterparty     Clearinghouse    Fund company

* Futures prices account for expected dividends
** 60% long-term, 40% short-term regardless of hold time

COMMODITY EXPOSURE (Gold)
─────────────────────────────────────────────────
Feature          MGC Futures      GLD ETF
─────────────────────────────────────────────────
Expense ratio    None             0.40%
Contango drag    You control      Priced in
Storage costs    Priced in        0.40% in ER
Tax treatment    60/40 rule       Collectible rate***
Leverage         ~15x             1x
Size             ~$22,000 notl    ~$200 (1 share)
Physical gold    Deliverable      Backed by bars

*** GLD taxed at 28% collectible rate, not standard CG
    Futures 60/40 rule is MUCH more favorable
```

**The 60/40 tax rule:**

```
SECTION 1256 TAX TREATMENT FOR FUTURES

All regulated futures contracts receive special tax treatment:
  - 60% of gains taxed at long-term capital gains rate
  - 40% of gains taxed at short-term capital gains rate
  - REGARDLESS of actual holding period

Example: $10,000 profit on a futures trade held for 2 days

Standard tax treatment (short-term):
  $10,000 x 37% = $3,700 tax
  After-tax profit: $6,300

Futures 60/40 treatment:
  $6,000 (60%) x 20% = $1,200
  $4,000 (40%) x 37% = $1,480
  Total tax: $2,680
  After-tax profit: $7,320

  Tax savings: $1,020 (27.6% less tax)
  
  This is a MAJOR advantage for active traders.
  The effective blended rate is approximately 26.8%
  versus 37% for short-term stock/option trades.
```

#### 7. Roll Yield and the Term Structure

Roll yield is the return (positive or negative) generated when rolling from an expiring futures contract to a later-dated one. It is one of the most important and least understood concepts in futures investing.

```
ROLL YIELD SCENARIOS

POSITIVE ROLL YIELD (Backwardation):
  Expiring contract: $72 (you are long)
  Next month contract: $70
  
  You sell at $72 and buy at $70
  Roll yield: +$2 per contract
  
  Over time, if backwardation persists, you earn
  a premium just from rolling. This is common in
  energy markets during supply disruptions.

NEGATIVE ROLL YIELD (Contango):
  Expiring contract: $70 (you are long)
  Next month contract: $72
  
  You sell at $70 and buy at $72
  Roll yield: -$2 per contract
  
  You lose $2 every month just from rolling.
  Over a year: -$24 per contract (potentially 30%+)
  This is why long-term commodity ETFs often underperform.

ZERO ROLL YIELD (Flat term structure):
  Rare in practice. Occurs when the futures curve
  is completely flat (all months at the same price).
```

```
IMPACT OF ROLL YIELD ON RETURNS

Commodity Spot Return (annual):  +10%
Term Structure:                  Contango (2% monthly roll cost)
Annual Roll Yield:               -24%

Total Futures Return: +10% - 24% = -14%

The commodity went UP 10% but your futures position
LOST 14%. This is the contango trap.

This is why USO (oil ETF) dramatically underperformed
oil prices during 2020-2023. The negative roll yield
consumed all gains and more.
```

#### 8. Contract Specifications and Reading Quotes

Understanding how to read futures quotes and specifications is essential:

```
FUTURES QUOTE: ES (E-mini S&P 500)

ESH6         <-- Contract symbol
  E  = E-mini
  S  = S&P 500
  H  = March (month code)
  6  = 2026 (year)

Month codes:
  F = January    G = February   H = March
  J = April      K = May        M = June
  N = July       Q = August     U = September
  V = October    X = November   Z = December

Sample quote:
  ESH6: 5,025.50
  Change: +12.25
  Volume: 1,245,000
  Open Interest: 2,890,000
  High: 5,032.00
  Low: 4,998.75
  Settlement: 5,013.25 (previous day)

Dollar value of the change:
  +12.25 points x $50/point = +$612.50 per contract
```

```
TICK VALUES FOR COMMON CONTRACTS

Contract    Tick Size    Tick Value    Daily Limit*
─────────────────────────────────────────────────
ES          0.25         $12.50       7% (Level 1)
MES         0.25         $1.25        7%
NQ          0.25         $5.00        7%
CL          $0.01        $10.00       varies
GC          $0.10        $10.00       varies
ZB          1/32         $31.25       varies
ZN          1/64         $15.625      varies

*Circuit breakers halt trading at certain % moves
 Level 1: 7% decline = 15-min halt
 Level 2: 13% decline = 15-min halt
 Level 3: 20% decline = trading halted for day
```

#### 9. Practical Trading Considerations

```
ORDER TYPES IN FUTURES

Market Order:
  Execute immediately at best available price
  Use for: Liquid markets (ES, NQ), urgent exits
  Risk: Slippage in fast markets

Limit Order:
  Execute only at specified price or better
  Use for: Entries, profit targets, less liquid contracts
  Risk: May not get filled

Stop Order (Stop Loss):
  Becomes market order when price hits trigger
  Use for: Risk management, automatic exits
  Risk: Slippage, gaps through your stop

Stop-Limit Order:
  Becomes limit order when price hits trigger
  Use for: Controlled risk management
  Risk: May not fill if price gaps through limit

Bracket Order:
  Entry order with attached profit target and stop loss
  Use for: Disciplined trading with pre-set exits
  Most futures platforms support this natively
```

```
FUTURES TRADING SESSION TIMES (Eastern Time)

Equity Index Futures (ES, NQ, YM, RTY):
  Sunday 6:00 PM - Friday 5:00 PM
  Daily maintenance halt: 5:00 PM - 6:00 PM ET
  
  Key sessions:
  - Globex overnight: 6:00 PM - 9:30 AM
  - Regular trading hours: 9:30 AM - 4:15 PM
  - Post-market: 4:15 PM - 5:00 PM
  
  Most liquid period: 9:30 AM - 4:00 PM
  
Treasury Futures (ZB, ZN, ZF):
  Sunday 6:00 PM - Friday 5:00 PM
  Most liquid: 8:20 AM - 3:00 PM

Crude Oil (CL):
  Sunday 6:00 PM - Friday 5:00 PM
  Most liquid: 9:00 AM - 2:30 PM

Gold (GC):
  Sunday 6:00 PM - Friday 5:00 PM
  Most liquid: 8:20 AM - 1:30 PM
```

#### 10. Risk Management for Futures Trading

```
POSITION SIZING FOR FUTURES

Rule: Risk no more than 1-2% of account per trade

Account size: $50,000
Risk per trade: 1% = $500

MES (Micro S&P 500):
  Point value: $5
  Points to risk: $500 / $5 = 100 points
  S&P at 5,000: 100/5,000 = 2% stop distance
  Maximum contracts: 1 MES (with 100-point stop)

ES (E-mini S&P 500):
  Point value: $50
  Points to risk: $500 / $50 = 10 points
  S&P at 5,000: 10/5,000 = 0.2% stop distance
  This is extremely tight -- NOT recommended on $50,000

  For ES on $50,000 account:
  Need at least 30-50 point stop = $1,500-2,500 risk
  This is 3-5% of account -- TOO MUCH
  
  CONCLUSION: $50,000 account should trade MES, not ES.
  ES requires $200,000+ account for proper risk management.

LEVERAGE GUIDELINES:
  Conservative: Margin used < 10% of account
  Moderate:     Margin used < 25% of account
  Aggressive:   Margin used < 50% of account
  
  Never exceed 50% margin utilization.
  Black swan events (flash crashes, limit downs) can
  blow through any stop loss.
```

---

### c) Common Misconceptions

**Misconception 1: "Futures margin works like stock margin."**

They are completely different. Stock margin is a loan -- you borrow money from your broker to buy more stock, and you pay interest on the loan. Futures margin is a performance bond -- a deposit ensuring you can meet your obligations. You do not pay interest on futures margin, and the leverage ratios are dramatically higher (20:1 or more vs. 2:1 for stock margin). This makes futures both more capital-efficient and more dangerous.

**Misconception 2: "Futures are only for speculators and commodity traders."**

While futures originated in commodity markets and are used by speculators, they are also essential tools for hedging (airlines hedging fuel costs, farmers hedging crop prices), portfolio management (pension funds adjusting equity exposure), and arbitrage (institutions keeping prices aligned across markets). Micro futures have made them practical tools for retail portfolio management as well.

**Misconception 3: "Contango means the market expects prices to rise."**

Contango does NOT necessarily reflect an expectation of rising prices. In most cases, contango reflects the cost of carry: storage costs, financing costs, and insurance. A gold futures curve in contango simply means the futures price includes the cost of storing gold until delivery. The market can be in contango and still expect the spot price to decline.

**Misconception 4: "Futures are riskier than options."**

This is an oversimplification. Futures have linear, unbounded risk in both directions. Options have bounded risk for buyers but unbounded risk for sellers. On a per-dollar-of-margin basis, futures and options can be equally risky. The key difference is that futures losses can exceed your initial margin, while long option losses are capped at the premium paid. But futures also do not suffer from time decay, which makes them superior for certain strategies.

**Misconception 5: "I can hold futures indefinitely like stocks."**

Futures expire. If you want continuous exposure, you must roll your position from the expiring contract to the next one. This rolling process has real costs (commissions, bid-ask spread, and roll yield), which can add up over time. You cannot simply buy and forget like you can with stocks.

**Misconception 6: "The front-month contract is always the best one to trade."**

For short-term trading, the front month is usually the most liquid. But for longer-term positions, the quarterly contracts (March, June, September, December) are often more appropriate because they require less frequent rolling. Additionally, the front month can become volatile and illiquid near expiration, making back-month contracts a safer choice in the final days of the contract.

---

### d) Common Questions and Answers

**Q1: How much money do I need to start trading futures?**

A: For micro futures, a minimum of $5,000 is recommended per contract traded. This provides enough margin plus buffer for normal market movements. For E-mini contracts, $25,000-50,000 is a more appropriate starting point, as the larger contract size requires more capital for proper risk management. Many brokers will let you open a futures account with as little as $2,000, but this is inadequate for sustained trading -- one bad day could wipe out the account.

**Q2: What happens if I hold a physically-settled contract to expiration?**

A: If you hold a physically-settled contract (like crude oil, CL) to expiration, you may be required to take delivery of the physical commodity. For CL, this means 1,000 barrels of oil delivered to Cushing, Oklahoma. Obviously, most retail traders do not want this. Always close or roll physically-settled contracts well before expiration -- typically by the first notice day, which is usually several days before the last trading day. Your broker will likely auto-liquidate the position if you do not, and may charge fees for this.

**Q3: How does the 60/40 tax rule work for futures?**

A: Under IRS Section 1256, all regulated futures contracts are marked to market at year-end. Any unrealized gains or losses are treated as if you had closed the position on December 31. The gains are then taxed at a blended rate: 60% at the long-term capital gains rate (currently 20%) and 40% at the short-term rate (up to 37%), regardless of how long you actually held the position. This results in a maximum effective rate of about 26.8%, compared to 37% for short-term stock trades. You also get to carry back losses 3 years to offset previous Section 1256 gains -- an option not available with standard capital losses.

**Q4: What is the difference between E-mini and micro futures?**

A: Micro futures are exactly one-tenth the size of their E-mini counterparts. The Micro E-mini S&P 500 (MES) has a $5 per point multiplier versus $50 for the E-mini (ES). This means the contract value of MES is about $25,000 versus $250,000 for ES, and margin is proportionally lower. Micro futures use the same trading hours, expiration dates, and settlement methods as their E-mini versions. They are ideal for smaller accounts and for fine-tuning position sizes.

**Q5: How do I roll a futures position?**

A: Rolling means closing your current contract and opening a new position in a later-dated contract. You can do this as two separate trades (sell the expiring contract, buy the next), or many brokers offer a "calendar spread" order that executes both legs simultaneously, which is more efficient. Roll timing varies by contract -- equity index traders typically roll on the Thursday before expiration week (known as "roll day"), when liquidity shifts to the next contract. Most active traders roll 1-2 weeks before expiration.

**Q6: Can I trade futures in an IRA?**

A: Yes, but with restrictions. Many futures brokers offer IRA accounts that allow futures trading. However, you cannot use leverage in a traditional margin sense -- you must have the full margin amount covered by your account balance. Some brokers restrict IRA accounts to certain futures products. The 60/40 tax rule does not apply in IRAs (since gains are already tax-deferred or tax-free), so the tax advantage of futures is lost in retirement accounts.

**Q7: Why do commodity ETFs underperform the spot price?**

A: Commodity ETFs that use futures (like USO for oil or UNG for natural gas) are subject to roll yield. When the futures market is in contango (futures price > spot price), the ETF must sell cheap expiring contracts and buy more expensive later-dated ones, losing money each roll. Over time, this "contango drag" can be enormous. USO, for example, has lost over 90% of its value since inception while oil prices have only declined modestly. This structural drag makes long-term commodity ETF holdings problematic in persistent contango markets.

**Q8: How do futures relate to overnight stock movements?**

A: Equity index futures (ES, NQ) trade nearly 24 hours a day, while the stock market trades only 6.5 hours. When you see a stock market "gap up" or "gap down" at the open, the futures market has already been trading at those levels for hours. Overnight futures trading reflects breaking news, international market movements, and economic data releases. Many professional traders watch futures before the market open to gauge the day's likely direction.

---

## YouTube Script

[VISUAL: Opening title card -- "Week 39: Futures Markets Introduction" with images of the CME trading floor transitioning to modern electronic trading screens]

**Alex**: Welcome to Week 39. We have spent the last two weeks deep in options territory, and today we are moving into a completely different arena -- futures markets. Sam, what do you know about futures?

**Sam**: Honestly, not much. I know they are contracts to buy or sell something at a future date. Farmers use them, oil companies use them. But I always thought they were too complicated or too risky for regular investors.

**Alex**: That was true until about 2019. The introduction of micro futures changed everything. But let us start from the beginning, because futures are actually simpler in many ways than options.

[VISUAL: Simple diagram of a futures contract between two parties]

**Alex**: A futures contract is an agreement between two parties. One party agrees to buy a specific asset at a specific price on a specific date. The other party agrees to sell. Both sides are obligated. That is the key difference from options, where only the seller is obligated.

**Sam**: So it is like a forward contract?

**Alex**: Very similar. The main difference is that futures are standardized and traded on an exchange, which eliminates counterparty risk. The exchange's clearinghouse guarantees both sides of every trade. If the person on the other side of your trade goes bankrupt, the clearinghouse still honors your contract.

**Sam**: That sounds important. So what are the most common futures contracts?

[VISUAL: Table of major futures markets organized by category]

**Alex**: There are four main categories. Equity index futures -- S&P 500, Nasdaq 100, Dow Jones, Russell 2000. Treasury futures -- 2-year, 5-year, 10-year, 30-year bonds. Commodity futures -- crude oil, gold, silver, natural gas, corn, soybeans. And currency futures -- euro, yen, pound.

**Sam**: The equity index ones seem most relevant for stock investors.

**Alex**: They are, and that is where we will focus. The E-mini S&P 500, ticker ES, is the most widely traded futures contract in the world. One contract is worth $50 times the S&P 500 index level. At S&P 5,000, that is $250,000 per contract.

**Sam**: $250,000? That is enormous. How can a regular person trade that?

**Alex**: Two answers. First, the margin requirement is only about $12,500 -- about 5% of the contract value. That gives you 20 to 1 leverage.

**Sam**: That is terrifying.

**Alex**: It can be. Which brings me to the second answer: micro futures. The Micro E-mini S&P 500, ticker MES, is one-tenth the size. $5 per point instead of $50. Contract value around $25,000. Margin around $1,250.

[VISUAL: Side-by-side comparison of ES vs MES contract specifications]

**Sam**: OK, $1,250 in margin to control $25,000 of S&P 500 exposure. That is still 20 to 1 leverage, but the dollar amounts are manageable.

**Alex**: Exactly. And this is where I need to explain how futures margin works, because it is nothing like stock margin.

[ANIMATION: animation/week39_futures_margin.py -- Animated visualization of the futures margin system. The animation shows a vertical "account balance" bar starting at the initial margin level. As simulated market data plays, the bar rises and falls in real-time representing mark-to-market gains and losses. Three horizontal reference lines are shown: initial margin (green), maintenance margin (yellow), and zero (red). When the account balance drops below the maintenance margin line, a "MARGIN CALL" alert flashes on screen, and the bar is shown being topped back up to the initial margin level with an arrow labeled "Variation Margin Deposit." The animation cycles through several days of simulated trading, showing both profitable and losing days.]

**Sam**: So the margin is more like a security deposit than a loan.

**Alex**: Perfect analogy. When you buy stock on margin, your broker lends you money, and you pay interest. When you trade futures, you post a performance bond. There is no loan and no interest. The leverage comes from the fact that you only need a small percentage of the contract value as your deposit.

**Sam**: And mark-to-market means gains and losses are settled every day?

**Alex**: Every single day. At the end of the trading day, your position is priced at the settlement price. If you made money, it is credited to your account in cash. If you lost money, it is debited. This is called variation margin.

[VISUAL: Day-by-day mark-to-market example with account balance tracking]

**Alex**: Let me walk you through an example. You buy one MES at 5,000 with $1,250 in initial margin. Day one, the S&P drops 30 points to 4,970. That is 30 times $5 equals $150 debited from your account. Your balance is now $1,100.

**Sam**: And the maintenance margin is...

**Alex**: About $1,130 for MES. So at $1,100, you are below maintenance. Margin call. You need to deposit enough to get back to initial margin -- about $150.

**Sam**: A 30-point drop in the S&P is only 0.6%. And I already got a margin call?

**Alex**: Now you understand why position sizing is so important in futures. With 20 to 1 leverage, a 0.6% move creates a 12% change in your margin account. This is why I recommend having at least $5,000 per MES contract, not the minimum $1,250.

**Sam**: $5,000 gives you a lot more room.

**Alex**: Right. With $5,000, the S&P could drop 750 points -- 15% -- before you face a margin call. That covers most normal market events.

[VISUAL: Account sizing recommendation chart]

**Sam**: Let us talk about something I have heard but never understood: contango and backwardation.

**Alex**: These are the shapes of the futures price curve, and they are absolutely critical for understanding commodities, volatility products, and many ETFs.

[VISUAL: Two curves side by side -- contango (upward sloping) and backwardation (downward sloping)]

**Alex**: Contango means the futures price is higher than the spot price, and each successive contract month is more expensive. This is the normal state for most markets because it reflects the cost of carry -- storage costs, insurance, and financing.

**Sam**: Give me an example.

**Alex**: Gold. If gold spot is $2,200 per ounce, the 1-month future might be $2,205, the 3-month $2,215, the 6-month $2,230. The premium reflects the cost of storing and insuring gold for those extra months.

**Sam**: That makes sense. And backwardation is the opposite?

**Alex**: Yes. In backwardation, the futures price is below the spot price. This typically happens when there is strong immediate demand or a supply shortage. Think of crude oil during a war or natural gas during a cold snap. People want the commodity now, so the spot price is bid up relative to future delivery.

**Sam**: So which one is better for investors?

**Alex**: If you are long futures and rolling your position, backwardation is your friend and contango is your enemy. Let me explain why.

[VISUAL: Roll mechanics animation showing contract expiry and new contract purchase]

**Alex**: When your futures contract expires, you need to sell it and buy the next month. In contango, the next month is more expensive. You sell low, buy high. That is a loss every time you roll. Over a year of monthly rolls, this "negative roll yield" can cost you 10-30% depending on the market.

**Sam**: That is why commodity ETFs underperform spot prices!

**Alex**: Exactly. USO, the popular oil ETF, uses oil futures and rolls them monthly. Over the years, contango has destroyed enormous amounts of value for USO holders. The spot price of oil might be flat, but USO is down because of contango drag.

**Sam**: In backwardation, it is the opposite? You sell high and buy low?

**Alex**: Right. Positive roll yield -- you actually earn money from rolling. This is why some commodity trading strategies specifically target markets in backwardation.

**Sam**: Let us talk about the practical stuff. How do futures compare to just buying an ETF like SPY?

[VISUAL: Detailed comparison table -- MES vs SPY]

**Alex**: There are several key differences. First, trading hours. SPY trades from 9:30 AM to 4 PM Eastern. MES trades nearly 24 hours a day, Sunday evening through Friday afternoon. If there is an earthquake in Japan at 2 AM, you can adjust your position immediately with futures. With SPY, you wait until the morning.

**Sam**: That seems like a big deal.

**Alex**: It is, especially for risk management. Second, the 60/40 tax rule. Under IRS Section 1256, all regulated futures contracts get special tax treatment. Sixty percent of your gains are taxed at the long-term capital gains rate, and 40% at the short-term rate, no matter how long you held the position.

**Sam**: So even a day trade gets 60% long-term treatment?

**Alex**: Yes. On $10,000 of profit, you would pay about $2,680 in tax with the 60/40 rule versus $3,700 as a short-term stock gain. That is over $1,000 saved. For active traders, this adds up to thousands per year.

[VISUAL: Tax comparison showing dollar savings]

**Sam**: What are the downsides of futures versus ETFs?

**Alex**: The biggest one is that you have to roll your contracts. Every quarter for equity index futures, you need to close the expiring contract and open the next one. It takes about 2 minutes, but it is a step that does not exist with ETFs. Second, there is no automatic dividend reinvestment. Dividends are already priced into the futures, so you are not missing them, but you do not receive quarterly cash payments. Third, leverage is a double-edged sword -- it is there whether you want it or not.

**Sam**: Can you manage the leverage down?

**Alex**: Yes, by keeping your position size small relative to your account. If you have $50,000 and trade one MES contract worth $25,000, your effective leverage is only 0.5x. You are actually less leveraged than owning 100% stocks.

**Sam**: That is a good point. You do not have to use the full leverage.

**Alex**: Exactly. The available leverage is 20x, but nobody is forcing you to use it. Professional futures traders typically use 2-5x leverage, not 20x.

**Sam**: What about risk management? How do I protect myself from a big overnight move?

[VISUAL: Risk management framework for futures trading]

**Alex**: Three critical rules. One, position size based on account equity, not margin. If your account is $50,000, risk no more than 1% per trade, which is $500. With MES at $5 per point, that is a 100-point stop loss. Plenty of room.

**Sam**: And if I am trading ES instead of MES?

**Alex**: ES is $50 per point. A $500 risk gives you only a 10-point stop, which is 0.2% of the S&P. That is absurdly tight -- you will get stopped out on normal noise. This is why ES requires at least $200,000 in my view for proper risk management. For accounts under $100,000, stick to MES.

**Sam**: That is really useful guidance.

**Alex**: Rule two: always use stop-loss orders. Futures markets can gap -- especially on weekends or during major news events. A stop does not guarantee your exit price, but it guarantees your position will be closed. Without a stop, a 5% overnight gap on one ES contract is a $12,500 loss.

**Sam**: And rule three?

**Alex**: Never use more than 25-50% of your account as margin. If your account is $50,000, your total margin requirement across all positions should not exceed $12,500 to $25,000. This ensures you have enough buffer for adverse moves and margin calls.

[VISUAL: Portfolio allocation showing margin used vs free capital]

**Sam**: Can you show me how a real futures trade works from start to finish?

**Alex**: Let us walk through it.

[VISUAL: Step-by-step trade example with MES]

**Alex**: Say you are bullish on the S&P 500. Account size: $25,000. You decide to buy one MES contract.

Step one: Check the contract specifications. MES, $5 per point, quarterly expiration. Current front month is trading at 5,010.

Step two: Determine your stop loss. You are willing to risk 1% of your account, which is $250. At $5 per point, your stop is 50 points below entry: 4,960.

Step three: Determine your profit target. You are targeting 100 points of upside, a 2:1 reward to risk ratio. Target: 5,110.

Step four: Place a bracket order -- buy 1 MES at market (or limit at 5,010), with a stop at 4,960 and a target at 5,110.

**Sam**: And then what?

**Alex**: The trade is live. Each day, your account is marked to market. If MES goes to 5,030 on day one, you have $100 credited to your account. If it drops to 4,990 on day two, you have $200 debited ($40 movement x $5). Your running P&L is -$100.

**Sam**: And if it hits my stop at 4,960?

**Alex**: Your position is automatically closed. Total loss: 50 points times $5 equals $250, which is 1% of your account. Painful but manageable.

**Sam**: And if it hits my target?

**Alex**: The position is closed at 5,110. Profit: 100 points times $5 equals $500, which is 2% of your account.

[VISUAL: P&L scenarios at different exit points]

**Sam**: This all seems very systematic. What are the biggest mistakes beginners make?

**Alex**: Number one: oversizing positions. Trading ES on a $20,000 account is a recipe for blowing up. Number two: not understanding roll dates and accidentally holding to expiration. Number three: ignoring overnight risk -- futures trade 23 hours a day, and big moves can happen while you sleep. Number four: treating futures like a casino because of the leverage. Number five: not accounting for the tax implications -- both the benefit of 60/40 treatment and the requirement to mark positions to market at year-end.

[VISUAL: "Top 5 Futures Mistakes" checklist]

**Sam**: That last point is interesting. You owe taxes on unrealized gains in futures?

**Alex**: Yes. Even if you hold a position over December 31, you must report the unrealized gain or loss as if you had closed it. This is unique to Section 1256 contracts. It is not necessarily a bad thing -- it forces you to recognize gains and losses regularly -- but it catches some people off guard at tax time.

**Sam**: This has been incredibly helpful. I feel like futures are much more accessible than I thought, especially with micro contracts.

**Alex**: They are. Micro futures have democratized access to markets that were previously reserved for institutional players. But remember -- the leverage is real, the risks are real, and the daily mark-to-market means you need adequate capital. Start with MES, one contract, proper stops, and build from there.

[VISUAL: Summary slide with key takeaways]

**Sam**: Three key takeaways?

**Alex**: One: futures margin is a performance bond, not a loan. Understand mark-to-market before you trade. Two: contango and backwardation affect every futures-based product, including popular ETFs. Know which regime you are in. Three: use micro futures if your account is under $100,000, and never use more than 25% of your account as margin.

**Sam**: Next week, we are going to explore one of the most fascinating and dangerous corners of the market -- the VIX and volatility trading. See you then!

[VISUAL: End card -- "Next Week: Week 40 -- Trading the VIX and Volatility"]

---

*End of Week 39*
