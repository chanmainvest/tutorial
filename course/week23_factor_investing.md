# Week 23: Factor Investing — Value, Momentum, Quality, Low-Vol, Size

---

## Part 1: Reading Section

---

### 1. Why This Is Important

For half a century the Capital Asset Pricing Model (CAPM) told a single
story: stocks beat bonds because stocks carry more market risk, and the
*only* thing the market rewards is bearing that one risk. One factor.
One reward. End of equation. Then in the early 1990s Eugene Fama and
Kenneth French sat down with sixty years of CRSP data and discovered
that the equation was missing terms. Small companies beat big ones by
more than their beta. Cheap (high book-to-market) stocks beat expensive
ones. Once they added a *size* factor and a *value* factor the residual
"alpha" of most US mutual funds collapsed — what looked like
stock-picking skill was, on the data, just systematic exposure to
factors the manager had never named. By 2015 Fama and French had added
*profitability* (RMW) and *investment* (CMA), and Mark Carhart had
bolted on *momentum* (UMD) into a six-factor framework that today
explains roughly 90% of the cross-section of US equity returns.

This matters for four reasons.

1. **It tells you what your portfolio actually is.** Whatever you
   own — a single mutual fund, a 60/40 mix, your spouse's "growth
   stock" picks — has factor loadings whether you measure them or
   not. Two portfolios with the same beta and the same expected
   return can behave very differently in the next regime if one is
   heavy on value-and-size and the other is heavy on quality-and-low-vol.
   Factors are how you read what's under the hood.

2. **It separates structural alpha from luck.** When a manager beats
   the S&P by 3% over a decade, the right question isn't "are they
   good?" — it's "what factor was that?" If their excess return loads
   onto small-value, you can replicate it with VBR for 7 bps of fee.
   If it loads onto momentum, you can replicate it with MTUM. The
   moment a putative "skill" fits inside an academic factor it stops
   being skill.

3. **It is one of the durable structural alpha lanes.** Among the
   handful of structural mispricings worth chasing — liquidity,
   sector rotation, long-term trends, buying what passive flows have
   abandoned, and the academic factor premia we're discussing this
   week — factors are the most *systematic* and the most *crowded* —
   which means they have the lowest barrier to entry and the most
   compressed forward expected return. They still pay; they just pay
   less than they did before everyone owned VLUE and MTUM.

4. **It frames the 2007 quant quake we covered in Week 14.** When
   AQR, Renaissance, and a hundred lesser stat-arb shops were all
   running the same factor signals on the same universe, a single
   mid-August deleveraging event vaporised three years of returns
   in four days. Factor investing with leverage was the canonical
   case study in *crowded-trade* risk. Retail factor ETFs in 2026
   are unleveraged, so the blow-up math is gentler — but the
   compression of premiums is the same disease.

---

### 2. What You Need to Know

#### 2.1 What a "factor" actually is

A factor is a *long-short portfolio* built from a measurable stock
characteristic. Take book-to-market: rank every US stock by B/M, go
long the top decile, short the bottom decile, weight the legs equally,
rebalance monthly. The monthly P&L of that portfolio is the *value
factor* (HML — High Minus Low book-to-market). Every factor in the
academic literature has the same shape: rank, long top, short bottom,
hedge out the market.

That construction matters, because the long-short structure is what
strips out the market. A pure value mutual fund is roughly *0.9 of
market + 0.4 of HML + noise*; the academic HML is the *0.4 of HML*
piece on its own, with the market dialled to zero. The factor
*premium* is the average return of that long-short portfolio. Six
factors dominate the modern literature: market (MKT-RF), size (SMB —
Small Minus Big), value (HML), profitability (RMW — Robust Minus
Weak), investment (CMA — Conservative Minus Aggressive), and
momentum (UMD — Up Minus Down). The first five are Fama-French 5;
adding UMD gives you the FF5 + momentum framework that almost every
sell-side risk model in 2026 starts from.

![Factor premia 1963-2024](../image/week23_factor_premia.png)

#### 2.2 The historical premia, in one breath

From July 1963 to December 2024, the realised annualised premia for
the US factors are roughly: MKT-RF ~6.6%, UMD ~7.5%, HML ~3.8%, CMA
~3.3%, RMW ~3.0%, SMB ~2.4%. Add a low-volatility factor (not in the
official Fama-French set but built the same way: long bottom-quintile
beta, short top-quintile beta) and you get roughly 1-2% of premium
*with materially lower standard deviation* — which is why low-vol
shows up well on a Sharpe-ratio basis even though the raw premium
looks small.

