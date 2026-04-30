# Side Lesson 28: Monte Carlo — Projecting Retirement and the Sequence-of-Returns Trap

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every retirement projection you see online — the bank's planner, the
401(k) provider's "you will have $X at 65" widget, the financial
advisor's slide deck — runs the same arithmetic. Plug in a starting
balance, an assumed return, a horizon, push the button, get one
number. *"At 7% per year for 30 years, your $1M becomes $7.6M."*

That number is a lie. Not because the math is wrong — `1.07^30` does
equal 7.61 — but because the markets you actually live in are not a
constant-return savings account. They deliver +30% in some years
and -25% in others. The calendar matters: getting the bad years
**first** versus **last** can be the difference between dying with
money in the bank and running out of it at age 78. The single-number
projection silently assumes the average returns arrive in a smooth,
well-behaved order. They never do.

Four reasons to learn Monte Carlo simulation properly:

1. **The same average produces wildly different outcomes.** Two
   retirees with identical 30-year average returns can finish with
   $0 or $4M depending only on the *order* in which the returns
   arrived. This is the single most under-appreciated risk in
   personal finance.
2. **The Bengen 4% rule is one number derived from one technique** —
   historical bootstrap on US data 1926-1976. Modern updates from
   Pfau (2020), Kitces, and Morningstar using lower forward-looking
   returns put the safe rate closer to **3.0-3.5%**. If your plan
   assumes 4% you may be 50 basis points too aggressive.
3. **The 95th-percentile-bad outcome is 30-40% lower than the
   median.** Planning to the median is planning for 50/50 success.
   Monte Carlo gives you the *distribution* — the shape and tail —
   not just a point estimate.
4. **SOUL #6**: vol-tail-wags-dog. The tail is not a curiosity; it
   is the entire game in withdrawal phase. A 30% drawdown in
   accumulation phase is a buying opportunity. The same drawdown in
   year three of retirement is a permanent reduction in lifetime
   spending capacity.

---

### 2. What You Need to Know

#### 2.1 Assumed Return + Assumed Vol vs. Monte Carlo

The traditional retirement projection is a single line:

$$ W_T = W_0 \cdot (1 + \mu)^T - C \cdot \frac{(1+\mu)^T - 1}{\mu} $$

where $W_0$ is your starting balance, $\mu$ is the assumed return,
$T$ is the horizon, and $C$ is the annual withdrawal. Plug in
$W_0 = \$1\text{M}$, $\mu = 7\%$, $T = 30$, $C = \$40k$ and the
formula spits out roughly $\$3.5\text{M}$ ending balance. Done.

The problem is that $\mu$ is not a number, it is a *distribution.*
The S&P 500's long-run nominal return is roughly 10% with a standard
deviation of 16%. In any single year the return is most often
somewhere between -22% and +42% (one-sigma band). Over 30 years the
*average* clusters near 10%, but the *path* — the order in which
the years arrive — varies enormously.

Monte Carlo simulation replaces the single line with **thousands of
randomized lines.** In each simulation:

1. Generate 30 random annual returns (or 360 monthly) from a
   distribution matching your assumed return and vol.
2. Compound them through a path with the same starting balance and
   contribution/withdrawal schedule.
3. Record the ending balance.

After 1,000 to 10,000 simulations you have a *distribution* of
outcomes. The 50th percentile is your median expected wealth. The
5th and 95th percentiles bracket the realistic range. The fraction
of paths that ended above zero is your **success probability.**

A 95% success rate on a $40k/yr withdrawal plan is much more honest
than "your expected balance is $3.5M." The first number tells you
the plan works; the second tells you only that *on average* it
works, while leaving you to discover for yourself that on average
you only die once.

![Monte Carlo wealth fan: 1,000 simulated 30-year paths from $1M starting balance with 7% expected return and 15% volatility, no withdrawals. The shaded bands show the 5/25/50/75/95 percentile range. The 90% confidence interval at year 30 spans roughly $3M to $20M — a 6x spread on identical inputs. The median is around $7.6M. The bottom band is the planning case; the top band is the inheritance case.](image/side28_mc_fan.png)

#### 2.2 Sequence-of-Returns Risk — The Killer

Two retirees both retire at 65 with $1M and the same plan: withdraw
$40k inflation-adjusted per year. Both experience the *exact same
30 annual returns.* The only difference is the order. Retiree A
gets a bad first decade; Retiree B gets a bad last decade.

