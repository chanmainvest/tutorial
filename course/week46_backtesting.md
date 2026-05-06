# Week 46: Backtesting — Survivorship Bias, Look-Ahead Bias, Transaction Costs, and the Deflated Sharpe

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A backtest is a story you tell yourself about a strategy. It is the
most persuasive financial document in the world: a smooth equity
curve, a tidy Sharpe number, a table of annual returns, all
generated in a few seconds by a program you wrote yesterday. The
problem is that almost every backtest is wrong, and almost every
backtest is wrong in the same direction — too optimistic. Empirical
work by Lopez de Prado, Bailey, and others shows that the median
in-sample Sharpe of a published quant strategy roughly *halves*
out of sample. Strategies that look like 1.5 Sharpe machines on
paper deliver 0.6 in production, if anything at all. Most retail
"systems" sold online deliver zero or negative excess return after
realistic frictions.

You need this material for four reasons.

1. **You will see, build, or buy backtests for the rest of your
   investing life.** Every ETF prospectus, every robo-advisor
   pitch, every YouTube quant influencer leads with a backtest.
   If you cannot reflexively spot survivorship bias, look-ahead
   bias, and the multiple-testing trap, you will mis-allocate
   capital. Alpha is rare; almost every backtest is selling you
   alpha. Reconcile.
2. **The deflated Sharpe ratio is now the institutional standard.**
   Bailey and Lopez de Prado's 2014 paper formalised what
   sceptical practitioners always knew: try a thousand strategies,
   the best one will look great by chance. Their formula
   converts a raw in-sample Sharpe into one that explicitly
   penalises the number of trials. Modern allocators ask for it.
   You should compute it on your own ideas.
3. **Transaction costs are usually the entire alpha.** A
   backtested edge of 4% per year, run weekly with 30 bps
   round-trip costs and ~50 turnovers per year, evaporates: 50 ×
   0.30% = 15% gross drag, swamping the edge by a factor of three.
   Most "discoveries" by retail systems live or die on cost
   modelling — which is why the slick PowerPoints all quietly
   omit it.
4. **Backtesting connects to four enduring ideas.** Alpha is
   rare. The vol tail wags the dog — a five-year backtest
   without a crisis is meaningless. Markets stay irrational
   long enough to stop you out before reverting. And the
   liquid US equity universe is the one place a sceptical
   backtester can actually validate point-in-time data without
   drowning in survivor noise.

This lesson walks through the seven canonical backtest pathologies,
the math of the deflated Sharpe, and a working calculator that
takes your in-sample number and tells you what to actually expect
out of sample.

---

### 2. What You Need to Know

#### 2.1 Survivorship Bias — The Universe You Don't See

The simplest, most pernicious bias. Open any data terminal, ask
for "all S&P 500 stocks since 1990, equal-weighted, monthly
rebalance." Your terminal returns the **current** S&P 500. Lehman
Brothers is missing. Bear Stearns is missing. WorldCom is
missing. Sears, Kodak, Polaroid, Wachovia, Washington Mutual,
Countrywide — all missing. You have backtested the strategy on a
universe of survivors.

Survivorship inflates returns by roughly 1-3% per year on a US
large-cap universe, more on small-caps, far more on emerging
markets and on hedge fund databases that only list funds still
reporting. A "long-only quality" backtest run on the survivors
of 1990 looks brilliant. The same strategy run on the actual
1990 universe — including the names that bankrupted — looks
mediocre.

The fix is **point-in-time index membership**. CRSP, Norgate,
S&P's IHS-Markit, and Compustat-CapIQ all sell historical
constituent files that mark which tickers were in the index on
which date. Free data sources rarely have this; if you backtest
with a free source, assume your top-line return is overstated
by 100-300 bps.

#### 2.2 Look-Ahead Bias — Using Tomorrow's Data Today

Look-ahead bias is when your trading rule on date *t* uses
information that was not actually available on date *t*. The
mechanisms are subtle.

- **Restated fundamentals.** Compustat shows you AAPL's FY2024
  revenue as currently restated. The version available in
  January 2025 — before the 10-K filed in November 2025 was
  amended in March 2026 — was different. A backtest using
  current-vintage fundamentals is using future data.
