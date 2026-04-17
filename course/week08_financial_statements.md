# Week 8: Reading Financial Statements - Basics

---

## Reading Section

### a) Why This Is Important

Financial statements are the language of business. If you want to invest in individual stocks, evaluate a company inside an ETF, or simply understand the economic news, you must be able to read financial statements. They are to an investor what X-rays and blood tests are to a doctor -- they reveal what is happening beneath the surface, exposing strengths and weaknesses that stock prices and headlines often obscure.

Here is why this skill is non-negotiable for serious investors:

1. **Financial statements are the only objective source of truth about a company.** Management can say anything in a press release. Analysts can have biases. Stock prices reflect sentiment and speculation. But the financial statements -- audited by independent accountants and filed with regulators -- contain verifiable, standardized data. They are the foundation of every credible investment analysis.

2. **Without financial literacy, you are investing blind.** Imagine buying a house without inspecting it, or hiring an employee without checking their references. When you buy a stock without reading the financial statements, you are trusting the crowd's assessment of a business you have not personally evaluated. Sometimes the crowd is right. But when it is wrong, the consequences can be devastating.

3. **Financial statements expose fraud and manipulation early.** Enron, WorldCom, Wirecard -- every major corporate fraud was hiding in plain sight in the financial statements for those who knew where to look. Revenue growing faster than cash flow. Debt hidden in off-balance-sheet entities. Receivables ballooning relative to sales. These warning signs are visible in the statements long before the stock price collapses.

4. **The three financial statements tell three different stories that must be consistent.** The income statement tells you whether the company is profitable. The balance sheet tells you whether the company is financially healthy. The cash flow statement tells you whether the company is actually generating cash. When these three stories align, you have confidence. When they diverge, something may be wrong.

5. **This is the foundation for everything that follows.** Valuation ratios like P/E, P/B, and EV/EBITDA (Week 21) are meaningless if you do not understand the numbers they are based on. Equity analysis, credit analysis, and advanced financial statement analysis all build on the basics covered in this lesson.

The CFA curriculum devotes an enormous portion of its study material to Financial Statement Analysis (FSA). At Level I alone, FSA accounts for roughly 13-15% of the exam. The CFA Institute considers it one of the core competencies of any investment professional, and for good reason: you cannot value what you cannot measure, and financial statements are how we measure businesses.

---

### b) What You Need to Know

#### 1. The Three Financial Statements -- An Overview

Every publicly traded company publishes three core financial statements, typically on a quarterly and annual basis:

```
THE THREE FINANCIAL STATEMENTS
=================================

+------------------------+     +------------------------+     +------------------------+
|   INCOME STATEMENT     |     |    BALANCE SHEET       |     |  CASH FLOW STATEMENT   |
|   (Profit & Loss)      |     |    (Financial Position)|     |  (Cash Movements)      |
+------------------------+     +------------------------+     +------------------------+
|                        |     |                        |     |                        |
| Revenue                |     | ASSETS                 |     | Operating Activities   |
| - Cost of Goods Sold   |     |   Current Assets       |     |   (Cash from business  |
| = Gross Profit         |     |   Non-Current Assets   |     |    operations)         |
| - Operating Expenses   |     |                        |     |                        |
| = Operating Income     |     | LIABILITIES            |     | Investing Activities   |
| - Interest Expense     |     |   Current Liabilities  |     |   (Cash for buying/    |
| - Taxes                |     |   Non-Current Liab.    |     |    selling assets)      |
| = Net Income           |     |                        |     |                        |
|                        |     | EQUITY                 |     | Financing Activities   |
| Covers: A PERIOD       |     |   Stockholders' Equity |     |   (Cash from/to        |
| (e.g., Jan-Dec 2025)   |     |                        |     |    investors/lenders)   |
|                        |     | Covers: A POINT IN     |     |                        |
| Answers: "Did the      |     | TIME (e.g., Dec 31)    |     | Covers: A PERIOD       |
|  company make money?"  |     |                        |     | (e.g., Jan-Dec 2025)   |
|                        |     | Answers: "What does    |     |                        |
|                        |     |  the company own and   |     | Answers: "Where did    |
|                        |     |  owe right now?"       |     |  the cash come from    |
|                        |     |                        |     |  and where did it go?" |
+------------------------+     +------------------------+     +------------------------+
```

A crucial distinction: the income statement and cash flow statement cover a **period of time** (like a movie), while the balance sheet captures a **point in time** (like a photograph). This matters because you can compare periods (Q1 this year vs. Q1 last year) or snapshots (balance sheet at year-end vs. the prior year-end).

---

#### 2. The Income Statement (Profit and Loss Statement)

The income statement shows whether a company made or lost money over a specific period. It starts with revenue at the top and works its way down through various expenses to arrive at net income (or net loss) at the bottom. This is why net income is often called the "bottom line."

```
INCOME STATEMENT STRUCTURE
============================

  Revenue (Sales)                              $1,000,000
  - Cost of Goods Sold (COGS)                   (600,000)
  ------------------------------------------------
  = GROSS PROFIT                                 $400,000    Gross Margin = 40%
  
  - Selling, General & Administrative (SG&A)     (150,000)
  - Research & Development (R&D)                  (80,000)
  - Depreciation & Amortization (D&A)             (30,000)
  ------------------------------------------------
  = OPERATING INCOME (EBIT)                      $140,000    Operating Margin = 14%
  
  - Interest Expense                              (20,000)
  + Interest Income                                 5,000
  ------------------------------------------------
  = EARNINGS BEFORE TAX (EBT)                    $125,000
  
  - Income Tax Expense (25%)                      (31,250)
  ------------------------------------------------
  = NET INCOME                                    $93,750    Net Margin = 9.4%
  
  Earnings Per Share (EPS) = Net Income / Shares
  If 10,000 shares outstanding: EPS = $9.38
```

**Key metrics from the income statement:**

```
MARGIN ANALYSIS
================

                          Healthy        Warning Sign
                          -------        ------------
  Gross Margin            >40%           <20% (unless retailer)
  (Revenue - COGS)        Industry-      Declining over time
  / Revenue               dependent      means pricing pressure

  Operating Margin        >15%           <5%
  (EBIT / Revenue)        Shows          Declining suggests
                          efficiency     cost problems

  Net Margin              >10%           <3%
  (Net Income /           After all      Thin margins mean
   Revenue)               costs          little room for error

  IMPORTANT: Margins vary enormously by industry!
  
  Typical ranges:
  Software/SaaS:    70-85% gross,  20-40% operating
  Consumer Staples: 30-50% gross,  15-25% operating
  Retail/Grocery:   25-35% gross,   3-8%  operating
  Airlines:         40-60% gross,   5-15% operating
  Banks:            N/A (use Net Interest Margin instead)
```

**What to look for on the income statement:**

- **Revenue growth.** Is the top line growing? Revenue is the hardest number to fake over long periods and is the ultimate driver of long-term value.
- **Margin trends.** Are margins expanding (good -- pricing power, cost efficiency) or contracting (bad -- competition, rising costs)?
- **One-time items.** Watch for "restructuring charges," "asset impairments," or "gains on sale" that distort the true operating picture. Normalize earnings by excluding non-recurring items.
- **Revenue quality.** Is revenue from recurring sources (subscriptions, contracts) or one-time sales? Recurring revenue is far more valuable.

---

#### 3. The Balance Sheet (Statement of Financial Position)

The balance sheet shows what a company owns (assets), what it owes (liabilities), and the residual value belonging to shareholders (equity) at a specific point in time. The fundamental equation is:

