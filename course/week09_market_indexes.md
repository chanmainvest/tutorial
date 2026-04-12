# Week 9: Understanding Market Indexes

---

## Reading Section

### a) Why This Is Important

Every day, you hear phrases like "the Dow is up 200 points" or "the S&P 500 hit a new all-time high." These market indexes are the scoreboard of the financial world. They tell you how the market is performing, they serve as benchmarks against which your own portfolio is measured, and they form the backbone of the largest investment products on earth -- index funds and ETFs. If you do not understand how indexes are constructed, you cannot understand what you are actually buying when you invest in an index fund, and you cannot evaluate whether your own performance is good, bad, or mediocre.

Understanding indexes matters for several critical reasons:

1. **Indexes define the market.** When someone says "the market was up 2% today," they are referring to an index. But which index? The Dow Jones Industrial Average, which tracks just 30 large U.S. stocks? The S&P 500, which covers 500? The Russell 2000, which focuses on small companies? Each tells a different story, and conflating them leads to confusion and poor decisions.

2. **Most investors own index funds.** Over the past two decades, index investing has become the dominant investment strategy. More than $15 trillion is invested in index funds globally. When you buy an S&P 500 index fund, you are making an implicit bet on every design choice embedded in that index -- how it selects stocks, how it weights them, and how it rebalances. These seemingly technical details have real consequences for your returns.

3. **Index construction creates market distortions.** When a stock is added to or removed from a major index, billions of dollars of forced buying and selling occur as index funds adjust their holdings. These mechanical flows can move stock prices by 3-7% or more, creating both risks and opportunities for informed investors. If you understand the plumbing, you can avoid being harmed by it and potentially benefit.

4. **Benchmarking requires the right benchmark.** If you hold a portfolio of small-cap growth stocks and compare your returns to the S&P 500, you are comparing apples to oranges. Choosing the right benchmark is essential for honestly evaluating your performance, and that requires understanding what each index actually represents.

5. **Global perspective demands index literacy.** Investing internationally means navigating dozens of indexes -- the FTSE 100, Nikkei 225, MSCI Emerging Markets, and many more. Each has its own methodology, biases, and quirks. Understanding the principles of index construction allows you to evaluate any index, anywhere in the world.

This lesson covers how indexes are built, the critical differences between weighting methods, how reconstitution and rebalancing work, and what this all means for you as an investor.

---

### b) What You Need to Know

#### 1. What Is a Market Index?

A market index is a statistical measure that tracks the performance of a selected group of stocks. It is not something you can buy directly. Instead, it is a calculation -- a number that goes up or down based on the collective movement of its component stocks.

Think of an index like a recipe. The recipe specifies which ingredients (stocks) to include and how much of each ingredient to use (the weighting method). Different recipes produce different dishes, even if some of the same ingredients appear in multiple recipes.

```
ANATOMY OF A MARKET INDEX
===========================

Every index has three key design choices:

1. SELECTION RULES       What stocks are included?
   (Universe)            - Size criteria (market cap thresholds)
                         - Liquidity requirements
                         - Sector representation
                         - Domicile / listing exchange

2. WEIGHTING METHOD      How much does each stock count?
   (Recipe)              - Price-weighted
                         - Market-cap-weighted
                         - Equal-weighted
                         - Factor-weighted (smart beta)

3. MAINTENANCE RULES     How often is the list updated?
   (Rebalancing)         - Scheduled reconstitution
                         - Buffer rules for additions/deletions
                         - Corporate action adjustments
```

These three design choices produce dramatically different outcomes. Two indexes can hold many of the same stocks but deliver very different returns depending on how they weight those stocks.

---

#### 2. The Three Major Weighting Methods

This is the most important concept in this lesson. The weighting method determines how much influence each stock has on the index's movement.

**Price-Weighted Index**

In a price-weighted index, stocks with higher share prices have more influence, regardless of company size. The index value is calculated by adding up all the share prices and dividing by a divisor.

```
PRICE-WEIGHTED INDEX EXAMPLE
==============================

Stock       Price      Weight in Index
-----       -----      ---------------
Stock A     $300       300/600 = 50.0%
Stock B     $200       200/600 = 33.3%
Stock C     $100       100/600 = 16.7%
                       ---------
Total       $600       100.0%

Index Value = Sum of Prices / Divisor
            = $600 / Divisor

Key Problem: Stock A has 3x the influence of Stock C,
even if Stock C is a much LARGER company by market cap.

If Stock A rises 1%: Index moves ~0.50%
If Stock C rises 1%: Index moves ~0.17%
```

The Dow Jones Industrial Average is the most famous price-weighted index. This is why a $5 move in a $300 stock (1.7%) affects the Dow more than a $5 move in a $50 stock (10%), even though the percentage move in the cheaper stock is much larger. This makes price-weighted indexes somewhat arbitrary, since a company's share price is largely a cosmetic choice -- a stock trading at $300 could just as easily trade at $150 if the company did a 2-for-1 stock split.

**Market-Capitalization-Weighted Index**

In a cap-weighted index, stocks are weighted by their total market value (share price times shares outstanding). Larger companies have more influence. This is the most common methodology worldwide.

```
MARKET-CAP-WEIGHTED INDEX EXAMPLE
====================================

Stock       Price     Shares Out    Market Cap       Weight
-----       -----     ----------    ----------       ------
Stock A     $300      1 billion     $300 billion     50.0%
Stock B     $200      500 million   $100 billion     16.7%
Stock C     $100      2 billion     $200 billion     33.3%
                                    ------------     ------
                                    $600 billion     100.0%

Now Stock A is the largest COMPANY and gets the most weight.
Stock C is second, despite having the lowest PRICE.

Notice: Stock C went from 16.7% (price-weighted) to 33.3%
(cap-weighted) because it has a large market cap despite
its lower share price.
```

The S&P 500, NASDAQ Composite, and most international indexes use cap-weighting. It has a natural logic -- larger companies represent more economic activity, so they should have more influence. However, it also means a small number of mega-cap stocks can dominate the index. In recent years, the top 10 stocks in the S&P 500 have sometimes accounted for over 30% of the entire index's weight.