- **Index reconstitutions announced before effective.** S&P
  announces additions ~5 trading days before they take effect.
  A backtest that uses "in-the-index-on-date-t" with current
  vintage data will pick up tomorrow's adds today.
- **End-of-day prices used as fill prices.** Your signal fires
  at 4:00 pm; you fill at the 4:00 pm close. In reality you
  filled the next morning, often at a worse price for momentum
  strategies and a better one for mean-reversion strategies.
  Look-ahead in fill timing flatters momentum and punishes MR.
- **Earnings dates.** A reported "EPS surprise" backtest that
  uses the current Compustat earnings-date field will pick up
  some companies one day *before* the announcement, because
  the field has been retroactively normalised.

The fix is **point-in-time data with as-reported timestamps**, and
a one-day lag rule: any signal computed on date *t* is acted on at
the open of date *t*+1. Without this rule, expect 2-5% per year
of phantom alpha.

#### 2.3 Transaction-Cost Modelling — Where Most Edges Die

For US-listed liquid equities (SPY, QQQ, large caps), realistic
all-in round-trip transaction costs in April 2026 are:

| Universe | Round-trip cost (bps) | Notes |
|---|---|---|
| SPY, QQQ, top-50 mega-caps | 1-3 bps | Tight spread + tiny impact |
| S&P 500 large-caps | 5-15 bps | Avg spread ~3 bps + impact |
| Russell 1000 mid-caps | 15-30 bps | Wider spread + slippage |
| Russell 2000 small-caps | 30-80 bps | Spread + impact + sometimes ADV-cap |
| Microcap, OTC, illiquid | 100-300 bps | And you may not get the size you want |

These are *all-in*: bid-ask spread, market impact, exchange and
SEC fees, plus brokerage commissions (now mostly zero for retail
in the US). For institutions trading size, market impact dominates
and rises roughly with the square root of (order size / ADV).

The arithmetic is brutal. A strategy with annualised gross alpha
$\alpha$ and turnover $\tau$ (round-trips per year) and round-trip
cost $c$ delivers net alpha:

$$ \alpha_{\text{net}} = \alpha_{\text{gross}} - \tau \cdot c $$

A 4% gross alpha at:

- $\tau = 0.5$ (annual rebalance), $c = 10$ bps → net = 3.95% — costs negligible.
- $\tau = 6$ (monthly), $c = 10$ bps → net = 3.40% — modest drag.
- $\tau = 50$ (weekly), $c = 30$ bps → net = -11% — entire alpha and then some lost.
- $\tau = 252$ (daily), $c = 30$ bps → net = -71.6% — strategy is a furnace.

This is why daily and intraday strategies rarely survive in
illiquid universes: even tiny gross edges are eaten alive by
turnover × cost. The chart in §2.5 makes this concrete.

![Annualised return after costs as a function of round-trip transaction cost (0/10/30/100 bps) for four turnover regimes (annual / monthly / weekly / daily rebalance), each starting from a 4% gross-alpha baseline. The annual-rebalance line is roughly flat; monthly drops modestly; the weekly line crosses zero between 30 and 100 bps; the daily line crosses zero before 10 bps and is deeply negative at 30 bps. Cost is the silent killer of high-turnover edges.](image/week46_cost_drag.png)

The diagonal lines fan out from the same starting point on the
left. By the time you reach 30 bps round-trip — typical for
small-cap US — the daily strategy has lost all of its alpha and
then some. This is why most published "high-frequency" retail
systems are pure storytelling: they look great in zero-cost
simulations and are catastrophic with realistic friction.

#### 2.4 The Multiple-Testing Problem — 1000 Random Strategies

Here is the single most under-appreciated fact in retail
quant: **if you try enough strategies, some will look great by
chance**. This is not a hypothesis. It is arithmetic.

Suppose you simulate 1000 strategies, each with **zero true
edge** — pure noise. Each generates an in-sample annualised
Sharpe estimate. Because Sharpe is a noisy estimator (with finite
sample size), the *distribution* of those 1000 estimates is wide.
For a one-year window of daily returns, the standard error of the
estimated annualised Sharpe is roughly 1.0. So out of 1000 random
strategies you should expect, by pure chance:

- ~25 with Sharpe > 2.0 (one-tail probability ~ 2.5%).
- ~160 with Sharpe > 1.0 (~ 16%).
- ~3 with Sharpe > 3.0 (~ 0.3%).

