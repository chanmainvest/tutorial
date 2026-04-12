<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 20: Earnings and Cash Flow - Quality, Manipulation, and Free Cash Flow

---

## Reading Section

### a) Why This Is Important

Earnings are the single most important number in investing. Stock prices ultimately follow earnings over time. But here is the uncomfortable truth that every investor must confront: earnings are an opinion, while cash flow is a fact.

When a company reports "earnings per share of $3.50," that number is the product of dozens of accounting judgments, estimates, and choices. How fast to depreciate assets, when to recognize revenue, how much to reserve for bad debts, whether to capitalize or expense a cost -- every one of these decisions affects reported earnings. Some of these choices are legitimate reflections of economic reality. Others are deliberate manipulation designed to make the company look more profitable than it is.

The difference between a good investor and a great investor often comes down to this skill: the ability to look beyond reported earnings and assess their quality. Is the company truly generating the profits it claims? Are those profits backed by actual cash flowing into the business? Or is the company using accounting tricks to inflate a number that will eventually be revealed as a mirage?

This matters for critical reasons:

1. **Earnings manipulation precedes most spectacular corporate failures.** Enron, WorldCom, Luckin Coffee, Wirecard -- every major corporate fraud involved earnings manipulation that, in hindsight, was detectable from publicly available financial statements. Investors who understood earnings quality avoided these disasters.

2. **The gap between earnings and cash flow reveals management quality.** Companies whose cash flow consistently exceeds reported earnings tend to have conservative, trustworthy management. Companies whose earnings consistently outpace cash flow are either genuinely investing heavily for growth or are playing accounting games. Distinguishing between these two scenarios is essential.

3. **Free cash flow, not earnings, determines intrinsic value.** The DCF model we learned in Week 21 discounts free cash flow, not accounting earnings. A company can report growing earnings while free cash flow deteriorates -- that company is becoming less valuable, not more, regardless of what the income statement says.

4. **Earnings quality predicts future stock returns.** Academic research by Sloan (1996) and others has consistently shown that companies with high-quality earnings (backed by cash flow) outperform those with low-quality earnings (driven by accruals) by several percentage points per year. This is one of the most robust anomalies in finance.

This lesson gives you the complete toolkit to evaluate earnings quality, understand the difference between accrual and cash-based accounting, calculate and interpret free cash flow, identify manipulation red flags, and use FCF yield as a valuation metric.

---

### b) What You Need to Know

#### 1. Earnings Per Share (EPS) -- The Basics

EPS is the most widely cited earnings metric. It represents the profit attributable to each share of common stock.

```
EPS FUNDAMENTALS
==================

Basic EPS = Net Income / Weighted Average Shares Outstanding

Diluted EPS = Net Income / (Shares + Options + Convertibles)

Example:
  Net Income:           $500 million
  Shares Outstanding:   200 million
  Stock Options:         20 million (in the money)
  Convertible Bonds:     5 million equivalent shares

  Basic EPS  = $500M / 200M = $2.50
  Diluted EPS = $500M / 225M = $2.22

ALWAYS use diluted EPS for valuation. Basic EPS
overstates per-share earnings by ignoring future dilution.

EPS COMPONENTS -- THE INCOME STATEMENT PATH
=============================================

Revenue                             $1,000M
 - Cost of Goods Sold                ($600M)
= Gross Profit                        $400M  <-- Gross Margin: 40%
 - Operating Expenses                ($200M)
= Operating Income (EBIT)             $200M  <-- Operating Margin: 20%
 - Interest Expense                   ($30M)
= Pre-Tax Income                      $170M
 - Taxes (25%)                        ($42.5M)
= Net Income                          $127.5M  <-- Net Margin: 12.75%

EPS = $127.5M / 200M shares = $0.6375

EACH LINE INVOLVES ACCOUNTING JUDGMENTS
that can increase or decrease reported earnings.
```

**Earnings "Beats" and "Misses":**

```
THE EARNINGS EXPECTATIONS GAME
=================================

Wall Street analysts publish EPS estimates before
each quarterly report. The stock price reaction
depends on the result versus expectations:

  Result vs. Estimate       Typical Stock Reaction
  --------------------       ----------------------
  Beat by 10%+ ("blowout")  +5% to +15% (often gaps up)
  Beat by 1-5%              +1% to +5%
  In-line (meet)            -1% to +1% (sometimes sells off)
  Miss by 1-5%              -3% to -8%
  Miss by 10%+ ("disaster") -10% to -30%

IMPORTANT: Management teams actively manage
expectations. They "guide" analysts to set
estimates the company can beat. This is called
"managing the whisper number." An earnings
"beat" might simply mean management sandbagged
the guidance, not that business is booming.

THE MANIPULATION OF "BEATS"
=============================

Real-World Example:
  True earnings power:     $1.00/share
  Management guides:       $0.85 (conservatively)
  Analysts estimate:       $0.90
  Company reports:         $0.92
  
  Headlines: "Company BEATS estimates!"
  Reality: Company missed its actual potential
  by pulling forward expenses / deferring revenue
  to "save" earnings for future quarters.
```

---

#### 2. Accrual Accounting vs. Cash Accounting -- The Critical Difference

This is perhaps the most important concept in this entire lesson. The financial statements you read are based on accrual accounting, which recognizes revenues when earned and expenses when incurred, regardless of when cash changes hands. This creates a gap between reported earnings and actual cash flow.

```
ACCRUAL vs. CASH ACCOUNTING
==============================

ACCRUAL (what the income statement shows):
  Record revenue when EARNED (goods delivered, services rendered)
  Record expenses when INCURRED (obligation created)
  Timing of cash flow is IGNORED

CASH (what the cash flow statement shows):
  Record revenue when CASH IS RECEIVED
  Record expenses when CASH IS PAID
  Timing of economic activity is IGNORED

EXAMPLE: SOFTWARE COMPANY
============================

January: Signs 3-year, $3 million contract.
         Customer pays nothing upfront.

ACCRUAL ACCOUNTING (Income Statement):
  January revenue: $83,333 (1 month of 36-month contract)
  Q1 revenue: $250,000
  Year 1 revenue: $1,000,000

CASH ACCOUNTING (Cash Flow):
  January cash received: $0
  Q1 cash received: $0 (customer has not paid yet)
  Year 1 cash received: $1,000,000 (annual payment)

The income statement shows smooth, predictable revenue.
The cash flow statement shows lumpy, real money.

NEITHER IS "WRONG" -- they measure different things.
But cash is harder to fake.
```

