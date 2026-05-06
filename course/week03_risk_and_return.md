# Week 3: Risk and Return — The Two Forces, Honestly Measured

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Last week we landed on a simple prescription: index ETF, automatic
monthly transfer, close the app. It works. It also obscures the
machinery underneath, and the machinery is what stops you panic-selling
the next time the market hands you a 40% drawdown and a dinner-party
guest tells you "this time it's different."

Risk and return are the two forces that drive every investment outcome.
Most beginners spend all their attention on return — *"how much can I
make?"* The professional question is the inverse: *"how much can I
lose, how often, and is that loss survivable?"* If your answer to the
second question is "I don't know," you are not investing. You are
gambling with extra steps.

This lesson is the foundation for everything that follows. We will
look at what risk actually is (and the three things people confuse
with it), how to measure it without lying to ourselves, why higher
expected return *requires* higher risk, why the same risk number
behaves entirely differently over different horizons, and how the
distinction between risk *capacity* and risk *tolerance* is the one
that gets retirees blown up.

The honest disclaimer up front: **standard textbook treatments of risk
assume return distributions look like a bell curve, and they don't.**
Markets have fat tails — extreme events happen far more often than the
math says they should. We will spend the second half of this lesson on
why "5σ event" is a phrase to laugh at, not to plan around.

---

### 2. What You Need to Know

#### 2.1 Risk Is Uncertainty of Outcomes — Not Just "Bad"

In everyday English, risk means *the chance something bad happens*.
In finance, risk has a more precise meaning: **risk is the uncertainty
of the outcome**. A risky asset is not necessarily one that will lose
you money. It is one whose future return you cannot predict.

A three-month US Treasury bill yielding 4.3% is considered nearly
risk-free not because the yield is high — it isn't — but because the
range of plausible outcomes one quarter from now is essentially
"4.3%, plus or minus a fraction of a percent." A single biotech stock
is risky because the range one year from now might run from "−90%
because the trial failed" to "+400% because the trial succeeded." The
T-bill has *low uncertainty*. The biotech has *enormous uncertainty*
in both directions.

Three things people confuse with risk that aren't:

1. **Volatility**. Volatility is one *measure* of risk — the most
   commonly used — but volatility ≠ risk. A position can be quiet for
   five years and then blow up in a month (think Long-Term Capital
   Management, 1998). A position can be loud every day and be
   structurally bounded (think a deeply hedged options book).
   *Realised price wiggles* and *risk* are not the same thing.
2. **Probability of loss**. A coin flip with payouts of −$1 / +$1 has
   a 50% probability of loss. A coin flip with payouts of −$1 / +$100
   has the same 50% probability of loss but is wildly different in
   risk-adjusted terms. The probability of loss alone tells you
   nothing about the *size* of the loss when it comes.
3. **The headline number on the news**. "Markets are crashing" is not
   a quantification of anything. Crashes are a feature of equity
   markets — they happen roughly once per decade, sometimes twice —
   and an investor who treats every crash as an emergency is going to
   spend their life selling the bottom.

> *"Risk comes from not knowing what you're doing."* — Warren Buffett

#### 2.2 Standard Deviation — The Workhorse Measure

The most common measure of risk is the **standard deviation** of
returns, often called **volatility** or "**vol**." It tells you how
widely an asset's actual returns have varied around its mean.

For an asset with average annual return $\mu$ and standard deviation
$\sigma$, *if* returns were normally distributed (a big if; see §2.6):

- About **68%** of years would fall in $[\mu - \sigma,\ \mu + \sigma]$.
- About **95%** of years would fall in $[\mu - 2\sigma,\ \mu + 2\sigma]$.
- About **99.7%** of years would fall in $[\mu - 3\sigma,\ \mu + 3\sigma]$.

Run that on the actual S&P 500 dataset since 1928 and what you get is
this:

![Histogram of S&P 500 annual total returns, 1928 through 2024 (Damodaran annual dataset). The empirical mean is roughly 11.5% and the standard deviation is roughly 19.5%. A normal distribution with the same mean and standard deviation is overlaid as a smooth curve. The histogram has visibly fatter tails than the normal curve — both the worst years (1931, 1937, 2008) and the best (1933, 1954, 1958) are far further from the centre than a normal distribution predicts.](image/week03_return_distribution.png)

