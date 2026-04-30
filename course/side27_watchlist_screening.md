# Side Lesson 27: Building a Watchlist — Screens that Find Quality at Value

---

## Part 1: Reading Section

---

### 1. Why This Is Important

There are roughly **4,000** stocks listed on the major US exchanges
(NYSE + Nasdaq, excluding ADRs, micro-caps under $50M, and the OTC
ghost-mall). No retail investor — and very few institutional ones —
can read a 10-K and an earnings call transcript on every one of them
each year. The number you can actually own with conviction is not 4,000.
It is somewhere between 5 and 20.

The job of a screener is to walk the funnel for you. You start with
4,000 names, eliminate 95% with three or four numerical filters, hand
the survivors to your eyes and your spreadsheet, and end up with a
**watchlist of 10-15 names you actually understand** plus a tighter
**buy-list of 3-7 you currently own**. Doing this without a screener
is like trying to find a wedding dress by walking through every store
on Fifth Avenue. Doing it with one is like asking the saleswoman to
pull only the white silk size-6 gowns.

Four reasons to take screening seriously:

1. **Filter discipline beats stock-picking discipline.** Per SOUL #1,
   alpha is rare. The single highest-leverage decision you will make is
   *which 30 names enter your due-diligence queue*, not which one of
   those 30 you eventually buy. A bad shortlist makes good selection
   impossible; a good shortlist makes mediocre selection profitable.

2. **It mechanises Buffett's "circle of competence."** Every screen
   has a thesis embedded in it. A GARP screen embeds *I believe ROIC
   above the cost of capital, bought below 1.2x PEG, compounds*. A
   deep-value screen embeds *I believe statistical cheapness in
   solvent businesses mean-reverts*. Writing the screen forces you to
   write the thesis.