**Why This Matters for Investors:**

```
THE ACCRUAL QUALITY SPECTRUM
==============================

HIGH QUALITY                                LOW QUALITY
(Cash > Earnings)                           (Earnings > Cash)
     |                                           |
     v                                           v
Revenue is received           Revenue is "earned" but cash
in cash before or             is not collected for months
at time of sale               or years (or ever)

Expenses are paid             Expenses are capitalized
when incurred                 (spread over future periods)
                              to boost current earnings

Depreciation reflects         Depreciation understated
real asset wear               to inflate earnings

Reserves are adequate         Reserves inadequate to
                              flatter current results

QUALITY INDICATOR:
                Net Income
Accrual Ratio = ─────────── - 1
                Operating CF

If ratio > 0: Earnings exceed cash flow (CAUTION)
If ratio < 0: Cash flow exceeds earnings (GOOD)
If ratio >> 0: Earnings far exceed cash flow (RED FLAG)
```

---

#### 3. Free Cash Flow -- The Most Important Number

Free cash flow (FCF) is the cash a company generates after accounting for capital expenditures needed to maintain and grow its asset base. It represents the cash truly available to shareholders -- for dividends, buybacks, debt reduction, or investment.

```
FREE CASH FLOW CALCULATION
=============================

Method 1 (from Cash Flow Statement):
  Operating Cash Flow
  - Capital Expenditures (Capex)
  = Free Cash Flow

Method 2 (from Income Statement):
  Net Income
  + Depreciation & Amortization
  + Other Non-Cash Charges
  - Changes in Working Capital
  - Capital Expenditures
  = Free Cash Flow

WORKED EXAMPLE
================

Company ABC -- Annual Financial Data:

Operating Cash Flow:         $350 million
Capital Expenditures:       ($120 million)
                            ─────────────
Free Cash Flow:              $230 million

Cross-Check from Income Statement:
Net Income:                  $200 million
+ Depreciation:              $100 million
+ Stock-Based Compensation:   $50 million
- Working Capital Increase:  ($80 million)
                              = Operating CF: $270 million
  Wait -- why does this not match?

Adjustments explanation:
  Operating CF per statement includes other items
  (deferred taxes, etc.) that bring it to $350M

INTERPRETATION
================

Net Income:     $200M
Operating CF:   $350M  <-- Cash generation EXCEEDS earnings (GOOD)
Free Cash Flow: $230M  <-- After maintaining assets, $230M is
                           truly "free" for shareholders

FCF > Net Income suggests HIGH QUALITY earnings.
Net Income > FCF suggests potential QUALITY CONCERNS.
```

**Maintenance Capex vs. Growth Capex:**

```
TYPES OF CAPITAL EXPENDITURE
===============================

MAINTENANCE CAPEX (Required)                GROWTH CAPEX (Optional)
---------------------------                 -----------------------
Replacing worn equipment                    Building new factories
Repairing facilities                        Entering new markets
Mandatory regulatory upgrades               R&D for new products
Keeping existing operations                 Capacity expansion
running at current capacity

If you only subtract maintenance capex,     Growth capex is an
you get "owner earnings" -- what             investment, not a
Buffett calls the true earning power         cost of doing business.
of the business.

PROBLEM: Companies do NOT separately report
maintenance vs. growth capex. You must estimate.

RULE OF THUMB:
  If capex roughly equals depreciation --> mostly maintenance
  If capex far exceeds depreciation --> significant growth investing
  If capex is below depreciation --> company may be underinvesting
                                     (consuming its asset base)

CAPEX ANALYSIS
================

                     Company X    Company Y
                     ---------    ---------
Depreciation:        $80M         $80M
Total Capex:         $85M         $200M
Capex/Depreciation:  1.06x        2.50x
Interpretation:      Maintenance  Heavy growth
                     mode         investment
```

---

#### 4. Quality of Earnings -- How to Spot the Real Thing

High-quality earnings are sustainable, repeatable, and backed by cash flow. Low-quality earnings are inflated by one-time items, aggressive accounting, or financial engineering.

```
EARNINGS QUALITY CHECKLIST
=============================

CHECK 1: Cash Flow Confirmation
  Operating Cash Flow / Net Income > 1.0?
  If consistently YES --> High quality
  If consistently NO  --> Investigate

CHECK 2: Accrual Level
  Large increase in accruals (receivables, inventory,
  deferred revenue changes) without corresponding
  revenue growth? --> WARNING

CHECK 3: Revenue Quality
  Is revenue growing from:
  [GOOD] More customers, higher prices, new products
  [BAD]  Channel stuffing, bill-and-hold, reclassifications

CHECK 4: Recurring vs. Non-Recurring
  What % of earnings comes from:
  [GOOD] Core operations, recurring sources
  [BAD]  Asset sales, lawsuit settlements, tax benefits,
         pension income, gain on investments

CHECK 5: Consistency
  Do earnings grow smoothly while the business is cyclical?
  Suspiciously smooth earnings often indicate manipulation.
  Real businesses have ups and downs.

CHECK 6: Margin Trajectory
  Are margins expanding due to:
  [GOOD] Scale, efficiency, pricing power
  [BAD]  Cutting R&D, reducing maintenance, one-time savings

QUALITY SCORECARD
===================

  High Quality                  Low Quality
  ============                  ===========
  OCF/NI > 1.0                 OCF/NI < 0.8
  Low accruals                  High accruals
  Recurring revenue             One-time gains
  Consistent with peers         Outlier margins
  Conservative estimates        Aggressive assumptions
  Clean audit opinion           Qualified audit opinion
  Management owns stock         Management sells stock
  Earnings match guidance       Frequent "beats" by $0.01
```