Three things to read off this chart:

- **The centre is roughly 11% per year.** That is the long-run nominal
  S&P 500 total-return average. The "real" number, after inflation, is
  closer to 7% — and the textbook's smooth 8% promise has the same
  status as Santa Claus.
- **The standard deviation is roughly 20%.** Sixty-eight percent of
  years fall between −9% and +30%. Plan for the *range*, not the
  average.
- **The distribution is wider than a normal curve in both tails.**
  −44% in 1931, −37% in 2008, +54% in 1933, +52% in 1954. None of
  these should be possible under the bell-curve model. They happened.
  The market has *fat tails*.

The headline rule of thumb for asset-class volatility:

| Asset class | Historical annual σ |
|---|---:|
| US Treasury bills | ~1% |
| Investment-grade bonds | ~6% |
| US large-cap stocks | ~16–20% |
| US small-cap stocks | ~22–28% |
| Emerging market stocks | ~24–30% |
| Single individual stock | ~30%+ |
| Bitcoin | ~70%+ |

Read the table from the bottom up. Bitcoin is roughly four times as
volatile as the S&P 500 — meaning whatever drawdown a bell-curve model
says is "extreme" for the index, you should expect roughly four times
that for BTC. That is a lot more risk than the headline-friendly "BTC
is up 200% this year" suggests.

#### 2.3 Equity Risk Premium — The Compensation for Bearing Risk

The **risk premium** is the extra return you earn above the risk-free
rate for accepting uncertainty. The most-cited number in all of
finance is the **equity risk premium (ERP)**: how much more, on
average, US stocks return above US Treasury bills.

Long-run, post-1928, that number has been roughly **5–7% per year**.
At a long-run T-bill mean of ~3.4% and a long-run S&P 500 mean of
~11%, the gap is around 7–8 points of nominal return — a gap that
compounded over a century turns $1 of T-bills into ~$23 and $1 of
stocks into ~$11,000 (in nominal dollars; the real numbers are
smaller but the *ratio* is essentially preserved).

Why must the ERP exist? Two equilibrium arguments:

1. **Investors are loss-averse.** Given two assets with the same
   expected return, almost everyone prefers the less volatile one.
   For investors to *willingly* hold the volatile one, the price has
   to fall until the *forward* expected return is high enough to
   compensate. That gap is the risk premium.
2. **Without it, the asset can't clear.** If stocks and T-bills
   offered the same expected return, no rational investor would hold
   stocks; everyone would sell into bonds, prices on stocks would
   fall, and forward returns would rise — until the gap re-opens.
   Risk premium is not a moral payment for "being brave"; it is the
   mechanical equilibrium price of clearing the volatile asset.

Two cautions, both important:

- **The premium is an *average over very long horizons*.** In any
  single year, stocks routinely *under*-perform T-bills. The ERP is
  the compensation for sticking with stocks *through* the years where
  T-bills win.
- **The premium can compress.** When stocks have already run up a long
  way, *forward* expected returns are lower; the premium implied by
  current prices may be much smaller than the historical average. Bob
  Shiller's CAPE ratio is one common attempt to put a number on this.
  In 2026, with CAPE around the high 30s, the implied forward ERP is
  closer to 3–4% than to 7%. That is not a prediction the next
  decade *will* be poor — it is a warning that the historical average
  is a different statistic from the current expected value.

#### 2.4 Systematic vs. Unsystematic Risk

This distinction is the single most important conceptual move in risk
management. It determines which risks the market pays you to bear and
which risks you are bearing for free.

- **Unsystematic (idiosyncratic) risk.** Specific to one company, one
  industry, or one position. Examples: a CEO scandal, a product recall,
  a fire at a single factory, a regulatory action against one firm,
  a mining accident. **Diversification eliminates this risk.** Hold
  500 names instead of 5, and a CEO scandal at any one of them moves
  your portfolio by a fraction of a percent rather than 20%.
- **Systematic (market) risk.** Affects the whole economy or whole
  market: recession, rate moves, inflation, war, pandemic. **You
  cannot diversify this away.** Even a perfectly diversified equity
  portfolio loses 35–55% in a 1929, a 1973–74, a 2008, or a 2020.
  Systematic risk is what the market *pays* you to bear via the equity
  risk premium.

