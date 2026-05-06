# Week 17: Performance Metrics — Sharpe, Sortino, Calmar, IR, Treynor, Alpha and Beta

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A return number on its own is almost useless. "I made 18% last year"
is a sentence; it is not an evaluation. It tells you nothing about
how much risk was taken to earn it, how often the strategy lost
money, or whether the same dollar in an index fund would have done
better. Professional investors, allocators, due-diligence teams, and
honest self-assessing retail investors all live in the world of
**risk-adjusted return** — return per unit of something painful.

You need this material for four reasons.

1. **Evaluating funds and managers.** Every fund tear-sheet on the
   planet quotes Sharpe, max drawdown, and tracking error. If you
   cannot read those numbers and intuit what they mean — what a
   Sharpe of 0.4 versus 1.2 actually feels like in client account
   statements — you will overpay for mediocre managers and miss
   genuinely good ones.
2. **Honestly grading yourself.** A 30% year is impressive only if
   you took less than 30% in vol to get it, and only if you can
   show it was not pure beta to a 30% market. Without Sharpe,
   Sortino, alpha, and beta, your year-end review is just
   storytelling.
3. **Picking the right metric for the right job.** Sharpe is the
   default but it punishes upside vol the same as downside. Calmar
   focuses on the worst pain. IR tells you whether your active bets
   actually paid. Treynor looks only at the systematic risk you
   could not diversify away. Each metric answers a different
   question; using the wrong one gives you the wrong answer.
4. **The vol tail wags the dog.** Standard deviation
   assumes returns are normally distributed. They are not. Tails
   are fat. So Sharpe consistently *under-penalises* strategies
   that quietly accumulate left-tail risk. Sortino and Calmar
   partially fix that. Knowing which metric flatters which
   strategy is most of the alpha in due diligence.

This lesson works through the whole taxonomy, runs every metric on
the Damodaran 1928-2024 dataset for four model portfolios, and
shows you how the rank order across metrics can reorder your
preferences.

---

### 2. What You Need to Know

#### 2.1 The Sharpe Ratio — Excess Return per Unit of Total Volatility

The Sharpe ratio is the foundation. Bill Sharpe (Nobel 1990) wrote
it down in 1966. The formula is simple:

$$ \text{Sharpe} = \frac{R_p - R_f}{\sigma_p} $$

Numerator: the **excess return** — your portfolio's return minus
the risk-free rate (3-month T-Bill). Denominator: the **total
standard deviation** of your portfolio's returns.

The Sharpe ratio answers: *how much return did this portfolio earn
per unit of total volatility?* Higher is better. A few rough
benchmarks for annualised Sharpe over a long horizon:

| Sharpe (annualised) | Interpretation |
|---|---|
| < 0 | Lost to the risk-free rate. Negative compensation for risk. |
| 0.0 - 0.3 | Mediocre. The S&P 500 averages about 0.4 over a century. |
| 0.3 - 0.6 | Decent. Most balanced portfolios live here. |
| 0.6 - 1.0 | Genuinely good — if real and persistent. |
| 1.0 - 2.0 | Excellent. Top quartile hedge funds, well-run risk parity. |
| > 2.0 | Suspicious. Either short data window, hidden tail risk, or fraud. |

Two important practical points.

**The frequency rescaling trap.** Sharpe is normally quoted
annualised. If you compute it from monthly returns, you must
multiply by $\sqrt{12}$, not 12. From daily, by $\sqrt{252}$. This
follows from the assumption that monthly returns are independent —
which they are not, exactly, but the convention has stuck. A
strategy with a monthly Sharpe of 0.30 has an annualised Sharpe of
$0.30 \times \sqrt{12} \approx 1.04$, not 3.6.

**The vol-tail problem.** Sharpe uses $\sigma$, which assumes
returns are roughly symmetric around the mean. They are not.
1987's -22% Black Monday was a 20-sigma event under a normal
model — meaning it should not have happened in the lifetime of the
universe. Yet there it was. So Sharpe systematically rewards
strategies that look smooth most of the time but blow up rarely
(short volatility, illiquid credit, leveraged carry). The volatility
tail wags the dog — do not pick managers on Sharpe alone.