```
THE ACCOUNTING EQUATION
========================

  ASSETS = LIABILITIES + SHAREHOLDERS' EQUITY

  What the         What the company     What belongs
  company OWNS     OWES to others       to shareholders

  Think of it as a personal analogy:
  
  Your house value     =   Your mortgage   +   Your home equity
  ($500,000)               ($300,000)           ($200,000)

  This equation ALWAYS balances. That is why it is
  called a "balance" sheet.
```

**Balance sheet structure:**

```
BALANCE SHEET LAYOUT
======================

ASSETS (What the company owns)         LIABILITIES (What the company owes)
================================       ==================================

CURRENT ASSETS (< 1 year)             CURRENT LIABILITIES (< 1 year)
  Cash & Equivalents       $50,000       Accounts Payable        $40,000
  Short-Term Investments    20,000       Short-Term Debt          25,000
  Accounts Receivable       80,000       Accrued Expenses         15,000
  Inventory                 60,000       Current Portion of        
  Prepaid Expenses          10,000         Long-Term Debt         10,000
                          --------                               --------
  Total Current Assets    $220,000       Total Current Liab.     $90,000

NON-CURRENT ASSETS (> 1 year)         NON-CURRENT LIABILITIES (> 1 year)
  Property, Plant &                      Long-Term Debt         $150,000
    Equipment (PP&E)      $300,000       Deferred Tax Liab.      20,000
  Goodwill                 100,000       Pension Obligations      30,000
  Intangible Assets         50,000                              --------
  Long-Term Investments     30,000       Total Non-Current      $200,000
                          --------
  Total Non-Current       $480,000     TOTAL LIABILITIES        $290,000

                                       SHAREHOLDERS' EQUITY
                                         Common Stock           $100,000
                                         Retained Earnings      $280,000
                                         Treasury Stock          (50,000)
TOTAL ASSETS              $700,000       Other                    80,000
                                                                --------
                                       TOTAL EQUITY             $410,000

                                       TOTAL LIAB. + EQUITY    $700,000
                                                                ========
                          $700,000  =  $290,000  +  $410,000    BALANCES!
```

**Key balance sheet concepts:**

**Current vs. Non-Current.** Current assets are expected to be converted to cash within one year (accounts receivable, inventory). Current liabilities are due within one year (accounts payable, short-term debt). The relationship between them is crucial for assessing short-term financial health.

**Working Capital.** Current Assets minus Current Liabilities. Positive working capital means the company can pay its short-term obligations. Negative working capital can signal financial distress (but some businesses like Amazon operate with negative working capital by design, collecting from customers before paying suppliers).

```
WORKING CAPITAL AND LIQUIDITY
===============================

  Working Capital = Current Assets - Current Liabilities
                  = $220,000 - $90,000
                  = $130,000  (positive = healthy)

  Current Ratio   = Current Assets / Current Liabilities
                  = $220,000 / $90,000
                  = 2.44x     (>1.5 generally healthy)

  Quick Ratio     = (Current Assets - Inventory) / Current Liabilities
                  = ($220,000 - $60,000) / $90,000
                  = 1.78x     (>1.0 generally healthy)
                  (Excludes inventory because it may not
                   be quickly convertible to cash)
```

**Goodwill and Intangible Assets.** Goodwill appears when a company acquires another company for more than the value of its tangible assets. It represents the premium paid for brand, customer relationships, synergies, and other intangibles. A large goodwill balance means the company has been an active acquirer. Goodwill impairments (writedowns) can signal that past acquisitions overpaid, which is a red flag for management's capital allocation skills.

**What to look for on the balance sheet:**

- **Debt levels.** Debt-to-Equity ratio above 2.0 warrants scrutiny. Excessive debt increases bankruptcy risk and limits financial flexibility.
- **Cash position.** Is there enough cash to cover short-term obligations? Cash-rich companies have a strategic advantage in downturns.
- **Receivables relative to revenue.** If receivables are growing much faster than revenue, the company may be booking revenue aggressively or having trouble collecting payments.
- **Inventory trends.** Rising inventory relative to sales can signal weakening demand or production problems.

---

#### 4. The Cash Flow Statement

The cash flow statement is arguably the most important financial statement for investors, yet it is the one that gets the least attention from beginners. It shows where cash actually came from and where it went, stripping away the accounting assumptions that can make the income statement misleading.

Why is cash flow so important? Because you cannot pay employees, suppliers, or dividends with accounting profits. You pay them with cash. A company can report positive net income for years while actually burning cash -- and eventually run out of money. The cash flow statement reveals this.

```
CASH FLOW STATEMENT STRUCTURE
================================

OPERATING ACTIVITIES (Cash from running the business)
------------------------------------------------------
  Net Income                                    $93,750
  + Depreciation & Amortization                  30,000
    (non-cash expense added back)
  - Increase in Accounts Receivable             (15,000)
    (sold goods but haven't collected cash yet)
  - Increase in Inventory                       (10,000)
    (bought inventory, cash went out)
  + Increase in Accounts Payable                 12,000
    (owe suppliers but haven't paid cash yet)
  + Other Adjustments                             5,000
                                               --------
  NET CASH FROM OPERATIONS                     $115,750

INVESTING ACTIVITIES (Cash for long-term assets)
------------------------------------------------------
  - Purchase of PP&E (Capital Expenditure)      (50,000)
  - Acquisition of Subsidiary                   (30,000)
  + Sale of Equipment                            10,000
                                               --------
  NET CASH FROM INVESTING                      ($70,000)

FINANCING ACTIVITIES (Cash from/to investors & lenders)
------------------------------------------------------
  + Proceeds from Long-Term Debt                 40,000
  - Repayment of Debt                           (20,000)
  - Dividends Paid                              (25,000)
  - Share Buybacks                              (15,000)
                                               --------
  NET CASH FROM FINANCING                      ($20,000)

                                               --------
  NET CHANGE IN CASH                            $25,750
  + Beginning Cash Balance                       24,250
                                               --------
  ENDING CASH BALANCE                           $50,000
```

**The three sections explained:**

```
OPERATING      "How much cash does the core business generate?"
               This is the most important section.
               Positive = business is self-sustaining
               Negative = business is burning cash (warning!)

INVESTING      "Is the company investing for future growth?"
               Usually negative (spending on PP&E, acquisitions)
               Positive can mean selling assets (may be good
               or bad depending on context)

FINANCING      "How is the company funded?"
               Positive = raising money (issuing debt or stock)
               Negative = returning money (paying debt,
               dividends, or buying back shares)
```

**Free Cash Flow -- The Number Investors Care About Most:**

```
FREE CASH FLOW (FCF)
=====================

  FCF = Cash from Operations - Capital Expenditures

  From our example:
  FCF = $115,750 - $50,000 = $65,750

  Why FCF matters:
  - It is the cash available AFTER maintaining/growing the business
  - It can be used for: dividends, buybacks, debt repayment,
    acquisitions, or building cash reserves
  - FCF is much harder to manipulate than net income
  - It is the basis of DCF valuation (Week 21)

  FCF YIELD = FCF / Market Capitalization
  
  If market cap = $800,000:
  FCF Yield = $65,750 / $800,000 = 8.2%
  
  Compare to:
  - Bond yields (~4-5%): FCF yield higher = stocks may be cheap
  - Stock market average FCF yield (~3-4%): This company looks
    attractive on a cash flow basis
```

---

#### 5. How the Three Statements Connect

