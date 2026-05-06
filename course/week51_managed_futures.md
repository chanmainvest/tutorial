# Week 51: Managed Futures and Trend-Following — Diversifying Alpha and Crisis Convexity

---

## Part 1: Reading Section

---

### 1. Why This Is Important

If you have read Week 47 you already know one of the strangest facts in
asset management: a trend-following CTA index returned roughly **+14%
in 2008** while the S&P 500 lost **−37%** and the dutifully-balanced
60/40 lost **−22%**. In 2022 the SocGen CTA Index ran **+20%** while
60/40 had its worst calendar year since 1937. In March 2020, with the
S&P down a third in twenty trading days, the same index was up
mid-single-digits. The pattern is not luck. It is the structural
signature of *trend-following* — the strategy that almost the entire
quantitative CTA industry runs in some form.

You need to understand managed futures for four reasons:

1. **It is the only systematic strategy with reliable crisis
   convexity.** Tail-hedging via puts (Week 47) buys explicit
   convexity for a known premium drag. Trend-following *manufactures*
   convexity from price action: as markets break down it goes short,
   so a sustained bear market is exactly when its P&L compounds.
   Different mechanism, similar shape, much smaller carry cost.
   That is rare enough that it deserves its own sleeve in any
   serious portfolio.

2. **It is genuinely uncorrelated to stocks and bonds.** The CTA-vs-
   S&P long-run correlation is roughly zero, with the *conditional*
   correlation turning sharply negative in extended drawdowns. This
   is the property the 60/40 lost in 2022 and that bonds lost in
   2008-by-default. A barbell only works if the two
   ends are actually different. CTAs are the cleanest "different"
   you can buy in liquid public markets.

3. **It is now retail-accessible at institutional cost.** For three
   decades trend-following was 2-and-20, $5M minimums, gated.
   Today DBMF, KMLM, FMF, and AHLT replicate the SocGen CTA Index at
   roughly 0.85 to 0.95% all-in expense ratios with daily liquidity.
   The fee compression is the single biggest change in liquid
   alternatives over the last five years.

4. **It is the textbook L5 alpha sleeve.** Of the small handful of
   places alpha can come from, trend-following is the most empirically
   validated at the *systematic* end (alongside size and
   value), with out-of-sample evidence going back to 1880 across
   futures markets that did not yet exist when the studies were
   funded. The strategy is not a secret — and it still works, because
   the source of the return (the volatility tail wagging the dog plus
   cross-asset momentum) is hard for marginal capital to arbitrage
   away without accepting the same drawdowns CTAs accept in chop
   markets.

This week's job is to wire that into a portfolio, not just to admire
it from a distance.

---

### 2. What You Need to Know

#### 2.1 What "Trend-Following" Actually Is

A textbook trend-follower is a rules-based system that goes long an
asset when its recent return is positive and short when it is
negative, sized inversely to that asset's recent volatility. The
canonical version is *time-series momentum*: at month-end, for each of
roughly 50–80 liquid futures contracts (S&P, Nasdaq, FTSE, JGB, Bund,
US 10-year, EUR, JPY, gold, copper, crude, corn, …), compute the
12-month total return; if positive, hold a long position; if negative,
hold a short. Each contract is sized so that it contributes the same
*risk* in volatility units to the portfolio. Lookbacks are usually a
blend (1-month, 3-month, 12-month) and the trade is rebalanced daily
or weekly.

That is the entire algorithm. There is no forecast of fundamentals,
no view on Fed policy, no DCF. The strategy says: *if this thing has
been going up, ride it; if it has been going down, ride that too*.
It is momentum applied across asset classes, with the
key innovation being that the universe is not just stocks. When
stocks fall and bonds rally and the dollar squeezes and crude tanks,
all four trades line up in the same direction, and the convex payoff
in a crisis is the sum of those four legs.

#### 2.2 The "Crisis Alpha" Pattern