#### 2.2 Sortino — Downside Deviation Only

The Sortino ratio is Sharpe's first repair. It replaces total
volatility with **downside deviation only**: the standard
deviation of returns *below a target*, usually zero or the
risk-free rate.

$$ \text{Sortino} = \frac{R_p - R_f}{\sigma_d} \quad \text{where} \quad \sigma_d = \sqrt{\frac{1}{N}\sum_{r_i < t}(r_i - t)^2} $$

By design, upside volatility no longer hurts your score — only
losses do. For a positively-skewed strategy (lots of small losses,
occasional big gains; trend-following is the classic example) the
Sortino ratio is materially higher than Sharpe. For a negatively-
skewed strategy (selling vol, picking up nickels in front of a
steam-roller) Sortino is closer to or worse than Sharpe.

A useful rule of thumb: when **Sortino is at least 1.4× Sharpe**,
the strategy has positive skew and the manager is genuinely
managing downside. When **Sortino is barely higher than Sharpe**,
the return distribution is symmetric or worse — left tail and
right tail look similar, and the manager is just running risk.

#### 2.3 Calmar — Return per Unit of Worst-Case Pain

Calmar is the cleanest answer to: *what is my return divided by my
worst draw-down?*

$$ \text{Calmar} = \frac{\text{Annualised return}}{|\text{Max drawdown}|} $$

If a strategy returns 12% annualised and the worst peak-to-trough
draw was 30%, Calmar is 0.40. Calmar values above 0.5 are good;
above 1.0 is rare and excellent over a long sample. The S&P 500
since 1928 has a Calmar of roughly **0.10** (≈10% return / ≈86%
1929-32 drawdown).

The strength of Calmar: it focuses on a single number every
investor actually cares about — the worst loss they would have
sat through. The weakness: it depends on the sample window. A
strategy launched in 2010 that never met its 2008 has a
flattering Calmar; a strategy whose track record happens to start
right before a crisis looks worse than it is. Always ask: *does
this Calmar include the worst available regime?*

#### 2.4 Information Ratio — Active Return per Unit of Tracking Error

For an *active* manager — one who claims to beat a specific
benchmark — Sharpe alone is insufficient. The right question is:
*per unit of how much you deviate from the benchmark, how much
extra return do you produce?*

The Information Ratio:

$$ \text{IR} = \frac{R_p - R_b}{\sigma(R_p - R_b)} = \frac{\text{Active return}}{\text{Tracking error}} $$

Numerator: the **active return** (your return minus the benchmark's
return). Denominator: the **tracking error** (standard deviation of
the difference). A closet-indexer with low tracking error and a
small positive active return can have a high IR; a wild stock-
picker with both large active return and large tracking error can
have a mediocre one.

Industry shorthand:

- IR < 0.0: Worse than the benchmark. Fire the manager.
- IR = 0.5: Top quartile institutional active manager.
- IR = 1.0: Top decile. Genuinely great.
- IR > 2.0: Vanishingly rare; demand to see the strategy in detail.

IR is the metric every pension consultant uses to grade active
managers. If you ever pay a fee above passive, you should know
yours.

#### 2.5 Treynor — Excess Return per Unit of Beta

Sharpe divides by *total* risk. Treynor divides only by
**systematic** risk — the part you cannot diversify away:

$$ \text{Treynor} = \frac{R_p - R_f}{\beta_p} $$

where $\beta_p$ is the slope of your portfolio's returns regressed
on the market's. A diversified equity sub-portfolio with $\beta = 1$
and 12% excess return has Treynor 0.12. A market-neutral fund with
$\beta \approx 0$ produces a divide-by-near-zero — Treynor is
undefined or infinite, which is a clue Treynor is the wrong metric
for hedged strategies.

