## Part 2: YouTube Script

---

**VIDEO TITLE:** Quantitative Methods for Investors — How to Tell Real Alpha from a Lucky Backtest
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Horace:** Welcome back. This week's lesson is the one where, if I
do my job, you walk away able to call BS on roughly half the
"performance" pitches you'll ever see.

**Stella:** Strong claim, Horace.

**Horace:** It's a defensible one. Quantitative methods — regression,
time-series models, ML pipelines — are the language people use to
*claim* skill. If you can read the language at a passable level, you
can ask the three questions that pop the bubble: what's the holdout,
how was it picked, and what's the t-stat?

**Stella:** And if they can't answer those?

**Horace:** Then you've just saved yourself 1.5% per year for the
next decade.

**Stella:** Set the agenda.

**Horace:** Three pieces. First, regression as the
alpha-attribution machine — what alpha means after you regress on
the right factors. Second, time series — what AR/MA/ARMA can and
can't do. Third, the ML pitch — train/validation/test, walk-forward,
and why most ML alpha is actually feature engineering.

**Stella:** And the principles?

**Horace:** Information edge is the hardest of the structural alpha
lanes — it sits right on top of all of this. The companion idea —
alpha is rare — is what the math will keep proving.

---

**[PART 1 — REGRESSION — 1:30-7:00]**

**Stella:** Single-factor first.

**Horace:** Yep. The line is

$$R_p - R_f = \alpha + \beta \cdot (R_m - R_f) + \varepsilon.$$

Two numbers come out: the slope, beta, and the intercept, alpha.
Alpha is the average return your portfolio produced *after* you
subtract what its market exposure already explained.

[VISUAL: image/week45_regression_alpha.png]

**Stella:** Talk us through this picture.

**Horace:** Sixty months of made-up data calibrated to alpha 2% per
year, beta 0.85. You can see the slope is gentler than 1 — that's
the 0.85 — and the line crosses the y-axis at about 17 basis
points per month. Annualised, 17 bps × 12 ≈ 2%. The dots scatter
around the line; that scatter is epsilon, the residual. The t-stat
on the alpha tells you whether 17 bps per month is distinguishable
from zero.

**Stella:** Punchline?

**Horace:** Yes. With 60 months and that residual vol, the t-stat
on a 2% alpha is barely 2.0. To *prove* skill at that magnitude you
need closer to twenty-five years.

**Stella:** Twenty-five years.

**Horace:** Twenty-five years. Alpha is rare — that's the math, not a
slogan.

**Stella:** Now multi-factor.

**Horace:** Same machine, more right-hand-side terms.

$$R_p - R_f = \alpha + \beta_1 \text{MKT} + \beta_2 \text{SMB} + \beta_3 \text{HML} + \beta_4 \text{UMD} + \varepsilon.$$

You take a small-cap value fund whose one-factor alpha was 4% per
year, run the five-factor regression, and almost always — almost
always — most of that alpha was a positive loading on SMB and HML
times the realised premia we catalogued in Week 23. The residual
alpha collapses to near zero.

**Stella:** That's the SPIVA result in equation form.

**Horace:** Exactly. The chart is the SPIVA report's mathematical
backbone.

---

**[PART 2 — TIME SERIES — 7:00-11:00]**

**Stella:** Time series.

**Horace:** Three building blocks: AR, MA, ARMA. The AR(1) model
asks one question: does this period's return predict next period's?

$$r_t = \phi \cdot r_{t-1} + \epsilon_t.$$

If phi is positive, returns trend. If negative, they mean-revert.
For US monthly equity returns, phi is about +0.10 — not zero, but
not big. For *daily* returns it's slightly negative. For *6-12
month relative cross-sectional* returns, phi is positive — that's
the Jegadeesh-Titman momentum effect.

**Stella:** And volatility?

**Horace:** Volatility is *highly* persistent. Phi on daily VIX is
about 0.95. Today's volatility tells you almost everything about
tomorrow's. That's why GARCH models genuinely forecast variance.

**Stella:** You said something important last week — the vol tail
wags the return dog.

**Horace:** Vol-tail-wags-dog. Returns are basically unforecastable
month-to-month. Variance is highly forecastable. So a lot of what
looks like "alpha" in option-selling, vol-targeting, or risk-parity
strategies is actually exploiting *that* asymmetry.

