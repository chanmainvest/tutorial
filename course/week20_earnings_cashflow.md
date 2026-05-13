# Week 20: Earnings vs Cash Flow — Drift, Accruals, and Why FCF Beats EPS

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Earnings are an opinion. Cash is a fact. That sentence is older than
any of the textbooks that quote it, and it is still the single most
useful sentence in fundamental investing.

Reported earnings per share — the number on the wire at 4:01 PM
Eastern that the algorithms react to in milliseconds — is the output
of dozens of accounting choices. When to recognise revenue. How fast
to depreciate. What to capitalise versus expense. How much to
reserve for bad debts. Each choice is, individually, defensible.
Stacked together, they create enough latitude that the same
underlying business can print a $2.10 EPS or a $1.85 EPS depending
on the mood of the CFO and the patience of the auditor.

Free cash flow is harder to fake. Cash either showed up in the bank
account, or it did not. The cash flow statement is not free of
accounting judgement — classification of operating versus investing
flows is genuinely ambiguous in places — but the *level* of cash
moves much less than the level of reported earnings under management
discretion. That asymmetry is why this week matters:

1. **Two of the most durable academic anomalies are about earnings
   quality, not earnings level.** Bernard & Thomas (1989) documented
   the post-earnings-announcement drift — stocks with positive
   surprises continue drifting up for sixty days, stocks with
   negative surprises continue drifting down. Sloan (1996)
   documented the accruals anomaly — firms whose earnings are mostly
   accruals underperform firms whose earnings are mostly cash by
   roughly seven to ten percentage points per year over the
   following year. Both anomalies have been replicated dozens of
   times. Both have weakened since publication. Neither has
   inverted.

2. **Almost every spectacular fraud is detectable from earnings
   quality.** Enron, WorldCom, Wirecard, Luckin, Valeant. In each
   case, the gap between reported earnings and operating cash flow
   was screaming for years before the headline. Reading the gap is
   not a substitute for an audit. It is a way to never own the
   companies the auditor will eventually have to disown.

3. **Free cash flow is what valuation actually discounts.** The DCF
   model in [Week 21](week21_valuation_dcf.md) discounts FCF, not
   EPS. A company whose EPS is growing while FCF is shrinking is, by
   that model, becoming less valuable, not more — regardless of
   what the analyst note says.

4. **EPS-vs-FCF dispersion widens late in the cycle.** When growth
   is getting harder to find, earnings management gets more
   aggressive. Receivables stretch out. Inventory builds. Costs get
   capitalised. Buybacks juice EPS even as FCF flatlines. The
   dispersion is itself a regime signal.

This is one of the structural alpha sources in this course:
cash-versus-accruals interpretation. It is
not a secret. It is not crowded out either, because most of the
market still trades on the headline number.

---

### 2. What You Need to Know

#### 2.1 The Identity: Accruals = Earnings − Cash Flow

Start with arithmetic. For any period:

- Net income = Operating cash flow + Total accruals
- Total accruals = Net income − Operating cash flow

That is not a model. That is the definition. Operating cash flow is
already net income with the accruals stripped out — depreciation
added back, working-capital changes adjusted, deferred tax adjusted.
What is left over after the bridge from net income to OCF is, by
construction, accruals.

Accruals are not bad. They exist for a reason. Revenue earned but
not yet collected — receivables — is a real asset. Inventory built
ahead of demand is a real economic activity. Depreciation, the
largest single accrual at most industrial firms, is an honest
attempt to match an asset's cost to the periods that asset is
producing.

The problem is that accruals are *also* the lever managers reach
for when the quarter is short. Every line on the bridge from net
income to OCF is a discretionary judgement, and every one of them,
when pushed hard enough, increases reported earnings without
increasing real cash.

**Two ways to compute accruals for a stock screen:**

- **Balance-sheet method (Sloan):** change in non-cash current
  assets, minus change in current liabilities (excl. short-term
  debt), minus depreciation. Scale by average total assets. Sort
  firms into quintiles annually. Long Q1 (lowest), short Q5
  (highest).
