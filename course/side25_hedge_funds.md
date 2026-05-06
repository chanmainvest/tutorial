# Side Lesson 25: Hedge Funds -- Strategies, Fees, Access, and Whether They Earn Their Keep

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Hedge funds are the most over-mythologised vehicle in finance.
The trillion-dollar AUM, the billionaire founders, the locked-up
capital, the manager letters that get screenshotted on Twitter --
all of it conspires to make the asset class look like a separate
species, accessible only through a velvet rope. Alpha is rare,
and there are five places it actually
hides: structurally constrained capacity, information edge,
behavioural anomalies, regulatory arbitrage, and skill in price
discovery. The honest answer about hedge funds is that *all five
of those alpha sources exist inside hedge funds*, and the top
quartile delivers them. The dishonest part is that the dollars
that flow into accessible hedge fund vehicles -- funds-of-funds,
retail multi-strats, BDC-wrapped credit, daily-liquid replication
ETFs -- almost never see the top quartile. You get the average,
minus the wrapper fees, minus the FoF layer, minus the
illiquidity that you no longer benefit from.

Four reasons this side lesson is worth twelve minutes:

1. **The category beat the market for thirty years and then
   stopped.** The HFRI Composite outpaced the S&P 500 from 1990
   through about 2008 -- credibly, on lower volatility. From
   2009 through Apr 2026, HFRI has roughly *matched 60/40*, with
   similar volatility and a slightly worse Sharpe ratio. The
   alpha did not vanish; it migrated to a smaller and smaller
   slice of the manager population while the long tail piled in
   with too much capital. The category average is now a
   60/40-with-extra-fees product.
2. **The 2008 Buffett-Protégé bet settled the retail question
   forever.** Warren Buffett bet $1M that the Vanguard S&P 500
   index would beat a basket of five funds-of-hedge-funds chosen
   by Protégé Partners over ten years (2008-2017). S&P 500
   compounded **+125.8%** ($1 -> $2.26). The FoF basket
   compounded **+36.3%** ($1 -> $1.36). Not close. The settlement
   was not surprising to anyone who had stacked the fees: 2/20 at
   the manager + ~1/10 at the FoF wrapper + cash drag = ~5%/yr
   gross alpha required just to match the S&P after fees.
3. **The fee structure is engineered to capture half of gross
   alpha.** Two-and-twenty -- 2% management fee, 20% of profits
   -- on a fund that generates 8% gross alpha leaves roughly
   3.4% net to the LP. The manager keeps 4.6%. Add a
   fund-of-funds wrapper and you keep ~2.0%. Compound that gap
   over decades against a 5 bp index ETF and the picture is the
   one Side 08 already showed: hedge fund ownership transfers
   most of the equity premium to the manager, not the LP. The
   point is not "active management is bad." It is "active
   management is rare *and expensive*; the math has to work."
4. **The retail proxy menu is a real thing now and you should
   know it.** Liquid alternatives -- BTAL (anti-beta), MERFX
   (merger arb), BNDD (managed-futures-bond), QAI (multi-strat
   replication), RPAR (risk-parity), DBMF (managed futures) --
   give retail investors daily-liquid, low-fee, transparent
   access to roughly the same factor exposures that hedge funds
   sold for 2/20 in 2005. They are not replacements for top-tier
   hedge funds. They are replacements for the *average* hedge
   fund, and the average hedge fund is what 95% of accessible HF
   dollars buy.

This is not a lesson about whether hedge funds "work." Some do,
spectacularly. It is a lesson about whether *you can access the
ones that work*, and what the right substitute is when the
answer is no.

---

### 2. What You Need to Know

#### 2.1 The Strategy Taxonomy

Hedge funds are a wrapper, not a strategy. The wrapper is a
limited partnership with a 2/20 fee, 1-3 year lockup, quarterly
liquidity, and accredited-investor or QP-only access. Inside the
wrapper, managers run very different strategies. The category
labels matter because risk, return, fee-fairness, and retail
substitutability all vary by strategy.

**Long/short equity (~30% of HF AUM).** Buy a basket of stocks
expected to outperform; short a basket expected to underperform.
Net exposure typically 30-70%; gross exposure 130-200%. Alpha
comes from stock selection on both sides; market exposure is a
residual. Best year: 2009 (+20% HFRI L/S). Worst: 2008
(-26% HFRI L/S). Retail proxy: BTAL (anti-beta long/short),
or DIY 130/30 via leveraged-ETF combinations. Moderate
substitutability.