**Stella:** Rolling versus expanding window?

**Horace:** Expanding window if the parameter is stable. Rolling if
it's drifting. Megacap beta is roughly stable since 1990 — use
expanding. The HML factor's market beta flipped sign around 2007 —
use rolling. There's no universal answer; there's a stability test.

---

**[PART 3 — THE ML PITCH — 11:00-15:30]**

**Stella:** Now the ML conversation.

**Horace:** Train, validation, test. Three separate slices. Train
fits the model. Validation tunes the hyperparameters. Test is used
*exactly once* to score the frozen model.

**Stella:** What goes wrong?

**Horace:** Two things. One, people iterate against the test set
until it becomes a second validation set. Two, people don't apply
multiple-testing corrections, so a strategy that looks impressive
in isolation is just the survivor of a hundred siblings that didn't.

[VISUAL: image/week45_overfit_curve.png]

**Stella:** This is the overfitting hump.

**Horace:** Classic shape. In-sample Sharpe rises monotonically
with model complexity — more parameters, deeper tree, more
features. Out-of-sample Sharpe rises briefly, peaks at some
moderate complexity, and then collapses. The gap between the two
curves is the overfitting tax.

**Stella:** And the multiple-testing correction?

**Horace:** Lopez de Prado's deflated Sharpe formalises it. The
short version: if you tried N variants, the Sharpe needed to clear
noise scales like the square root of two log N. Try a thousand
strategies, your bar is roughly 3.7 standard deviations of the
unconditional null — which on a five-year backtest is a Sharpe of
about 1.6 just to *justify having looked*. Most published anomalies
don't clear that bar.

**Stella:** Why is feature engineering so important?

**Horace:** Because financial data has a brutal signal-to-noise
ratio. The marginal value of model complexity is sharply
diminishing. Two shops with the same features and different ML
models converge to similar Sharpes. Two shops with the same model
and different feature sets diverge sharply. The features are where
the information sits.

**Stella:** And for the retail investor?

**Horace:** For us, the consequence is humbling. The serious money
in quant alpha is rarely made by yet another XGBoost on yet
another OHLCV dataset. It's made by sourcing features no one else
has — alternative data, satellites, credit-card panels. The
information lane of alpha is real but expensive. The
structural lanes — factor compression, liquidity, vol-tail
mispricing — remain the cheaper and more durable retail game.

---

**[PART 4 — THE LAB — 15:30-17:00]**

**Stella:** Show the lab.

**Horace:** Open `interactive/week45_regression_lab.html`. You
control four sliders: number of points, true alpha in basis points,
true beta, and noise volatility. The page generates synthetic data
inline using a deterministic LCG, runs ordinary least squares, and
draws the scatter plus the regression line plus a 95% confidence
band.

**Stella:** What should viewers play with first?

**Horace:** Set true alpha to 200 bps and noise vol to 4% — that's
the canonical "low-noise skilled manager" case. The estimated alpha
will land within about 30 bps of 200 with 60 points. Now drop
points to 24 — two years of data — and watch the confidence band
double in width. With 24 points you can't reject zero alpha at the
2 standard-error level.

**Stella:** And the deeper lesson?

**Horace:** The width of the alpha confidence band is the size of
your "I don't know." It's not a number to round to zero — it's the
honest measure of how much of your apparent alpha is the data
talking and how much is the noise. Most managers operate inside
that band their whole careers.

---

**[OUTRO — 17:00-18:00]**

**Stella:** What's next week?

**Horace:** Week 46 — we use this toolkit to dissect a real
hedge-fund track record. Take published returns, run the
five-factor regression, and we'll see what the residual alpha
actually is.

**Stella:** Practical homework?

**Horace:** Three things. One: pick a fund you own. Find five
years of monthly returns. Run a five-factor regression — Kenneth
French publishes the data free. Read the alpha and t-stat. Two:
go play with the lab — push noise vol up and watch the
confidence band swallow the alpha. Three: write down, in one
sentence, the difference between "I have alpha" and "I have
statistically-significant alpha." If you can't say it, the next
sales pitch will sound credible. After this week, it shouldn't.

**Stella:** Stay sceptical.

**Horace:** Stay sceptical. See you next week.

[END]