Use Treynor when you are evaluating a sub-portfolio inside a
larger book — for example, deciding whether the 40% of your
equity sleeve that is in tech is earning enough for its market
exposure, ignoring its idiosyncratic noise that diversifies away
at the parent level. Use Sharpe when you are evaluating a
stand-alone investment.

#### 2.6 Jensen's Alpha and Beta — From the CAPM Regression

Beta and alpha both come out of the same equation: the CAPM
regression of excess returns:

$$ R_p - R_f = \alpha + \beta (R_m - R_f) + \varepsilon $$

Run that regression on your monthly returns versus the S&P 500's,
and:

- $\beta$ is the slope. It tells you how much your portfolio
  moves for each unit of market move. $\beta = 1.2$ means a
  1% market drop drags you down ~1.2%.
- $\alpha$ is the intercept. It is what you earned **above** the
  return CAPM said you should have earned for taking that beta
  exposure. Annualised, alpha is the holy grail.

A few honest realities:

1. Most retail strategies have alpha statistically indistinguishable
   from zero. Alpha is rare. Treat any alpha estimate
   from fewer than 60 monthly observations as extremely noisy.
2. Beta is often more useful than alpha for *risk decomposition*.
   If $\beta = 1.4$, your "stock pick" is really 1.4× S&P leverage
   plus some noise; the size of that lever explains most of
   what is happening to the equity curve.
3. Alpha can be persistent for short windows by luck. It can also
   be persistent because of an undisclosed factor exposure
   (small-cap, value, low-vol, momentum). Modern attribution
   strips those out before declaring "alpha".

The interactive at the end of this lesson lets you draw the CAPM
scatter live: portfolio monthly excess returns vs S&P 500 excess
returns, with $\alpha$ as the intercept and $\beta$ as the slope.

#### 2.7 The Metrics Disagree, On Purpose

The whole reason there are five-plus ratios is that **they
emphasise different parts of the return distribution**. The chart
below runs Sharpe, Sortino, Calmar, and Treynor on four canonical
portfolios using Damodaran 1928-2024:

![A 2x2 bar grid showing four risk-adjusted metrics across four model portfolios (100/0 stocks, 60/40, 30/70, 0/100 bonds) computed on Damodaran 1928-2024. Each metric panel ranks the portfolios differently. Sharpe favours the 60/40 mix; Calmar punishes 100% stocks heavily because of the 1929-32 drawdown; Treynor undefined-or-extreme on the bond-heavy book because beta-to-equities is small. The visual point: pick a different metric, get a different winner.](image/week17_metric_comparison.png)

Notice: by Sharpe, the 60/40 mix scores highest because the
correlation discount on volatility (Week 4) lifts the denominator's
denominator. By Calmar, all-bonds wins because the bond series'
worst drawdown over the sample is shallower than the 1929-32 stock
loss. By Treynor, the all-stock portfolio looks fine because beta
=1 by construction — but Treynor on the bond portfolio is
calculated against equity beta and looks unreliable. Same data,
four different rankings.

This is not a bug. It is the entire point. A defensible portfolio
review reports **at least three metrics** and explains where they
agree and where they disagree.

#### 2.8 Sharpe Through Time — The Regime Story

Even for a single asset, the Sharpe ratio is not a constant. Below
is the rolling 10-year Sharpe of the S&P 500 (excess over 3-month
T-Bills) since 1937:

![Rolling 10-year Sharpe ratio of the S&P 500 over 3-month T-Bills, 1937-2024, computed on Damodaran annual data. The line oscillates between roughly 0.0 in the 1970s stagflation window and near 1.5 in the post-GFC 2010s, with intermediate troughs around 2002 and 2009. The chart visualises why naïve Sharpe quotes drawn from a single decade are unreliable: regime drives the number.](image/week17_sharpe_window.png)