**Global macro (~12%).** Top-down trades on currencies, rates,
commodities, equity indices. Soros breaking the BoE in 1992 is
the canonical trade. Modern examples: Brevan Howard, Bridgewater
Pure Alpha. Best year: 2008 (+14% HFRI Macro). Worst: 2018
(-3.7%). Retail proxy: managed futures ETFs (DBMF, KMLM) or
diversified commodity (PDBC). Good substitutability for the
trend-following sub-strategy.

**Event-driven (~25%).** Catalysts: M&A, spinoffs, restructurings,
proxy fights, post-bankruptcy equity. Includes sub-strategies
*merger arb* (long target / short acquirer in a stock deal,
collect spread; ~3-7% annual return historically),
*activist* (Pershing Square, Elliott; concentrated long with a
plan), and *distressed credit* (buy bonds at 30c, work them
out at 60c). Best year: 2009 (+25%). Worst: 2008 (-21%).
Retail proxy: MERFX (merger arb mutual fund, 1.30% ER), GAMR or
ARB (slim ETF options), distressed bond ETFs (HYG/JNK -- crude
substitute). Reasonable substitutability for merger arb only.

**Relative value / arbitrage (~18%).** Convertible arb (long
convert / short stock), fixed-income arb (LTCM-style), statistical
arb (high-frequency mean-reversion), volatility arb (sell expensive
vol, buy cheap vol). All variations on "two things that should
trade together but don't, lever it 5-15x, collect the spread."
Best year: 2009 (+47% HFRI Conv Arb after the 2008 dislocation).
Worst: 2008 (-34%). Retail proxy: essentially none -- the
strategy lives or dies on cheap leverage and low transaction
cost. Daily-liquid attempts (CWB for convertible long-only) miss
the short leg entirely.

**Multi-strategy (~15%).** Runs all of the above inside one
fund, with internal capital allocation that shifts toward
whichever strategy is paying. Citadel, Millennium, Point72,
Balyasny. The "pod shop" model. Best year: 2008 (+8% HFRI
Multi-Strat -- one of the few HF categories *up* in 2008).
Worst: never down more than -2% in any calendar year since
2002 for the top quartile. Closed to new capital almost
universally. Retail proxy: QAI (IndexIQ Hedge Multi-Strat
Tracker ETF). Poor substitutability -- pod shops generate alpha
through internal capital allocation that no daily-liquid wrapper
can replicate.

#### 2.2 Two-and-Twenty: Where the Money Goes

Take a hedge fund that returns 10% gross before fees on $100M
AUM in a calendar year.

| Line item | Amount | Whose pocket |
|---|---|---|
| Gross return | $10.0M | LP nominal |
| Less management fee 2% on $100M | -$2.0M | Manager |
| Pre-incentive return | $8.0M | LP |
| Less performance fee 20% of $8.0M | -$1.6M | Manager |
| Net to LP | $6.4M | LP |

The LP gets 6.4% net. The manager gets 3.6%. The manager
captured **36% of gross alpha** in a 10% year. In a 15% year,
the split is roughly 9.0% / 6.0% -- still 40% to the manager.
In a 5% year, the split is 2.4% / 2.6% -- the manager takes more
than half. The fee schedule gets *more* punishing in mediocre
years, not less, because the 2% management fee does not flex
with returns.

Now layer a fund-of-funds. The FoF charges typically 1% / 10% on
top, on returns that are themselves already net of the underlying
2/20. A 10% gross year at the underlying becomes 6.4% to the FoF,
which becomes ~5.0% to the FoF investor after FoF fees. The
manager kept 3.6%, the FoF kept 1.4%, the LP kept 5.0%. Half
the gross alpha lives somewhere other than the LP's account.

Funds-of-funds were the dominant retail-and-small-institutional
hedge fund access model from 1995 through 2008. They have shrunk
since, but they still account for roughly $700B globally as of
2024. **Most retail dollars that touch hedge fund strategies
today still go through this double-fee layer.**

#### 2.3 The Buffett-Protégé Bet, 2008-2017

In 2008 Warren Buffett challenged any hedge fund manager to bet
$1 million that "an index fund will, over ten years, outperform
a fund-of-funds invested in hedge funds, after fees." Protégé
Partners accepted, picked five FoFs (which themselves invested
in roughly 100 underlying hedge funds), and the bet ran from
January 1, 2008 through December 31, 2017.

| Asset | 10-yr cumulative | CAGR |
|---|---|---|
| Vanguard S&P 500 Admiral (VFIAX) | **+125.8%** | 8.5%/yr |
| Protégé FoF basket (5 FoFs avg) | **+36.3%** | 3.2%/yr |