---

#### 5. Earnings Manipulation Red Flags

Companies manipulate earnings for many reasons: to meet analyst expectations, trigger management bonuses, maintain the stock price, or hide deteriorating fundamentals. Here are the techniques to watch for and how to detect them.

```
MANIPULATION TECHNIQUE 1: REVENUE MANIPULATION
=================================================

Technique               How It Works              Detection
---------               ------------              ---------
Channel Stuffing        Ship excess product to     Check: Receivables
                        distributors at quarter    growing faster than
                        end; they return it next   revenue? Returns
                        quarter                    increasing?

Bill-and-Hold           Record revenue for goods   Check: Inventory
                        that customer has not      remaining at company
                        actually taken delivery    facilities? Unusual
                        of yet                     revenue spikes at
                                                   quarter end?

Round-Tripping          Company A sells to         Check: Related party
                        Company B, Company B       transactions? Revenue
                        sells back to Company A    without economic
                                                   substance?

Early Recognition       Record multi-year          Check: Deferred
                        contract revenue upfront   revenue declining?
                        instead of over time       Revenue recognition
                                                   policy changes?

MANIPULATION TECHNIQUE 2: EXPENSE MANIPULATION
=================================================

Technique               How It Works              Detection
---------               ------------              ---------
Capitalizing            Record an operating        Check: Capitalized
Expenses                expense as an asset        costs growing?
                        (e.g., put marketing       Cash flow from
                        costs on balance sheet)    operations diverging
                                                   from earnings?

Under-Depreciating      Use unrealistically long   Check: Asset useful
                        useful life assumptions    lives longer than
                        for assets                 industry norms?
                                                   Compare depreciation
                                                   rates to peers

Cookie Jar              Take large reserves in     Check: Unusual
Reserves                good years, release them   reserve releases in
                        in bad years to smooth     weak quarters?
                        earnings                   Reserves declining
                                                   without explanation?

Pension                 Use aggressive return       Check: Pension
Assumptions             assumptions to reduce       return assumptions
                        pension expense            vs. actual returns?
                                                   Higher than peers?

MANIPULATION TECHNIQUE 3: BALANCE SHEET MANIPULATION
=====================================================

Technique               How It Works              Detection
---------               ------------              ---------
Off-Balance-Sheet       Move liabilities to        Check: Footnotes
Entities                special purpose entities   about unconsolidated
                        to hide debt               entities, guarantees,
                        (Enron's playbook)         or commitments

Goodwill                Avoid writing down          Check: Goodwill
Overstatement           impaired acquisition       as % of total
                        goodwill to prevent a      assets? Acquisitions
                        large earnings charge      underperforming?

Inventory               Understate obsolete        Check: Inventory
Manipulation            inventory to avoid         turnover declining?
                        write-downs                Days inventory
                                                   increasing?
```

```
THE MANIPULATION DETECTION FRAMEWORK
=======================================

Step 1: Compare Net Income to Operating Cash Flow
  +--------+--------+---------+--------+--------+
  | Year   |  Net   | Oper.   | FCF    | OCF/NI |
  |        | Income | Cash Fl.|        | Ratio  |
  +--------+--------+---------+--------+--------+
  | Year 1 | $100M  |  $130M  | $80M   | 1.30   | GOOD
  | Year 2 | $120M  |  $140M  | $90M   | 1.17   | GOOD
  | Year 3 | $150M  |  $125M  | $70M   | 0.83   | CONCERN
  | Year 4 | $180M  |  $100M  | $30M   | 0.56   | RED FLAG
  | Year 5 | $200M  |   $60M  |($20M)  | 0.30   | DANGER
  +--------+--------+---------+--------+--------+

  Earnings are growing 19%/year. Looks great!
  Cash flow is DECLINING. The earnings are a mirage.

Step 2: Check Balance Sheet Build-Up
  - Are receivables growing faster than revenue?
  - Is inventory growing faster than cost of goods sold?
  - Are accrued liabilities (reserves) being released?
  - Is capex being capitalized aggressively?

Step 3: Read the Footnotes
  - Revenue recognition policy changes?
  - Accounting estimate changes?
  - Related party transactions?
  - Off-balance-sheet commitments?

Step 4: Compare to Peers
  - Are margins out of line with peers?
  - Is the company an outlier on OCF/NI ratio?
  - Are accounting policies more aggressive?
```

---

#### 6. Free Cash Flow Yield -- A Powerful Valuation Metric

FCF yield is one of the most useful valuation metrics because it is based on cash (harder to manipulate) rather than earnings (easy to manipulate). It tells you what cash return you are getting for the price you pay.

```
FCF YIELD CALCULATION
=======================

                Free Cash Flow
FCF Yield = ─────────────────────
              Market Capitalization

Or equivalently:

                FCF Per Share
FCF Yield = ─────────────────────
              Stock Price

EXAMPLE:
  Free Cash Flow:     $500 million
  Market Cap:         $10 billion
  FCF Yield:          $500M / $10B = 5.0%

Interpretation: For every $100 invested, the company
generates $5 in free cash flow annually.

FCF YIELD BENCHMARKS
======================

FCF Yield     Interpretation          Notes
---------     ---------------         -----
< 0%          Negative FCF            Company is consuming
                                      cash (may be investing
                                      for growth or in trouble)

0 - 2%        Very low yield          Typical for high-growth
                                      companies reinvesting
                                      everything

2 - 4%        Below average           Growth company with
                                      some cash generation

4 - 6%        Average / Fair          Typical mature company;
                                      roughly in line with
                                      market average

6 - 8%        Above average           Potentially undervalued
                                      or slow-growth

8 - 12%       High yield              Either very undervalued
                                      or market sees risk

> 12%         Very high yield         Likely a value trap OR
                                      extraordinary opportunity;
                                      investigate deeply

COMPARISON: FCF YIELD vs. EARNINGS YIELD vs. DIVIDEND YIELD
==============================================================

                    FCF Yield    Earnings     Dividend
                                 Yield (1/PE) Yield
                    ---------    ----------   --------
Based on:           Cash flow    Accounting   Cash paid
                    (hard to     earnings     to share-
                    fake)        (can be      holders
                                 managed)

Captures:           All free     All net      Only the
                    cash for     income       portion
                    shareholders              paid out

Includes capex:     Yes          Partially    No
                                 (via deprec.)

Best for:           Absolute     Quick P/E    Income
                    valuation    comparison   investors

Manipulation        Low          Moderate     Very low
risk:                            to high
```