A few orderings on this list are surprising. Momentum, the only
factor that didn't come out of Fama-French's stable, has the largest
premium of any of them — and the worst single drawdown. Size, the
factor that started the whole literature, is the *smallest* premium
and arguably indistinguishable from zero post-2000 once you adjust for
microcap illiquidity. Value, the factor your wealth manager probably
mentions first, is middle-of-the-pack and has *flatlined for the last
seventeen years*.

#### 2.3 The factor-decay problem since 2003

Pull up the rolling 10-year HML premium and you'll see something
ugly: it averaged about +5% per year from 1963 to roughly 2002, then
fell off a cliff. The rolling 10-year ending in 2020 was *negative*.
Between 2008 and 2020, the academic value factor — the long-short
construction, not value mutual funds — lost money on average. UMD
has its own version of the same disease, with a different shape: a
long mean of 7-8% interrupted by the *2009 momentum crash*, when the
factor drew down roughly 45% in calendar 2009 (and ~83% peak-to-trough)
as the market V-bottomed and previously losing junk stocks ripped
higher off the lows.

![Rolling 10-year HML and UMD premium](../image/week23_factor_decay.png)

There are three competing explanations for why the premia have
compressed, and they're probably all true. First, *publication
arbitrage*: every academic factor that gets written up in the JoF
attracts capital, and that capital bids up the long leg and sells
down the short leg until the premium shrinks. The peer-reviewed
finding is the obituary of the trade. Second, *intangibles
mis-measurement*: book-to-market punishes asset-light tech firms
that show low book equity *because* their value is in non-capitalised
R&D and brand. The HML construction reads them as "expensive" when
on a corrected basis they're not. Third, *post-GFC central-bank
liquidity*: zero rates compress dispersion across stocks. Everything
trades together; nothing trades on fundamentals; nothing is cheap or
expensive any more. Pick whichever theory you like — the empirical
fact is that the premium has roughly halved versus its pre-2003 mean.

#### 2.4 The 2007 quant quake — what factor crowding actually feels like

The week of August 6, 2007 is the textbook example of factor
crowding, and we covered it in detail in Week 14 from the
pair-trading angle. Here's the factor-investing version. Every
quantitative long-short shop in 2007 was running essentially the
same factor portfolio: long value, long momentum, long quality,
short the opposite, leveraged 5-8x for risk-target purposes. On
August 6 *something* — most plausibly a multi-strat fund forced to
deleverage to meet redemptions in its credit book — started
unwinding the standard factor portfolio in size. Because *every other
quant fund held the same book*, the unwind didn't find counterparties
in the way an idiosyncratic position would; it found a hundred funds
all running the same risk model and all stopping out at roughly the
same loss threshold, all at the same time. By Friday August 10 the
standard factor portfolio had drawn down about 25% — three years of
realised premium gone in four trading days. The market itself moved
about 1%. The retail tape never noticed.

Two lessons survive from that week. First, *factor exposure is risk
even when the factor's beta to the market is zero*. The risk you took
wasn't market risk; it was crowded-trade risk. Second, *unleveraged
factor exposure is a different animal*. Retail factor ETFs in 2026
have no leverage and no daily VaR-driven stop-out. They can sit
through a quant unwind and just take the temporary mark. The blow-up
math is mostly a leverage-and-redemption problem, not a factor
problem per se.

#### 2.5 The retail factor ETF menu in 2026

The factor literature got cheap and scalable. iShares and Vanguard
between them now run the standard menu of single-factor ETFs at
expense ratios between 8 and 25 bps:

- **VLUE** (iShares MSCI USA Value Factor) — value tilt, 0.08% ER.
- **MTUM** (iShares MSCI USA Momentum Factor) — momentum tilt, 0.15% ER.
- **QUAL** (iShares MSCI USA Quality Factor) — RMW-flavoured quality
  tilt, 0.15% ER. Largest of the bunch by AUM.
- **USMV** (iShares MSCI USA Min Vol Factor) — low-volatility tilt,
  0.15% ER.
- **IWM / IJR** (iShares Russell 2000 / S&P SmallCap 600) — size
  tilt via small-cap exposure, 0.19% / 0.06% ER.