Mathematically they have identical *arithmetic* mean returns — the
calendar can be reshuffled freely without changing the average. But
the wealth paths are completely different. The reason is brutal:
**withdrawals from a depressed portfolio sell more shares than
withdrawals from an inflated portfolio.** A $40k withdrawal at
$700k forces you to liquidate 5.7% of remaining shares; the same
$40k at $1.4M is only 2.9%. The shares sold during a drawdown are
*permanently* gone — they cannot participate in the eventual
recovery.

Run a constructed example: first decade averages -5% per year, last
two decades average +13% per year. Arithmetic mean over 30 years
hits 7%. Run the *opposite* ordering: +13% for 20 years then -5%
for 10. Same mean, same volatility, same end-of-history return.

- **Sequence A (bad early):** Portfolio bleeds out fast. Year-10
  balance roughly $278k. The recovery returns kick in too late —
  the portfolio runs to **zero around year 24**, six years before
  the end of the 30-year plan. Retiree A dies broke.
- **Sequence B (bad late):** Portfolio compounds aggressively for
  20 years to roughly $8M, then bleeds during the bad final decade
  but ends with **multi-million-dollar dynastic wealth.** Retiree B
  leaves an inheritance.

Same mean. Same vol. Same withdrawals. Same starting balance. **The
difference between dying broke and leaving generational wealth is
the calendar order alone.** This is sequence-of-returns risk, and
no single-number projection captures it.

![Sequence-of-returns risk: two paths with identical 7% arithmetic-mean annual returns but reversed orderings. Sequence A (red) front-loads the bad decade and runs out of money around year 24; sequence B (green) back-loads it and finishes with multi-million-dollar wealth. Same withdrawals, same returns, calendar matters.](image/side28_sequence_risk.png)

The retirees most exposed to sequence risk are those in the first
five to ten years of withdrawal, when the balance is largest and
withdrawals are nibbling at the principal. After year 15-20 the
sequence risk attenuates — surviving portfolios are usually large
enough that further drawdowns cannot ruin them.

#### 2.3 The Bengen 4% Rule and Its Modern Updates

In 1994 William Bengen, a financial planner in southern California,
published *Determining Withdrawal Rates Using Historical Data* in the
*Journal of Financial Planning.* He ran a then-novel exercise:
**bootstrap 30-year retirements from the actual historical sequence
of US returns 1926-1976.** For each starting year he asked the same
question: what is the highest constant inflation-adjusted withdrawal
rate that survived all 30 years?

The answer was **4.15%** for a 50/50 stock-bond portfolio. Bengen
rounded down to **4.0% as a "safe" rule of thumb.** The rule rapidly
displaced earlier industry conventions (most of which assumed
withdrawal rates of 6-7% based on average returns, ignoring
sequence risk).

The 4% rule is calibrated to **the worst historical 30-year period
in US data,** not the median. The worst case in Bengen's window was
a retirement starting in 1966, just before the stagflation decade
of 1968-1981. That sequence — bad first 15 years, recovery from
1982 onward — is the canonical sequence-of-returns nightmare. A
portfolio that survived 1966-1995 will, by Bengen's logic, survive
any other 30-year window in the historical sample.

The Trinity Study (Cooley, Hubbard, Walz 1998) ran the same
exercise on a wider date range and slightly different portfolios
and confirmed the 4% number with **96% historical success rate** at
30 years on a 50/50 stock-bond mix. The number stuck.

But: the 4% rule is **historical-bootstrap-derived,** which embeds
two huge implicit bets:

1. The historical equity premium of ~6.5% will persist.
2. The historical 30-year-Treasury yield of ~5% will persist.

In April 2026 neither assumption is on solid ground. Forward-looking
expected returns from sober sources (Vanguard, BlackRock, GMO,
Research Affiliates) cluster around **5-7% nominal for US equities**
and **4-5% for 10-year Treasuries** — well below the historical
numbers Bengen used. Wade Pfau's 2020 update *Safe Withdrawal Rates:
A Comprehensive Examination* recalculated the Bengen exercise using
forward-looking expected returns and found the safe rate falls to
**3.0-3.5%.** Morningstar's 2024 *State of Retirement Income*
report converged on **3.7%** for new retirees under current
valuations.

The practical translation: if you used the 4% rule to set your
nest-egg target, **you may be undersized by 15-30%.** A retiree who
wanted $80k/year with the 4% rule needed $2M. Under a 3.5% rule the
target is $2.29M — a 14% increase in the required nest egg. Under
3.0% it is $2.67M — a 33% increase.