This is one of the most important concepts in accounting and financial analysis. The three statements are not independent -- they are deeply interconnected. Understanding these connections is what separates a competent analyst from a beginner.

```
HOW THE THREE STATEMENTS ARE LINKED
======================================

                    INCOME STATEMENT
                    ================
                    Revenue
                    - Expenses
                    = Net Income ---+
                                    |
                    +---------------+---------------+
                    |                               |
                    v                               v
            BALANCE SHEET                  CASH FLOW STATEMENT
            =============                 ====================
            Assets | Liabilities           STARTS with
                   | + Equity              Net Income
                   |                       (from Income Stmt)
     Net Income -->| Retained              
     flows into    | Earnings              Adjusts for non-cash
     Retained      | increases             items and working
     Earnings      |                       capital changes
                   |                       
     Cash from  -->| Cash (asset)          ENDS with
     Cash Flow     | changes               change in Cash
     Stmt updates  |                       (which updates the
     Cash on       |                       Balance Sheet)
     Balance Sheet |

CIRCULAR CONNECTIONS:
  1. Net Income from Income Statement feeds into
     Retained Earnings on Balance Sheet

  2. Net Income is the starting point of the
     Cash Flow Statement (indirect method)

  3. Ending Cash from Cash Flow Statement updates
     Cash on the Balance Sheet

  4. Depreciation on Income Statement reduces PP&E
     on Balance Sheet and is added back on
     Cash Flow Statement

  5. New debt on Cash Flow Statement (financing)
     increases Liabilities on Balance Sheet and
     creates Interest Expense on Income Statement
```

**A practical example of the interconnection:**

```
TRACING A SALE THROUGH ALL THREE STATEMENTS
=============================================

Event: Company sells $10,000 of product on credit
       (cost of goods was $6,000)

INCOME STATEMENT IMPACT:
  Revenue:          +$10,000
  COGS:             -$6,000
  Gross Profit:     +$4,000
  (Net income increases)

BALANCE SHEET IMPACT:
  Accounts Receivable:  +$10,000  (asset increases)
  Inventory:            -$6,000   (asset decreases)
  Retained Earnings:    +$4,000   (equity increases, via net income)
  (Assets = Liabilities + Equity still balances!)

CASH FLOW STATEMENT IMPACT:
  Net Income:               +$4,000
  Increase in Receivables:  -$10,000  (cash not yet collected)
  Decrease in Inventory:    +$6,000   (cash was spent earlier)
  Net Cash Impact:          $0        (no cash moved yet!)

KEY INSIGHT: The company booked $4,000 in profit,
but received ZERO cash! The cash arrives only when
the customer pays. This is why the cash flow
statement exists -- to show the truth about cash.
```

---

#### 6. Key Financial Ratios

Financial ratios translate raw statement numbers into comparable, meaningful metrics. They fall into four broad categories:

```
FINANCIAL RATIO CATEGORIES
============================

1. PROFITABILITY RATIOS
   "Is the company making money efficiently?"
   +------------------------------------------+
   | Gross Margin    = Gross Profit / Revenue  |
   | Operating Margin= EBIT / Revenue          |
   | Net Margin      = Net Income / Revenue    |
   | ROE             = Net Income / Equity     |
   | ROA             = Net Income / Total Assets|
   +------------------------------------------+

2. LIQUIDITY RATIOS
   "Can the company pay its short-term bills?"
   +------------------------------------------+
   | Current Ratio   = Current Assets /        |
   |                   Current Liabilities      |
   | Quick Ratio     = (Cash + Receivables) /  |
   |                   Current Liabilities      |
   | Cash Ratio      = Cash / Current Liab.    |
   +------------------------------------------+

3. LEVERAGE (SOLVENCY) RATIOS
   "How much debt is the company carrying?"
   +------------------------------------------+
   | Debt-to-Equity  = Total Debt / Equity     |
   | Debt-to-Assets  = Total Debt / Total Assets|
   | Interest Cover. = EBIT / Interest Expense |
   | (Times Interest Earned)                   |
   +------------------------------------------+

4. EFFICIENCY RATIOS
   "How well does the company use its resources?"
   +------------------------------------------+
   | Inventory Turn. = COGS / Avg Inventory    |
   | Receivable Turn.= Revenue / Avg Receivables|
   | Asset Turnover  = Revenue / Total Assets  |
   | Days Sales Out. = 365 / Receivable Turnover|
   | (DSO)                                     |
   +------------------------------------------+
```

**Return on Equity (ROE) and the DuPont Decomposition:**

ROE is arguably the single most important ratio for equity investors. It measures how much profit a company generates with shareholders' money. The DuPont framework breaks ROE into three components to reveal what is driving it:

```
DUPONT DECOMPOSITION OF ROE
=============================

  ROE = Net Income / Shareholders' Equity

  Can be decomposed as:

  ROE = (Net Income/Revenue) x (Revenue/Assets) x (Assets/Equity)
        ^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^
         Profit Margin          Asset Turnover      Financial
         (Profitability)        (Efficiency)        Leverage

  Example Company A:  ROE = 20%
    Profit Margin:     10%  x
    Asset Turnover:    1.0  x
    Leverage:          2.0  = 20%
    (Moderate margins, moderate efficiency, some leverage)

  Example Company B:  ROE = 20%
    Profit Margin:     5%   x
    Asset Turnover:    2.0  x
    Leverage:          2.0  = 20%
    (Low margins but high efficiency, same leverage)

  Example Company C:  ROE = 20%
    Profit Margin:     20%  x
    Asset Turnover:    0.5  x
    Leverage:          2.0  = 20%
    (High margins but low efficiency, same leverage)

  SAME ROE, but VERY different business models!
  DuPont reveals WHY a company earns what it earns.

  WATCH OUT: High ROE driven primarily by leverage
  (high Assets/Equity) is RISKY. The company is
  borrowing heavily to boost returns.
```

---

#### 7. Red Flags in Financial Statements

Knowing what to look for can protect you from disasters:

```
FINANCIAL STATEMENT RED FLAGS
================================

RED FLAG                              WHY IT MATTERS
--------                              ---------------

Revenue growing but cash flow         May be booking revenue
from operations declining             aggressively or having
                                      collection problems

Receivables growing faster            Customers not paying,
than revenue                          or stuffing the channel

Inventory growing faster              Products not selling,
than revenue                          potential writedowns ahead

Frequent "one-time" charges           They are not one-time
that appear year after year           if they keep happening

Cash from operations                  The company is borrowing
consistently below net income         or using accounting tricks
                                      to report profits

Growing gap between operating         Acquisitions destroying
income and free cash flow             value, or heavy capex
                                      with poor returns

Frequent changes in accounting        Possible manipulation,
policies or auditor changes           loss of credibility

Goodwill that is very large           Past acquisitions may have
relative to total assets              overpaid; impairment risk

Related-party transactions            Potential conflicts of
that are large or unusual             interest, self-dealing

Declining interest coverage           May be heading toward
ratio (EBIT / Interest)              difficulty paying debt
```

---

#### 8. Reading Financial Statements -- The CFA Perspective

The CFA curriculum approaches Financial Statement Analysis (FSA) with particular rigor. Several concepts from the CFA framework are worth understanding even for non-candidates:

**Accrual Accounting vs. Cash Accounting:**
The income statement uses accrual accounting -- revenue is recognized when earned and expenses when incurred, regardless of when cash changes hands. This is why a company can be profitable on paper but cash-poor in reality. The CFA curriculum emphasizes understanding the difference between accrual earnings and cash earnings, and treating the cash flow statement as the more reliable indicator of financial health.