- **AVUV / AVDV** (Avantis US / International Small Value) —
  combined size+value+profitability tilt, 0.25% ER. The 2020s
  flagbearer of the academic-factor school.

You can build a respectable multi-factor blend with four of these
tickers, total expense ratio under 0.20%, and you've replicated what
hedge funds were charging 2-and-20 for in 2003. The premium has
compressed, but so has the cost of harvesting it — and the *net*
premium (gross minus fee minus tax drag) is roughly the same as it
was for the leveraged hedge funds twenty years ago, because the fee
compression has roughly matched the premium compression. Cheap beta
ate expensive alpha.

#### 2.6 Where this fits in the bigger picture

Factor investing is the most *structural* of the available alpha
lanes — and the *least* idiosyncratic. It scales infinitely (any
size of capital can run it), it requires no special information, and
the academic literature documenting it is freely available on SSRN.
That's also exactly why the premium has compressed: anything anyone
can run, eventually everyone runs. Compare that to "buying what
passive flows have abandoned" (the contrarian sector trade): that
*requires* discomfort, requires being early, requires holding through
a period when nobody else does. The factor trade requires only that
you click VLUE and forget about it. The market is efficient at
arbitraging away premium that requires no discomfort to capture.

The implication for your own book: factors belong in the *passive
core* (the foundational, lowest-active tranche), not in the *active
sleeve*. A modest tilt — 10-20% of your equity allocation in QUAL or
AVUV
versus a market-cap-weighted core — gets you most of the diversification
benefit without taking concentrated factor-blow-up risk. Putting 100%
of your equity in MTUM is taking the 2009-style tail risk; putting
10% in MTUM and 90% in VTI gets you 80% of the long-run mean and
20% of the tail.

---

### 3. Common Misconceptions

1. **"Factor investing is the same as value investing."** Value is
   one factor of six. The Fama-French framework is a *system*: each
   factor is a separate long-short portfolio, and a "factor
   investor" usually owns several of them. Calling factor investing
   "value" is like calling exercise "running."

2. **"The size factor has a big premium."** SMB has the *smallest*
   realised premium of the headline factors, around 2.4% annualised.
   Most of the gap shows up only in the bottom microcap quintile,
   which has serious illiquidity issues. The "small-cap effect" you
   hear about is mostly a small-*value* effect — value, not size,
   doing the work.

3. **"Momentum is just the trend-following you read about in the
   1990s."** The academic UMD factor is *cross-sectional*: rank stocks
   by their past 12-month return (skip the most recent month), go long
   the winners, short the losers, monthly rebalance. Trend-following
   in commodities is *time-series*: long if the asset itself is up,
   short if it's down. Different construction, different correlation,
   different drawdown profile.

4. **"Factors are dead — they don't work any more."** The premia have
   compressed, not disappeared. Even at half their pre-2003 means, a
   four-factor multi-factor blend has positive expected excess return
   net of fees in 2026. What's *dead* is the leveraged-quant version
   from 2007 — the unleveraged retail-ETF version is alive but smaller.

5. **"More factors is always better."** The literature has identified
   over 400 "factors" in published papers, most of which fail to
   replicate out of sample. The Fama-French 5 plus momentum is the
   conservative consensus. Anyone selling you exposure to a 20-factor
   model is selling overfit.

6. **"Low-vol works because low-vol stocks are mispriced."** Maybe
   partly, but mostly low-vol works because of *leverage aversion*:
   most institutional investors can't lever, so to get equity-like
   returns they crowd into high-beta stocks, bidding their prices up
   and their forward returns down. Low-beta stocks get under-bid as a
   result. Take away leverage constraints and the premium would
   shrink — which is partly why hedge-fund "betting against beta"
   strategies have done well.

7. **"Quality and low-vol are the same factor."** They overlap (quality
   companies tend to be lower-vol) but diverge in stress: in 2008-09,
   USMV-style low-vol got hammered along with everything else as
   correlations went to 1, while QUAL-style quality (high ROE, low
   debt) outperformed. Different definitions, different risk shapes.

8. **"I should rebalance my factor blend monthly to capture the
   premium."** Monthly rebalancing for a *single* factor (the academic
   construction) is correct. For a *multi-factor blend* held in retail
   ETFs, monthly rebalancing has a tax cost that often exceeds the
   rebalancing benefit. Annual rebalance is a defensible compromise
   for taxable accounts.

