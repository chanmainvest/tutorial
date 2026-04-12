<!-- 此檔案需要翻譯為台灣繁體中文 -->
<!-- This file needs translation to TW Traditional Chinese -->

# Week 19: Corporate Finance - Capital Structure, WACC, Dividends, and Governance

---

## Reading Section

### a) Why This Is Important

Every publicly traded company makes a continuous stream of financial decisions that directly affect the value of your investment. How much debt should the company take on? Should it pay a dividend or buy back shares? How should it allocate capital between growth investments, acquisitions, and returning cash to shareholders? These are corporate finance decisions, and understanding them transforms you from a passive stock price watcher into someone who can evaluate whether management is creating or destroying value.

Consider this contrast. Company A earns $1 billion in profit. Its management uses $400 million to invest in a new product line with a 25% expected return, returns $400 million to shareholders through buybacks at a reasonable valuation, and holds $200 million in cash for flexibility. Company B also earns $1 billion. Its management acquires a competitor for $800 million at an inflated price (the CEO wanted a bigger empire), pays the board excessive compensation, and issues more shares to fund the acquisition, diluting existing shareholders. Both companies earned the same profit. But Company A is building long-term value while Company B is destroying it.

Here is why corporate finance knowledge is essential for every investor:

1. **Capital allocation is the CEO's most important job.** Over a 10-year period, a company making $1 billion annually will deploy $10 billion in capital. How intelligently that money is deployed determines far more of your return than quarter-to-quarter earnings beats. Warren Buffett has said that after ten years in a job, a CEO whose company retains earnings of $10 per share should have created at least $10 of market value -- if not, the capital was misallocated.

2. **Capital structure affects risk and return.** A company funded entirely by equity is safer but may be inefficient. A company loaded with debt is riskier but can magnify returns. Understanding this tradeoff helps you assess whether a company's financial structure is appropriate for its business model.

3. **Dividends and buybacks are how companies return value to you.** But not all return policies are created equal. Some dividend programs are sustainable and signal confidence. Others are funded by debt and are on the verge of being cut. Some buyback programs create enormous value. Others are egregious wastes of shareholder money, executed at inflated prices to offset dilution from executive stock compensation.

4. **Corporate governance protects you from management misbehavior.** The agency problem -- the conflict of interest between managers and shareholders -- is one of the most studied phenomena in finance. Understanding governance helps you identify companies where your interests as a shareholder are protected versus those where management is enriching itself at your expense.

This lesson covers the essential framework: how companies finance themselves, how to evaluate their capital allocation decisions, and how to identify the governance red flags that precede value destruction.

---

### b) What You Need to Know

#### 1. Capital Structure -- Debt vs. Equity