**Quality of Earnings:**
The CFA curriculum devotes significant attention to assessing whether reported earnings are sustainable and reliable. High-quality earnings are characterized by:

```
EARNINGS QUALITY SPECTRUM
===========================

  HIGH QUALITY                         LOW QUALITY
  +--------------------------------+  +--------------------------------+
  | Cash-backed (operating cash    |  | Non-cash (large accruals,      |
  |   flow close to net income)    |  |   growing receivables)         |
  | Recurring (from core business) |  | One-time (asset sales, gains)  |
  | Conservative accounting       |  | Aggressive accounting          |
  | Transparent disclosures       |  | Complex, opaque reporting      |
  | Stable or rising margins      |  | Volatile, erratic margins      |
  +--------------------------------+  +--------------------------------+

  KEY METRIC: Accruals Ratio
  = (Net Income - Cash from Operations) / Average Total Assets
  
  Lower accruals ratio = higher quality earnings
  Higher accruals ratio = more of earnings are "on paper"
```

**IFRS vs. US GAAP:**
The CFA curriculum covers both International Financial Reporting Standards (IFRS) and US Generally Accepted Accounting Principles (US GAAP). While broadly similar, they differ in important areas including inventory accounting (LIFO is allowed under GAAP but not IFRS), development costs (can be capitalized under IFRS but typically expensed under GAAP), and how certain financial instruments are classified. For global investors, understanding these differences is essential.

---

#### 9. A Complete Example: Analyzing a Company

```
MINI CASE STUDY: ANALYZING "WIDGET CORP"
==========================================

INCOME STATEMENT (Year Ended Dec 31)
                              2025         2024        Change
                              ----         ----        ------
Revenue                    $500,000     $450,000       +11.1%
COGS                       (275,000)    (240,000)      +14.6%
Gross Profit               $225,000     $210,000       +7.1%
  Gross Margin:             45.0%        46.7%         -1.7pp

SG&A                       (100,000)     (90,000)      +11.1%
R&D                         (40,000)     (35,000)      +14.3%
D&A                         (20,000)     (18,000)      +11.1%
Operating Income            $65,000      $67,000       -3.0%
  Operating Margin:          13.0%        14.9%        -1.9pp

Interest Expense            (10,000)      (8,000)      +25.0%
EBT                         $55,000      $59,000       -6.8%
Taxes (25%)                 (13,750)     (14,750)
Net Income                  $41,250      $44,250       -6.8%
  Net Margin:                 8.3%         9.8%        -1.5pp

EPS (10,000 shares):         $4.13        $4.43        -6.8%

ANALYSIS:
- Revenue growing 11%, good top-line growth
- But COGS growing 14.6%, FASTER than revenue --> margins compressing
- Gross margin declined from 46.7% to 45.0% --> cost or pricing pressure
- Operating income actually DECLINED despite revenue growth
- Interest expense up 25% --> company took on more debt
- Net income declined 6.8% despite 11.1% revenue growth
- CONCLUSION: Revenue growth is masking deteriorating profitability
```

```
BALANCE SHEET SNAPSHOT
                              2025         2024        Change
                              ----         ----        ------
Cash                        $30,000      $45,000       -33.3%
Receivables                  90,000       65,000       +38.5%
Inventory                    75,000       55,000       +36.4%
Total Current Assets       $195,000     $165,000       +18.2%

PP&E                       $250,000     $220,000       +13.6%
Goodwill                    100,000       50,000      +100.0%
Total Assets               $545,000     $435,000       +25.3%

Current Liabilities         $85,000      $70,000       +21.4%
Long-Term Debt             $130,000      $90,000       +44.4%
Total Liabilities          $215,000     $160,000       +34.4%

Shareholders' Equity       $330,000     $275,000       +20.0%

KEY RATIOS:
  Current Ratio: 195/85 = 2.3x (healthy)
  D/E Ratio: 130/330 = 0.39x (moderate)
  Interest Coverage: 65/10 = 6.5x (adequate but declining)

RED FLAGS:
- Cash declined 33% while revenue grew 11% -- where is the cash going?
- Receivables up 38.5% vs revenue up 11.1% -- collection problems?
- Inventory up 36.4% vs revenue up 11.1% -- demand slowing?
- Goodwill doubled -- made a $50,000 acquisition (was it wise?)
- Long-term debt up 44.4% -- borrowed to fund the acquisition?
```

```
CASH FLOW STATEMENT
                              2025         2024
                              ----         ----
Net Income                  $41,250      $44,250

Operating Adjustments:
  D&A                        20,000       18,000
  Increase in Receivables   (25,000)     (10,000)
  Increase in Inventory     (20,000)      (8,000)
  Increase in Payables        8,000        5,000
Cash from Operations        $24,250      $49,250    <-- DOWN 51%!

Investing:
  Capital Expenditures      (50,000)     (35,000)
  Acquisition               (50,000)          --
Cash from Investing       ($100,000)    ($35,000)

Financing:
  New Long-Term Debt         60,000       10,000
  Dividends Paid            (15,000)     (15,000)
  Share Buybacks            (10,000)          --
Cash from Financing         $35,000      ($5,000)

Net Change in Cash         ($40,750)      $9,250
+ Beginning Cash             45,000       35,750
                           --------     --------
  ENDING CASH SHOULD BE:    $4,250       $45,000

Wait -- the Balance Sheet shows $30,000 in Cash, not $4,250!
(In a real analysis, other adjustments would reconcile this.
 For our teaching example, note the directional concern:
 cash is declining sharply.)

CRITICAL FINDING:
  Net Income:           $41,250  (looks okay)
  Cash from Operations: $24,250  (much lower -- quality concern!)
  Free Cash Flow:       $24,250 - $50,000 = ($25,750) NEGATIVE!

  The company is reporting profit but BURNING CASH.
  Receivables and inventory are soaking up cash.
  The acquisition consumed $50,000.
  They had to borrow $60,000 to fund it all.

VERDICT: Widget Corp has growing revenue but deteriorating
fundamentals. Margins are compressing, working capital is
ballooning, and the company is borrowing to fund an
acquisition while free cash flow has turned negative.
This stock needs further investigation before buying.
```

---

### c) Common Misconceptions

**Misconception 1: "If a company has positive net income, it is doing well."**

Reality: Net income is an accounting concept, not a cash concept. A company can report profits while actually burning cash. Enron reported billions in profits while its cash flows were deeply negative. Always cross-reference net income with cash from operations. If cash from operations is consistently and significantly below net income, the quality of those earnings is questionable.

**Misconception 2: "Revenue growth is always good."**

Reality: Revenue growth is only good if it comes with acceptable margins and is ultimately converted to cash. A company that grows revenue 20% but sees margins decline from 15% to 5% is actually destroying value as it grows. Similarly, a company that grows revenue by extending increasingly generous credit terms (sell now, collect maybe later) is booking revenue that may never convert to cash.

**Misconception 3: "A strong balance sheet means lots of assets."**

Reality: A strong balance sheet means the right composition of assets, manageable liabilities, and adequate equity. A company with $10 billion in assets but $9.5 billion in liabilities has a weak balance sheet despite having enormous assets. Asset quality matters too -- $100 million in cash is very different from $100 million in goodwill. Cash is guaranteed to be worth $100 million; goodwill might need to be written down to zero.

**Misconception 4: "Depreciation is just an accounting fiction -- ignore it."**