The "free lunch" insight that won Markowitz the Nobel Prize: **since
unsystematic risk can be eliminated for free through diversification,
the market does not pay you to bear it.** Holding a concentrated
five-stock portfolio gives you much higher total risk than holding the
S&P 500, but the *expected return* is essentially the same as the index
(~10% nominal in long-run averages, by definition). The extra
volatility is uncompensated. You are taking risk *for free*.

This is the entire argument for index funds rendered as a single
sentence: an index fund holds enough names that idiosyncratic risk is
essentially zero, leaving you with only the systematic risk that the
market actually pays you for. Concentrated stock-picking, *unless you
have a real edge*, is voluntarily eating risk you don't get paid for.

#### 2.5 Drawdowns — The Risk That Actually Tests You

Standard deviation is a textbook measure. **Maximum drawdown** —
the peak-to-trough decline of an equity curve — is the measure your
nervous system is going to use, whether you like it or not.

Below is the actual S&P 500 drawdown chart from 1950 onward. The
shaded peaks are the major bear markets. The number that matters in
each case is not the size of the drawdown so much as the *time it
took to recover* and the temperament that survival required.

![S&P 500 total-return drawdown chart, monthly, 1985–2026 (Yahoo Finance ^GSPC). Each shaded region is a peak-to-recovery drawdown. The four largest visible in the modern data are 1987 Black Monday (-34%), 2000–2002 dot-com (-49%), 2007–2009 GFC (-55%), and the 2020 COVID crash (-34%). The 2022 selloff (-25%) and the post-2018 vol shock appear as smaller indentations. The 1973–74 oil-shock bear (-48%) predates this monthly series but lives in the recovery-time table below.](image/week03_drawdowns.png)

Recovery times (peak-to-new-high), by event:

| Event | Drawdown | Months to bottom | Total round-trip recovery |
|---|---:|---:|---:|
| 1973–74 (oil shock) | −48% | 21 | 7.5 years |
| 1987 Black Monday | −34% | 3 | 2 years |
| 2000–02 dot-com | −49% | 30 | 7 years |
| 2007–09 GFC | −55% | 17 | 5.5 years |
| 2020 COVID | −34% | 1 | 5 months |
| 2022 selloff | −25% | 10 | 2 years |

Two observations from this table that the standard-deviation number
does not capture:

- **The drawdowns are deeply asymmetric to the up-years.** A single
  −48% year requires +92% just to break even. A bell-curve model that
  averages your good and bad years symmetrically misses this entirely.
- **Recovery time matters as much as drawdown depth.** The 2020 COVID
  crash was the same size as the 1987 crash — but the 1987 took two
  years to recover; 2020 took five months. The Federal Reserve's
  active intervention is the mechanical reason. A retiree in
  decumulation through 1973–74 had to live for *seven and a half
  years* without their portfolio recovering, while still drawing
  income from it. That is a different problem from the same drawdown
  in 2020 with a 5-month bounce.

The behavioural lesson is simple. If your investment plan does not
survive a 50% drawdown — meaning, you would sell — your plan is
already broken. The plan must be *built around* the drawdown, not
*despite* it.

#### 2.6 Beta — The Slope, Not the Whole Picture

While standard deviation measures *total* risk, **beta** measures
*systematic* risk only — the portion of risk that moves with the
market.

A formal definition: beta is the slope of the regression of the
asset's returns against the market's returns.

$$ \beta_i = \frac{\text{Cov}(r_i, r_M)}{\text{Var}(r_M)} $$

Read the slope, not the formula:

| Beta | What it means |
|---|---|
| 1.0 | Moves with the market — index funds, by construction |
| 1.5 | Moves 50% more than market — typical tech / cyclical stock |
| 0.5 | Moves 50% less — utilities, consumer staples |
| 0.0 | Uncorrelated to market — short-term Treasury bills |
| < 0 | Moves *opposite* to market — gold sometimes, long volatility |

The **Capital Asset Pricing Model (CAPM)** uses beta to compute an
expected return:

$$ E[r_i] = r_f + \beta_i \cdot (E[r_M] - r_f) $$