9. **"The 2007 quant quake means factor investing is dangerous."**
   The 2007 event was about *leverage* and *redemption-driven
   deleveraging*, not factors per se. An unleveraged retail factor
   blend in a taxable account doesn't have the same blow-up topology.
   The risk is *forgone return* (factors compress further), not
   *catastrophic loss*.

10. **"If everyone knows about factors, the premium should be zero."**
    The premium *has* halved since 2003, which is the strong-form
    version of "everyone knows." It hasn't gone to zero because (a) a
    lot of capital still cares more about benchmark tracking than
    about factor exposure, and (b) some of the premium is
    risk-compensation that doesn't go away just because the risk is
    well-understood. The remaining premium is the residual after the
    arbitrageable portion has been arbed out.

---

### 4. Q&A Section

**Q1: Should I replace my S&P 500 fund with a multi-factor ETF?**
No — keep the cap-weighted core for cost, tax, and tracking-error
reasons, then *tilt* with 10-30% of your equity allocation toward
factors. The cap-weighted core gets you the market premium for almost
no cost; the factor tilt gets you the (compressed) factor premium on
top. Replacing the core with a factor product takes on tracking-error
risk you usually don't need.

**Q2: Which single factor is best?**
Long-run, momentum has the highest gross premium and the highest
volatility — so it has the worst tail (2009) and the best mean.
Quality has the best Sharpe ratio. Value has the best valuation case
in 2026 because it's the most beaten-down. Pick by your tolerance for
which kind of regret: missing-the-rally (avoid momentum) or
the-thing-keeps-getting-cheaper (avoid value).

**Q3: How long should a factor go through a drawdown before I quit?**
Long enough that the answer should be "I won't quit." HML drew down
for *thirteen years* from 2007 to 2020 before the 2021-22 value
rally. If you can't sit through a decade-plus drawdown of the factor
you tilted to, you don't have the conviction to harvest it; you'll
sell at the bottom and miss the rebound. If 13 years sounds
intolerable, *don't tilt* — own the cap-weighted index.

**Q4: Why is small-value (AVUV) so popular if size is a weak factor?**
Because the *interaction* of size and value (and profitability) is
where the literature still finds robust premium. Small *junk* stocks
underperform; small *value-with-profitability* stocks have a
materially better historical profile than either size or value alone.
AVUV is built around that interaction.

**Q5: Are factors correlated with each other?**
Some are highly correlated (HML and CMA), some are negatively
correlated (HML and UMD historically — value and momentum are partial
hedges for each other), and some are weakly correlated (SMB with
everything). A multi-factor blend gets diversification benefit
*because* the factors aren't perfectly correlated. The HML/UMD
negative correlation is the single most useful pairing for a retail
blend: when one is in a drawdown the other is often having a good
year.

**Q6: Does international factor investing work?**
The academic premia replicate internationally (developed and EM)
with similar magnitudes and similar 2003-2020 compression. We stay
US-only for *investability* reasons (FX, custody, tax,
information disadvantage), but the academic story is broadly
international, not US-specific.