---

#### 7. Cash Flow Statement Analysis -- The Investor's X-Ray Machine

The cash flow statement is divided into three sections. Each tells a different story.

```
THE THREE SECTIONS OF THE CASH FLOW STATEMENT
================================================

+--------------------------------------------------+
|  OPERATING CASH FLOW (OCF)                       |
|  Cash generated from core business operations     |
|                                                   |
|  Healthy company: POSITIVE and growing            |
|  Starts with Net Income, adjusts for non-cash     |
|  items and working capital changes                |
+--------------------------------------------------+
              |
              | This is the "engine"
              v
+--------------------------------------------------+
|  INVESTING CASH FLOW (ICF)                       |
|  Cash spent on / received from investments        |
|                                                   |
|  Growing company: NEGATIVE (spending on growth)   |
|  Includes: capex, acquisitions, asset sales       |
+--------------------------------------------------+
              |
              | This is "reinvestment"
              v
+--------------------------------------------------+
|  FINANCING CASH FLOW (FCF_fin)                   |
|  Cash from / to capital providers                 |
|                                                   |
|  Mature company: NEGATIVE (returning cash)        |
|  Includes: debt issuance/repayment, dividends,    |
|  buybacks, equity issuance                        |
+--------------------------------------------------+

CASH FLOW PATTERN ANALYSIS
=============================

Pattern           Operating  Investing  Financing   Diagnosis
-------           ---------  ---------  ---------   ---------
Healthy mature      (+)        (-)        (-)       Using cash from
company                                             operations to invest
                                                    and return to holders

Growth company      (+)        (--)       (+)       Operations + new
                                                    capital fund heavy
                                                    investment

Startup / turnaround (-)       (-)        (+)       Burning cash; relying
                                                    on external funding

Cash cow            (+)        (small)    (--)      Returning most cash;
                                                    little reinvestment

Restructuring       (+)        (+)        (-)       Selling assets, paying
                                                    down debt

Distressed          (-)        (+)        (-)       Selling assets to pay
                                                    obligations; death spiral

IMPORTANT: Read the cash flow statement EVERY QUARTER.
It is the single most reliable financial statement.
Income statements involve judgment. Balance sheets
involve estimates. Cash flow statements count money.
```

---

#### 8. Putting It All Together -- The Earnings Quality Diagnostic

```
COMPLETE EARNINGS QUALITY DIAGNOSTIC
=======================================

STEP 1: THE 5-YEAR TREND TEST
---------------------------------

Plot these metrics over 5 years:

Revenue          Net Income       Operating CF       FCF
--------         ----------       ------------       ---
$500M            $50M             $70M               $40M
$550M            $60M             $80M               $50M
$600M            $75M             $95M               $60M
$650M            $85M             $105M              $65M
$700M            $100M            $120M              $75M

ALL growing together? GOOD QUALITY.

Now a problematic company:

Revenue          Net Income       Operating CF       FCF
--------         ----------       ------------       ---
$500M            $50M             $70M               $40M
$580M            $70M             $65M               $30M
$650M            $95M             $55M               $10M
$720M            $115M            $40M              ($15M)
$800M            $140M            $20M              ($50M)

Earnings growing but cash flow DECLINING = RED FLAG.
The earnings growth is an accounting illusion.

STEP 2: THE ACCRUAL RATIO
---------------------------------

                  (Net Income - Operating CF)
Accrual Ratio = ─────────────────────────────
                      Total Assets

Interpretation:
  < -10%:  Extremely high quality (rare, maybe one-time)
  -10% to -5%: Very high quality
  -5% to 0%:   Good quality
  0% to 5%:    Average quality
  5% to 10%:   Below average quality
  > 10%:       Poor quality / potential manipulation

STEP 3: THE BENEISH M-SCORE
---------------------------------

The M-Score is a mathematical model that uses 8
financial ratios to detect earnings manipulation.

M-Score > -1.78: HIGH probability of manipulation
M-Score < -1.78: LOW probability of manipulation

Key inputs include:
  - Days Sales in Receivables Index (DSRI)
  - Gross Margin Index (GMI)
  - Asset Quality Index (AQI)
  - Sales Growth Index (SGI)
  - Total Accruals to Total Assets (TATA)

Studies show the M-Score correctly identified
Enron's manipulation years before the collapse.

STEP 4: PEER COMPARISON
---------------------------------

Compare your company's ratios to industry peers:

                    Company    Industry    Verdict
                    -------    --------    -------
OCF/Net Income      0.7x       1.1x       POOR
Receivables Days    85         60          CONCERN
Inventory Days      120        90          CONCERN
Accrual Ratio       8%         -3%         RED FLAG
FCF Margin          2%         8%          POOR
Capex/Depreciation  0.8x       1.2x       Underinvesting

If the company is an outlier on multiple metrics,
investigate further before investing.
```

---

### c) Common Misconceptions

**Misconception 1: "EPS growth always means the business is growing."**

Reality: EPS can grow even when the underlying business is stagnant or declining. Share buybacks reduce the denominator (shares outstanding), mechanically increasing EPS without any improvement in net income. A company that earns the same $100 million year after year but buys back 5% of its shares annually will show 5% EPS growth. Check total net income and free cash flow growth, not just EPS.