- **Cash-flow method:** simply `(Net income − Operating cash flow) /
  average total assets`. Equivalent in spirit, slightly cleaner
  since 2002 when SFAS rules tightened.

The accruals anomaly is shown below:

![Bar chart: average annual one-year-ahead return for the five quintiles of accruals-to-assets, US-listed firms, 1990-2020. Quintile 1 (lowest accruals) averages 16.8%, Q2 14.2%, Q3 12.4%, Q4 10.1%, Q5 (highest accruals) 7.6%. Cross-sectional average around 12%. Spread Q1 minus Q5 is roughly 9% per year. Quintiles are colour-graded from green (Q1) to red (Q5).](../image/week20_accruals_anomaly.png)

The Q1-minus-Q5 spread is the academic estimate of the alpha. In a
real portfolio, half of it gets eaten by transaction costs, capacity
limits, and short-borrow fees on the Q5 leg. But even after that,
this is one of the best risk-adjusted long-short signals ever
documented in equity markets.

#### 2.2 The Post-Earnings-Announcement Drift (PEAD)

The PEAD is the closest cousin to the accruals anomaly. Bernard &
Thomas (1989) ranked every quarterly earnings announcement by
standardised unexpected earnings (SUE) — the surprise relative to
analyst consensus, divided by the historical standard deviation of
that surprise. Top quintile vs bottom quintile, post-announcement
returns over sixty trading days, averaged over thousands of
announcements: the result is stable enough to be boring.

![Schematic line chart of cumulative abnormal return over 60 trading days after the earnings release. Top quintile (positive surprise) drifts upward in a concave path to roughly +3.6%; bottom quintile drifts to roughly -2.9%; middle quintile sits near zero. The market reaction on Day 0 is incomplete; the drift continues for two to three months before fading.](../image/week20_pead_drift.png)

The drift is incomplete absorption of news. The market reacts on
Day 0 — the day of the release and the conference call — but the
reaction is, on average, only about two thirds of what it should
be. The remaining third leaks out over the next sixty days as
analyst revisions catch up, as the next quarter's pre-announcement
narrows expectations, and as slower investors finally trade on what
fast ones already saw.

Why does this not get arbitraged away? Three reasons that show up
across all of the persistent earnings anomalies:

- **Limits to arbitrage.** Borrow on the Q5 leg is genuinely
  expensive. Many of the most accrual-heavy firms are small-cap or
  mid-cap with shallow short-borrow markets. The frictions eat the
  alpha for funds that need to size up.
- **Career risk.** A long-short manager whose Q1 leg has a six-month
  drawdown will be redeemed before the academic mean-reversion
  arrives. Fading the crowd is correct on average and dangerous in
  any individual year.
- **The signal is slow.** PEAD is a sixty-day phenomenon. The
  accruals anomaly is a twelve-month phenomenon. Most of the market
  is trading on a one-day phenomenon: the print versus the
  consensus. The slow signals are not crowded by the fast traders.

This connects to the two sides of price discovery: momentum and
mean-reversion. PEAD is fundamentally a momentum effect — the stock
that surprised up keeps drifting up — because the *information* is
travelling through the market slower than the price. The accruals
anomaly is a mean-reversion effect — earnings inflated by accruals
revert toward cash over the following year. They sit on opposite
sides of the same coin.

#### 2.3 Free Cash Flow, Carefully Defined

FCF gets quoted three different ways in the wild. You need to know
which one you are reading.

- **FCF to the firm (FCFF) = OCF − Capex.** The plain definition.
  The cash left over after maintaining and growing the asset base,
  before any return to debt or equity holders. This is the number
  the DCF model wants.
- **FCF to equity (FCFE) = FCFF − Net debt repayment + Net debt
  issuance.** The cash left over for *equity* holders specifically.
  Used in dividend-discount frameworks.
- **"Adjusted FCF" (whatever management says it is).** Sometimes
  adds back stock-based compensation. Sometimes excludes
  acquisition-related capex. Sometimes excludes "one-time"
  working-capital movements that have shown up four years in a row.
  Treat all adjusted FCF the way you treat adjusted EBITDA: with
  one eyebrow permanently raised.