Sébastien Page and the AQR research team coined the phrase *crisis
alpha* for what trend-following does in extended bear markets. The
mechanism is mechanical: most large equity drawdowns are not single
days — they are *trends*. The S&P 500 drawdown of 2007–2009 played
out over 17 months. The 2000–2002 drawdown over 31 months. 2022 over
9 months. Trend-followers caught all three, because each of those
drawdowns was preceded by a regime in which most futures across asset
classes were trending in the same direction long enough for the
12-month signal to flip and the position to size up.

The flip side is sideways or chop markets, which are bad for trend.
2011-2015 was the longest stretch of CTA underperformance in
40 years — five years of roughly zero return while equities ran 70%.
2014 was the redemption year (commodity trends finally re-engaged),
2015 was flat, 2016-2019 mixed. Then 2022 paid back the entire
2011-2019 gap in a single year for the index.

![Time-series chart of the SocGen CTA Index from 2000 through 2024 with the S&P 500 total return overlaid. Strong CTA years are highlighted: 2002 +18%/SPX -22%, 2008 +13%/SPX -37%, 2014 +16%/SPX +14%, 2022 +21%/SPX -18%. Chop/loss years for CTA also marked: 2011 -4%, 2015 ~0%, 2018 -3%, 2020 +2%/SPX +18%. The two lines weave around each other with low unconditional correlation but sharply negative conditional correlation in extended bear markets — the structural signature of crisis alpha. Five years of chop are paid back by one big trending crisis year.](image/week51_cta_history.png)

That is the deal: in calm markets you pay a small or zero opportunity
cost; in extended trending crises you get paid a multiple of your
allocation. The few months that matter dominate the long-run
return distribution, and trend-following is structurally *long* those
months.

#### 2.3 The SocGen CTA Index and What "Average CTA" Means

The SocGen CTA Index (formerly Newedge CTA Index) is the industry
benchmark: equally-weighted composite of the 20 largest reporting CTA
managers, rebalanced annually, AUM-weighted in older versions. It
goes back to 2000. The trend-following sub-index goes back to 2000
as well, but proxy series stitched from BarclayHedge and other
databases extend the picture to 1990.

A few calendar-year landmarks since 2000:

| Year | SocGen CTA | S&P 500 (TR) | Notes |
|---|---:|---:|---|
| 2002 | +18.3% | −22.1% | dot-com tail, USD weakness, bond rally |
| 2008 | +13.1% | −37.0% | crisis alpha, all asset trends |
| 2011 | −4.4%  | +2.1%  | euro-debt chop, no follow-through |
| 2014 | +15.7% | +13.7% | dollar surge, oil collapse, JGB rally |
| 2015 | 0.0%   | +1.4%  | reversal year, wrong-footed in Q3 |
| 2018 | −2.9%  | −4.4%  | feb Volmageddon + Q4 chop |
| 2020 | +1.9%  | +18.4% | COVID round-trip neutralised trend |
| 2022 | +20.5% | −18.1% | dollar/rates/energy all trending |

The arithmetic mean since 2000 is roughly 4–5% with about 10–11%
volatility — Sharpe a hair under 0.4. That is *much lower* than US
equities' Sharpe, and that is the point: you are not buying CTAs for
return-density. You are buying them for the *shape* of the return,
specifically the negative-correlation-when-it-matters property.

#### 2.4 Capacity, Fees, and the Retail Vehicles

Until ~2019 the only way to buy this strategy was a direct allocation
to a CTA fund: $1M to $5M minimums, 1+10 to 2+20 fee schedules
(typical: 1.5% management + 17.5% performance), monthly liquidity at
best. The good systematic CTAs (AHL, Winton, Aspect, Campbell,
Graham, Millburn, Transtrend) ran tens of billions and delivered the
bulk of what the index showed.

