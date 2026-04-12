<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 28: Cash-Secured Puts for Entry

## Reading Section

### a) Why This Is Important

Every investor faces the same dilemma when they find a stock they want to buy: should I buy now, or should I wait for a better price? Buying now means you might pay too much if the stock drops next week. Waiting means the stock might continue rising and you miss the opportunity entirely. This is the age-old tug-of-war between urgency and patience, and it paralyzes millions of investors.

The **cash-secured put** strategy elegantly resolves this dilemma. Instead of agonizing over timing, you pick the price you want to pay, sell a put at that strike price, and get paid to wait. If the stock drops to your price, you buy it at a discount. If it does not drop, you keep the premium and try again. There is no scenario where you lose compared to simply waiting with cash in your account.

**Why this strategy is critical for building wealth:**

**1. It converts idle cash into an income-producing asset.** The average investor keeps 10-30% of their portfolio in cash, waiting for opportunities. On a $500,000 portfolio, that is $50,000-$150,000 earning savings-account rates. Cash-secured puts can generate 8-20% annualized return on that idle cash, turning dead money into active income.

**2. It removes emotion from buying decisions.** Instead of watching a stock daily and trying to pick the perfect entry point, you define your ideal price in advance and let the market come to you. The premium you receive is compensation for your patience and discipline. This systematic approach eliminates the panic buying that often occurs during market rallies and the paralysis that prevents buying during dips.

**3. It guarantees a better entry price than a market order.** When you sell a put for $3.00 at a $140 strike, your effective purchase price is $137.00. Even if you are assigned, you entered the stock at a lower cost than anyone who bought at $140 with a regular order. The premium always works in your favor.

**4. It creates a structured buying framework.** Instead of making ad hoc buying decisions, you build a list of target stocks with target prices and sell puts systematically. This transforms investing from a series of emotional decisions into a methodical process. Professional fund managers have used this approach for decades.

**5. It naturally builds positions during market weakness.** Because puts are assigned when stocks drop, the strategy automatically buys stocks during pullbacks and corrections, which is exactly when long-term investors should be buying. The cash-secured put is a built-in "buy the dip" mechanism with income attached.

Cash-secured puts are the ideal complement to covered calls (Week 27). Together, they form the complete **wheel strategy**: sell puts to enter positions while collecting income, then sell covered calls on those positions for ongoing income, and if assigned on the calls, start selling puts again. This continuous cycle can generate 12-20% annual income on a well-managed portfolio.

---

### b) What You Need to Know

#### What Is a Cash-Secured Put?

A **cash-secured put** is a position where you:

1. **Sell (write) a put option** at a strike price you are willing to buy the stock at.
2. **Hold enough cash** in your account to buy 100 shares at that strike price.

The "cash-secured" part is critical. Unlike a naked put (which uses margin), a cash-secured put has the full purchase amount set aside. Your broker holds this cash as collateral. If you are assigned, the cash is used to purchase the shares. There is no margin risk.

```
CASH-SECURED PUT STRUCTURE:

  +---------------------------------------------------+
  |  POSITION:                                        |
  |                                                   |
  |  SHORT: 1 AAPL $140 Put, 30 days to expiration   |
  |  Premium received: $2.50/share ($250 total)       |
  |                                                   |
  |  CASH RESERVED: $14,000 ($140 x 100 shares)      |
  |                                                   |
  |  COMMITMENT:                                      |
  |  "I agree to buy 100 shares of AAPL at $140      |
  |   if the stock drops to or below $140 before      |
  |   expiration. In return, I receive $250 now."     |
  |                                                   |
  |  EFFECTIVE PURCHASE PRICE IF ASSIGNED:            |
  |  $140.00 - $2.50 = $137.50 per share             |
  +---------------------------------------------------+
```

#### Capital Requirement

The capital required for a cash-secured put equals the strike price multiplied by 100 (shares per contract). This cash must be available in your account and will be held as collateral until the option expires or is closed.

```
CAPITAL REQUIREMENT EXAMPLES:

  Stock     Strike    Cash Required    Typical Premium   Yield/Month
  =====     ======    =============    ===============   ===========
  AAPL      $140      $14,000          $1.50-$3.50       1.1-2.5%
  MSFT      $380      $38,000          $4.00-$8.00       1.1-2.1%
  GOOGL     $160      $16,000          $2.00-$4.50       1.3-2.8%
  JPM       $180      $18,000          $2.00-$4.00       1.1-2.2%
  SPY       $520      $52,000          $5.00-$10.00      1.0-1.9%
  KO        $55       $5,500           $0.60-$1.20       1.1-2.2%

  NOTE: Lower-priced stocks require less capital per contract,
  making them more accessible for smaller accounts.
  
  For a $50,000 account:
    Can sell 3 KO $55 Puts ($16,500 reserved)
    Can sell 1 AAPL $140 Put ($14,000 reserved)
    Can sell 1 JPM $180 Put ($18,000 reserved)
    Remaining cash: $1,500 buffer
```

#### Selecting the Strike Price

The strike price is your target buy price. It should be a price at which you would be genuinely happy to own the stock. Here are the key considerations:

```
STRIKE PRICE SELECTION FRAMEWORK:

  Current Stock Price: $155 (AAPL example)

  APPROACH 1: Fundamental Valuation
    - Calculate fair value using PE ratio, DCF, or other methods
    - Set strike at or below fair value
    - Example: Fair value estimate = $145, sell $145 put
    - You buy at a discount to your estimate of intrinsic value

  APPROACH 2: Technical Support Levels
    - Identify price levels where stock has historically found support
    - Set strike at or just below support
    - Example: AAPL has support at $148-$150, sell $148 put
    - You buy at a level where the stock has historically bounced

  APPROACH 3: Percentage Below Market
    - Set strike at a fixed percentage below current price
    - Conservative: 10-15% below (strike $132-$140)
    - Moderate: 5-10% below (strike $140-$147)
    - Aggressive: 0-5% below (strike $147-$155)

  APPROACH 4: Using Delta
    - Delta 0.20 = ~20% probability of assignment = ~8-12% OTM
    - Delta 0.30 = ~30% probability of assignment = ~5-8% OTM
    - Delta 0.40 = ~40% probability of assignment = ~3-5% OTM
    - Lower delta = further OTM = lower premium but lower assignment risk
```

```
STRIKE PRICE vs. PREMIUM TRADEOFF (AAPL at $155, 30 days):

  Strike   Distance   Delta   Premium   Monthly   Ann. Yield   Assign Prob
  ======   ========   =====   =======   =======   ==========   ==========
  $155     ATM        0.50    $4.50     3.0%      36.0%        ~50%
  $150     3.2% OTM   0.35    $2.80     1.9%      22.4%        ~35%
  $145     6.5% OTM   0.25    $1.70     1.2%      14.1%        ~25%
  $140     9.7% OTM   0.18    $0.95     0.7%      8.1%         ~18%
  $135     12.9% OTM  0.12    $0.50     0.4%      4.4%         ~12%
  $130     16.1% OTM  0.07    $0.25     0.2%      2.3%         ~7%

  SWEET SPOT: $140-$150 range (5-10% OTM)
  Balances meaningful premium with a purchase price you want.
```

#### Selecting the Expiration