For screening, use FCFF. Use a multi-year average — three to five
years — because single-year FCF is noisy from working-capital and
capex timing. The Apple FY2014-FY2024 chart from
[Week 8](week08_financial_statements.md) is the canonical example:
EPS and FCF/share track within pennies most years, and where they
diverge (FY2020 working-capital release; FY2024 EU tax charge), the
divergence has a clean accounting explanation.

The interactive lab below lets you flip between six representative
companies and see the EPS-vs-FCF profile and the per-year accrual:

[Open: Earnings vs Cash Flow Lab](interactive/week20_earnings_lab.html)

The pattern matters more than any single year. Apple's FCF runs
above EPS most years — capital-light, working-capital favourable.
Coca-Cola's two lines hug each other within pennies — steady-state
brand-rent business. Microsoft's FCF lagged EPS in FY2023-2024 not
because of manipulation but because of the AI capex bulge — that is
an investment story, not a quality story. Amazon shows the textbook
cash-light-but-EPS-light case where huge non-cash D&A makes earnings
look thin while the cash story (post-2022 capex moderation) is what
actually matters. GE shows the opposite — multi-year restructuring
charges depress EPS far below the underlying cash. JPM is a bank;
"FCF" for a bank is conceptually meaningless, and you need ROTCE
instead (covered in [Week 19](week19_corporate_finance.md)).

#### 2.4 Earnings Quality Red Flags — The Five That Matter

A short list. Most quality work in the wild is a variation of
these five.

**1. Days sales outstanding (DSO) rising faster than revenue.** DSO
= receivables / (revenue / 365). If revenue grew 12% and DSO grew
30%, the company is "selling" to customers who are not yet paying.
Revenue is being recognised earlier in the cycle, or to customers
who will not actually pay. Aggressive DSO is the most common
precursor to a revenue restatement.

**2. Days inventory outstanding (DIO) rising faster than revenue.**
DIO = inventory / (COGS / 365). Inventory builds either because the
company is building ahead of expected demand (sometimes legitimate)
or because the inventory the company already produced is not
selling (usually the bad version). Either way, it is a use of cash
that does not show up on the income statement until the markdown
finally hits COGS.

**3. Capitalisation of costs that should be expensed.** R&D under
US GAAP is mostly expensed; under IFRS, much of it can be
capitalised. Software development costs, content production costs,
acquisition-related "integration" costs — the more cost a firm
moves to the balance sheet, the higher today's earnings and the
lower tomorrow's. WorldCom's fraud was, mechanically, this exact
move on $11B of network operating expense.

**4. Recurring "one-time" charges.** A company that takes a large
restructuring charge in three out of four years is not
restructuring; it is telling you the underlying earnings power is
lower than the "adjusted" headline. The charges are real cost. They
just keep getting flagged as not-real-cost.

**5. The accrual ratio itself.** `(Net income − OCF) / Net income`,
or scaled by average assets, year after year. A persistent positive
gap is a quality concern. A persistent *negative* gap (FCF > EPS)
is the opposite — the signature of a capital-light business with
non-cash charges dragging on earnings.

None of these are deterministic. Each has a legitimate version. But
in a screen, the firms that flunk three of the five tests have a
materially worse forward return distribution than the firms that
pass them all.

#### 2.5 Late-Cycle Dispersion — Why This Week Matters in 2026

Through 2024 and into 2025, the EPS-vs-FCF dispersion in the S&P
500 widened. Reported earnings continued to grow at 8-10% per year
while operating cash flow growth slowed to 3-4%. Some of that gap
is real — AI capex is genuinely investment, not manipulation. Some
of it is the late-cycle pattern — DSO and DIO drifting up,
"adjusted" metrics drifting further from GAAP, share buybacks
juicing EPS while FCF flatlines. The cycle is not the same every
time. The gap behaves roughly the same every time.