```
CONCENTRATION RISK IN CAP-WEIGHTED INDEXES
=============================================

S&P 500 Weight Distribution (Illustrative):

Top 10 stocks:    ~30-35%  ||||||||||||||||
Next 40 stocks:   ~25-30%  ||||||||||||||
Next 50 stocks:   ~15-18%  ||||||||
Next 100 stocks:  ~12-15%  ||||||
Bottom 300:       ~8-10%   ||||

The "500" in S&P 500 is somewhat misleading.
The index behaves more like a portfolio of
50-100 stocks with 400 small positions.
```

**Equal-Weighted Index**

In an equal-weighted index, every stock gets the same weight, regardless of price or market cap. A $10 billion company has the same influence as a $1 trillion company.

```
EQUAL-WEIGHTED INDEX EXAMPLE
===============================

Stock       Price     Market Cap       Weight
-----       -----     ----------       ------
Stock A     $300      $300 billion     33.3%
Stock B     $200      $100 billion     33.3%
Stock C     $100      $200 billion     33.3%
                                       ------
                                       100.0%

Every stock contributes equally to returns.

If all three rise 10%: Index rises 10%
(same as cap-weighted and price-weighted)

If only Stock C rises 10%:
Equal-weighted:  +3.33%  (10% x 33.3%)
Cap-weighted:    +3.33%  (10% x 33.3%)  <-- coincidence here
Price-weighted:  +1.67%  (10% x 16.7%)

But if only Stock B rises 10%:
Equal-weighted:  +3.33%  (10% x 33.3%)
Cap-weighted:    +1.67%  (10% x 16.7%)
Price-weighted:  +3.33%  (10% x 33.3%)
```

Equal-weighting gives more influence to smaller companies compared to cap-weighting. Historically, equal-weighted versions of the S&P 500 have outperformed the cap-weighted version over long periods, largely because they have greater exposure to the "size" and "value" factors. However, equal-weighted indexes require frequent rebalancing (selling winners, buying losers), which generates higher transaction costs and potential tax consequences.

---

#### 3. Comparing the Three Methods Side by Side

```
WEIGHTING METHOD COMPARISON
=============================

Feature             Price-Wt     Cap-Wt       Equal-Wt
-------             --------     ------       --------
Driver of weight    Share price  Market cap   None (fixed)
Largest stock       Highest      Biggest      Same as
influence           priced       company      smallest

Bias toward         High-price   Large-cap    Small/mid-cap
                    stocks       stocks       stocks

Rebalancing need    Minimal      Minimal      Frequent
Turnover            Low          Low          High
Concentration risk  Arbitrary    High         Low

Famous example      Dow Jones    S&P 500      S&P 500
                    (DJIA)       NASDAQ       Equal Weight
                                 Russell      (RSP)

Historical return   Moderate     Moderate     Higher
(long-term)                                   (with caveats)
```

---

#### 4. Major U.S. Indexes in Detail

**The Dow Jones Industrial Average (DJIA)**

```
DOW JONES INDUSTRIAL AVERAGE
==============================

Established:     1896 (one of the oldest indexes)
Components:      30 large-cap U.S. stocks
Weighting:       Price-weighted
Selection:       Chosen by a committee at S&P Dow Jones
                 Indices (subjective, not formula-based)
Divisor:         Adjusted for stock splits and changes
                 (the "Dow Divisor" is published daily)

Strengths:
- Long history, cultural significance
- Blue-chip companies, household names
- Simple to understand conceptually

Weaknesses:
- Only 30 stocks -- very narrow
- Price-weighting is arbitrary
- Committee-selected, not rules-based
- No small or mid-cap exposure
- A stock split changes its index influence

Current Dow Divisor:
When the Dow was created, the divisor was 30 (the number
of stocks). Due to decades of splits and substitutions,
the divisor is now a fraction less than 1. This means a
$1 move in ANY Dow stock moves the index by more than
1 point.
```

**The S&P 500**

```
S&P 500
========

Established:     1957 (with back-calculated data to 1928)
Components:      ~500 large-cap U.S. stocks
Weighting:       Float-adjusted market-cap-weighted
Selection:       Committee-selected based on criteria:
                 - U.S. company
                 - Market cap >= ~$14.5 billion (as of 2024)
                 - Positive earnings (most recent quarter
                   and sum of last four quarters)
                 - Adequate liquidity
                 - Public float >= 50%

"Float-adjusted" means:
Only shares available for public trading are counted.
Shares held by insiders, governments, or other companies
are excluded from the weight calculation.

Why it matters:
A company with 1 billion shares outstanding but 400
million held by the founder has a float of 600 million.
The index uses 600M x price, not 1B x price.

Strengths:
- Broad representation of U.S. large-cap market
- The single most-tracked benchmark globally
- Trillions of dollars indexed to it
- Float-adjustment reflects investable reality

Weaknesses:
- Committee subjectivity in additions/deletions
- Earnings requirement excludes some large companies
- Cap-weighting leads to concentration
- Only large-cap; excludes mid, small, micro-cap
```

**The NASDAQ Composite and NASDAQ-100**

```
NASDAQ COMPOSITE vs. NASDAQ-100
==================================

                    NASDAQ Composite       NASDAQ-100
                    ----------------       ----------
Components          ~3,000+ stocks         100 stocks
Exchange            All NASDAQ-listed      Largest non-financial
                                           NASDAQ-listed
Weighting           Cap-weighted           Modified cap-weighted
Financial cos.      Included               Excluded
Technology bias     Significant            Very significant

The NASDAQ-100 (tracked by QQQ ETF) is heavily tilted
toward technology. The top 10 holdings often represent
50%+ of the index.

NASDAQ-100 SECTOR BREAKDOWN (Illustrative):
+--------------------------------------------+
| Technology         ~50-55%  |||||||||||||||  |
| Comm. Services     ~15-18%  |||||           |
| Consumer Disc.     ~12-15%  ||||            |
| Healthcare         ~6-8%    ||              |
| Other              ~5-10%   ||              |
+--------------------------------------------+

Important: NASDAQ does NOT mean "tech index."
It is an exchange. Many non-tech companies list
on NASDAQ. But the cap-weighting and concentration
of large tech firms create a de facto tech tilt.
```