The 2019 launch of DBMF (iMGP DBi Managed Futures Strategy) was the
inflection. The fund replicates the SocGen CTA Index using a
40-factor regression on the index returns themselves, then runs a
mirror portfolio of liquid futures that targets the same factor
loadings. The result is roughly 0.85% all-in (no performance fee, no
lockups), daily liquidity, 1099 reporting (no K-1), Section 1256
60/40 capital gains tax treatment on the futures sleeve.

The current retail CTA menu, April 2026:

| Ticker | Vehicle | ER | AUM | Style |
|---|---|---:|---:|---|
| **DBMF** | iMGP DBi Managed Futures | 0.85% | ~$1.6B | Index-replication of SocGen CTA |
| **KMLM** | KFA Mount Lucas Managed Futures | 0.92% | ~$0.6B | Long-only-trend on commodities-FX-rates |
| **FMF**  | First Trust Managed Futures | 0.95% | ~$0.3B | 50/30/20 equity/comm/FX trend |
| **AHLT** | AHL Trend ETF (Man Group) | 0.95% | ~$0.4B | Direct-from-AHL trend, multi-tenor |
| **AQR Managed Futures (mutual fund)** | QMHIX/QMHRX | 1.18% | ~$3.8B | AQR full-strength trend, mutual-fund wrapper |

The mutual fund version of AQR's strategy (QMHIX) is the closest
thing to "buy AQR's trend desk in your IRA." DBMF is the cheapest
proxy for the index average. KMLM has the longest standalone live
record of the ETFs (since 2020). For most investors at the start, a
single position in DBMF or KMLM at 10–15% of portfolio is the right
default.

#### 2.5 Why Trend Is "Long-Vol" Even Though It Buys No Options

A trend-follower never buys a put or a call. It also has no
convexity built into a single trade — a long futures position is
linear in the underlying. The convexity comes from the *signal*: as
prices move enough, the position is added to (more long if rallying
hard, more short if collapsing). If a drawdown lasts long enough
for the signal to flip from long to short, the realised P&L on the
short position grows quadratically with the size of the move — same
qualitative shape as a put.

The mathematical sketch: if you imagine a perfect trend-follower that
always holds the right sign at every instant, the P&L is the integral
of |dS|, which is path-dependent and dominated by big moves. That is
the signature of a long-straddle — a long volatility position. Trend-
following synthesises a straddle out of price changes, paying for it
in chop markets (when the signal whipsaws) rather than option
premium (when the underlying drifts).

Practical implication: trend-following is *correlated* to realised
volatility, not implied volatility. It does badly when realised vol
collapses (2017, 2019), well when realised vol stays elevated and
*directional* (2022). In years with high implied vol but no follow-
through (2018), it can lose despite VIX being elevated.

#### 2.6 Where Trend Sits in the Four-Tranche Framework

Slot the strategy into the four-tranche structure:

| Tranche | Target | Role of CTA sleeve |
|---|---:|---|
| **Growth** (60–70%) | Stocks: VTI, factor tilts | unchanged |
| **Income** (10–20%) | Bonds, JEPI, MLPs | unchanged |
| **Stores of Value** (5–15%) | Gold, T-bills, USD cash | partially overlaps with CTA |
| **Opportunistic / Tactical** (5–15%) | **CTA + tail hedges + alt sleeves** | here |

For a 100k portfolio with the L5 default 80/10/10/0:
- 80k VTI/VOO,
- 10k bonds,
- **10k DBMF or KMLM** as the "stores of value plus opportunistic"
  blend,
- 0–5k SPY OTM puts if you want explicit tail (Week 47).

A more aggressive split is 70/10/15/5 with the 15 being entirely CTA.
That is approximately the AQR house-portfolio recommendation for
endowment-style mandates.

