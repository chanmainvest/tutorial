# Week 8: Reading Financial Statements — IS, BS, CF for Investors

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A public company speaks in three documents. The income statement, the
balance sheet, and the cash flow statement. Everything else — the
press release, the conference call, the analyst note, the stock
price — is commentary on those three. If you cannot read the
documents themselves, you are reading a translation of a translation,
hoping the translator did not lie.

For an investor — not an accountant, not an auditor — the goal is
narrow. You are not trying to recompute deferred tax liabilities. You
are trying to answer four questions, in order, in under twenty
minutes per company:

1. **Is the business growing, and is the growth profitable?** That
   lives on the income statement, in the path from revenue down to
   operating income.
2. **Is the business solvent and capitalised?** That lives on the
   balance sheet — assets versus liabilities, working capital, the
   debt stack.
3. **Is the reported profit real cash, or accounting?** That lives
   on the cash flow statement, in the gap between net income and
   operating cash flow. It is the only one of the three that is hard
   to fake.
4. **Are the three stories consistent?** When revenue grows but cash
   flow does not, when earnings grow but receivables grow faster,
   when book equity grows but free cash flow does not — something is
   either wrong, or about to be.

The CFA curriculum spends roughly fifteen percent of Level I on
financial statement analysis. We will spend one week on it, plus a
side lesson on the 10-K filing wrapper ([side02_10k_filing.md](side02_10k_filing.md)).
The two together are enough to read most filings competently. They
are not enough to audit one. That is fine. As Horace puts it: alpha
sources include "look at cash, not earnings" (SOUL #5). You do not
need to outwork the auditors to outperform the index. You need to
know which line of which statement to land on first.

---

### 2. What You Need to Know

#### 2.1 The Three Statements as One Story

The three statements are not three independent documents. They are
three views of one underlying ledger, and they are mathematically
linked.

- The **income statement** covers a period (a quarter or a year). It
  starts at revenue and works down to net income. Time-window view:
  flow.
- The **balance sheet** is a snapshot at a single date — usually the
  last day of the period. Assets equal liabilities plus equity.
  Point-in-time view: stock.
- The **cash flow statement** also covers a period. It explains the
  change in cash on the balance sheet, broken into three buckets:
  cash from operations (OCF), cash used for investing (CFI), and
  cash from financing (CFF).

The three are linked by two bridges:

- **Net income flows into retained earnings on the balance sheet.**
  Last year's equity plus net income minus dividends equals this
  year's equity, before share buybacks and other adjustments.
- **Operating cash flow starts from net income and adjusts.** Add
  back non-cash charges (depreciation, stock-based compensation),
  adjust for working capital changes (receivables, payables,
  inventory). Whatever is left after capital expenditure is **free
  cash flow**, and that is the number that pays dividends, retires
  debt, and funds buybacks.

The investor's discipline: read all three together, and trust the
cash flow statement most when they disagree.

#### 2.2 The Income Statement — Revenue Down to Net Income

The income statement is a waterfall. Revenue at the top, deductions
at each step, net income at the bottom. Five waypoints matter.

**Revenue.** What customers actually paid (or owed) for goods and
services delivered in the period. The single hardest line to fake
across multiple years, because it is also the line that auditors
tie back hardest to receipts and contracts.

**Gross profit = Revenue − Cost of goods sold.** Direct cost of
producing what was sold. Gross margin (gross profit / revenue) tells
you how much pricing power and unit economics the business has. A
software company should print 70%+ gross margin; an airline,
10–20%. Compare within an industry, not across.

**Operating income (EBIT) = Gross profit − Operating expenses.**
Subtract R&D, SG&A, depreciation, and amortisation. This is what
the actual *operations* of the business earned, before the financial
structure (interest) and the tax authority (taxes). Operating margin
is the cleanest measure of business quality.

**Pre-tax income = Operating income − Net interest.** Add interest
income, subtract interest expense, throw in any non-operating items
(gains or losses on investments). This is where the *capital
structure* shows up. A heavily-indebted company can have great
operating margins and ugly pre-tax income.

**Net income = Pre-tax income − Income taxes.** The "bottom line."
Divided by share count, you get earnings per share (EPS).

The image below walks Apple's FY2024 (year ending September 2024)
income statement and cash flow as a single horizontal waterfall —
revenue all the way to free cash flow.

![Apple FY2024 income-statement and cash-flow waterfall, $ billions. Bars from left to right: Revenue $391B, then negative bars peeling off Cost of revenue ($210B) leaving Gross profit $181B; subtract Operating expenses ($57B) to get Operating income $123B; subtract Income tax and other items to get Net income $94B; then add back Depreciation/amortisation, stock-based compensation, and working-capital release to land at Operating cash flow $118B; subtract Capex of $9B to land at Free cash flow $109B. The chart shows that Apple converts more cash than it reports as profit because non-cash charges and working capital favour cash.](image/week08_aapl_decomposition.png)

The most important visual takeaway is the gap between the rightmost
two bars: **net income $94B versus free cash flow $109B**. Apple
converted *more* cash than it booked as accounting profit. That is
a hallmark of a healthy capital-light business. The opposite gap —
net income materially above free cash flow, year after year — is
the textbook accounting-quality warning sign.

#### 2.3 The Balance Sheet — Assets, Liabilities, Equity

The balance sheet is governed by one identity:

$$ \text{Assets} = \text{Liabilities} + \text{Shareholders' Equity} $$

It always balances by construction. Bookkeeping is double-entry —
every dollar of asset has a dollar of either a claim against it
(liability) or ownership of it (equity). This is not deep economics;
it is the structure of the ledger.

What matters for an investor is the **composition** of each side.

On the **asset** side, the order top-to-bottom is liquidity:

- **Cash and equivalents.** Sitting in a money-market fund or short
  T-bills. Spendable today.
- **Short-term investments and accounts receivable.** Convertible
  to cash within a year — but receivables can go bad.
- **Inventory.** Goods waiting to be sold. The longer it sits, the
  staler and more discountable it becomes.
- **Property, plant, and equipment (PP&E).** Factories, machines,
  data centres. Long-lived. Reported at historical cost less
  accumulated depreciation, which can wildly understate replacement
  value (think a hundred-year-old refinery).
- **Goodwill and intangibles.** What the company paid for
  acquisitions above the target's book value, plus internally-held
  brand or patent values. The line that gets *impaired* (written
  down) when an acquisition turned out to be a mistake.

On the **liability** side, the order is when the bill is due:

- **Accounts payable.** Owed to suppliers, typically 30–60 days.
- **Short-term debt and current portion of long-term debt.** Coming
  due within a year. The classic solvency stressor.
- **Long-term debt.** Bonds and term loans. The single most
  important liability for understanding the capital stack.
- **Pension and lease obligations.** Often understated or
  off-balance-sheet under prior accounting; now mostly captured
  under the current rules but still worth checking.

**Shareholders' equity** is the residual — assets minus liabilities.
It is mostly composed of (1) common stock plus paid-in capital
(what shareholders put in), (2) retained earnings (cumulative net
income kept inside the business), and (3) treasury stock (the
negative of buybacks). For a mature company that has been buying
back stock for years, treasury stock can be enormous; companies like
Boeing and Starbucks have *negative* shareholders' equity precisely
because they have bought back more stock than they have retained.
Negative book equity is not by itself a problem if the cash flow is
healthy — it is just a note that the company has chosen buybacks
over balance-sheet padding.

The two practitioner ratios you actually use:

- **Current ratio = Current assets / Current liabilities.** Above 1
  is generally healthy; below 1 means the company depends on
  refinancing, inventory turnover, or revolver capacity to meet
  near-term obligations.
- **Net debt / EBITDA.** Total debt minus cash, divided by trailing
  twelve-month EBITDA. Below 2× is conservative; 3–4× is normal for
  many sectors; above 5× is leveraged-buyout territory and starts to
  look fragile under a recession or a rate spike.

#### 2.4 The Cash Flow Statement — The One That's Hard to Fake

This is the statement that separates investors from speculators.

Net income is an *opinion* — a defensible one, signed by auditors,
but built on dozens of estimates: depreciation lives, allowance for
doubtful accounts, inventory write-downs, stock-based compensation,
revenue-recognition timing. Cash flow is a *fact*. Either the bank
balance went up, or it didn't.

The statement is built in three sections:

- **Cash from operating activities (CFO or OCF).** Starts at net
  income, adds back non-cash items (depreciation, amortisation,
  stock-based compensation), and adjusts for working-capital changes
  (receivables up = cash out; payables up = cash in; inventory up =
  cash out). End result: actual cash the operating business
  generated.
- **Cash from investing (CFI).** Capital expenditure (negative,
  reinvested in the business), acquisitions (negative), proceeds
  from sales of assets (positive), and changes in marketable
  securities portfolios.
- **Cash from financing (CFF).** Debt raised or repaid, equity
  issued or bought back, dividends paid.

The single most-used investor metric:

$$ \text{Free Cash Flow (FCF)} = \text{OCF} - \text{Capex} $$

Free cash flow is what the business *could* return to all capital
providers without diminishing its operating capacity. It pays
dividends, funds buybacks, retires debt, finances acquisitions.
Persistent free cash flow is the only economic basis for any of
those things. Companies that pay dividends or buy back stock without
generating free cash flow are doing so by issuing debt or equity —
borrowing from one set of investors to pay another, which is fine
for a year and ruinous over a decade.

The discipline Horace pushes (SOUL #5): when the gap between net
income and free cash flow grows, distrust the income statement.
Earnings can be manipulated; cash is harder. The chart below shows
this exact gap for Apple over the last decade.

![Apple FY2014–FY2024 split-adjusted diluted EPS versus free cash flow per share (USD). Both lines rise from roughly $1.6–$1.9 in FY2014 to $6.1–$7.1 in FY2024. EPS and FCF per share track each other closely except in FY2020, where FCF per share ran ahead of EPS — the COVID year, when working capital released cash even as inventory and supply-chain disruption depressed reported earnings. The FY2024 gap also widens because a one-time roughly $10B EU State-aid tax charge depressed reported net income while leaving cash flow untouched.](image/week08_eps_vs_fcf.png)

In FY2020, EPS dropped relative to FCF because COVID-era working
capital released cash (customers paid, inventory drew down) faster
than accounting earnings were recognised. In FY2024, a one-time
roughly $10B European Commission tax charge depressed reported net
income without touching the actual cash collected from customers.
Both years are clean illustrations of the same lesson: the cash is
the fact; the earnings are the opinion.

#### 2.5 Common-Size Statements — Reading Across Time and Companies

Raw dollar figures are hard to compare. Apple at $391B revenue and
Coca-Cola at $46B revenue are not in the same league of *size*, but
they may be in the same league of *quality*. **Common-size
statements** rebase every line as a percentage of revenue (income
statement) or total assets (balance sheet). That removes the size
bias and makes the *structure* of the business visible.

A common-size income statement for FY2024 looks like this for our
three example companies:

| Line | Apple | Coca-Cola | JPMorgan |
|---|---:|---:|---:|
| Revenue | 100% | 100% | 100% |
| Gross profit | 46% | 60% | n/a |
| Operating income | 32% | 30% | 41% |
| Net income | 24% | 23% | 32% |
| Free cash flow / revenue | 28% | 21% | n/a |

Three very different businesses, three very different cost
structures, but all three converting roughly a quarter of revenue
into net profit — a sign that all three sit at the high-quality end
of their respective sectors. Banks (JPMorgan) are excluded from the
gross-profit and FCF rows because their income statement structure
is fundamentally different (net interest income, provisions for
credit losses, no real "cost of goods sold"). Banks need their own
template, which we cover in Week 33.

The interactive panel below lets you switch between Apple, Coca-Cola,
and JPMorgan, toggle between Revenue / Net Income / OCF / FCF, and
see the ten-year history side by side with common-size ratios. The
goal is to develop a *visual* sense for how different sectors look
on the page, so you can flag anomalies on filings you have never
seen before.

#### 2.6 What an Investor Actually Reads, in What Order

A practical reading sequence for a new company, twenty minutes:

1. **Revenue trend, ten years.** Growing? Decelerating? Cyclical?
   Look at the cash flow statement summary too — does cash track
   revenue?
2. **Operating margin trend, ten years.** Expanding (pricing
   power), flat (steady state), contracting (competition or cost
   pressure)?
3. **Free cash flow versus net income, ten years.** Do they track?
   When they diverge, in which direction and why? Persistent FCF
   below net income is the loudest single warning.
4. **Net debt / EBITDA, current and trend.** Capital structure
   sustainable in a 5%-rate world? Refinancing wall in the next
   18 months?
5. **Capital allocation, last three years.** Buybacks vs dividends
   vs reinvestment vs M&A. Funded from FCF or from new debt?

The 10-K side lesson ([side02_10k_filing.md](side02_10k_filing.md))
covers where in the document to find each of these — Item 7 (MD&A),
Item 8 (statements), Item 1A (risk factors), notes to the financial
statements. The combination of *what to read* (this lesson) and
*where in the filing it lives* (the side lesson) is enough to put
you in the top decile of retail investors by financial literacy.
That is a low bar but a real one.

---

### 3. Common Misconceptions

**Misconception 1: "Earnings are the most important number."**

Earnings are an opinion produced by accounting choices. Free cash
flow is a fact. When they agree, the business is genuinely
profitable. When they disagree persistently, the cash flow is
right and the earnings are wrong, almost without exception.

**Misconception 2: "A profitable company cannot go bankrupt."**

Profitable companies go bankrupt all the time — when they cannot
service their debt. Profit is on the income statement; cash to pay
bondholders is on the cash flow statement. Many of the most famous
bankruptcies (Toys "R" Us, Hertz at the LBO peak) happened to
companies that were "profitable" right up until the refinancing
window slammed shut.

**Misconception 3: "Negative book equity means the company is
insolvent."**

Not in the modern era. Mature buyback-heavy companies (Boeing,
Starbucks, McDonald's at points) have negative book equity simply
because they have repurchased more stock than they have retained.
Solvency is determined by the ability to service obligations from
cash flow, not by the sign of the book-equity line.

**Misconception 4: "Big depreciation charges are bad."**

Depreciation is a non-cash charge. It reduces accounting profit
but does not reduce cash. A capital-intensive business (utility,
railroad, refinery) will always have high depreciation; it
compresses earnings but not cash flow. The right comparison is
capex versus depreciation: capex above depreciation means the
business is growing or replacing aging assets; capex well below
depreciation means the company is harvesting (running down its
asset base for cash). Either can be right depending on the strategy.

**Misconception 5: "Stock-based compensation is not a real cost."**

It is. Companies (especially in tech) like to present "adjusted
EPS" with SBC added back, framing it as non-cash. It is non-cash
in the period, but it dilutes existing shareholders and very much
costs them economically. Treat SBC as a real cost. Adjusted EBITDA
that excludes SBC is one of the few numbers in finance that is
nearly always misleading.

**Misconception 6: "Goodwill represents real value."**

Goodwill is a plug — the residual of acquisition price over the
target's identifiable net assets. It is not depreciated; it is
tested for impairment annually. Many companies' goodwill quietly
balloons through acquisitions and then suddenly collapses in a
single quarter when the deal does not work. Treat the goodwill line
with extreme skepticism, especially for serial acquirers.

**Misconception 7: "If the auditor signed it, it's accurate."**

Auditors test for material misstatement, not truth. The Big Four
sign-off on Enron, Wirecard, and Lehman are the standing reminders
that audit assurance is far weaker than retail investors imagine.
The audit is a backstop, not a guarantee.

**Misconception 8: "All companies in the same sector should look
similar."**

The sector frames the *structure*, not the *quality*. Two software
companies can both have 70% gross margins, but if one has 30%
operating margin and the other 5%, they are not in the same
business in any meaningful sense. Common-size analysis is most
useful precisely because it highlights these dispersions within a
sector.

---

### 4. Q&A

**Q1: I have never read a 10-K. Where do I start?**

A: Open Apple's most recent 10-K on EDGAR. Read Item 7 (MD&A) end
to end — it is management explaining the year in their own words.
Then jump to Item 8 and look at the three statements. Spend ten
minutes on each. Then read the first three risk factors in Item 1A.
That is a working forty-minute first pass. The side lesson on the
10-K filing structure ([side02_10k_filing.md](side02_10k_filing.md))
walks the document section by section.

**Q2: What is the single most informative ratio?**

A: There is no single one. If you held a gun to my head, **free
cash flow / revenue** for non-financial businesses. It captures
the ability to convert sales into spendable cash, which subsumes
gross margin, working-capital efficiency, and capital intensity in
one number. Above 15% is high-quality; above 20% is exceptional.
For banks, **return on tangible common equity (ROTCE)** is the
analogous one-number summary.

**Q3: Why do GAAP earnings and "adjusted earnings" disagree?**

A: Companies present non-GAAP adjusted figures to highlight what
they argue is the recurring economic earnings power, excluding
one-time items, M&A-related amortisation, restructuring charges,
and (often) stock-based compensation. Some adjustments are honest
(genuine one-time charges); some are not (recurring SBC dressed up
as non-recurring). Read both. Distrust the gap. SEC Regulation G
requires reconciliation of any non-GAAP figure to its GAAP
equivalent — the reconciliation is where the truth lives.

**Q4: How do I read a bank's financial statements?**

A: Banks are different. Their "revenue" is net interest income
plus non-interest income, not "revenue minus COGS." Their key
lines are net interest margin, provision for credit losses, the
efficiency ratio (non-interest expense / revenue), and ROTCE.
Their balance sheet is dominated by loans (asset) and deposits
(liability). We cover this in Week 33; the framework is genuinely
distinct.

**Q5: What is "earnings management" and how do I spot it?**

A: Smoothing reported earnings via legal but discretionary
accounting choices — accelerating revenue recognition into a soft
quarter, deferring expenses, building or releasing reserves. Spot
it by comparing operating cash flow to net income year over year.
Persistent operating cash flow below net income, with growing
receivables or growing inventory, is the classic combination.
Beneish's M-Score and Sloan's accruals ratio are formal tools
investors use; for a casual reader, the OCF-to-NI gap is enough.

**Q6: What about non-US companies — same statements?**

A: Mostly. Outside the US, companies file under IFRS (International
Financial Reporting Standards) rather than US GAAP. The structure
of the three statements is the same; the line-item conventions
differ in places (LIFO inventory not allowed, capitalised R&D
allowed, lease accounting differs). Per SOUL #16, this course
restricts the *investable* universe to US-listed equities — but
many of those (ADRs, foreign-domiciled US-listed companies) file
under IFRS via 20-F. The three-statement framework still applies.

**Q7: How often should I re-read a company's statements?**

A: Quarterly, lightly. Annually, deeply. The 10-K (annual) is the
document that matters. The 10-Qs (quarterly) are progress reports;
read the MD&A and skim the statements to make sure nothing is
breaking. Re-read the full 10-K every year for any position you
hold longer than twelve months.

**Q8: Should I trust company-reported metrics that aren't on the
financial statements? (e.g., monthly active users, ARR, "core EPS")**

A: With calibration. Operating metrics outside GAAP can be useful
forward indicators but are unaudited and definitionally elastic.
Compare year over year *and* against the company's own definition
in prior periods (companies sometimes redefine MAUs or ARR to
flatter trends). Cross-check against the audited cash flow.
Persistent ARR growth that does not show up as cash collected is
a story; cash collected with declining ARR is a real warning.

**Q9: How does this connect to valuation?**

A: Every valuation method we cover from Week 21 onward uses these
three statements as inputs. P/E uses net income. P/B uses
shareholders' equity. EV/EBITDA uses operating income plus
depreciation. DCF uses free cash flow projections. You cannot
pressure-test any valuation if you cannot rebuild the inputs from
the statements. That is why this lesson sits where it does in the
sequence — before any of the valuation work.

**Q10: Will I have to do this forever, or do tools automate it?**

A: Tools (StockAnalysis, Macrotrends, Tikr) display the headline
numbers. They do not read the notes, do not catch the SBC games,
do not flag the goodwill build-ups. The screen-and-skim layer is
automated; the reading layer is not, and probably will not be.
The portfolio-level edge is still in *which lines you look at and
in what order*, which is what this lesson teaches.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Reading Financial Statements — IS, BS, CF for Investors (Not Accountants) | Week 8

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** A public company speaks in three documents. The income
statement, the balance sheet, the cash flow statement. Everything
else — the press release, the analyst note, the stock price — is
commentary on those three.

**Stella:** And we're going to read all three in eighteen minutes.

**Horace:** Not as accountants. As investors. Different job. Auditors
need to verify every line. We need to know which four lines tell us
whether to keep reading.

**Stella:** Four lines?

**Horace:** Revenue trend. Operating margin. Free cash flow versus
net income. Net debt over EBITDA. If those four look right,
ninety percent of the rest of the document confirms what the four
already told you.

---

**[SEGMENT 1: WHY THREE STATEMENTS]**

**Horace:** The three statements are not three separate documents.
They are three views of one ledger. The income statement covers a
period — a movie. The balance sheet is a snapshot — a photo. The
cash flow statement explains how the photo changed during the
movie.

**Stella:** And they're connected.

**Horace:** Two bridges. Net income from the income statement flows
into retained earnings on the balance sheet. And the cash flow
statement starts at net income, adjusts back to actual cash. Both
bridges are in the same document. If they don't tie out, something
is wrong.

---

**[SEGMENT 2: THE INCOME STATEMENT WATERFALL]**

[VISUAL: image/week08_aapl_decomposition.png]

**Horace:** Apple, fiscal year 2024. Revenue three hundred ninety
one billion dollars. Strip out cost of revenue, two hundred ten
billion. You're at gross profit, one eighty one. Strip out operating
expenses — R&D, SG&A — fifty seven. You're at operating income,
one twenty three.

**Stella:** And then taxes.

**Horace:** Taxes and a little non-operating, lands you at net
income, ninety four billion. That's the bottom line of the income
statement.

**Stella:** But the bar keeps going.

**Horace:** Right. Because we're now on the cash flow statement.
Add back depreciation, amortisation, stock-based comp — all
non-cash. Add the working capital release. You land at operating
cash flow, one hundred eighteen billion. Subtract capex, nine
billion, you get to free cash flow, one hundred nine billion.

**Stella:** Free cash flow is bigger than net income.

**Horace:** Fifteen billion bigger. That's the most important fact
on the chart. Apple converted *more* cash than it booked as
profit. That is the signature of a high-quality, capital-light
business.

---

**[SEGMENT 3: THE BALANCE SHEET IDENTITY]**

**Horace:** Balance sheet. Single equation. Assets equal liabilities
plus equity. It always balances by construction. That's just
double-entry bookkeeping; not deep economics.

**Stella:** Then what do you actually read?

**Horace:** The composition. On the asset side, top to bottom in
liquidity — cash, receivables, inventory, PP&E, goodwill. On the
liability side, top to bottom by when the bill is due — payables,
short-term debt, long-term debt. Equity is the residual.

**Stella:** Two ratios?

**Horace:** Current ratio above one — current assets cover current
liabilities. Net debt over EBITDA below three for most sectors,
below two if conservative. That's it for a first pass.

---

**[SEGMENT 4: THE CASH FLOW STATEMENT — THE HARD ONE TO FAKE]**

**Horace:** This is the statement that separates investors from
speculators. Net income is an opinion. Cash flow is a fact.

**Stella:** Why is net income an opinion?

**Horace:** Because it embeds dozens of estimates. Depreciation
schedules. Allowance for bad receivables. Stock-based comp expense.
Revenue-recognition timing. Each one is defensible. Each one is
also a knob. Cash flow is harder to fake — either the bank account
went up, or it didn't.

**Stella:** Free cash flow.

**Horace:** Operating cash flow minus capex. That's what's available
to pay dividends, buy back stock, retire debt. That's what every
valuation discounts at the end of the day. When earnings grow but
free cash flow doesn't — distrust the earnings.

---

**[SEGMENT 5: EPS VERSUS FCF — APPLE TEN YEARS]**

[VISUAL: image/week08_eps_vs_fcf.png]

**Horace:** Apple's split-adjusted EPS versus free cash flow per
share, fiscal 2014 through 2024. Two lines that mostly track each
other. Both rise from about a dollar sixty to about six.

**Stella:** Where do they diverge?

**Horace:** Two places. FY2020 — COVID year. FCF runs above EPS.
Working capital releases cash even as accounting earnings stay
suppressed by inventory and supply chain. And FY2024 — there's a
one-time European Commission tax charge of about ten billion
dollars that hits net income but not the cash collected from
customers.

**Stella:** Both years, cash tells the truth.

**Horace:** Both times. That's the lesson Horace pushes — alpha
sources include "look at cash, not earnings." When the two lines
disagree, the cash line is right.

---

**[SEGMENT 6: COMMON-SIZE — THREE COMPANIES]**

**Horace:** The interactive panel below lets you flip between three
companies — Apple, Coca-Cola, JPMorgan. Toggle the metric — revenue,
net income, operating cash, free cash flow.

**Stella:** Three different businesses.

**Horace:** Three completely different cost structures. Apple has
forty-six percent gross margin, software-like. Coca-Cola has sixty
percent gross margin, brand-rent business. JPMorgan doesn't have a
gross margin in any meaningful sense — banks need their own
template. We cover banks in Week 33.

**Stella:** And the common-size view?

**Horace:** Reveals the structure independent of size. Apple converts
twenty-eight percent of revenue into free cash. Coca-Cola, twenty
one. Both are excellent. Both look completely different on the
page.

---

**[SEGMENT 7: THE TWENTY-MINUTE READING SEQUENCE]**

**Horace:** Practical sequence for a new company. Twenty minutes.

One — revenue ten years. Growing? Cyclical? Accelerating or
decelerating?

Two — operating margin ten years. Expanding means pricing power.
Contracting means competition or cost pressure.

Three — free cash flow versus net income. Do they track? When they
diverge, which direction and why?

Four — net debt over EBITDA. Capital structure sustainable at five
percent rates? Any refinancing walls in the next year and a half?

Five — capital allocation. Where is FCF going? Buybacks, dividends,
reinvestment, acquisitions? And is it actually funded by FCF, or by
new debt?

**Stella:** That's it?

**Horace:** That puts you in the top decile of retail investors by
financial literacy. Low bar. Real bar.

---

**[OUTRO]**

**Horace:** Three statements. Two bridges. One question — does the
cash flow confirm the earnings? When the answer is yes, the rest
of the document mostly tells you what you already know. When the
answer is no, that's where alpha lives. Or where the next blow-up
lives. Same place, viewed two different ways.

**Stella:** And the side lesson?

**Horace:** Side lesson two — Reading a 10-K Filing. Where in the
document each of these numbers actually lives. Item 7, Item 8,
Item 1A. Read this lesson first, then that one. Then go open
Apple's 10-K and try the twenty-minute sequence on it.

---

**END SCREEN:** "Next: Week 9 — Equity Valuation Foundations"