In English: an asset's expected return equals the risk-free rate
plus the asset's beta times the equity risk premium. CAPM is on
every CFA exam and in every textbook. **It is also a description
that does not work very well in practice.** Real-world cross-sections
of expected return are explained better by other factors (size,
value, profitability, momentum) than by beta alone — a finding that
launched the entire factor-investing literature, which we cover in
Week 23. Treat CAPM as the orthodox starting point that every
finance professional understands; treat the factor models as the
empirical refinements.

#### 2.7 Time Horizon — Why "Risk" Means Something Different at 1y vs. 30y

One of the most-debated topics in finance is whether stocks become
*less risky* over longer holding periods. The data has a nuanced
answer.

Run the historical S&P 500 dataset and compute the *worst* and *best*
annualised return over rolling holding periods of 1, 5, 10, 20, and
30 years. The picture is striking.

![Range of annualised real returns for rolling holding periods on the S&P 500, 1928–2024 (Damodaran annual data, total return less CPI). Each line/band shows the worst (red), best (green), and 10th–90th-percentile range (blue band) for that holding length. The 1-year window runs from -38% to +53% — a 91-point range. The 30-year window runs from +4% to +10%. Time does not eliminate risk, but it dramatically shrinks the *range* of plausible annualised outcomes.](image/week03_holding_periods.png)

Two true things that look contradictory:

- **The range of rolling returns narrows dramatically with horizon.**
  At 1 year, anything from −38% to +52% is on the historical menu. At
  30 years, the menu collapses to roughly +3% to +10% annualised. By
  the time you are 30 years out, "stocks have always made money" is
  a defensible statement about the past.
- **The *cumulative* dollar consequence of a bad sequence still
  compounds.** A 30-year period that annualises to "only" +3% real
  ends up *materially* poorer than one that annualises to +9% real.
  Time narrows the *rate*, not the *spread of cumulative wealth*.

The practical implication: **horizon expands what risk you can
afford to bear.** A 25-year-old with a stable income and a 40-year
investment horizon can run a much higher equity weight than a
65-year-old with a portfolio that has to fund the next 25 years of
groceries. The 25-year-old has time to wait out a 50% drawdown; the
65-year-old does not.

That is the sequence-of-returns risk that the next paragraph
captures. A retiree who experiences a 1973–74 in the *first* two
years of retirement is permanently impaired — every dollar withdrawn
during the drawdown removes shares that don't get to compound back.
A retiree who experiences the same drawdown 15 years into retirement
is barely affected. **Same drawdown. Same return distribution.
Different sequence. Different outcome.**

#### 2.8 Risk Capacity vs. Risk Tolerance — The Mismatch That Kills

One last distinction. It is the one most often missed, and it is the
one that actually blows up retail portfolios.

**Risk capacity** — how much risk you can *afford* to bear, based on
objective conditions:

- Time horizon
- Stability of income
- Net worth relative to lifestyle costs
- Insurance and other buffers
- Whether the portfolio funds your living expenses

**Risk tolerance** — how much risk you are *psychologically*
comfortable bearing:

- How you actually react when you see your account down 30%
- Whether you can sleep through a bear market
- Whether bad portfolio days affect your relationships, your sleep,
  your work

The mismatch quadrant is the dangerous one:

| | High capacity | Low capacity |
|---|---|---|
| **High tolerance** | *Match.* Take appropriate risk, sleep fine. | **Danger zone.** "I can handle volatility" + portfolio funds your rent = one bad year wipes you out. |
| **Low tolerance** | Education problem — you have the time horizon, but emotion drives you out at the bottom. | *Match.* Conservative positioning is the right answer. |

The two failure modes:

- **High tolerance, low capacity.** The 67-year-old retiree who
  watched 2009–2024 melt up and decided he *believes in stocks*. He
  is now 100% equities, two years into a drawdown, drawing 4% a year
  to live on. The 30% drawdown forces him to sell shares at the
  bottom to fund living expenses; those shares never recover for him.
  Three more bad years and the portfolio is permanently impaired.
  This is *the* most common way retired retail investors blow up —
  treating their tolerance as if it were also their capacity.
- **Low tolerance, high capacity.** The 28-year-old engineer with a
  20-year horizon and a healthy salary who keeps her savings in a
  high-yield savings account because "I don't trust the market." She
  has the capacity to ride a 50% drawdown — the income is coming in
  every two weeks regardless. What she lacks is the *experience* that
  lets her sit through one. The fix is not "be braver." The fix is
  graduated exposure: small allocation, watch a drawdown, see it
  recover, increase, repeat. Build the tolerance over time.

