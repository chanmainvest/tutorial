## Part 2: YouTube Script

---

**VIDEO TITLE:** VaR, CVaR, and Why All Three Methods Break in the
Tails — Risk Management Without the Lies (Week 42)

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:20]**

**Stella:** Welcome back to Week 42. Last week we did the conceptual
side of risk management — how big to size, when to cut, how to
budget pain across positions. This week we put numbers on it.

**Horace:** And this week is the most-quoted, most-misused risk
number on Wall Street. Value at Risk. VaR. Every bank in the world
runs one. Every fund tear-sheet shows one. And every single one of
them is wrong in the tail. So today we are going to learn three
ways to compute it, why all three are wrong, and what the smart
people do instead.

**Stella:** That sounds like a setup for the marshmallow conclusion
already.

**Horace:** It is. The volatility tail wags the dog. Parametric VaR
at 95% is a useful number. At 99% it is a guess. At 99.9% it is
fiction. The difference between those three statements ate
Long-Term Capital, the structured-credit desks in 2008, and the
vol-targeting funds in March 2020. So pay attention.

**[1:20 — Section 1: The definition]**

**Horace:** First the definition, slowly. Value at Risk is the
**largest loss you do not exceed with a given probability over a
given horizon**. Three knobs. Confidence level — usually 95 or 99.
Time horizon — usually one day or ten days. Currency amount — the
VaR number itself.

**Stella:** Sentence form?

**Horace:** "Our 1-day 99% VaR is five million dollars." That means
on 99 days out of every 100 we expect to lose less than five
million in a single trading day. On the hundredth day, the loss may
be larger — and VaR has nothing to say about *how much* larger.
That last clause matters more than anything else we will cover
today.

**[2:30 — Section 2: Method 1, parametric]**

**Stella:** Method one. Parametric.

**Horace:** Assume returns are Normal — the bell curve from your
statistics class. Mean μ, standard deviation σ. Then the VaR is just
$z_\alpha$ times σ minus μ, times your portfolio value. Z values:
1.645 at 95%, 2.326 at 99%, 3.090 at 99.9%. You can do this in
Excel.

**Stella:** Strength?

**Horace:** Lightning fast. Variance adds, correlations are linear,
you can do a thousand-position portfolio in a spreadsheet.

**Stella:** Weakness?

**Horace:** The Normal assumption is *wrong*. October 19th 1987 the
S&P fell 20.5% in a day. Under the parametric model that is a 19
sigma event. Probability $10^{-79}$. It should not happen between
now and the heat death of the universe. It happened. On a Monday.

**Stella:** So at 95% it is fine, at 99% it lies, at 99.9% it is
science fiction.

**Horace:** Exactly the marshmallow.

**[4:00 — Section 3: Method 2, historical]**

**Horace:** Method two. Historical simulation. Drop the Normal
assumption. Just take the last thousand days of your portfolio's
P&L, sort them, and read off the percentiles. The 10th worst day
in a thousand is your 99% VaR. No model. Just the data.

**Stella:** Strength?

**Horace:** Free fat tails. If 2008 is in your window, your VaR
includes 2008. If COVID is in your window, your VaR includes
COVID. The math does not have to *guess* about the tail; it
*remembers* it.

**Stella:** Weakness?

**Horace:** You only see what you have seen. If your window ends in
October 2007, you have no 2008 in your data, and your 99% VaR
reads like a 95% VaR the moment Lehman fails. This is exactly what
happened to many bank desks in autumn 2008 — their VaR was
calibrated on the placid 2003-2007 sample, so the breach was
"impossible" right up until it wasn't.

**[VISUAL: image/week42_var_methods.png]**

**Stella:** Show the three-panel chart.

**Horace:** Left panel: histogram of daily S&P returns from 1990 to
April 2026. The blue bars are the empirical distribution; the gold
curve is a Normal with the same mean and standard deviation. Look
at the shoulders. The Normal curve cannot reach where the data
actually is. The empirical histogram has thicker shoulders below
-2% and a long left tail running out to -10% and beyond. The Normal
curve is essentially zero out there.

**Stella:** Middle panel?

**Horace:** Annual returns, Damodaran 1928 to 2024. With vertical
markers at the 95%, 99%, and 99.9% empirical VaR levels. Notice
that the parametric Normal-fit VaR sits well to the *right* of the
historical 99% threshold — meaning the parametric estimate is
*less conservative* than the data warrants.

**Stella:** Right panel?

**Horace:** The empirical CVaR over VaR ratio at three confidence
levels. CVaR at 95% is about 1.20× VaR. At 99% it is 1.35× VaR. At
99.5% it is 1.45× VaR. The deeper into the tail you go, the worse
the *breach* — not just the threshold, the average size of the
loss when the threshold is exceeded. That is the headline image.

**[7:00 — Section 4: Method 3, Monte Carlo]**

**Horace:** Method three. Monte Carlo. You write down a model. You
simulate ten thousand or a hundred thousand portfolio paths. You
compute P&L on each. You sort. You read the percentile.

**Stella:** What do you put in the model?

**Horace:** Anything you can write down. Could be Normal — in which
case Monte Carlo agrees with parametric, plus sampling noise. Could
be Student-t with five degrees of freedom — heavy tails, much
closer to the data. Could be GARCH — vol today depends on vol
yesterday. Could be jump-diffusion — Normal noise plus occasional
Poisson jumps for the crash days. Could be regime-switching
Gaussian mixtures.

**Stella:** Strength?

**Horace:** Total flexibility. Captures non-linear payoffs — options,
structured products. Captures path-dependence — barriers, callable
bonds. You can build whatever world you want.

**Stella:** Weakness?

