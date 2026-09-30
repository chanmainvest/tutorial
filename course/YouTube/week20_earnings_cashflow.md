## Part 2: YouTube Script

---

**VIDEO TITLE:** Earnings Are an Opinion. Cash Is a Fact. — Week 20
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. This is Week 20, and the question for the
next eighteen minutes is the oldest question in fundamental
investing: when a company tells you it earned a dollar per share,
how much of that dollar is real?

**Horace:** Hong Kong markets just closed. The Apple result the
night before printed an EPS beat by three cents. The stock gapped
up two percent in the after-hours, traded sideways through the
Asia session, and you can already see analysts on Bloomberg arguing
whether the beat is "high quality" or "low quality." That argument
is not new and it is not going away. It is the topic of this week.

**Stella:** Two facts to anchor on before we get into the
mechanics. One: the difference between net income and operating
cash flow is called total accruals, and it has predicted future
stock returns, on average, with a meaningful spread, in every
replication study since Sloan published the original paper in 1996.
Two: stocks that beat earnings drift up for the next sixty trading
days, and stocks that miss drift down, also documented since 1989.
Both effects have weakened over time. Neither has inverted.

**Horace:** This is one of our structural alpha sources.
"Look at cash, not earnings." It sounds
trite. It is also genuinely persistent, because most of the market
is trading on the headline.

---

**[SECTION 1 — ACCRUALS, THE IDENTITY — 1:30]**

**Stella:** Start with the arithmetic. For any company, in any
period, net income equals operating cash flow plus total accruals.
That is not a model. That is the definition.

**Horace:** Accruals are not a dirty word. They are how accounting
matches revenue to the period it was earned and expenses to the
period they were incurred, regardless of when cash moved. That is
useful. A subscription business that bills annually but delivers
monthly *should* recognise the revenue across twelve months. That
is an accrual, and it is correct.

**Stella:** The problem is that every line on the bridge from net
income to operating cash flow is a discretionary judgement. Pace
of depreciation. Reserves for bad debts. Capitalisation versus
expensing. Working-capital classification. Each is individually
defensible. Stacked, they create enough latitude that the same
underlying business can print quite different EPS depending on the
mood of the CFO and the patience of the auditor.

**Horace:** And cash, by contrast, is much harder to fake. Either
it showed up in the bank account or it did not. The cash flow
statement is not free of judgement — operating versus investing
classification is genuinely ambiguous in places — but the *level*
of cash moves much less than the level of reported earnings under
management discretion.

---

**[SECTION 2 — THE ACCRUALS ANOMALY — 4:00]**

**Stella:** Sloan, 1996. Take every US-listed firm. Each year,
compute total accruals scaled by average total assets. Sort firms
into five quintiles. Q1 is lowest accruals — most cash-backed
earnings. Q5 is highest accruals — most accrual-heavy earnings.
Hold each quintile for the next twelve months. Repeat every year
for thirty years.

[VISUAL: image/week20_accruals_anomaly.png]

**Horace:** The picture is the result. Q1 averages roughly 16.8
percent. Q2 14.2. Q3 12.4. Q4 10.1. Q5, 7.6. The cross-sectional
average is around twelve percent. The Q1-minus-Q5 spread is about
nine percentage points per year. That is the academic estimate of
the alpha, and it is one of the largest robust spreads ever
documented in equity markets.

**Stella:** A few caveats. Half of the spread gets eaten by
transaction costs, capacity limits, and short-borrow fees on the
Q5 leg in any real implementation. The signal has weakened since
the paper was published — which always happens to good signals
once they are public. And the implementation of the short side, in
particular, is harder than the academic study suggests, because
the worst accruals firms are often small-caps with shallow
short-borrow markets.

**Horace:** Practical version for a retail book: do not short. Use
the screen to *exclude* high-accrual names from your long
portfolio. You will get most of the asymmetry without the
operational complexity. That is also a tranche-discipline
point — long quality goes in the core tranche; the short side, if
you do it at all, goes in the specialty tranche, with size limits.

---