**Misconception 2: "A company that beats earnings estimates is doing well."**

Reality: The earnings expectations game is heavily managed. Companies deliberately guide analysts to set beatable estimates. A company that "beats by a penny" every single quarter is almost certainly managing expectations, not outperforming. Look at the actual year-over-year earnings growth and cash flow trends, not the beat/miss versus artificially managed estimates.

**Misconception 3: "Revenue growth is always good."**

Reality: Revenue growth that comes with declining margins, increasing receivables, or negative free cash flow can actually destroy value. A company that grows revenue by 20% but offers increasingly generous credit terms (extending payments to customers who may not pay) is booking illusory revenue. Revenue quality matters as much as revenue quantity.

**Misconception 4: "Depreciation is just an accounting entry and can be ignored."**

Reality: Depreciation represents the consumption of real assets. A factory that depreciates $10 million per year will eventually need to be replaced or refurbished at a real cash cost. Ignoring depreciation overstates the cash available to shareholders. This is why free cash flow (which subtracts capex) is more reliable than EBITDA (which adds back depreciation) as a measure of true profitability.

**Misconception 5: "Negative free cash flow always means the company is in trouble."**

Reality: High-growth companies often have negative free cash flow because they are investing heavily in future growth -- building warehouses, developing software, expanding into new markets. Amazon had negative or minimal free cash flow for years while building its logistics empire. The key question is whether the investments will eventually generate returns above the cost of capital. Negative FCF from growth investment is very different from negative FCF due to a broken business model.

**Misconception 6: "The income statement is the most important financial statement."**

Reality: For investors, the cash flow statement is arguably more important because it is harder to manipulate and shows actual cash generation. Profitable companies can run out of cash and go bankrupt (if all their "profit" is locked in receivables or inventory). Unprofitable companies can thrive for years if they generate positive cash flow (through collecting cash before delivering services). Always cross-reference income statement claims with the cash flow statement.

---

### d) Common Questions and Answers

**Q1: Where do I find free cash flow? Is it on the financial statements?**

A: Free cash flow is not directly reported on any standard financial statement. You calculate it by taking Operating Cash Flow (from the cash flow statement) and subtracting Capital Expenditures (also on the cash flow statement, under "Investing Activities"). Many financial data providers like Yahoo Finance, Morningstar, and company investor relations pages calculate and display FCF, but always verify by doing the calculation yourself. Some providers include or exclude different items, so the numbers may not match exactly.

**Q2: How do I distinguish between legitimate growth investment and earnings manipulation?**

A: Ask three questions. First, is the company transparent about its investments? Legitimate growth investing comes with clear explanations of what is being built and expected returns. Second, are peers making similar investments? If the entire industry is expanding capacity, heavy capex is expected. Third, does management have a track record of generating returns on past investments? Check ROIC trends. Companies with a history of high ROIC are more likely to be genuinely investing for growth. Companies with low ROIC that keep spending heavily may be empire building.

**Q3: What is stock-based compensation and should I add it back to free cash flow?**

A: Stock-based compensation (SBC) is when companies pay employees with stock options or restricted stock units instead of cash. It appears as a non-cash expense on the income statement and is added back in the operating cash flow calculation. Some investors argue SBC should be added back to FCF because it is non-cash. Others (including Warren Buffett) argue it should be subtracted because it is a real cost that dilutes shareholders. The second view is correct. SBC is a real expense -- it transfers value from shareholders to employees. Always subtract SBC from FCF if the cash flow statement has added it back.

**Q4: What is the difference between EBITDA and free cash flow?**

A: EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) is a measure of operating profit before non-cash charges. Free cash flow is the actual cash available after all operating expenses AND capital expenditures. The main differences: (1) EBITDA ignores capex -- it assumes the business requires no reinvestment, which is rarely true. (2) EBITDA ignores working capital changes -- a company may report high EBITDA but consume cash through growing receivables and inventory. (3) EBITDA ignores taxes -- real businesses pay taxes in cash. FCF is a more complete and honest metric.

**Q5: How do I use the Beneish M-Score?**

A: The Beneish M-Score uses eight financial ratios to generate a score that indicates the likelihood of earnings manipulation. An M-Score greater than -1.78 suggests a high probability of manipulation. You can calculate it manually using data from the financial statements, but many financial analysis platforms and screening tools now include it. The key inputs include changes in receivables relative to sales, gross margin trends, asset quality, and the ratio of total accruals to total assets. While not perfect, studies show it would have flagged companies like Enron and WorldCom before their collapses.

**Q6: What is "channel stuffing" and how do I detect it?**

A: Channel stuffing occurs when a company ships excess product to distributors or retailers at the end of a quarter to inflate reported revenue. The distributors have not actually sold the product and will likely return it next quarter. Detection clues: (1) Revenue spikes at quarter-end with no corresponding demand increase. (2) Accounts receivable growing significantly faster than revenue (product shipped but not paid for). (3) Increases in sales returns and allowances in subsequent quarters. (4) Inventory at distributors (if disclosed) growing faster than end-customer demand. Companies in consumer products, technology hardware, and pharmaceuticals are most susceptible.

**Q7: What is the relationship between earnings quality and stock returns?**

A: The Sloan Accrual Anomaly (1996) is one of the best-documented findings in financial research. Stocks with high accruals (earnings far exceeding cash flow) consistently underperform stocks with low accruals (cash flow exceeding earnings) by 5-10% annually over subsequent years. The market appears to naively extrapolate headline earnings without examining whether those earnings are backed by cash. Value investors can exploit this by screening for companies with high cash flow relative to earnings and avoiding those where the reverse is true.

**Q8: Can a company have positive earnings but negative free cash flow indefinitely?**

A: Not indefinitely, but it can persist for many years, particularly for companies in heavy growth phases. Amazon reported positive net income as early as 2003 but had negative or minimal free cash flow for many years afterward because of massive capital expenditures on warehouses, data centers, and logistics. Eventually, the gap must close -- either the investments start generating enough cash to turn FCF positive, or the earnings were an illusion. If a mature, non-growing company consistently has earnings above FCF, that is a serious red flag.

