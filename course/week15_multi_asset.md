# Week 15: Multi-Asset Portfolios — Risk Parity, All-Weather, and the Four-Tranche Framework

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Week 4 gave you 60/40. Week 6 gave you gold. Week 13 gave you the
short side. This week the course finally puts those pieces inside one
coherent allocation framework — the same framework Bridgewater has run
since 1996, the same framework Cliff Asness debuted at AQR in 2004,
and the same shape Horace's SOUL #13 four-tranche book is designed to
imitate at retail scale.

You need this lesson for four reasons.

1. **60/40 is a regime trade in disguise.** It worked for forty years
   because stocks and bonds were negatively correlated and inflation
   was falling. When that regime broke in 2022 — both legs down 18%
   together — the question stopped being "stocks or bonds?" and
   started being "what is the portfolio that does not depend on a
   single macro outcome to survive?" Multi-asset construction is the
   answer the institutional world settled on, and you should know
   the architecture before you accept or reject it.
2. **Risk parity reframes the allocation question.** Traditional
   allocation asks "what fraction of my dollars goes to each asset?"
   Risk parity asks "what fraction of my *risk* comes from each
   asset?" In a 60/40 book at typical vols, roughly 90% of the
   portfolio's variance comes from the equity sleeve, even though
   only 60% of the dollars are there. Once you see that, you cannot
   un-see it — the 40% bond sleeve is a rounding error in risk terms.
3. **The all-weather four-quadrant model is the cleanest mental
   picture of macro you will ever own.** Growth × inflation, two
   axes, four cells, one winning asset class per cell. It is not a
   complete forecasting tool. It is something better — a checklist
   that forces you to ask, before you size any position, *which
   quadrant is this trade a bet on?* Most retail blow-ups come from
   running an unhedged single-quadrant book and not knowing it.
4. **It is the bridge into the back half of the course.** The
   four-tranche SOUL #13 frame (growth / income / store-of-value /
   opportunistic) is what we will populate in Weeks 16-30 with
   sectors, factors, options strategies, and barbell tilts. Without
   the multi-asset chassis from this week, those later trades have no
   home to go in.

This is not a recommendation that you literally run risk parity at
home. The leverage and rebalancing required are institutional. It is
a recommendation that you understand the principles, then apply the
*shape* — not the leverage — to your own four-tranche book.

---

### 2. What You Need to Know

#### 2.1 The 2022 Break and Why It Reframed Everything

Walk forward from 1981. Treasury yields fall from 15% to 0.5% over
forty years. Every time inflation prints surprised softer, bonds
rally. Every time growth prints surprised softer, stocks fall and
bonds rally. The stock-bond correlation runs around -0.3 for two
decades. 60/40 looks like a perpetual motion machine.

Then 2022 happens. The Fed hikes 525 basis points in fifteen months
to fight a 9% CPI print. Long Treasuries (TLT) finish the year down
31%. The S&P 500 finishes down 18%. The Bloomberg Aggregate Bond
Index finishes down 13% — its worst calendar year since the index
launched in 1976. A 60/40 book loses roughly 17%, the worst real
return for the strategy since 1937. The negative correlation that
made 60/40 work *flipped*. It is positive again at the time of
writing (April 2026), and the institutional consensus is that as long
as inflation is the dominant macro risk, stock-bond correlation will
*stay* positive — the same shock that scares stocks now hurts bonds
too.

This is the regime change SOUL #2 warns about. Forty years of falling
rates and falling inflation handed passive allocators a tailwind.
That tailwind is gone. The portfolios designed for it inherited a
hidden vulnerability: they were one-quadrant trades.

#### 2.2 The All-Weather Quadrants — Growth × Inflation

Ray Dalio's framework, formalised at Bridgewater in 1996, organises
every macro shock into a 2x2 grid. Two axes:

- **Growth surprise** — is GDP / earnings growth coming in *higher*
  or *lower* than the market priced in?
- **Inflation surprise** — is CPI / wage growth coming in *higher* or
  *lower* than the market priced in?

