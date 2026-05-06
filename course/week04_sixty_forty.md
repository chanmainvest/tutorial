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
   trend, factor tilts, the barbell shape we get to in Week 14 — is
   measured against 60/40. You cannot evaluate any of those if you
   don't know what they are improving on.
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

- $763 at 100% stocks
- $304 at 60/40
- $9 at 100% bonds

The bonds-only line barely keeps up with inflation across the full
century — the long-run real return on Treasuries is close to 1.5%
per year. Stocks compound at roughly 7% real. 60/40 lands at
roughly 5.7% real, two-thirds of the way to the equity line in
*compound-rate* terms but with materially smaller drawdowns
along the way.

By decade, the picture is more nuanced:

| Decade | 60/40 (real ann.) | Stocks (real ann.) | Bonds (real ann.) | 60/40 max drawdown |
|---|---:|---:|---:|---:|
| 1930s | 1.0% | -0.1% | 4.7% | -28% |
| 1940s | 1.6% | 3.6% | -3.5% | -13% |
| 1950s | 12.5% | 16.7% | -2.6% | -8% |
| 1960s | 3.5% | 5.0% | -0.7% | -14% |
| 1970s | -0.7% | -1.4% | -1.0% | -18% |
| 1980s | 9.7% | 12.0% | 7.2% | -8% |
| 1990s | 8.7% | 14.8% | 4.6% | -6% |
| 2000s | 1.8% | -3.4% | 4.4% | -33% |
| 2010s | 6.8% | 11.4% | 1.6% | -10% |
| 2020-24 | 1.6% | 6.7% | -3.5% | -22% |

The 1980s and 1990s are the two decades that built 60/40's reputation.
Real bond returns above 7% per year. Real stock returns above 12%.
Stock-bond correlation around −0.3 to −0.4. Whatever-asset-was-falling-
the-other-was-rising, and the rebalance trade *paid* you to
mechanically buy the underperformer.

The 2020–24 row is what concerns the modern industry.

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

#### 2.4 The 2022 Debacle — What Actually Happened

In one calendar year:
- S&P 500 total return: −18.1%.
- 10-year Treasury total return: −17.8%.
- 60/40: roughly −18.0%.
- CPI: +6.5%.
- 60/40 in real terms: roughly −24%.

That last number is the worst real-return year for the 60/40 portfolio
since 1937. The mechanism was simple and terrifying. The Fed funds
rate started 2022 at 0.25% and ended above 4%. Long bonds repriced
because of the rate move. Stocks repriced because the discount rate
on future cash flows is the long bond yield, and that doubled. Both
fell. Together. With no place to hide for the unhedged investor.

The 2022 drawdown also showed something else: **a 60/40 portfolio
provides no protection against an inflation shock.** Cash earned
under inflation, gold roughly held value, commodities rose. The
classic two-asset diversifier was the *worst* allocation in the
year of high inflation that everyone had been talking about for a
decade.

#### 2.5 Modern Adaptations — Where 60/40 Goes Now

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

The honest framing is the one Horace pushes throughout the course:
**60/40 worked because of a specific macro regime that is unlikely
to repeat with the same intensity over the next decade**. It is not
broken. It is no longer optimal. The barbell shape — concentrated
safety on one end, asymmetric speculation on the other, very little
in the structurally-mediocre middle — is the more honest answer for
investors who can stomach a different shape of returns.

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

Rebalancing back to a fixed allocation is *not* active management.
It is a mechanical rule. Active management would be changing the
target allocation based on a view (e.g., reducing the bond weight
when yields are low). The strict 60/40 with annual rebalancing is
fully passive at the strategy level.

**Misconception 6: "I should rebalance frequently to capture the
rebalance bonus."**

The rebalancing premium is real but small (~0.2–0.4% per year on
typical 60/40 backtests). Quarterly or annual rebalancing captures
most of it; weekly or daily rebalancing trades against the same
return mean-reverts in the wrong direction and incurs transaction
costs. Annual is the conventional answer; semi-annual is fine.
More than that is over-engineering.

---

### 4. Q&A

**Q1: Should I run 60/40 in 2026?**

A: For a long-horizon investor with no edge and no time to manage
a portfolio actively, 60/40 is still a defensible answer — but the
better defensible answer in the current regime is *60/30/10*
(stocks / short-duration Treasuries / cash) or 55/30/10/5
(adding gold). Pure long-bond 40% is the part most exposed to a
reversal of the 2022-style positive correlation regime.

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

A: In 2008, stocks fell ~37% but Treasuries *rallied* roughly +20%
on the flight to safety. The 60/40 drawdown was about −22% — bad,
but materially less than the equity drawdown. In 2022, both fell
together. The mechanism: 2008 was a deflationary credit shock; 2022
was an inflationary monetary shock. The 60/40 portfolio is hedged
against the former and exposed to the latter.

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
calls, momentum equity, crypto), with very little in between.

**Q9: Is the rebalancing premium taxable?**

A: In a taxable account, every rebalance trade is a potential
realisation. To preserve the premium net of taxes, rebalance with
contributions where possible (no realisation), and use tax-advantaged
accounts (IRA, 401k, 529) for the sleeve that accumulates
fastest-growing gains. The two-ETF 60/40 is genuinely cheap on
expense; on taxes, your account structure matters more than the
ETF choice.

**Q10: How does this connect to the rest of the course?**

A: 60/40 is the baseline. Week 5 covers diversification more deeply.
Week 13–14 introduce the barbell. Week 23 covers factor investing,
which slices the equity sleeve into return premia. Week 47 covers
the long-volatility hedge that you can graft onto 60/40 to address
the inflation-shock vulnerability. Every subsequent allocation
discussion will compare to this baseline.

The interactive panel below lets you slide the stock weight from
0% to 100% and the rebalance frequency from monthly to never. It
plots the resulting cumulative real wealth on the Damodaran 1928–2024
dataset along with the maximum drawdown and the geometric annualised
return. Slide it. Watch where the Sharpe-ratio peak sits, and watch
how the 1973–74 drawdown changes shape as you move the bond weight.

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
seven hundred and sixty in 100% stocks, three hundred in 60/40,
and nine in 100% bonds.

**Stella:** Bonds barely beat inflation across a century.

**Horace:** That's the whole century in one statistic. The long-run
real return on Treasuries is about 1.5% per year. Stocks, about
7%. 60/40 lands around 5.7%. Two-thirds of the equity rate, with
materially shallower drawdowns at every crisis.

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

**[SEGMENT 4: 2022 THE ANATOMY]**

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

**Horace:** 60/40 hedges *recessionary* shocks. It has no answer for
*inflationary* shocks. If the next decade looks more like the
1970s than like the 2010s, 60/40 will continue to underperform a
diversified inflation-hedged version.

---

**[SEGMENT 5: WHAT TO DO INSTEAD]**

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

**END SCREEN:** "Next: Week 5 — Diversification Done Right"