The line is wild. In the 1970s, a 10-year window earning roughly
zero excess over T-Bills produced a Sharpe near 0.0. In the
1980s-1990s tailwind, Sharpe climbed past 1.0. The 2000s
double-decade-of-disappointment (dot-com + GFC) cratered it back
toward zero. The 2010s rebuilt it to ~1.5 on the back of QE-driven
multiple expansion.

The takeaway: be very careful when someone quotes "the long-run
Sharpe of the S&P 500 is X." It is X *over the chosen window*.
The 1980-2020 regime was anomalous — and so
was its Sharpe.

---

### 3. Common Misconceptions

1. **"Sharpe of 2 is great."** It is *too* great. Real,
   long-horizon, capacity-bearing Sharpes above ~1.2 are rare.
   A short-window Sharpe of 2 usually decomposes into either
   selection bias (the survivors), short data (overfit), or
   hidden tail risk (about to blow up).
2. **"Higher Sharpe = lower risk."** Higher Sharpe = better
   excess return per unit of *measured* risk. If the risk
   measure (standard deviation) misses fat tails, the apparent
   Sharpe lies — the volatility tail wags the dog.
3. **"Calmar is fairer than Sharpe because it uses real
   drawdowns."** Calmar is sample-dependent. A strategy with no
   crisis in its track record has artificially high Calmar. The
   right comparison is Calmar over a *common window* including
   stress periods.
4. **"Sortino rewards skill."** Sortino rewards return shape, not
   skill. A leveraged long-only equity book with no risk
   management has a high Sortino in any sustained bull market.
5. **"Beta = risk."** Beta = systematic risk *to the market you
   regressed on*. A "low-beta" stock with $\beta=0.4$ to the
   S&P 500 may have $\beta=2$ to oil prices. The beta you
   compute depends entirely on the chosen market index.
6. **"Alpha proves skill."** Alpha proves *unexplained excess
   return given the chosen factor model*. If your model omits
   small-cap, value, momentum, or quality, you will read off
   alpha that is really just a known factor premium. Most
   "alpha" in academic backtests pre-1995 has since been
   shown to be omitted-factor exposure.
7. **"Information ratio measures the same thing as Sharpe."** No
   — Sharpe is total excess over total vol. IR is *active*
   excess over *tracking error*. A manager with low IR but high
   Sharpe is just running market beta.
8. **"Treynor is better than Sharpe because it uses beta."**
   Treynor only makes sense when the portfolio is part of a
   larger diversified book where idiosyncratic risk genuinely
   diversifies away. For a stand-alone retirement account,
   Sharpe is the correct metric.
9. **"You annualise Sharpe by multiplying by 12."** No. By
   $\sqrt{12}$. Multiplying by 12 inflates Sharpe by a factor
   of 3.46 and is a classic résumé fraud signal.
10. **"Risk-adjusted return is the only thing that matters."**
    Risk-adjusted return matters for *picking among* strategies of
    similar absolute return. But a 0.6 Sharpe at 12% return
    grows your wealth far more than a 1.2 Sharpe at 4% return.
    Real wealth is built on the absolute return; Sharpe just
    helps you choose between two paths to the same end.

---

### 4. Q&A Section

**Q1. Which metric should I quote first when describing a fund?**
A1. Sharpe is still the default and the easiest for a literate
audience to interpret. Pair it with max drawdown and one of
{Sortino, Calmar} so the reader can spot fat-tail strategies.
Quoting only Sharpe in 2026 is a yellow flag.

**Q2. What risk-free rate do I use?**
A2. For US-dollar-denominated portfolios, the 3-month T-Bill yield
matched in time to your return series. Damodaran's annual table
includes this column. Annualised series use the year-end T-Bill;
monthly series use the prevailing T-Bill divided by 12.

**Q3. My monthly Sharpe is 0.4, my annualised is 1.4. Why the gap?**
A3. Annualised Sharpe = monthly Sharpe × √12 = 0.4 × 3.46 = 1.39.
That is correct.

**Q4. How long a window do I need before Sharpe is meaningful?**
A4. At minimum 3 years (36 monthly observations). Below that, the
standard error of Sharpe is so large the number is essentially
random. Five to ten years is typical for institutional allocation
decisions.