**The Russell Indexes**

```
RUSSELL INDEX FAMILY
======================

Russell 3000: Broadest U.S. index (~3,000 stocks)
              Covers ~98% of U.S. investable equity
              |
              +-- Russell 1000: Top 1,000 by market cap
              |   (large + mid cap, ~93% of market)
              |   |
              |   +-- Russell 1000 Growth
              |   +-- Russell 1000 Value
              |
              +-- Russell 2000: Next 2,000 by market cap
                  (small cap, ~7% of market)
                  |
                  +-- Russell 2000 Growth
                  +-- Russell 2000 Value

KEY DIFFERENCES from S&P indexes:
- Rules-based selection (no committee)
- Annual reconstitution on one day (late June)
- Clear market-cap breakpoints
- Growth/Value split based on quantitative factors

The Russell 2000 is THE benchmark for small-cap stocks.
If you invest in small-cap funds, their performance
is measured against the Russell 2000.
```

---

#### 5. How Indexes Are Maintained: Rebalancing and Reconstitution

Indexes are not static. They must be updated to reflect changes in the market. This maintenance happens through two distinct processes:

```
REBALANCING vs. RECONSTITUTION
=================================

REBALANCING:
- Adjusting the weights of EXISTING members
- Happens quarterly for most cap-weighted indexes
- For equal-weighted: selling winners, buying losers
  to restore equal weights
- Minimal impact on stock prices

RECONSTITUTION:
- Adding and removing members entirely
- Happens on a schedule (annually for Russell,
  quarterly review for S&P 500)
- Can cause LARGE price impacts
- Creates forced buying (additions) and forced
  selling (deletions) by index funds

Timeline example (S&P 500):
+--------+----------+----------+---------+
|Announce|  Market   |Effective |  Actual |
| Date   | Reacts    |  Date    | Trading |
+--------+----------+----------+---------+
  Day 0     Day 0-5    Day 5-10   Day 10
  |         |          |          |
  Index     Traders    More       Index
  announces front-run  buying/    funds
  change    the change selling    execute
```

---

#### 6. Index Flow Effects: Why Additions and Deletions Move Prices

When a stock is added to a major index like the S&P 500, every index fund tracking that benchmark must buy shares. This creates enormous demand. Conversely, when a stock is deleted, index funds must sell.

```
THE INDEX ADDITION EFFECT
============================

Announcement: "Company XYZ added to S&P 500"

What happens next:

1. ACTIVE TRADERS (Day 0-1):
   Front-run the forced buying
   Stock price jumps 2-4%

2. INDEX FUNDS (Day 1-5):
   Begin accumulating shares
   Continued upward pressure

3. EFFECTIVE DATE:
   All index funds must own the stock
   Final burst of buying at close

4. POST-ADDITION (Days 5-30):
   Price may partially revert as
   front-runners sell

TYPICAL PRICE PATTERN:

Price
  |         _____
  |        /     \______ (new equilibrium)
  |       /
  |      /
  |_____/
  |
  +-----|------|------|----- Time
     Announce  Eff.   +30d
               Date

Average excess return around S&P 500 addition:
+3% to +7% (varies by study and time period)
Average excess return around deletion:
-3% to -10% (deletions often hurt more)
```

This effect matters because it represents a real cost to index fund investors. The stocks they must buy are more expensive (because others front-run the purchase), and the stocks they must sell are cheaper (because others front-run the sale). This is sometimes called the "index inclusion tax."

---

#### 7. Float Adjustment and Its Consequences

Most modern cap-weighted indexes use "float-adjusted" market caps rather than total market caps.

```
FLOAT ADJUSTMENT EXPLAINED
=============================

Total Shares Outstanding:     1,000,000,000
Less:
  Founder/Insider holdings:   -200,000,000
  Government holdings:        -100,000,000
  Strategic investors:         -50,000,000
  Restricted shares:           -50,000,000
                              -------------
Free Float Shares:             600,000,000

Total Market Cap:    1B shares x $100 = $100 billion
Float Market Cap:    600M shares x $100 = $60 billion

Index weight based on $60B, not $100B.

WHY THIS MATTERS:
- Companies with large insider ownership get less
  index weight than their total value suggests
- When insiders sell (increasing float), the stock's
  index weight increases, forcing more index buying
- IPO lockup expirations increase float, changing
  index dynamics
```

---

#### 8. Global Indexes

Investing internationally requires familiarity with major global indexes and the index providers that create them.

```
MAJOR GLOBAL INDEXES
======================

AMERICAS:
  S&P 500 (U.S.)              500 large-cap U.S.
  S&P/TSX Composite (Canada)  ~230 Canadian stocks
  Bovespa (Brazil)             ~80 Brazilian stocks

EUROPE:
  FTSE 100 (UK)               100 largest on London SE
  DAX 40 (Germany)             40 largest on Frankfurt
  CAC 40 (France)              40 largest on Euronext Paris
  Euro Stoxx 50 (Eurozone)     50 largest eurozone stocks
  STOXX Europe 600             600 stocks across 17 countries

ASIA-PACIFIC:
  Nikkei 225 (Japan)           225 stocks, PRICE-WEIGHTED
  TOPIX (Japan)                ~2,000 stocks, cap-weighted
  Hang Seng (Hong Kong)        ~80 stocks
  SSE Composite (China)        All Shanghai-listed stocks
  S&P/ASX 200 (Australia)      200 Australian stocks
  KOSPI (South Korea)          All stocks on Korea Exchange

Note: Nikkei 225 is price-weighted, like the Dow.
TOPIX is cap-weighted and is the more representative
measure of the Japanese equity market.
```