**Q7: How do I tell if my actively-managed mutual fund is just
running a factor tilt?**
Run a regression of the fund's monthly excess returns against the
six factors (you can pull the data free from Ken French's website).
If the R-squared is over 0.90 and four or more factor loadings are
statistically significant, the fund's performance is mostly factor
exposure, and you should compare its fee against the
factor-replication ETF cost. Morningstar Direct and Portfolio
Visualizer both run this regression for free; there's no reason to
pay an active manager for what amounts to a buyable factor blend.

**Q8: What about the "low-vol anomaly" — isn't it a free lunch?**
It's the closest thing the equity market has to a free lunch on a
Sharpe basis, but it's not free. Low-vol underperforms in
melt-up regimes (think 1999, 2020-21) and tracks-error materially
against the cap-weighted index. The factor pays for itself in
risk-adjusted terms over a full cycle, but the absolute return drag
versus the S&P during a tech-led rally can be 10-15% over two years.

**Q9: Did the 2009 momentum crash kill momentum forever?**
No — UMD has had positive returns in most years since 2009, and the
post-2010 mean is roughly half the long-run mean (still positive,
just smaller). The 2009 crash is a permanent feature of momentum's
return distribution, not a one-off — there were similar (smaller)
momentum crashes in 1932, 2002, and a mini one in March 2020. Owning
momentum means accepting that one out of every twenty years it
loses 30%+.

**Q10: Should I time my factor exposures based on valuation?**
Empirically yes — Cliff Asness's "Value of Everything" research
shows that the *valuation spread* of a factor (cheap-leg P/B vs
expensive-leg P/B) predicts the factor's forward 5-year return. In
2026 the value factor is at the cheap end of its history (so the
forward expected premium is above the long-run mean) and momentum is
near the expensive end. But this is a slow-moving overlay, not a
trading rule — you adjust 10-20% of your tilt every few years, not
every quarter.

**Q11: How does factor investing fit with the four-tranche framework?**
Factors live in tranche one (the passive core) and tranche two (the
slightly-active tilt). They do *not* belong in tranche three (the
active concentrated book) or tranche four (the convex tail). A
factor blend isn't trying to compound 30% — it's trying to add 50-100
bps a year to your passive return at modest tracking error. That's
the tranche-one-and-two job description.

**Q12: What's a reasonable multi-factor blend for 2026?**
A defensible starter: 60% VTI (cap-weighted core), 10% AVUV
(small-value-quality), 10% MTUM (momentum), 10% QUAL (quality), 10%
USMV (low-vol). Total ER under 12 bps. This gives you all six factor
tilts at modest weights, with cap-weighted core dominating. Annual
rebalance. If you can hold this through a 30% momentum drawdown
without selling, you'll harvest most of what's left of the academic
factor premium.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Factor Investing in 2026 — Value, Momentum, Quality, Low-Vol, Size, and Why the Premium Halved
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

[INTRO]

**Stella:** Welcome back. Today we're doing the topic that probably
launched more PhD theses in finance than any other one — factor
investing. Value, momentum, quality, low-vol, size. The five flavours
your wealth manager has been pitching at you, plus market beta, plus
the academic framework that ties them together.

**Horace:** And we're doing it with a hook the textbooks don't lead
with. The premium on every one of these factors has *roughly halved*
since 2003. Half. Compressed. The thing that worked for Fama and
French in their 1992 paper still works in 2026, just at half the
size. We're going to look at why, and what to do about it.

**Stella:** Three things on this episode. One — what factors actually
are, mathematically. Two — the historical premium of each, and the
post-2003 decay story that nobody on the sell-side wants to dwell on.
Three — a hands-on factor-blender lab where you can build your own
multi-factor portfolio and backtest it against the Fama-French data
1963 to 2024.

**Horace:** And as always, where this fits the broader framework.
Factors are alpha lane number five — the structural one. They belong
in your passive core, *not* in your active book. By the end of the
episode you'll know how much of your portfolio should be in factor
ETFs and how much shouldn't.

[VISUAL: image/week23_factor_premia.png]

---

[SECTION 1: WHAT A FACTOR ACTUALLY IS]

**Horace:** Let's start with the definition because it's surprisingly
clean. A factor is not a kind of stock. A factor is a *long-short
portfolio*. You take every US stock, you rank them on some
characteristic — say book-to-market — go long the cheapest decile,
short the most expensive decile, hedge out the market, rebalance
monthly. The monthly P&L of that long-short portfolio is the value
factor. HML, in Fama-French notation. High Minus Low.

**Stella:** And the same construction applies to all of them.

**Horace:** Same construction every time. Rank, long top, short
bottom, equal-weight legs, monthly rebalance. Size is small minus
big — SMB. Momentum is up minus down — UMD. Profitability is robust
minus weak — RMW. Investment is conservative minus aggressive — CMA.
Plus the market factor itself, MKT minus the risk-free rate.

**Stella:** Six factors total in the modern framework.

**Horace:** Five Fama-French plus momentum, which Mark Carhart bolted
on in '97. That's the framework that explains roughly 90% of the
cross-section of US equity returns in 2026. Not 100% — there's still
residual stuff. But 90% means the typical "stock picker's alpha" is
actually a factor exposure with a fancier name.

**Stella:** Let's pull up the chart of historical premia.

[VISUAL: image/week23_factor_premia.png]

**Horace:** This is annualised long-run premium per factor, July 1963
through end of 2024. Market is the biggest at 6.6%, which makes sense
— it's the equity risk premium, the one CAPM was built on. Then
momentum at 7.5% — the only one bigger than market.

**Stella:** Momentum has the biggest factor premium of any of them?

**Horace:** And the biggest drawdown. We'll get to that. After
momentum, value at 3.8%, then investment at 3.3%, profitability at
3.0%, and size at the bottom around 2.4%. Notice size is the
*smallest* premium even though it's the factor that started the
whole literature in 1981 with Banz's paper.

**Stella:** Why is size the smallest?

**Horace:** Two reasons. One, most of the realised "small-cap
premium" turns out to be a small-*value* premium when you double-rank
on size and book-to-market. Size on its own is barely there. Two,
microcap illiquidity makes the academic measurement unreliable —
you can't actually trade the bottom of the size distribution at the
prices the long-short uses.

[SECTION 2: THE FACTOR DECAY STORY]

**Horace:** Now the part that doesn't show up on the BlackRock
marketing deck. Every one of these premia has *compressed* since
2003. Roughly halved.

[VISUAL: image/week23_factor_decay.png]

**Stella:** This is rolling 10-year mean of HML and UMD.

**Horace:** Right. The blue line is HML — the value factor's rolling
10-year premium, ending year by year. From the 1970s to about 2002,
that line averages 4 to 6%. Then it falls off a cliff. The rolling
10-year ending 2020 is *negative*. Negative. The academic value
factor lost money on average across the 2010s.

**Stella:** And the orange line — momentum.

**Horace:** Momentum's a different shape. The factor has a long-run
mean of 7-8%, and you can see that's where it sits for most of the
history. But notice the cliff in 2009. That's the momentum crash —
the 2009 single-year UMD drawdown was roughly 45% as the market
V-bottomed off the GFC lows and the previously-losing junk stocks
ripped higher. One year ate the next decade.

**Stella:** Why are all the premia compressing?

**Horace:** Three theories, all probably true. First — *publication
arbitrage*. The moment a factor gets written up in the Journal of
Finance, capital flows in to harvest it, the long leg gets bid up,
the short leg gets sold down, and the spread compresses. The
peer-reviewed paper is the obituary of the trade. Second —
*intangibles*. Book-to-market is a 1963 measure designed for an
industrial economy. It penalises asset-light tech firms whose value
is in non-capitalised R&D, brand, network effects. HML reads them as
"expensive" when on a corrected basis they're not. Third —
*central-bank liquidity*. Zero rates compress dispersion. Everything
trades together. Nothing is cheap or expensive any more.

**Stella:** So is factor investing dead?

**Horace:** It's not dead. It's smaller. The premium is still
positive — just half what it was. And the cost of harvesting it has
dropped even faster than the premium. In 2003 you paid a hedge fund
2-and-20 to run leveraged factors. In 2026 you click QUAL or AVUV
for 15 to 25 bps. So the *net* premium to the retail investor is
roughly the same as the *net* premium to the hedge-fund client was
in 2003. Cheap beta ate expensive alpha.

[SECTION 3: THE 2007 QUANT QUAKE]

**Horace:** Brief callback to Week 14 because it matters here. The
canonical case study in factor crowding is the August 2007 quant
quake.

**Stella:** Walk us through it.

**Horace:** Every leveraged long-short shop in 2007 — AQR, Renaissance,
Goldman GEO, dozens of mid-tier — was running essentially the same
factor portfolio. Long value, long momentum, long quality, short the
opposites. Levered five to eight times for risk-target purposes.
Then the week of August 6, somebody — probably a multi-strat fund
forced to deleverage to meet redemptions in their credit book —
started unwinding the standard factor portfolio in size.

**Stella:** And because everyone owned the same book —

**Horace:** Nobody on the other side. By Friday August 10 the
standard quant factor portfolio was down 25%. Three years of premium,
gone in four days. The S&P moved one percent. Retail never noticed.

**Stella:** What's the lesson for retail factor investing in 2026?

**Horace:** The blow-up was a *leverage* and *redemption* story, not
a factor story. Unleveraged retail factor ETFs don't have daily
VaR-driven stop-outs. They can sit through a quant unwind and just
take the temporary mark. The risk to retail is *forgone return*
— factors compress further — not catastrophic loss.

[SECTION 4: THE 2026 RETAIL ETF MENU]

**Stella:** Let's run the menu.

**Horace:** Five tickers cover the main factors, total ER under 25
bps. VLUE for value at 8 bps. MTUM for momentum at 15 bps. QUAL for
quality at 15 bps. USMV for low-vol at 15 bps. AVUV for combined
small-value-quality at 25 bps. IWM or IJR for size at 19 or 6 bps.

**Stella:** A retail investor can replicate the entire FF5+momentum
framework for under 20 basis points all-in?

**Horace:** Easily. And here's the bigger-picture angle. Factors are
the structural mispricing alpha lane — the academic factor premium
is the most arbitrageable subset. They
belong in tranche one or tranche two of your portfolio. The passive
core, with maybe a 10-30% tilt to factors. They do *not* belong in
your active concentrated book. The reason they pay less than they
used to is precisely because they're the easy lane — the lane that
doesn't require discomfort, doesn't require holding through hated
positions, doesn't require being early. Anything that easy gets
arbed.

**Stella:** And anything that requires discomfort —

**Horace:** Stays paying. That's why "buying what passive flows have
abandoned" — the contrarian sector trade, week 16 territory — is
still a 5%+ alpha lane while the academic factor portfolios are at
2-4%. Discomfort is the moat.

[SECTION 5: THE LAB]

**Stella:** Let's go to the interactive.

[VISUAL: course/interactive/week23_factor_blender.html]

**Horace:** Five sliders — your weights to MKT, SMB, HML, UMD, RMW.
The constraint is they have to sum to 100. The lab embeds the annual
Fama-French series 1963 to 2024 — 62 years of data — and runs your
chosen blend through it. Output is cumulative wealth, max drawdown,
Sharpe ratio.

**Stella:** And there are presets.

**Horace:** Four. Pure Value — 100% HML. Pure Momentum — 100% UMD.
Quality plus Low-Vol — equal-weight RMW and a low-vol proxy. And
GMO 60/40-style — Jeremy Grantham's classic value-tilt blend.

**Stella:** Click pure value first.

**Horace:** Now look at what happens. Wealth grows nicely from 1963
to 2007. Then the line goes flat. Twelve years of dead money.
That's the rolling-10-year HML decay we showed earlier in the
chart.

**Stella:** Now pure momentum.

**Horace:** Beautiful upward line — and a nasty 2009 cliff. The 45%
calendar drawdown is right there in the wealth curve. One year ate
five years.

**Stella:** Now the GMO blend — 50% market, 30% value, 10% quality,
10% momentum.

**Horace:** Smoother. Sharpe is better than any single-factor sleeve.
That's the point. The factors aren't perfectly correlated, so a
blend gets diversification on top of the average premium. Value and
momentum in particular are *negatively* correlated — when one's
suffering the other is usually doing fine. That's the most useful
pairing for a retail blend.

**Stella:** What's your recommended allocation for somebody starting
fresh in 2026?

**Horace:** Sixty percent in VTI as the cap-weighted core. Then ten
percent each in AVUV, MTUM, QUAL, USMV. Total ER under 12 bps,
exposure to all six factors at modest weights, cap-weighted core
dominant. Annual rebalance, hold for a decade-plus, don't sell when
one of the tilts is having a bad five years. That's the discipline
the strategy requires.

**Stella:** And if somebody can't sit through a five-year drawdown
of one of their tilts?

**Horace:** Don't tilt. Own VTI. The factor premium isn't worth
selling at the bottom and missing the rebound. If you can't hold
through pain, the cap-weighted index is the better product for you.

[OUTRO]

**Stella:** Recap. Factors are long-short portfolios built from
ranked stock characteristics. The Fama-French 5 plus momentum
explains 90% of the cross-section. Long-run premia: market 6.6%,
momentum 7.5%, value 3.8%, investment 3.3%, profitability 3.0%, size
2.4%. All of them have compressed since 2003 — roughly halved — for
publication-arbitrage and intangibles-mismeasurement reasons. The
2007 quant quake was about leverage and redemptions, not factors per
se. Retail factor ETFs in 2026 deliver the academic premium at under
25 bps. Use them as a 10-30% tilt on a cap-weighted core, not as a
replacement for it.

**Horace:** And the structural-alpha framing. Factors are the
structural alpha lane — the most systematic, the most scalable, and
the most arbed.
They belong in your passive core. The lane that pays *more* — the
lane the academic literature can't write a clean paper about — is the
contrarian one. Buying what passive flows have abandoned. We did that
in week 16 with sectors and we'll do it again in later weeks.

**Stella:** Next week we move from factor investing to the broader
question of style boxes — large-versus-small, growth-versus-value,
and the 9-cell Morningstar grid that organises most of the US equity
mutual fund universe. See you there.