**Q5. What if my portfolio has no market beta — is Treynor useful?**
A5. No. Treynor with $\beta \approx 0$ is mathematically unstable
(divide by near-zero). Use Sharpe and Calmar for market-neutral
strategies. Treynor is for sub-portfolios with clear directional
market exposure.

**Q6. Sortino > Sharpe. Should I always prefer high Sortino strategies?**
A6. Probably yes — but only if you confirm the sample includes a
real drawdown event. A trend-following strategy looks fantastic on
Sortino during a sustained trend; the test is how it does in a
choppy, mean-reverting regime.

**Q7. Why do hedge funds quote IR more than Sharpe?**
A7. Because hedge fund LPs typically benchmark them against an
index (long-short equity vs. S&P 500, market-neutral vs. T-Bills,
etc.). IR is the natural metric for "did your active risk pay?"
Sharpe answers a different question: "did your absolute return
compensate me for absolute volatility?"

**Q8. Can a portfolio have positive alpha but a negative Sharpe?**
A8. Yes, in stress periods. Alpha just measures unexplained excess
over CAPM. If the market and your portfolio both lose money, but
yours loses *less than CAPM said you should have lost given your
beta*, alpha is positive while raw Sharpe is negative. 2008
Treasury managers had this experience.

**Q9. How do I compute beta for a long-short portfolio?**
A9. Same regression: monthly excess returns of the portfolio
versus monthly excess returns of the S&P 500. The slope is your
**net** beta. Gross beta (sum of long beta + short beta absolute
values) is a separate exposure measure for risk attribution.

**Q10. The risk-free rate has been near zero for a decade. Does
that distort Sharpe?**
A10. It inflates it. With $R_f \approx 0$, raw return *equals*
excess return, so Sharpe rises mechanically when rates fall. To
compare across regimes, always use the contemporaneous T-Bill
rate, not a constant assumption.

**Q11. Why does the rolling Sharpe of the S&P 500 swing so wildly?**
A11. Because both numerator and denominator move with the regime.
In low-vol bull markets (1990s, 2010s) the numerator is high and
denominator low — Sharpe explodes. In stagflation (1970s) or
crisis decades (2000s) numerator collapses and denominator rises
— Sharpe craters. Regime drives almost everything in
quoted single-number stats.

**Q12. What single number would Horace use to grade his own year?**
A12. Two numbers, not one: realised CAGR and max intra-year
drawdown. Then a sanity check: Sharpe over 3-year and 10-year
rolling windows to see whether the year was on-trend or a fluke.
"Risk-adjusted return" in a single ratio is always partial.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Sharpe Is Lying to You: The Real Toolkit for Grading Investment Performance

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO - 0:00 to 1:20]**

[VISUAL: title card on cream background, gold accent, "Week 17: Performance Metrics"]

HORACE: Welcome back. This is Week 17 of the chanmainvest course.
Today is the most-quoted, most-misunderstood corner of finance:
risk-adjusted performance metrics. Sharpe, Sortino, Calmar, IR,
Treynor, alpha, beta.

STELLA: That's a big alphabet soup. Why so many ratios for
basically the same idea — return divided by risk?

HORACE: Because "risk" is not one thing. Total volatility is one
definition. Downside-only volatility is another. Worst drawdown
is a third. Tracking error is a fourth. Each metric corresponds
to a different definition of risk, and each one flatters a
different kind of strategy.

STELLA: So picking the right metric is half the battle.

HORACE: It's *all* of the battle. By the end of this episode you
will know which metric to ask for, which to ignore, and how to
use them together to spot strategies that quietly accumulate
fat-tail risk.

[VISUAL: cut to chapter list]

---

**[SECTION 1 - 1:20 to 4:00] - Sharpe**

HORACE: Start with the foundation. The Sharpe ratio is excess
return — your return minus the risk-free rate — divided by total
standard deviation.