Reality: While depreciation is a non-cash charge (which is why we add it back on the cash flow statement), it represents real economic cost. Equipment wears out. Factories age. Technology becomes obsolete. A company must eventually spend real cash to replace depreciated assets. Ignoring depreciation means ignoring the ongoing capital needs of the business. This is exactly why free cash flow (which subtracts capital expenditures) is a better measure than EBITDA for assessing a company's true cash generation.

**Misconception 5: "The balance sheet shows what a company is truly worth."**

Reality: The balance sheet shows historical cost (adjusted for depreciation), not current market value. A piece of land bought for $1 million in 1980 might be worth $50 million today, but the balance sheet still shows it near its historical cost. Conversely, a patent valued at $10 million on the balance sheet might be worthless if the technology has been superseded. Book value is a starting point for analysis, not the answer.

**Misconception 6: "Financial statements tell you everything about a company."**

Reality: Financial statements are backward-looking and limited to what accounting standards require. They do not capture many of the most important aspects of a business: the quality of management, employee morale, competitive positioning, brand strength, customer loyalty, or industry trends. They are necessary but not sufficient for investment analysis. This is why reading the Management Discussion and Analysis (MD&A) section and understanding the business qualitatively is just as important as the numbers.

---

### d) Common Questions and Answers

**Q1: Where do I find a company's financial statements?**

A: For US-listed companies, all financial statements are filed with the Securities and Exchange Commission (SEC) and are freely available at sec.gov through the EDGAR system. Look for the 10-K (annual report) and 10-Q (quarterly report). Most companies also publish financial statements on their investor relations webpage. Financial data aggregators like Yahoo Finance, Google Finance, and Morningstar provide summarized versions, but for serious analysis, read the actual filings.

**Q2: What is the difference between the 10-K and the annual report?**

A: The 10-K is the official filing with the SEC and is comprehensive but plain -- all substance, no style. The annual report (often called the glossy annual report) is a separate publication aimed at shareholders that typically includes a letter from the CEO, photos, and marketing-style presentation alongside the financial statements. The 10-K is what analysts rely on. It contains the financial statements plus detailed footnotes, risk factors, management discussion and analysis (MD&A), and other required disclosures.

**Q3: How do I know if a company's accounting is aggressive or conservative?**

A: Several indicators help. Compare cash from operations to net income -- if net income consistently exceeds cash from operations, the company may be using aggressive accruals. Check the footnotes for revenue recognition policies -- does the company recognize revenue up front or over time? Look at how it handles capitalization versus expensing -- capitalizing costs (putting them on the balance sheet) inflates short-term profits, while expensing them (putting them on the income statement) is more conservative. Look for frequent changes in accounting estimates or policies. And compare the company's margins and ratios to its closest peers -- if one company's margins are significantly higher than every competitor, ask why.

**Q4: What is EBITDA and why do people use it?**

A: EBITDA stands for Earnings Before Interest, Taxes, Depreciation, and Amortization. It is a rough proxy for operating cash flow that strips out financing decisions (interest), jurisdictional differences (taxes), and non-cash charges (depreciation and amortization). Analysts use it because it allows apples-to-apples comparison between companies with different capital structures, tax situations, and depreciation methods. However, EBITDA has serious limitations -- it ignores the real cost of replacing depreciated assets and the real obligation to pay interest and taxes. Warren Buffett has famously criticized EBITDA, asking "Does management think the tooth fairy pays for capital expenditures?"

**Q5: What does "goodwill impairment" mean and why should I care?**

A: Goodwill impairment is a writedown of previously recorded goodwill, typically triggered when the acquired business is worth less than what was paid for it. It means the company's past acquisition overpaid. While the impairment charge itself is non-cash (it does not affect current cash flow), it is a powerful signal about management quality. A company that repeatedly writes down goodwill is telling you that management destroys value through acquisitions -- they pay too much and cannot integrate effectively. This should make you skeptical of future acquisitions.

**Q6: How is Financial Statement Analysis tested on the CFA exam?**

A: At CFA Level I, FSA covers the mechanics of all three statements, key ratios, revenue recognition, inventory accounting, long-lived assets, income taxes, and financial reporting quality. At Level II, it goes deeper into advanced topics like intercorporate investments, employee compensation, multinational operations, and evaluating financial reporting quality (detecting manipulation). At Level III, FSA is integrated into portfolio management and security analysis rather than tested as a standalone topic. Overall, FSA typically represents 13-15% of the Level I exam and a significant portion of Level II.

**Q7: Should I focus on quarterly or annual financial statements?**

A: Both have value. Annual statements (10-K) provide the most comprehensive data and are audited, making them more reliable. Quarterly statements (10-Q) are more timely and let you track trends during the year, but they are only reviewed (not audited) and may contain seasonal distortions. For most long-term investors, annual statements are the primary focus, with quarterly statements used to monitor for significant changes or emerging trends between annual reports.

**Q8: What is the most common way companies manipulate earnings?**

A: The most common methods include: aggressive revenue recognition (booking revenue before it is truly earned), capitalizing expenses that should be expensed (inflating reported profits), managing reserves and provisions (creating "cookie jar" reserves in good years and releasing them in bad years to smooth earnings), and channel stuffing (shipping excess product to distributors at period end to boost reported revenue). The antidote is always the same: compare reported earnings to cash from operations. Cash is much harder to fake than accounting earnings.

**Q9: What does negative shareholders' equity mean?**

A: Negative equity means the company's liabilities exceed its assets (on the balance sheet). This can signal severe financial distress, or it can reflect aggressive financial engineering. Some highly profitable companies like McDonald's and Starbucks have negative book equity because they have used so much debt to buy back shares that accumulated buybacks exceed retained earnings. In these cases, negative equity is not a sign of distress but of confidence in future cash flows. Context matters: a consistently profitable company with negative equity from buybacks is very different from an unprofitable company with negative equity from accumulated losses.

**Q10: How do I learn to read financial statements better?**

A: Practice is the only answer. Pick a company you know well -- perhaps one whose products you use daily -- and read its latest 10-K filing from start to finish. Calculate the key ratios yourself. Then pick a competitor and compare. Repeat this process with companies in different industries (a bank, a retailer, a software company, a manufacturer). Each industry has its own financial statement quirks, and exposure to diverse companies is the fastest way to build fluency. The CFA Level I curriculum is also an excellent structured learning resource even if you do not plan to take the exam.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 8: Reading Financial Statements - Basics"]

**Horace:** Welcome back everyone. Today we are learning one of the most fundamental skills in all of investing -- how to read financial statements. If last week was about the discipline of rebalancing, this week is about developing the ability to actually understand what a company is doing with its money. And I promise you, once you learn this, you will never look at a stock the same way again.

**Stella:** I will be honest, Horace. Financial statements sound intimidating. When I see those huge tables of numbers in an annual report, my eyes glaze over. Where do I even start?

**Horace:** Here is the good news. There are only three financial statements you need to understand, and each one answers a simple question. The income statement answers: "Did the company make money?" The balance sheet answers: "What does the company own and owe right now?" And the cash flow statement answers: "Where did the cash actually come from, and where did it go?"

**Stella:** Three statements, three questions. I can handle that.

**Horace:** Good. And here is the even better news -- you do not need to understand every line item on day one. You need to understand the structure, know where to look for the important numbers, and most importantly, understand how the three statements connect to each other. That is what we are going to do today.

[VISUAL: Three side-by-side document icons labeled "Income Statement," "Balance Sheet," and "Cash Flow Statement," with their key questions displayed beneath each one]

**Stella:** Let us start at the beginning. The income statement.