**Q9: How should I handle companies that report "adjusted EPS" instead of GAAP EPS?**

A: Be very cautious with adjusted (non-GAAP) EPS. Companies exclude "one-time" charges like restructuring costs, acquisition expenses, and stock-based compensation to present a rosier picture. Some adjustments are legitimate -- truly one-time events that distort the ongoing picture. But many companies have "one-time" charges every single quarter, which means they are not one-time at all. Always compare adjusted EPS to GAAP EPS and to free cash flow. If adjusted EPS is consistently 30-50% higher than GAAP EPS, the company is likely overstating its profitability. If adjusted EPS is close to GAAP EPS, the adjustments are probably reasonable.

**Q10: How do I build a simple earnings quality screen?**

A: Start with these four filters: (1) Operating Cash Flow / Net Income greater than 1.0 for at least 3 of the last 5 years. (2) Free Cash Flow positive for at least 4 of the last 5 years. (3) Accrual ratio below 5% (total accruals as a percentage of total assets). (4) Receivables growing no faster than revenue over the past 3 years. This simple screen will eliminate most earnings manipulation and low-quality earnings situations. Layer in valuation metrics like FCF yield to find stocks that are both high quality and reasonably priced.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 20: Earnings and Cash Flow - Quality, Manipulation, and Free Cash Flow"]

**Alex:** Welcome back everyone. Today we are going to learn a skill that separates truly sophisticated investors from everyone else -- the ability to tell whether a company's reported profits are real or a mirage. We are talking about earnings quality, cash flow analysis, and how to spot manipulation.

**Sam:** This sounds almost forensic. Like we are going to become financial detectives.

**Alex:** That is exactly what we are going to become. And here is why this matters so much. Every major corporate collapse in the last 25 years -- Enron, WorldCom, Luckin Coffee, Wirecard -- involved earnings manipulation that was actually detectable from publicly available financial statements. Investors who knew how to read the cash flow statement and compare it to earnings were not surprised. They had already moved on.

**Sam:** Okay, I am hooked. Where do we start?

**Alex:** Let us start with the most basic metric every investor sees -- earnings per share, or EPS. When a company reports quarterly results, the headline number is almost always EPS. "Company X reports EPS of $2.15, beating estimates of $2.08." That is the format you see everywhere.

[VISUAL: Mock-up of a financial news headline showing "TechCorp Reports Q3 EPS of $2.15 vs. $2.08 Expected -- Stock Jumps 5%"]

**Sam:** Right, I see those headlines all the time. And the stock usually goes up if they beat and down if they miss.

**Alex:** Correct. But here is what most people do not understand. That $2.15 is not a fact like the temperature outside. It is the output of dozens of accounting judgments, estimates, and management choices. How quickly are they depreciating their equipment? When are they recognizing revenue? How much are they reserving for customer returns? Each of these decisions affects the final EPS number.

**Sam:** So earnings are not just "how much money the company made?"

**Alex:** Not exactly. This brings us to one of the most important concepts in all of finance -- the difference between accrual accounting and cash accounting.

[VISUAL: Title card "Accrual vs. Cash Accounting -- The Most Important Distinction in Financial Analysis"]

**Alex:** The income statement -- where EPS comes from -- is based on accrual accounting. This means revenue is recorded when it is earned, not when cash is received. And expenses are recorded when they are incurred, not when they are paid.

**Sam:** Can you give me a concrete example?

**Alex:** Sure. Imagine a software company signs a three-year, $3 million contract on January 1st. Under accrual accounting, the company recognizes $83,000 in revenue each month -- one thirty-sixth of the contract value. But the customer might not actually pay anything until six months in. The income statement shows revenue. The bank account shows no money.

**Sam:** So the company looks profitable on the income statement but might not have any cash?

**Alex:** Exactly. And this is why the cash flow statement is arguably more important than the income statement for investors. Cash flow tells you what actually went into and out of the bank account. It is much harder to manipulate because you either have the cash or you do not.