[VISUAL: equation overlay, $\text{Sharpe} = (R_p - R_f) / \sigma_p$]

STELLA: And what's a good Sharpe?

HORACE: Long-run S&P 500: about 0.4. A balanced 60/40: about 0.5.
Top-quartile active managers: 0.7 to 1.0. Anything above 1.5 over
a long sample is suspicious.

STELLA: Suspicious how?

HORACE: Either short data window — easy to look great over five
years if you avoid a crisis — or hidden tail risk. Long-Term
Capital Management ran a Sharpe above 4 right up until the day it
blew up.

STELLA: That's terrifying.

HORACE: That's the underlying lesson — the volatility tail wags the
dog. Sharpe assumes returns are normally distributed. They are
not. So strategies that look smooth most of the time but explode
rarely score very high on Sharpe — until they don't.

[VISUAL: image/week17_sharpe_window.png — the rolling 10-year
S&P 500 Sharpe chart]

HORACE: Here's why even single-asset Sharpe is unreliable. This is
the rolling 10-year Sharpe of the S&P 500 over 3-month T-Bills,
1937 to today. Look at the range — from near zero in the 1970s,
to roughly 1.5 in the post-GFC 2010s.

STELLA: A factor of fifteen?

HORACE: A factor of fifteen, on the same asset, just by changing
the window. So when someone says "the Sharpe of stocks is 0.4,"
you should ask: *over which window?*

---

**[SECTION 2 - 4:00 to 6:30] - The frequency rescaling trap]**

STELLA: One thing that confuses people is annualising. If I have
monthly Sharpe of 0.3, what's the annual?

HORACE: Times square-root-of-12. About 1.04. Not times 12.

STELLA: Where does the square root come from?

HORACE: It's the same scaling rule we used in Week 4 for
volatility. If you assume monthly returns are independent, the
variance scales linearly with time, but the standard deviation —
which is the square root of variance — scales with the square
root of time.

STELLA: So multiplying by 12 instead of square-root-of-12 inflates
Sharpe by a factor of...

HORACE: 3.46. That's the résumé-fraud number. Anyone who quotes a
monthly Sharpe times 12 is either lying or doesn't know what
they're doing. Either way, walk away.

---

**[SECTION 3 - 6:30 to 9:00] - Sortino, Calmar]**

HORACE: Sharpe punishes upside vol the same as downside. Sortino
fixes that by using only downside deviation.

[VISUAL: equation overlay, Sortino with $\sigma_d$]

STELLA: So a strategy with big up moves and small down moves
scores higher on Sortino than on Sharpe?

HORACE: Exactly. Trend-following is the textbook example —
positively skewed, lots of small losing months, occasional huge
winning months. Sortino can be 1.5x Sharpe for a good trend book.

STELLA: And Calmar?

HORACE: Calmar is the bluntest, most honest metric. Annualised
return divided by absolute max drawdown. Asks the question every
investor actually cares about: how much pain did you put me
through to earn that return.

STELLA: Pain in what units?

HORACE: Peak-to-trough percentage. The S&P 500's worst was 86%
during 1929-32. So even at a 10% long-run return, the S&P's
century Calmar is about 0.10. A Calmar above 1.0 over a long
sample is genuinely excellent.

STELLA: But Calmar depends on whether the sample contains a
crisis, right?

HORACE: Right. A strategy launched in 2010 that has never seen a
crisis quotes a flattering Calmar. Always ask: does the window
include the worst available regime?

---

**[SECTION 4 - 9:00 to 11:30] - IR and Treynor]**

HORACE: Information Ratio. Active return divided by tracking
error. The metric pension consultants use.

STELLA: Active return — meaning your return minus the benchmark's?

HORACE: Yes. And tracking error is the standard deviation of that
difference. So a closet-indexer with low tracking error and a
small consistent edge has a high IR. A wild stock-picker with
big edge and big tracking error can have a mediocre IR. The
ratio cares about *consistency of active payoff*, not magnitude.