The single most useful question to ask yourself before sizing a
position: **"If this position dropped 50% next month, would I be a
forced seller?"** If the honest answer is yes, the position is too
large. Cut it until the answer is no, regardless of what your
"tolerance" tells you.

> *"The market can stay irrational longer than you can stay solvent."*
> — John Maynard Keynes (attributed)

---

### 3. Common Misconceptions

**Misconception 1: "Higher risk always means higher return."**

Higher risk means higher *expected* return *for the asset class as a
whole*, on long horizons. It does not mean higher return for any
individual position. A single biotech stock is extremely risky and
may return nothing if its trial fails. The risk premium applies to
diversified bearers of *systematic* risk; concentrated positions in
single names accept enormous *idiosyncratic* risk that the market
does not pay you to bear. Risk and expected return scale together
*at the asset-class level*, not at the single-position level.

**Misconception 2: "If I just hold long enough, stocks always go up."**

US stocks have always recovered eventually, but "eventually" can mean
seven to fifteen years. Japanese stocks peaked in 1989 and did not
surpass that level until 2024 — a 35-year wait. There is also a
**survivorship bias** problem: we study the US market because it
became the most successful equity market of the 20th century. China,
Russia, Argentina, Egypt all had thriving exchanges in 1900 and
delivered −100% real returns over the subsequent century. "Stocks for
the long run" is true on the *measured sample*. The sample is
US-conditional.

**Misconception 3: "Standard deviation captures all the risk."**

It captures *Gaussian* risk under the assumption that returns are
normally distributed. They are not. Markets have **fat tails** —
extreme moves happen far more often than the bell-curve model
predicts. The 2008 crash was, by Gaussian arithmetic, a roughly 5σ
event, which a normal distribution says should occur once every
~14,000 years. It happened. So did 1987 (a 22σ event under the
prevailing models). The standard deviation of the *body* of the
distribution does not predict the size or frequency of the *tails*.
This is why we will spend Week 47 on tail-risk hedging instead of
trusting the bell curve to size positions.

**Misconception 4: "Bonds are safe."**

Bonds are *less volatile* than stocks. They are not risk-free. Long
bonds lost roughly 30% of their value in 2022 alone — that is a
larger drawdown than the median equity bear market. Bond holders also
face inflation risk (a 4% bond in a 6% real-inflation environment
loses purchasing power even while paying a positive nominal yield)
and credit risk (the issuer defaults). The 1982–2020 bond bull market
trained an entire generation of investors and advisors to think of
"bonds" and "safety" as synonyms. They are not, and the regime that
made them feel synonymous has reversed.

**Misconception 5: "Low realised volatility means low risk."**

Sometimes. Sometimes not. Bernie Madoff's fund showed implausibly
low volatility and steady returns from 1992 onward — *because the
returns were fabricated*. Long-Term Capital Management's strategy
ran with extremely low realised volatility for years before blowing
up over a single quarter in 1998 and requiring a Federal Reserve-
coordinated bailout. *Realised* volatility is one observation
window; *risk* is the full distribution of possible outcomes,
including the ones that haven't happened yet. Low vol can be a
trap — the calm before the regime break.

**Misconception 6: "Risk tolerance is a fixed personality trait."**

It moves with experience, with portfolio size, and with life stage.
A 25-year-old who has never seen a bear market often discovers, in
their first one, that the tolerance they self-reported on their
brokerage's questionnaire was theoretical. The same person ten years
later, having watched two drawdowns recover, sleeps through a third
without thinking about it. Tolerance is built, not declared.

**Misconception 7: "Diversification means owning lots of different
funds."**

Diversification is about owning *uncorrelated exposures*. Owning ten
US large-cap funds run by ten different managers gives you almost
nothing — they all hold roughly the same names with the same betas
and they all fall together. Owning a US equity fund, a long Treasury
fund, gold, and a long-volatility hedge gives you *real*
diversification because the assets respond differently to the same
macro shocks. Number-of-funds is a vanity metric. Number-of-distinct-
risk-factors is the real one.

---

### 4. Q&A

**Q1: If I can never get rid of systematic risk, why bother
diversifying within equities?**