**Global Index Providers**

```
THE BIG THREE INDEX PROVIDERS
================================

1. S&P Dow Jones Indices
   - S&P 500, S&P MidCap 400, S&P SmallCap 600
   - S&P Global 1200, S&P Developed, S&P Emerging
   - Dow Jones Industrial Average

2. MSCI (Morgan Stanley Capital International)
   - MSCI World (23 developed markets)
   - MSCI ACWI (All Country World Index: 23 dev + 24 EM)
   - MSCI Emerging Markets (24 countries)
   - Used by most international ETFs and mutual funds

3. FTSE Russell
   - Russell 1000, Russell 2000, Russell 3000
   - FTSE 100, FTSE All-World
   - FTSE Global All Cap

MSCI WORLD vs. MSCI ACWI vs. MSCI EM:

    MSCI ACWI (All Country World Index)
    +-------------------------------------------------+
    |                                                 |
    |  MSCI World (Developed Markets)      ~88%       |
    |  +-----------------------------------------+    |
    |  |  U.S.            ~62%                   |    |
    |  |  Japan            ~6%                   |    |
    |  |  UK               ~4%                   |    |
    |  |  Other Developed  ~16%                  |    |
    |  +-----------------------------------------+    |
    |                                                 |
    |  MSCI Emerging Markets               ~12%       |
    |  +-----------------------------------------+    |
    |  |  China            ~3%                   |    |
    |  |  India            ~2%                   |    |
    |  |  Taiwan           ~2%                   |    |
    |  |  Other EM         ~5%                   |    |
    |  +-----------------------------------------+    |
    |                                                 |
    +-------------------------------------------------+

    Note: A "World" index (MSCI World, FTSE Developed)
    does NOT include emerging markets despite the name.
```

---

#### 9. Choosing the Right Benchmark for Your Portfolio

```
BENCHMARK SELECTION GUIDE
============================

Your Portfolio                  Appropriate Benchmark
--------------                  ---------------------
U.S. large-cap stocks           S&P 500 or Russell 1000
U.S. small-cap stocks           Russell 2000
U.S. total market               Russell 3000 or Wilshire 5000
International developed         MSCI EAFE or FTSE Developed ex-US
Emerging markets                MSCI EM or FTSE Emerging
Global all-cap                  MSCI ACWI or FTSE Global All Cap
U.S. growth stocks              Russell 1000 Growth
U.S. value stocks               Russell 1000 Value
60/40 balanced portfolio        60% S&P 500 / 40% Bloomberg Agg

COMMON MISTAKE:
Comparing a portfolio of small-cap value stocks
to the S&P 500. If small caps are out of favor,
you will look bad even if you are beating the
correct benchmark (Russell 2000 Value).

The benchmark should match:
1. Geographic exposure
2. Market-cap range
3. Style (growth vs. value)
4. Asset class (equity, fixed income, multi-asset)
```

---

#### 10. Practical Implications for Index Fund Investors

```
WHAT INDEX FUND INVESTORS SHOULD KNOW
========================================

1. YOU ARE MAKING ACTIVE CHOICES
   Choosing "the S&P 500" over "the total market" is an
   active decision to exclude mid-caps, small-caps, and
   micro-caps. Know what you own and what you do not.

2. CONCENTRATION RISK IS REAL
   Cap-weighted indexes become top-heavy over time. If
   the top 7 stocks fall 30% but everything else is flat,
   a cap-weighted S&P 500 fund can drop 10%+ while an
   equal-weighted fund barely moves.

3. EQUAL-WEIGHT HAS HIGHER COSTS
   The RSP (S&P 500 Equal Weight ETF) has an expense
   ratio of ~0.20% vs. ~0.03% for VOO (S&P 500 cap-
   weighted). It also has higher turnover and potential
   tax drag from frequent rebalancing.

4. THE INDEX PROVIDER MATTERS
   S&P uses committee selection. Russell uses rules.
   This creates different experiences around reconstitution
   events. Russell's annual reconstitution causes massive
   volume spikes in late June.

5. INTERNATIONAL INDEX CHOICE MATTERS
   MSCI and FTSE classify countries differently. South
   Korea is "emerging" in MSCI but "developed" in FTSE.
   If you mix ETFs from different providers, you may
   have unintended gaps or overlaps.
```

---

### c) Common Misconceptions

**Misconception 1: "The Dow Jones IS the market."**

Reality: The Dow tracks only 30 stocks using an outdated price-weighting methodology. It is a culturally significant but statistically poor representation of the U.S. market. The S&P 500 or Russell 3000 provides a much broader and more representative picture. The Dow persists in headlines primarily because of its 130-year history and name recognition, not because of its analytical superiority.

**Misconception 2: "A higher index value means a more expensive market."**

Reality: The index level itself tells you nothing about valuation. The S&P 500 at 5,000 is not "more expensive" than the S&P 500 at 2,000 -- it depends entirely on how much the underlying companies are earning. If earnings doubled while the index doubled, valuations have not changed at all. To assess whether the market is expensive, you need to look at valuation metrics like P/E ratios, not index levels.

**Misconception 3: "An S&P 500 index fund is fully diversified."**

Reality: The S&P 500 excludes mid-cap, small-cap, and international stocks. Even within its own universe, cap-weighting can create significant concentration. A total market fund (Russell 3000 or Wilshire 5000) combined with international exposure provides much broader diversification than the S&P 500 alone.

**Misconception 4: "All S&P 500 index funds are identical."**

Reality: While all S&P 500 funds track the same index, they differ in expense ratios, tracking error, securities lending revenue, tax efficiency, and the timing of reconstitution trades. These small differences compound over decades. The difference between a 0.03% expense ratio and a 0.15% expense ratio over 30 years on a $100,000 investment at 10% annual returns is approximately $22,000.

**Misconception 5: "Price-weighted and cap-weighted indexes produce similar returns."**