**Horace:** The income statement -- also called the profit and loss statement, or P&L -- shows the company's financial performance over a period of time. Usually a quarter or a year. Think of it as a movie, not a photograph. It captures everything that happened between two dates.

**Stella:** And it starts with revenue at the top?

**Horace:** Exactly. Revenue, also called sales or the "top line," is the total amount the company earned from selling its products or services. Then you subtract costs, layer by layer, until you get to net income at the bottom -- which is why net income is called the "bottom line."

[ANIMATION: animation/week08_three_statements.py - Animated waterfall chart building the income statement from top to bottom. Starting with a tall Revenue bar, then sequentially subtracting COGS (the bar shrinks), operating expenses (shrinks more), interest (shrinks slightly), and taxes (shrinks again) to arrive at the final Net Income bar. Each subtraction is animated with the expense amount visually "cutting" from the revenue bar, and margin percentages appear alongside each level.]

**Stella:** What are the layers of costs?

**Horace:** The first and usually largest is Cost of Goods Sold, or COGS. This is the direct cost of producing whatever the company sells -- raw materials, factory labor, shipping. Revenue minus COGS gives you gross profit.

**Stella:** And gross margin is gross profit divided by revenue?

**Horace:** Right. A company with $1 million in revenue and $600,000 in COGS has a gross profit of $400,000 and a gross margin of 40%. That 40% tells you that for every dollar of revenue, 40 cents is left after covering the direct costs of production.

**Stella:** What is a good gross margin?

**Horace:** It depends entirely on the industry. Software companies often have gross margins of 70-85% because the cost of producing one more copy of software is nearly zero. Grocery retailers might have gross margins of 25-30% because they are selling physical goods with thin markups. The key is to compare within the same industry and to watch the trend over time. If gross margin is declining, it usually means either input costs are rising or the company is being forced to cut prices due to competition.

[VISUAL: Bar chart showing typical gross margins by industry -- Software 75%, Pharmaceuticals 65%, Consumer Staples 40%, Retail 30%, Grocery 25%]

**Stella:** After gross profit, what comes next?

**Horace:** Operating expenses -- the costs of running the business beyond producing the product. This includes Selling, General and Administrative expenses (SG&A), Research and Development (R&D), and Depreciation and Amortization (D&A). Subtract these from gross profit and you get operating income, also called EBIT -- Earnings Before Interest and Taxes.

**Stella:** Why is operating income important?

**Horace:** Because it shows how profitable the core business operations are, before considering how the company is financed (interest) or where it is located (taxes). Two identical businesses with different amounts of debt will have different net incomes but similar operating incomes. Operating margin -- EBIT divided by revenue -- is one of the most useful metrics for comparing companies.

**Stella:** Then below operating income?

**Horace:** You subtract interest expense -- the cost of borrowed money -- and then taxes. What is left is net income, the famous bottom line. This is what is available for shareholders, either to be paid as dividends or reinvested in the business.

**Stella:** And Earnings Per Share is just net income divided by the number of shares outstanding?

**Horace:** Exactly. If a company earns $100 million in net income and has 50 million shares outstanding, EPS is $2.00. That is the number you see in earnings reports and the denominator in the P/E ratio.

[VISUAL: Complete income statement example with all major line items, margins calculated and displayed on the right side, with arrows pointing from key items to their corresponding margin calculations]

**Stella:** Got it. Now the balance sheet. This one always confuses me.

**Horace:** The balance sheet is actually elegant once you understand the fundamental equation. Assets equals Liabilities plus Shareholders' Equity. Everything the company owns, everything it owes, and the difference belongs to shareholders. This equation always balances -- that is literally why it is called a balance sheet.

**Stella:** Can you give me a real-world analogy?

**Horace:** Sure. Think about your personal finances. Your assets are your house, your car, your savings account. Your liabilities are your mortgage, your car loan, your credit card balance. Your equity -- your net worth -- is the difference. If you own a $500,000 house with a $300,000 mortgage, your equity in the house is $200,000.

[VISUAL: Split screen showing a personal balance sheet (house, car, bank account on left; mortgage, car loan on right; net worth at bottom) transitioning to a corporate balance sheet with the same structure]

**Stella:** That makes sense. So a company with $1 billion in assets and $600 million in liabilities has $400 million in equity.

**Horace:** Exactly. And that $400 million in equity is the book value of the company -- what accountants say it is worth. The stock market might value it at more or less than book value, which is why the Price-to-Book ratio exists. But that is a Week 21 topic.

**Stella:** What is the difference between current and non-current on the balance sheet?

**Horace:** Great question. Current means within one year. Current assets are things that will be converted to cash within a year -- like accounts receivable (money customers owe you), inventory (products waiting to be sold), and of course cash itself. Current liabilities are obligations due within a year -- like accounts payable (money you owe suppliers) and short-term debt.

**Stella:** And non-current is everything longer term?

**Horace:** Right. Non-current assets include things like property, factories, equipment -- the long-lived assets that support the business for years. Non-current liabilities are mainly long-term debt -- bonds and loans that mature more than a year out.

[VISUAL: Balance sheet diagram with current assets and liabilities highlighted at the top, non-current items below, with a timeline showing "within 1 year" versus "beyond 1 year" to illustrate the distinction]

**Stella:** Why does the current versus non-current distinction matter?

**Horace:** Because it tells you about the company's short-term financial health. If current liabilities exceed current assets, the company might struggle to pay its bills. The current ratio -- current assets divided by current liabilities -- is a quick health check. Above 1.5 is generally comfortable. Below 1.0 means the company may not be able to cover its short-term obligations without additional financing.

**Stella:** That sounds like a critical thing to check.

**Horace:** It is. Plenty of companies have gone bankrupt not because they were unprofitable, but because they ran out of cash to pay bills that came due. Profitable companies can die of illiquidity. This is why the balance sheet matters even for companies with strong income statements.

**Stella:** Okay, now the third statement -- cash flow. You mentioned this is the most important one?

**Horace:** Many experienced investors consider it the most important, and I agree. Here is why. The income statement uses something called accrual accounting. That means revenue is recorded when it is earned, not when cash is received. Expenses are recorded when incurred, not when cash is paid. This creates a gap between accounting profits and actual cash.

[VISUAL: Two timelines showing the same transaction -- the income statement records the sale when goods are delivered, but the cash flow statement records it when payment is received weeks later]

**Stella:** Can you give me an example of why that matters?

**Horace:** Sure. Imagine a company sells $10 million worth of products in December but gives customers 90 days to pay. On the December income statement, it books $10 million in revenue and reports a nice profit. But the cash? The cash does not arrive until March. On December 31st, the company has a healthy income statement but might not have enough cash to pay its January bills.

**Stella:** So a company can be profitable on paper but broke in reality?

**Horace:** Exactly. And this is not hypothetical. Many fast-growing companies have gone bankrupt precisely because of this dynamic. They grew so fast that their cash was tied up in receivables and inventory, and they could not pay their obligations even though the income statement showed profits.

**Stella:** That is scary. So the cash flow statement shows what is really happening with the cash?

**Horace:** It does. And it has three sections. Operating activities, investing activities, and financing activities.

[ANIMATION: animation/week08_three_statements.py - Animated funnel diagram showing cash flowing through the three sections. Cash from operations flows in at the top (green), then investing activities show cash flowing out for equipment and acquisitions (red arrows going down), then financing activities show debt and equity flows (blue arrows both directions). The remaining cash at the bottom updates a running cash balance counter that matches the balance sheet.]