[ANIMATION: animation/week20_accrual_vs_cash.py - Two parallel timelines showing the same company's year. The top timeline (Income Statement) shows smooth, growing revenue bars each quarter. The bottom timeline (Cash Flow) shows lumpy, irregular cash receipts and payments. The revenue line looks beautiful and consistent. The cash flow line looks messy but real. Annotations highlight the gap: "The income statement tells a story. The cash flow statement tells the truth."]

**Sam:** If cash flow is harder to fake, why do companies use accrual accounting at all?

**Alex:** Because accrual accounting actually gives a better picture of economic performance in most cases. If a company delivers $100 million in products this quarter but has not collected payment yet, the accrual approach correctly shows $100 million in economic activity. Cash accounting would show zero until the money arrives, which could be misleading. Accrual accounting is not bad -- it is when companies abuse the judgment calls within accrual accounting that problems arise.

**Sam:** So the key is comparing the two -- what the income statement says versus what the cash flow statement says?

**Alex:** Precisely. And this brings us to one of the most powerful tools in an investor's arsenal: the operating cash flow to net income ratio.

[VISUAL: Large formula display: "OCF / Net Income Ratio -- Compare every quarter"]

**Alex:** You simply divide operating cash flow by net income. If the ratio is above 1.0, cash flow exceeds reported earnings, which is a positive quality signal. If it is below 1.0, earnings exceed cash flow, and you need to investigate why.

**Sam:** What would a good company look like versus a suspicious one?

**Alex:** Let me show you a five-year comparison. A high-quality company might look like this. Year one, net income is $100 million and operating cash flow is $130 million. Year two, $120 million and $140 million. Year three, $150 million and $170 million. Both are growing, and cash flow consistently exceeds earnings.

**Sam:** And the suspicious company?

**Alex:** The suspicious company shows net income growing from $100 million to $200 million over five years -- impressive headline growth. But operating cash flow goes from $130 million down to $60 million. Earnings are going up and cash flow is going down. That divergence is one of the most reliable red flags in all of financial analysis.

[ANIMATION: animation/week20_divergence.py - Two line charts animating over 5 years. Chart A ("High Quality Company") shows net income and operating cash flow lines both rising, with OCF consistently above net income. Chart B ("Red Flag Company") shows net income rising while operating cash flow declines, with the lines crossing and then diverging dramatically. At the crossover point, a warning icon flashes. The final frame highlights: "When earnings go up but cash flow goes down, the earnings are likely not real."]

**Sam:** That is powerful. But how does a company manage to report growing earnings while cash flow declines?

**Alex:** Several ways, and this is where it gets really interesting. Let me walk you through the most common manipulation techniques.

**Alex:** First, there is revenue manipulation. The most famous technique is called channel stuffing. A company ships excess product to its distributors right before the quarter ends. On the income statement, that counts as revenue because the product has been "sold." But the distributors did not actually need the product, and they will return it next quarter.

**Sam:** So the company is just borrowing revenue from the future?

**Alex:** Exactly. And it shows up in the financials if you know where to look. Accounts receivable -- the money customers owe the company -- will grow much faster than revenue. Why? Because the company is shipping product to distributors who have not paid for it and probably will not.

[VISUAL: A chart showing Revenue growing at 10% per year side by side with Accounts Receivable growing at 30% per year. An alarm bell icon appears with the caption: "When receivables grow faster than revenue, someone is not paying -- or the revenue is not real."]

**Sam:** What about expense manipulation?

**Alex:** One of the most common techniques is capitalizing expenses. Normally, when you spend money on something that gets consumed quickly -- like marketing or maintenance -- it flows through the income statement as an expense, reducing earnings. But if you capitalize it -- put it on the balance sheet as an asset -- it does not hit earnings this year. Instead, you depreciate it slowly over many years.

**Sam:** So the company is hiding current expenses by pretending they are long-term investments?

**Alex:** Exactly. WorldCom did this with billions of dollars of ordinary operating costs. They classified regular maintenance expenses as capital investments, which inflated their earnings by billions. On the income statement, everything looked fine. But on the cash flow statement, the cash was obviously going out the door. The cash flow statement does not care whether you call something capex or an expense -- cash spent is cash spent.

**Sam:** This is really making me appreciate the cash flow statement.

**Alex:** It should. Which brings us to free cash flow -- the single most important number for long-term investors.

[VISUAL: Title card "Free Cash Flow: The Most Important Number in Investing"]

**Alex:** Free cash flow is operating cash flow minus capital expenditures. It represents the cash a company generates after spending what it needs to maintain and grow its operations. It is the cash truly available to shareholders -- for dividends, buybacks, debt payoff, or further investment.

**Sam:** Why is FCF more important than net income for investors?

**Alex:** Because net income includes non-cash items and accounting estimates that can distort reality. Free cash flow strips all of that away and tells you: how much cash did the business actually produce that could be handed to me, the owner?

**Alex:** Let me use a concrete example. Suppose Company ABC reports $200 million in net income. Sounds great. But when you calculate free cash flow, you discover it is only $50 million. Where did the other $150 million go? Maybe $100 million went to depreciation adjustments that artificially inflated net income. Maybe $50 million went to a build-up in accounts receivable -- revenue was booked but cash was never collected.

[VISUAL: Waterfall chart starting with Net Income of $200M, then showing adjustments: +$100M depreciation, +$50M stock-based compensation, -$80M working capital build-up, = $270M Operating Cash Flow, -$220M Capital Expenditures, = $50M Free Cash Flow. The contrast between $200M in net income and $50M in FCF is stark and visually dramatic.]

**Sam:** $200 million in earnings but only $50 million in free cash flow. That is a huge gap.

**Alex:** And it tells you the reported earnings are overstating the company's actual cash-generating ability. Now, there are legitimate reasons for a gap. A company investing heavily in growth -- building new factories, developing new technology -- will have high capex that reduces FCF below net income. Amazon was in this situation for years. The question is whether those investments will generate future returns above the cost of capital.

**Sam:** How do I tell the difference between good investment and waste?

**Alex:** Three things to check. One, look at the company's return on invested capital, or ROIC. If past investments have consistently generated returns above the WACC we learned about last week, management has earned the benefit of the doubt. Two, look at what peers are spending. If the entire industry is investing heavily, the capex is likely necessary. Three, listen to what management says and whether their past promises about investment returns actually materialized. Some CEOs repeatedly promise returns from new investments that never pan out -- that is a pattern of capital destruction.

**Sam:** Now, you mentioned FCF yield as a valuation metric. How does that work?

**Alex:** FCF yield is free cash flow divided by market cap. It tells you the cash return you are getting for the price you pay. Think of it like the yield on a bond, but for a stock.

[VISUAL: Simple calculation showing: "FCF: $500M, Market Cap: $10B, FCF Yield: 5.0%". Below it, a comparison bar chart showing FCF yields for the S&P 500 (3-4%), a value stock (7%), a growth stock (1%), and the 10-year Treasury yield (4.5%), providing context for what constitutes a high or low FCF yield.]

**Alex:** If a company has an FCF yield of 5%, it generates $5 in cash for every $100 of market value. You can compare this directly to bond yields. If the 10-year Treasury yields 4.5% and a stock has an FCF yield of 7%, the stock is generating more cash than the bond -- and that cash can grow, unlike bond coupons.

**Sam:** What is a good FCF yield?

**Alex:** The average for the S&P 500 is roughly 3 to 5%. Below 2% is typical for high-growth companies that reinvest everything. Above 6% is above average and potentially attractive. Above 10% is either a deep value opportunity or a value trap -- you need to figure out which.

**Sam:** How do you tell the difference?

**Alex:** A high FCF yield is a genuine opportunity if the company's cash flows are sustainable, the business is stable, and the market is just being pessimistic. It is a value trap if cash flows are about to decline due to competitive threats, expiring contracts, or secular headwinds. This is where the qualitative analysis -- understanding the business -- meets the quantitative analysis.

**Sam:** Let me ask about something practical. When I am looking at a company's financial statements, how should I actually read the cash flow statement?

**Alex:** The cash flow statement has three sections, and each tells a different story. The first section is operating cash flow -- cash generated from the core business. This should be positive and growing for any mature company. If it is negative, the company is not self-sustaining.

**Alex:** The second section is investing cash flow -- cash spent on investments like equipment, acquisitions, or financial assets. For a growing company, this is usually negative, which is fine. For a declining company selling assets to stay alive, it might be positive -- and that is a warning sign.

**Alex:** The third section is financing cash flow -- cash from or to capital providers. This includes issuing or repaying debt, issuing or buying back stock, and paying dividends. For mature companies returning capital, this is typically negative.

[ANIMATION: animation/week20_cash_flow_sections.py - Three animated funnels representing the three sections of the cash flow statement. Green dollars flow through the Operating funnel (largest, flowing in). Red dollars flow through the Investing funnel (flowing out for capex). Blue dollars flow through the Financing funnel (flowing out for dividends and buybacks). The net of all three flows into a "Cash Balance" bucket at the bottom, which fills or drains based on the totals. Different company profiles are shown -- healthy mature company, high-growth company, and distressed company -- each with dramatically different flow patterns.]

**Sam:** This is really clicking. Let me try to put it all together. When I analyze a company, I should look at EPS for the headline, but then immediately check operating cash flow to see if the earnings are backed by real cash. I should calculate free cash flow to see what is actually available to me as a shareholder. And I should compare FCF yield to other investments to see if the valuation makes sense.

**Alex:** That is an excellent framework. And I want to add one more layer. Always look at trends over time, not just a single year. One year of low cash flow relative to earnings might be a timing issue. Three or four consecutive years of deteriorating cash flow quality is a serious red flag that the reported earnings may not be sustainable.

**Sam:** Are there any tools or quick metrics I can use to screen for earnings quality?

**Alex:** Yes. There is a model called the Beneish M-Score that uses eight financial ratios to estimate the probability that a company is manipulating its earnings. An M-Score above negative 1.78 suggests a high probability of manipulation. It is not perfect, but studies show it would have flagged companies like Enron before they collapsed. Many financial analysis platforms now include it.

**Sam:** For the average investor who does not want to run complex models, what are the top three things to check?

**Alex:** Number one, check the OCF to net income ratio. It should be above 1.0 most years. Number two, check whether receivables are growing faster than revenue. That is the simplest and most reliable manipulation flag. Number three, read the auditor's opinion in the annual report. If it is anything other than a clean, unqualified opinion -- or if the auditor recently changed -- investigate further.

[VISUAL: A "Quick Earnings Quality Check" card with three items:
1. OCF / Net Income > 1.0? (check mark or X)
2. Receivables growing slower than revenue? (check mark or X)
3. Clean audit opinion? (check mark or X)
"If all three check marks: proceed with confidence. If any X: investigate before investing."]

**Sam:** What about adjusted earnings? I see a lot of companies reporting "adjusted EPS" that is higher than the regular number.

**Alex:** This is one of my pet peeves. Many companies report "non-GAAP" or "adjusted" earnings that exclude things like stock-based compensation, restructuring charges, and acquisition costs. The problem is that some of these "one-time" charges happen every single quarter. Stock-based compensation is a real cost -- it dilutes shareholders. Restructuring charges year after year suggest the business is perpetually struggling.

**Sam:** So I should ignore adjusted earnings?

**Alex:** Not ignore, but be deeply skeptical. Always compare adjusted EPS to GAAP EPS. If the gap is small -- say 5 to 10% -- the adjustments are probably reasonable. If the gap is 30, 40, 50% -- the company is painting a dramatically different picture than reality, and you should rely on the GAAP number and free cash flow instead.

**Sam:** This episode has fundamentally changed how I will look at financial statements. I feel like I had been reading only the income statement and completely ignoring the cash flow statement.

**Alex:** You are not alone. Most retail investors focus almost exclusively on earnings and revenue because that is what the financial media emphasizes. But the smart money -- professional value investors, short sellers, forensic accountants -- they start with the cash flow statement and work backward. If the cash flow supports the earnings, great. If it does not, there is a problem, regardless of how good the headline EPS looks.

**Sam:** One final question. Where should someone start if they want to practice this analysis?

**Alex:** Pick five companies you own or are interested in. Pull up their cash flow statements on the SEC's EDGAR website or any financial data provider. For each company, calculate the OCF to net income ratio for the last five years. Calculate free cash flow and FCF yield. Check if receivables are growing faster than revenue. You will be amazed at what you find. Some companies you thought were great will have concerning quality signals, and some you overlooked will turn out to be cash flow machines.

[VISUAL: End screen with key takeaways:
- Earnings are an opinion; cash flow is a fact
- OCF/Net Income > 1.0 signals high quality
- Free Cash Flow = Operating Cash Flow minus Capex
- FCF Yield is a valuation metric based on real cash
- Receivables growing faster than revenue is a red flag
- Always compare GAAP EPS to adjusted EPS
- The cash flow statement is the investor's X-ray machine]

**Sam:** What is next week?

**Alex:** Next week is equity valuation -- we are going to bring everything together and learn how to actually determine what a stock is worth using P/E ratios, EV/EBITDA, and discounted cash flow analysis. All the earnings and cash flow analysis we learned today feeds directly into valuation.

[VISUAL: Preview card for Week 21 with "Equity Valuation: P/E, P/B, and DCF"]

**Alex:** Thanks for watching everyone. If you have ever bought a stock based purely on EPS growth without checking the cash flow statement, today's lesson just saved you from potentially costly mistakes in the future. Share it with anyone who invests based on headlines without reading the financials. See you next week.

[VISUAL: Outro animation with subscribe button and links to previous episodes]