**[SECTION 3 — POST-EARNINGS-ANNOUNCEMENT DRIFT — 7:30]**

**Stella:** The accruals anomaly is a twelve-month phenomenon. Its
faster cousin is the post-earnings-announcement drift, sixty days
after the print.

[VISUAL: image/week20_pead_drift.png]

**Horace:** Bernard and Thomas, 1989. Rank every quarterly
earnings release by standardised unexpected earnings — basically,
the surprise relative to consensus, scaled by the firm's typical
surprise volatility. Top quintile drifts up. Bottom quintile drifts
down. The middle quintile sits near zero. The drift continues for
about sixty trading days, then fades into the next earnings cycle.

**Stella:** In modern data the drift is smaller than the picture
suggests — replications through 2024 put the top-vs-bottom spread
at roughly two to three percent over sixty days, not the four to
five percent Bernard and Thomas reported in the original paper.
But the sign is stable. The drift has not inverted. The
information from the print is still being absorbed by the market
more slowly than a fully efficient model would predict.

**Horace:** Why does the market not arbitrage this away? Limits to
arbitrage, career risk, and the slow horizon. The accruals anomaly
takes twelve months to play out. PEAD takes sixty days. Most of
the trading volume in this market is operating on a one-day
horizon — the print versus the consensus. The slow signals do not
compete with the fast traders.

**Stella:** This is also where it touches the momentum-vs-
mean-reversion duality — the twin phenomena of price discovery.
PEAD is fundamentally a momentum effect — the stock
that surprised up keeps drifting up, because the information is
travelling through the market slower than the price. The accruals
anomaly is a mean-reversion effect — earnings inflated by accruals
revert toward cash over the next year. Same coin, opposite faces.

---

**[SECTION 4 — FREE CASH FLOW, CAREFULLY — 10:30]**

**Horace:** Free cash flow gets quoted three different ways in the
wild. We need the right one for screening.

**Stella:** FCF to the firm — operating cash flow minus capex.
That is the plain definition and the one the DCF model wants. FCF
to equity — FCFF minus net debt repayment plus net debt issuance —
is what the dividend-discount frameworks use. And then there is
"adjusted FCF," which is whatever management says it is. Adjusted
FCF gets the same eyebrow as adjusted EBITDA. Permanently raised.

**Horace:** Stock-based compensation deserves a side note. SBC is
a real cost. The company is handing out part of itself to
employees. The cash that would have been spent on payroll is
instead being raised by issuing new shares, which dilutes you. The
right adjustment is to *subtract* SBC from FCF, not add it back.
Many "adjusted FCF" presentations in software earnings releases
get this exactly backwards. Treat them accordingly.

[VISUAL: interactive/week20_earnings_lab.html]

**Stella:** The interactive lab embedded in the lesson lets you
flip between six representative companies. Apple, Microsoft,
Amazon, JPM, Coca-Cola, GE. For each one we plot diluted EPS and
FCF per share over fiscal years 2020 through 2024, and then a
separate bar chart of the per-year accrual, defined as EPS minus
FCF per share.

**Horace:** Apple is the textbook capital-light name — FCF runs
slightly above EPS most years, because non-cash charges and
working capital favour cash. The 2024 gap widened on a one-time
European tax charge that depressed reported earnings. Coca-Cola is
the steady-state benchmark — the two lines hug each other within
pennies year after year. That is what high-quality earnings look
like over time.

**Stella:** Microsoft's FCF lagged EPS in fiscal 2023 and 2024,
but not because of manipulation — because of a capex bulge for AI
data centres. That is an investment story, not a quality story.
Whether the capex earns its cost of capital is the right question,
and the gap is informative rather than damning. Amazon shows the
opposite case — huge non-cash D&A from AWS makes EPS look thin
while the underlying cash story is much better.

**Horace:** GE shows the messy real-world case, multi-year
restructuring with huge non-cash charges, where FCF is telling the
truth about the underlying industrial businesses better than
reported EPS does. JPM is in there as a reminder — banks do not
have a meaningful FCF in the industrial sense. Use ROTCE for
banks, [Week 19](week19_corporate_finance.md) covered it.