The S&P 500 fell 38% in 2008 alongside the hedge funds (which
were down 20-25% as a group). After that, the hedge funds simply
could not catch up. The FoFs generated something like 6-7% gross
alpha as a basket; the fee stack consumed nearly all of it.

The bet was a bull-market 10-year window, which favoured the
index. But the *structural* point is independent of the window:
in any market regime, a hedge fund FoF needs to generate
~5%/yr alpha just to break even with the index after fees. Few
do. None do reliably.

Buffett donated his winnings ($2.2M, including the bet's
appreciation in zero-coupon bonds and later Berkshire B shares)
to Girls Inc. of Omaha.

![Cumulative-wealth chart of $1 invested January 2008 through December 2017 in Vanguard's S&P 500 Admiral (VFIAX) versus a basket of five funds-of-hedge-funds picked by Protégé Partners. Year 1 (2008): both lines fall — S&P to $0.62, FoF basket to $0.76 (hedge funds did less badly but did not protect). From 2009 onward the S&P line accelerates relentlessly while the FoF basket grinds at single digits. End of 2017: S&P at $2.26 (+125.8% cumulative, 8.5%/yr CAGR); FoF basket at $1.36 (+36.3% cumulative, 3.2%/yr CAGR). The S&P returned more than three times the fund-of-funds. The chart is the single cleanest empirical refutation of the retail hedge-fund pitch.](image/side25_buffett_bet.png)

#### 2.4 The HFRI Composite vs 60/40, 2000-Apr 2026

Look at the wealth path. From January 2000 through April 2026:

| Asset | $1 -> | CAGR | Vol | Sharpe (rf=2%) |
|---|---|---|---|---|
| HFRI Composite | $4.85 | 6.2%/yr | 7.0% | 0.60 |
| 60/40 (SPY/AGG) | $5.30 | 6.5%/yr | 9.5% | 0.47 |
| S&P 500 (SPY) | $7.60 | 7.9%/yr | 15.2% | 0.39 |

HFRI matched 60/40 on dollars over 26 years and beat it slightly
on Sharpe via lower volatility. It substantially trailed the
S&P 500 in dollars but had a much smaller drawdown profile
(-21% peak-to-trough vs -55% for SPY in 2008-09).

But the comparison hides the *regime* divide. From 2000-2008
HFRI compounded **+8.4%/yr** vs SPY -1.4%/yr -- the alpha was
genuine. From 2009-Apr 2026, HFRI has compounded **+5.0%/yr**
vs SPY +13.6%/yr -- the alpha disappeared and what remained was
roughly 60/40-with-fees. The 1990s and 2000s produced the
hedge-fund mythology; the 2010s and 2020s have demolished it
for the average fund.

Top-quartile managers continue to deliver. The category average
does not. **Retail allocators almost certainly receive the
category average.**

![Cumulative-wealth chart of $1 invested January 2000 through April 2026 across three sleeves: HFRI Fund-Weighted Composite (the AUM-weighted hedge-fund industry average, blue), a 60/40 SPY/AGG portfolio rebalanced annually (green), and the S&P 500 alone (orange). HFRI ends at $4.85 (6.2%/yr, vol 7%, Sharpe 0.60); 60/40 ends at $5.30 (6.5%/yr, vol 9.5%, Sharpe 0.47); SPY ends at $7.60 (7.9%/yr, vol 15%, Sharpe 0.39). The HFRI line outpaces both 60/40 and SPY through the 2000-2008 stretch (the genuine hedge-fund mythology era), then stalls from 2009 onward — matching 60/40 in dollars and trailing SPY by a wide margin. The chart shows the regime divide that retail allocators almost never see in marketing material.](image/side25_hfri_vs_60_40.png)

#### 2.5 Liquid Alternatives -- The Retail Substitute Menu

The 2010-2024 wave of "liquid alts" packaged hedge fund
strategies inside daily-liquid mutual funds and ETFs at 50-100
bp instead of 2/20. The good ones approximate the *factor
exposures* of hedge fund strategies; they do not replicate the
*alpha*. That is acceptable if the factor exposure is what you
wanted (downside protection, low correlation, crisis alpha),
which for most retail allocators it is.

The accessible menu (Apr 2026):

| Strategy mapping | Vehicle | ER | AUM | Notes |
|---|---|---|---|---|
| Anti-beta long/short | BTAL | 1.40% | $0.4B | Long low-beta / short high-beta |
| Merger arbitrage | MERFX | 1.30% | $1.8B | Mutual fund, 30-yr track record |
| Managed futures | DBMF | 0.85% | $1.0B | iMGP DBi; trend-follower replication |
| Multi-strat replication | QAI | 0.80% | $0.7B | IQ Hedge multi-strat |
| Risk parity | RPAR | 0.50% | $1.4B | RPAR Risk Parity |
| Bond-managed-futures hybrid | BNDD | 1.05% | $0.2B | Quadratic; intended for tail hedging |
| Macro / global tactical | KMLM | 0.92% | $0.6B | KFA Mt Lucas; MD-based trend |
| Long/short equity | QLEIX | 1.49% | $1.0B | AQR Long/Short, mutual fund |

These are real products with real expense ratios. None will
generate 12-15% annualised returns over decades. They will
generate 4-7% returns with low correlation to stocks/bonds and
typically *positive* returns in equity-bear-market years, which
is the actual job description of an alternative sleeve.

Sizing follows the same rule as Side 14 (private markets): a
total alternative sleeve of 5-15% of portfolio, split across two
or three uncorrelated strategies. This is the
"non-correlated barbell tail" of the portfolio -- it earns less
than equities in good markets and is the only thing that pays
in 2008/2022-style scenarios.

#### 2.6 Bottom Line: Who Should Touch Hedge Funds

Three clean rules.

1. **If you are not accredited and a QP, you cannot access the
   strategies that earn their keep.** Stop looking. Use liquid
   alts and accept that you are buying factor exposure, not
   alpha.
2. **If you are accredited but not allocating $5M+, the only
   hedge fund vehicles open to you are FoFs and retail
   multi-strats.** Both are double-fee structures. The math
   says you will not beat 60/40 net of fees over 10+ years.
   Pass. Use liquid alts.
3. **If you are an institution or family office with $50M+ and
   real manager-selection capability, top-quartile hedge funds
   are a legitimate sleeve.** The selection bar is high: closed
   to new capital, founder still active, capacity-constrained
   strategy, transparent reporting, no "key man" concentration
   risk. ~5-15% of total portfolio, similar to private markets.

The retail playbook for the alternative sleeve, all-in: 3-5% in
DBMF (or KMLM) for managed futures crisis alpha, 2-3% in MERFX
for low-correlation event-driven yield, 1-2% in BTAL or RPAR
for portfolio-vol dampening. Total: 6-10% sleeve, ~75 bp
weighted ER, daily liquid, no lockup, no K-1 (DBMF/RPAR are 1099
ETFs; MERFX is mutual fund 1099-DIV; BTAL is 1099). Pair with
core 60/40 or barbell. Done.

The conclusion: alpha is rare *and*
the access table is constrained. The retail investor's job is
not to chase the alpha that hedge funds generate; it is to buy
the *exposures* the alpha sleeves provide and skip the wrapper
that prices in alpha you will never see.

---

### 3. Common Misconceptions

1. **"Hedge funds hedge."** No. The word is historical. Some
   hedge funds run net-30% market exposure and call themselves
   long/short. Many run 130% net long and call themselves
   "growth-oriented." Multi-strats can run -50% net short for
   weeks. The label is a wrapper, not a risk profile.

2. **"Hedge funds beat the market."** As a category, they did
   pre-2008 and have not since. The HFRI Composite has roughly
   matched 60/40 since 2009. Top-quartile managers still beat
   the market; you cannot access them.

3. **"2/20 is fair because it aligns incentives."** It aligns
   the manager's incentive to *take risk*, not to deliver alpha.
   The 2% management fee is paid in flat years, down years, and
   wind-down years. Watermark provisions help but do not fix the
   asymmetry. Many funds reset watermarks after closures and
   re-open under new entities.

4. **"Lockups are the price of access to better strategies."**
   They are, for genuinely illiquid strategies (distressed
   credit, late-stage activism, real-asset arb). For long/short
   equity and macro running 90%+ liquid instruments, the lockup
   serves the manager, not the strategy.

5. **"Liquid alts replicate hedge funds."** They replicate the
   factor exposures, not the alpha. DBMF gives you trend-
   following beta at 85 bp; it does not give you Renaissance
   Medallion's idiosyncratic alpha at any price.

6. **"Funds-of-funds diversify away manager risk."** They
   diversify away alpha as well, in proportion. The math of the
   double fee layer almost guarantees the FoF investor receives
   60/40-equivalent returns minus 2-2.5%/yr.

7. **"Hedge funds protected investors in 2008."** The HFRI
   Composite was -19% in 2008. Better than -38% S&P 500, but
   not "protection." Multi-strat (+8%) and managed futures
   (+14%) were the only categories actually positive.

8. **"My advisor's hedge fund picks are different."** Roughly
   90% of advisor-recommended hedge fund products are FoFs,
   retail-class multi-strats, or BDC-wrapped credit. All carry
   the double-fee structure. Ask: "What is the all-in fee load,
   inclusive of underlying fund fees? What is the historical
   alpha after that load?" The answer is usually no answer.

9. **"Buffett's bet was unfair because 2008-2017 was a bull
   market."** Partly true; the index beat by an unusually wide
   margin. But run the same bet 1990-1999 (also a bull market)
   and HFRI beat the S&P 500 by 4%/yr. The pattern reversed
   exactly when manager capacity exceeded market alpha
   capacity, around 2008-2009.

10. **"Multi-strat pods are the new hedge fund alpha."** They
    are -- for the institutions that can write the $250M
    minimum check and accept the 5%-of-NAV-per-year "pass-through
    expense" charge that makes the all-in load 6-9%/yr. For
    everyone else, QAI is the daily-liquid replacement and it
    runs at a much lower fee but also a much lower alpha.

---

### 4. Q&A Section

**Q1: I am accredited. Should I buy a hedge fund through my
broker?**

A: Almost certainly not. The hedge funds your broker can sell
you are funds-of-funds, retail-class multi-strats, or
BDC-wrapped credit -- not the closed-to-new-capital top
quartile. The math of the double-fee layer says you will
underperform 60/40 over 10+ years. Use the liquid alt menu
instead and save the fee stack.

**Q2: What is the minimum to access a top-quartile hedge fund?**

A: For a name like Renaissance, Citadel, Millennium, D.E. Shaw,
TCI: typically closed to new capital, period. When they open,
minimums are $5-25M and require multi-year strategic
relationships. For second-tier well-regarded funds: $1-5M and
qualified-purchaser status ($5M investments outside primary
residence). Most retail and HNW clients are below this floor.

**Q3: Are managed futures (DBMF) really a hedge fund proxy?**

A: They are a proxy for the trend-following sub-strategy, which
is roughly a third of macro hedge fund AUM. DBMF is calibrated
on the SocGen CTA Index (Week 51 covered this); it captures
~70% of the index's return at ~85 bp instead of the underlying
2/20. It does not proxy long/short equity, event-driven, or
relative-value strategies. For the trend-following slice, it is
a credible substitute.

**Q4: What is a "pass-through expense" in multi-strat funds?**

A: Pod shops (Citadel, Millennium) charge LPs the actual
operating expenses of the firm -- portfolio manager comp, tech,
data, financing -- as direct expenses, in addition to the
management and performance fees. The pass-through can be
2-7%/yr on top of the headline fees. Total all-in cost on a
typical multi-strat is 6-9%/yr. The funds still close to new
capital because the gross returns are 18-25%/yr.

**Q5: Is BDC stock a hedge fund proxy?**

A: Public BDCs (ARCC, MAIN, BXSL) are exposed to roughly the
same loan book a hedge fund credit sleeve would hold, at a
fraction of the fee. They pay 8-10% yields. They are *not* a
hedge fund replacement -- BDCs are levered direct lenders, not
opportunistic credit traders. But for the "earn 8-10% on senior
loans" exposure that drives most credit-focused HF returns, a
small BDC sleeve is the cleaner retail substitute (Side 14
covered this).

**Q6: Why did long/short equity funds underperform so badly
2010-2024?**

A: Three reasons. (1) Short-side alpha collapsed as quantitative
factor research flooded the market and "short overvalued
companies" stopped working. (2) Borrow costs rose for hard-to-
borrow names (the actual interesting shorts), so the carry on a
short book turned from net-positive to net-negative. (3) The
"meme stock" episodes of 2021 (GameStop, AMC) generated short-
squeezes that wiped years of alpha for funds that had genuine
short-thesis books. The strategy is in structural decline as a
category.

**Q7: What is the right fee for a hedge fund-style product I
*can* access?**

A: For a daily-liquid replication ETF (DBMF, QAI, RPAR), 50-100
bp is reasonable. For a mutual fund running real
operationally-active arb (MERFX), 1.0-1.5% is reasonable
because the strategy actually trades. For an advisor-wrapped
"alternatives sleeve" of FoFs charging 2.0%+ all-in, the math
does not work -- pass.

**Q8: Did the 2022 bear market vindicate hedge funds?**

A: Selectively. Managed futures had their best year since 2008
(+20% SocGen CTA, +25% DBMF). Multi-strats were +8 to +12%.
Long/short equity was -15 to -20%, slightly better than the
S&P 500's -18% but not enough to justify the fee load. The
HFRI Composite was roughly flat for 2022 vs -16% for 60/40.
*That single year* is the strongest case for an alt sleeve in
20 years of data.

**Q9: How do hedge funds report returns? Can I trust them?**

A: HFRI, BarclayHedge, and HFR Indices report monthly returns
self-reported by managers. There are well-documented biases:
*survivorship* (failed funds drop out), *backfill* (good early
years get added when a fund joins the index), and *late
reporting* (managers delay reporting bad months, hoping for
recovery). Academic work (Aiken, Clifford, Ellis 2013) suggests
true HF returns are 1.5-2% lower than reported indices over long
periods. The HFRI numbers cited in this lesson are the *reported*
ones; the actual investor experience is worse.

**Q10: Where does crypto fit in the hedge fund taxonomy?**

A: Crypto-focused hedge funds (Pantera, Polychain, Multicoin,
Galaxy Digital's funds) are technically "long/short" or "global
macro" by SEC classification. They are mostly long-biased
directional bets on crypto with a thin trading layer on top.
Performance has been catastrophic in down cycles (-60 to -90% in
2022) and spectacular in up cycles. They are *not* a
diversifying sleeve; they are levered crypto exposure with HF
fees. Side 09 covered the much better retail alternative -- spot
ETFs (IBIT, FBTC) at 25 bp.

**Q11: Does Bridgewater's All Weather count as a hedge fund?**

A: Bridgewater is structurally a hedge fund (LP wrapper, 2/20-ish
fee base), but All Weather is a risk-parity strategy -- different
from Pure Alpha (their global macro fund). All Weather post-
inception (1996) has compounded ~7%/yr with low volatility,
which is in line with -- not better than -- a DIY 60/40.
Retail equivalent: RPAR at 50 bp. Bridgewater's actual alpha
fund, Pure Alpha, has done well historically but has been roughly
flat for 2010-2024.

**Q12: If hedge funds are mostly bad, why do institutions
allocate to them?**

A: Three reasons. (1) Top-quartile managers genuinely earn their
fees and institutions can identify them through manager-due-
diligence operations that retail cannot replicate. (2) Career
risk: a CIO who allocates 10% to "alternatives" looks
sophisticated; one who runs 100% Vanguard 3-fund looks lazy.
(3) Endowment-model momentum: Yale and Harvard built their
reputations on alternative allocations in the 1990s, and the
peer pressure on smaller endowments to copy them is
considerable. The first reason is real; the other two are
agency problems.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Hedge Funds: 2/20 Buys You 60/40 -- Side Lesson 25

**RUNTIME TARGET:** ~12 minutes

**HOSTS:**
- **Horace** (teacher): Has a copy of *More Money Than God* on
  the desk.
- **Stella** (student): Just got a hedge fund pitch from her
  bank's wealth advisor.

---

**[INTRO -- 0:00]**

[VISUAL: Animated logo "Side Lesson 25 -- Hedge Funds: Strategies,
Fees, and Whether They Earn Their Keep"]

**Stella:** Horace. My bank's wealth advisor wants me to put 10%
of my portfolio in their "Alternatives Solution." It is a
fund-of-hedge-funds. The pitch is "low correlation, downside
protection, manager skill." 1.5% management fee, 10% performance
fee on top of the underlying 2/20.

**Horace:** Stop. Before we touch the math. What was the most
expensive bet Warren Buffett ever made?

**Stella:** I have no idea.

**Horace:** A million dollars in 2008, against a basket of five
hedge fund-of-funds picked by Protégé Partners. Vanguard S&P 500
on his side. Ten-year horizon.

**Stella:** Who won?

**Horace:** S&P 500 compounded 125%. The fund-of-funds basket
compounded 36%. The S&P returned more than three times the FoFs.
Buffett donated his winnings to charity.

**Stella:** That is the exact product my bank is selling me.

**Horace:** That is the exact product everyone's bank is selling.
Twelve minutes. Let me show you why.

---

**[SEGMENT 1 -- THE HFRI vs 60/40 WEALTH PATH -- 1:00]**

[VISUAL: image/side25_hfri_vs_60_40.png on screen]

**Horace:** This is the entire hedge fund industry, by AUM-
weighted average return, since January 2000 through April 2026.
Twenty-six years.

The blue line is the HFRI Fund Weighted Composite. That is the
industry average. $1 became $4.85. About 6.2% per year. Volatility
about 7%. Sharpe ratio of 0.6.

The green line is a plain 60/40. SPY plus AGG, rebalanced
annually. $1 became $5.30. About 6.5% per year. Vol of 9.5%.
Sharpe of 0.47.

The orange line is the S&P 500 alone. $1 became $7.60. 7.9% per
year. Vol of 15%. Sharpe of 0.39.

**Stella:** So hedge funds beat 60/40 on Sharpe but lost on
dollars?

**Horace:** Tied on dollars. Marginally won on Sharpe. Got
demolished by the S&P 500 on dollars. And here is the part that
matters -- the hedge fund advantage was *entirely* in the first
nine years.

From 2000 to 2008, HFRI compounded 8.4% per year. The S&P, with
the dot-com crash and the financial crisis, was *negative* 1.4%
per year. Hedge funds *destroyed* the index over that decade.

From 2009 forward, HFRI has compounded 5%. The S&P has compounded
13.6%. Hedge funds, on average, did not just lose to the index --
they roughly *matched 60/40, with extra fees*.

**Stella:** What changed?

**Horace:** Three things. The category got too big -- you cannot
run 4 trillion dollars through alpha strategies that have
combined capacity of maybe 500 billion. The factor research
flooded the market -- hedge funds used to have edge in
"buy small-cap value, sell large-cap growth" and now there's an
ETF for that. And ZIRP eliminated the cash yield that funded the
short book. The structural alpha source dried up.

---

**[SEGMENT 2 -- THE BUFFETT-PROTÉGÉ BET -- 3:30]**

[VISUAL: image/side25_buffett_bet.png on screen]

**Horace:** Now. The Buffett-Protégé bet, expanded to a chart.

January 2008, Buffett puts $1 of nominal capital in Vanguard's
S&P 500 Admiral. Protégé puts $1 in a basket of five funds-of-
hedge-funds. We let it run ten years.

Year 1, 2008. The S&P falls 38%. The FoF basket falls 24%.
Hedge funds did *less badly* but they did not protect; they were
losing too. End of 2008, S&P at 62 cents, FoFs at 76 cents.
Hedge funds look smart for one year.

Year 2, 2009. S&P up 26%. FoFs up 16%.
Year 3, 2010. S&P up 15%. FoFs up 5%.
Years 4-10, the gap widens every year. The S&P is doing 12-15%
in a relentless bull market. The FoFs are doing 3-6%.

End of 2017. S&P at $2.26 -- compounded 125.8%, about 8.5% per
year. FoFs at $1.36 -- compounded 36.3%, about 3.2% per year.

**Stella:** The hedge funds *lost to the S&P by 4x* in dollars?

**Horace:** They lost to the S&P by 4x in dollars. And before
you say "well, that's just one bull market window" -- the
*structural* number is what matters. The fee load on a fund-of-
funds is roughly: 2% management at the underlying, plus 20% of
profits at the underlying, plus 1% management at the FoF, plus
10% of profits at the FoF. To break even with the S&P after
fees, the gross alpha at the underlying funds needs to be on the
order of 5% per year. Almost no fund delivers that, and the ones
that do are closed to FoFs.

**Stella:** Buffett picked the cleanest possible example.

**Horace:** He picked the *most accessible* example. The product
Protégé bought is the product 90% of accredited investors are
sold by their advisors. The bet was rigged in Buffett's favour by
the structure of the fee stack, not by the choice of decade.

---

**[SEGMENT 3 -- THE STRATEGY TAXONOMY -- 6:30]**

[VISUAL: interactive/side25_hf_explorer.html on screen]

**Horace:** Open the interactive. You will see five strategy
buckets across the top. Click each one and the panel changes.

**Long/short equity.** 30% of HF AUM. Buy good stocks, short
bad stocks. Net 30-70%. Best year was 2009 at +20%. Worst was
2008 at -26%. Typical net return after fees: 4-7%. Retail proxy:
BTAL at 1.4% expense ratio.

**Global macro.** 12% of AUM. Top-down trades. Currencies,
rates, commodities. Soros breaking the Bank of England in '92.
Best year 2008 at +14%. Retail proxies: managed futures ETFs
DBMF and KMLM, 85-90 bp.

**Event-driven.** 25% of AUM. M&A arb, distressed, activist.
Best year 2009 at +25%. Retail proxy for the M&A arb sleeve:
MERFX at 1.30% expense ratio. Real fund, 30-year track record.

**Relative value.** 18% of AUM. Convertible arb, fixed-income
arb, statistical arb. The strategies LTCM ran. Need 5-15x
leverage to make money. *No retail proxy* -- the strategy lives
on cheap leverage and tight bid-ask, neither of which a 1099 ETF
can replicate.

**Multi-strategy.** 15% of AUM. Citadel, Millennium, Point72.
Pod-shop model. Closed to new capital almost universally. The
*best* category by Sharpe ratio in the entire HF universe.
Retail proxy: QAI at 80 bp. Significantly worse than the real
thing but only thing accessible.

**Stella:** And the panel shows what for each one?

**Horace:** Typical net return, vol, Sharpe, the fee structure,
the 2008 drawdown, and the retail proxy. The point is to make
the trade-off concrete: this is what you would have paid, this
is what you would have gotten, and here is what the daily-liquid
version costs.

---

**[SEGMENT 4 -- THE LIQUID ALT MENU -- 9:30]**

**Stella:** OK. So what *should* I tell my advisor?

**Horace:** Tell them you want a self-built liquid-alts sleeve
instead of their FoF.

**Stella:** Which products?

**Horace:** Three to four ETFs and mutual funds, 6-10% of total
portfolio, weighted ER under 100 bp.

DBMF for managed futures. 85 bp. Captures most of the SocGen CTA
trend-following return. Up 25% in 2022, up 14% in 2008. *Real*
crisis alpha.

MERFX for merger arbitrage. 130 bp. Mutual fund, 30-year history.
Returns 4-6% per year with very low correlation to anything.

BTAL or RPAR for portfolio vol dampening. 50-140 bp. Anti-beta or
risk-parity exposure.

Total sleeve fee: 75-100 bp. Total sleeve size: 6-10% of
portfolio. Pair with core 60/40 or barbell. You now have
real alternative diversification at a tenth of what your bank
was going to charge.

**Stella:** And the 2/20 hedge funds my bank pitches...

**Horace:** Capture roughly half of gross alpha as fees. Layer a
FoF on top, capture another quarter. You receive what's left,
which is empirically 60/40 minus 2%/yr. Don't.

---

**[SEGMENT 5 -- THE ONE-PERCENT EXCEPTION -- 11:00]**

**Stella:** Are there *any* hedge funds worth touching?

**Horace:** Yes. Three or four characteristics in combination
make a fund worth the fee.

One: closed to new capital, with a wait list. If anyone can give
them money, the strategy probably isn't capacity-constrained.

Two: founder-still-active and original team intact. Two-thirds
of the HF universe is people running other people's models with
the founder's name on the door. That is fee extraction, not
manager skill.

Three: capacity-constrained strategy. Volatility arb. Statistical
arb on small-cap. Distressed credit at the bottom of cycles.
Things where the strategy itself has a finite size.

Four: transparent reporting. If you can see the positions
quarterly and the historical drawdowns are honestly disclosed.

If you find a fund with all four, and you can write the $5M+
check, and you have 5 years of lockup tolerance -- go. That is
where "alpha is rare" actually pays.

For the rest of us: liquid alts. Daily liquid. Transparent.
1099. Boring. Effective.

---

**[OUTRO -- 11:45]**

**Horace:** Three things to remember.

One: hedge funds, as a category, were a real alpha vehicle from
1990 to 2008 and have not been one since. The category average
is now 60/40 with extra fees.

Two: the fee structure -- 2/20 plus FoF wrapper -- captures
roughly half of gross alpha. Buffett's 2008-2017 bet showed it
quantitatively: S&P returned 125%, FoFs returned 36%. The bet
was settled by the fee math, not the market.

Three: liquid alts give retail investors the *factor exposures*
of hedge fund strategies at 50-100 bp. DBMF, MERFX, BTAL, RPAR,
QAI. Sized at 6-10% of portfolio, they do the job a 2/20
hedge fund was supposed to do, at a tenth of the cost.

Alpha is rare. The corollary nobody draws often enough:
when alpha is rare, the *fee load* matters more than the *fund
selection*. A 50 bp ETF that earns 5% beats a 2/20 hedge fund
that earns 9% gross. The math is not subtle.

**Stella:** I am calling my advisor in the morning to decline
the FoF.

**Horace:** Tell them you want DBMF, MERFX, and BTAL instead.
Watch them try to sell you their advisor share class. Same
strategies, 200 bp markup. Decline that too.

---

**[END]**