**Horace:** Operating activities start with net income from the income statement and then adjust for all the non-cash items and working capital changes. You add back depreciation because it is a non-cash charge -- the company did not actually write a check for depreciation. You subtract increases in receivables because that revenue has not been collected as cash yet. You subtract increases in inventory because the company spent cash buying inventory.

**Stella:** So operating cash flow is the real cash the business generated from its operations?

**Horace:** Exactly. And here is the key test: if operating cash flow is consistently well above net income, that is a sign of high-quality earnings. The company is generating real cash, not just accounting profits. If operating cash flow is consistently below net income, red flag. Something in the accounting is creating profits that do not translate to cash.

**Stella:** What about the investing section?

**Horace:** Investing activities show cash spent on or received from long-term assets. The biggest item is usually capital expenditures -- buying property, equipment, or technology. This section is usually negative, which is fine -- it means the company is investing in its future. If it is positive, it often means the company is selling assets, which could be strategic or could be a sign of distress.

**Stella:** And financing activities?

**Horace:** Financing shows cash flows between the company and its investors and lenders. Taking on new debt or issuing new stock brings cash in. Paying off debt, paying dividends, or buying back shares sends cash out.

[VISUAL: Three-column summary with icons: Operating (factory/gear icon) = "Cash from running the business," Investing (building/plant icon) = "Cash for building the future," Financing (handshake icon) = "Cash between company and capital providers"]

**Stella:** Now here is something I have been reading about -- free cash flow. How does that fit in?

**Horace:** Free cash flow is the single most important number for investors. It is cash from operations minus capital expenditures. Think of it as the cash left over after the company has paid all its operating expenses and invested in maintaining and growing its assets.

**Stella:** Why is it so important?

**Horace:** Because free cash flow is the money that is truly available for shareholders. It can be used to pay dividends, buy back shares, pay down debt, make acquisitions, or simply build a cash reserve. Companies with strong, growing free cash flow are the ones that can reward shareholders over the long term. Companies with weak or negative free cash flow are either in growth mode (spending heavily to build the business) or in trouble.

**Stella:** How can I tell the difference between "good negative FCF" from growth spending and "bad negative FCF" from problems?

**Horace:** Great question. Look at what is driving the negative FCF. If it is heavy capital expenditure or R&D investment in a company with strong revenue growth and expanding addressable market, that can be good -- they are investing in future cash flows. Amazon had negative free cash flow for years while building its logistics network and AWS infrastructure, and that turned out to be brilliantly invested money. But if FCF is negative because operating cash flow itself is weak -- meaning the existing business is not generating cash -- that is a serious concern regardless of how much they are spending on growth.

[VISUAL: Side-by-side comparison: "Good Negative FCF" (strong operating cash flow minus large capex for growth) versus "Bad Negative FCF" (weak operating cash flow, business itself is burning cash)]

**Stella:** Can you show me how the three statements connect to each other? That is the part I find most confusing.

**Horace:** This is the most important concept in all of financial statement analysis. Let me walk you through it.