Reality: Over long periods, the difference between weighting methods can be substantial. Because the Dow is price-weighted and holds only 30 stocks, its returns frequently diverge from the S&P 500. In some years, the difference exceeds 5-10 percentage points. The weighting method is not a minor technicality -- it fundamentally determines the portfolio you own.

**Misconception 6: "When a stock is added to an index, it means the company is doing well."**

Reality: Addition to an index like the S&P 500 indicates that a company meets specific criteria (size, liquidity, profitability, domicile), not that it is a good investment. Some stocks are added near their peaks. Similarly, deletion does not necessarily mean the company is failing -- it might be due to a merger, privatization, or shift in index methodology.

---

### d) Q&A

**Q1: Why does the Dow still exist if it is such a flawed index?**

A: Inertia, brand recognition, and a 130-year track record. The Dow was one of the first stock market indexes, and its daily movements have been reported in newspapers since the late 1800s. Despite its flaws, it has enormous cultural significance. Financial media continue to report it because audiences recognize it. Additionally, it does capture the general direction of the market most of the time -- it just does so with unnecessary distortions from price-weighting and its narrow 30-stock composition.

**Q2: What happens to the Dow divisor when a stock splits?**

A: When a Dow component does a stock split, the divisor is adjusted downward so that the index level does not change purely due to the split. For example, if a $300 stock does a 3-for-1 split, its price drops to $100. Without adjusting the divisor, the Dow would plunge even though no actual value was destroyed. The divisor is recalculated so the index value stays continuous. This is why the Dow divisor today is a small fraction (less than 1) rather than the original value of 30. Decades of splits and constituent changes have compounded these adjustments.

**Q3: How does a stock get added to the S&P 500?**

A: A committee at S&P Dow Jones Indices selects stocks based on several criteria: U.S. domicile, market capitalization above approximately $14.5 billion, positive earnings in the most recent quarter and over the trailing four quarters, adequate trading liquidity, and at least 50% public float. Meeting these criteria does not guarantee inclusion -- the committee uses judgment about sector representation and other qualitative factors. This subjectivity is both a strength (the committee can exclude companies with questionable earnings quality) and a weakness (it introduces human bias).

**Q4: What is the "Russell Reconstitution" and why does it matter?**

A: Every year in late June, FTSE Russell reconstitutes the Russell indexes based on market capitalizations measured on a specific "rank day" in May. Companies that have grown may move from the Russell 2000 (small-cap) to the Russell 1000 (large-cap), and vice versa. Because this happens on a single day with fixed rules, the trading volume on reconstitution day is astronomical -- often 2-3 times normal volume. Index funds must buy all new additions and sell all deletions at the close on that day. This creates predictable trading patterns that hedge funds actively exploit.

**Q5: Should I invest in an equal-weighted index fund instead of a cap-weighted one?**

A: It depends on your goals. Equal-weighted funds historically have slightly outperformed cap-weighted funds over very long periods due to their tilt toward smaller companies and their systematic rebalancing (selling high, buying low). However, they come with higher expense ratios, higher turnover, greater tax drag, and periods of significant underperformance -- particularly when mega-cap stocks are leading the market. For most investors, a cap-weighted total market fund at very low cost is the simplest and most tax-efficient choice. If you want small-cap exposure, adding a dedicated small-cap fund to a cap-weighted core may be more efficient than using equal-weighting.

**Q6: What does "float-adjusted" mean and why should I care?**

A: Float adjustment excludes shares that are not available for public trading -- insider holdings, government stakes, strategic cross-holdings, and restricted shares. Only freely tradable shares count toward the index weight. This matters because it aligns the index with investable reality. If a company has a $100 billion total market cap but half the shares are locked up by insiders, only $50 billion worth of stock can actually be bought by investors. Float adjustment prevents index funds from trying to buy shares that are not available.

**Q7: How do country classifications affect my international investments?**

A: MSCI and FTSE classify countries differently between "developed" and "emerging" markets. The most notable discrepancy is South Korea, which MSCI classifies as emerging but FTSE classifies as developed. If you use an MSCI-based developed markets ETF and an FTSE-based emerging markets ETF, you will have no exposure to South Korea at all. If you use both from the same provider, you will have the intended coverage. Always check which index provider your ETFs use.

**Q8: Can I use index movements to time the market?**

A: Index levels and short-term movements are very poor timing signals. Indexes hitting all-time highs is normal in a long-term upward trend -- the market spends a surprisingly large percentage of time near all-time highs. Trying to time entries and exits based on index levels typically leads to worse returns than simply staying invested. However, valuation measures derived from index data (like the Shiller CAPE ratio of the S&P 500) can provide useful context about long-term expected returns.

**Q9: What is a "total return" index versus a "price" index?**

A: A price index (like the commonly quoted S&P 500 level) only tracks the change in stock prices. A total return index also includes dividends reinvested. Over long periods, the difference is enormous. Including dividends, the S&P 500 has returned approximately 10% per year historically. Excluding dividends, the return is only about 7% per year. When evaluating your own performance, always compare against a total return benchmark. Most index funds aim to match the total return, not just the price return.

**Q10: Why do some ETFs track the same index but have different returns?**

A: Several factors cause tracking differences. Expense ratios are the most obvious -- a fund charging 0.10% will lag one charging 0.03% by 7 basis points. Securities lending revenue can offset some costs; large funds lend out shares to short sellers and earn income. Transaction costs from rebalancing and reconstitution trading affect returns. Cash drag occurs because funds hold a small cash buffer for redemptions, which slightly dilutes equity exposure. Sampling approaches (holding a representative subset rather than all 500 stocks) can cause both positive and negative tracking error. Over long periods, these small differences compound significantly.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 9: Understanding Market Indexes"]

**Alex:** Welcome back everyone. Today we are going to pull back the curtain on something you hear about every single day but probably do not fully understand -- market indexes. The Dow is up, the S&P is down, the NASDAQ hit a record. What do all these numbers actually mean, and why should you care?

**Sam:** Honestly, I have always just assumed they all measure the same thing -- you know, how the stock market is doing. Are they really that different?