The same principles from covered calls apply to cash-secured puts. The 30-45 day window is optimal for the balance between premium income and theta decay.

```
EXPIRATION COMPARISON (AAPL $145 Put):

  Expiration    Days   Premium   Ann. Yield   Theta/Day   Management
  ==========   ====   =======   ==========   =========   ==========
  1 Week        7     $0.45     33.4%*       $0.064      Weekly
  2 Weeks       14    $0.80     23.7%*       $0.057      Biweekly
  1 Month       30    $1.70     14.1%        $0.057      Monthly     <--
  45 Days       45    $2.40     13.1%        $0.053      ~Monthly    <--
  2 Months      60    $3.00     12.3%        $0.050      Bimonthly
  3 Months      90    $4.00     10.9%        $0.044      Quarterly

  * Weekly/biweekly yields look very high annualized but are harder
    to sustain due to higher transaction frequency and occasional
    gaps between cycles.

  RECOMMENDED: 30-45 days (marked with arrows)
  - Best theta decay rate relative to premium
  - Manageable frequency (monthly attention)
  - Sufficient premium to justify the trade
```

#### Effective Purchase Price

One of the most important calculations in put selling is your **effective purchase price**. This is the actual cost per share if you are assigned, after accounting for the premium received.

```
EFFECTIVE PURCHASE PRICE FORMULA:

  Effective Price = Strike Price - Premium Received

  Example:
    Sell AAPL $145 Put for $2.80
    Effective price = $145.00 - $2.80 = $142.20

  What this means:
    If you are assigned, you buy 100 shares at $145.
    But you already received $280 in premium.
    Your NET cost per share is $142.20.
    
    This is equivalent to buying the stock at $142.20 on the open market.

  WITH REPEATED SELLING (before eventual assignment):

    Month 1: Sell $145 Put for $2.80 -> Not assigned -> Keep $280
    Month 2: Sell $145 Put for $2.30 -> Not assigned -> Keep $230
    Month 3: Sell $145 Put for $3.10 -> Not assigned -> Keep $310
    Month 4: Sell $145 Put for $3.50 -> ASSIGNED

    Total premiums: $280 + $230 + $310 + $350 = $1,170
    Per share: $11.70
    
    Assignment price: $145.00
    Effective purchase price: $145.00 - $11.70 = $133.30
    
    Stock was at $155 when you started.
    You effectively bought at $133.30, a 14% discount from the
    original price and an 8% discount from your $145 strike.
```

#### The Four Scenarios at Expiration

Every cash-secured put will end in one of these four scenarios:

```
SCENARIO 1: Stock stays well above strike (MOST COMMON)
====================================================
  Setup: AAPL at $155, Sold $145 Put for $2.80
  At expiration: AAPL at $158

  Result: Put expires worthless.
  Premium: Keep $280 (1.9% return in 30 days)
  Shares: None purchased
  Cash: $14,500 returned (no longer reserved)
  Action: Sell another put for next month

  +--------------------------------------------------+
  |  AAPL Price Path:                                |
  |  $160|           ___/                            |
  |  $155|____/\___/                                 |
  |  $150|                                           |
  |  $145|- - - - - - - - - - - STRIKE - - - - - -  |
  |  $140|                                           |
  |      |____|____|____|____|____|                   |
  |      Day1  Day7  Day14 Day21 Day30               |
  |                                                  |
  |  Stock never threatened the strike.              |
  |  Put decayed to zero. Keep premium.              |
  +--------------------------------------------------+


SCENARIO 2: Stock drops to strike, hovers near it
====================================================
  Setup: AAPL at $155, Sold $145 Put for $2.80
  At expiration: AAPL at $144

  Result: Put is $1 in the money. You are assigned.
  Purchase: Buy 100 shares at $145
  Premium: Keep $280
  Effective cost: $142.20 per share
  Stock value: $144 (small unrealized gain from effective cost!)
  Action: Start selling covered calls on your new shares

  +--------------------------------------------------+
  |  AAPL Price Path:                                |
  |  $155|____                                       |
  |  $150|    \____                                  |
  |  $145|- - - - -\__ _STRIKE_ ___/\____           |
  |  $140|          \_/                   \          |
  |  $135|                                           |
  |      |____|____|____|____|____|                   |
  |      Day1  Day7  Day14 Day21 Day30               |
  |                                                  |
  |  Stock crossed below strike.                     |
  |  Assigned at $145, effective cost $142.20.       |
  +--------------------------------------------------+


SCENARIO 3: Stock drops significantly below strike
====================================================
  Setup: AAPL at $155, Sold $145 Put for $2.80
  At expiration: AAPL at $125

  Result: Put is $20 in the money. You are assigned.
  Purchase: Buy 100 shares at $145
  Premium: Keep $280
  Effective cost: $142.20 per share
  Stock value: $125 (unrealized loss of $17.20/share)
  Loss: $1,720 (but $280 less than buying at $145 outright)

  +--------------------------------------------------+
  |  AAPL Price Path:                                |
  |  $155|__                                         |
  |  $150|  \__                                      |
  |  $145|- - \_STRIKE_ - - - - - - - - - - - - -   |
  |  $140|     \                                     |
  |  $135|      \___                                 |
  |  $130|          \____                            |
  |  $125|               \______                     |
  |      |____|____|____|____|____|                   |
  |      Day1  Day7  Day14 Day21 Day30               |
  |                                                  |
  |  Stock dropped hard. Assigned at $145.           |
  |  Paper loss, but you wanted to own the stock.    |
  |  Effective cost of $142.20 is still better       |
  |  than buying at $145 with a limit order.         |
  +--------------------------------------------------+


SCENARIO 4: Stock rallies strongly above starting price
====================================================
  Setup: AAPL at $155, Sold $145 Put for $2.80
  At expiration: AAPL at $175

  Result: Put expires worthless.
  Premium: Keep $280 (1.9% return in 30 days)
  Shares: None purchased
  Opportunity cost: You "missed" the rally from $155 to $175
  
  BUT: You also missed nothing with a limit order at $145,
  which also would not have been filled!

  +--------------------------------------------------+
  |  AAPL Price Path:                                |
  |  $175|                              _____/       |
  |  $170|                         ___/              |
  |  $165|                    ___/                   |
  |  $160|               ___/                        |
  |  $155|____      ___/                             |
  |  $150|    \___/                                  |
  |  $145|- - - - - - - - -STRIKE- - - - - - - - -  |
  |      |____|____|____|____|____|                   |
  |      Day1  Day7  Day14 Day21 Day30               |
  |                                                  |
  |  Stock rallied. You did not buy.                 |
  |  Same result as a limit order, but you earned    |
  |  $280 in premium while the limit order earned $0.|
  +--------------------------------------------------+
```

#### Comparison to Buying Stock Outright

Let us directly compare three approaches to acquiring the same stock:

```
THREE APPROACHES TO BUYING AAPL (currently at $155):

APPROACH 1: Buy at Market
  Action: Buy 100 shares at $155
  Cost: $15,500
  If stock goes to $170: Profit = $1,500 (9.7%)
  If stock goes to $140: Loss = -$1,500 (-9.7%)
  If stock stays at $155: Gain = $0 (0%)

APPROACH 2: Limit Order at $145
  Action: Place limit buy at $145, wait
  Cost if filled: $14,500
  If stock never reaches $145: No shares, $0 income
  If stock drops to $145 and assigned: Cost = $145/share
  Opportunity cost: Cash earns savings rate (~4-5% annually)

APPROACH 3: Cash-Secured Put at $145
  Action: Sell $145 Put for $2.80, reserve $14,500
  If stock stays above $145: Keep $280, repeat next month
  If stock drops to $145: Effective cost = $142.20/share
  Annual income if never assigned: ~14-17% on reserved capital

SIDE-BY-SIDE COMPARISON TABLE:

  Outcome              Market Buy   Limit Order   CSP ($145)
  ==================   ==========   ===========   ============
  Stock to $170        +$1,500      Not filled    Not filled
                                    $0 income     +$280 income
  
  Stock stays $155     $0           Not filled    Not filled
                                    $0 income     +$280 income
  
  Stock to $145        -$1,000      Buys at $145  Buys at $142.20
                                    $0 income     $280 premium
  
  Stock to $130        -$2,500      Buys at $145  Buys at $142.20
                                    Loss: $1,500  Loss: $1,220
  
  Income while         $0           ~$0           $280/month
  waiting                           (savings rate) (14%+ ann.)

  CONCLUSION: Cash-secured puts win in every scenario except
  the one where you want to buy at market price RIGHT NOW.
```

#### Managing Assignments

When you are assigned on a cash-secured put, your broker automatically purchases 100 shares at the strike price using the reserved cash. Here is what to do next:

```
ASSIGNMENT MANAGEMENT CHECKLIST:

  [ ] 1. Confirm the assignment in your account
        - Check: 100 shares added, cash deducted
        - Note your cost basis (strike price, adjusted for premium)

  [ ] 2. Reassess the stock
        - Has the fundamental thesis changed?
        - Is the stock dropping for temporary or permanent reasons?
        - Would you still buy at this price if starting fresh?

  [ ] 3. If fundamentals are intact:
        - START SELLING COVERED CALLS on your new shares
        - Select strike above your effective cost basis
        - This begins the "wheel strategy" cycle
        
        Example:
          Assigned at $145 (effective $142.20)
          Stock now at $143
          Sell $155 covered call for $2.00
          If called away: Profit = $155 - $142.20 + $2.00 = $14.80/share

  [ ] 4. If fundamentals have deteriorated:
        - Consider selling shares immediately
        - Take the loss (premium cushion reduces it)
        - Reallocate capital to better opportunities
        - Do NOT sell more puts hoping to "average down" unless thesis holds

  [ ] 5. Update your portfolio tracking
        - Record the assignment
        - Calculate your effective cost basis
        - Plan your covered call strategy
```

#### The Wheel Strategy Preview

The **wheel strategy** is a continuous cycle of cash-secured puts and covered calls. It is the most complete income-generating strategy for stock investors. Here is how it works:

```
THE WHEEL STRATEGY CYCLE:

  +------------------------------------------+
  |                                          |
  |   PHASE 1: SELL CASH-SECURED PUTS       |
  |   "Getting paid to wait for your price"  |
  |                                          |
  |   -> Stock stays above strike?           |
  |      Keep premium, sell new put          |
  |      (REPEAT PHASE 1)                   |
  |                                          |
  |   -> Stock drops below strike?           |
  |      Assigned: Buy shares               |
  |      (MOVE TO PHASE 2)                  |
  |                                          |
  +------------------------------------------+
                     |
                     | (Assigned)
                     v
  +------------------------------------------+
  |                                          |
  |   PHASE 2: SELL COVERED CALLS           |
  |   "Getting paid to hold and wait"        |
  |                                          |
  |   -> Stock stays below strike?           |
  |      Keep premium, sell new call         |
  |      (REPEAT PHASE 2)                   |
  |                                          |
  |   -> Stock rises above strike?           |
  |      Assigned: Sell shares               |
  |      (RETURN TO PHASE 1)               |
  |                                          |
  +------------------------------------------+
                     |
                     | (Called away)
                     v
             Return to Phase 1
             (Sell puts again)


INCOME AT EVERY STAGE:
  Phase 1: Put premiums (while waiting to buy)
  Phase 2: Call premiums + dividends (while holding)
  
  There is NEVER a phase where you are not earning income.
```

```
WHEEL STRATEGY COMPLETE EXAMPLE:

Stock: JPM (JPMorgan Chase)
Starting: Cash of $18,000, JPM at $195

PHASE 1 - PUT SELLING:
  Month 1: Sell $180 Put for $2.50 -> JPM at $192 -> Keep $250
  Month 2: Sell $180 Put for $2.20 -> JPM at $198 -> Keep $220
  Month 3: Sell $180 Put for $3.00 -> JPM drops to $175 -> ASSIGNED

  Put premiums collected: $250 + $220 + $300 = $770
  Shares acquired: 100 at $180
  Effective cost basis: $180 - $7.70 = $172.30

PHASE 2 - COVERED CALL SELLING:
  Month 4: Sell $195 Call for $2.80 -> JPM at $182 -> Keep $280
  Month 5: Sell $195 Call for $2.50 -> JPM at $188 -> Keep $250
           Also receive JPM dividend: $1.15/share = $115
  Month 6: Sell $195 Call for $3.20 -> JPM at $190 -> Keep $320
  Month 7: Sell $195 Call for $3.50 -> JPM rises to $198 -> CALLED AWAY

  Call premiums collected: $280 + $250 + $320 + $350 = $1,200
  Dividend received: $115
  Sale price: $195

TOTAL CYCLE RESULTS (7 months):
  Put premiums:   $770
  Call premiums:   $1,200
  Dividend:        $115
  Capital gain:    ($195 - $180) x 100 = $1,500
  ================================================
  TOTAL PROFIT:    $3,585

  Return on $18,000 capital: 19.9% in 7 months = 34.2% annualized

RETURN TO PHASE 1:
  Month 8: Cash of $19,500+, sell $180 puts again...
  The wheel keeps turning.
```

#### Position Management: When and How to Close Early

Not every put needs to be held to expiration. Here are guidelines for early management:

```
EARLY CLOSE GUIDELINES:

  TAKE PROFIT (Buy back the put):
  - Put has lost 50% of its value -> Close for 50% profit
    Example: Sold for $2.80, now worth $1.40 -> Buy back at $1.40
    Profit: $140 in ~15 days (vs $280 in 30 days)
    Why: Capture most of the profit, free up capital, reduce risk

  - Put has lost 75% of its value -> Strongly consider closing
    Example: Sold for $2.80, now worth $0.70 -> Buy back at $0.70
    Profit: $210 in ~20 days
    Why: Remaining $70 is not worth the risk of holding

  CUT LOSS (Buy back the put at a loss):
  - Put has DOUBLED in value -> Consider closing
    Example: Sold for $2.80, now worth $5.60 -> Buy back at $5.60
    Loss: -$280
    Why: Prevent further loss. The stock has moved against you.
    Reassess whether you still want to own the stock.

  - Stock has dropped through strike with bad news -> Close
    If the reason for the drop changes your thesis about the company,
    take the loss and move on.

  ROLL (Close current put, open new one):
  - Stock is near strike with a few days left
  - You still want to own it, but want more premium
  - Close the current put, sell next month's put
  - Example: Buy back $145 March Put at $3.50, sell $145 April Put
    for $5.00 -> Net credit of $1.50

MANAGEMENT SCHEDULE:
  Day 1-7:    Set it and forget it (unless major news)
  Day 8-20:   Check weekly. Close if 50%+ profit achieved.
  Day 21-25:  Evaluate closely. Roll or close if needed.
  Day 26-30:  Expiration week. Final decision: expire or close.
```