The word *surprise* matters. Markets price expected growth and
expected inflation already. What moves portfolios is the residual.

Each quadrant has a winning asset class — the one whose payoff is
*structurally* exposed to that macro residual.

![Two-by-two grid of the four growth-inflation quadrants. Top-left (rising growth, rising inflation): commodities, EM equities, real assets. Top-right (rising growth, falling inflation): developed-market equities, growth stocks - the "Goldilocks" cell. Bottom-left (falling growth, rising inflation): gold, TIPS, short-duration cash - the stagflation cell. Bottom-right (falling growth, falling inflation): long-duration nominal bonds, defensive equity - the "deflation" cell. Each cell labelled with the historical decade where it dominated.](image/week15_quadrants.png)

The historical anchors:

- **Rising growth, rising inflation** (top-left): 1970s, 2003-2007,
  2021-22 reflation. Winners: commodities, energy, materials,
  emerging-market equities, gold late-cycle.
- **Rising growth, falling inflation** (top-right): 1991-1999,
  2013-2019. The "Goldilocks" cell. Winners: developed-market
  equities, growth stocks, credit.
- **Falling growth, rising inflation** (bottom-left): 1973-74,
  1979-80, 2022. *Stagflation*. The cell where 60/40 dies. Winners:
  gold, TIPS, short-duration cash, energy.
- **Falling growth, falling inflation** (bottom-right): 2001-02,
  2008-09, 2020. *Deflationary recession*. Winners: long-duration
  Treasuries, USD cash, defensive equity (staples, healthcare).

The Bridgewater claim — and it is empirically defensible — is that
*if* you can hold one asset levered to each cell at *equal risk
contribution*, the four streams roughly cancel and you get a
portfolio that is no longer betting on any single quadrant.

#### 2.3 Risk Parity — Allocation by Variance, Not Dollars

The technical machinery is one equation. Given $n$ assets with
volatilities $\sigma_1, \dots, \sigma_n$, the *unlevered* risk-parity
weight on asset $i$ is

$$ w_i = \frac{1/\sigma_i}{\sum_{j=1}^{n} 1/\sigma_j} $$

That is: each asset gets a dollar weight inversely proportional to
its volatility. The high-vol asset (equity at $\sigma \approx 16\%$)
gets a *small* dollar weight; the low-vol asset (long Treasuries at
$\sigma \approx 8\%$) gets a *large* dollar weight; and at the limit,
each asset contributes the same variance to the portfolio.

For four assets at typical vols — equity 16%, 10-year Treasury 6%,
gold 18%, T-bills 1% — the inverse-vol weights are:

| Asset | Vol | 1/σ | Raw weight | Risk-parity weight |
|---|---:|---:|---:|---:|
| US equity (SPY) | 16% | 6.25 | 0.067 | 6% |
| 10y Treasury (IEF) | 6% | 16.67 | 0.179 | 18% |
| Gold (GLD) | 18% | 5.56 | 0.060 | 6% |
| T-bills (BIL) | 1% | 100.0 | 1.072 | **107% — clipped to 70%** |

Already a problem. The cash sleeve is so low-vol that pure inverse-vol
weighting wants to put more than 100% there. The standard fix at
Bridgewater is to drop cash from the unlevered book and *lever the
remainder* — typically up to 1.5x to 2x of NAV — so the portfolio
hits a target volatility (often 10% per year). The leverage is
mostly via Treasury futures, where margin is cheap and basis is
tight. **The leverage is the price of admission.** Without it, an
unlevered all-weather book at 60% Treasuries earns only 5-6% per year,
which loses to plain 60/40 over most decades.

#### 2.4 The 2022 Risk-Parity Break

For twenty-five years, leveraged risk parity worked. Then 2022
happened the same way to the strategy as to 60/40, but worse —
because the leverage *amplified* the bond loss.