3. **Market caps do the heavy lifting.** US-listed equities (per SOUL
   #16) come with audited GAAP filings, deep secondary liquidity, and
   the SEC EDGAR plumbing that makes all of this work. Run the same
   process on a Shenzhen B-share index and the data layer breaks.

4. **It defends against narrative.** The best filter against
   "Cathie said it on CNBC" is not willpower; it is a numerical
   tripwire that says *PEG > 1.5 -> no further work*. Pre-committed
   filters convert the impulse buy into a process buy. (SOUL #12: the
   market can stay irrational longer than you can stay solvent — and
   longer than your conviction, too.)

![A funnel diagram showing 4,000 US-listed stocks narrowing in four steps: 250 pass the screen, 50 advance to deep-dive, 10 sit on the active watchlist, and 3 are currently owned. Each stage is labelled with the typical activity (filter, due diligence, valuation, position).](image/side27_screener_funnel.png)

The funnel above is the canonical pipeline: **filter -> due-diligence
-> watchlist -> position**. The numbers will not match yours exactly,
but the *shape* should — most names die in the first two stages.

---

### 2. What You Need to Know

#### 2.1 The Tool Stack — Free, Brokerage, and Paid

Three tiers of screener exist. The differences are not "feature
count" but **data depth, history length, and cross-sectional rigour.**

**Free tier (good enough for 90% of retail investors).**

- **Finviz** (`finviz.com`) — fastest screener on the open web. Eighty-plus
  fundamental + technical filters, real-time delayed quotes, sector
  heat-map. Free version capped at 20 screens; **Finviz Elite** at
  $39.50/month adds intraday data, backtesting, and email alerts.
- **Yahoo Finance Screener** — fewer filters, but free, ad-supported,
  and integrated with the Yahoo data layer. Useful for quick
  one-shot checks.
- **TradingView** — strongest if you also chart. Built-in screener
  with TradingView's technical indicators and 90+ fundamental fields.
  Free tier limited to one screen at a time.
- **Schwab StreetSmart Edge / Fidelity Active Trader Pro** — your
  brokerage already includes a screener for free. Schwab's covers
  about 60 fundamentals; Fidelity's adds proprietary "equity
  summary score" composites.

**Paid tier (worth it if you run weekly screens or hold >20 names).**

- **Stock Rover** ($28-$40/month, $79/yr Essentials) — 600+ metrics
  including 10 years of fundamentals, sector benchmarks, custom
  formulas, and GICS-aware ranking. The retail-investor gold
  standard for fundamental work.
- **TIKR.com** ($24-$30/month) — institutional-style data feed
  (S&P Capital IQ behind it), 25-year financial history, transcripts,
  global coverage. Best if you also read 10-Ks.
- **Roic.ai** ($14/month) — clean ROIC-centric layout, useful for
  quality screens; weaker on backtesting.
- **YCharts / Koyfin** (free + $39/month tier) — chart-first; Koyfin
  is the closest free-with-a-paywall analogue to a Bloomberg
  Terminal that exists.

You do not need all of these. **Pick one free + one paid** and stop.
The marginal hour spent learning a third platform is better spent
reading a 10-K.

#### 2.2 Screen 1 — GARP (Growth at a Reasonable Price)

GARP is Peter Lynch's screen, formalised. The thesis: *pay no more
than 1x PEG for a high-ROIC business growing free cash flow*. It is
the workhorse screen for tranche-1 (long-term compounders, per SOUL
#13).

| Filter | Threshold | Why |
|---|---|---|
| Market cap | > \$2 B | liquidity + audited Big-4 books |
| PEG (forward) | < 1.2 | growth not already priced in |
| FCF growth (5y) | > 10% | thesis-confirming cash dynamics |
| ROIC (TTM) | > 15% | spread above ~10% cost of capital |
| Debt / equity | < 1.0 | survives a credit cycle |
| Gross margin | > 40% | pricing power floor |

A GARP screen run on the S&P 1500 in April 2026 returns roughly
**80-120 names**. Typical hits today (representative, not a buy
list): MSFT, GOOGL, V, MA, ADBE, NOW, INTU, TXN, MCO, MSCI, AVGO,
LIN, ANET, CDNS. Not all are cheap right now — the screen is the
*entry filter*, not the buy decision. PEG below 1.0 is rare in 2026
because the index is trading at a 22x forward P/E vs a long-run mean
of 16x. Loosen to 1.5 and you get 200+ names; tighten to 0.8 and you
get 15 — which is the right number for a deep-dive queue.

#### 2.3 Screen 2 — Deep Value (Statistical Cheapness, Solvent)

Deep value is the Graham screen, the academic HML factor, the Bogle
"reversion to the mean" version. The thesis: *the market over-discounts
boring, slow, or temporarily impaired businesses, and a basket of them
mean-reverts.*

| Filter | Threshold | Why |
|---|---|---|
| Market cap | > \$500 M | tradeable, audited |
| P/E (TTM) | < 12 | bottom quintile |
| P/B | < 1.5 | balance-sheet protection |
| Current ratio | > 2.0 | survives 12 months without a roll |
| FCF (TTM) | > \$0 | not a value trap |
| Debt / EBITDA | < 3 | rate-cycle resilient |

Deep value is the screen you run *into* market panics, not out of
them. April 2026 is mid-cycle, the screen is sparse — energy mid-caps
(DVN, MRO, OVV), some regional banks (FNB, RF, CFR), and a handful of
consumer staples (KMB, K, GIS). In March 2020, the same screen
returned 600+ names. The screen does not change; the market does.

#### 2.4 Screen 3 — Quality Compounder (10-Year Track Record)

The Munger screen. The thesis: *a great business at a fair price beats
a fair business at a great price*. This is the screen you keep open
in the background and run quarterly.

| Filter | Threshold | Why |
|---|---|---|
| ROE | > 20% in **each** of last 5 years | stable, not levered up |
| Gross margin | > 40% | moat indicator |
| Operating margin | > 15% | converts revenue to cash |
| FCF positive | 8 / 10 years | proven through a cycle |
| Debt / equity | < 0.8 | optionality, not leverage |
| Buybacks > issuance | net negative shares | management aligned |

This is the most punishing screen of the four — it returns about
**40 names** in any reasonable market. April 2026 hits include AAPL,
MSFT, V, MA, COST, ULTA, MCO, MSCI, ROL, PAYX, AZO, TROW, FAST.
**There is no PEG/PE filter here on purpose.** This screen finds the
universe; valuation enters at the watchlist stage. You wait for one of
the 40 to fall 25-35% below its 5-year median EV/EBITDA, then you act.

#### 2.5 Screen 4 — Recovery (52-Week-Low Quality)

The contrarian screen. The thesis: *good businesses occasionally trade
near their 52-week low for reasons that have nothing to do with
long-term economics. Catch them before the market re-rates.*

| Filter | Threshold | Why |
|---|---|---|
| Price | within 10% of 52-week low | psychologically hated |
| Gross margin | > 25% | rules out commodity wreckage |
| Working capital | > 0 | survives the next 12 months |
| Net debt / EBITDA | < 4 | solvable balance sheet |
| Insider buying (90d) | > 0 net | management agrees |
| Short interest | < 8% of float | not a known short-seller target |

Recovery screens are the easiest to mis-execute (the "falling knife"
problem) and the most rewarding when right. Insider buying + short
interest filters are the quality gates. April 2026 candidates: a
small handful of regional banks post-2024 deposit-flight, a couple
of consumer-discretionary mid-caps that missed Q1, and one or two
healthcare names hit by tariff noise. Limit position size to 0.5-1% of
the portfolio — these are tranche-4 (opportunistic), not tranche-1.

![A scatter plot of trailing P/E (x-axis) versus return on equity (y-axis) for 30 well-known US-listed stocks. Quadrants are labelled cheap/expensive on the price axis and low-quality/high-quality on the ROE axis. The lower-right "GARP zone" — low P/E, high ROE — is shaded green and contains the screen's most attractive candidates.](image/side27_garp_quadrant.png)

The scatter above is the visual frame. Anything in the lower-right
quadrant is a candidate; anything in the upper-left is the
"glamour-stock trap" (high P/E, mediocre ROE). Most US large-caps
in April 2026 sit in the upper-right — quality at a premium. The
GARP screen is, geometrically, *find the names heading into the
lower-right.*

#### 2.6 The Watchlist Pipeline — From Screen to Position

The screen is step 1 of a five-step funnel:

1. **Screen** (4,000 -> 250). Run the four screens monthly. Union the
   hits.
2. **Triage** (250 -> 50). Eyeball each name for two minutes. Reject
   anything with restated financials, going-concern language, SEC
   investigation, or sub-$200M average daily dollar volume.
3. **Deep dive** (50 -> 10). Read the latest 10-K (or three of them
   for compounders), the most recent earnings transcript, and one
   short-seller report if one exists. Build a one-page thesis with
   five lines: *what they do, how they make money, what could kill
   it, what is it worth, what is it trading at.* (See `side02_reading_10k.md`.)
4. **Watchlist** (10 -> 3-7). Add to your tracked watchlist with
   *price triggers* — the price at which you would buy, not the
   price you wish you had bought at. A watchlist without triggers is
   a daydream.
5. **Position** (buy when triggered). Use a 1/3-1/3-1/3 entry: buy
   1/3 at trigger, 1/3 if it falls another 10%, 1/3 if it falls
   another 10% on no thesis-breaking news. Per SOUL #14, the barbell
   says you are wrong sometimes; the staggered entry pays you to be
   wrong about timing.

The buy-trigger is the single most underrated discipline. Decide the
price at the desk, in good light, with the 10-K open and CNBC off. By
the time the price arrives, the market will be telling you not to buy.

#### 2.7 Avoiding the Common Pitfalls of Screening

Three traps eat 80% of screening returns:

**Trap 1 — Optimising on the back-test.** The temptation to keep
adding filters until the screen returns "all winners" historically
is irresistible and fatal. Per SOUL #1, every additional filter
narrows your universe and adds in-sample bias. Stop at 6 filters.
Ever. (See week46_backtest_validator.html.)

**Trap 2 — Confusing screen output with research output.** The
screen tells you which 50 names are *worth investigating*. It tells
you nothing about whether you should *own* them. The 50->10 stage is
where your edge actually lives.

**Trap 3 — Not running the screen on yourself.** Once a year, run
the four screens with your own current holdings as the input
universe. If a position you currently own does not appear in *any*
of the four screens, you are holding it on inertia, not thesis.
Either re-justify it from scratch or sell.

---

### 3. Common Misconceptions

1. **"More filters -> better screen."** Past 6 filters, you are
   curve-fitting noise. The marginal filter typically removes more
   future winners than future losers.

2. **"The same screen should always return names."** Deep-value
   screens are *supposed* to return 0-10 names in a frothy market.
   An empty screen is a regime signal, not a tool failure.

3. **"Free screeners are not good enough for serious work."** Finviz +
   your brokerage's screener will get you 90% of the way to Stock
   Rover for a passive long-only book. Pay up only when your hours
   start to outweigh your money.

4. **"PEG < 1 means cheap."** PEG uses analyst consensus growth,
   which is wrong on average and very wrong at turning points. Treat
   PEG as a triage filter, not a valuation conclusion.

5. **"ROE > 20% means quality."** Not if it is leverage-driven. A
   bank with 15x equity multiplier and 1.5% ROA has 22% ROE and is
   not a quality compounder. Always check ROIC alongside ROE.

6. **"A screen finding 200 names is too noisy to use."** That is
   exactly the right number to *triage* down. The problem with
   screens is too few hits, not too many.

7. **"Insider selling is a sell signal."** Insiders sell for a hundred
   reasons (taxes, divorce, diversification, 10b5-1 plans). Insider
   *buying*, especially open-market and outside an earnings window,
   is the asymmetric signal.

8. **"Screening should be automated."** The screen should be saved
   and rerun-able. The *interpretation* must stay manual. The day
   you automate "buy anything that screens green" is the day you buy
   the next Enron at 8x earnings.

9. **"My watchlist is full -> I am done."** A watchlist is a queue,
   not a museum. Every name on it should have a price trigger and a
   review date. Names with neither are dead weight.

10. **"Backtested screens that worked for 10 years will keep working."**
    Per SOUL #2, the macro regime changes every 30-40 years. A screen
    that worked 1995-2020 (cheap quality) might fail 2025-2040 (rates
    higher, cheap-quality re-rates faster). Re-validate annually.

---

### 4. Q&A Section

**Q: How often should I run the screens?**
A: Monthly is the institutional default. Quarterly is fine for
retail. Daily is overkill — the names that pass a 5-filter screen
do not move daily.

**Q: I have 60 names from the GARP screen. How do I get to 10?**
A: First, eliminate sectors you do not understand. Second, kill any
name you cannot describe in one sentence. Third, sort the rest by
ROIC descending and take the top decile. You will be at 6-8 names.

**Q: Can I just buy an ETF that does the screen for me?**
A: Yes. AVUV (small-cap value), QUAL (quality), MTUM (momentum),
COWZ (cash-flow yield) are factor ETFs that mechanise screens 1-3.
They are a perfectly reasonable substitute for individual stock
screening if you are time-constrained. (See `week50_factor_tilts.md`.)

**Q: How is screening different from factor investing?**
A: Factor ETFs hold all 100-500 names that pass a single factor
filter. Stock screens are an idea-generation step that is followed
by *concentrated* manual research. Factors win on diversification;
screens win on conviction-per-name.

**Q: My deep-value screen hits the same energy mid-caps every month.
Should I just buy them?**
A: No. The fact that a name has been cheap for 36 months running is
information about *why* it is cheap (structural decline, governance,
commodity cycle). Run the *recovery* screen on that universe instead;
the names that pass both deep-value AND recovery have the asymmetry.

**Q: How do I screen for moats?**
A: You cannot, directly. Proxies: 5-year gross margin > 40% AND
stable; ROIC > 15% across a full cycle; market share gains over 10
years. Screen for the financial fingerprint, then verify the moat
qualitatively.

**Q: What about screens for short ideas?**
A: Same engine, inverted thresholds: PE > 80, P/B > 8, FCF < 0 for
3 years, debt/EBITDA > 6, accruals > 10% of assets. Per SOUL #5,
short alpha is real but the borrow + dividend-pass-through + carry
is brutal — most retail investors should let factor short ETFs do
the work.

**Q: How long does this whole process take per week?**
A: Steady-state, 2-3 hours: 30 min to run screens, 90 min to
deep-dive 1-2 names, 30 min to update existing thesis pages. The
first month is heavier (5-8 hours/week) while you build the
infrastructure.

**Q: What if I run the same screens as everyone else?**
A: You will. The edge is not the filter — it is the 50->10 stage,
which depends on your *judgement*. PEG < 1.2 + ROIC > 15% returns
the same 100 names for everyone. Picking the right 5 from those 100
is where the alpha lives. (SOUL #5: alpha sources are stable, but
each requires manual judgement at the buy decision.)

**Q: Can I use these screens in tax-advantaged accounts only?**
A: Recovery and deep-value screens generate higher turnover — better
in IRAs. GARP and quality compounders work in either; quality compounders
especially in taxable accounts because hold periods stretch into LTCG
territory by year 2. (See SOUL #15 + `side04` for tax-location maths.)

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** From 4,000 to 5: Building the Watchlist that Funds the Next Decade

**RUNTIME TARGET:** ~12 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:00]**

**HORACE:** There are about 4,000 stocks listed on the New York Stock
Exchange and the Nasdaq. Forget global. Forget OTC. Just the US
universe — the only one we own per SOUL principle 16. Four thousand.
And the question that determines everything about whether you make
money in stock-picking is not *which one do you buy*. It is *which 30
do you bother to read about*.

**STELLA:** Today we are going to walk through the funnel. Four
screens, each with six filters. 4,000 -> 250 -> 50 -> 10 -> 3. The same
funnel that institutional analysts run, simplified to what a retail
investor can do on a weekend with Finviz.

**HORACE:** And we are going to be honest about something the
investing media never tells you: in April 2026, three of the four
screens we will show you return *almost no names*. That is a feature.

---

**[ACT I — THE TOOL STACK — 1:00 to 2:30]**

**STELLA:** Three tiers of screener. Free — Finviz, Yahoo, TradingView,
your brokerage. Paid — Stock Rover at $28 a month, TIKR at $24, and a
handful of others.

**HORACE:** Pick one free, pick one paid, stop. There is a tendency
to collect platforms. Don't. The marginal hour is better spent
reading a 10-K than learning a third UI.

**STELLA:** For 90% of retail investors, Finviz plus their
brokerage's screener is sufficient.

[VISUAL: image/side27_screener_funnel.png]

**HORACE:** That is the funnel. 4,000 listed. 250 pass the screen.
50 we triage. 10 sit on the active watchlist. 3 we currently own. The
shape of that funnel — that is the entire game.

---

**[ACT II — THE FOUR SCREENS — 2:30 to 7:30]**

**HORACE:** Four screens. Each with one thesis.

**STELLA:** **Screen 1, GARP — growth at a reasonable price.** Six
filters: market cap above $2 billion, PEG below 1.2, free cash flow
growth above 10%, ROIC above 15%, debt-to-equity below 1, gross
margin above 40%.

**HORACE:** Peter Lynch's screen. The thesis is: *I will pay up for
quality, but not more than the growth justifies.* In April 2026, this
returns about 80 names. Tighten PEG to 0.8 and you are at 15 — which
is the right size for a deep-dive queue.

**STELLA:** **Screen 2, deep value.** P/E below 12, P/B below 1.5,
current ratio above 2, positive free cash flow, debt-to-EBITDA below
3.

**HORACE:** Graham's screen. Bogle's screen. The HML factor. Right
now, in mid-cycle, this returns about 30 names — mostly energy
mid-caps and regional banks. In March 2020, it returned 600. Run it
*into* panics, not out of them.

**STELLA:** **Screen 3, quality compounder.** ROE above 20% every
year for 5 years, gross margin above 40%, operating margin above 15%,
free cash flow positive in 8 of the last 10 years, debt-to-equity
below 0.8, net buybacks positive.

**HORACE:** This is the Munger screen. There is no valuation filter
on purpose. The screen finds the universe of forty or so businesses
that *can* compound. You then wait for one of them to drop 25-35%
below its five-year median EV/EBITDA, and you act.

**STELLA:** **Screen 4, recovery.** Within 10% of the 52-week low,
gross margin above 25%, working capital positive, net debt/EBITDA
below 4, insider buying positive in the last 90 days, short interest
below 8%.

**HORACE:** The contrarian screen. The asymmetric one. And the
hardest to execute — the falling knife problem. The insider-buying
filter and the short-interest filter are what keep you out of the
truly broken businesses.

[VISUAL: image/side27_garp_quadrant.png]

**STELLA:** This scatter is the visual frame. P/E on the x-axis. ROE
on the y-axis. Thirty well-known US-listed names plotted as of April
2026.

**HORACE:** Lower-right is the GARP zone — low P/E, high ROE. That
is the green-shaded region. Upper-right is *quality at a premium* —
which is where most of the S&P 500 currently sits. Upper-left is
the glamour-stock trap. Lower-left is value-trap territory.

**STELLA:** The screens are, geometrically, asking the same question:
*find the names migrating toward the lower-right.*

[VISUAL: interactive/side27_screener.html]

**HORACE:** And we built you a live one. Drag the four sliders — max
P/E, min ROE, min revenue growth, max debt-to-equity — and the panel
on the right shows you which of the 30 stocks survive your filters.

**STELLA:** This is not a buy list. It is a triage list. The screen's
job is to give you a 50-name queue. Your job is the next stage.

---

**[ACT III — THE PIPELINE — 7:30 to 10:30]**

**HORACE:** Five stages from screen to position.

**STELLA:** **Stage 1 — Screen.** 4,000 to 250. Done.

**STELLA:** **Stage 2 — Triage.** 250 to 50. Two minutes per name.
Reject restated financials, going-concern language, SEC investigations,
sub-$200 million daily dollar volume.

**STELLA:** **Stage 3 — Deep dive.** 50 to 10. Read the 10-K. Read
the latest transcript. Build a one-page thesis. Five lines: what they
do, how they make money, what could kill it, what it is worth, what
it is trading at.

**HORACE:** Side lesson 02 walks you through reading a 10-K. Watch
that one back if you have not.

**STELLA:** **Stage 4 — Watchlist.** 10 to 3-7. Add to a tracked list
with *price triggers*. The price at which you would buy. Not "I'll
keep an eye on it." A specific number.

**HORACE:** A watchlist without triggers is a daydream. The trigger
is the only thing that converts a list into a decision.

**STELLA:** **Stage 5 — Position.** Buy when triggered. One-third at
trigger, one-third on a 10% drop, one-third on another 10% drop with
no thesis-breaking news.

**HORACE:** Per SOUL principle 14 — the barbell. You are wrong about
timing more often than you think. The 1/3-1/3-1/3 entry pays you to
be wrong.

---

**[ACT IV — THE PITFALLS — 10:30 to 11:30]**

**HORACE:** Three traps.

**STELLA:** **Trap 1 — Filter creep.** Stop at six filters. Ever. Past
that, you are curve-fitting in-sample noise.

**STELLA:** **Trap 2 — Confusing screen output with research output.**
The screen does not tell you what to own. It tells you what to study.

**STELLA:** **Trap 3 — Not running the screen on yourself.** Once a
year, screen your own holdings. If a position does not pass any of
the four, you are holding it on inertia. Re-justify or sell.

**HORACE:** That last one is the hardest and the most useful. Most
investors never apply their own discipline to their own portfolio.

---

**[OUTRO — 11:30 to 12:00]**

**STELLA:** A screen is the most leveraged tool a retail investor has.
Five filters and a $40-a-month subscription replaces what used to take
an analyst team.

**HORACE:** And per SOUL principle 1, alpha is rare. You will not
out-research the buy-side. But you can out-*select* the average
self-directed investor by an enormous margin, simply by replacing
"my friend mentioned it" with "it passed five numerical filters and
I read the 10-K."

**STELLA:** Build the funnel. Run it monthly. Use the interactive on
the website. See you next time.

---
