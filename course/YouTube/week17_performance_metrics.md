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