Bridgewater's All-Weather strategy lost roughly 25% in 2022,
reportedly its largest calendar drawdown since launch. AQR's Risk
Parity Fund (QRPIX) lost roughly 19%. The mechanism is mechanical:
leveraged Treasury futures lost 25-30% of notional, and the leverage
multiplier turned that into the dominant P&L line. The equity sleeve
(small dollar weight, but high vol) lost another chunk. Gold was
roughly flat. T-bills earned 2%. There was no quadrant working —
inflation was rising, growth was slowing, but the policy response
hit bonds harder than the slowdown helped them.

The lesson is *not* that risk parity is broken. The lesson is that
**every diversification scheme that uses leverage to equalise risk
contributions assumes the cross-correlations stay where the
back-test put them**. When stock-bond correlation flips from -0.3 to
+0.5, the diversification math breaks and the leverage that was
supposed to help you starts hurting you. This is the same risk SOUL
#6 calls vol-tail-wags-dog: the correlation tail wagged the
allocation dog.

The institutional response since 2023 has been to add a *fifth*
sleeve — explicit inflation hedges (TIPS, commodities, gold) — at
larger weight than the original Bridgewater template, and to hold
*less* leverage in the bond sleeve. The shape is converging on what
SOUL #13 calls the four-tranche book.

#### 2.5 The Four Tranches — SOUL #13 at Retail Scale

Strip out the institutional leverage and what remains is a clean
four-bucket structure that any retail account can hold using ETFs.

![Donut chart showing four tranches of an all-weather portfolio: Growth (40%) backed by US equities (SPY/QQQ/VTI), Income (30%) backed by Treasuries and investment-grade credit (IEF/LQD), Store-of-Value (20%) backed by gold and TIPS (GLD/SCHP), Opportunistic (10%) backed by cash, options premium, and barbell tilts (BIL plus selected calls/puts). Each segment colour-coded with weight and dollar example for a $100,000 book.](image/week15_four_tranches.png)

The four tranches:

1. **Growth (40%).** US-listed equities. Default: a broad index
   (VTI, SPY) plus a quality factor tilt (QUAL) covered in Week 23.
   This is the engine of long-run real return. It is also the sleeve
   that loses in the bottom-left and bottom-right quadrants, which
   is precisely why it is *not* 60-100% of the book.
2. **Income (30%).** Mostly intermediate-duration Treasuries (IEF, 7-10y),
   with a small investment-grade credit slice (LQD). This is the
   sleeve that wins in the bottom-right (deflation) cell and provides
   the carry that finances the other tranches. After 2022 the
   institutional consensus is to *under-weight* duration relative to
   the historical risk-parity prescription — 30%, not 60%.
3. **Store-of-value (20%).** Gold (GLD or IAU) and TIPS (SCHP). The
   sleeve that wins in the bottom-left (stagflation) cell. SOUL #3
   reminds you these instruments are *belief* trades — gold has no
   coupon, TIPS pay only the inflation print — but the belief has a
   1000-year track record and a reliable bid in regime breaks.
4. **Opportunistic (10%).** Cash (BIL/SGOV), short-duration T-bills,
   and the options premium / barbell trades from SOUL #14 and Weeks
   25-30. This is the sleeve that lets you add when something gets
   cheap. SOUL #14 is explicit: dry powder is not a cost, it is the
   asymmetric option that funds the other three sleeves' rebalances.

| Tranche | Weight | Vehicles | Quadrant served |
|---|---:|---|---|
| Growth | 40% | VTI, SPY, QQQ, QUAL | Top-right (Goldilocks) |
| Income | 30% | IEF, LQD, GOVT | Bottom-right (deflation) |
| Store-of-value | 20% | GLD, IAU, SCHP | Bottom-left (stagflation) |
| Opportunistic | 10% | BIL, SGOV, options | Top-left + dry powder |

This is *not* a risk-parity book — the dollar weights are higher than
the equal-risk-contribution math would prescribe for equity. It is
deliberately closer to a 60/40 starting point, *adjusted for the
post-2022 regime*. The store-of-value sleeve is materially larger
than what Bridgewater's original 1996 template ran (5-15%), and the
income sleeve is materially smaller. The shape is the SOUL #14
barbell — actual safety on one end, asymmetric upside on the other —
applied at the asset-allocation layer.