Every company finances its operations with some combination of debt (borrowed money) and equity (shareholders' money). The mix is called the capital structure, and it has profound implications for risk, return, and valuation.

```
CAPITAL STRUCTURE BASICS
==========================

                    TOTAL CAPITAL
                   /              \
                  /                \
            DEBT                  EQUITY
         (Borrowed)             (Ownership)
         /        \             /         \
     Bank       Bonds       Common      Retained
     Loans                  Stock       Earnings

DEBT vs. EQUITY COMPARISON
==============================

Feature          Debt              Equity
-------          ----              ------
Cost             Lower (tax        Higher (dividends
                 deductible)       not deductible)

Risk to firm     Higher (must      Lower (no mandatory
                 pay or default)   payments)

Investor claim   Senior (paid      Junior (paid last,
                 first)            bears losses first)

Tax treatment    Interest is        Dividends NOT
                 tax-deductible     deductible

Control          No voting          Voting rights
                 rights

Upside           Fixed return       Unlimited upside
                 (capped)           potential

EXAMPLE: TWO IDENTICAL BUSINESSES, DIFFERENT STRUCTURES
=========================================================

                    All-Equity Co.     Leveraged Co.
                    --------------     -------------
Total Assets:       $1,000,000         $1,000,000
Debt:               $0                 $500,000 @ 6%
Equity:             $1,000,000         $500,000

Operating Income:   $150,000           $150,000
Interest Expense:   $0                 $30,000
Pre-Tax Income:     $150,000           $120,000
Tax (25%):          $37,500            $30,000
Net Income:         $112,500           $90,000

Return on Equity:   11.25%             18.0%

Leveraged Co. has HIGHER ROE despite LOWER net income
because equity investors put up less capital.

But if operating income drops to $20,000:
                    All-Equity Co.     Leveraged Co.
                    --------------     -------------
Operating Income:   $20,000            $20,000
Interest Expense:   $0                 $30,000
Pre-Tax Income:     $20,000            -$10,000  LOSS!
Net Income:         $15,000            -$10,000

Return on Equity:   1.5%               -2.0%

Leverage magnifies both gains AND losses.
```

---

#### 2. The Modigliani-Miller Theorem -- The Starting Point

In 1958, Franco Modigliani and Merton Miller proved that in a perfect world (no taxes, no bankruptcy costs, no information asymmetry), capital structure does not matter -- the total value of a firm is the same regardless of how it is financed. This might seem useless, but it is actually brilliant because it tells us exactly which real-world frictions make capital structure matter.

```
MODIGLIANI-MILLER AND THE REAL WORLD
=======================================

Perfect World (M&M):   Capital structure does not matter.
                        Total firm value is constant.

Real World Additions:

  + Tax Advantage of Debt
    Interest is tax-deductible, so debt creates
    a "tax shield" = Debt x Tax Rate
    --> Pushes toward MORE debt

  - Bankruptcy Costs
    Too much debt increases probability of
    financial distress (legal costs, lost
    customers, fire-sale asset values)
    --> Pushes toward LESS debt

  - Agency Costs
    Managers may use free cash flow wastefully;
    debt forces discipline (must make payments)
    --> Pushes toward MORE debt (sometimes)

  = OPTIMAL CAPITAL STRUCTURE
    Balances tax benefits against distress costs

OPTIMAL DEBT LEVEL (CONCEPTUAL)
==================================

  Firm Value
     ^
     |                     ****
     |                  ***    ****
     |               ***          ****
     |            ***                 ****
     |         ***                        ****
     |      ***          Tax              Bankruptcy
     |   ***          benefits            costs start
     |  *             increasing          dominating
     | *
     +*-----|------------|------------|-------> Debt/Equity
     0%    20%         50%          80%        Ratio

     Sweet spot: where marginal tax benefit
     = marginal increase in distress risk
     (typically 30-50% for mature companies)
```

---

#### 3. Weighted Average Cost of Capital (WACC)

WACC is the blended cost of all the capital a company uses. It is critically important because it is the hurdle rate for new investments -- any project must earn at least the WACC to create value for shareholders.

```
WACC FORMULA
==============

                E                D
WACC = Re x --------- + Rd x --------- x (1 - Tax Rate)
              E + D            E + D

Where:
  Re = Cost of equity (what shareholders require)
  Rd = Cost of debt (interest rate on borrowings)
  E  = Market value of equity
  D  = Market value of debt
  Tax Rate = Corporate tax rate

WORKED EXAMPLE
================

Company XYZ:
  Market cap (E):      $800 million
  Debt (D):            $200 million
  Cost of equity (Re): 10%
  Cost of debt (Rd):   5%
  Tax rate:            25%

  Equity weight: $800M / $1,000M = 80%
  Debt weight:   $200M / $1,000M = 20%

  WACC = (10% x 0.80) + (5% x 0.20 x 0.75)
       = 8.0% + 0.75%
       = 8.75%

Interpretation: Every project or investment this company
undertakes must earn AT LEAST 8.75% to create value.

If a project earns 12% --> Creates value (12% > 8.75%)
If a project earns 6%  --> Destroys value (6% < 8.75%)
```

**How Cost of Equity Is Estimated:**

```
COST OF EQUITY ESTIMATION (CAPM)
===================================

Re = Rf + Beta x (Rm - Rf)

Where:
  Rf = Risk-free rate (10-year Treasury yield)
  Beta = Stock's sensitivity to market movements
  Rm - Rf = Equity risk premium (~5-6% historically)

Example:
  Risk-free rate:       4.5%
  Beta:                 1.2
  Equity risk premium:  5.5%

  Re = 4.5% + 1.2 x 5.5% = 4.5% + 6.6% = 11.1%

WACC SENSITIVITY
==================

The WACC changes with capital structure:

Debt/Equity    Cost of     Cost of     WACC
Ratio          Equity      Debt
----------     --------    --------    ------
0% debt        9.0%        N/A         9.0%
20% debt       9.5%        4.0%        8.2%
40% debt       10.5%       4.5%        7.5%
60% debt       12.0%       5.5%        7.0%  <-- Minimum
80% debt       16.0%       8.0%        8.0%  (risk premium
                                              spikes)

Note: As debt increases, BOTH cost of equity AND cost of
debt rise (higher risk), but the tax shield initially
outweighs the higher costs. Past a point, distress risk
overwhelms the tax benefit and WACC rises again.
```

---

#### 4. Dividends -- Returning Cash to Shareholders

A dividend is a direct cash payment from the company to its shareholders, typically paid quarterly. Dividend policy is one of the most visible and closely watched corporate finance decisions.

```
DIVIDEND FUNDAMENTALS
=======================

KEY DATES IN A DIVIDEND CYCLE
-------------------------------

Declaration   Ex-Dividend   Record    Payment
Date          Date          Date      Date
  |              |            |          |
  |   Board      |  Must own  | Shares-  | Cash
  |   announces  |  BEFORE    | holder   | arrives
  |   dividend   |  this date | list     | in your
  |              |  to get    | finalized| account
  |              |  dividend  |          |
  v              v            v          v
 Day 1         Day 15       Day 16     Day 45

On the ex-dividend date, the stock price typically
DROPS by approximately the dividend amount.

DIVIDEND METRICS
==================

Metric              Formula                     Meaning
------              -------                     -------
Dividend Yield      Annual Div / Stock Price    Income return
Payout Ratio        Dividends / Net Income      % of earnings
                                                paid out
Retention Ratio     1 - Payout Ratio            % reinvested
                                                in business
Div. Growth Rate    Annual % increase in        Sustainability
                    dividend per share           signal
Div. Coverage       EPS / DPS                   Safety margin
                                                (higher = safer)
```

**Dividend Sustainability Analysis:**

```
IS THE DIVIDEND SAFE?
=======================

Healthy Dividend:
  Earnings per share:    $5.00
  Dividend per share:    $2.00
  Payout ratio:          40%
  Free cash flow/share:  $4.50
  FCF payout ratio:      44%
  Debt/EBITDA:           1.5x
  Dividend growth:       7% annually for 10 years
  Verdict:               SAFE -- well covered by earnings
                         and cash flow, room to grow

WARNING SIGNS:
  Payout ratio:          > 80%
  Dividend growth:       Stalled or cut
  FCF < Dividends:       Funding dividends with debt
  Rising debt levels:    Borrowing to maintain payout
  Cyclical business:     Earnings volatile but dividend fixed
  One-time items:        Earnings inflated by non-recurring gains

DANGEROUS DIVIDEND:
  Earnings per share:    $2.00
  Dividend per share:    $2.50
  Payout ratio:          125%  <-- Paying out more than earned!
  Free cash flow/share:  $1.80
  FCF payout ratio:      139%
  Debt/EBITDA:           4.5x
  Dividend growth:       0% for 3 years
  Verdict:               DIVIDEND CUT LIKELY

WHAT HAPPENS WHEN A DIVIDEND IS CUT
======================================

                    Stock Price
  $50 |  *****
      |       *
  $40 |        *
      |         *    <-- Dividend cut announced
  $30 |          ****
      |              *****
  $25 |                   *****   <-- New equilibrium
      |
      +--|--|--|--|--|--|--|--|--|-->
         Weeks before and after cut

Dividend cuts typically cause 20-30% price declines
because they signal management's lack of confidence
AND force income-seeking investors to sell.
```

---

#### 5. Share Buybacks -- The Other Way to Return Cash

A share buyback (or repurchase) is when a company buys its own shares on the open market or through a tender offer, reducing the number of shares outstanding. This increases each remaining shareholder's ownership percentage.

```
HOW BUYBACKS CREATE VALUE
============================

Before Buyback:
  Net Income:           $100 million
  Shares Outstanding:   100 million
  EPS:                  $1.00
  Stock Price:          $15.00
  P/E Ratio:            15x

Company uses $150 million to buy back 10 million shares:

After Buyback:
  Net Income:           $100 million  (unchanged)
  Shares Outstanding:   90 million    (reduced by 10%)
  EPS:                  $1.11         (increased by 11.1%)
  Stock Price:          $16.67        (at same 15x P/E)
  Shareholder gain:     +11.1% per share

BUYBACKS vs. DIVIDENDS COMPARISON
====================================

Feature              Buybacks              Dividends
-------              --------              ---------
Tax efficiency       Better (gains         Worse (taxed as
                     deferred, taxed       income in year
                     at capital gains      received)
                     rate when sold)

Flexibility          High (can stop        Low (cutting a
                     anytime with no       dividend is seen
                     stigma)               as a negative signal)

Signal               Ambiguous (could      Clearer (management
                     mean stock is cheap   commits to ongoing
                     or management has     payments)
                     no better ideas)

Price sensitivity    Matters a LOT         Matters less
                     (buying back at       (fixed per-share
                     high prices wastes    amount regardless
                     money)                of price)

Who benefits         All shareholders      All shareholders
                     (increased % owner-   (direct cash)
                     ship of the company)

Regularity           Irregular             Regular (quarterly)
```

**When Buybacks Destroy Value:**

```
GOOD BUYBACKS vs. BAD BUYBACKS
==================================

GOOD: Company trades at $30, intrinsic value is $50.
  Each buyback dollar buys $1.67 of value.
  Remaining shareholders gain from the discount.

BAD: Company trades at $50, intrinsic value is $30.
  Each buyback dollar buys only $0.60 of value.
  Remaining shareholders are harmed.

THE BUYBACK TRAP (Common Problem):

  Company generates $500M in free cash flow
  Company issues $200M in stock options to executives
  Company spends $300M on buybacks
  Net shares barely decrease

  The buyback is NOT returning cash to shareholders --
  it is merely offsetting the dilution from executive
  compensation. The executives got $200M of value.
  Shareholders got $100M less than they think.

CHECK: Is share count ACTUALLY declining?
  Year 1:  1,000M shares
  Year 2:    990M shares  ($500M buyback)
  Year 3:    985M shares  ($500M buyback)
  Year 4:    982M shares  ($500M buyback)

  $1.5 billion spent but only 1.8% share reduction!
  Where did the money go? Stock-based compensation.
```

---

#### 6. Capital Allocation Framework

The best CEOs are master capital allocators. They consistently deploy capital into the highest-returning opportunities and return the rest to shareholders. Here is how to evaluate capital allocation quality.

```
CAPITAL ALLOCATION DECISION TREE
===================================

Company generates Free Cash Flow
              |
              v
    +--------------------+
    | Can we invest in   |
    | projects with      |  YES --> Invest (organic growth,
    | returns > WACC?    |          R&D, capex)
    +--------------------+
              |
              NO
              v
    +--------------------+
    | Can we acquire     |
    | businesses at      |  YES --> Acquire (but be skeptical --
    | attractive prices? |          most acquisitions destroy value)
    +--------------------+
              |
              NO
              v
    +--------------------+
    | Is our stock       |
    | undervalued?       |  YES --> Buy back shares
    +--------------------+
              |
              NO
              v
    +--------------------+
    | Pay a dividend or  |  YES --> Return cash to shareholders
    | special dividend   |          (they can invest it better)
    +--------------------+

THE CAPITAL ALLOCATION SCORECARD
===================================

Metric                            Good         Bad
------                            ----         ---
Return on Invested Capital        > WACC       < WACC
  (ROIC)                          (creating    (destroying
                                   value)       value)

Acquisition track record          Disciplined, Overpaying,
                                  accretive    dilutive

Buyback price discipline          Buys below   Buys at any
                                  intrinsic    price to hit
                                  value        EPS targets

Dividend sustainability           Growing,     Funded by
                                  covered by   debt, payout
                                  FCF          > 100%

Management ownership              Meaningful   Trivial
                                  skin in the  (or selling
                                  game         shares)

Capital expenditure returns       ROIC > WACC  Empire building
```

---

#### 7. Corporate Governance and Agency Problems

Corporate governance is the system of rules, practices, and processes by which a company is directed and controlled. The central issue is the agency problem: managers (agents) may not always act in the best interest of shareholders (principals).

```
THE AGENCY PROBLEM
====================

Shareholders (Principals)     Managers (Agents)
-------------------------     -----------------
Want: maximize share value    Want: maximize personal
  and returns                   wealth, power, prestige

Want: disciplined capital     Want: empire building,
  allocation                    higher compensation

Want: transparency and        Want: information
  accountability                advantage, job security

Want: appropriate risk-       Want: either too little risk
  taking for growth             (job safety) or too much
                                (option-like compensation)

THE MISALIGNMENT
==================

         Shareholder Interest
              ^
              |        * Ideal (aligned)
              |       /
              |      /
              |     /
              |    /
              |   / <-- Good governance keeps
              |  /      interests aligned
              | /
              |/
              +------------------------------> Manager Interest

Without governance:
              ^
              |
              |                    * Manager
              |                   /  enrichment
              |                  /
              |                 /
              |                /
              |  * Shareholders
              |    get left
              |    behind
              +------------------------------> Manager Interest
```

**Key Governance Mechanisms:**

```
GOVERNANCE PROTECTION MECHANISMS
===================================

Mechanism                   How It Protects Shareholders
---------                   ----------------------------
Independent Board           Directors without management ties
                            can objectively oversee executives

Separation of               CEO should not also be Chairman
CEO/Chairman Roles          (who oversees the CEO?)

Executive Compensation      Pay should be tied to long-term
Alignment                   value creation, not short-term
                            stock price or earnings targets

Shareholder Voting Rights   One share, one vote allows
                            shareholders to influence decisions

Proxy Access                Shareholders can nominate their
                            own board candidates

Clawback Provisions         Executives must return compensation
                            if financial results are restated

Auditor Independence        External auditors free from
                            management influence

Whistleblower Protections   Employees can report misconduct
                            without fear of retaliation
```

**Red Flags in Corporate Governance:**

```
GOVERNANCE RED FLAGS
=====================

RED FLAG                           WHY IT MATTERS
--------                           ---------------
CEO is also Chairman               No one oversees the CEO

Board members serve 15+ years      Captured by management;
                                   not truly independent

Excessive executive pay relative   Extracting value rather
to performance                     than creating it

Dual-class share structure         Founders/insiders control
                                   votes with small economic
                                   stake (e.g., 10% ownership
                                   but 51% voting control)

Related-party transactions         Insider dealing; conflicts
                                   of interest

Frequent accounting restatements   Financial reporting
                                   unreliable

Board lacks financial expertise    Cannot effectively oversee
                                   complex financial decisions

Anti-takeover provisions           Entrenches management;
(poison pills, staggered boards)   blocks discipline of market
                                   for corporate control

Management selling shares          Insiders know bad news
aggressively                       is coming

Auditor changes                    Previous auditor may have
                                   raised concerns
```

---

#### 8. Mergers and Acquisitions -- Buyer Beware

M&A is one of the most significant corporate finance events, and research consistently shows that most acquisitions destroy value for the acquiring company's shareholders. Understanding why helps you evaluate M&A announcements.

```
M&A VALUE CREATION/DESTRUCTION
================================

Academic research on M&A outcomes:

  Target shareholders:    +15-30% premium on average
  Acquirer shareholders:  -1% to -5% on average
  Combined value:         Often NEGATIVE

WHY MOST ACQUISITIONS FAIL
=============================

1. Winner's Curse
   To win a bidding war, acquirer must pay MORE than
   anyone else thinks the target is worth.

2. Integration Difficulties
   Combining cultures, systems, and people is far
   harder and more expensive than projected.

3. Synergy Overestimation
   "We will save $500M in synergies" often becomes
   $200M after restructuring costs.

4. Empire Building
   CEOs want bigger companies (more prestige, higher
   pay) even if the acquisition is value-destructive.

5. Overpaying at Cycle Peaks
   Most M&A occurs late in economic expansions when
   prices are highest and optimism is greatest.

ACQUISITION WARNING SIGNS FOR INVESTORS
==========================================

   Concern                      What to Watch
   -------                      -------------
   Price paid                   > 15x EBITDA for mature business
   Funding method               100% debt or heavy stock dilution
   Strategic fit                Conglomerate diversification
   Management history           Serial acquirer, poor track record
   Timing                       Late in economic cycle
   Synergy claims               > 50% of deal premium
   "Transformational"           Management admits current
                                business is failing
```

---

### c) Common Misconceptions

**Misconception 1: "More debt is always bad."**

Reality: Moderate debt is actually beneficial for shareholders because interest is tax-deductible, creating a tax shield that reduces the effective cost of capital. A company with zero debt may be leaving value on the table. The key is whether the company can comfortably service its debt through economic cycles. A stable utility can safely carry more debt than a cyclical semiconductor company.

**Misconception 2: "Dividends are free money."**

Reality: On the ex-dividend date, the stock price drops by approximately the dividend amount. You are not receiving something for nothing -- value is being transferred from the company to your pocket. The stock price adjusts downward because the company's cash balance decreases by the dividend amount. Dividends are a return of capital, not a creation of wealth. Their value lies in discipline, signaling, and tax-efficient income distribution.

**Misconception 3: "Share buybacks are always good for shareholders."**

Reality: Buybacks are only good when conducted at prices below intrinsic value. When a company buys back shares at inflated prices, it is transferring wealth from remaining shareholders to departing shareholders. Furthermore, many buyback programs exist primarily to offset dilution from stock-based compensation, not to actually reduce share count. Always check whether the total share count is actually decreasing over time.

**Misconception 4: "A high dividend yield means a good investment."**

Reality: An unusually high dividend yield is often a warning sign, not a buying signal. The yield may be high because the stock price has fallen in anticipation of a dividend cut. This is called a "yield trap." A stock yielding 8% when its peers yield 3% often means the market expects the dividend to be slashed. Look at payout ratios, free cash flow coverage, and the trend in dividends before chasing yield.

**Misconception 5: "Good managers do not need governance oversight."**

Reality: Even well-intentioned managers face conflicts of interest and cognitive biases. Strong governance structures are not about distrust -- they are about creating systems that align incentives and provide checks and balances. The best companies have strong governance precisely because their leaders understand that structural alignment is more reliable than individual virtue.

**Misconception 6: "Companies should always reinvest profits rather than return them."**

Reality: Reinvestment only creates value if the return on investment exceeds the cost of capital. Many mature companies cannot find enough high-return projects to absorb all their profits. In such cases, returning cash to shareholders (via dividends or buybacks) is the best use of capital -- shareholders can then invest in higher-growth opportunities elsewhere. Hoarding cash or investing in low-return projects destroys value.

---

### d) Common Questions and Answers

**Q1: How do I determine a company's optimal capital structure?**

A: Look at comparable companies in the same industry, as capital structure norms vary significantly by sector. Utilities and REITs commonly carry 50-60% debt because their cash flows are stable and predictable. Technology companies often carry 0-20% debt because their cash flows are less predictable. Also examine the company's interest coverage ratio (EBIT / Interest Expense) -- a ratio below 3x suggests the company may be over-leveraged. Credit rating agencies like Moody's and S&P provide guidelines for what leverage ratios correspond to each credit rating.

**Q2: Is WACC constant over time?**

A: No. WACC changes whenever its inputs change. When interest rates rise, both the cost of debt and the cost of equity increase, raising WACC. When a company takes on more debt, the debt weight increases, initially lowering WACC (due to the tax shield) but eventually raising it (due to higher risk). When a stock's beta changes (perhaps because the business becomes more or less risky), the cost of equity changes. Analysts should use a current or forward-looking WACC, not a historical one.

**Q3: Should I prefer companies that pay dividends or companies that buy back shares?**

A: It depends on your situation. If you need regular income (retirees, for example), dividends provide predictable cash flow without selling shares. If you are in a high tax bracket and do not need income, buybacks are more tax-efficient because you control when (and if) you realize the gain. From a pure value creation perspective, the best companies combine moderate dividends with disciplined buybacks when shares are undervalued. The worst approach is a high payout ratio combined with buybacks at any price.

**Q4: What is "shareholder yield" and why does it matter?**

A: Shareholder yield combines dividends and net buybacks (buybacks minus stock issuance) into a single metric. A company yielding 2% in dividends plus 4% in net buybacks has a 6% shareholder yield. This gives a truer picture of total cash being returned to shareholders than dividend yield alone. Research by Mebane Faber and others has shown that portfolios sorted by shareholder yield have historically outperformed portfolios sorted by dividend yield alone, likely because it captures both forms of capital return and penalizes companies that dilute shareholders.

**Q5: How can I tell if a CEO is a good capital allocator?**

A: Track these metrics over 5-10 years: (1) Is return on invested capital (ROIC) consistently above WACC? If so, every dollar reinvested creates value. (2) Has the total share count decreased? If massive buybacks are announced but shares outstanding are flat, compensation dilution is eating the buybacks. (3) Have acquisitions been successful? Check post-acquisition ROIC versus pre-acquisition projections. (4) Has book value per share grown faster than peers? (5) Does the CEO have significant personal ownership? CEOs who own meaningful stock tend to make better decisions.

**Q6: What is "agency cost" and how does it show up in practice?**

A: Agency costs are the economic losses that result from the conflict between managers' interests and shareholders' interests. They show up in several ways: excessive executive compensation packages, empire-building acquisitions that destroy value, perquisites like corporate jets and lavish offices, reluctance to return excess cash to shareholders (managers prefer a bigger cash pile for security), and decisions that reduce short-term earnings volatility even when long-term value creation requires accepting more volatility.

**Q7: Why do some companies maintain dual-class share structures?**

A: Dual-class structures (where founders hold shares with 10x voting power) exist because founders want to maintain control while raising capital. The argument for them is that visionary founders can make long-term decisions without being pressured by short-term-oriented shareholders. Facebook, Google, and Berkshire Hathaway all have dual-class structures. The argument against is that they insulate management from accountability and allow poor decisions to persist unchecked. Academic evidence suggests dual-class companies trade at a valuation discount, reflecting the governance risk.

**Q8: When should a company raise its dividend versus buy back shares?**

A: A company should raise its dividend when it has durable, growing cash flows and wants to signal long-term confidence to shareholders. Once raised, dividends are very difficult to cut without damaging the stock price, so the increase must be sustainable. Buybacks are more appropriate when: the stock is trading below intrinsic value (returning capital at a discount), cash flows are lumpy or uncertain (buybacks can be paused without stigma), or the shareholder base prefers tax-efficient returns. In practice, many large companies do both simultaneously.

**Q9: What role do activist investors play in corporate governance?**

A: Activist investors buy significant stakes in companies they believe are poorly managed and then push for changes -- new board members, strategic shifts, spin-offs, management changes, or increased capital returns. They serve as an external governance mechanism, complementing the internal mechanisms of the board. Research shows that activist campaigns are associated with meaningful improvements in operating performance and stock returns on average. However, some activists pursue short-term financial engineering that may come at the expense of long-term investment.

**Q10: How does WACC relate to the valuation lessons we covered in Week 21?**

A: WACC is the discount rate used in DCF valuation. When you discount a company's future free cash flows back to the present, you use the WACC as the rate. A lower WACC means future cash flows are worth more today, resulting in a higher valuation. A higher WACC means future cash flows are worth less, resulting in a lower valuation. This is the direct link between corporate finance and valuation -- the company's capital structure decisions (which determine WACC) directly affect what the company is worth.

---

## YouTube Script

[VISUAL: Animated intro with title "Week 19: Corporate Finance - Capital Structure, WACC, Dividends, and Governance"]

**Alex:** Welcome back everyone. Today we are going under the hood of how companies actually manage their money. This is corporate finance, and I promise you this will change how you look at every company you invest in.

**Sam:** Why should I care about how a company structures its finances? I just want to know if the stock price is going up.

**Alex:** And that is exactly why you need to understand this. Stock prices over the long term are driven by how effectively management allocates capital. Think of it this way -- when you buy a stock, you are essentially hiring the management team to invest your money for you. Would you hire someone without understanding how they plan to use your money?

**Sam:** When you put it that way, no.

**Alex:** Exactly. So let us start with the most fundamental decision in corporate finance: how should a company fund itself? Should it use debt, equity, or some combination?

[VISUAL: Title card "Capital Structure: Debt vs. Equity" with a building illustration. One side of the building is labeled "Debt" and is shaded blue, the other side "Equity" shaded green. The proportion changes dynamically.]

**Sam:** I think I know this. Debt is borrowed money and equity is ownership money, right?

**Alex:** Correct. But the choice between them has enormous consequences. Let me give you a concrete example. Imagine two identical pizza restaurant chains, each with $1 million in assets generating $150,000 in operating income. Chain A is financed entirely with equity -- the owners put up all the money. Chain B is financed with $500,000 in equity and $500,000 in debt at 6% interest.

**Sam:** So Chain B owes $30,000 a year in interest.

**Alex:** Right. Chain A earns $150,000 before tax, pays $37,500 in tax at a 25% rate, and keeps $112,500. That is an 11.25% return on the owners' million-dollar investment. Chain B earns $150,000 but pays $30,000 in interest, leaving $120,000 before tax. After $30,000 in tax, they keep $90,000. But here is the key -- the owners only invested $500,000, so their return is 18%.

[ANIMATION: animation/week19_leverage_effect.py - Split screen showing two identical restaurant buildings. Money flows in from the top (revenue) and out the bottom (expenses). Chain A shows all equity funding with a modest return arrow. Chain B shows half equity, half debt, with a larger return arrow on the equity portion but also an interest payment flowing out to a bank. As the operating income slider moves, both chains' returns change -- but Chain B's moves more dramatically in both directions, showing the leverage amplification effect.]

**Sam:** Wait, Chain B's owners made a higher return even though the company had lower net income?

**Alex:** Exactly. This is the power of leverage. Because the owners put up less money but the business generated the same operating income, their return on equity is higher. But here is the catch. What happens if the business has a bad year and operating income drops to $20,000?

**Sam:** Chain A would still make a small profit, but Chain B has to pay $30,000 in interest on only $20,000 of income -- they are in the red.

**Alex:** Precisely. Leverage magnifies returns in both directions. Good times become great, and bad times become terrible. This is the fundamental tradeoff of debt -- higher potential returns but also higher risk.

**Sam:** So is there an optimal amount of debt?

**Alex:** There is, and finding it is one of the central problems in corporate finance. In 1958, two economists named Modigliani and Miller proved something remarkable. In a perfect world -- no taxes, no bankruptcy costs -- the mix of debt and equity would not matter at all. The total value of the firm would be the same regardless.

**Sam:** But we do not live in a perfect world.

**Alex:** Right. In reality, there are two major frictions that make capital structure matter. First, interest on debt is tax-deductible, which gives debt a cost advantage. If a company borrows $1 million at 5%, the $50,000 in interest reduces taxable income, saving $12,500 in taxes at a 25% rate. That tax shield is worth real money. Second, too much debt creates the risk of financial distress -- if you cannot make your interest payments, you face bankruptcy, which is enormously costly.

[VISUAL: A graph showing firm value on the y-axis and debt ratio on the x-axis. The value curve rises as debt increases (tax benefit) but then peaks and declines (bankruptcy costs). The peak is labeled "Optimal Capital Structure" and is shown around 30-50% debt for a typical company. Annotations show "tax benefits dominating" on the left side and "distress costs dominating" on the right side.]

**Sam:** So the optimal capital structure balances the tax benefits of debt against the bankruptcy risks?

**Alex:** Exactly. And this optimal point varies by industry. A utility company with stable, predictable cash flows can safely carry 50-60% debt. A technology startup with volatile and uncertain cash flows should carry very little. The general rule is: the more stable and predictable your cash flows, the more debt you can safely handle.

**Sam:** This makes sense. Now, you mentioned WACC earlier. What is that?

**Alex:** WACC stands for Weighted Average Cost of Capital. It is the blended cost of all the money a company uses. Think of it as the minimum return the company must earn on its investments to satisfy both its lenders and its shareholders.

**Sam:** How do you calculate it?

**Alex:** You take the cost of equity multiplied by the equity weight, plus the cost of debt (after tax) multiplied by the debt weight. Let me use a real example. Say a company has a $800 million market cap and $200 million in debt. Shareholders require a 10% return and the company borrows at 5%. The tax rate is 25%.

**Alex:** Equity weight is 80%, debt weight is 20%. WACC equals 10% times 80% plus 5% times 20% times 75%, which is 8% plus 0.75%, equaling 8.75%.

[VISUAL: Animated WACC calculation showing the components assembling like building blocks. Equity block (large, labeled 10% x 80% = 8.0%) and debt block (small, labeled 5% x 20% x 75% = 0.75%) stack together to form the total WACC bar of 8.75%. A "hurdle" line is drawn at 8.75% with the text "Every project must clear this bar to create value."]

**Sam:** So if the company invests in a project that returns 7%, that is bad?

**Alex:** It is destroying value. The project earns 7% but the capital costs 8.75%. Shareholders would have been better off getting their money back. This is one of the most important concepts in all of corporate finance -- only invest in projects that earn above the cost of capital.

**Sam:** Let us talk about what happens when the company has more cash than good projects. How does it return money to shareholders?

**Alex:** Two main ways: dividends and share buybacks. Let us start with dividends. A dividend is simply a cash payment from the company to its shareholders. If a company pays $1 per share per quarter and you own 1,000 shares, you receive $1,000 in cash every three months.

**Sam:** That sounds great. Why does not every company pay dividends?

**Alex:** Because some companies have better uses for their cash. If a company can reinvest profits at a 25% return, sending that money to shareholders who might only earn 8% in the market is a poor decision. Amazon famously paid no dividends for decades because Jeff Bezos could reinvest every dollar at extraordinary returns. But mature companies with limited growth opportunities should return excess cash rather than hoarding it or wasting it on low-return projects.

[VISUAL: Decision tree flowchart. Starting with "Company has $100M in free cash flow." First branch: "Can we invest at returns above WACC?" If yes, "Invest in growth." If no, "Return cash to shareholders" which branches into "Dividends" and "Buybacks" with pros and cons listed for each.]

**Sam:** What makes a dividend safe or risky?

**Alex:** The key metric is the payout ratio -- what percentage of earnings is being paid out as dividends. A payout ratio of 40% is very comfortable. It means the company can absorb a significant earnings decline and still afford the dividend. A payout ratio of 90% is dangerous -- any earnings stumble could force a cut. Even more important, look at whether free cash flow covers the dividend. Some companies report good earnings but poor cash flow, and if the cash is not there, the dividend is not sustainable.

**Sam:** What happens when a company cuts its dividend?

**Alex:** It is usually a bloodbath for the stock price. Dividend cuts are one of the strongest negative signals a company can send. They are saying "we can no longer afford to pay you." The stock typically drops 20-30% on a dividend cut announcement because it signals fundamental deterioration AND forces income-seeking investors -- who held the stock specifically for the dividend -- to sell.

[VISUAL: A chart showing a hypothetical stock price stable at $50 with consistent quarterly dividends. On the day the dividend cut is announced, the price gaps down to $35 with high volume. The stock then drifts lower over the following weeks. A caption reads: "Dividend cuts are among the most destructive single-day events for shareholders."]

**Sam:** Okay, so what about buybacks? How do they work?

**Alex:** When a company buys back its own shares, it reduces the number of shares outstanding. If a company has 100 million shares and buys back 10 million, there are now only 90 million shares. Each remaining share represents a larger piece of the company. If earnings stay the same at $100 million, EPS goes from $1.00 to $1.11 -- an 11% increase without the company earning a single additional dollar of profit.

**Sam:** That is clever. So buybacks increase your ownership percentage?

**Alex:** Exactly. But here is where it gets controversial. Buybacks only create value if the company is buying at a reasonable price. If the stock is worth $50 and the company buys at $30, that is a fantastic deal -- they are buying dollars for 60 cents. But if the stock is worth $30 and they are buying at $50, they are paying $1.67 for every dollar of value. That destroys value for remaining shareholders.

**Sam:** How do I know if a buyback is being done at a good price?

**Alex:** Look at the valuation metrics we learned in Week 21. If the company is buying back stock when its P/E is below its historical average and below peers, that is likely a good buyback. If it is buying at all-time-high valuations, be skeptical. Also, and this is critical -- check whether the share count is actually declining. Many companies announce huge buyback programs but the share count barely moves because they are simultaneously issuing new shares as executive compensation.

[ANIMATION: animation/week19_buyback_dilution.py - A pie chart showing "Total Shares Outstanding." On one side, slices are being removed (buybacks). On the other side, new slices are being added (stock-based compensation). The net effect is shown over 5 years -- despite $5 billion in announced buybacks, the pie barely changes size. Final reveal shows "Announced buybacks: $5B. Actual share reduction: 2%. Executive compensation: the hidden cost."]

**Sam:** That feels like a scam.

**Alex:** It is one of the most common forms of shareholder wealth transfer, and most retail investors never notice it. Always check shares outstanding over time, not just buyback announcements.

**Sam:** Let us talk about corporate governance. What is it and why should an investor care?

**Alex:** Corporate governance is the system that keeps management accountable to shareholders. Remember, when you own a stock, you are an owner of the company but you do not run it day to day. You delegate that to the CEO and management team. The governance system ensures they act in your interest, not just their own.

**Sam:** What is the main risk if governance is weak?

**Alex:** The agency problem. Managers and shareholders have naturally different interests. Shareholders want to maximize the value of their investment. Managers want to maximize their compensation, job security, and prestige. These goals overlap sometimes, but not always. A CEO might pursue a massive acquisition not because it is the best use of shareholder capital, but because running a bigger company means higher pay and more power.

[VISUAL: Two-column comparison showing "What shareholders want" vs. "What managers might want." Shareholders: maximize returns, efficient capital use, transparency, appropriate risk. Managers: higher pay, bigger empire, job security, personal perks. The overlap area is labeled "Good governance aligns these."]

**Sam:** What are the warning signs of bad governance?

**Alex:** Several red flags. First, the CEO is also the chairman of the board -- the person being overseen is overseeing themselves. Second, board members have served for 15 or 20 years -- they are likely captured by management and not truly independent. Third, executive compensation is excessive relative to performance. If the stock drops 30% but the CEO still gets a $20 million bonus, the pay structure is broken. Fourth, dual-class share structures where insiders control voting with a small economic stake.

**Sam:** You mentioned dual-class shares. How does that work?

**Alex:** Some companies issue two classes of stock. Class A might have 1 vote per share and Class B has 10 votes per share. The founders hold the Class B shares. So a founder might own only 10% of the economic value of the company but control 51% of the votes. Google, Meta, and Snap all have structures like this.

**Sam:** Is that bad?

**Alex:** It depends on who the founder is. If the founder is Mark Zuckerberg building Meta into one of the world's most valuable companies, the dual-class structure arguably protects the long-term vision from short-term pressure. If the founder is running the company into the ground, the dual-class structure prevents shareholders from holding them accountable. It is a bet on the judgment of one person.

**Sam:** One last topic. You mentioned that most acquisitions destroy value. Why do companies keep doing them?

**Alex:** This is one of the great puzzles of corporate finance. Study after study shows that on average, the acquiring company's stock falls on announcement of a major acquisition. The target company's shareholders get a 20-30% premium, but the acquirer's shareholders lose value. Yet the M&A industry is enormous and CEOs keep doing deals.

**Sam:** Why?

**Alex:** Several reasons. One, CEO compensation is often tied to company size -- bigger company, bigger paycheck. Two, overconfidence -- every CEO thinks they will be the exception who makes the acquisition work. Three, investment bankers earn enormous fees from deals, so they are always pitching acquisition ideas. Four, sometimes acquisitions are genuinely the right move, and the statistical average includes both good and bad deals.

[VISUAL: Bar chart showing "Average stock price reaction to M&A announcements." Target company: +25% in green. Acquiring company: -3% in red. Combined: -1% in light red. Caption: "On average, M&A transfers value from acquirer to target shareholders."]

**Sam:** So how do I evaluate an acquisition as a shareholder?

**Alex:** Ask five questions. One, what price is being paid? Compare it to the target's valuation multiples and to comparable transactions. Two, how is it being funded? All-cash is usually better than stock (issuing stock dilutes existing shareholders). Three, what are the claimed synergies, and are they realistic? Cuts synergies (cost savings) are more reliable than growth synergies (revenue increases). Four, what is the acquirer's track record with previous deals? Some companies are serial acquirers with a history of value destruction. Five, does the deal make strategic sense, or is it empire building?

**Sam:** This has been incredibly dense but really valuable. Let me try to summarize. Capital structure is the mix of debt and equity -- debt amplifies returns but increases risk. WACC is the minimum return a company must earn. Dividends and buybacks are how companies return cash, but both can be done well or poorly. And governance is the system that keeps management honest.

**Alex:** Perfect summary. And here is the one thing I want you to take away from today. When you evaluate any company as an investment, ask yourself: is management creating value with my money or extracting value from me? Capital allocation quality, shareholder returns policy, and governance structures will tell you the answer.

[VISUAL: A "Management Quality Checklist" with six items:
1. ROIC consistently above WACC?
2. Share count actually declining?
3. Dividend well-covered by FCF?
4. M&A track record positive?
5. Board independent with aligned incentives?
6. Management has meaningful stock ownership?]

**Sam:** Next week?

**Alex:** Next week we are going to look at earnings and cash flow quality -- how to tell whether a company's reported profits are real or an accounting mirage. It is one of the most practical skills you can develop as an investor, and it connects directly to what we learned today about capital allocation.

[VISUAL: Preview card for Week 20 with "Earnings and Cash Flow: Quality, Manipulation, and Free Cash Flow"]

**Alex:** Thanks for watching everyone. Corporate finance might not sound glamorous, but I promise you -- the investors who understand how companies use their money consistently outperform those who just chase stock prices. Share this with anyone who is making investment decisions without looking under the hood. See you next week.

[VISUAL: Outro animation with subscribe button and links to previous episodes]