---

**[SECTION 5 — THE FIVE RED FLAGS — 14:00]**

**Stella:** A short list of earnings-quality red flags. Most of
the forensic accounting work in the wild is a variation of these
five.

**Horace:** One. Days sales outstanding rising faster than
revenue. DSO is receivables divided by daily revenue. If revenue
grew twelve percent and DSO grew thirty, the company is "selling"
to customers who are not yet paying. That is the most common
precursor to a revenue restatement.

**Stella:** Two. Days inventory outstanding rising faster than
revenue. Inventory builds either because the company is producing
ahead of demand — sometimes legitimate — or because what was
already produced is not selling, which is the bad version. Either
way, it is cash going into the warehouse instead of into the bank.

**Horace:** Three. Capitalisation of costs that should be
expensed. WorldCom's fraud was, mechanically, exactly this —
eleven billion dollars of network operating expense moved to the
balance sheet as capital. R&D, software development, content
production, "integration" costs after acquisitions. The more cost
a firm moves to the balance sheet, the higher today's earnings and
the lower tomorrow's.

**Stella:** Four. Recurring "one-time" charges. A company taking a
restructuring charge in three out of four years is not
restructuring; it is telling you the underlying earnings power is
below the "adjusted" headline. The charges are real costs that
keep getting labelled as not-real-costs.

**Horace:** Five. The accrual ratio itself. Net income minus
operating cash flow, scaled by assets, year after year. A
persistent positive gap is a quality concern. A persistent
*negative* gap — FCF above EPS — is the opposite signature, the
capital-light business with non-cash charges weighing on reported
earnings.

**Stella:** None of these red flags is deterministic. Each has a
legitimate version. But in a screen, firms that flunk three of the
five tests have a materially worse forward return distribution
than firms that pass them all.

---

**[SECTION 6 — LATE-CYCLE DISPERSION, 2026 — 16:00]**

**Horace:** Where this takes us, in April 2026. Through 2024 and
into 2025, the EPS-versus-FCF dispersion in the S&P 500 widened.
Reported earnings continued to grow at eight to ten percent per
year. Operating cash flow growth slowed to three to four. Some of
that gap is real — AI capex is genuinely investment, not
manipulation. Some of it is the late-cycle pattern — DSO and DIO
drifting up, "adjusted" metrics drifting further from GAAP, share
buybacks juicing per-share earnings even as total cash flow
flatlines.

**Stella:** The contrarian read. The firms whose FCF is keeping
pace with EPS in this environment are getting a quality premium
that the headline EPS multiple does not yet fully reflect. The
firms whose EPS-FCF gap has widened for three years running are
tomorrow's accrual reversion candidates. That is the screen we run
for the quality tranche.

**Horace:** And this is structural,
not tactical. Cash-versus-accruals interpretation works in every
regime. It works hardest when the rest of the market has stopped
checking. Which, late in the cycle, they tend to do.

---

**[OUTRO — 17:30]**

**Stella:** Three takeaways for the week.

**Horace:** One. Accruals equals net income minus operating cash
flow. The Q1 minus Q5 spread on accruals-to-assets has been worth
roughly seven to ten percentage points per year, and is one of the
most replicated alphas in finance.

**Stella:** Two. Post-earnings-announcement drift exists. The
print matters for the next sixty days, not just the next twenty-
four hours. Top quintile drifts up about two to three percent;
bottom quintile drifts down about the same. The fade comes around
the next pre-announcement window.

**Horace:** Three. Free cash flow, multi-year averaged, is the
right input to valuation. Watch the accrual ratio over time.
Rising DSO, rising DIO, capitalised costs, recurring "one-times,"
persistent positive accrual gap — three of those five flunked is
worth excluding from the long book.

**Stella:** Next week, [Week 21](week21_valuation_dcf.md) — the
discounted cash flow model. Now that we know which cash flow to
trust, we can put it in a spreadsheet and discount it.

**Horace:** Cash is the fact. Earnings are the opinion. Trust the
cash line.