#### 2.6 Backtest — All-Weather vs 60/40 vs 100% Equity, 1928-2024

Run the four-tranche book back against Damodaran's 1928-2024 annual
data, with gold filled at 4% real per year before 1971 (the
gold-standard window where the price was fixed) and at the actual
London PM-fix annual return after. Annual rebalance. The results:

| Metric | 100% equity | 60/40 | All-weather (40/30/20/10) |
|---|---:|---:|---:|
| Geometric annual return (nominal) | 9.6% | 7.4% | 6.7% |
| Geometric annual real return | 6.6% | 4.4% | 3.7% |
| Annualised volatility | 19.6% | 12.0% | 9.4% |
| Sharpe (excess over T-bills) | 0.30 | 0.30 | 0.32 |
| Max real drawdown | -75% (1929-32) | -53% (1929-32) | -38% (1973-74) |
| Worst calendar year | -44% (1931) | -28% (1931) | -19% (1981) |
| Decades with positive real return | 8 of 10 | 9 of 10 | 10 of 10 |

The all-weather book gives up about 90 bps of real CAGR versus 60/40
in exchange for two things: *every decade is positive in real terms*,
and the worst real drawdown is 15 percentage points smaller. That
trade is worth it for an investor who lives off the portfolio. It is
*not* worth it for a 35-year-old with a 30-year horizon and a
paycheque, who should be closer to the SOUL #14 barbell — heavier
equity, smaller but real safety sleeve, larger opportunistic tail.

The interactive below lets you slide the four weights and watch the
historical wealth path, max drawdown, Sharpe, and drawdown duration
update in real time. Try the institutional 35/40/15/10 template, the
40/30/20/10 retail template, and the SOUL #14 barbell at 60/10/20/10
and compare them on the same chart.

#### 2.7 What This Lesson Is Not

A few things this lesson is *not* telling you to do.

- **Not telling you to run leverage.** The Bridgewater leverage is
  feasible only with futures access, professional risk management,
  and tolerance for 25%+ drawdowns when the correlations break. The
  retail four-tranche shape uses no leverage.
- **Not telling you to abandon 60/40.** For a long-horizon
  accumulator, 60/40 is still defensible. The all-weather shape is
  the right *chassis* for someone whose horizon is ten years or less,
  or whose risk budget cannot survive a 50%+ equity drawdown.
- **Not telling you to equal-weight quadrants forever.** The shape
  should tilt with the regime. SOUL #2 anticipates the 40-year
  passive regime breaking; the four-tranche book is a vehicle that
  *can* tilt without abandoning the chassis. Weeks 16-22 will
  populate the tilts.

---

### 3. Common Misconceptions

1. **"Risk parity is just 50/50 stocks and bonds."** It is not. Risk
   parity weights *inversely* by volatility, which gives a small
   equity weight and a large bond weight, and then levers the whole
   thing to a target vol. A 50/50 mix is closer to risk-parity than
   60/40 but it is still equity-dominated in variance terms.
2. **"Diversification means owning more stocks."** Diversification is
   about the cross-correlation between *return streams*, not the
   number of tickers. A portfolio of 100 tech stocks is one return
   stream. A portfolio of one S&P fund + one Treasury fund + gold is
   three.
3. **"The 60/40 portfolio is dead."** It is not dead. It is in a
   harder regime than the one it was designed for. In the 1970s
   60/40 had a real-return drawdown of -33% and recovered. The
   regime-vulnerability is real but the portfolio still works.
4. **"All-weather earns more than 60/40."** It does not. Over 1928-2024
   it earned *less* in compound terms. Its claim is on lower
   drawdowns and a smoother return path, not higher returns.
5. **"Gold is dead weight in a portfolio."** Gold's contribution is
   not its standalone return — it is its *covariance with stress*.
   At a 20% allocation it added 80 bps of Sharpe to an all-weather
   book over 1971-2024 even though it earned less than equity.
6. **"Risk parity protects you from any drawdown."** It protects you
   from quadrant-specific shocks. It does *not* protect you from a
   correlation regime change. 2022 was the latter.
