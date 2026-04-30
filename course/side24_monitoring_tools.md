# Side Lesson 24: Portfolio Monitoring Tools

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The model from Week 52 ends at "build the portfolio." Real life starts there. A
portfolio you cannot see clearly is a portfolio you cannot run. The job after
the IPS is signed is to inspect — at most monthly, never daily — whether the
thing you wrote down is the thing you actually own. That is what monitoring
tools do.

1. **Drift kills good plans.** A 35/25/15/5/10/5/5 model L4 portfolio rebuilt
   from Week 52 will drift on its own. After one strong equity year the growth
   tranche bulges to 42% and the cash sleeve thins to 3%. Without a tool that
   measures drift against target — sleeve by sleeve — you cannot tell whether
   you have crossed the +/-5pp band that triggers a trim.

2. **You cannot see overlap by squinting.** Holding VTI, VOO, SPY, QQQ, and
   SCHD looks like five funds. The X-Ray says it is mostly one fund: AAPL,
   MSFT, NVDA, AMZN, META, GOOG appear in all five at high weight. Sector
   double-counting is the most common silent failure of retail portfolios, and
   it is invisible without a holdings-level pass-through.

3. **Fees are flat-rate compounding tax (SOUL #1).** A 0.50% expense ratio on a
   $500k portfolio is $2,500 a year, every year, automatically — silently
   debited and never invoiced. The tools that aggregate every account and
   compute *expense-weighted average ER* are the ones that turn the abstract
   "fees matter" into a specific dollar number you can decide whether to pay.

4. **Behavioural guardrails come from automation.** Paradoxically, having
   *better* monitoring lets you check *less*. When alerts fire only on band
   breaches and the dashboard lives on a fixed monthly cadence, the urge to log
   into your brokerage every morning fades. The tool watches; you live your
   life. That is exactly the discipline SOUL #12 demands — staying solvent
   long enough for the strategy to compound.

---

### 2. What You Need to Know

#### 2.1 Portfolio Visualizer — the free institutional terminal

[portfoliovisualizer.com](https://www.portfoliovisualizer.com) is the single
most useful free tool in the retail kit. Five modules deserve your attention:

- **Backtest Portfolio.** Enter weights and ticker list, pick a start date,
  and the tool returns annualised return, vol, max drawdown, Sharpe, Sortino,
  Calmar, and a year-by-year table. It runs against monthly data back to 1985
  for most ETFs, with mutual fund proxies extending some series further. You
  can compare three portfolios side by side — exactly what Week 04 / Week 15 /
  Week 52 expect you to do before changing weights.
- **Asset Class Backtest.** Same engine, but with reconstructed broad asset
  classes (US large, US small value, intl developed, EM, REITs, gold,
  long-bond, T-bill) reaching back to 1972. This is how you stress-test a
  60/40 or All-Weather sleeve against the 1970s inflation regime that doesn't
  exist in the ETF window.
- **Factor Regression.** Runs Fama-French 3, Carhart 4, and FF 5 + momentum
  on any ticker or portfolio. Output: alpha (with t-stat), beta exposures to
  market / size / value / momentum / quality / low-vol. This is how you
  *prove* your factor tilt is doing what you paid the higher ER for.
- **Monte Carlo.** Forward simulation with capital-market assumptions you can
  override. Useful for SWR stress and sequence-of-returns tail testing.
- **Asset Correlations.** Rolling and full-period matrices, with
  user-controllable window. Quick eyeball of the correlation collapse problem
  from Week 19.

The free tier covers all of the above. The paid tier ($30/month) adds
optimization and historical Sharpe rolling charts; for a retail investor the
free tier is enough indefinitely.

#### 2.2 Morningstar Instant X-Ray — the overlap detector

X-Ray is the free tool buried inside a Morningstar account. Paste your
ticker list and weights and it returns:

- **Asset-class breakdown** — how much US stock, intl stock, bond, cash, other
  you actually own once funds are flattened to holdings.
- **Sector allocation** — eleven GICS sectors, with the S&P 500 reference
  alongside.
- **Region allocation** — North America / Europe / Japan / Asia ex-Japan /
  Latin America / Middle East / Africa.
- **Top 10 holdings** — across the *entire* portfolio after fund pass-through.
  This is where "I own VTI and SCHD" turns into "27% of my equity is in seven
  US mega-caps."
- **Stock overlap** — a number between 0% and 100% that quantifies how much
  of two funds' weighted holdings are the same names.

If you take only one thing from this lesson it is the overlap number. A retail
portfolio of VTI + VOO + SPY + IVV reads as four funds and is in fact one fund
with a 99.5% overlap. The image script `side24_overlap_detection.py` walks
through a 5-fund example where the pairwise overlap heatmap shows ~60% top-ten
overlap on the diagonal cluster.

#### 2.3 Empower (formerly Personal Capital) — the aggregator

Empower's free tools include an account aggregator that pulls from most US
brokerages, banks, and 401(k) providers via Plaid. Once linked it runs three
analytics that matter:

- **Retirement Planner.** Monte Carlo forward projection from your actual
  current balances and contribution rates.
- **Investment Checkup.** Asset-class breakdown across *all* accounts at once
  — the cross-account view that no single brokerage gives you. Compares to a
  target allocation and flags the gap.
- **Fee Analyzer.** The killer feature. Aggregates every fund's expense ratio
  weighted by holding size and reports the dollar fee impact over your time
  horizon. The version that surfaces the difference between a 0.65% advisor
  fee and a 0.05% DIY portfolio over thirty years has converted more retail
  investors away from full-service advisors than any blog post ever has.

The catch: Empower's business model is a wealth-management lead funnel.
Expect calls. Decline politely; the tools remain free.

#### 2.4 Brokerage built-ins — Schwab, Fidelity, Vanguard

Every major US brokerage has shipped a portfolio-analytics dashboard in the
2020-2025 wave:

- **Schwab Portfolio Checkup** — pulls into the X-Ray engine via partnership
  and surfaces sector / asset class / overlap views inside your Schwab login.
- **Fidelity Portfolio Analysis** — strong on tax-lot view and unrealised
  gain/loss reporting. Their "Compare to Benchmark" panel produces a clean
  rolling-return comparison vs. any index.
- **Vanguard Portfolio Watch** — basic but free; useful if your portfolio is
  Vanguard-only.

Use the brokerage tool when you want to look at the accounts at *that*
brokerage. Use Empower or X-Ray when you need the full cross-account view.

#### 2.5 The DIY spreadsheet — the tool you actually run

Despite the polished web tools, most disciplined retail investors I know run
a Google Sheet or Excel workbook as their primary monthly dashboard. Three
reasons: it owns no opinions about your asset categories, it never changes
its UX out from under you, and it works offline.

A minimum-viable monthly sheet has six columns: ticker, target weight, target
dollars, current dollars, drift in pp, action (trim / add / hold). Underneath
that, three computed cells: total portfolio value, expense-weighted ER, and
trailing-twelve-month return vs. a 60/40 reference. That's it. The image
script `side24_dashboard_template.py` shows what this looks like rendered as
four panels: wealth path, drawdown, asset-class breakdown, and rolling fee
spend.

`GOOGLEFINANCE("VTI", "price")` and friends pull live prices into Google
Sheets at 20-minute delay, free, forever. There is nothing the paid tools do
in their dashboard panes that a column of `=GOOGLEFINANCE()` calls cannot
replicate.

#### 2.6 The monthly review checklist

The tool is useless without the cadence. Once a month, on a fixed day:

1. **Total return YTD and trailing 12m.** Vs. the 60/40 reference. One
   sentence written in a notes column.
2. **Realised volatility and trailing peak drawdown.** From the spreadsheet
   or PV. Compare against the IPS-stated maximum drawdown.
3. **Sleeve drift.** For each of the seven Week-52 sleeves: is it within +/-5
   percentage points of target? Any breach triggers a trim/add of *just* that
   sleeve, ideally directed via new contributions before any sales.
4. **Factor exposures.** Quarterly is enough here — run the PV factor
   regression on your tilt sleeves (MTUM, AVUV, QUAL, USMV) and confirm beta
   to the named factor is still > 0.5 and t-stat > 2. Decay below that
   threshold for two consecutive quarters triggers the half-weight stop-rule.
5. **Fees paid year-to-date.** Expense-weighted ER * portfolio value, prorated
   for the year. Watch for advisor-managed accounts and fund-of-fund wrappers
   that slip in via 401(k) target-date defaults.
6. **Rebalancing band breaches.** Anything over the 5pp band gets actioned
   *that day*. Anything under stays untouched until next month.

The interactive `side24_dashboard.html` lets you build a 5-ETF portfolio from
a 12-fund dropdown and see asset-class breakdown, expense-weighted average,
and pairwise top-10 overlap in real time — a working miniature of the retail
toolkit described above.

---

### 3. Common Misconceptions

1. **"More tools means more insight."** No. Five overlapping dashboards is
   five different framings of the same numbers, and the dashboard you check
   at 9am gets read; the four others rot. Pick one primary (spreadsheet or
   Empower), one analytics deep-dive (Portfolio Visualizer), and one overlap
   checker (Morningstar X-Ray). Stop there.

2. **"My brokerage already shows me everything."** Only for accounts at *that*
   brokerage. The cross-account view — including the spouse's IRA, the prior
   employer's 401(k), and the HSA — is exactly what no single brokerage gives
   you. Aggregator or spreadsheet is the only way.

3. **"Daily checking keeps me informed."** It keeps you anxious. Studies of
   active retail traders find a near-monotonic relationship between login
   frequency and underperformance (Barber & Odean 2000). Set a fixed monthly
   day, do the checklist, close the tab.

4. **"X-Ray is for fund-of-funds, my ETF portfolio is clean."** Wrong. SCHD,
   VYM, DGRO, and NOBL look like four different income strategies. Run them
   through X-Ray: 50%+ holdings overlap because they all filter the same S&P
   500 universe for dividend characteristics.

5. **"The expense ratio is the only fee I pay."** No. The full menu is ER +
   12b-1 + transaction costs inside the fund + bid-ask + advisory fee +
   account fees. Empower's fee analyzer surfaces the first; only Form ADV
   reading and tax-return inspection surfaces the rest.

6. **"Monte Carlo says 87% success — I'm safe."** Monte Carlo assumes the
   future return distribution looks like the historical one. SOUL #2 says it
   *won't*. Treat the simulation as a sensitivity tool, not a probability
   forecast.

7. **"Free tools are limited; the paid versions show the truth."** The paid
   tier of Portfolio Visualizer adds optimization (which over-fits) and a few
   convenience features. The truth is in the free tier. Pay only when you've
   exhausted what it gives you.

8. **"Rebalancing bands are arbitrary; I'll just rebalance annually."**
   Calendar-only rebalancing is fine in calm markets. In 2008 or 2020 a
   strict-calendar portfolio missed the 25-30% mid-year band breach where the
   real rebalancing premium lives. Hybrid (annual + 5pp band) captures both.

---

### 4. Q&A Section

**Q1. How often should I actually log in?**
A. Once a month for the dashboard checklist. Once a quarter for the deeper
factor regression and stop-rule check. Annually for the full IPS rewrite.
That's it. More than this is cost without benefit.

**Q2. Is Portfolio Visualizer's data accurate?**
A. For monthly total returns of US-listed ETFs back to inception, yes — it
sources from CRSP and the funds' own filings. The asset-class reconstructions
back to 1972 use academic indices (Fama-French, Damodaran-style splices) that
are accurate in shape but not investable in real life. Use them for shape, not
forecast.

**Q3. Empower or a spreadsheet?**
A. Both. Empower for the cross-account aggregation and fee analyzer.
Spreadsheet for the monthly drift check and sleeve action plan. They serve
different purposes; the spreadsheet is your operating tool, Empower is your
audit tool.

**Q4. What overlap percentage is too much?**
A. As a working rule, any pair of funds with > 50% top-10 holdings overlap is
double-counting. Either drop one or accept that you have one larger position
in the shared names. The five-S&P-500-ETF portfolio is the reductio: 99.5%
overlap, paying 4x the ER for the same exposure.

**Q5. Should I pay for Morningstar Premium?**
A. No, for monitoring purposes. The X-Ray tool is free with a basic account.
Premium adds analyst star ratings (which Morningstar's own studies show have
little forward predictive power) and screener access. The free X-Ray pane is
the only Morningstar product that earns a regular spot in the workflow.

**Q6. Does the brokerage's "risk score" mean anything?**
A. No. Schwab, Fidelity, and Empower each have a proprietary "risk score"
that combines vol, beta, and concentration into a single 0-100 number. The
weights are opaque, the methodology is unverified, and the score is mainly a
sales tool to flag accounts as candidates for managed services. Ignore.

**Q7. How do I track tax-loss harvesting opportunities?**
A. Brokerage tax-lot view + spreadsheet. Sort lots by unrealised loss
descending; any lot below cost by more than $500 and held outside the 30-day
wash-sale window is a candidate. See Side Lesson 04 for the full TLH
mechanics. No mainstream monitoring tool surfaces TLH well — the brokerage
tax-lot screen is your primary source.

**Q8. Can I automate alerts?**
A. Yes. Most brokerages let you set price alerts; combine with a Google
Sheet that flags drift > 5pp in conditional formatting and emails you on
trigger via a 10-line Apps Script. That's the entire automation budget. Going
beyond it (real-time triggers, mobile push) is exactly the dopamine pump that
SOUL #12 warns against.

**Q9. What about crypto holdings — none of these tools handle BTC?**
A. Empower aggregates Coinbase. Most others ignore crypto. The simplest fix:
a manual cell in your spreadsheet for the BTC sleeve, refreshed monthly. The
5% sizing from Side Lesson 09 doesn't need second-by-second precision.

**Q10. The dashboard says I'm 8pp overweight equity. Do I sell or wait?**
A. Sell — partially. The 5pp band trigger means action *now*, not "wait for
year-end." Direct new contributions to the under-target sleeves first; if
that doesn't close the gap within one month, sell down enough of the
overweight sleeve to land back inside the band. Tax-lot pick the highest
basis lots in taxable accounts; in IRAs there is no tax cost so trim freely.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** The Portfolio Dashboard That Actually Works (Side 24)
**RUNTIME TARGET:** ~11 minutes
**HOSTS:** Horace, Stella

---

**HORACE:** Welcome back. Side lesson 24. We've spent fifty-two weeks
designing a portfolio. Today we talk about the boring half — keeping it
running. The tools you actually use to look at the thing once a month.

**STELLA:** And the rule I want viewers to take away first: the tool is
useless without the cadence. Pick a day, run the checklist, close the tab.

**HORACE:** That. So today's plan: four free tools that matter, then the
six-item monthly checklist, then we look at our two images and the
interactive dashboard.

---

**[VISUAL: image/side24_dashboard_template.png]**

**HORACE:** Start with the dashboard image. Four panels. Top-left, wealth
path versus a 60/40 reference — that's your "is the strategy working" line.
Top-right, drawdown — the question is, are you inside your IPS-stated
maximum drawdown number, or have you blown through it? Bottom-left,
asset-class breakdown versus target — that's drift. Bottom-right, fees paid
year to date.

**STELLA:** And every one of those panels can be reproduced in Google
Sheets with `GOOGLEFINANCE` calls. You don't need a SaaS product to see
this.

---

**HORACE:** The four tools.

Tool one: Portfolio Visualizer. Free. The free tier gives you backtest, asset
correlations, factor regression, Monte Carlo, and asset-class data back to
1972. That's the institutional terminal — for retail, free, forever.

Tool two: Morningstar Instant X-Ray. Free with a basic Morningstar account.
This is the overlap detector. Paste your fund list, get back asset-class
breakdown, sector breakdown, top-10 holdings across the whole portfolio, and
pairwise stock overlap.

**STELLA:** Which is the problem most retail portfolios don't know they
have.

**[VISUAL: image/side24_overlap_detection.png]**

**HORACE:** Look at this image. Five funds — VTI, VOO, SPY, QQQ, SCHD.
They feel like five different bets. The heatmap shows the pairwise top-10
overlap. VTI versus VOO: 99% — they are the same fund. VTI versus QQQ:
about 50% — Apple, Microsoft, Nvidia, Amazon, Meta, Alphabet are in both.
VOO versus SCHD: about 30% — even a "value income" ETF shares a third of
the top names with the S&P 500. Average pairwise overlap on this five-fund
portfolio: roughly 60%.

**STELLA:** Which means you are running one concentrated mega-cap bet, paying
four expense ratios for it, and *thinking* you have a diversified portfolio.

**HORACE:** Exactly. The X-Ray catches this in ten seconds. Squinting at
ticker tape doesn't.

---

**HORACE:** Tool three: Empower, formerly Personal Capital. Free aggregator.
Three features matter — the cross-account asset-class view, the fee
analyzer, and the retirement Monte Carlo. The fee analyzer is the killer.
It tells you what sixty basis points compounds to over thirty years on
your *actual* portfolio. That number has talked more retail investors out of
full-service advisors than any blog post.

**STELLA:** Caveat: Empower is a wealth-management lead funnel. They will
call you. Decline politely. The tools stay free.

**HORACE:** Tool four: your brokerage's built-in. Schwab Portfolio Checkup,
Fidelity Portfolio Analysis, Vanguard Portfolio Watch. Use these *for
accounts at that brokerage*. They don't see your spouse's IRA at a different
firm. That's where Empower or the spreadsheet picks up.

---

**HORACE:** Now the workflow most disciplined retail investors actually run
— and it isn't any of those four. It's a Google Sheet. Six columns: ticker,
target weight, target dollars, current dollars, drift in percentage points,
action. Three computed cells: total value, expense-weighted ER, trailing
twelve-month return.

**STELLA:** That's the operating tool. Empower is the audit tool. PV is the
deep-dive tool. X-Ray is the overlap-check tool. Four roles, one each, no
duplicates.

---

**HORACE:** The monthly checklist. Six items.

One. Total return year to date and trailing twelve months versus 60/40. One
sentence in a notes column.

Two. Realised vol and trailing peak drawdown. Inside the IPS number?

Three. Sleeve drift. Each of the seven Week-52 sleeves — within plus or
minus five percentage points of target?

Four. Factor exposures. Quarterly is enough. PV factor regression on your
tilt sleeves. Beta to the named factor still above 0.5? T-stat above 2?

**STELLA:** And if it isn't, that's the half-weight stop-rule from Week 50.

**HORACE:** Five. Fees paid year to date. ER times portfolio value,
prorated. Watch the 401(k) target-date defaults — they slip 0.6% in.

Six. Rebalancing band breaches. Anything over five percentage points gets
actioned *today*. New contributions go to under-target sleeves first.

---

**HORACE:** Now, the interactive. Pick five ETFs from a dropdown of twelve.
Watch the dashboard fill in: asset-class breakdown, sector breakdown,
expense-weighted average, pairwise overlap matrix. Try it.

**STELLA:** Try the all-S&P-500 portfolio first. VTI plus VOO plus SPY plus
IVV plus SCHX. Watch the overlap heatmap go red.

**HORACE:** Then try the model L4 from Week 52. VTI, BND, GLDM, IBIT, DBMF.
Overlap drops near zero, asset-class breakdown spreads across five buckets,
expense-weighted ER comes in around fifteen basis points.

**STELLA:** That's the difference between a portfolio that *looks*
diversified and one that is.

---

**HORACE:** Closing thought. The point of the dashboard is not to give you
something to look at. It's to give you permission to *not* look — between
review days. The tools watch the bands, you live your life, and on the
fixed monthly day you do the six-item walkthrough. That's the discipline
that compounds.

**STELLA:** Tools without cadence is just a hobby. Cadence without tools is
guessing. You need both.

**HORACE:** Side 24, monitoring tools. That's a wrap.

---