![Cumulative-wealth chart of three portfolios from 1990 through April 2026, all starting at $1: 100% S&P 500 (highest terminal wealth, but worst drawdowns at -51% in 2009 and -24% in 2022), classic 60/40 stocks/bonds (middle terminal, drawdowns -30% / -20%), and a 50/30/20 split with 20% in a synthetic CTA proxy (slightly below 60/40 on terminal wealth but the *best* drawdown profile of the three at -22% / -10%). The CTA-blend portfolio's wealth path is the smoothest of the three. The chart is the empirical case for a 10-15% CTA sleeve — same long-run shape as 60/40 but with roughly half the worst-year pain.](image/week51_60_40_with_cta.png)

The wealth-path chart shows the empirical reason. From 1990 to April
2026 a 100% S&P portfolio compounds to the highest terminal value
but has the worst drawdown profile (−51% in 2009, −24% in 2022). A
60/40 has lower terminal but a less severe drawdown (−30% / −20%).
A 50/30/20 with 20% in a synthetic CTA proxy lands between the two
on terminal wealth but with the *best* drawdown profile of the three
(−22% / −10%) — exactly what you would expect from a sleeve with
−0.2 unconditional correlation that goes more negative in crashes.

#### 2.7 Sizing, Fees, and the Behavioural Trap

Three rules of thumb I have used myself:

1. **Size for the chop, not the crash.** The right question is
   "how big a position can I hold in 2015 when this returns 0% for
   the year while my friends are up 20% in stocks?" If your answer
   is 5%, hold 5%. If you size for the 2008-style payoff and then
   redeem in the chop, you get the worst of both worlds.

2. **Pick one ETF and hold it.** Switching from DBMF to KMLM to
   AHLT based on YTD performance is a disaster — you are buying the
   manager who just had the lucky year. The dispersion across CTA
   indices in any given year is tiny (most are within 3% of each
   other) so the choice does not matter as much as the stickiness.

3. **Treat the carry as a permanent cost.** The strategy can have
   3-year stretches of zero return. If you are not prepared to wear
   that, the position is not the right one for you. Better to size
   smaller and never sell than to size big and capitulate.

The behavioural trap is identical to the one with tail hedges (Week
47): the strategy looks broken right when it is closest to paying
off. Markets stay irrational longer than you stay solvent — that
applies to the *holder* of the hedge as much as it does to the trader
on the other side of one.

---

### 3. Common Misconceptions

1. **"CTAs don't work anymore — the trend factor is dead."** The
   2011–2019 stretch made this a popular thesis. Then 2022 happened
   and the index returned 20%+ for the year, on the same model the
   "dead" critics were criticising. The trend signal is structurally
   tied to drawdown duration, and drawdowns have not stopped.

2. **"It's the same as just buying VIX or puts."** No. VIX/UVXY are
   long *implied* vol; trend is long *realised* vol. They behave
   differently in a 2018-style implied-vol shock without follow-
   through (UVXY +200% in February, trend −2%). Tail puts pay on
   speed; trend pays on duration.

3. **"It's a hedge — so it should always make money in a bad year."**
   No. It needs the bad year to be a *trend*, not a single-day or
   single-week shock. February 2018, August 2015, August 2024 are
   all years CTAs lost money in equity-stress months because the
   move was too fast for the signal to engage.

4. **"DBMF / KMLM should track AQR's mutual fund tightly."** They
   target the *index* (SocGen CTA), not any one manager, so manager
   dispersion shows up as tracking error. The right benchmark is the
   index, not another product.

5. **"You can replace your bond allocation with CTAs."** Bonds and
   CTAs are diversifiers in different regimes — bonds in
   deflationary/growth shocks (2008, 2020), CTAs in stagflationary/
   trending shocks (2022, 1970s). A mature portfolio carries some of
   each, not just one.

6. **"The fees aren't worth it — I should run trend myself."** You
   *can*, on the micro futures (Week 39 — /MES, /MNQ, /MCL, /MGC).
   The capital required to run 30 contracts at the right vol-target
   is roughly $300k+, the bookkeeping is daily mark-to-market, and
   the operational risk is real. For most retail allocations DBMF at
   85bp is the right call.

7. **"It worked in 2008 because of the GFC — that won't happen
   again."** It worked in 1973–74, 2000–02, 2008, 2014 dollar
   shock, 2020 COVID, 2022 inflation regime change. That is six
   distinct macro environments over 50 years. The mechanism — long-
   duration trends across uncorrelated markets — has not been
   regime-specific.

8. **"Trend is 'short gamma' because it sells into rips."** No. Trend
   buys strength and sells weakness — that is *long* gamma in the
   options-Greek sense. The whipsaw cost in chop is the gamma cost
   you pay every period for the convex payoff in a sustained move.

9. **"I can just hold managed futures inside a 60/40 fund."** Mutual
   funds with "managed futures" sleeves often run 5–10% allocations
   that are too small to move the line. To get the 2008/2022-style
   convexity you need 15–20% in a *pure* CTA, not a slice of a
   target-date fund.

---

### 4. Q&A Section

**Q: How big should the CTA sleeve be?**
A: For a default L5 portfolio, 10–15% is the right range. The lower
end is a hedge, the upper end starts to *materially* change the
drawdown profile. Above 20% you are actively expressing a trend-
follow-as-a-return-source view, which is fine but requires more
conviction in chop years.

**Q: DBMF, KMLM, FMF, or AHLT?**
A: Default DBMF for the cheapest index replication, KMLM if you want
a slightly longer-only-commodity tilt, AHLT if you want direct AHL
exposure. The dispersion among them is small in most years.

**Q: What about AQR's QMHIX mutual fund?**
A: It is the most "pure" version (full-strength AQR trend, no ETF
replication overlay), but ER is 1.18% and minimums apply at some
brokerages. For tax-deferred accounts (IRA, 401k where available),
QMHIX is excellent.

**Q: Section 1256 tax treatment — does it pass through DBMF?**
A: Yes. DBMF holds futures directly; gains are 60% LTCG / 40% STCG
regardless of holding period at the fund level, and that flows
through to your 1099 (no K-1). This makes CTAs tax-efficient even
in taxable accounts.

**Q: Does CTA pair well with my SPX-puts tail hedge from Week 47?**
A: Yes — they are complements, not substitutes. Puts pay on a fast
shock (March 2020); CTA pays on a sustained trend (2022). A 5-15%
CTA + 0.5-1% puts-rolled-quarterly is a robust crisis-convex sleeve.

**Q: What's the worst-case scenario for trend-following?**
A: Sharp reversal at the end of a long trend — September-October
2008 caught some funds wrong-side as commodities collapsed faster
than positions could flip; February 2018 caught funds long after
years of low-vol uptrend. Three- to nine-month drawdowns of 10-15%
are normal. Drawdowns of 20%+ have happened roughly once a decade.

**Q: Should I rebalance the CTA sleeve?**
A: Yes — annually or at 5%-band thresholds, like any other sleeve.
Rebalancing into a CTA in a chop year (say end-2015 or end-2019) is
exactly when it has historically been most additive going forward.

**Q: What about long-only commodities — same thing as CTA?**
A: No. Long-only commodities (DBC, PDBC) are passive futures
exposure with roll cost (Week 39). CTA can go *short* commodities,
which is the entire point. In 2014 commodities fell 30%+ and CTAs
made money on the short leg; long-only got crushed.

**Q: Is the strategy "crowded"?**
A: Total CTA AUM is about $400B globally, vs $50T+ in liquid global
futures markets. The market-impact cost of the strategy is real but
manageable, and academic studies (Hurst-Ooi-Pedersen 2017, AQR 2022
update) find no decay in the trend factor through 2024. Still
working, even after the audit.

**Q: How does CTA fit with private alts / hedge funds in a fancy
portfolio?**
A: Most institutional portfolios already have CTA via their hedge-
fund sleeve, and may double-count. The Yale endowment, for example,
holds ~25% in absolute-return / hedge funds, of which a meaningful
fraction is trend-style. For retail, DBMF at 10-15% replicates that
exposure cleanly.

**Q: Why does the SocGen CTA Index look so much better than the
HFRI Macro Index?**
A: HFRI Macro mixes discretionary global macro (which has
underperformed for a decade) with systematic trend. SocGen CTA is
the trend-only sub-index. Same reason the SP500 looks better than
"all stocks" — composition matters.

**Q: What's the interactive for this week?**
A: A blender. Slide your % to S&P, bonds, and CTA; it backtests
against real annual returns 1990-2024 plus the synthetic CTA proxy
and shows you CAGR, vol, Sharpe, max drawdown, the 2008 and 2022
calendar returns, and the correlation matrix. The point is to
*see* what the −22% 60/40 of 2022 turns into when you swap 20% of
it into a CTA proxy. Spoiler: roughly −5%.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Why Every Serious Portfolio Should Have 10-15% in Managed Futures
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**INTRO**

**Horace:** [open] Stella, what was the worst calendar year for a
60/40 portfolio in the last fifty years?

**Stella:** Most people say 2008. The right answer is 2022.

**Horace:** 2022. Down 18% on stocks, down 13% on bonds — the
diversifier broke. 60/40 lost about 17% inflation-unadjusted, 22%
real. That is the worst year for the textbook portfolio since 1937.

**Stella:** And in the same year, one strategy made over 20%.

**Horace:** The SocGen CTA Index — managed futures, trend-following.
That is what we are talking about today: the alpha sleeve that
actually works in the year nothing else does.

**SECTION 1 — What Is It**

**Horace:** Trend-following is the simplest systematic strategy in
finance. For each of about 50 to 80 liquid futures contracts —
S&P, Nasdaq, US 10-year, gold, crude, currencies — you compute the
trailing 12-month return. Positive: go long. Negative: go short.
Size each so each contract contributes the same volatility-dollars
to the portfolio. Rebalance daily or weekly. That is the whole
algorithm.

**Stella:** No fundamentals. No Fed-watching. No DCFs.

**Horace:** Pure price action. Momentum applied across
asset classes instead of just stocks. The reason the universe
matters is what makes the strategy diversifying. When stocks go
down, bonds rally, dollar squeezes, oil tanks, all four trends line
up in the same direction in a crisis, and the convex payoff is the
sum of those legs.

**SECTION 2 — The History**

**Horace:** [VISUAL: image/week51_cta_history.png] Here is the
SocGen CTA Index from 2000 through 2024 with the S&P overlaid. Look
at the highlighted bars.

**Stella:** 2008 — CTA up 13, S&P down 37. 2014 — CTA up 16. 2022 —
CTA up 20, S&P down 18.

**Horace:** Those are the strong years. Now look at the red ones.
2011 — CTA down 4, S&P up 2. 2015 — flat. 2018 — down 3.

**Stella:** Those are the chop years. No follow-through, signal
whipsaws.

**Horace:** That is the deal. Five years of chop for one year of
crisis-alpha that pays back the entire gap. The few
months that matter dominate the long-run distribution, and trend-
following is structurally on the right side of those months when
they unfold over quarters.

**SECTION 3 — Why It Pays in a Crisis**

**Stella:** The mechanism, in one sentence?

**Horace:** Most large equity drawdowns are not single days. They
are trends. 2008 played out over 17 months. 2000-02 over 31. 2022
over 9. Every one of those gave the 12-month signal time to flip
from long to short, and the position grew with the move. That is
the convexity. Not bought, manufactured.

**Stella:** And it fails when?

**Horace:** Fast shocks. February 2018 — minus 10 in two weeks
then back. August 2024 — yen carry unwind, four-day spike, gone.
Trend needs duration. Tail puts pay on speed; trend pays on
duration. They are complements.

**SECTION 4 — The Wealth Path**

**Horace:** [VISUAL: image/week51_60_40_with_cta.png] 1990 to April
2026, three portfolios. 100% S&P, 60/40, and a 50/30/20 — half
stocks, 30 bonds, 20 in a synthetic CTA proxy at 6% mean and 11%
vol, correlated minus 0.2 with stocks.

**Stella:** S&P wins on terminal wealth.

**Horace:** As it should — equity risk premium is what compounds.
But look at the drawdowns. S&P has minus 51 in 2009, minus 24 in
2022. 60/40 has minus 30 and minus 20. The 50/30/20 with CTA has
minus 22 and minus 10.

**Stella:** Same shape, half the pain.

**Horace:** That is what diversification is supposed to do. The
60/40 lost the property in 2022 because bonds correlated with
stocks. The CTA sleeve restored it.

**SECTION 5 — The Vehicles**

**Stella:** Until 2019 you needed five million dollars and a fund
manager.

**Horace:** Today: DBMF, 0.85% expense ratio. KMLM, 0.92. AHLT,
0.95. FMF, 0.95. All ETFs, daily liquidity, 1099 reporting, Section
1256 tax treatment. The futures sleeve gets 60/40
capital gains tax regardless of holding period.

**Stella:** Picking among them?

**Horace:** Default DBMF — index replication, cheapest. KMLM if you
want a commodity tilt. AHLT for direct AHL exposure. AQR's QMHIX
mutual fund inside a tax-deferred account if you want full-strength
trend. The dispersion across them is small in most years. The
behavioural trap is switching. Don't switch.

**SECTION 6 — Sizing**

**Horace:** [VISUAL: interactive/week51_cta_blender.html] Open the
blender. Three sliders — S&P, bonds, CTA. Sum to 100.

**Stella:** Default L5 is 80/10/10/0. So slide to 70/15/15.

**Horace:** Look at the numbers. CAGR roughly 9.2 vs the all-equity
10.4. Vol 11.8 vs 16.1. Max drawdown 28 vs 51. Sharpe 0.55 vs 0.50.
2008 calendar return: minus 12 vs minus 37. 2022: minus 5 vs minus
18.

**Stella:** Lower return.

**Horace:** Slightly. But the *risk-adjusted* return is higher and
the drawdown is half. That is the trade. The right end of a
barbell is convex small allocations that pay
asymmetrically in stress. CTA is one of the cleanest versions of
that available in liquid markets.

**SECTION 7 — The Three Sizing Rules**

**Stella:** Three rules?

**Horace:** One — size for the chop, not the crash. If you cannot
hold this in 2015 when stocks are up 20 and CTA is flat, hold
less. Two — pick one ETF and stick. Switching after a bad year is
buying the manager who just got lucky. Three — treat the carry as a
permanent cost, like an insurance premium. If you would not pay 1%
a year for a tail-risk hedge, you will not be happy holding CTA in
a chop year.

**Stella:** Same idea — markets outlast solvency.

**Horace:** Markets stay irrational longer than you stay solvent —
applies to the holder of the hedge as much as the speculator on the
other side of it.

**SECTION 8 — Misconceptions**

**Stella:** Top two.

**Horace:** One — it is not the same as buying VIX or puts. VIX is
implied vol; trend is realised vol. Different beast. Two — it does
not always make money in a bad equity year. It needs the bad year
to be a *trend*. February 2018 was a 10% shock with no follow-
through, and trend lost.

**Stella:** Three — bonds versus CTA.

**Horace:** Different regimes. Bonds work in deflationary growth
shocks — 2008, 2020. CTA works in trending stagflationary shocks —
2022, 1970s. Mature portfolio carries some of each.

**OUTRO**

**Horace:** Final line. Of the small handful of sources of alpha,
trend-following is the most empirically validated at the systematic
end, with out-of-sample evidence going back to 1880
across futures markets that did not yet exist when the studies
were funded. The strategy is not a secret. It still works. The
reason it still works is because the source of return — long-
duration trends in macro markets — is hard for marginal capital to
arbitrage away without accepting the same chop-year drawdowns CTAs
accept.

**Stella:** And the simplest implementation is one ticker.

**Horace:** DBMF. Ten percent of the portfolio. Hold it.

**Stella:** That's a wrap.