#### Building a Cash-Secured Put Portfolio

For investors with sufficient capital, running a diversified portfolio of cash-secured puts can generate substantial, consistent income.

```
CASH-SECURED PUT PORTFOLIO EXAMPLE: $100,000 Capital

Allocation Strategy:
  - 5 positions across different sectors
  - 15-20% of capital per position
  - 10-15% kept as cash buffer for opportunities or margin of safety

+--------------------------------------------------------------+
| STOCK | SECTOR      | STRIKE | CAPITAL  | PREMIUM | ANN YLD |
+--------------------------------------------------------------+
| AAPL  | Technology  | $140   | $14,000  | $1.80   | 15.4%   |
| JPM   | Financials  | $180   | $18,000  | $2.50   | 16.7%   |
| JNJ   | Healthcare  | $150   | $15,000  | $1.60   | 12.8%   |
| KO    | Cons.Staple | $55    | $16,500* | $0.70   | 15.3%   |
|       |             |        | (3 cnts) |         |         |
| AMZN  | Consumer    | $180   | $18,000  | $3.20   | 21.3%   |
+--------------------------------------------------------------+
| TOTAL               |        | $81,500  | $1,250  | 15.7%   |
| Cash buffer          |        | $18,500  |         |         |
+--------------------------------------------------------------+
* 3 contracts of KO at $55 = $16,500

Monthly Income: $1,250 (premiums across 5 positions)
Annual Income: $15,000 (15.0% on invested capital)
Annual Income on Total: $15,000 / $100,000 = 15.0%

Diversification:
  Technology: 14%
  Financials: 18%
  Healthcare: 15%
  Consumer Staples: 16.5%
  Consumer Discretionary: 18%
  Cash: 18.5%
```

#### Comparing Cash-Secured Puts Across Different Market Environments

Understanding how the strategy performs in different conditions helps you set realistic expectations:

```
PERFORMANCE IN DIFFERENT MARKETS:

BULL MARKET (stock rising 15-25% per year):
  - Puts expire worthless month after month
  - You collect premium but never buy the stock
  - Annual return on cash: 10-18% (premiums only)
  - Emotional challenge: Watching the stock rise without owning it
  - Reality check: You are earning more than a savings account
  - Adjustment: Consider selling closer to ATM for higher premiums
                 or just buy the stock at market

FLAT MARKET (stock moves sideways, +/- 5%):
  - Most puts expire worthless
  - Occasional assignment followed by recovery
  - Annual return on cash: 12-18% (premiums)
  - This is the IDEAL environment for put selling
  - You earn consistent income while the stock goes nowhere

MILD BEAR MARKET (stock declining 5-15%):
  - You get assigned on some puts
  - Effective cost is below strike price (premium cushion)
  - You own stocks at discounted prices
  - Transition to covered calls on assigned shares
  - Net result: Buying stocks at good prices with income along the way

SEVERE BEAR MARKET (stock declining 25%+):
  - Multiple assignments
  - Unrealized losses on assigned shares
  - Premium cushion helps but does not eliminate losses
  - This is the time to hold assigned shares and sell covered calls
  - Long-term: These become your best entry prices
  
  HISTORICAL EXAMPLE: Selling AAPL puts in 2022
    AAPL dropped from $182 to $129 (29% decline)
    Put seller assigned at ~$150, effective cost ~$145
    By mid-2023, AAPL recovered to $190
    Result: 31% gain from effective cost in ~12 months
    Plus: Covered call premiums during the hold = additional 8-12%
```

#### Practical Checklist: Before You Sell a Put

Use this checklist every time you are about to sell a cash-secured put:

```
PRE-TRADE CHECKLIST:

  STOCK QUALITY:
  [ ] Company has been profitable for at least 3 years
  [ ] Debt-to-equity ratio is reasonable for its industry
  [ ] No pending litigation or regulatory risks that concern me
  [ ] I understand what the company does and how it makes money
  [ ] I would hold this stock for at least 2-3 years if assigned

  STRIKE SELECTION:
  [ ] Strike is at or below my fair value estimate
  [ ] Strike is at least 5% below current price (for OTM approach)
  [ ] If assigned, my total position in this stock stays under 20%
  [ ] I have confirmed the support level on the price chart

  EXPIRATION SELECTION:
  [ ] 30-45 days to expiration
  [ ] No earnings announcement between now and expiration
  [ ] No major economic events (Fed meeting, etc.) that concern me

  PREMIUM CHECK:
  [ ] Annualized yield is at least 8% (my minimum threshold)
  [ ] Bid-ask spread is tight (under $0.30 for a ~$3 option)
  [ ] Volume and open interest are sufficient (at least 100 OI)

  CAPITAL CHECK:
  [ ] I have cash to cover the full assignment (strike x 100)
  [ ] This position does not use more than 20% of my total capital
  [ ] I have at least 15% of my total capital in cash reserve
  [ ] I am NOT using margin for this position

  MANAGEMENT PLAN:
  [ ] I know at what profit level I will close early (50-75%)
  [ ] I know at what loss level I will cut the position (2x premium)
  [ ] If assigned, I have a plan (sell covered calls or hold)
```

#### Risk Management for Cash-Secured Puts

Understanding and managing risk is essential for long-term success:

```
RISK MANAGEMENT FRAMEWORK:

  1. STOCK SELECTION RISK
     Mitigation: Only sell puts on stocks you want to own
     - Strong balance sheet (low debt)
     - Consistent earnings growth
     - Competitive moat
     - Reasonable valuation at your strike price
     Rule: If you would not buy 100 shares at the strike with a
     market order, do NOT sell a put at that strike.

  2. CONCENTRATION RISK
     Mitigation: Diversify across sectors and stocks
     - Maximum 20% of capital in any single stock
     - Minimum 4-5 different stocks
     - Spread across at least 3 sectors
     Rule: No single assignment should be devastating to your portfolio.

  3. MARKET CRASH RISK
     Mitigation: Keep 15-20% cash buffer
     - If ALL positions are assigned, you still have cash reserves
     - A crash that assigns all puts at once is rare but possible
     - In a broad crash, your effective costs are still below market
     Rule: Size positions so that being assigned on ALL of them
     simultaneously does not exceed your total capital.

  4. EARNINGS/EVENT RISK
     Mitigation: Avoid selling puts expiring during earnings week
     - Earnings can cause 10-20% gaps overnight
     - If you sell a put through earnings, accept the gap risk
     - Better: sell puts AFTER earnings, when IV has settled
     Rule: Know the earnings calendar for every stock you sell puts on.

  5. OPPORTUNITY COST RISK
     Mitigation: Use short-duration puts (30-45 days)
     - Cash is tied up for the option's duration
     - If a better opportunity arises, you may not have free cash
     - Shorter durations free cash more frequently
     Rule: Keep enough liquid cash to act on unexpected opportunities.

MAXIMUM LOSS CALCULATION:

  Absolute worst case (stock goes to $0):
    Max Loss = (Strike Price - Premium) x 100 x Number of Contracts
    
    AAPL $140 Put at $2.80:
    Max Loss = ($140 - $2.80) x 100 = $13,720 per contract
    
    This would require AAPL to go to $0, which is essentially
    impossible for a company of Apple's size and financial strength.

  Realistic worst case (stock drops 30%):
    AAPL drops from $155 to $108.50
    You buy at $140, effective cost $137.20
    Unrealized loss: ($137.20 - $108.50) x 100 = $2,870
    
    This is painful but manageable, especially if you believe
    AAPL will recover and you start selling covered calls.
```