A: To eliminate the *unsystematic* risk you are not paid to bear.
Holding 500 names instead of 5 reduces idiosyncratic risk to nearly
zero, leaving the systematic risk that the equity premium is
compensation *for*. The five-stock portfolio has more *total* risk
but the same expected return as the index — the extra risk is the
free lunch you are eating in reverse.

**Q2: Bitcoin's volatility is 70%+. Does the same risk-premium logic
apply?**

A: In principle yes — bitcoin's expected return must be high enough
to clear at its volatility. In practice, bitcoin's expected return
is *not knowable* from price history alone because the asset is too
young and its monetary regime is still being negotiated. Standard
risk-premium math uses 100 years of data to triangulate the equity
premium; for bitcoin you have 15 years, of which the first 8 were
near-zero adoption and the last 7 are the entire price history. Apply
the framework, but don't pretend the standard error on the estimate
is small.

**Q3: How do I estimate my own risk tolerance honestly?**

A: Two steps, in order. First, take an honest *capacity* assessment:
horizon, income stability, dependence of living expenses on the
portfolio. Second, take a small allocation to a volatile asset and
*see how you actually feel* during a drawdown. Self-reported risk
tolerance from a brokerage questionnaire correlates poorly with
behaviour in a real bear market. Tolerance is observed, not
declared.

**Q4: Why is 60/40 the conventional portfolio if bonds aren't a
reliable inflation hedge anymore?**

A: 60/40 was built around a specific 40-year window (1982–2020) in
which (a) bonds yielded above inflation and (b) bonds rallied when
stocks fell. Both broke in 2022, when stocks and bonds fell roughly
20% together. The conventional 60/40 is a *legacy* allocation
matching a legacy regime. Modern equivalents replace some or all of
the bond sleeve with cash, gold, and long-volatility hedges (Week 47,
Level 5).

**Q5: What is the most useful single risk number for a retail
investor?**

A: **Maximum drawdown** of the strategy you are running, sized to
*your* portfolio. Multiply your portfolio value by 0.5 (a plausible
once-per-decade equity drawdown), and ask whether the dollar amount
that you would see in red on the screen would force you into bad
decisions. If yes, you are over-allocated to risk. If no, you can
proceed.

**Q6: Why does the textbook keep using the standard deviation if it's
not great?**

A: Because it has nice mathematical properties (additive under linear
combinations, easy to estimate from data, well-behaved in models),
not because it captures the risk that matters. The standard deviation
is a useful *summary* of the central body of the distribution. It is
inadequate as a descriptor of the *tails*, which is exactly where the
losses you remember actually live. The honest professional uses
standard deviation *plus* drawdown *plus* tail-event analysis — never
any one alone.

**Q7: Is volatility a good or bad thing for an investor?**

A: For a *buyer* who is dollar-cost averaging in over years, mild
volatility is mildly good (you buy at a discount during dips). For a
*holder* who is sitting on accumulated wealth, volatility is mostly
the cost of doing business — not "bad" in expectation, but the
emotional load you carry. For a *seller* in decumulation,
volatility is genuinely costly because of sequence-of-returns risk.
The same number means different things at different life stages.

**Q8: What does "fat tails" actually mean for sizing my positions?**

A: Whatever drawdown a normal-distribution model says is "extreme" —
size as if a drawdown twice that depth is genuinely possible. The
2008 GFC was a 5σ event under the prevailing risk models; planning
to survive a 5σ event of the right magnitude (so, ~50% on US large
cap rather than ~25% the model predicted) is what kept investors in
the game. The shorthand: *plan for half-off, every decade, no
warning.*

**Q9: How does a "barbell" shape relate to standard
deviation?**

A: The barbell *exploits* the fat-tailed distribution. By holding
high-conviction safety on one end (short-Treasuries, gold, cash) and
asymmetric speculation with capped downside on the other (long calls,
long-vol structures), the resulting portfolio has a *higher*
arithmetic standard deviation than a passively-diversified core but
a *better* drawdown profile and a *better* response to tail events.
The standard deviation alone makes it look "riskier"; the drawdown
distribution shows it actually isn't. This is a Week 14 / Level 5
topic but the framing matters for how you read this lesson.

**Q10: How does this lesson connect to the rest of the course?**