[ANIMATION: animation/week08_three_statements.py - Animated diagram showing all three statements side by side with animated arrows showing the connections between them. Net Income flows from the Income Statement to both the Balance Sheet (Retained Earnings) and the Cash Flow Statement (starting point). The Cash Flow Statement's ending cash balance updates the Cash line on the Balance Sheet. Depreciation reduces PP&E on the Balance Sheet while being added back on the Cash Flow Statement. New debt appears in Financing Activities and increases Liabilities on the Balance Sheet.]

**Horace:** Start with the income statement. Net income -- the bottom line -- flows to two places. First, it flows to the balance sheet. Specifically, it increases Retained Earnings, which is part of shareholders' equity. This makes sense -- if the company earned money, the shareholders' claim on the business grew.

**Stella:** And the second place?

**Horace:** Net income is also the starting point of the cash flow statement, under the indirect method, which is what most companies use. From there, you make adjustments to reconcile accounting profit with actual cash flow. And the ending cash balance from the cash flow statement becomes the cash line item on the balance sheet.

**Stella:** So the cash flow statement is the bridge between the income statement and the balance sheet?

**Horace:** That is a brilliant way to think about it. The income statement tells a story in accrual accounting terms. The cash flow statement translates that story into cash terms. And the balance sheet is the cumulative snapshot that reflects everything that has happened.

**Stella:** Can you walk me through a specific example?

**Horace:** Let us say a company makes a sale on credit for $10,000. The product cost $6,000. On the income statement: revenue goes up $10,000, COGS goes up $6,000, and profit increases by $4,000. On the balance sheet: accounts receivable goes up $10,000 (the customer owes us), inventory goes down $6,000 (we shipped the product), and retained earnings goes up $4,000 (the profit). On the cash flow statement: net income shows the $4,000 profit, but then we subtract $10,000 for the increase in receivables and add back $6,000 for the decrease in inventory. Net cash impact: zero.

**Stella:** Zero? The company made a $4,000 profit but got zero cash?

**Horace:** Exactly. No cash changes hands until the customer actually pays. The income statement says "we made money." The cash flow statement says "but we have not collected it yet." This is why you need both statements. One without the other gives you an incomplete and potentially misleading picture.

[VISUAL: The $10,000 credit sale traced through all three statements simultaneously, with the key insight "Profit does not equal cash!" highlighted]

**Stella:** That is an incredible example. Now I understand why people say the cash flow statement is the truth detector.

**Horace:** It is. And here is a rule of thumb that will serve you well for your entire investing career: when the income statement and the cash flow statement tell different stories, trust the cash flow statement. Cash does not lie.

**Stella:** Let us talk about ratios. I see these mentioned all the time -- current ratio, ROE, debt-to-equity. What are the essential ones?

**Horace:** There are four categories of ratios you should know. Profitability ratios tell you how effectively the company converts revenue into profit. Liquidity ratios tell you whether the company can pay its short-term bills. Leverage ratios tell you how much debt the company is carrying. And efficiency ratios tell you how well the company manages its assets.

[VISUAL: Four quadrants labeled Profitability, Liquidity, Leverage, and Efficiency, each with their key ratios listed]

**Horace:** For profitability, the most important is Return on Equity -- ROE. It measures how much profit the company generates for each dollar of shareholder equity. An ROE of 15% means the company generates $15 of profit for every $100 of shareholder investment. Above 15% is generally good. Above 20% is excellent. Below 10% may suggest the company is not using shareholders' capital efficiently.

**Stella:** But I have heard ROE can be misleading?

**Horace:** Very perceptive. This is where the DuPont decomposition comes in. ROE equals profit margin times asset turnover times financial leverage. A company can have a high ROE for three very different reasons: it has great margins, it uses assets efficiently, or it has a lot of debt. The first two are healthy. The third is risky.

**Stella:** So two companies with the same 20% ROE might be very different?

**Horace:** Exactly. Company A might have 20% ROE because it has a 10% profit margin and turns over its assets efficiently. Company B might have 20% ROE because it is leveraged to the hilt with debt. If a recession hits, Company A is fine. Company B might face a debt crisis. The DuPont decomposition reveals which type of ROE you are dealing with.

[VISUAL: DuPont framework showing ROE broken into three components, with two different companies achieving the same ROE through different combinations]

**Stella:** What about those red flags you mentioned in the reading? What should scare me when I look at financial statements?

**Horace:** The number one red flag is a persistent divergence between net income and cash from operations. If the company keeps reporting profits but cash flow keeps declining or is negative, something is not right. The profits may be accounting-driven rather than real.

**Stella:** What causes that divergence?

**Horace:** Several things. Accounts receivable growing faster than revenue -- the company is booking sales but not collecting cash. Inventory building up faster than revenue -- the company is producing products it cannot sell. Capitalizing expenses -- putting costs on the balance sheet as "assets" instead of running them through the income statement as expenses. All of these inflate reported profit while draining cash.

**Stella:** Can you give me a real-world example?

**Horace:** Think about a company that is "stuffing the channel" -- shipping huge quantities of product to distributors at the end of every quarter to hit revenue targets. The distributors have not sold the product to actual customers, but the company books it as revenue. Receivables balloon. Inventory at the distributors piles up. Eventually, the distributors stop ordering, the music stops, and revenue collapses. This exact pattern has been seen in companies from pharmaceutical firms to tech hardware companies.

[VISUAL: Chart showing revenue line steadily climbing while accounts receivable line climbs even faster, with the gap highlighted as a warning sign]

**Stella:** Another red flag you mentioned was frequent "one-time" charges. What is that about?

**Horace:** This is one of my favorites. Some companies report "one-time" restructuring charges almost every single year. They present adjusted earnings that exclude these charges, making profitability look much better than the GAAP earnings. But if a company has a "one-time" charge every year for ten years, it is not one-time -- it is a recurring cost of doing business that management is trying to sweep under the rug.

**Stella:** So I should be skeptical of adjusted earnings?

**Horace:** Always compare adjusted earnings to GAAP earnings and to cash from operations. If adjusted earnings are significantly higher than both GAAP earnings and operating cash flow, management may be painting too rosy a picture.

**Stella:** Let me try to put this all together with a practical exercise. If I am looking at a stock for the first time, what is my checklist?

**Horace:** Great idea. Here is my framework.

[VISUAL: Numbered checklist appearing one item at a time as Horace describes each step]

**Horace:** Step one: check revenue trends. Is revenue growing? How fast? Is growth accelerating or decelerating? Step two: check margin trends. Are gross, operating, and net margins stable, expanding, or contracting? Step three: look at the balance sheet. Is debt reasonable relative to equity? Is the current ratio above 1.5? How much cash is on hand? Step four: check cash from operations versus net income. Are they in the same ballpark, or is there a big gap? Step five: calculate free cash flow and the FCF yield. Is the company generating real cash after capital expenditures? Step six: look for red flags -- rapidly growing receivables or inventory, frequent one-time charges, declining cash despite reported profits.

**Stella:** That is a solid framework. How long does it take to do this analysis?

**Horace:** Once you have practice, you can do a preliminary screen in about 15-20 minutes per company. The deep dive -- reading the full 10-K, understanding the footnotes, comparing to peers -- might take several hours. But even the quick screen will catch the most obvious problems and opportunities.

**Stella:** Let us talk about something from the CFA perspective. What is this "quality of earnings" concept?

**Horace:** Quality of earnings is one of the most important concepts in the CFA curriculum and in professional investing. It asks: how reliable and sustainable are the reported profits? High-quality earnings are backed by cash, come from the company's core business, and are likely to continue in the future. Low-quality earnings are driven by accounting choices, one-time events, or aggressive assumptions.

**Stella:** How do I assess quality?

**Horace:** The simplest test is the accruals ratio. Take net income, subtract cash from operations, and divide by average total assets. A low or negative accruals ratio means earnings are mostly cash-backed -- high quality. A high accruals ratio means earnings are driven by non-cash accounting items -- lower quality. Academic research has shown that companies with high accruals ratios tend to underperform in subsequent years.

[VISUAL: Formula for accruals ratio with examples of high-quality (low ratio) and low-quality (high ratio) companies, with subsequent stock performance shown]

**Stella:** That is a powerful tool. One more question -- you mentioned IFRS versus GAAP. Does it matter for regular investors?

**Horace:** It matters if you invest internationally. US companies report under US GAAP. Most of the rest of the world uses International Financial Reporting Standards, or IFRS. The two systems are broadly similar but differ in important details. For example, under US GAAP, a company can use LIFO (Last In, First Out) for inventory, which can significantly affect reported profits during inflationary periods. IFRS does not allow LIFO. When comparing a US company to a European competitor, you need to be aware of these differences.

**Stella:** Do I need to memorize all the differences?

**Horace:** No. Just be aware that they exist and be cautious when comparing companies that report under different standards. When in doubt, focus on cash-flow-based metrics, which are less affected by accounting standard differences.

[VISUAL: Simple comparison table showing the three most important GAAP vs. IFRS differences: inventory methods, development cost treatment, and lease accounting]

**Stella:** Before we wrap up, can you walk me through what a quick analysis looks like in practice? Maybe give me a company scenario?

**Horace:** Absolutely. Let me give you Widget Corp from the reading. Revenue grew 11% -- looks good on the surface. But gross margin declined from 46.7% to 45% -- costs are rising faster than revenue. Operating income actually fell 3% despite 11% revenue growth. And the cash flow statement is the real eye-opener: cash from operations dropped 51%, from $49,000 to $24,000. Receivables and inventory are both growing at more than three times the rate of revenue.

**Stella:** That sounds bad despite the revenue growth.

**Horace:** Exactly. And when you calculate free cash flow -- cash from operations of $24,000 minus capital expenditures of $50,000 -- it is negative $26,000. The company is burning cash. They covered the shortfall by borrowing $60,000 in new long-term debt. Revenue growth is masking fundamental deterioration in the business.

**Stella:** So on the surface it looks like a growing company, but underneath it is a company borrowing money to paper over declining profitability and cash flow problems.

**Horace:** That is exactly right. And this is why you need all three statements. The income statement alone says "growing company." The balance sheet raises questions about rising debt, receivables, and inventory. The cash flow statement reveals the truth: this business is not generating cash from its operations.

[VISUAL: Three-panel dashboard showing Widget Corp's income statement (green arrow for revenue growth), balance sheet (yellow warning for rising debt and receivables), and cash flow statement (red alert for negative FCF), with an overall verdict: "Proceed with extreme caution"]

**Stella:** This whole lesson has been an eye-opener. If I had to remember three things from today, what would they be?

**Horace:** First, always look at all three financial statements together. The income statement, balance sheet, and cash flow statement each tell part of the story, and the connections between them reveal the full picture. Second, when in doubt, follow the cash. Cash from operations is the most reliable indicator of a company's financial health because it is the hardest number to manipulate. Third, watch the trends, not just the absolute numbers. A single year's financial statements tell you where the company is; multiple years of statements tell you where it is going.

**Stella:** Perfect. So to summarize: the income statement tells me if the company made money, the balance sheet tells me what it owns and owes, and the cash flow statement tells me whether the profits are real by showing where the cash actually went. And I should never look at any one of them without the other two.

**Horace:** That is an excellent summary. You are now equipped to do something most investors never bother to do -- actually read the financial statements before buying a stock. It is like reading the inspection report before buying a house. It will not guarantee a good outcome, but it will help you avoid the worst disasters.

[VISUAL: Summary card with three key takeaways:
1. All three financial statements tell one interconnected story -- read them together
2. When earnings and cash flow diverge, trust the cash flow
3. Watch trends over multiple years, not just single snapshots]

**Stella:** Next week, we are going to dive into the world of investing psychology and behavioral finance. Why do smart people make dumb investment decisions? And how can we protect ourselves from our own worst instincts?

**Horace:** It is going to be fascinating. See you then.

**Stella:** Thanks everyone for watching!

[VISUAL: End screen with subscribe button and links to previous lessons]

---