The contrarian read: the firms whose FCF is keeping pace with EPS
in this environment are getting a quality premium that the headline
EPS multiple does not yet reflect. The firms whose EPS-FCF gap has
widened for three years running are tomorrow's accrual reversion
candidates. This is why "look at cash, not earnings" is a
structural alpha source, not a tactical one. It
works in every regime. It works hardest when the rest of the
market has stopped checking.

---

### 3. Common Misconceptions

1. **"FCF is always better than EPS."** Wrong. FCF is more useful
   for *quality* questions; EPS is more useful for *profitability*
   comparisons within a stable industry. A capex-heavy firm in
   year-three of a four-year build will show ugly FCF and fine EPS.
   That is not a quality problem. It is a timing problem.

2. **"Accruals are accounting fraud."** Wrong. Accruals are
   accounting. Without them you would have cash accounting, which
   is useless for businesses with multi-period contracts, inventory,
   or long-lived assets. The question is not whether accruals
   exist; it is whether they are growing faster than economic
   reality.

3. **"PEAD has been arbitraged away."** Mostly wrong. The drift has
   shrunk — Bernard & Thomas reported a 60-day spread of 4-5% in
   the 1980s; modern estimates are 2-3% for the top vs bottom
   quintile. But the asymmetry has not flipped, and the drift is
   still detectable in every replication through 2024.

4. **"A negative FCF year is always bad."** Wrong. Amazon ran
   negative or near-zero FCF for most of its first decade as a
   public company while building infrastructure that is now
   generating tens of billions per year. Negative FCF in service
   of a high-return investment programme is great. Negative FCF
   because the working capital is hemorrhaging is fatal. Look at
   the *cause*.

5. **"EPS beats are what matter."** Misleading. The EPS print
   versus consensus matters in the *next 24 hours*. The PEAD says
   it also matters in the next 60 days. But the multi-year story —
   quality of those earnings, conversion to cash — is what
   compounds the stock price over a 5-10-year hold.

6. **"Stock-based compensation is non-cash so I should add it
   back."** Wrong, mostly. SBC is a real cost — the firm is giving
   away part of the company. The cash that would have been spent on
   payroll is instead being raised by issuing new shares, which
   dilutes you. The right adjustment is to subtract SBC from FCF,
   not add it back, and many "adjusted FCF" presentations get this
   exactly backwards.

7. **"Revenue can't be faked."** Wrong. Revenue is the most
   audit-tested line, but channel-stuffing, bill-and-hold,
   round-trip transactions, and aggressive percentage-of-completion
   accounting have all been used to inflate revenue in real cases.
   The DSO check exists precisely because revenue *can* be pulled
   forward.

8. **"If a company beats earnings, it's a good investment."**
   Wrong. The PEAD says you get some drift after a beat, on
   average, in excess of the immediate reaction. But the average
   masks dispersion — beats that come with deteriorating cash flow
   tend to mean-revert hard. Beat plus rising accruals is a worse
   profile than in-line plus stable accruals.

9. **"FCF yield is the new P/E."** Useful, not magical. FCF yield
   (FCF / market cap) is a cleaner valuation metric for mature
   non-bank businesses than P/E. For high-growth firms with
   negative FCF, it is meaningless. For banks and insurers, it is
   meaningless. For asset-heavy capex-cycle firms, single-year FCF
   yield is noisy — average over five years.

10. **"Forensic accounting is for activists, not retail
    investors."** Wrong. The five red flags above are computable
    from the standard 10-K filing in 30 minutes per company. They
    will not catch a sophisticated fraud. They will catch the
    obvious ones, and they will tell you which 10-Ks deserve
    another hour of your time.

---

### 4. Q&A Section

**Q1: How quickly can I screen for accruals on US-listed
equities?**
A: With a paid data feed (Compustat, FactSet, S&P Capital IQ) the
ratio is one column and the quintile sort is one query. With free
sources, pull (Net Income − OCF) from the 10-K cash flow statement
for each name in your watchlist; scale by average total assets. A
twenty-name watchlist takes an hour the first time and ten minutes
per quarter to refresh.