Every one of these is pure noise. Yet a researcher who ran a
1000-strategy grid search and *only reports the best* would
proudly publish a "Sharpe 3 strategy" with a t-stat of 3, and the
reviewer who does not adjust for the trial count will believe it.

![Histogram of 1000 simulated random-strategy Sharpe ratios (true Sharpe = 0, 252 daily observations), with the theoretical null distribution overlaid as a smooth curve and the 2.0 and 3.0 thresholds marked with vertical lines. About 25 of the 1000 random strategies clear Sharpe > 2 by chance, and about 3 clear Sharpe > 3 — none of which are real edges. The chart visualises why "I tried 1000 things and the best one had Sharpe 2.5" is not evidence.](image/week46_deflated_sharpe.png)

The vertical lines are at Sharpe = 2 and Sharpe = 3. Every bar to
the right of those lines is a strategy with **literally zero
alpha** that nonetheless tested above the conventional thresholds.

#### 2.5 The Deflated Sharpe Ratio — Bailey & Lopez de Prado

Bailey, Borwein, Lopez de Prado, and Zhu (2014) wrote down a
formal correction. The **deflated Sharpe ratio** (DSR) starts
from the observed in-sample Sharpe $\widehat{SR}$, subtracts the
expected maximum-of-N null Sharpe, and divides by the
distribution-aware standard error of the Sharpe estimator:

$$ \widehat{SR}_0 \approx \sqrt{\frac{2 \ln N}{T}} \quad \text{(expected max under null, large N)} $$

where $N$ is the number of strategy variants tried and $T$ is the
sample length in periods.

$$ \text{DSR} = \Phi\!\left(\frac{(\widehat{SR} - \widehat{SR}_0)\sqrt{T-1}}{\sqrt{1 - \gamma_3 \widehat{SR} + \frac{\gamma_4 - 1}{4}\widehat{SR}^2}}\right) $$

Here $\gamma_3$ is skewness and $\gamma_4$ is kurtosis of returns;
$\Phi$ is the standard-normal CDF. Read the output as a
probability: DSR is the chance that the strategy's true Sharpe is
above the multiple-testing-adjusted null. A DSR of 0.95 means 95%
confident the strategy is real; 0.50 means a coin flip; 0.30 is
"probably noise."

The intuition is simple even if the formula is not: **reporting
the best of N tries is like running a one-tailed test at
significance level 1/N**. To clear that bar, your raw Sharpe has
to beat $\sqrt{2 \ln N / T}$ — and for N = 1000 trials over T = 5
years of daily data, that haircut is roughly $\sqrt{2 \times 6.91
/ 1260} \approx 0.10$ on a *daily* SR, or about 1.66 on an
annualised SR. So a researcher reporting Sharpe 2.0 from a
1000-strategy search has, after deflation, an effective Sharpe of
roughly 0.34 — barely better than the bond market.

#### 2.6 Walk-Forward Analysis — The Gold Standard

The honest way to validate a strategy is **walk-forward**: fit
parameters on a rolling window, test on the immediately
subsequent out-of-sample window, then roll forward. For example:
fit on 2010-2014, test 2015; fit on 2011-2015, test 2016; and so
on. The concatenation of the test-period returns is your true
out-of-sample track record.

Walk-forward kills three birds:

- **Look-ahead.** You can only fit on data older than the test
  window, by construction.
- **Overfitting.** If your strategy needs 12 parameters to look
  good in-sample, the rolling refits will produce wildly different
  parameter sets each window — a tell that the parameters are not
  capturing a real signal.
- **Regime drift.** A strategy that worked 1995-2005 but failed
  2015-2025 will show in the walk-forward equity curve as a clean
  break. A naïve full-sample backtest hides that break inside the
  averages.

A strategy whose walk-forward Sharpe is *less than half* of its
full-sample in-sample Sharpe is overfit. Most published retail
systems fail this test on inspection.

#### 2.7 Regime-Shift Robustness

Even after deflation, walk-forward, and proper costs, one final
question remains: *does the strategy work in different regimes?*
A momentum strategy that backtests beautifully on 2010-2021 (one
long QE-driven uptrend) is not the same as one that backtests
across 1929-32, 1973-74, 2000-02, 2008, and 2020 stress windows.