**Alex:** They are very different, and understanding those differences is crucial. Let me ask you this -- if I told you "the Dow was up 1% today but the S&P 500 was down 0.5%," what would you think?

**Sam:** I would be confused. How can the market be up and down at the same time?

**Alex:** Exactly. And that confusion disappears once you understand what each index actually measures and how it is built. Think of indexes like recipes. The S&P 500 and the Dow share some of the same ingredients -- they both include Apple, Microsoft, and other big companies. But the recipes are different. Different quantities, different preparation methods, different results.

[VISUAL: Kitchen analogy showing two recipes side by side, same ingredients but different proportions, producing different dishes. Labels show "Dow Recipe: 30 ingredients, measure by price" and "S&P 500 Recipe: 500 ingredients, measure by size"]

**Sam:** So what is the recipe for an index? What are the key design choices?

**Alex:** Every index has three critical design decisions. First, which stocks to include -- the selection rules. Second, how much weight to give each stock -- the weighting method. And third, how and when to update the list -- the maintenance rules. Let us start with the weighting method because that is where the biggest differences lie.

[VISUAL: Three pillars labeled "Selection," "Weighting," and "Maintenance" supporting a platform labeled "Market Index"]

**Sam:** Okay, what are the different weighting methods?

**Alex:** There are three main ones: price-weighted, market-cap-weighted, and equal-weighted. Let me illustrate with a simple example. Imagine an index with just three stocks.

[ANIMATION: animation/week09_index_construction.py - Animated comparison of three weighting methods using three hypothetical stocks. The animation shows three columns, each representing a different weighting approach. Stock A has a high price but medium market cap, Stock B has a medium price and small market cap, and Stock C has a low price but large market cap. The bars dynamically resize as the user watches, showing how the same three stocks produce completely different portfolio weights depending on the method chosen. The animation then shows a simulated day where Stock C rises 10% and illustrates how the index return differs across all three methods.]

**Alex:** Stock A trades at $300 per share, Stock B at $200, and Stock C at $100. In a price-weighted index, like the Dow, Stock A dominates simply because it has the highest share price. It gets 50% of the weight.

**Sam:** Wait, so a stock gets more influence just because its price per share happens to be higher? That seems arbitrary.

**Alex:** It is arbitrary! And that is the fundamental flaw of price-weighting. A company's share price is largely a cosmetic choice. A $300 stock could easily be a $150 stock if the company did a 2-for-1 split. The company's actual value has not changed at all, but its influence in a price-weighted index just got cut in half.

**Sam:** So when a Dow stock splits, it immediately loses influence in the Dow?

**Alex:** Exactly. And the Dow has to adjust its divisor -- a special number it divides by -- to keep the index level from jumping around. The Dow divisor has been adjusted so many times over the decades that it is now less than 1. The original divisor was 30 -- just the number of stocks.

[VISUAL: Timeline showing the Dow divisor from 1928 (value of 30) to present (value less than 1), with major adjustments labeled for stock splits and constituent changes]

**Sam:** Okay, so price-weighting has problems. What about cap-weighting?

**Alex:** Market-cap weighting is what the S&P 500 and most modern indexes use. Instead of weighting by share price, you weight by total market value -- share price times the number of shares outstanding. So a trillion-dollar company gets ten times the weight of a hundred-billion-dollar company. This makes much more economic sense. The biggest companies should have the most influence because they represent the most economic activity.

**Sam:** That sounds more logical. Is there a downside?

**Alex:** The big downside is concentration. When a handful of companies get extremely large, they dominate the index. In recent years, the top 10 stocks in the S&P 500 have represented over 30% of the entire index. So when someone says "I own an S&P 500 index fund for diversification," they should realize that almost a third of their money is in just 10 companies.

[VISUAL: Pie chart of S&P 500 showing the top 10 stocks as a large wedge, with the remaining 490 stocks divided into progressively smaller segments. Animated transition showing how this concentration has grown over the past 20 years.]

**Sam:** That is surprising. I always thought of the S&P 500 as this perfectly diversified portfolio of 500 companies.

**Alex:** It is 500 companies, but it is not 500 equal positions. The bottom 300 stocks combined might make up less than 10% of the index. So really, the S&P 500 behaves more like a portfolio of 50 to 100 meaningful positions with 400 rounding errors.

**Sam:** Harsh but fair. What about equal-weighting?

**Alex:** Equal-weighting is exactly what it sounds like. Every stock gets the same weight, regardless of its price or its market cap. In a 500-stock index, each stock is 0.2% of the portfolio. A $10 billion company has the same influence as a $3 trillion company.

**Sam:** That seems more democratic. Does it perform better?

**Alex:** Historically, yes -- over very long periods, the equal-weighted S&P 500 has modestly outperformed the cap-weighted version. But there are two important caveats. First, equal-weighting requires constant rebalancing. Every quarter, you have to sell your winners and buy your losers to get back to equal weights. That generates transaction costs and tax consequences. Second, it does not always outperform. When mega-cap stocks are on a tear, the cap-weighted version wins handily.

[VISUAL: Performance chart comparing S&P 500 (cap-weighted) vs. S&P 500 Equal Weight (RSP) over 20 years, with shaded periods showing which method was winning during each phase]

**Sam:** So there is no perfect weighting method.

**Alex:** No, there is not. Each has trade-offs. Let me summarize with a quick comparison.

[VISUAL: Three-column comparison table showing Price-Weighted, Cap-Weighted, and Equal-Weighted side by side, with rows for: what drives weight, concentration risk, rebalancing needs, turnover, bias, and famous examples]

**Sam:** Got it. Now let us talk about the actual indexes. Can you walk me through the big ones? Starting with the Dow?

**Alex:** The Dow Jones Industrial Average was created in 1896. It tracks just 30 stocks and uses price-weighting. The stocks are hand-picked by a committee -- there is no formula for selection. It is one of the oldest and most recognized market indicators in the world, but from an analytical standpoint, it is probably the weakest of the major indexes.