**Q2: Should I short the high-accrual names?**
A: Probably not as a retail investor. Short borrow on small- and
mid-cap names is expensive, mark-to-market drawdowns can be sharp,
and short squeezes happen even on terminal cases. The cleaner
implementation is to screen those names *out* of your long book
and concentrate on the long-cash quality side. That captures most of
the asymmetry without the operational complexity — long-cash quality
goes in the core tranche; the short side, if you run it at all, sits
in a specialty tranche.

**Q3: Why does PEAD drift continue for 60 days and not longer?**
A: Around the 60-day mark the next quarter's pre-announcement
window opens and forward expectations start being discounted into
the price. The "old" surprise is no longer the marginal news.
Empirically the drift fades into the next earnings cycle, not after
a fixed calendar window.

**Q4: Is the accruals anomaly the same as the quality factor?**
A: Related, not identical. The "quality" factor as MSCI and others
construct it usually combines accruals, gross profitability,
leverage, and earnings stability. Accruals is one input. The pure
accruals anomaly is more concentrated than the blended quality
factor and historically had a bigger Sharpe.

**Q5: What about non-US markets?**
A: The accruals anomaly has been replicated in most developed
markets — UK, Japan, Australia, Western Europe — at varying
strengths. In emerging markets the data quality is weaker and the
shorting frictions worse. Our investable universe in this course is
US-listed equities anyway, so this is not a real constraint for us.

**Q6: How do I use FCF yield in valuation?**
A: For mature non-bank firms, an FCF yield (5-year average FCF
over current market cap) above the long Treasury yield plus a
sensible equity premium is a reasonable starting screen. So if
10-year Treasuries are at 4.5% and you want a 4-5% equity premium,
you are looking for FCF yield above 8.5-9.5%. Below that you are
paying for expected growth; above that you are being paid to wait.

**Q7: Why did Microsoft's FCF lag EPS in 2024?**
A: Capex. Microsoft is spending $50-60B per year on AI data
centres, chips, and cooling infrastructure. That capex is real and
is flattening FCF even though OCF and EPS are at all-time highs.
Whether the AI capex earns its cost of capital is the real
question — the FCF gap itself is informative but not by itself a
quality problem.

**Q8: What's the difference between "earnings management" and
"earnings manipulation"?**
A: Mostly intent and degree. Both shift earnings between periods
using legal accounting choices. Management is done quietly to
smooth quarterly volatility — almost every public company does
some of it. Manipulation is done aggressively to hit a target the
company would otherwise miss, and shades into fraud when the
choices stop having a defensible accounting basis. The
earnings-quality red flags catch both.

**Q9: How does this lesson interact with valuation (Week 21)?**
A: Directly. The DCF in [Week 21](week21_valuation_dcf.md)
discounts free cash flow, which means everything you learned this
week about the *quality* of FCF feeds straight in. Two firms with
identical projected FCF deserve different multiples if one has a
clean accruals profile and the other does not. The market does not
always price that gap; you can.

**Q10: What about software companies with deferred revenue and
SBC?**
A: Two complications, opposite directions. Deferred revenue (cash
received for services not yet rendered) inflates OCF relative to
EPS; that is a *legitimate* tilt, not a quality issue, as long as
the underlying contracts are renewable. SBC, as discussed in
misconception #6, is a real cost and should be subtracted from FCF
to get the true equity-holder cash. The net effect varies by firm
— modern SaaS often shows very high OCF and middling SBC-adjusted
FCF.

**Q11: Is there a "bad" version of FCF > EPS?**
A: Rarely, but yes. A firm that is shrinking — drawing down
working capital and not replacing assets — can post FCF above EPS
for a year or two while the business is being liquidated. The clue
is declining revenue and declining capex. The healthy version of
FCF > EPS is a stable or growing capital-light business. The
unhealthy version is a melting ice cube monetising its inventory
and receivables one last time.

**Q12: How much weight should I put on a single quarter?**
A: Less than the headlines do. PEAD says the print does matter for
the next 60 days. But the 12-month forward return is much more
correlated with multi-year accrual quality and cash-flow conversion
than with any single quarter's surprise. Quarter-to-quarter
volatility is mostly noise; the trend in EPS-vs-FCF dispersion is
signal.

---

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