STELLA: Where does Treynor fit?

HORACE: Treynor is excess return divided by beta. Use it when
you're evaluating a sub-portfolio — like the tech slice of your
equity sleeve — and you only care about systematic exposure
because the idiosyncratic noise diversifies away at the parent
level.

STELLA: And don't use it when?

HORACE: When the portfolio is stand-alone, or when beta is near
zero. A market-neutral fund's Treynor is divide-by-near-zero —
mathematically unstable. Use Sharpe.

---

**[SECTION 5 - 11:30 to 14:00] - Alpha and beta from CAPM]**

HORACE: Beta and alpha both come out of one regression. Take your
portfolio's monthly excess returns. Take the S&P 500's monthly
excess returns. Regress one on the other.

[VISUAL: equation overlay, $R_p - R_f = \alpha + \beta(R_m - R_f) + \varepsilon$]

HORACE: The slope is beta. The intercept is alpha. Beta tells you
how much of your return is just leverage on the market. Alpha
tells you what you earned beyond what CAPM said you should have.

STELLA: And alpha is the holy grail.

HORACE: Alpha *annualised, statistically significant, persistent
out of sample, and not explained by a known factor* is the holy
grail. Alpha is rare. Most "alpha" you read
in retail backtests is one of three things — small sample noise,
omitted factor exposure, or survivorship bias.

STELLA: How long a sample do you need before alpha is real?

HORACE: At least 60 monthly observations. Below that, your t-stat
is so noisy the alpha estimate is essentially random.

STELLA: We have an interactive that lets you see this live, right?

HORACE: We do. The lesson page has a CAPM scatter — pick a stock
weight and start year, watch the regression line redraw, and
read off alpha and beta in real time.

[VISUAL: cut to interactive, ml-metrics-lab]

---

**[SECTION 6 - 14:00 to 16:30] - Metrics disagree]**

[VISUAL: image/week17_metric_comparison.png]

HORACE: This is the punch-line chart. Four model portfolios —
100% stocks, 60/40, 30/70, 100% bonds — on Damodaran 1928-2024.
Four metrics — Sharpe, Sortino, Calmar, Treynor.

STELLA: And the rank order changes?

HORACE: Constantly. By Sharpe, 60/40 wins because the correlation
discount on volatility lifts the denominator's denominator. By
Calmar, the bond-heavy book wins because its worst drawdown is
shallower. By Treynor against equity beta, the bond books look
unstable because their equity-beta is small.

STELLA: So how do you pick the "right" portfolio?

HORACE: You don't pick on a single metric. A serious portfolio
review reports at least three — Sharpe, Sortino, max drawdown —
and explains where they agree and where they disagree. Then you
make a judgement informed by *all* of them, plus the regime
context.

---

**[SECTION 7 - 16:30 to 17:30] - The lab]**

HORACE: The interactive on this page lets you build a stock-bond
portfolio with any weight from zero to 100, pick a start year
between 1928 and 2010, and watch six metrics update live: Sharpe,
Sortino, Calmar, max drawdown, volatility, and geometric
annualised return.

STELLA: And the side chart?

HORACE: The CAPM scatter. Each dot is one year. Slope is your
beta to the S&P 500; intercept is your annualised alpha. Try
running a 100% stock book — beta should be exactly 1.0, alpha
exactly 0, by construction. Then dial down to 30/70 and watch
beta fall while alpha drifts toward whatever the bond's edge over
the equity-implied return was in that period.

---

**[OUTRO - 17:30 to 18:00]**

HORACE: Three rules to take away. One: never quote a single
metric. Two: always check the sample window. Three: when Sharpe
and Sortino agree, the return distribution is symmetric; when
they disagree, look at the skew before deciding which is more
honest.

STELLA: Next week — Week 18 — we get into the practical question
of what to actually do with these metrics in portfolio
construction. Until then, go play with the lab and try to break it.

HORACE: See you next week.

[VISUAL: end card with course logo]