#### 2.4 Bootstrap vs. Parametric Monte Carlo

There are two flavours of Monte Carlo, and the choice matters more
than people realise.

**Parametric MC.** Assume returns follow a parametric distribution
— most often Normal with assumed $\mu$ and $\sigma$. Generate
random samples from the distribution. Run forward.

- Pros: simple, fast, infinitely-extendable, the math is clean.
- Cons: **the distribution assumption is wrong.** Real equity
  returns have fat tails (Week 42 — kurtosis of monthly S&P 500
  returns is roughly 7-15, not the 3.0 a Normal distribution
  predicts). Parametric MC under the Normal assumption
  systematically underestimates the probability of catastrophic
  outcomes.

**Bootstrap MC.** Sample with replacement from the actual historical
sequence of returns. No distributional assumption — the data
generates the distribution.

- Pros: captures fat tails, captures observed correlation structure
  between asset classes, captures observed serial dependence (mean
  reversion at long horizons).
- Cons: limited by the historical sample. The US dataset has only
  about three independent 30-year windows in it. The future may not
  resemble the past.

A practical compromise: **block bootstrap** with 5- to 10-year
blocks. This preserves observed within-block correlation and serial
structure while still allowing recombination. It is the technique
Pfau, Kitces, and most academic researchers default to.

The retail tools (Vanguard's projection tool, Schwab's, the typical
robo-advisor) usually run parametric Normal MC because it is faster
and easier. The underestimate of tail risk is real but typically
small at 30-year horizons (the central limit theorem helps), and
the difference between 3% and 5% safe withdrawal rate is dominated
by the *return assumption,* not the sampling method.

#### 2.5 Reading the Output — Probability of Success

The Monte Carlo output you actually use is not the median ending
wealth, it is the **success rate** — the fraction of simulations
where the plan does not run out of money before the end of the
horizon.

Industry conventions:

| Success rate | Verdict |
|---|---|
| ≥ 95% | Plan is over-funded. Consider spending more or retiring earlier. |
| 85-95% | Solid plan. Normal target. |
| 70-85% | Plan is risky. Build flexibility into withdrawals. |
| < 70% | Plan is broken. Save more, work longer, or spend less. |

Two crucial nuances:

1. **Success rate is binary;** it does not tell you whether the
   failed plans failed at year 23 (recoverable with part-time work)
   or at year 5 (catastrophic). The conditional-on-failure analysis
   is just as important as the headline number.
2. **The 5th-percentile ending balance** is what you should compare
   against the 50th percentile, not against the goal. A plan with a
   95% success rate but a 5th-percentile ending balance of $50k
   leaves you with no margin in the bad scenarios. A plan with 90%
   success but a 5th-percentile ending balance of $1M is far more
   robust to surprises.

The interactive lab on this page exposes both numbers — the success
rate and the 5/50/95 percentile terminal wealth. Practice reading
them as a pair.

#### 2.6 Common Pitfalls

Three modelling mistakes that show up in nearly every retail
retirement projection:

1. **Assuming Normal returns.** Real equity returns are negatively
   skewed and fat-tailed. A Normal model with $\sigma = 16\%$ says a
   single-year -32% return (-2 sigma) happens once every 44 years.
   The empirical record has it happening every 15-20 years on
   average, plus the occasional -45% (1931, 2008-09 cumulative).
   See Week 42.
2. **Assuming constant volatility.** Vol clusters. The 2017 calm
   regime had realized vol of 6%; 2008 had 40%. Models that hold
   $\sigma$ constant at 16% smooth over the regime shifts entirely
   and hide the joint event of "your portfolio drops 35% in the
   year you start withdrawing." Vol-of-vol is a real risk that
   parametric MC ignores.
3. **Ignoring correlation regime shifts.** The 2003-2021 negative
   stock-bond correlation made 60/40 portfolios look bulletproof in
   simulation. The 2022 correlation flip to **+0.3** broke every
   60/40 backtest in real time. Models that assume a static
   correlation matrix between asset classes will under-state crisis
   correlations and over-state diversification benefits — exactly
   the wrong direction for retirement planning.

The fix for all three is the same: **use bootstrap or block-bootstrap
on real historical data,** and stress-test the output by re-running
with the worst observed historical regime as the starting point.
Ask the planner: "what is the success rate if I retire into another
1966?"