**Sam:** If it is so flawed, why does everyone still talk about it?

**Alex:** Tradition and brand recognition. "The Dow was up 300 points" has been a headline for over a century. Financial media keep reporting it because audiences recognize it. And to be fair, over the very long term, the Dow roughly tracks the broader market because its 30 components are major companies that overlap significantly with the S&P 500. It just does so with more noise and distortion than necessary.

[VISUAL: Side-by-side chart of Dow Jones and S&P 500 over 50 years showing similar general trajectory but notable divergences in certain years, with percentage difference highlighted]

**Sam:** What about the S&P 500? That seems like the gold standard.

**Alex:** It is. The S&P 500 is the single most important benchmark in global finance. It covers about 500 large-cap U.S. stocks, representing roughly 80% of the total U.S. stock market value. It uses float-adjusted market-cap weighting, and its components are selected by a committee based on specific criteria -- size, profitability, liquidity, and public float.

**Sam:** What does float-adjusted mean?

**Alex:** Great question. Float adjustment means the index only counts shares that are actually available for public trading. If a company has a billion shares outstanding but the founder holds 300 million of them, only 700 million count toward the index weight. This makes sense because index funds cannot buy shares that are locked up by insiders. The weight should reflect what is actually investable.

[VISUAL: Diagram of a company's shares showing Total Shares Outstanding as a full circle, with insider holdings, government holdings, and restricted shares carved out, leaving the "free float" portion. An arrow shows this float being used for index weight calculation.]

**Sam:** And the NASDAQ?

**Alex:** You need to distinguish between the NASDAQ Composite and the NASDAQ-100. The NASDAQ Composite includes all 3,000-plus stocks listed on the NASDAQ exchange. The NASDAQ-100, which is what the famous QQQ ETF tracks, includes only the 100 largest non-financial companies on the exchange. Because so many large technology companies are listed on NASDAQ, the NASDAQ-100 has a very heavy technology tilt -- often 50% or more of its weight is in tech stocks.

**Sam:** So when people say "the NASDAQ was up 2%," they are basically saying tech stocks did well?

**Alex:** Usually, yes. Although technically the NASDAQ is an exchange, not a sector index, the concentration of tech mega-caps makes it behave like one. That is important to understand -- if you own a NASDAQ-100 ETF and also hold individual tech stocks, you may be much more concentrated in technology than you realize.

[VISUAL: NASDAQ-100 sector breakdown as a stacked bar chart, with technology dominating. A second bar shows a hypothetical portfolio combining QQQ with individual tech stocks, revealing extreme sector concentration.]

**Sam:** Now, what about the Russell indexes? I hear about the Russell 2000 a lot.

**Alex:** The Russell family is unique because it is entirely rules-based -- no committee picks and chooses. The Russell 3000 is the broadest U.S. index, covering about 98% of the investable U.S. equity market. It splits into the Russell 1000 for the top thousand stocks by market cap and the Russell 2000 for the next two thousand. The Russell 2000 is THE benchmark for small-cap stocks.

**Sam:** What is special about how Russell updates its indexes?

**Alex:** The Russell indexes reconstitute once per year, in late June, based on market caps measured on a specific "rank day" in May. This is a massive event. Every stock that has grown enough crosses from the Russell 2000 to the Russell 1000, and every stock that has shrunk moves the other direction. Because this all happens on a single day with completely predictable rules, the trading volume is extraordinary.

[ANIMATION: animation/week09_index_construction.py - Animated calendar showing the Russell reconstitution timeline: rank day in May, preliminary lists published in June, final reconstitution at market close on the last Friday of June. Volume bars show the massive spike in trading on reconstitution day, with the dollar value of forced index fund trades labeled. Stocks are shown visually migrating from one index to another as size thresholds are crossed.]

**Sam:** How big is the volume spike?

**Alex:** On Russell reconstitution day, trading volume can be two to three times normal levels. Billions of dollars of forced buying and selling occur as index funds adjust. This creates predictable price patterns that hedge funds actively exploit. Small-cap stocks being promoted to the Russell 1000 often see price increases in the weeks leading up to reconstitution as traders front-run the forced buying.

**Sam:** That seems like a disadvantage for index fund investors.

**Alex:** It is, and it is called the "index inclusion tax." When index funds must buy a newly added stock, they are buying from traders who already bought at a lower price in anticipation. And when they must sell a deleted stock, they are selling to traders who will buy at a lower price. The index fund is systematically on the wrong side of these predictable trades. The cost is estimated at 20 to 80 basis points per year for some small-cap index funds.

[VISUAL: Price chart of a stock being added to the S&P 500 showing the announcement date, the run-up in price as traders front-run, the effective date spike, and the partial reversion afterward. Key price levels and the cost to index fund investors are labeled.]

**Sam:** Is there any way to reduce that cost?

**Alex:** Some fund managers use patient trading strategies, spreading their reconstitution trades over several days instead of executing everything at the close on the effective date. Others use "reconstitution-aware" indexing that anticipates changes and trades gradually. Vanguard, for example, is known for being thoughtful about minimizing these costs.

**Sam:** Let us talk about global indexes for a minute. If I want to invest internationally, what do I need to know?

**Alex:** The two dominant providers for international indexes are MSCI and FTSE. MSCI World covers 23 developed markets. MSCI Emerging Markets covers 24 emerging market countries. MSCI ACWI combines both. FTSE has similar products. One important gotcha -- an index labeled "World" typically means developed markets only, which can be confusing.

**Sam:** So MSCI World does not include the whole world?

**Alex:** Correct. MSCI World excludes emerging markets. If you want true global coverage, you need MSCI ACWI -- All Country World Index -- which combines developed and emerging markets. Or you need to combine a developed markets fund with a separate emerging markets fund.

[VISUAL: Nested box diagram showing MSCI ACWI as the outer box containing MSCI World (developed) and MSCI Emerging Markets. Country flags are placed in each box with approximate weights. A callout points to South Korea, which appears in MSCI EM but FTSE Developed.]

**Sam:** You mentioned something about South Korea and a classification discrepancy?

**Alex:** Yes, this is a real-world gotcha. MSCI classifies South Korea as an emerging market. FTSE classifies it as a developed market. If you buy, say, an MSCI-based developed markets ETF and pair it with an FTSE-based emerging markets ETF, you will have zero exposure to South Korea -- it falls through the cracks. Always check that your international ETFs use the same index provider, or at least verify that you are not creating unintended gaps.

**Sam:** That is something I never would have thought to check.

**Alex:** It is the kind of detail that only matters until you realize your portfolio has been underweight one of the largest economies in Asia for years. The fix is simple -- just use ETFs from the same provider family.

**Sam:** Okay, let us talk about choosing benchmarks. How do I know which index to compare my portfolio against?

**Alex:** The benchmark should match your portfolio across four dimensions: geography, market cap, style, and asset class. If you own U.S. large-cap stocks, benchmark against the S&P 500 or Russell 1000. If you own U.S. small-cap stocks, use the Russell 2000. If you own international developed markets, use MSCI EAFE or FTSE Developed ex-US.

**Sam:** What happens if you pick the wrong benchmark?

**Alex:** You get a distorted picture of your performance. Imagine you built a portfolio of small-cap value stocks in a year when large-cap growth stocks dominated the market. Against the S&P 500, you might look terrible -- maybe you returned 8% while the S&P returned 25%. But against the Russell 2000 Value, which returned 5%, you actually outperformed by 3 percentage points. The right benchmark reveals your actual skill; the wrong benchmark creates an illusion in either direction.

[VISUAL: Bar chart showing the same portfolio return (8%) compared against three different benchmarks -- S&P 500 (25%), Russell 2000 (10%), and Russell 2000 Value (5%) -- showing how the portfolio looks bad, okay, or great depending on benchmark choice]

**Sam:** So benchmark selection is not just an academic exercise -- it actually changes how you evaluate yourself.

**Alex:** Exactly. And it changes your behavior. If you benchmark against the wrong index and feel like you are underperforming, you might abandon a perfectly good strategy out of frustration. That is one of the most expensive mistakes an investor can make.

**Sam:** Let me ask about something practical. When I buy an S&P 500 index fund, am I really getting the same returns as the S&P 500?

**Alex:** Very close, but not identical. The fund has an expense ratio -- the annual fee -- that drags on returns. Even at 0.03%, which is what the cheapest S&P 500 funds charge, that is money you do not get. Beyond that, there is tracking error from cash drag -- the fund holds a tiny bit of cash for redemptions. There is also the reconstitution cost we discussed. And there is the timing of reconstitution trades -- the fund may not execute at exactly the same prices the index calculation assumes.

**Sam:** How much do all those factors add up to?

**Alex:** For the best S&P 500 funds, total tracking difference is often less than 5 basis points -- so $50 per $100,000 invested per year. For less efficient funds or more exotic indexes, it can be much larger. This is why comparing expense ratios alone is not sufficient. You should also look at the fund's tracking difference -- the gap between the fund's actual return and the index's return -- over multiple years.

[VISUAL: Chart showing the cumulative cost of tracking difference over 30 years for three hypothetical funds tracking the same index: Fund A (0.03% tracking difference), Fund B (0.10%), and Fund C (0.25%). The compounding effect over decades turns small differences into meaningful dollar amounts.]

**Sam:** One more question -- what is the difference between a price index and a total return index?

**Alex:** This is critical and most people do not realize it. The S&P 500 level you see quoted on the news -- 5,000, 5,200, whatever -- is the price index. It only tracks stock price changes. But stocks also pay dividends. The total return index reinvests those dividends, and over long periods, the difference is enormous. Historically, dividends have contributed about 2 to 3 percentage points of annual return. Over 30 years, reinvested dividends can account for more than half of your total wealth accumulation.

**Sam:** So when I compare my portfolio return to "the S&P 500," I should make sure I am comparing to the total return version?

**Alex:** Absolutely. If your index fund returned 10% and you compare it to the price-only S&P 500 return of 7.5%, you might think you crushed the index. But really, you just matched it -- the difference was dividends. Always benchmark against total return.

[VISUAL: Two line charts growing from the same starting point -- one labeled "S&P 500 Price Return" and one labeled "S&P 500 Total Return (with dividends)." The gap between them widens dramatically over 30 years, with the total return line ending roughly 2x higher.]

**Sam:** That gap is striking. All right, let us do our summary. Give me the key takeaways from today.

**Alex:** Three things to remember. First, the weighting method is the single most important design choice in an index. Price-weighted, cap-weighted, and equal-weighted produce meaningfully different portfolios and returns from the same set of stocks. Know what method your index fund uses and understand its biases.

**Sam:** Second?

**Alex:** Cap-weighted indexes, which are by far the most popular, have an inherent concentration risk. A small number of mega-cap stocks can dominate the index. That is not necessarily bad, but you should own that risk consciously, not by accident.

**Sam:** And third?

**Alex:** Index reconstitution and rebalancing create predictable trading patterns that impose costs on index fund investors. These costs are generally small for large-cap indexes like the S&P 500 but can be meaningful for small-cap indexes. Understanding these mechanics helps you choose better funds and set more realistic return expectations.

[VISUAL: Summary card with three key takeaways. A preview graphic for next week's lesson on economic cycles shows a sine wave with labels for expansion, peak, contraction, and trough.]

**Sam:** This was really eye-opening. I never realized there was so much going on under the hood of something as simple as an index fund.

**Alex:** That is the thing -- index funds are simple to own but not simple in their construction. The more you understand the machinery, the better decisions you will make. Next week, we are diving into economic cycles -- how the economy moves through expansion, peak, contraction, and trough, and what that means for your portfolio. See you then.

**Sam:** Can not wait. Thanks everyone for watching!

[VISUAL: End screen with subscribe button and links to previous lessons]

---
