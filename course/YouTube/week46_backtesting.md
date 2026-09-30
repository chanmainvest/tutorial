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