A: Risk and return are the foundation under everything that follows.
Week 4 (60/40) and Week 7 (rebalancing) are exercises in shaping the
risk profile of a multi-asset portfolio. Week 13 onwards (long/short,
pair trading) are about removing systematic risk and isolating
specific bets. Weeks 25–30 (options) are the toolkit for *expressing*
risk asymmetrically. Week 47 (tail risk) is the explicit treatment of
the fat-tail problem this lesson opened. Every subsequent strategy
will be evaluated on its risk profile — not just its return.

The interactive demo on the website extends this lesson with a
**holding-period explorer**: a slider lets you choose any rolling
window from 1 to 30 years, and the chart shows the historical
distribution of annualised real returns for that window — best,
worst, median, and the odds of ending up below zero. The shape of
the distribution at 1 year and 20 years is essentially the §2.7
chart, but you can slide between them and watch the tails close.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Risk and Return — The Two Forces (and the Five-Sigma Lie) | Week 3

**RUNTIME TARGET:** ~22 minutes

**HOSTS:**
- **Horace** (teacher)
- **Stella** (student)

---

**[INTRO]**

[VISUAL: title card "Week 3 — Risk and Return"]

**Horace:** Two weeks in, we've established two things: inflation is
gravity, so you have to invest. And the right default for almost
everyone is a low-cost index ETF. Today is the lesson where I tell
you what it actually feels like to *hold* that ETF — because the
machinery underneath is the part that decides whether you sell at the
bottom or stay invested.

**Stella:** And the machinery is risk and return.

**Horace:** Two forces. They are inseparable. And almost every
mistake in retail investing comes from focusing on the first and
ignoring the second.

---

**[SEGMENT 1: WHAT RISK ACTUALLY IS]**

**Horace:** Forget the dictionary definition for a moment. In finance,
risk is *uncertainty of outcome*. A T-bill yielding 4.3% — you know
almost exactly what you'll have in three months. A biotech stock —
you might be up 400% or down 90%. The biotech is risky not because
it's *bad*; it's risky because the future is *unknowable*.

**Stella:** So volatility is risk?

**Horace:** Volatility is a *measure* of risk. It is not risk itself.
A position can be quiet for years and then blow up in a month. The
realised price wiggles you see on a chart and the actual probability
distribution of future outcomes are not the same thing.

[ANIMATION: animation/week03_definitions.mp4 — three panels: T-bill
range very tight, S&P 500 range medium-wide, single biotech range
extremely wide.]

---