A useful discipline: split your sample into the canonical regime
buckets (Week 10's framework) and report Sharpe, drawdown, and
hit-rate **within each regime**. A strategy that works in three
of four regimes and fails in one is potentially deployable with
a regime overlay. A strategy that only works in one regime is a
beta exposure dressed up as alpha. The 1980-2020 regime was
anomalous; do not let your sample window inherit its
flattering arithmetic.

The interactive at the end of this lesson lets you drag five
sliders — in-sample Sharpe, years of backtest, number of
strategies tried, round-trip cost, and trades per year — and
watch four numbers update live: deflated Sharpe (multiple-testing
penalty), out-of-sample Sharpe estimate, Sharpe-after-costs, and
the probability the strategy is real. Most "great" backtests
collapse instantly under realistic settings.

---

### 3. Common Misconceptions

1. **"My backtest looks great, so the strategy works."** Your
   backtest is a *best-case* simulation under your particular
   choices of data, costs, and timing. The realised performance
   is almost always worse — and alpha is rare, so the prior on
   any backtest is that it is overstated.
2. **"Survivorship bias is a problem only for small-caps."** It
   is a problem everywhere. Lehman, Bear, WorldCom, Enron, GE
   removed from the Dow — all large-cap. The bias is universal;
   it is just larger in noisier universes.
3. **"I used adjusted prices, so I'm fine."** Split- and
   dividend-adjusted prices fix one issue (corporate-action
   distortion) but tell you nothing about whether the ticker
   was in the relevant universe at the historical date.
4. **"Transaction costs are negligible for retail because
   commissions are zero."** Zero commission ≠ zero cost. Spread
   plus market impact still costs you 5-30 bps round-trip on
   most US equities, and far more on small-caps. The
   "commission-free" branding is marketing.
5. **"I tested in-sample and out-of-sample, so I'm fine."** A
   single in/out split is barely better than no split when you
   chose the split point after seeing the data. Walk-forward is
   the standard.
6. **"P-value below 0.05 means the strategy is real."** Not if
   you tried more than 20 variants. Multiple-testing correction
   (Bonferroni, FDR, or DSR) is mandatory.
7. **"Deflated Sharpe is too conservative — it kills good
   strategies."** It kills *most* strategies, and that is
   correct. Alpha is rare — the deflation is just that fact in
   formula form.
8. **"Higher in-sample Sharpe is better."** Higher in-sample
   Sharpe with fixed sample size and fixed turnover is better,
   yes. Higher in-sample Sharpe coming from a larger search
   space is *worse* — because you tried more.
9. **"Walk-forward eliminates overfitting."** It reduces it; it
   does not eliminate it. If the underlying strategy class is
   overfit (e.g., 12 parameters), walk-forward parameters will
   still flap around and out-of-sample performance will still
   degrade, just less catastrophically.
10. **"Regime-robust strategies are the only good ones."** Some
    perfectly good strategies work only in specific regimes
    (trend-following in trending markets, value in mean-reverting
    ones). The honest play is to *acknowledge* the regime and
    size accordingly, not to pretend the strategy is
    all-weather.

---

### 4. Q&A Section

**Q1. How many strategy variants do I have to declare?**
A1. Every variation tried — across asset universes, parameter
grids, signal definitions, and rebalance frequencies. If you ran
a 5×5×4 grid search, $N = 100$. Including the variants you tried
and discarded "because they didn't look good" is critical;
omitting them is the heart of p-hacking.

**Q2. What's a realistic out-of-sample haircut on the in-sample Sharpe?**
A2. The literature finds the median OOS Sharpe of published quant
strategies is roughly 50% of the in-sample Sharpe, and the worst
quartile delivers zero or negative. A reasonable working
assumption: $\widehat{SR}_{\text{OOS}} \approx 0.5 \times
\widehat{SR}_{\text{IS}}$ before costs.

**Q3. What round-trip cost should I assume for a Russell 2000 strategy?**
A3. 30-50 bps for institutional sizing on liquid small-caps. Up
to 80-100 bps for the bottom decile of small-caps where ADV is
low. Retail traders moving small notional can sometimes do 15-25
bps but cannot scale it.

**Q4. My in-sample Sharpe is 1.5 over 5 years and I tried 200
variants. Is that worth deploying?**
A4. Run the deflated Sharpe. With $T \approx 1260$ days and $N =
200$, $\widehat{SR}_0 \approx \sqrt{2 \ln 200 / 1260} \approx 0.092$
on a daily basis, or about 1.46 annualised. So your 1.5 IS Sharpe
is essentially the multiple-testing null — DSR will be near 50%.
That is a coin flip, not a strategy.

**Q5. Why is daily-frequency a graveyard for retail quants?**
A5. Daily turnover at 252 round-trips per year times even 10 bps
cost is 25.2% annualised drag. You need a 25%+ gross edge before
you net anything. Arithmetic plus the rarity of alpha: those edges
effectively
do not exist for retail.

**Q6. How do I get point-in-time fundamental data without paying
for Compustat?**
A6. Imperfectly. Free EDGAR scraping gets you as-filed financials
with proper timestamps, but reconstructing the full universe is
painful. Quandl (now Nasdaq Data Link) sells some point-in-time
slices at retail prices. For most retail purposes, lag your
fundamental data by 90 days as a crude correction.

**Q7. Does walk-forward preserve transaction-cost realism?**
A7. Yes — and it should. The cost model applies inside each
walk-forward step exactly as it would in live trading. If
anything, walk-forward exposes cost-sensitivity better than
full-sample backtests because it reveals turnover changes across
parameter refits.

**Q8. My strategy works in bull markets and fails in bear
markets. Is it deployable?**
A8. Maybe — with a regime overlay. Identify the trigger
(e.g., 200-day moving average, VIX threshold) that turns it on
and off, and incorporate that switch into the backtest. If the
strategy is profitable only with the regime overlay, your
"alpha" is partly the overlay's alpha. Be honest about
attribution.

**Q9. Should I use bootstrap or block-bootstrap to estimate
Sharpe confidence intervals?**
A9. Block bootstrap (with block length matched to the
auto-correlation of the strategy's returns) is the right tool
for serially correlated strategies — most of them. Naïve i.i.d.
bootstrap understates the variance.

**Q10. What's the simplest defensible backtest workflow?**
A10. Five steps. (1) Define the strategy in one paragraph
*before* looking at data. (2) Use point-in-time data with a
one-day signal-to-execution lag. (3) Apply realistic costs based
on the universe. (4) Walk-forward at quarterly or yearly
re-fits. (5) Compute deflated Sharpe with honest $N$. If the
deflated Sharpe is below ~0.7, do not deploy.

**Q11. Can survivor bias ever flatter a strategy *less* than
expected?**
A11. Rarely, in highly distressed periods where the strategy was
specifically betting on the survivors (e.g., long-quality through
2008). Even then, the bias usually rounds in favour of the
backtest. Default assumption: survivorship adds 100-300 bps/year.

**Q12. How does Horace size a strategy after passing all of these
tests?**
A12. Barbell sizing at the L4 sleeve level. A strategy that
deflates to a Sharpe of ~1 OOS, with realistic costs and a
multi-regime sample, gets a small slice of the *opportunity
sleeve* — usually 1-3% of total wealth. If it works, fine. If it
does not, the 90%+ core is unaffected. Backtests are not
permission to bet large; they are permission to bet *some*.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Why Most Backtests Lie: Survivorship, Look-Ahead, Costs, and the Deflated Sharpe

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO - 0:00 to 1:30]**

[VISUAL: title card, cream + gold, "Week 46: Backtesting"]

HORACE: Welcome back. This is Week 46 of the chanmainvest course.
Today's topic is one I have been waiting all year to do honestly:
backtesting. The single most persuasive document in finance is
a backtest. The single most over-rated document in finance is
also a backtest.

STELLA: I have heard you say "backtests lie" about a hundred
times. Today we explain why.

HORACE: Today we explain why, and we put a calculator in your
hand that converts a flattering in-sample Sharpe into the number
you should actually expect out of sample. Spoiler: most great
backtests collapse to nothing once you correct for the realistic
trial count and transaction costs.

STELLA: Alpha is rare — again.

HORACE: Alpha is rare. Backtests routinely manufacture the
appearance of alpha. We are going to spend this episode
demolishing four of the biggest illusions: survivorship bias,
look-ahead bias, transaction costs, and the multiple-testing
problem. And then we will work through the deflated Sharpe ratio
that fixes the last one.

[VISUAL: chapter list overlay]

---

**[SECTION 1 - 1:30 to 4:30] - Survivorship and look-ahead**

HORACE: Start with survivorship. Every data terminal you query
returns the *current* universe. The S&P 500 today does not
include Lehman Brothers. It does not include Bear Stearns,
WorldCom, Enron, Sears, Kodak, Polaroid, Wachovia, Washington
Mutual, or Countrywide.

STELLA: All the names that blew up.

HORACE: All the names that blew up are not in your backtest. So
when you simulate "long-only large-cap quality, 1990 onward,"
your simulation is on the list of survivors. The bankruptcies
are silently dropped. That alone adds 100 to 300 basis points
per year of phantom return.

STELLA: That's enormous.

HORACE: That's the difference between a 12 percent strategy and
a 9 percent strategy. The fix is point-in-time index membership
data — CRSP, Norgate, Compustat-CapIQ — and free databases
basically do not have it. So if you run a backtest with free
data, your top-line return is overstated. Every time.

STELLA: And look-ahead bias?

HORACE: Look-ahead is when your trading rule on date *t* uses
data that was not available on date *t*. The classic case is
restated fundamentals. Compustat shows you Apple's fiscal-2024
revenue *as currently restated*. The version available in
January 2025, before the 10-K was amended, was different. A
strategy backtested on current-vintage fundamentals is using
future information.

STELLA: So how do you avoid it?

HORACE: Lag everything. Signal computed on date *t* is acted on
the next morning. Fundamentals lagged 90 days. Index membership
checked as-of-date. Without those rules, expect 200 to 500 bps
per year of phantom alpha.

---

**[SECTION 2 - 4:30 to 7:30] - Transaction costs**

[VISUAL: image/week46_cost_drag.png]

HORACE: This is the chart that ends most retail "high-frequency"
systems. Four lines. Each starts at the same 4 percent gross
alpha. Each represents a different rebalance frequency: annual,
monthly, weekly, daily. The x-axis is round-trip transaction cost
in basis points.

STELLA: And the daily line dives off a cliff.

HORACE: The daily line is a furnace. At zero cost, all four
strategies tie at 4 percent. At 10 basis points round-trip — which
is realistic for SPY — the daily strategy has lost 25 percentage
points of return per year. At 30 basis points — realistic for
small-caps — the daily strategy is at minus 71 percent and the
weekly is at minus 11 percent. Both are catastrophic.

STELLA: So the alpha didn't go away. It got eaten.

HORACE: Right. Turnover times cost is the alpha tax. Annual
rebalancing pays almost nothing in tax. Monthly pays a bit.
Weekly pays a lot. Daily is a self-destruction machine unless
your gross edge is above 25 percent — which on liquid US
equities effectively does not exist.

STELLA: This is why every retail quant influencer's "daily
algorithm" is a scam.

HORACE: Or honest naïveté. Either way, the math doesn't care.
If you cannot show a real cost model and a real turnover number,
the system is not a system.

---

**[SECTION 3 - 7:30 to 11:00] - Multiple testing**

[VISUAL: image/week46_deflated_sharpe.png]

HORACE: This is the chart most retail backtesters have never
seen. I simulate 1000 random strategies. Each one has true
Sharpe of zero — pure noise. Each one generates 252 daily returns.
I compute their in-sample Sharpe ratio and plot the histogram.

STELLA: It's a bell curve centred on zero.

HORACE: A bell curve centred on zero, with standard deviation of
about one. So one in forty random strategies clears Sharpe two.
Three in a thousand clear Sharpe three.

STELLA: Are you saying that if I randomly generate 1000
strategies, twenty-five of them will have Sharpe above two?

HORACE: I am saying exactly that. And the researcher who
publishes only the best one — and there is *always* such a
researcher — produces a "Sharpe two strategy with t-stat three"
that is literally pure noise.

STELLA: That's terrifying.

HORACE: That's the multiple-testing problem. Every backtest is
embedded in an implicit search space. If you only report the
winner, you have to deflate the winner's Sharpe by the implied
trial count. Bailey and Lopez de Prado wrote down the formula in
2014. We call it the deflated Sharpe ratio.

STELLA: And the formula?

HORACE: The expected maximum Sharpe under the null grows with
square-root of two-times-log-N over T. So for a thousand trials
on five years of daily data, the null max Sharpe — purely from
chance — is about 1.66 annualised. To clear that bar, your raw
Sharpe has to beat 1.66 *before* we even look at out-of-sample.

STELLA: So a published Sharpe of two from a thousand-strategy
search is essentially nothing.

HORACE: Essentially nothing. Effective Sharpe after deflation is
about 0.34. Worse than the bond market.

---

**[SECTION 4 - 11:00 to 13:30] - The interactive lab**

HORACE: We built a calculator that does this for you. Five
sliders. In-sample Sharpe — what you observed. Years of backtest
— how long the sample is. Number of variants tried — your $N$.
Round-trip cost in basis points. Trades per year — your turnover.

STELLA: And the outputs?

HORACE: Four big numbers. Deflated Sharpe — your Sharpe after
the multiple-testing penalty. Out-of-sample Sharpe estimate —
what we expect you to actually realise. Sharpe-after-costs —
what you realise after frictions. And probability the strategy
is real — the chance the true Sharpe is above zero.

STELLA: Walk us through a worst-case.

HORACE: Sure. In-sample Sharpe two. Two years of data. Five
hundred variants tried. Thirty bps round-trip. Fifty trades per
year. Hit recompute. Probability strategy is real: about 25
percent. So we expect a coin flip with the coin slightly biased
against us.

STELLA: And a good case?

HORACE: In-sample Sharpe one-point-two. Twenty years of data.
Five variants tried. Five bps round-trip — large-cap. Twelve
trades per year — monthly. Probability strategy is real: about
ninety percent. That is a deployable signal.

STELLA: The difference is mostly the trial count and the data
length.

HORACE: Almost entirely. Alpha is rare — that is what
shows up in the math. The longer the data, the smaller the trial
count, the more your in-sample number means.

---

**[SECTION 5 - 13:30 to 15:30] - Walk-forward and regime**

HORACE: Two more checks before deployment. Walk-forward and
regime robustness.

STELLA: Walk-forward.

HORACE: Walk-forward is the gold standard. Fit your parameters
on a rolling window. Test on the immediately following window.
Roll forward. The concatenated test-period returns are your
honest out-of-sample track record. If your walk-forward Sharpe
is less than half your full-sample in-sample Sharpe, the
strategy is overfit. Throw it away.

STELLA: And regime.

HORACE: Regime: split your sample into Week 10's canonical
buckets — bull-quiet, bull-volatile, bear, recovery — and
report Sharpe and drawdown *within each*. A strategy that
works in three of four regimes is potentially deployable with
an overlay. A strategy that works only in one regime is a beta
exposure dressed as alpha. Do not let your
sample window inherit the flattering arithmetic of one regime.

---

**[SECTION 6 - 15:30 to 17:00] - The honest workflow**

HORACE: Here is the simplest defensible workflow. Five steps.

STELLA: Counting.

HORACE: One. Define the strategy in one paragraph *before*
looking at data. Two. Use point-in-time data with a one-day lag
between signal and execution. Three. Apply realistic costs based
on the universe. Four. Walk-forward at quarterly or yearly
refits. Five. Compute deflated Sharpe with the honest trial
count.

STELLA: And the deployment threshold?

HORACE: Deflated Sharpe above 0.7 OOS, after costs. Below that —
do not deploy. Period.

STELLA: How much do you bet on a strategy that passes all of
these?

HORACE: A barbell. The strategy goes
into the L4 opportunity sleeve. One to three percent of total
wealth, max. If it works, great. If it doesn't, the 90 percent
core is unaffected. Backtests are not permission to bet large.
They are permission to bet *some*.

---

**[OUTRO - 17:00 to 18:00]**

HORACE: Three rules to take away. One: every backtest lies a
little; the question is how much. Two: deflated Sharpe is the
single most important number you can compute on your own ideas.
Three: turnover times cost is the alpha tax — and on daily
strategies the tax usually exceeds the alpha.

STELLA: Next week — Week 47 — we get into tail risk: how to
hedge the left tail without giving up too much of the right.
Until then, go play with the lab and try to make a strategy
"survive."

HORACE: Most won't. That's the point. See you next week.

[VISUAL: end card]