#### 2.7 Building Sequence-Risk Robustness Into a Plan

Three structural defences against sequence-of-returns risk that
work in real life:

1. **Cash buffer / two-bucket strategy.** Hold 2-3 years of expenses
   in cash + short Treasuries outside the equity sleeve. In a bear
   market, withdraw from the buffer instead of selling depressed
   equity. Refill the buffer in good years. Reduces forced
   liquidation at lows; small drag on long-run return (~30-50bps).
2. **Variable withdrawal rules.** Instead of $40k inflation-adjusted
   forever, let withdrawals scale with portfolio balance. The
   simplest version (Guyton-Klinger guardrails) cuts withdrawals by
   10% if the current rate exceeds 5% of the portfolio after a bad
   year, and ratchets up by 10% if it drops below 4%. Pfau's
   research finds this lifts the safe initial rate from 3.5% to
   4.5-5% with the same success probability.
3. **Equity glidepath.** Start retirement at 40% equities, ramp up
   to 70% over the first 15 years. This is counterintuitive — most
   people de-risk over time — but it explicitly *reduces* exposure
   to the highest-sequence-risk window and *increases* it during
   the late-retirement window when sequence risk has attenuated.
   Kitces and Pfau (2014) showed it improves success probability by
   2-4 percentage points on the same withdrawal rate.

SOUL #14, barbell, applied to retirement: keep two years of cash
ironclad, let the equity sleeve be aggressive. The bond/cash side
is for *survival*; the equity side is for *return*. Mixing them at
60/40 throughout retirement is the worst of both worlds — too much
volatility for the early years, too little growth for the late
years.

---

### 3. Common Misconceptions

**1. "Monte Carlo gives precise answers."** It gives a probability
distribution, which is much more honest than a point estimate, but
the distribution is only as good as the input assumptions. Garbage
return assumptions produce garbage Monte Carlo output.

**2. "If I average 7% per year I will hit the 7% line."** No. The
*median* of a 30-year 7%-mean path is roughly the 7% line, but
*your* particular path will diverge from the median by a factor of
2-3x in either direction.

**3. "Sequence risk only matters in the first few years of
retirement."** It matters most then, but a bad decade in years 5-15
is also fatal. The risk window extends roughly through year 15-20
of withdrawals.

**4. "More simulations means more accurate results."** Beyond about
1,000-5,000 simulations the Monte Carlo error is dominated by
*model error* (wrong distribution, wrong correlations) rather than
*sampling error.* Running 100,000 sims of a misspecified model just
gets you wrong answers with more decimal places.

**5. "The 4% rule is a law of nature."** It is one specific result
from one specific bootstrap on one specific dataset. Modern updates
using forward-looking returns put the safe rate at 3.0-3.5%.

**6. "If my plan has a 95% success rate I'm safe."** Success rate
is binary. The 5% of failed paths can fail catastrophically (year
5) or marginally (year 28). Always look at the conditional-on-
failure year of ruin alongside the headline rate.

**7. "Monte Carlo accounts for everything."** It accounts for return
volatility within the assumed model. It does not account for: model
risk, regime shifts, your own behavioural failures (panic-selling
in March 2020), longevity uncertainty, healthcare cost shocks, or
divorce. Real retirement planning is Monte Carlo plus stress tests
plus margin.

**8. "Lowering the withdrawal rate fixes the plan."** It fixes the
math. It does not fix the lifestyle problem of having saved for an
$80k/yr retirement and now needing to live on $60k/yr. Plan-fixing
should preferentially happen *before* retirement, not after.

**9. "I'll just adjust if returns are bad."** Sometimes you can,
sometimes you cannot. Health, family obligations, and the labour
market all constrain late-life income flexibility. Variable
withdrawal rules (Guyton-Klinger) build this adjustment into the
plan structurally rather than relying on improvisation.

**10. "Monte Carlo replaces backtesting."** It complements
backtesting. Backtests show what the past actually did; Monte Carlo
shows what *could* happen given assumed dynamics. A plan that
survives both a bootstrap of 1929-1959 *and* a parametric MC at
forward-looking returns has been stress-tested two ways. A plan
that only survives one has not been.

---

### 4. Q&A

**Q1: How many simulations should I run?**

**1,000 to 10,000.** Below 1,000 the percentile estimates are noisy
(the 5th percentile in a 100-path simulation has a wide confidence
interval). Above 10,000 the marginal information is small, and
runtime grows linearly. Most retail tools run 1,000; institutional
planners run 10,000 or more.