**[SEGMENT 2: THE BELL CURVE THAT ISN'T]**

[VISUAL: cut to the historical-distribution image —
image/week03_return_distribution.png]

**Horace:** Here are the actual annual returns of the S&P 500 from
1928 through last year. The smooth curve overlaid is what a normal
distribution with the same mean and standard deviation says the
returns *should* look like.

**Stella:** The actual data has fatter tails than the curve.

**Horace:** Materially fatter. Look at 1931. Look at 2008. Look at
1933 on the upside. None of those should be possible under a
bell-curve model. They happened. The standard textbook treatment of
risk uses the bell curve. The honest treatment notes that markets
have what we call *fat tails*, and that whatever the model says is a
"5-sigma event" — which a normal curve says happens once every
fourteen thousand years — happens roughly every decade in real
markets.

**Stella:** So when someone on TV says "this was a 5-sigma move" —

**Horace:** They are admitting their model is wrong. That phrase
should make you laugh, not nod.

---

**[SEGMENT 3: THE EQUITY RISK PREMIUM]**

**Horace:** Now the second force. Why do stocks return more than
T-bills? Because investors are loss-averse. If stocks paid the same
expected return as bonds, no rational investor would hold the
volatile asset. So the price of stocks falls until the *forward*
expected return is high enough to compensate for the volatility. That
gap is the equity risk premium. Historically about five to seven
points per year.

**Stella:** "Historically" doing a lot of work in that sentence.

**Horace:** It is. The forward premium implied by *current* prices is
much smaller than the long-run average right now. Shiller's CAPE
ratio is in the high 30s. At those valuations the forward expected
return is around 3–4 percent real, not 7. Doesn't mean the next
decade will be bad — but it means the historical average is a
different statistic from the current expected value.

---

**[SEGMENT 4: SYSTEMATIC VS UNSYSTEMATIC]**

[VISUAL: animation/week03_diversification.mp4 — five stocks → 50
stocks → 500 stocks; idiosyncratic noise melting away while a
floor of systematic vol remains.]

**Horace:** Two kinds of risk. *Unsystematic* is specific to one
company — a CEO scandal, a factory fire, a bad drug trial.
*Systematic* is what affects the whole market — recession, inflation,
war.

**Stella:** And one of them I can diversify away.

**Horace:** Unsystematic, yes. Hold 500 names instead of 5 and a CEO
scandal at any one of them moves the portfolio by half a percent.
Systematic — the 35% drawdown in 2008, the COVID bear, the dot-com
crash — you cannot diversify your way out of it. *And the market
only pays you for the systematic kind.*

**Stella:** So if I hold a five-stock portfolio…

**Horace:** You're taking unsystematic risk on top of systematic risk
and the market only pays you for the second. That is the entire
argument for index funds, in one sentence.

---

**[SEGMENT 5: DRAWDOWNS — THE NUMBER YOUR NERVOUS SYSTEM USES]**

[VISUAL: cut to image/week03_drawdowns.png and walk through the four
big bear markets.]

**Horace:** Standard deviation is what the textbook uses. *Drawdown*
— peak to trough — is what your nervous system uses. Look at this
chart. Four major bear markets. 1973–74, dot-com, GFC, COVID.

**Stella:** The COVID one looks tiny compared to the others on the
time axis.

**Horace:** Same magnitude — about 34% — but the recovery was five
months instead of seven and a half years. Federal Reserve
intervention is the mechanical reason. The same drawdown felt
completely different depending on which decade you happened to live
through.

**Stella:** And if I had been a retiree in 1973?

**Horace:** You would have lived through seven and a half years
without your portfolio recovering, while drawing down on it to live.
That is sequence-of-returns risk, and it's the reason "stocks for the
long run" sounds different at 25 than it does at 65.

---

**[SEGMENT 6: HORIZON COLLAPSES THE RANGE]**

[VISUAL: cut to image/week03_holding_periods.png]

**Horace:** Now the good news. Look at the rolling-return chart. At
one year, US stocks have returned anywhere from minus 38 to plus 52
percent. At thirty years, the worst is about plus 3 real, the best
about plus 10.

**Stella:** Time crushes the range.

**Horace:** Of the *annualised rate*. The cumulative dollar
consequence of a bad sequence still compounds — a thirty-year
sequence at plus 3 real is dramatically poorer than one at plus 9
real. But "stocks always make money over thirty years" is, on the US
sample, defensible. The footnote is *on the US sample*. Survivors
bias is real.

---

**[SEGMENT 7: CAPACITY VS TOLERANCE — WHERE PEOPLE BLOW UP]**

**Horace:** Last concept and it is the most important one. Two
different ideas that get mashed together.

*Risk capacity* — how much you can afford. Time horizon, income,
whether the portfolio funds your rent. Objective.

*Risk tolerance* — how you actually feel watching it drop. Subjective.

**Stella:** And the dangerous combination is high tolerance, low
capacity.

**Horace:** The 67-year-old retiree who watched the 2010s and
decided he believes in stocks, runs 100% equities, draws 4% a year
to live, then hits a 30% drawdown and is forced to sell shares at the
bottom to pay rent. The shares he sold never recover *for him*. That
person is the typical retail blow-up. He had the tolerance — what he
didn't have was the capacity to lose. The two were never the same
question.

**Stella:** And the fix?

**Horace:** Position size to your *capacity*, not to your *tolerance*.
The single best question to ask before sizing anything: *if this
position dropped 50% next month, would I be a forced seller?* If yes,
the position is too large. Cut until the answer is no. Regardless of
how brave you feel.

---

**[OUTRO]**

**Horace:** Next week we build the first multi-asset portfolio — the
classic 60/40. We'll see why it worked for forty years, why it broke
in 2022, and what people are doing to replace it. The risk and
return concepts from today are the lens we use to compare.

**Stella:** And the interactive on the website?

**Horace:** Holding-period explorer. Slider for the window, see the
distribution of annualised real returns. Watch the tails close as you
slide from 1 year to 30. Play with it before next week.

---

**END SCREEN:** "Next: Week 4 — The 60/40 Portfolio"