---

### c) Common Misconceptions

**Misconception 1: "Selling puts is the same as buying stock, so why bother?"**

While the risk profiles are similar (both have downside exposure), the economics are different. The put seller has a lower effective cost basis (by the amount of the premium), and earns income while waiting for the entry price. A stock buyer at $155 starts at $155. A put seller at $145 strike with $2.80 premium starts at $142.20 if assigned, and earns $280 if not. Over time, the put seller's entry is significantly better.

**Misconception 2: "Cash-secured puts tie up too much capital."**

This is true if you compare it to margin-based strategies, but the comparison should be to what you would do with the cash otherwise. If the cash is sitting in a savings account at 4-5%, selling cash-secured puts at 12-18% annualized yield is a dramatic improvement. The capital is "tied up" in the same way it would be tied up waiting for a limit order to fill: you have decided to buy the stock at a certain price, so the capital is already mentally allocated.

**Misconception 3: "You should sell puts on high-volatility stocks for bigger premiums."**

Higher volatility does mean higher premiums, but it also means higher probability of large drops, which increases assignment risk and potential losses. A biotech stock might offer $8 in premium on a $50 put, but the stock could easily drop 40% on a failed drug trial. You should sell puts on stocks with moderate volatility that you genuinely want to own, not on the most volatile names for premium size alone.

**Misconception 4: "Getting assigned on a put is a bad outcome."**

Assignment means you bought a stock you wanted at a price you chose, at an effective cost lower than that price. This is a successful execution of your plan. The only time assignment is truly bad is when the stock drops catastrophically due to fundamental problems (fraud, bankruptcy, structural decline). This risk exists equally with any form of stock purchase. Assignment itself is neutral to positive.

**Misconception 5: "I should always roll to avoid assignment."**

Rolling has a cost. If the stock is below your strike and you roll, you are buying back an in-the-money put (expensive) and selling a new one (hopefully for more). The net credit may be small or you may even pay a debit. If you want the stock at the strike price, just accept assignment. Rolling makes sense only when: (a) your view on the stock has changed and you no longer want to buy, or (b) you want more time to collect premium before buying.

**Misconception 6: "Cash-secured puts only work in bull markets."**

Cash-secured puts actually work in ALL market environments, but the outcomes differ. In bull markets: puts expire worthless, you keep premium. In flat markets: same result, premium income is your return. In mild bear markets: you get assigned and buy stocks at a discount, which is ideal for long-term investors. In severe bear markets: you buy stocks at a discount but face unrealized losses, though your effective cost is still better than buying without the put strategy. The strategy fails only if you are selling puts on fundamentally flawed companies.

---

### d) Common Questions and Answers

**Q1: How is a cash-secured put different from a naked put?**

A: The strategy is the same; the collateral is different. A cash-secured put requires you to have the full cash amount to buy the shares ($14,000 for a $140 put). A naked put uses margin, meaning you only need to post a fraction of the value (perhaps $3,000-$5,000 depending on your broker). Naked puts have the same profit potential but carry additional risk because if you are assigned and the stock drops further, you may face a margin call. In this course, we exclusively teach cash-secured puts because they eliminate margin risk and align with a conservative investing philosophy.

**Q2: Can I sell puts on index ETFs like SPY?**

A: Yes, and SPY puts are among the most liquid options in the world. The capital requirement is higher ($52,000 for a $520 put), but you get broad market diversification in a single contract. SPY puts are an excellent choice for investors who want to build a position in the overall market at a lower price. The premiums on SPY are somewhat lower on a percentage basis (due to lower volatility), but the consistency and liquidity are exceptional.

**Q3: What happens if I do not have enough cash when I am assigned?**

A: If your put is cash-secured, this should not happen because your broker has already reserved the full amount. If you are using margin and get assigned without sufficient funds, your broker will issue a margin call. You will need to either deposit more cash or sell securities to cover the purchase. This is one of the key reasons we recommend cash-secured puts over naked puts: the cash is always there when needed.

**Q4: Should I sell puts weekly or monthly?**

A: Monthly (30-45 days) is recommended for most investors. Weekly puts require more frequent management and have smaller individual premiums. While the annualized yield of weekly puts can be higher, the additional effort and transaction frequency often do not justify the marginal increase. Monthly puts provide a good premium with minimal management. If you are more experienced and have time, selling weekly puts can work, but start with monthly.

**Q5: What is the difference between selling a put and buying a deep-in-the-money call?**

A: Economically, they are similar but not identical. Both give you bullish exposure with a lower initial outlay than buying stock. However, selling a put generates income (you receive premium), while buying a call costs money (you pay premium). Selling a put also requires full cash collateral and has limited profit (the premium). Buying a deep ITM call costs less upfront but loses value to time decay and has unlimited profit potential. For income-oriented investors, selling puts is generally preferred.

**Q6: How do I account for dividends when selling puts?**

A: If you sell a put on a dividend-paying stock and get assigned, you will receive future dividends on the shares you now own. However, you do not receive dividends while you hold the short put position (you do not own the shares yet). This is a minor disadvantage compared to owning the stock outright, but the put premium typically exceeds the dividend you would have received during the same period.

**Q7: What happens to my put if the stock splits?**

A: Options are adjusted for stock splits. If AAPL does a 4-for-1 split and you have a $140 put, your position would be adjusted to 4 contracts of $35 puts (same economic exposure). The OCC handles all adjustments automatically. You do not need to take any action.

**Q8: Can I sell puts in a margin account even if I want them cash-secured?**

A: Yes. You can choose to keep enough cash in your margin account to fully cover the put, effectively making it cash-secured even though the account type allows margin. Many investors use margin accounts for the flexibility but maintain cash reserves equivalent to full coverage. The key discipline is not using the margin to sell more puts than you could cover with cash.

**Q9: What if I want to be more conservative? Can I sell puts on stocks I already own?**

A: Yes, this is called selling an "additional put." If you already own 100 shares of AAPL and sell a $140 put, getting assigned would give you 200 shares. This is a way to double down on stocks you love at lower prices. Just ensure your total position size remains within your risk tolerance and portfolio allocation limits.

**Q10: How does the wheel strategy compare to traditional buy-and-hold?**

A: Over long periods, the wheel strategy typically generates higher income but may slightly underperform during strong bull markets (due to the covered call capping upside). In flat and mildly bearish markets, the wheel significantly outperforms because of the premium income. Research on the CBOE PutWrite Index (PUT) shows that a systematic put-writing strategy has delivered returns comparable to the S&P 500 with about 25-30% less volatility. The wheel adds covered calls on top, further enhancing income. For income-focused investors, the wheel is often superior to pure buy-and-hold.