**Horace:** You build whatever world you want. Garbage in, garbage
out. If your model is wrong in the tail, your Monte Carlo VaR is
wrong in the tail — with the *illusion of precision*. A hundred
thousand paths from a wrong model give you a confidently wrong
answer.

**[9:00 — Section 5: CVaR / Expected Shortfall]**

**Horace:** Now the better number. CVaR. Conditional Value at Risk.
Also known as Expected Shortfall.

**Stella:** Definition?

**Horace:** *Given that the loss has exceeded the VaR threshold,
what is the average loss?* You compute VaR, then average all the
outcomes that breach VaR. That is CVaR.

**Stella:** Why is it better?

**Horace:** Two reasons. One, it answers the question VaR ducks —
how bad is the breach. Two, it has a property called *coherence*.
VaR can fail sub-additivity in heavy-tailed distributions —
combining two portfolios can give you a VaR larger than the sum.
That is mathematically pathological and it incentivises hidden
tail-risk concentration. CVaR does not have this problem.

**Stella:** Did regulators move to it?

**Horace:** Yes. Basel III replaced VaR with Expected Shortfall at
97.5% in the 2016 Fundamental Review of the Trading Book. The big
banks have been on CVaR for years. Retail platforms still mostly
quote VaR — fine for a baseline, but ask for CVaR if your platform
shows it.

**[11:00 — Section 6: The fat-tail problem]**

**Horace:** Show the kurtosis chart.

**[VISUAL: image/week42_kurtosis_history.png]**

**Stella:** This is rolling 5-year kurtosis of daily S&P 500 returns
since 1990.

**Horace:** Notice the dashed horizontal line at three. That is what
kurtosis equals if returns are truly Normal. Notice that the
empirical line is *above three* — every single day of the sample.
For thirty-six years it has never touched the Normal value. Mostly
it lives between seven and twelve. The 1987-window prints above
thirty. The 2008-window around twelve. Even quiet windows like
2003-2007 are above five.

**Stella:** And the implication?

**Horace:** Parametric VaR underestimates real losses. By 5-15% at
95%, by 30-100% at 99%, and by *2 to 5 times* at 99.9%. Every
single bank that relied on parametric VaR in the last forty years
has discovered this in tears. LTCM 1998. The structured-credit
desks 2008. The vol-target funds in March 2020. The model said it
could not happen. The world said it just had.

**[13:00 — Section 7: Practical framework]**

**Horace:** What do you actually do.

**Stella:** Walk us through.

**Horace:** Five steps. One: run all three methods. Parametric,
historical, Monte Carlo with Student-t. Look at the spread.
Two: quote CVaR at 97.5%, not VaR at 99%. Same regulatory
conservatism, more honest math. Three: always run an explicit
stress test. 1987, 2008, March 2020, 2022. These are not VaR
events; they are *plan-for-them* events. Four: size positions for
the tail, not the average. Barbell — most of the
book in instruments sized for normal vol, a small high-conviction
sleeve in defined-risk structures. Five: discount the headline
number. Whatever 99% VaR your platform reports, *double it for
sleep purposes*. The cost of being too conservative is a few basis
points. The cost of being too aggressive is the obituary section.

**[14:30 — Section 8: Interactive lab]**

**Stella:** Interactive walkthrough.

**Horace:** This week's lab is a VaR calculator. Three sliders:
portfolio value from ten thousand to ten million. Volatility
assumption from 5% to 40% annualised. Confidence level — 90, 95,
99, 99.5, 99.9. And a method toggle: Normal, Student-t with a
degrees-of-freedom slider, or Historical resampled from the last
five years of S&P data.

**Stella:** What do we read off?

**Horace:** Five outputs. 1-day VaR, 1-day CVaR, 1-month VaR (square-
root scaled), and a comparison bar showing all three methods side
by side at the chosen confidence. Plus a histogram of the chosen
return distribution with the tail shaded.

**Stella:** Things to do.

**Horace:** Start at 99%. Compare Normal versus Student-t with
df=5. Watch the VaR jump 30-50% just by switching the
distribution. Now move to 99.9%. The gap between Normal and
Student-t blows out to 2× or more. *That gap is the LTCM trade.*
Then run the historical method and compare again. The historical
number will sit between Normal and Student-t depending on what
your 5-year window contains. Now drop confidence back to 95%. The
three methods nearly converge. That is the point: parametric
*works* in the body, *fails* in the tail.

**[16:30 — OUTRO]**

**Stella:** Wrap.

**Horace:** Three takeaways. One. VaR is a *threshold*. CVaR is the
*average breach*. Always quote CVaR when you can. Two. All three
methods break in the tail — kurtosis is 7 to 15 in real equity
data, never 3, and the deeper you go the more the methods
disagree. Three. The right risk system runs all three plus an
explicit stress test, and treats the spread as the irreducible
uncertainty in the number. Vol-tail-wags-dog. The model is not the
world. The world will, eventually, surprise the model. Plan for it
before it does.

**Stella:** And the deeper objection?

**Horace:** In my own book, VaR is institutional theatre. It exists
because risk committees need a single number for the slide, and it
under-reports exactly the regimes where you need a risk number —
the vol-on expansions, the days when the option tail wagging the
equity dog produces "impossible" moves. The retail fix isn't a
better model; it's a better portfolio shape. Run a barbell with a
small persistent tail-hedge sleeve sized so the worst case on the
hedged book is the *known* premium you paid for the hedge — not a
number a Student-t tells you after the fact. Choose a shape whose
worst case is bounded by construction, and let VaR be a sanity
check rather than the load-bearing input.

**Stella:** Next week — Week 43, hedging strategies. How to actually
buy insurance against the tail without paying full retail.

**Horace:** Don't blow up.

**[END]**
