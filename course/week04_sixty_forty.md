# Week 4: The 60/40 Portfolio — Why It Worked and Why 2022 Broke It

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Sixty percent stocks, forty percent bonds. The most famous asset
allocation in the history of investing, the default of every
financial advisor, the benchmark every balanced fund is measured
against, and — until 2022 — the closest thing to a "set it and
forget it" portfolio that the textbook profession would put in
print.

You need to understand 60/40 for four reasons, even if you end up
not running it.

1. **It is the baseline.** Every more complex strategy — risk parity,
   trend, factor tilts, the barbell shape we build in Level 5
   (Weeks 47–52) — is measured against 60/40. You cannot evaluate
   any of those if you don't know what they are improving on.
2. **It demonstrates what diversification actually buys you.** When
   stocks and bonds are negatively correlated, the 60/40 mix
   delivers roughly 80% of the equity return with about 60% of the
   equity risk. That is not arithmetic — that is a *correlation
   discount* on portfolio volatility, the central insight of
   Markowitz's Nobel-winning work.
3. **It demonstrates the limits of diversification.** In 2022, both
   stocks and bonds fell roughly 18% together, the worst year for
   60/40 since 1937. Understanding *why* matters more than the
   loss itself: the regime that made 60/40 work for forty years had
   a specific macro signature, and that signature reversed.
4. **It teaches you that correlation is the most important variable
   in portfolio construction.** Returns shift the level of your
   wealth. Correlations shift the *shape* of the distribution. The
   stock-bond correlation flipped sign in 2022, and the entire
   industry is still digesting what that means.

This lesson covers the origin and mechanics, the historical
performance by decade, the correlation history, the 2022 break, and
the modern adaptations.

---

### 2. What You Need to Know

#### 2.1 The Mechanics — Why Mix Stocks and Bonds at All?

The single insight: **the volatility of a portfolio is not the
weighted average of the volatilities of its parts.**

For two assets with weights $w_1, w_2$, standard deviations
$\sigma_1, \sigma_2$, and correlation $\rho$:

$$ \sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \sigma_1 \sigma_2 \rho} $$

When $\rho < 1$, that square root is *less* than the weighted-average
volatility. The closer to $\rho = -1$, the more risk reduction.
**Diversification is correlation arithmetic.**

A worked example before the table makes the point concrete. Take US
stocks at $\sigma = 16\%$ and US Treasuries at $\sigma = 6\%$, and a
60/40 mix. The naive guess — that 60/40 risk equals 60% of stock
risk plus 40% of bond risk — gives $0.6 \times 16\% + 0.4 \times 6\% =
12.0\%$. That is what you would get if the two assets moved in
lockstep. With a more realistic correlation of $\rho = -0.3$, the
formula gives:

$$ \sigma_p = \sqrt{0.6^2 \cdot 16^2 + 0.4^2 \cdot 6^2 + 2 \cdot 0.6 \cdot 0.4 \cdot 16 \cdot 6 \cdot (-0.3)} \approx \sqrt{88.1} \approx 9.4\% $$

That gap from 12.0% down to 9.4% — about a 22% reduction in
portfolio volatility for *no give-up in expected return* — is the
entire point of mixing the two assets. It is not a budget calculation;
it is the correlation discount Markowitz won the Nobel for.

For US stocks ($\sigma \approx 16\%$) and US Treasuries
($\sigma \approx 6\%$), with the long-run correlation between them:

| Stock-bond ρ | 60/40 σ | Diversification benefit |
|---|---:|---|
| +1.0 (perfectly correlated) | 12.0% | None — pure weighted average |
| 0.0 (uncorrelated) | 10.1% | About 16% volatility reduction |
| −0.3 (typical 1990s–2010s) | 9.4% | About 22% reduction |
| −1.0 (theoretical) | 7.2% | Maximum reduction |

The 1990s–2010s regime delivered an average stock-bond correlation
around −0.3. That is the entire reason 60/40 worked so well for so
long. It was *not* about either asset's expected return; it was
about the cross-correlation.

#### 2.2 Historical Performance — The Forty-Year Tailwind

The chart below plots the cumulative real wealth (after CPI) of 100%
stocks, 100% Treasuries, and 60/40 from 1928 forward, all rebalanced
annually.