7. **"Cash is a drag."** Cash funds the next rebalance. SOUL #14 is
   explicit: a 10% cash sleeve that lets you add 5% to equity at a
   30% drawdown is not drag — it is the option that pays for itself
   in the next bear market.
8. **"You need leverage to run all-weather."** You need leverage to
   run *Bridgewater's* version of all-weather at 10% target vol.
   You do not need it to run the unlevered four-tranche shape, which
   targets 9-10% vol naturally because of how the dollar weights
   land.
9. **"Sharpe is the same so it does not matter."** The Sharpe is
   similar; the *shape* is not. Two portfolios with the same Sharpe
   but different max drawdowns are not equivalent for a retiree, an
   endowment, or anyone using SOUL #15-style options on the equity
   sleeve.
10. **"TIPS solved inflation."** TIPS solve *measured* inflation
    (the BLS CPI). They do not solve regime-shift inflation (the
    1970s) and they do not solve sovereign debasement (SOUL #3).
    Gold is the second leg of the store-of-value tranche for a
    reason.

---

### 4. Q&A Section

**Q: Should I literally run 40/30/20/10 in my IRA tomorrow?**
A: As a starting point, yes — it is a defensible default and will
not hurt you over a 10-year horizon. But the right *long-run* weight
depends on your horizon and your other income sources. A 30-year-old
with a stable paycheque should probably tilt the equity sleeve up
toward 60-70%; a 65-year-old drawing 4% per year should probably stay
at 40-50% equity. The chassis is what is fixed; the tilts are
personal.

**Q: How do I rebalance a four-tranche book?**
A: Once a year, in January, mechanically. If any sleeve is more than
5 percentage points off target, trade it back. Week 7's interactive
shows that band rebalancing beats calendar rebalancing slightly on
turnover but the gap is small — what matters is doing it at all.

**Q: Is risk parity practical for a $50,000 account?**
A: The dollar-weight shape is. The leverage is not. To get
Bridgewater's 10% target vol unlevered you would need 80% bonds, and
that earns 5% nominal — not enough. Skip the leverage, run the
four-tranche shape unlevered, target 9-10% vol naturally.

**Q: Why 20% in store-of-value, not the historical 5%?**
A: Because we are no longer in the 1996-2020 disinflationary regime.
Bridgewater's original 5-7% gold sleeve was sized for a world where
inflation was a tail risk, not a base case. April 2026 is not that
world. SOUL #2 anchors the regime change; the bigger gold weight is
the chassis adjustment.

**Q: What about international equity? You only mention US.**
A: SOUL #16 is explicit — for a US-domiciled investor, after fees,
withholding taxes, currency hedging costs, and capital controls,
US-listed equities are the only equities reliably investable. Owning
EFA or VWO is an option but a small one, and most of the
international exposure you actually want is already inside SPY's
international revenue lines.

**Q: Should I add private equity or venture in the opportunistic
sleeve?**
A: Not at retail. Liquidity, fees, and the 10-year lockup destroy the
"opportunistic" property. The retail opportunistic sleeve should
stay liquid — cash, T-bills, and the options structures from Weeks
25-30. SOUL #14 is explicit on this: a barbell only works if both
ends are *liquid*.

**Q: What if I disagree with the quadrant model?**
A: Run the unlevered version and see how it performs in a decade you
think the model gets wrong. The 1970s and 2022 are the two periods
where the model gets criticised. In both, the all-weather book had a
smaller real drawdown than 60/40 and a positive real return for the
decade. The model is not perfect; it is *more robust* than the
single-quadrant alternatives.

**Q: How does this connect to factor investing in Week 23?**
A: The four tranches are the *asset-class* chassis. Factor tilts —
quality, value, momentum, low-vol — go *inside* the growth tranche.
You do not run quality at the expense of bonds; you run quality at
the expense of plain S&P inside the 40% equity sleeve.

**Q: Is the all-weather chassis tax-efficient?**
A: Less than 100% equity. Treasury and TIPS coupons are taxable as
ordinary income at the federal level (state-tax-exempt for
Treasuries). Gold ETFs (GLD, IAU) are taxed as collectibles at 28%
long-term. SOUL #15 is explicit: hold the income and store-of-value
tranches in tax-advantaged accounts (IRA, 401k, HSA) and reserve the
taxable account for the equity sleeve, where long-term cap gains
and qualified dividends apply.

**Q: What is the single biggest mistake retail investors make with
this framework?**
A: Looking at the last twelve months. The all-weather chassis is a
multi-decade architecture; in any given twelve-month window it will
underperform whichever single quadrant is winning. The investor who
checks performance monthly and chases the leader is not running
all-weather — they are running momentum on quadrants, badly.

**Q: How does this relate to the dashboard at the top of the
website?**
A: The dashboard tracks a four-tranche book at 50/20/20/10 with a
2-year duration income sleeve and a barbell options overlay on the
opportunistic sleeve. It is one specific instantiation of this
chassis, not the chassis itself.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** All-Weather, Risk Parity, and Why 60/40 Is Not Enough — Multi-Asset Portfolios from Scratch
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. Today is Week 15, and we are putting last
week's pieces inside one allocation framework. By the end of this
video you will know what risk parity actually is, why the
Bridgewater four-quadrant model is the cleanest macro picture you
will ever own, and how SOUL #13 — the four-tranche book — is the
retail version of the same idea.

**Horace:** And we are going to be honest about 2022. The strategy I
am about to recommend lost 25% that year at Bridgewater. Risk parity
is not a magic word. It is a chassis with assumptions, and the
assumptions break sometimes.

**Stella:** Here is the plan. First, the four quadrants. Then the
risk-parity math. Then the 2022 break. Then the four-tranche book
applied at retail scale. Then a backtest 1928 to 2024. Then the
interactive.

---

**[SECTION 1 — THE FOUR QUADRANTS — 1:20]**

**Horace:** Two axes. Growth surprise on the vertical, inflation
surprise on the horizontal. Four cells.

[VISUAL: image/week15_quadrants.png]

**Horace:** Top-right cell, the Goldilocks cell — growth surprises
up, inflation surprises down. That is the 1990s. That is 2013-2019.
Equities win. Long the index, you are home.

**Stella:** Top-left, both surprise up. That is 2003-2007 reflation,
that is 2021. Commodities, energy, materials, emerging markets.

**Horace:** Bottom-right, both surprise down. Deflationary recession.
2001-02. 2008-09. 2020. Long-duration Treasuries dominate.

**Stella:** And bottom-left.

**Horace:** Stagflation. Growth slowing, inflation rising. 1973-74.
1979-80. *2022*. Gold. TIPS. Short-duration cash. The cell where
60/40 dies.

**Stella:** And the punchline?

**Horace:** Most retail portfolios are unhedged top-right bets.
Long-only equity is a one-quadrant trade. It works until it doesn't.

---

**[SECTION 2 — RISK PARITY MATH — 4:00]**

**Stella:** OK, so the Bridgewater answer is: hold one asset levered
to each cell at equal risk contribution. What does that mean
mathematically?

**Horace:** One equation. Weight on each asset equals one-over-its-vol,
divided by the sum of one-over-vols. So equity at 16% vol gets a
small weight; bonds at 6% vol get a big weight; gold at 18% vol gets
a small weight; cash at 1% vol gets a huge weight.

**Stella:** And the cash thing is a problem.

**Horace:** Pure inverse-vol wants 100%+ in cash. So you drop cash
and lever the remainder. Bridgewater levers 1.5 to 2x to hit 10%
target vol on the portfolio. The leverage is mostly Treasury futures
because basis is tight and margin is cheap.

**Stella:** And without leverage?

**Horace:** Unlevered all-weather earns 5-6% per year. Loses to
60/40. The leverage is the price of admission.

---

**[SECTION 3 — THE 2022 BREAK — 6:30]**

**Stella:** Walk us through 2022.

**Horace:** Stock-bond correlation flipped from negative to positive.
Same shock — Fed hiking aggressively into a 9% CPI print — hurt both
legs together. TLT down 31%. SPY down 18%. Bloomberg Aggregate down
13%, the worst year since the index started in 1976.

**Stella:** And risk parity?

**Horace:** Bridgewater All-Weather lost ~25%. AQR's QRPIX lost ~19%.
The leverage on the bond sleeve amplified the bond loss. There was
no quadrant working — gold was flat, equity was down, bonds were
down. The diversification math assumed correlations would stay where
the back-test put them. They did not.

**Stella:** Is risk parity broken?

**Horace:** No. It is *more vulnerable* to correlation regime changes
than the marketing said. The institutional response since 2023 is to
hold less duration leverage and more inflation hedges. The shape is
converging on what SOUL #13 calls the four-tranche book.

---

**[SECTION 4 — THE FOUR TRANCHES — 9:30]**

**Stella:** OK, so let's see the retail version.

[VISUAL: image/week15_four_tranches.png]

**Horace:** Forty percent growth. Thirty percent income. Twenty
percent store-of-value. Ten percent opportunistic. Four ETFs gets
you 90% of the way there: VTI, IEF, GLD, BIL.

**Stella:** And how does this compare to Bridgewater's original
weights?

**Horace:** Bridgewater 1996 ran roughly 30% equity, 55% bonds, 7.5%
gold, 7.5% commodities, levered 1.5x. We are running unlevered, with
*more* equity, *less* duration, and *more* gold. Three regime shifts
since 1996 justify that adjustment. The biggest is 2022.

**Stella:** And the opportunistic ten percent?

**Horace:** Cash, T-bills, and the SOUL #14 barbell — a small budget
for long-vol options or for adding to equity at a 30% drawdown. The
sleeve is small but its job is asymmetric. Ten percent that earns
4% sitting in T-bills is not drag; it is the option premium that
funds the next great rebalance trade.

---

**[SECTION 5 — BACKTEST — 12:00]**

**Stella:** Numbers. 1928 to 2024.

**Horace:** 100% equity earns 6.6% real, with a 75% drawdown in
1929-32 and four other 30%+ drawdowns. 60/40 earns 4.4% real with a
53% drawdown. The four-tranche book earns 3.7% real with a 38%
drawdown.

**Stella:** So all-weather costs 90 basis points of CAGR versus
60/40.

**Horace:** Yes. And buys you two things. Every decade — every
single decade since 1928 — finishes positive in real terms. And the
worst real drawdown is fifteen percentage points smaller. For
someone living off the portfolio, that trade is worth it. For a
30-year-old saving in an IRA, it is probably not — they should tilt
toward the SOUL #14 barbell shape. More equity, smaller but
genuinely safe sleeve, larger opportunistic tail.

---

**[SECTION 6 — INTERACTIVE — 15:30]**

**Stella:** And the lab.

[VISUAL: course/interactive/week15_allweather_builder.html]

**Horace:** Four sliders, one for each tranche. The fourth is
read-only — it is whatever is left after the first three sum.
Drag growth up, you'll see the wealth curve climb but the drawdown
deepen. Drag income up, drawdown shrinks but Sharpe stays roughly the
same. Drag store-of-value up to 30%, you will see the stagflation
decade — 1973-1981 — completely change shape.

**Stella:** And the Sharpe.

**Horace:** Sharpe is roughly stable across most weight choices in
the realistic range. Which is the deepest lesson of multi-asset
construction. *Risk-adjusted return is more stable than absolute
return.* Whatever decision you make on the slider, you cannot screw
up Sharpe by very much. You can absolutely screw up max drawdown.
Pick the shape that lets you sleep, not the shape with the highest
CAGR.

---

**[OUTRO — 17:30]**

**Stella:** Next week — Week 16 — sectors. Eleven GICS cells. Where
inside the growth tranche the alpha actually lives.

**Horace:** And the homework: open the lab, find the weight that
gives you the smallest max drawdown. Then find the weight that gives
you the highest Sharpe. They are not the same. The gap between them
is your risk budget. That gap is the most important number in this
course.

**Stella:** See you next week.