---

## YouTube Script

[VISUAL: Animated intro with show logo. Text: "Week 28: Cash-Secured Puts for Entry - Level 3: Advanced"]

**Alex:** Welcome back. Over the past three weeks, we have built a complete foundation in options. We started with the basics in Week 25, then learned to think of options as conditional orders in Week 26, and mastered covered calls for income in Week 27. Today we complete the picture with cash-secured puts.

**Sam:** And then we are going to put it all together with the wheel strategy?

**Alex:** That is exactly right. Cash-secured puts are the entry mechanism of the wheel. They are how you get into stocks while getting paid to do so. By the end of today, you will have the complete toolkit.

[VISUAL: A wheel diagram showing the cycle: "Cash -> Sell Puts -> Assigned -> Own Shares -> Sell Calls -> Called Away -> Cash" with today's focus "Sell Puts" highlighted]

**Sam:** OK, let us start with the basics. What is a cash-secured put?

**Alex:** A cash-secured put is when you sell a put option and keep enough cash in your account to buy the shares if you are assigned. You are making a promise: I will buy this stock at this price if it drops to that level. In return, someone pays you a premium right now.

**Sam:** And the "cash-secured" part means I am not using borrowed money?

**Alex:** Exactly. Your broker holds the full amount, say $14,000 for a $140 put, as collateral. If you are assigned, that cash is used to buy the shares. No margin, no borrowed money, no surprises.

[VISUAL: Diagram showing a bank vault labeled "$14,000" connected to a put option contract. Arrow labeled "Premium $280" flowing from the option to the investor's pocket. Arrow labeled "If assigned" flowing from the vault to "100 shares"]

**Sam:** Let me walk through an example. Apple is at $155 and I think $145 is a great price to buy.

**Alex:** Perfect setup. Instead of placing a limit order at $145, you sell one AAPL $145 put expiring in 30 days. Let us say the premium is $2.80. You receive $280 immediately, and your broker reserves $14,500 in cash.

**Sam:** And now what?

**Alex:** Now you wait. And one of four things will happen.

[ANIMATION: Reference animation/week28_cash_secured_put.py - Animation showing a stock price chart with AAPL starting at $155 and a $145 strike line drawn horizontally. Four animated paths branch from the starting point: (1) stock stays flat around $155, (2) stock rises to $175, (3) stock drops to $144, (4) stock drops sharply to $125. For each path, the animation shows the outcome: premium kept or assignment occurring, with the effective cost calculator updating in real-time. A running P&L display shows the put seller's position at each stage.]

**Alex:** Scenario one, the most common: Apple stays above $145. The put expires worthless. You keep the $280 and your $14,500 is freed up. You earned 1.9% in 30 days, which is 23.6% annualized. Then you sell another put for next month.

**Sam:** Nice. Scenario two?

**Alex:** Apple drops to exactly $145 or slightly below. You are assigned. You buy 100 shares at $145. But remember, you already received $2.80 per share in premium, so your effective cost is $142.20.

**Sam:** Which is lower than what a limit order would have given me.

**Alex:** By $2.80 per share. That is 1.9% better than a limit order. And it does not sound like much, but over many cycles, these savings compound dramatically.

[VISUAL: Two receipts side by side. Left: "Limit Order Receipt - 100 shares AAPL at $145.00 - Total: $14,500". Right: "Cash-Secured Put Receipt - 100 shares AAPL at $145.00 - Premium Received: -$280 - Effective Cost: $14,220 - Savings: $280"]

**Sam:** What about scenario three, a big drop?

**Alex:** Say Apple drops to $125. You are assigned at $145, effective cost $142.20. You are now sitting on an unrealized loss of $17.20 per share. This is the risk of the strategy.

**Sam:** But the limit order person is also sitting on a loss.

**Alex:** Right. The limit order buyer at $145 has an unrealized loss of $20 per share. You have a loss of $17.20 per share. You are $2.80 better off. In a big drop, nobody wins, but the put seller loses slightly less.

**Sam:** And scenario four? Apple rockets higher?

**Alex:** Apple goes to $175. Your put expires worthless. You keep the $280 but you did not buy any shares. You "missed" the rally. But here is the thing: your limit order at $145 also was not filled. The limit order person also missed the rally and earned nothing. You at least earned $280.

[VISUAL: Scoreboard showing all four scenarios. For each, the put seller's outcome is compared to the limit order person's outcome. In every scenario, the put seller is equal to or better than the limit order approach.]

**Alex:** In every single scenario, the put seller does at least as well as the limit order, and usually better. That is the fundamental mathematical advantage of this strategy.

**Sam:** That is compelling. Now let me ask about strike price selection. How do I decide what strike to sell?

**Alex:** There are several approaches, and the best one depends on your situation. The first approach is fundamental valuation. You estimate the stock's fair value and set your strike at or below that number.

**Sam:** So if I think Apple is worth $145 based on its PE ratio and earnings, I sell the $145 put?

**Alex:** Exactly. You are saying, I am willing to buy Apple at fair value, and I will accept premium for making that commitment. The second approach is using support levels from a price chart. If Apple has bounced off $148 three times in the past year, that is a strong support level and a logical strike.

**Sam:** And the third approach?

**Alex:** Percentage below market. Simply go 5-10% below the current price. For Apple at $155, that is $140-$147. This is the simplest approach and works well for beginners.

[VISUAL: Three-panel display. Panel 1: Fundamental analysis showing PE ratio and earnings with a "Fair Value: $145" label. Panel 2: Price chart with support line at $148. Panel 3: Current price $155 with 5% and 10% arrows pointing to $147 and $140 respectively.]

**Sam:** I notice there is always a tradeoff between the premium and the strike distance. Can you walk through that?

**Alex:** Absolutely. The further out of the money you go, the less premium you receive, but the lower your probability of being assigned. Think of it as a dial between income and safety.

[VISUAL: A dial/gauge with "More Income" on the left and "More Safety" on the right. Specific strike prices are marked along the dial with their premiums and assignment probabilities.]

**Alex:** At the $155 strike, right at the money, you might get $4.50 in premium. That is a 3% monthly return, but there is a 50% chance you get assigned. At the $145 strike, 6.5% out of the money, you get $1.70. That is a 1.2% monthly return with about a 25% chance of assignment. At $135, 13% out of the money, you get $0.50. That is 0.4% per month with only a 12% chance of assignment.

**Sam:** So for conservative investors, the $140-$145 range seems like the sweet spot?

**Alex:** For most people, yes. You are getting a meaningful premium, maybe 1-2% per month, with a 15-25% chance of assignment at a price you would love to own the stock. If you are assigned, you are happy. If you are not, you earned income. Win-win.

**Sam:** Now let us talk about what happens after assignment. I sold a put, I got assigned, I now own 100 shares. What do I do?

**Alex:** This is where the wheel strategy comes alive. Step one: check that the stock's fundamentals are still intact. Is this drop temporary or permanent? If the company is still strong, step two: start selling covered calls on your new shares.

**Sam:** So I immediately transition from put selling to covered call selling?

**Alex:** Exactly. Let us say you were assigned on AAPL at $145, effective cost $142.20. The stock is now at $143. You sell a $155 covered call for $2.50. Now you are collecting income while you wait for the stock to recover.

[VISUAL: Transition animation showing the wheel turning from "Phase 1: Put Selling" to "Phase 2: Covered Call Selling". The investor's dashboard changes from showing a short put position to showing long shares plus a short call.]

**Alex:** If Apple recovers to $155 and your shares are called away, your total profit on the cycle is: $155 minus $142.20 effective cost plus $2.50 call premium equals $15.30 per share. That is a $1,530 profit on a position that started with a put.

**Sam:** And then you go back to selling puts?

**Alex:** You go back to Phase 1. You have $15,500 in cash from the sale, plus the accumulated premiums. You sell another put and the wheel keeps turning.

[VISUAL: The complete wheel cycle shown as a circular flow chart with dollar amounts at each stage, showing how capital grows through each phase]

**Sam:** Let me ask about the complete portfolio approach. If I have $100,000, how should I set this up?

**Alex:** Divide your capital across 4-6 quality stocks in different sectors. Keep 15-20% as a cash buffer. Sell one monthly put on each stock.

[VISUAL: Portfolio allocation pie chart with 5 stocks and a cash buffer segment, showing the specific positions and premiums]

**Alex:** With $100,000, you might have five positions using about $80,000 in capital, with $20,000 in reserve. Each month, you collect roughly $1,000-$1,500 in total premiums. That is $12,000-$18,000 per year, or 12-18% on your total capital.

**Sam:** And if one or two get assigned?

**Alex:** You start selling covered calls on those positions while continuing to sell puts on the others. Your portfolio evolves naturally between Phase 1 and Phase 2 positions. Some months you might have all puts. Other months, a mix of puts and covered calls. The income keeps flowing regardless.

**Sam:** This is starting to feel like a real income business.

**Alex:** That is exactly what it is. And the best part is, it aligns perfectly with what a long-term investor already wants to do. You are buying quality stocks at good prices and selling them at higher prices. The wheel just pays you at every step of that process.

[ANIMATION: Reference animation/week28_cash_secured_put.py - A second animation sequence showing a 12-month wheel strategy simulation. The animation shows a portfolio of 3 stocks cycling through put selling and covered call phases. A monthly income tracker shows premiums accumulating. An equity curve shows the portfolio value growing steadily compared to a simple buy-and-hold approach. Key metrics update: total premiums collected, number of assignments, total return.]

**Sam:** Let us talk about risk management. What are the things that could go wrong?

**Alex:** The biggest risk is a stock you sell puts on experiencing a fundamental deterioration. Imagine selling puts on a company that then announces massive fraud or a failed product. The stock drops 50% and you are forced to buy at your strike price.

**Sam:** How do you protect against that?

**Alex:** Three ways. First, only sell puts on high-quality companies with strong balance sheets, competitive moats, and consistent earnings. You are not selling puts on speculative biotech stocks or meme stocks. Second, diversify. If you have five positions and one stock drops 30%, it is painful but not devastating. Third, have a stop-loss mentality. If the stock starts dropping and the fundamental thesis changes, buy back the put at a loss. A $500 loss is much better than a $5,000 loss.

[VISUAL: Three pillars of risk management: "Quality Companies" (images of blue-chip logos), "Diversification" (pie chart), "Stop-Loss Discipline" (circuit breaker image)]

**Sam:** What about market-wide crashes? Like 2008 or March 2020?

**Alex:** In a broad market crash, if you have puts on five stocks and the market drops 25%, you could be assigned on all of them. This is where the cash buffer matters. If you have $100,000 and only $80,000 in put positions, you can handle the assignments without stress.

**Alex:** But here is the silver lining: in a crash, you are buying stocks at your target prices during maximum fear. Historically, these have been the best times to buy. If you sold $145 puts on Apple and the market crashes to bring Apple to $130, you buy at an effective cost of $142.20. If Apple recovers to $200 over the next two years, which it historically does, you made an incredible entry.

**Sam:** So the short-term pain is real, but the long-term opportunity is also real.

**Alex:** Exactly. The put seller's advantage is that they entered at $142.20, not $145. Every dollar matters when you are buying at a low.

[VISUAL: Historical chart showing S&P 500 crashes and recoveries: 2008, 2020, 2022. Arrows showing "Put sellers buying here" at the low points, with recovery trajectories and eventual profits.]

**Sam:** Let me ask about expiration selection. We talked about 30-45 days being the sweet spot for covered calls. Is it the same for puts?

**Alex:** Same principles apply. 30-45 days gives you the best balance of premium versus time commitment. Theta decay accelerates after 45 days, so you capture the most decay per day. Monthly cycles align well with most people's schedules: spend 30 minutes on expiration day managing positions, then forget about it for three weeks.

**Sam:** What about weekly puts?

**Alex:** Weekly puts give you higher annualized yields on paper, but they require weekly attention, have smaller absolute premiums per trade, and sometimes the bid-ask spread eats up a larger percentage of the premium. For most investors, monthly is the way to go. Weekly works for experienced traders who enjoy the process.

[VISUAL: Calendar view showing monthly put selling schedule. One day per month highlighted as "Management Day" where positions are reviewed and new puts are sold.]

**Sam:** Can I do all of this in my Roth IRA?

**Alex:** Absolutely, and I strongly recommend it. In a Roth IRA, the premium income grows tax-free forever. No capital gains tax, no income tax on premiums. Over 20-30 years, the tax savings from doing this strategy in a Roth IRA can amount to tens or hundreds of thousands of dollars.

**Sam:** That is huge. What about traditional IRAs?

**Alex:** Also excellent. The income grows tax-deferred. You pay taxes when you withdraw, but in the meantime, you can reinvest the full premium amount without any tax drag. Both IRA types are ideal for the wheel strategy.

[VISUAL: Comparison of three accounts: "Taxable: Premium taxed at 22-37%", "Traditional IRA: Tax-deferred", "Roth IRA: TAX-FREE". A 20-year growth chart shows the compounding difference.]

**Sam:** Let us do one more complete example. Walk me through a full year of cash-secured put selling.

**Alex:** Let us do it with Microsoft, currently at $420. We think $380 is a great entry price.

[VISUAL: MSFT stock chart with $380 level marked. Monthly timeline below showing put selling activity.]

**Alex:** Month 1: We sell the $380 put for $4.50. Microsoft stays at $415. Put expires. We keep $450.

Month 2: Sell $380 put for $3.80. Microsoft at $425. Expires. Keep $380.

Month 3: Sell $380 put for $5.00. Microsoft at $410. Expires. Keep $500.

Month 4: Sell $380 put for $4.20. Microsoft at $418. Expires. Keep $420.

Month 5: Sell $380 put for $6.50 (higher IV before earnings). Microsoft drops to $395 after earnings but stays above $380. Expires. Keep $650.

Month 6: Sell $380 put for $4.00. Microsoft at $400. Expires. Keep $400.

**Sam:** So after six months, we have collected $2,800 in premiums and Microsoft never hit our price.

**Alex:** Right. $2,800 on $38,000 reserved capital is 7.4% in six months, or about 14.7% annualized. And we still have not bought the stock.

Month 7: Sell $380 put for $5.20. Microsoft drops to $375. We get assigned.

**Sam:** So now we own 100 shares at $380.

**Alex:** Yes, but our effective cost is much lower. We collected $2,800 plus the final $520 premium. Total premiums: $3,320, or $33.20 per share. Our effective cost basis is $380 minus $33.20 equals $346.80.

[VISUAL: Calculator showing the running total: 7 months of premiums adding up to $3,320. Final effective cost: $346.80 vs original price of $420 when we started. Savings: $73.20 per share or 17.4%.]

**Sam:** We effectively bought Microsoft at $346.80 when it was at $420 when we started. That is a 17% discount.

**Alex:** And now we start Phase 2. We sell covered calls on our 100 shares at a strike above our cost basis. Even though Microsoft is at $375 now, our cost is $346.80, so we have room to sell calls at $360, $370, or $380 and still make a profit if called away.

**Sam:** The wheel keeps turning.

**Alex:** And income keeps flowing. That is the beauty of the system.

**Sam:** One last thing I want to address. Some people watching this are going to say, why not just buy the stock? Why go through all this?

**Alex:** Fair question. If you have a stock you want to own right now and you believe it will go up significantly, buying at market is fine. Cash-secured puts are not about avoiding stock ownership. They are about making the process of building positions more efficient and profitable.

**Alex:** Think of it this way. A contractor could dig a foundation with a shovel or with an excavator. Both get the job done. But the excavator is more efficient. Cash-secured puts are the excavator. Same end result, stock ownership, but with income along the way and a better effective entry price.

[VISUAL: Side-by-side: "Buying Stock = Shovel" (simple, direct) vs "Cash-Secured Puts = Excavator" (more efficient, better result)]

**Sam:** I love that analogy. Let me summarize today. A cash-secured put means selling a put while holding enough cash to buy the shares. It is like a limit buy order that pays you. Your effective purchase price is always lower than the strike price because of the premium. If the stock stays above the strike, you keep the premium and try again. If you are assigned, you start selling covered calls. And this creates the wheel strategy: a continuous cycle of income generation.

**Alex:** Perfect. And I want to leave everyone with this thought: the wheel strategy is not about getting rich quick. It is about building a systematic, income-generating investment machine. Month after month, year after year, the premiums accumulate, the positions cycle, and your wealth grows with a level of consistency that few other strategies can match.

**Sam:** Before we close, can we do a rapid-fire FAQ? I have a bunch of quick questions that viewers have sent in.

**Alex:** Let us do it.

**Sam:** Can I sell puts in a Roth IRA?

**Alex:** Yes, and I highly recommend it. Premiums grow tax-free forever. Most brokers allow cash-secured puts and covered calls in Roth and traditional IRAs.

**Sam:** What happens if I get assigned and the stock keeps dropping?

**Alex:** You hold the stock and start selling covered calls. The premiums from covered calls reduce your cost basis further. If the company is still fundamentally sound, the stock will eventually recover, and you will profit from the recovery plus all the premiums collected.

**Sam:** Is there a minimum account size?

**Alex:** For cash-secured puts, you need enough to buy 100 shares at the strike price. For a $55 stock like Coca-Cola, that is $5,500. For a $180 stock like JPMorgan, that is $18,000. Start with lower-priced quality stocks if you have a smaller account.

**Sam:** Can I sell puts on ETFs?

**Alex:** Yes, SPY, QQQ, IWM, and sector ETFs all have active options markets. ETF puts are a great way to build positions in the broad market at lower prices. The premiums are slightly lower percentage-wise due to lower volatility, but the diversification benefit is significant.

**Sam:** What is the difference between a cash-secured put and a naked put?

**Alex:** Same option trade, different collateral. Cash-secured means you have 100% of the cash to buy the shares. Naked means you are using margin and only posting a fraction. We exclusively teach cash-secured because it eliminates margin risk. Never sell naked puts as a beginner.

**Sam:** How many stocks should I sell puts on at once?

**Alex:** Four to six is a good range. This gives you diversification without becoming unmanageable. Each position should use no more than 20% of your total capital, and you should keep 15-20% as a cash reserve.

**Sam:** What if I want to buy a stock right now? Should I still sell a put?

**Alex:** If you want to buy immediately and you are bullish, just buy the stock. Cash-secured puts are for when you want to buy at a LOWER price. If you are patient and have a target entry, sell the put. If you think the stock is going up and you do not want to miss it, buy at market.

**Sam:** Last question: what is the single biggest mistake new put sellers make?

**Alex:** Selling puts on stocks they would not actually want to own. They see a fat premium on a volatile stock and think, "This will never hit the strike." Then it does, and they are stuck owning 100 shares of a company they do not believe in. Only sell puts on stocks you love at prices you would celebrate buying at.

**Sam:** Love it. Sell puts on stocks you love at prices you would celebrate. That should be on a poster.

**Alex:** Maybe I will make one.

**Sam:** Thank you all for joining us through these four weeks of options education. We started knowing nothing about options, and now we have a complete, practical framework.

**Alex:** If you have watched all four lessons, you now understand more about practical options strategies than most investors ever will. Start small, practice with one or two positions, and scale up as you gain confidence. The wheel rewards patience and discipline.

**Sam:** Let me give our four-lesson summary for anyone who wants the big picture.

[VISUAL: Four-panel summary appearing one by one]

**Sam:** Week 25: We learned what options are. Calls, puts, strike prices, expiration, time decay. The building blocks.

**Sam:** Week 26: We learned to think of options as conditional orders. Puts are paid limit buys. Calls are paid limit sells. This is the mental model that makes everything click.

**Sam:** Week 27: We mastered covered calls. Own shares, sell calls, generate income. Premium income can be 2-3 times dividends or more.

**Sam:** Week 28: We completed the picture with cash-secured puts. Get paid to wait for your buy price. When assigned, start selling covered calls. The wheel keeps turning.

**Alex:** And here is the beautiful thing: these four lessons give you a complete, practical system. You do not need to learn straddles, strangles, iron condors, or butterfly spreads. The wheel strategy, using only cash-secured puts and covered calls, is all most long-term investors will ever need.

**Sam:** Simple, powerful, and proven. Thanks for watching, everyone.

**Alex:** Please like and subscribe if this series has been valuable. And leave a comment telling us about your first cash-secured put or covered call trade. We love hearing your stories. See you in the next lesson.

[VISUAL: End screen with subscribe button. Series recap showing all four weeks: "Week 25: Options Basics -> Week 26: Options as Orders -> Week 27: Covered Calls -> Week 28: Cash-Secured Puts". Text: "You now have the complete toolkit. Start the wheel."]

---

*Animation Reference: animation/week28_cash_secured_put.py - This animation shows two main sequences. First, an interactive payoff diagram for a cash-secured put, where the strike price and premium can be adjusted. The effective purchase price updates dynamically. Four stock price paths are animated to show each scenario (stays above, drops to strike, drops well below, rallies higher), with outcome boxes appearing for each. Second, a 12-month wheel strategy simulation showing a portfolio of 3 stocks cycling through put and covered call phases. Monthly income bars accumulate in a chart, and an equity curve compares the wheel approach to simple buy-and-hold, demonstrating the income advantage in flat and mildly bearish markets.*