![Cumulative real wealth of three portfolios from 1928 through 2024 (Damodaran annual data, $1 starting balance, log scale, real terms after CPI). The three lines: 100% S&P 500 (steepest, most volatile), 100% 10-year US Treasury (smoothest but lowest), 60/40 rebalanced annually (the middle path that captures most of equity's compounding with materially smaller drawdowns). The 60/40 line ends near the 100% stocks line in real wealth but with visibly shallower troughs at 1937, 1973-74, 2000-02, and 2008.](image/week04_sixty_forty_growth.png)

Read the chart from far right to far left. By 2024, $1 invested in
1928 in real terms became roughly:

- $565 at 100% stocks
- $128 at 60/40
- $4 at 100% bonds

The bonds-only line barely keeps up with inflation across the full
century — the long-run real return on Treasuries is about 1.4%
per year. Stocks compound at roughly 6.8% real. 60/40 lands at
roughly 5.1% real, three-quarters of the way to the equity line in
*compound-rate* terms but with materially smaller drawdowns
along the way.

By decade, the picture is more nuanced. The drawdown columns are
each asset's *within-decade* worst peak-to-trough loss in real terms
(annual data, so an event that bottoms in the next decade is
attributed there).

| Decade | 60/40 (real ann.) | Stocks (real ann.) | Bonds (real ann.) | 60/40 max DD | Stocks max DD | Bonds max DD |
|---|---:|---:|---:|---:|---:|---:|
| 1930s | 1.0% | -0.1% | 4.7% | -23% | -38% | -1% |
| 1940s | 1.6% | 3.6% | -3.5% | -23% | -25% | -32% |
| 1950s | 12.5% | 16.7% | -2.6% | -6% | -13% | -11% |
| 1960s | 3.5% | 5.0% | -0.7% | -12% | -14% | -17% |
| 1970s | -0.7% | -1.4% | -1.0% | -36% | -49% | -33% |
| 1980s | 9.7% | 12.0% | 7.2% | -8% | -13% | -9% |
| 1990s | 8.7% | 14.8% | 4.6% | -5% | -1% | -11% |
| 2000s | 1.8% | -3.4% | 4.4% | -15% | -37% | -13% |
| 2010s | 6.8% | 11.4% | 1.6% | -4% | -6% | -10% |
| 2020-24 | 1.6% | 6.7% | -3.5% | -23% | -23% | -34% |

The 1980s, 1990s, *and* 2000s are the three decades that built
60/40's reputation. The 1980s–90s contributed the return story:
real bond returns above 7% per year in the '80s, real stock returns
above 12% in the '90s. The 2000s contributed the *protection*
story: stocks lost 3.4% per year in real terms across the
dot-com bust and GFC, and the bond sleeve carried the 60/40 portfolio
to a positive real return anyway. That decade is where retail
advisors learned to *trust* the bond hedge, not just price it.
Across all three decades the stock-bond correlation ran around
−0.3 to −0.4. Whatever-asset-was-falling-the-other-was-rising, and
the rebalance trade *paid* you to mechanically buy the underperformer.
The 2020–24 row is what concerns the modern industry — and it is
the row the rest of this lesson exists to explain.

##### Why is rebalancing actually good — and why isn't 60/40 always worse than 100% stocks?

Look at the table honestly. Across the full 97-year window, 100%
stocks compounds at 6.8% real and 60/40 at 5.1% — roughly $565 vs
$128. **Over a long horizon, with no behaviour problem, 100% stocks
wins on terminal wealth.** The course is not going to pretend
otherwise. The case for 60/40 is not "higher return"; it is three
related effects:

1. **Drawdown compression.** In every crisis decade — 1930s, 1970s,
   2000s — 60/40 took materially less of the equity loss. -38%,
   -49%, -37% on stocks compressed to -23%, -36%, -15% on 60/40.
   That smaller hole is the *behavioural* alpha: an investor who
   does not panic-sell at -25% is a different person from one who
   panic-sells at -49%.
2. **The rebalancing premium.** Annual rebalancing forces a
   mechanical "sell what just outperformed, buy what just
   underperformed." Over decades that adds roughly 0.2–0.4% per
   year on a 60/40 mix (Bouchey, Nemtchinov, Paulsen and others
   estimate it in this range). It is not a free lunch — it
   requires *both* assets to be roughly mean-reverting and
   negatively correlated, which is exactly what failed in 2022 —
   but in normal regimes it is real and persistent.
3. **Volatility drag is non-linear.** A portfolio that goes -50%
   then +50% lands at -25% of starting value. A portfolio that goes
   -25% then +25% lands at -6%. Cutting the drawdown in half does
   *more* than halve the recovery cost. Lower-vol portfolios
   compound geometric returns closer to their arithmetic returns.

Honest framing for the lesson: **the correct comparison for a
buy-and-hold investor with a 30-year horizon is 100% stocks vs
60/40 vs the barbell — not 60/40 vs nothing.** 100% stocks wins on
terminal wealth across long enough windows; 60/40 wins on the worst
two-year stretch you have to live through; the barbell tries to keep
most of the equity upside while replacing the middle-of-the-curve
bonds with structurally better diversifiers (cash + gold + tail
hedges). We come back to that comparison at the end of this lesson.

##### Can rule-based / "timed" rebalancing improve on the calendar?

This is a real research literature, not folklore. The headline
finding: **rule-based variants modestly improve on calendar
rebalancing in *backtest*, but the improvement is small relative to
the variance across implementations and is fragile out of sample.**

- *Threshold (band) rebalancing* — rebalance only when the
  allocation drifts more than 5% in absolute terms (e.g., from 60%
  stocks to 65%) — captures most of the rebalance premium with
  fewer trades and less tax friction. Vanguard's working papers find
  it is marginally better than annual calendar rebalancing on a
  long-run US 60/40 backtest, ~0.05–0.15% per year.
- *Trend-overlay rebalancing* — only rebalance into an asset when
  it is above its 200- or 10-month moving average — improves
  drawdowns in some windows (notably 2008) and worsens them in
  others (notably 2020 V-shaped recovery, where you sold equities
  in March and bought back at a higher price in August). Net effect
  is close to a wash on long horizons.
- *Valuation-tilt rebalancing* — over-weight equities when CAPE is
  cheap, under-weight when expensive. Long-horizon backtests show
  ~0.3–0.6% per year of improvement on US data, but with very long
  drag spells (the strategy was wrong about US equities for most of
  2010–2020) and with severe data-mining concerns: there is one
  US history, the rules are tuned on it, and the next 30 years are
  not the previous 30 years.

Bottom line: a calendar or band-rebalanced 60/40 captures roughly
all of the *robust* premium. Anything more clever crosses the line
into *active* allocation — which can work, but at that point you
are no longer running a passive 60/40. We come back to discretionary
rebalancing under "Misconceptions" below and again in §2.7.

#### 2.3 The Correlation Story — The Hidden Variable

The chart below is the rolling 36-month correlation between US stocks
and US Treasuries from 1928 forward. The single most important fact
in the entire lesson lives on this chart.

![Rolling 36-month correlation between annual US stock returns and US Treasury returns, 1928 through 2024 (Damodaran data). The correlation oscillates dramatically: deeply positive (+0.6) through the 1970s, falling through zero around 1997, deeply negative (-0.4 to -0.6) for almost the entire 2000-2020 window, and snapping sharply positive again starting in 2022.](image/week04_stock_bond_corr.png)

Three regimes are visible:

- **1928–1997: stocks and bonds usually moved together.** Inflation
  was the dominant driver. Higher inflation meant both lower bond
  prices (rates rose) *and* lower stock prices (real earnings
  squeezed). Lower inflation lifted both. Correlation positive,
  diversification effect mediocre.
- **1998–2021: the great inverse window.** Inflation faded as the
  dominant driver and growth/recession became dominant. In
  recessions, the Fed cut rates → bonds rallied. In recessions,
  earnings cratered → stocks fell. Correlation deeply negative.
  60/40 delivered its best forty years ever.
- **2022 onward: the inverse regime cracked.** When the Fed had to
  tighten aggressively to fight 9% CPI, bonds fell *and* the
  earnings multiple compressed *and* stocks fell. Correlation
  flipped positive again. 60/40 had its worst year since the
  Great Depression-era stretch.

The simple frame: **stocks and bonds are negatively correlated when
the dominant macro driver is growth/recession; they are positively
correlated when the dominant driver is inflation.** Decide which
regime you think the next decade will be, and you have decided
whether 60/40 is still your friend.

#### 2.4 Bond Yields Are a Policy Variable, Not a Market Price

Before we get to 2022, one thing every investor running 60/40 needs
to understand and almost no certification curriculum says out loud:
**the bond half of your portfolio is not priced in a free market.**
The level and shape of the yield curve is set, in large part, by the
central bank. Short rates are *literally* set by the Federal Reserve
at the FOMC meeting. Long rates are nominally a market price but are
heavily steered by quantitative easing and tightening, by forward
guidance about future policy rates, and — in some jurisdictions —
by explicit *yield-curve control* (YCC), where the central bank
commits to buying or selling unlimited size to peg the yield at a
chosen level.

The cleanest worked example is the Bank of Japan. From 2016 to 2024
the BOJ ran explicit YCC, capping the 10-year Japanese government
bond yield first at 0% then at 0.25%, then 0.5%, then 1.0% — every
"adjustment" was a mini policy regime change that moved the entire
JGB curve overnight. JGB holders for those eight years were not
holding a free-market asset; they were holding a *policy promise*
whose payoff depended on the BOJ's willingness to keep printing.
When the BOJ exited YCC in 2024, the long end repriced sharply.

The Fed has done softer versions of the same thing. The 2008–2014
QE program suppressed long-Treasury yields by an estimated 100–150
basis points below where a free market would have cleared. The
2020–2021 emergency easing kept the 10-year below 1% for over a year.
The 2022 tightening was the *unwind* of those policy positions, not
a market-driven move.

What this means for your 60/40 portfolio is uncomfortable:

- The bond sleeve's expected return is the *current yield*, and the
  current yield is partially a *policy variable*. When you buy a
  10-year Treasury at 1% yield, you are accepting a return path
  that the Fed has explicitly chosen. When the Fed changes its
  mind — because of an inflation shock, a fiscal-dominance pivot,
  or a new chair with a different reaction function — the bond
  sleeve's price moves, sometimes brutally.
- "Tail risks" for the bond sleeve are policy events: yield-curve
  control, financial repression, an explicit higher inflation
  target, a debt-monetisation regime, restrictions on foreign
  Treasury holdings. None of these are tradable risks in the
  Markowitz sense; they are political events.
- The classic 60/40 *requires the Fed put* to work. The unstated
  assumption of the last forty years is: when stocks crash, the Fed
  cuts rates aggressively, bonds rally, and the bond sleeve carries
  the portfolio. Take away the Fed's willingness or ability to cut
  — because inflation is too high (1970s, 2022) or because rates
  are already at zero (2020 was the last time this constraint
  bit) — and the bond sleeve has nothing to give.

This is part of why bond yield *level* matters so much for whether
60/40 is sensible at any given moment (we revisit this directly in
Q1). At a 1% 10-year yield, the bond sleeve has almost no income
buffer and enormous duration risk on a rate-up move. At a 4–5% yield
the math is genuinely different: even a 100 bp rate shock leaves
the bond sleeve roughly flat over a year. The 60/40 portfolio is
a different instrument depending on where the central bank has set
the yield curve when you start.

#### 2.5 The 2022 Debacle — What Actually Happened

In one calendar year:

| Asset | 2022 total return |
|---|---:|
| S&P 500 (incl. dividends) | -18.1% |
| 10-year Treasury (incl. coupons) | -17.8% |
| 60/40 portfolio | ~-18.0% |
| CPI (inflation) | +6.5% |
| **60/40 in real terms (after CPI)** | **~-24%** |

That last number is the worst real-return year for the 60/40 portfolio
since 1937. The mechanism was simple and terrifying. The Fed funds
rate started 2022 at 0.25% and ended above 4%. Long bonds repriced
because of the rate move. Stocks repriced because the discount rate
on future cash flows is the long bond yield, and that doubled. Both
fell. Together. With no place to hide for the unhedged investor.

The 2022 drawdown also showed something else: **a 60/40 portfolio
provides no protection against an inflation shock.** Cash *lost less*
than long bonds because cash has near-zero duration and short T-bill
rates kept reinvesting at the rapidly rising Fed funds rate; gold
roughly held value; commodities rose. The classic two-asset
diversifier was the *worst* allocation in the year of high inflation
that everyone had been talking about for a decade.

##### What broke — a checklist

Five things had to be true for 60/40 to keep working. In 2022, all
five flipped at once. Use this as your forward-looking dashboard:

| Pillar | 1990s–2010s setting | 2022 setting |
|---|---|---|
| Inflation regime | Falling / anchored ≤2% | Spike to 9%, sticky |
| Policy rates | Low and falling, Fed put active | Rapid hiking, Fed put withdrawn |
| Stock-bond correlation | ~−0.3 (negative) | Sharply positive |
| Long-bond duration risk | Hidden by 40-year bull market | Realised — 30%+ losses on TLT |
| Real-return capture | Stocks + bonds beating CPI | Both lost real value together |

Read the right column as the warning sign. If those settings persist
or recur — if inflation stays sticky and the Fed cannot credibly cut
into a recession because CPI is still 4%, if the correlation stays
positive — the 1990s–2010s shape of 60/40 will not return. If they
reverse — disinflation back to 2%, growth scares pulling rates lower,
correlation flips back negative — 60/40's "golden age" framing is
appropriate again.

#### 2.6 Modern Adaptations — Where 60/40 Goes Now

A short history note before the adaptations. **60/40 is not a Ray
Dalio invention.** The 60/40 mix is the conventional advisor and
balanced-fund default that predates risk parity by decades — the
"60% stocks, 40% bonds" rule of thumb appears in pension and trust
literature back to the 1950s. *Dalio's* contribution is the **All
Weather portfolio** (and its institutional sibling, *risk parity*):
roughly 30% stocks, 55% long bonds, 15% commodities and gold by
*capital* weight, but balanced so each asset class contributes
equal *risk*. The unifying idea — diversify across macro regimes
rather than across asset labels — is genuinely different from
60/40. All Weather was designed precisely so that no single regime
(growth shock, inflation shock, deflation shock, recession) could
sink the portfolio. We come back to risk parity and All Weather
explicitly in Week 15 ("Multi-Asset and Risk Parity") and again in
Level 5; for the rest of this lesson we keep the focus on the
plain-vanilla 60/40 baseline.

Three modifications, in increasing order of complexity.

1. **Replace some bonds with cash.** When bond yields are below
   inflation, T-bills (short-duration, highest reinvestment of new
   yield) outperform long bonds in nearly every scenario. A 60/30/10
   allocation (stocks/short-Treasuries/cash) gives up almost no
   long-run return and dramatically reduces 2022-style drawdowns.
2. **Add a 5–10% gold sleeve.** Gold's correlation to stocks is near
   zero in normal regimes and turns negative in inflation shocks.
   The classic Permanent Portfolio (25/25/25/25 stocks / long-bonds
   / cash / gold) is the historical archetype; modern variants run
   smaller gold weights with a bigger equity tilt. Gold is not free
   — it has no yield and high real-rate sensitivity — but in the
   regime where 60/40 broke, gold worked.
3. **Add a long-volatility or trend-following sleeve.** A small
   allocation (5–10%) to managed-futures or long-vol structures
   pays for itself in tail events. This is the institutional
   adaptation; we cover it in detail in Week 47 and Week 50.

Comparing the major archetypes side-by-side:

| Allocation | Stocks | Bonds (long) | Cash / short Tsy | Gold | Other | Best regime | Worst regime |
|---|---:|---:|---:|---:|---:|---|---|
| 100% stocks | 100 | — | — | — | — | Long expansions, low CPI | Deep bear / GFC-style crash |
| Classic 60/40 | 60 | 40 | — | — | — | Disinflation + Fed put (1990s–2010s) | Inflation shock (1970s, 2022) |
| 60/30/10 | 60 | 30 | 10 | — | — | Same as 60/40 but cheaper drawdown in rate shocks | Same as 60/40, milder |
| 55/30/10/5 | 55 | 30 | 10 | 5 | — | Adds inflation buffer; closer to all-weather | Sustained negative real rates with no inflation |
| Permanent Portfolio | 25 | 25 | 25 | 25 | — | Any single-regime shock | Long bull market in stocks (gives up upside) |
| Dalio All Weather (~) | 30 | 40 | — | 7.5 | 22.5 commodities/TIPS | Diversified across all four macro regimes | Persistent stagflation with rising real rates |
| Barbell (Level 5 preview) | 50–70 (concentrated + asymmetric) | 0 | 20–35 | 5–10 | 5–10 tail hedges | Volatile regimes with both up- and down-tails | Long quiet grind upward (overpays for hedges) |

The honest framing is the one Horace pushes throughout the course:
**60/40 worked because of a specific macro regime that is unlikely
to repeat with the same intensity over the next decade**. It is not
broken. It is no longer optimal. The barbell shape — concentrated
safety on one end, asymmetric speculation on the other, very little
in the structurally-mediocre middle — is the more honest answer for
investors who can stomach a different shape of returns.

> **Important caveat.** The barbell is an *advanced migration path*,
> not a Week 4 implementation instruction. It requires the option,
> hedging, sizing, and tax tools we develop across Levels 2–4
> (especially Weeks 25–30, 41–42, 47, and 50). Do not try to build
> a barbell after this lesson. Build the 60/40 (or 60/30/10)
> baseline first, run it through one full crisis cycle, and only
> then consider the barbell migration described in Week 52. The
> right Week 4 takeaway is "I now understand the baseline that
> every later allocation will compare to."

#### 2.7 Rebalancing Strategies for 60/40

Three families of rebalancing rule, ordered by how much work they
take and roughly how much they capture of the rebalancing premium.

| Rule | What it does | Trades / year | Premium captured | Tax cost (taxable account) |
|---|---|---:|---|---|
| **Buy & hold (no rebalance)** | Let weights drift forever | 0 | None — equity allocation grows toward 100% | Zero |
| **Calendar — annual** | Reset to 60/40 every January | 1 | Most of it (~0.2–0.4% / yr) | Moderate |
| **Calendar — quarterly / monthly** | Reset on schedule | 4–12 | Marginal additional gain; transaction & tax costs eat it | High |
| **Threshold / band — 5% absolute** | Rebalance only when stock weight drifts ≥5% from target | ~0.3 in calm markets, several in crises | Comparable to annual, with fewer trades | Lower than annual |
| **Threshold / band — relative (e.g., ±25% of target)** | Wider bands; even fewer trades | ~0.1–0.5 | Slight underperformance vs annual | Lowest |
| **Trend / momentum overlay** | Only rebalance into an asset when it is above its trend (e.g., 200-day or 10-month MA) | Variable | Helps in trending bears (2008); hurts in V-recoveries (2020) | Variable |
| **Valuation tilt** | Over-weight the cheaper asset (CAPE, real-yield rules) | 1–4 | ~0.3–0.6% / yr in long backtests; severe data-mining risk | Moderate–high |

Two practical recommendations:

1. **For most retail 60/40 investors, threshold rebalancing on a 5%
   absolute band, checked quarterly, is the right answer.** It
   captures essentially all of the calendar-rebalance premium with
   fewer trades, lower taxes, and one psychological benefit: you
   only act when something has actually moved enough to matter.
2. **Direct new contributions toward the under-weight sleeve before
   ever selling.** Selling-to-rebalance is the last resort —
   contribution-rebalancing has zero tax cost and zero spread cost.
   Many investors going through their accumulation years never
   need to sell-rebalance at all if they are still adding new money.

The deeper trade-off — when "rule-based" rebalancing crosses the
line into discretionary active management — is covered under
Misconception 5 below.

---

### 3. Common Misconceptions

**Misconception 1: "Bonds are the safe part of 60/40."**

Bonds are *less volatile* than stocks. They are not safe. In 2022,
US Treasuries lost more than they had in any year of the prior
seven decades. Long bonds lost roughly 30%, which is a larger loss
than the median equity bear market. The "bond sleeve = safety"
framing is a 1980–2020 artefact of a 40-year bull market in bonds
caused by falling rates.

**Misconception 2: "60/40 has always worked."**

In real terms, 60/40 lost money over the entire 1965–1981 stretch.
For 16 years a balanced investor saw real wealth shrink because
inflation outran the combined nominal returns of stocks and bonds.
It was not until the 1980s that the long-run *real* trend returned.

**Misconception 3: "Adding bonds to a stock portfolio always reduces
return."**

Not necessarily. When you rebalance annually, the rebalancing
trade — selling whichever asset just outperformed and buying the
underperformer — is a small but persistent source of additional
return on top of the buy-and-hold blend, because it is a
mechanical "buy low, sell high." Some 60/40 backtests over long
horizons show *higher* compound returns than 100% stocks because
of this rebalancing premium plus the smaller drawdowns. The
free-lunch component is small, but real.

**Misconception 4: "International diversification fixes the problem."**

International stocks have a high correlation to US stocks in the
events that actually matter (recessions, financial crises, the COVID
crash). They reduce some country-specific risk but do little to
solve the stock-bond correlation problem in 60/40. *Asset-class*
diversification, not *geographic* diversification, is what shifts
the portfolio's response to inflation shocks.

**Misconception 5: "60/40 is actively managed if you rebalance."**

Calendar or band rebalancing back to a *fixed* allocation is *not*
active management — it is a mechanical rule with no view on the
future. Strict 60/40 with annual or 5%-band rebalancing is fully
passive at the strategy level. The key word is **fixed**.

Where the line moves is when the *target itself* changes based on a
view: reducing the bond weight when yields are low, raising stocks
when CAPE is cheap, switching to cash when the 200-day moving average
breaks. **Those are active decisions.** They may *each* be coded as
a mechanical rule, but the *choice of rule* is a discretionary view
on the future of returns and correlations. Once you do that, you
are no longer running passive 60/40 — you are running a tactical
allocation overlay, and you should evaluate it as one (alpha, edge,
out-of-sample robustness, drawdown vs benchmark). The honest test
is: would a different family of rules — selected today, with the
same logic — give a different allocation? If yes, it is active.

**Misconception 6: "I should rebalance frequently to capture the
rebalance bonus."**

The rebalancing premium is real but small (~0.2–0.4% per year on
typical 60/40 backtests). Quarterly or annual rebalancing captures
most of it; weekly or daily rebalancing has three problems that
together usually destroy the premium:

1. **Selling against momentum.** Most market moves run in trends
   over horizons of weeks-to-months before mean-reverting.
   Rebalancing weekly forces you to sell whatever just rallied
   *while it is still rallying* — selling a winner that is about
   to keep winning is the worst version of "buy low, sell high."
2. **Transaction costs and bid-ask.** Each unnecessary trade pays
   the spread plus, in some accounts, commissions. On a 60/40
   portfolio with weekly rebalancing the round-trip cost can match
   the entire rebalance premium.
3. **Tax friction in taxable accounts.** Every sell-side rebalance
   is a realisation event. Short-term gains are taxed as ordinary
   income (often >35% federal + state). A weekly rebalancer in a
   taxable account can give *all* of the rebalance premium back to
   the IRS — and then some. This is exactly why §2.7 recommends
   contribution-rebalancing first and threshold-band rebalancing
   second; both minimise realisations.

Annual is the conventional answer; semi-annual or 5%-band quarterly
is fine. More frequent than that is over-engineering that pays
momentum, spread, *and* the tax man for the privilege of looking
busy.

---

### 4. Q&A

**Q1: Should I run 60/40 in 2026?**

A: Honestly, "it depends on the bond yield." 60/40 is most defensible
at *higher* nominal bond yields and least defensible at low ones,
because the entire bond sleeve is asymmetric to the starting yield.
At a 1% 10-year yield (the 2020–2021 setup), the bond half delivers
1% of carry and takes a -10% hit on every 100 bp of rate-up move —
that is a structurally bad trade. At a 4–5% 10-year yield (closer to
where the curve has reset post-2022), the bond half delivers a
meaningful coupon, the duration risk is partially compensated, and
the math of 60/40 is genuinely much better. As of writing, US 10-year
yields in the 4-handle make 60/40 *more* defensible than it was in
2020 — but still inferior to the cash-tilted variants.

The deeper issue is the *Fed-put assumption*. The classic 60/40
implicitly assumes that when stocks crash, the Fed will cut rates
aggressively, bonds will rally, and the bond sleeve will carry the
portfolio. That assumption holds whenever inflation is anchored
near 2% (1990s–2010s). It breaks whenever inflation is sticky and
the Fed cannot credibly cut without re-igniting CPI (1970s, 2022).
Before committing to 60/40, ask yourself: *do I believe the next
crisis will be deflationary (Fed cuts, bonds save me) or
inflationary (Fed cannot cut, bonds fall with stocks)?*

For a long-horizon investor with no edge and no time to manage a
portfolio actively, 60/40 is still a defensible answer — but the
better defensible answer in the current regime is *60/30/10*
(stocks / short-duration Treasuries / cash) or 55/30/10/5
(adding gold). Pure long-bond 40% is the part most exposed to a
reversal of the 2022-style positive correlation regime, and it is
also the part most exposed to a Fed that is no longer free to cut.

**Q2: Why not 70/30 or 50/50? What's special about 60/40?**

A: Nothing is special — it's a convention, not a derivation. The
Sharpe ratio is fairly flat from about 40/60 to 70/30. The "right"
allocation is the one you can hold through a 35% drawdown without
selling. 70/30 is for higher-tolerance / longer-horizon investors;
50/50 is for shorter-horizon / lower-tolerance ones. 60/40 sits
in the middle and got institutionalised because of that.

**Q3: How do I implement 60/40 with ETFs in practice?**

A: Two ETFs is enough. VTI (or VOO/SPY for S&P 500) for the equity
sleeve; AGG or BND for the bond sleeve. Set monthly automatic
contributions in 60/40 proportions. Once a year, rebalance back to
60/40. Total annual time commitment: about thirty minutes. Total
expense ratio: roughly 0.04%.

**Q4: What about "all-in-one" balanced funds?**

A: Vanguard's VBAIX (60/40), iShares' AOR (60/40), and similar
products do the rebalancing internally. Slightly higher expense
ratio (0.07–0.30% vs 0.04% for the two-ETF version), no rebalancing
chore for you. Reasonable for accounts you don't want to touch.
For taxable accounts the two-ETF version is better because you can
control the tax timing on rebalances.

**Q5: Why did 2008 not break 60/40 the way 2022 did?**

A: In 2008, stocks fell ~37% and long Treasuries *rallied* roughly
+20%. The 60/40 drawdown was about −22% — bad, but materially less
than the equity drawdown. The bond rally had two compounding
causes: (1) **the Fed cut the funds rate from 5.25% in mid-2007 to
essentially 0% by December 2008** — a roughly 500 bp easing cycle
that mechanically lifted long-bond prices through duration; and
(2) a flight-to-safety bid, where investors fleeing equities and
credit parked cash in Treasuries, *adding* to the price move on top
of the policy-rate cut. The Fed-cut leg is by far the bigger driver
of the 20% bond rally — pure flight-to-safety in a quiet rate
environment usually delivers a few percent at most. In 2022 the
Fed was *raising* rates instead of cutting, so neither force was
available: there was no monetary tailwind for bonds and no
durable safe-haven bid (bonds were the asset people were fleeing
*from*). Mechanism difference: 2008 was a deflationary credit
shock with the Fed put fully active; 2022 was an inflationary
monetary shock with the Fed put withdrawn. The 60/40 portfolio is
hedged against the former and exposed to the latter.

**Q6: Should I rebalance with new contributions or by selling?**

A: With new contributions if you can. Direct your monthly inflow
to whichever sleeve is below target — that rebalances without
realising taxable gains and without paying spread. Sell-to-rebalance
only when contributions are no longer enough to fix the drift, or
once a year as a clean-up.

**Q7: What about international bonds?**

A: For US-domiciled investors, hedged international developed-market
bonds (BNDX) provide marginal additional diversification. In
practice the diversification benefit is small (the world's
investment-grade sovereign debt is heavily correlated through the
global rate cycle), and the FX hedge eats some of the yield. Most
practitioners skip them and just hold US Treasuries.

**Q8: Where does a "barbell" allocation fit relative to
60/40?**

A: The barbell rejects 60/40 at the philosophical level. The middle
of the risk spectrum (investment-grade bonds, dividend-stock
defensive allocations) is exactly the part the barbell strips out
because it is the part that gets crushed in inflation shocks. The
barbell holds *more* concentrated safety than 60/40 (cash, short
T-bills, gold) and *more* asymmetric speculation than 60/40 (long
calls, momentum equity, Bitcoin or specific asymmetric trades sized
as speculation — *not* a generic "crypto" allocation), with very
little in between.

**Q9: Is the rebalancing premium taxable?**

A: In a taxable account, every rebalance trade is a potential
realisation. To preserve the premium net of taxes, rebalance with
contributions where possible (no realisation), and use tax-advantaged
accounts (IRA, 401k, 529) for the sleeve that accumulates
fastest-growing gains. The two-ETF 60/40 is genuinely cheap on
expense; on taxes, your account structure matters more than the
ETF choice.

**Q10: How does this connect to the rest of the course?**

A: 60/40 is the baseline. **Week 5** goes deep on the bond half
(coupons, prices, yields, duration) — the mechanics behind why the
bond sleeve behaved the way it did in 2008 and 2022. **Week 6**
covers gold and commodities, which are the natural inflation-shock
complements to 60/40. **Week 11** merges rebalancing into the
behavioural-discipline lesson and covers the mechanics in detail.
**Week 15** introduces multi-asset and risk parity — the Dalio
"All Weather" alternative to 60/40. **Week 23** covers factor
investing, which slices the equity sleeve into return premia.
**Week 47** covers the long-volatility / tail-hedge sleeve that you
can graft onto 60/40 to address the inflation-shock vulnerability.
**Level 5 (Weeks 47–52)** is where the *barbell* portfolio shape
is actually built. Every subsequent allocation discussion will
compare to the 60/40 baseline you have just learned.

##### Interactive panel

The interactive panel below is a generalisation of the cumulative
wealth chart in §2.2: it starts from the same Damodaran 1928–2024
dataset and the same 60/40 line, but lets you sweep the stock
weight in 10% steps from 0% to 100% (so the static 60/40 line in
the §2.2 chart is what you see when the slider sits at 60%), toggle
between annual rebalancing and pure buy-and-hold, and switch
between real (CPI-adjusted) and nominal terms. Underneath the
wealth curve it draws the rolling drawdown from each running peak,
and reports the geometric annual return, annualised volatility,
worst drawdown, and Sharpe ratio (using the 3-month T-bill as the
risk-free rate). Slide it. Watch where the Sharpe-ratio peak sits,
and watch how the 1973–74 and 2008 drawdowns change shape as you
move the stock weight.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** The 60/40 Portfolio — Why It Worked, Why 2022 Broke It | Week 4

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** Last week was risk and return. This week is the most
famous portfolio on earth. 60% stocks, 40% bonds. Every advisor in
the country has recommended it. Every target-date fund is some
version of it. And in 2022 it had its worst year since 1937.

**Stella:** So is it broken or not?

**Horace:** It's not broken. It's also not what it was. By the end
of this lesson you'll know exactly which it is for *you*.

---

**[SEGMENT 1: WHY MIX AT ALL]**

**Horace:** The whole point of mixing stocks and bonds is one
equation. The volatility of a portfolio isn't the weighted average
of the volatilities of its parts. When the two assets are
negatively correlated — when one zigs while the other zags — the
combined volatility is *less* than either component, weighted.

**Stella:** That's the diversification benefit.

**Horace:** Right. And how big the benefit is depends entirely on
the correlation between stocks and bonds. From the late 1990s to
2021, that correlation was about minus 0.3. That negative
correlation is *the entire reason* 60/40 worked so well for so long.

---

**[SEGMENT 2: THE GROWTH CHART]**

[VISUAL: image/week04_sixty_forty_growth.png]

**Horace:** Here's the long-run growth chart. 100% stocks, 100%
bonds, 60/40 — all rebalanced annually, in real terms after
inflation, since 1928. By 2024, your dollar in real terms became
about five hundred sixty-five in 100% stocks, one hundred twenty-eight
in 60/40, and four in 100% bonds.

**Stella:** Bonds barely beat inflation across a century.

**Horace:** That's the whole century in one statistic. The long-run
real return on Treasuries is about 1.4% per year. Stocks, about
6.8%. 60/40 lands around 5.1%. Three-quarters of the equity rate,
with materially shallower drawdowns at every crisis.

**Stella:** Wait — if 100% stocks compounds at 6.8% and 60/40 only
at 5.1%, isn't 100% stocks just *strictly* better over a long
horizon?

**Horace:** On terminal wealth, yes — and this course is not going
to pretend otherwise. The case for 60/40 is not higher return.
It's three things together: drawdown compression, the rebalancing
premium of about a quarter percent a year, and the non-linear math
of volatility drag. The investor who can sit through a -49% real
drawdown in 100% stocks lands at $565. The one who panics at -49%
and sells lands at zero. 60/40 trades expected return for
behavioural survivability — and for some people that trade is the
difference between staying invested and not.

---

**[SEGMENT 3: THE CORRELATION FLIP]**

[VISUAL: image/week04_stock_bond_corr.png]

**Horace:** This is the most important chart in the lesson. Rolling
36-month correlation between stocks and bonds. Three regimes.

Up to 1997, mostly positive. Inflation was the dominant driver, and
inflation crushes both stocks and bonds simultaneously. From 1998 to
2021, deeply negative. Growth and recessions were the dominant
driver, and the Fed's cut-rates-in-recessions policy made bonds rally
while stocks fell. Then in 2022, snap.

**Stella:** Back to positive.

**Horace:** When inflation came back, the inflation regime came back.
Both fell together. The 60/40 portfolio had no shelter.

---

**[SEGMENT 4: 2022 THE ANATOMY — AND WHY THE BOND HALF IS A POLICY BET]**

**Horace:** Year of 2022. S&P 500 down 18. Ten-year Treasury down
17.8. CPI up 6.5. So 60/40 in nominal terms down 18, in real terms
down 24. Worst real year for the strategy since 1937.

**Stella:** Why did the Fed do that?

**Horace:** They had to. Inflation hit 9% and the policy rate was at
a quarter percent. They needed to fight inflation, which means
raise rates aggressively, which mechanically tanks bond prices. And
the same rate move tanked equity multiples. Same shock, both ends
of the portfolio.

**Stella:** And the lesson?

**Horace:** Two lessons, and the second one is the one professional
curricula skip. First: 60/40 hedges *recessionary* shocks. It has
no answer for *inflationary* shocks. Second — and bigger — the
bond half of your portfolio is *not* priced in a free market. The
central bank sets short rates directly at the FOMC meeting and
steers long rates through quantitative easing, forward guidance, and
in some places explicit yield-curve control. Look at the Bank of
Japan: from 2016 to 2024 they pegged the 10-year JGB yield first at
zero, then 0.25, then 0.5, then 1.0 percent — every adjustment was
a mini policy regime change. That is not a free market. The classic
60/40 implicitly *requires the Fed put* to work — the unstated
assumption that whenever stocks crash, the Fed cuts rates, bonds
rally, and the bond sleeve carries the portfolio. Take that
assumption away — because inflation is too high and the Fed cannot
credibly cut — and the bond sleeve has nothing to give. That is
2022 in one sentence.

**Stella:** And the bond yield level itself matters?

**Horace:** Hugely. At a 1% 10-year yield, 60/40 is structurally
broken — you have one percent of carry and almost infinite duration
risk on a rate-up move. At a 4 or 5% 10-year yield, 60/40 starts
making sense again. The same allocation is a different instrument
depending on where the central bank has set the curve when you
start. If the next decade looks more like the 1970s than the 2010s,
60/40 will continue to underperform a diversified inflation-hedged
version.

---

**[SEGMENT 5: WHAT TO DO INSTEAD]**

**Horace:** Quick history note before the modifications. 60/40 is
*not* a Ray Dalio invention — it is the conventional advisor and
balanced-fund default that goes back to the 1950s. Dalio's
contribution is the All Weather portfolio, which is genuinely
different: roughly 30 / 55 / 15 by capital but balanced so each
asset class contributes equal *risk*. The unifying idea is
diversifying across macro regimes, not across asset labels. We
come back to All Weather and risk parity in Week 15.

**Stella:** And for plain 60/40?

**Horace:** Three modifications, in order of how much work they take.

One. Trade some long bonds for short bonds or cash. Cash and short
Treasuries lost almost nothing in 2022 because they kept reinvesting
at higher yields. That's the cheapest fix.

Two. Add 5 to 10 percent gold. Zero correlation in normal times,
strong inflation hedge in regime breaks like 2022. Costs you the
yield-give-up but earns it back in tail events.

Three. Add a long-volatility sleeve. Trend-following or
managed-futures strategies pay for themselves in years like 2022 and
2008. We cover this in Week 47 — it's the institutional answer.

**Stella:** And the barbell people keep hearing about?

**Horace:** That's the Level 5 endpoint, not a Week 4 to-do.
The barbell strips out the structurally-mediocre middle and
replaces it with concentrated safety on one end and asymmetric
speculation on the other. It is the most honest answer for a
post-2022 world, but it requires the option, hedging, sizing, and
tax tools we build over Levels 2 through 4. Build the 60/40 or
60/30/10 baseline first, run it through one full crisis cycle, and
*then* think about the barbell migration. Don't skip the baseline.

---

**[SEGMENT 6: REBALANCING — HOW OFTEN, WITH WHAT RULE]**

**Stella:** And rebalancing? Annual, monthly, only-when-it-drifts?

**Horace:** Three families of rule. Calendar — once a year, every
January. Threshold — only rebalance when the stock weight drifts
five percent absolute from target. And rule-based overlays like
trend or valuation tilts. For most people, threshold on a 5%
absolute band, checked quarterly, is the right answer — it captures
essentially all of the rebalance premium with fewer trades and less
tax friction. And before any selling, direct your new contributions
to the underweight sleeve — that rebalances with zero tax cost.

**Stella:** And weekly?

**Horace:** Three problems. You sell winners that are still trending,
you pay the spread on every trade, and in a taxable account every
sell is a realisation event. Weekly rebalancing in a taxable account
gives all of the rebalance premium back to the IRS. Annual or 5%
band is the answer.

**Stella:** And once you start picking *which* rule based on a
view — like "reduce bonds when yields are low" — you've crossed
into active?

**Horace:** Exactly. The line is whether the *target itself* changes
on a view. Mechanical rebalance to a fixed 60/40 is passive.
Discretionary tactical overlay, even if each rule is mechanical, is
active. Evaluate it as such.

---

**[OUTRO]**

**Horace:** 60/40 is not broken. It is no longer the default-best.
The default-best in 2026 is closer to 60/30/10 with a small gold or
trend overlay. And whether you adopt that or stick with the classic,
you should know *why* you chose it. That's the whole lesson.

**Stella:** And the interactive?

**Horace:** Slider for the stock weight, slider for the rebalance
frequency. Plots the wealth curve, the drawdown, the Sharpe. Slide
it. Find your own sweet spot.

---

**END SCREEN:** "Next: Week 5 — Bonds: Coupons, Prices, and Yields"