**Q2: What return assumption should I use?**

For US equities in April 2026: **5-7% nominal expected return**
(Vanguard CMA: 4.5-6.5%; BlackRock: 6-7%; GMO 7-year: ~3% real for
US large-cap, more for international and value). For bonds: roughly
the current 10-year yield (4.0-4.3% in April 2026) plus 0-50bps for
credit risk. Do not use the historical 10% S&P average — it embeds
the 1980-2000 valuation expansion that is unlikely to repeat.

**Q3: What volatility assumption?**

**S&P 500 long-run vol is roughly 16% nominal.** A balanced 60/40
portfolio is roughly 10-11%. The lab on this page defaults to 15%,
which is a touch optimistic for 100% equities but realistic for the
tilted-equity portfolios most retirees actually hold.

**Q4: Should I model inflation?**

Yes. The simplest method is to deflate everything to today's
dollars: use *real* expected return (subtract 2-2.5% expected
inflation from the nominal) and keep withdrawals fixed in today's
dollars. The output is then directly comparable to your current
spending. The lab does this implicitly — change the inputs to real
returns and the picture works.

**Q5: How do I handle taxes in the projection?**

For most projections, tax is a constant drag — a $40k pre-tax
withdrawal from an IRA at 22% bracket is $31k spending. You can
either (a) reduce the withdrawal goal to after-tax, or (b) use
after-tax expected returns. For tax-mixed portfolios (taxable +
401k + Roth) the order of withdrawals matters and is best handled
by a tax-aware projection tool (NewRetirement, ProjectionLab, or
the IRS's actuarial spreadsheets).

**Q6: What about Social Security?**

Treat it as a fixed inflation-adjusted income stream that reduces
the required portfolio withdrawal. A $30k/yr Social Security benefit
on an $80k spending need leaves $50k from the portfolio — which is
a 5% withdrawal rate on $1M, much more aggressive than the 4%
headline. The portfolio is doing the *marginal* work; SS is the
floor.

**Q7: Should I use parametric or bootstrap MC?**

**Block bootstrap** is the academic standard. Most retail tools use
parametric Normal because it is faster. The difference at 30-year
horizons is modest (1-2 percentage points on success rate). The
return assumption matters far more than the sampling technique.

**Q8: How often should I re-run the simulation?**

Annually at minimum, after any major life change, and after any
market move greater than 15% in either direction. The plan that
made sense in 2019 (8% expected returns, 0% rates) does not make
sense in 2026 (lower equity returns, 4% rates). Static Monte Carlo
is a snapshot; the plan is a process.

**Q9: What is the worst sequence in US history I should stress-test
against?**

**Retirement starting in 1966.** Stagflation 1968-1981, the lost
decade to 1982 in real terms, then a recovery. A 60/40 portfolio
withdrawing 4% inflation-adjusted from a 1966 retirement survived 30
years but with very low ending balance. A 5% rate failed. The 1966
cohort is Bengen's worst case and the canonical sequence-of-returns
nightmare.

**Q10: Where can I run a serious Monte Carlo for free?**

The interactive lab on this page is the educational version. For a
real plan: **Portfolio Visualizer** (free, runs both parametric and
bootstrap MC at retail level), **NewRetirement** (free tier;
tax-aware), **ProjectionLab** (paid; the most flexible). Avoid
single-number projection tools — if it does not show you a
distribution, it is not modelling sequence risk at all.

**Q11: Does the 95th-percentile-bad outcome really matter?**

**Yes.** That is the outcome where you are still alive at 90 with
$50k remaining. Planning to the median means accepting a 50% chance
of running out of money before death — which is a catastrophic
outcome you would not knowingly accept anywhere else in life. The
whole point of running MC is to *see* the bottom of the distribution
and design the plan to survive it.

**Q12: What's the takeaway in one sentence?**

Single-number retirement projections are wrong and dangerous; Monte
Carlo replaces them with an honest distribution of outcomes; the
sequence in which returns arrive matters as much as their average;
the modern safe-withdrawal rate is closer to 3.5% than 4.0%; and
the cash-buffer / variable-withdrawal / glidepath defences let you
push that rate back up while keeping success probability high.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Monte Carlo Retirement Planning — Why "7% per Year" Is a Lie | Side Lesson 28

**RUNTIME TARGET:** ~13 minutes

**HOSTS:**
- **Horace** (teacher): runs the simulation.
- **Stella** (student): asks the questions every retiree has.

---

**[INTRO]**

[VISUAL: Animated logo "Side Lesson 28 — Monte Carlo & Sequence Risk"]

**Horace:** Stella, your bank's retirement planner says you will
have $7.6 million at age 95. Do you believe it?

**Stella:** Probably not, but I am not sure why. The math looks
right.

**Horace:** The math is right. The model is wrong. Today we are
going to look at why every single-number retirement projection is
lying to you, and what to use instead.

---

**[SEGMENT 1: THE LIE OF THE SINGLE NUMBER]**

[VISUAL: bar showing $1M -> $7.61M with the formula 1.07^30 = 7.61]

**Horace:** Here is the standard projection. You have $1 million
today, you do not contribute or withdraw, you compound at 7% per
year for 30 years. Result: $7.61 million.

**Stella:** That is exactly what my 401k page tells me.

**Horace:** Yes, and the number is mathematically perfect and
operationally useless. The market does not deliver 7% per year. It
delivers 30% one year and -25% the next. The compound gets you to
roughly 7%, but the *path* matters.

---

**[SEGMENT 2: THE FAN CHART]**

[VISUAL: image/side28_mc_fan.png]

**Horace:** This is the same projection done honestly. One thousand
random paths, each one drawing 30 annual returns from a Normal
distribution with 7% mean and 15% standard deviation, all starting
at $1 million, all running 30 years.

**Stella:** Wide.

**Horace:** Very wide. The median path lands around $7.6 million,
matching the textbook answer. But the 95th-percentile path ends near
$20 million, and the 5th-percentile path ends around $3 million.
Same starting balance, same return assumption, same vol. The
difference is the order in which the returns arrived.

**Stella:** $3 million is still fine though.

**Horace:** It is — for the no-withdrawal case. Now let us add
withdrawals.

---

**[SEGMENT 3: SEQUENCE OF RETURNS RISK]**

[VISUAL: image/side28_sequence_risk.png]

**Horace:** Two retirees. Both start with $1 million at age 65. Both
withdraw $40,000 per year — the famous 4% rule. Both experience the
exact same 30 annual returns. Same average. Same volatility.

**Stella:** And...

**Horace:** Retiree A gets the bad decade first. The first ten years
average -5% per year. Then years 11 through 30 deliver +13% per
year. Average over the full 30 years is 7%. Math says fine.

**Stella:** And reality says...

**Horace:** Retiree A runs out of money around year 24. Six years
before the end of the plan. Retiree B gets the *exact same returns
in reverse* — the good decades first, then the bad decade at the
end. Retiree B finishes with several million in the bank.

**Stella:** Same returns. Same withdrawals. The ordering kills one
of them?

**Horace:** The ordering kills one of them. This is sequence-of-
returns risk and it is the single most underappreciated risk in
personal finance. Withdrawing from a depressed portfolio sells more
shares than withdrawing from an inflated one. The shares you sell
at the bottom never participate in the recovery. Permanent capital
destruction.

---

**[SEGMENT 4: THE 4% RULE AND ITS UPDATE]**

[VISUAL: Title card "Bengen 1994 -> Pfau 2020"]

**Horace:** Bengen, 1994, ran this exercise on US data 1926-1976
and found that a 50/50 portfolio could safely withdraw 4.15% of the
initial balance, inflation-adjusted, for 30 years. He rounded to
4.0% and the rule stuck.

**Stella:** And the 4% rule is fine?

**Horace:** It was fine in 1994. It assumed the 1926-1976 historical
returns would persist — equity premium of 6.5%, ten-year Treasury
of 5%. In April 2026 forward-looking expected returns from sober
sources cluster at 5-7% nominal for equities and 4-4.5% for ten-year
Treasuries. Pfau ran the same Bengen exercise with these
forward-looking numbers and the safe rate fell to 3 to 3.5%.

**Stella:** That is a big difference.

**Horace:** Half a percent on $80,000 a year is $400 a month forever.
And in nest-egg terms, going from 4% to 3.5% means you need 14%
more saved for the same retirement. The market's lower forward
returns translate one-to-one into bigger required nest eggs.

---

**[SEGMENT 5: BOOTSTRAP VS PARAMETRIC]**

[VISUAL: Title card "Two Flavours of Monte Carlo"]

**Horace:** Two ways to generate the random returns. Parametric:
assume Normal distribution with given mean and vol, draw samples.
Bootstrap: sample with replacement from actual historical returns.

**Stella:** And the difference?

**Horace:** Real equity returns are fat-tailed. Kurtosis of monthly
S&P returns is 7 to 15 — Normal predicts 3. Parametric Normal
under-models the tail. Bootstrap captures it directly. The academic
standard is **block bootstrap** — sample 5- or 10-year blocks at a
time so you preserve correlations and serial structure.

**Stella:** Which does the lab use?

**Horace:** Parametric Normal, for speed and simplicity in the
browser. The take-away difference at 30-year horizons is roughly 1
to 2 percentage points on the success rate. The return *assumption*
matters far more than the sampling method.

---

**[SEGMENT 6: THE INTERACTIVE LAB]**

[VISUAL: cut to interactive/side28_mc_lab.html]

**Horace:** Five sliders. Starting balance, monthly contribution or
withdrawal — positive for accumulation, negative for retirement —
expected return, volatility, and horizon.

*(types: balance $1M, withdrawal -$3,333/mo i.e. -$40k/yr, return 7%, vol 15%, horizon 30y)*

**Horace:** That is the Bengen baseline. Look at the success rate.

*(reads the dashboard)*

**Horace:** Around 85-90%. Below the 95% comfort threshold. The 5th
percentile ending balance is zero — that is what Pfau warned about.

*(adjusts withdrawal to -$3,000/mo / -$36k/yr)*

**Horace:** Now into the low 90s. Adjust to -$2,917 — that is 3.5%
— and the success rate moves toward 95%. That is the modern safe
rate.

**Stella:** What if I want to go to 4% and stay safe?

**Horace:** Two ways. Reduce vol — 60/40 instead of 100% equities.
Or build flexibility — variable withdrawals. The Guyton-Klinger
guardrails I mentioned in the reading. Both lift the safe rate by
50-100 basis points without changing the success target.

---

**[SEGMENT 7: PITFALLS]**

[VISUAL: Title card "Three Modeling Mistakes"]

**Horace:** Three things any honest practitioner will tell you the
parametric Monte Carlo gets wrong. One: assumes Normal returns when
reality is fat-tailed. Two: assumes constant volatility when real
vol clusters and shifts regime. Three: assumes constant correlations
between asset classes when 2022 just demonstrated that those
correlations can flip in a quarter.

**Stella:** So why use it at all?

**Horace:** Because it is honest about what it can model — the
distribution of paths under the assumed dynamics — and that is
already infinitely better than a single-number projection. Run
parametric MC. Then run bootstrap MC. Then stress-test against the
1966 cohort. If the plan survives all three, you have a real plan.
If it only survives one, you have a wish.

---

**[SEGMENT 8: THE BARBELL APPLIED]**

[VISUAL: Title card "Sequence-Risk Defenses"]

**Horace:** Three structural defences. Cash buffer — two years of
expenses outside the equity sleeve so you do not have to sell during
a drawdown. Variable withdrawals — let spending flex with balance.
Equity glidepath — start retirement at 40% equities, ramp *up* to
70% over 15 years.

**Stella:** Up, not down?

**Horace:** Up. Counterintuitive but right. The first decade is when
sequence risk is fatal — that is when you want *less* equity
exposure. The second and third decades are when sequence risk has
attenuated — that is when you want *more* equity exposure for the
return. SOUL fourteen, barbell, applied to retirement: cash
ironclad on one side, equity aggressive on the other, and reduce
the middle.

---

**[OUTRO]**

[VISUAL: Summary card with three bullets:
- Single-number projections lie about sequence risk
- 95th percentile bad case is 30-40% below median
- Bengen 4% is now closer to 3.5% on forward returns]

**Horace:** Three takeaways. One: any retirement projection that
gives you a single number is hiding sequence risk. Get a tool that
shows you a distribution. Two: the median is a coin flip; plan to
the 5th percentile of the distribution. Three: the 4% rule is a
1994 result on 1926-1976 data; the modern equivalent is closer to
3.5%, and the gap is real money.

**Stella:** Got it. Run the distribution, look at the bad tail, plan
to a 3.5% withdrawal, build the cash buffer, run the glidepath up.

**Horace:** That is the lesson. Markets do not deliver averages.
They deliver paths. Plan for the path, not the average.

[END CARD: "Side Lesson 28 — Monte Carlo & Sequence Risk"]
