# Side Lesson 22: Commodities — Gold, Oil, Agriculture as Portfolio Diversifiers

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Commodities are the only asset class that the rest of finance is *priced
off*. Bonds discount expected inflation; stocks discount future earnings
that ride on input costs; currencies adjust to terms of trade. Yet ask
a typical retail portfolio for its "commodities sleeve" and the answer
is usually a confused mix of GLD, an energy ETF, and the suspicion that
"it didn't work in 2024." The reason is that commodities, as a financial
exposure, behave nothing like the underlying physical goods most people
imagine they are buying.

Four reasons this lesson exists as its own slot rather than a paragraph
under the inflation chapter (Side 06):

1. **Most retail "commodity" exposure is futures-rolled, not spot.** USO,
   UNG, DBC, PDBC and the entire BCOM-tracking ecosystem hold *futures*,
   roll them quarterly, and bleed the contango term-structure. From 2009
   to 2020 USO lost about half its value while WTI front-month was
   essentially flat. The instrument is not the commodity.
2. **Gold is structurally different from every other commodity** because
   GLDM/IAU/GLD hold *physical bullion in a vault* — no roll, no decay,
   pure spot exposure. Gold is a store of value because
   collective belief makes it one; oil is industrial input that decays
   in your portfolio whether or not you believe in it.
3. **Long-term real returns to a passive commodity basket are flat to
   negative.** Erb-Harvey (2006) and twenty years of follow-up work put
   the real geometric return of the Bloomberg Commodity Index at
   approximately zero over multi-decade windows. The diversification
   argument is real; the long-run return premium is not.
4. **Inflation-hedge value is concentrated in supply-shock windows.**
   Oil 1973, agriculture 2007, energy 2022. Outside those windows
   commodities are dead weight. If your sizing rule does not account for
   the regime-conditional payoff, you will hold them for the
   wrong reasons and trim them at the wrong time.

The goal of this lesson is to make the spot-vs-futures distinction
mechanical, calibrate the long-run real-return number, and produce a
sizing rule that lets a four-tranche portfolio carry commodities without
expecting them to be a quiet contributor.

![Real (CPI-deflated) Bloomberg Commodity Index 1970 to April 2026, plotted as a wealth path of $1 invested in 1970. Real wealth peaks during the 1970s oil shocks and the 2008 supercycle, but the long-run trend is flat, with terminal real wealth near $1 — confirming Erb-Harvey's finding that broad commodity baskets pay no real-return premium over inflation.](../image/side22_real_commodities.png)

---

### 2. What You Need to Know

#### 2.1 The Four Sectors and What Drives Each

Index providers split commodities into **energy, metals, agriculture,
and livestock**. The standard Bloomberg Commodity Index (BCOM, April
2026 weights) is roughly 28% energy, 38% metals (split 17% precious /
21% industrial), 31% agriculture, and 3% livestock. The S&P GSCI tilts
much heavier into energy (~55%); the difference matters because GSCI
returns are dominated by oil while BCOM is closer to a balanced basket.

Each sector responds to a different driver. **Energy** is set by OPEC+
production discipline, US shale capex, transportation demand, and
geopolitical supply shocks (1973 embargo, 1990 Gulf War, 2022 Ukraine).
**Industrial metals** — copper, aluminium, zinc, nickel — track the
global manufacturing PMI and Chinese fixed-asset investment, which is
why "Dr Copper" leads the cycle by six to nine months. **Precious
metals** — gold and silver — track real interest rates and central-bank
demand; they barely correlate with industrial activity. **Agriculture**
— corn, wheat, soybeans, sugar, cotton, coffee — is dominated by
weather, planting decisions, and biofuel mandates; supply shocks are
sharp and short. **Livestock** is the smallest and most idiosyncratic,
driven by feed costs and disease cycles.

The diversification within commodities is real: in 2022, energy
returned +35%, industrial metals -10%, precious metals near flat,
agriculture +12%, livestock +9%. A broad basket smooths these out;
single-sector ETFs do not. That same dispersion is, separately, one
of the cleanest sector-rotation signatures the market gives away
for free — when energy and industrial metals are pulling apart by
forty points in a single year, the macro thesis underneath is loud
enough to trade off, and rotation is one of the few alpha sources
I trust over decades.

#### 2.2 Spot vs Futures: The Mechanism Most Investors Get Wrong

When you buy XOM stock you own a share of an oil company. When you buy
USO you do not own oil — you own a basket of front-month WTI futures
contracts that the fund **rolls** every month into the next contract.
Each roll is a sale of the expiring contract and a purchase of the next
one, executed mechanically.

If the futures curve is in **contango** (next contract priced higher
than front), the fund sells low and buys high every roll, and the
position bleeds at the rate of the contango spread. If the curve is in
**backwardation** (next priced lower than front), the fund collects a
positive roll yield. Industrial commodities with high storage costs
(natural gas, oil during gluts) live in chronic contango. Soft and
crisis commodities (oil during embargoes, agricultural products during
drought) flip into backwardation.

The historical drag on USO from contango alone is about -6% to -9% per
year averaged over 2009-2020. Front-month WTI started 2009 near $42 and
ended 2020 near $48 — essentially flat. USO over the same window lost
roughly half its NAV. The investor was right about oil and lost money
anyway. (Week 39 covers the term-structure mechanics in detail; this
side lesson borrows the result.)

The clean way to express commodity views without roll drag is to use
**equity proxies**: XOM/CVX for oil, FCX for copper, NEM for gold
miners, ADM/BG for agriculture. They carry equity beta and management
risk in exchange for eliminating the futures bleed.

#### 2.3 Gold vs Oil: Same Asset Class, Opposite Mechanics

Gold ETFs (GLDM 0.10% ER, IAU 0.25%, GLD 0.40%, SGOL 0.17%, BAR 0.175%)
hold **physical bullion in a vault**. There is no futures contract, no
roll, no contango. The fund's NAV tracks the spot price of gold less the
expense ratio. From 2000 to April 2026 gold went from about $280 to
roughly $3,500 — a wealth multiple in the 12x range, an annualised
nominal return near 10%. Real return over the same window, net of CPI,
is approximately 6-7% per year — anomalous by the long-run gold
literature, driven by central-bank de-dollarisation buying since 2022.

Oil ETFs (USO, BNO, USL) hold futures. From 2000 to April 2026 USO
delivered roughly negative one to two per cent per year — and remember
WTI spot started near $25 in 2000 and is around $70 today, a 2.8x spot
move erased by the roll. The same physical commodity expressed two
different ways produces a 30x divergence in terminal wealth. The chart
makes this concrete.

![Wealth path of $1 invested January 2000 in physical gold (GLDM-equivalent, vault-held bullion) versus USO (front-month WTI futures rolled monthly), through April 2026. Gold compounds to roughly $12 while USO drifts to under $0.50, with the gap visualised as the cumulative cost of the futures roll versus a spot-tracking instrument.](../image/side22_gold_vs_oil.png)

This is the single most important picture in the lesson. Two
"commodities," same starting capital, opposite outcomes — entirely
because of *how the wrapper holds the underlying*.

#### 2.4 Broad-Basket ETFs: PDBC, DBC, BCI, GSG

For investors who do want a diversified commodity sleeve and accept the
roll drag, the menu is:

- **PDBC** (Invesco Optimum Yield Diversified Commodity Strategy
  No-K-1, 0.59% ER, ~$5B AUM) — uses futures with an optimisation
  layer that picks roll dates to minimise contango bleed. Issues a
  1099, not a K-1.
- **DBC** (Invesco DB Commodity Index Tracking, 0.85% ER, K-1) — older,
  similar holdings, larger contango drag.
- **BCI** (abrdn Bloomberg All Commodity Strategy, 0.25% ER, 1099) — the
  cleanest BCOM tracker; smaller AUM ~$1B but adequate liquidity.
- **GSG** (iShares S&P GSCI, 0.75% ER, K-1) — energy-heavy GSCI tracker.
- **COMT, CMDY** — niche alternatives.

All four are US-listed and acceptable. The K-1 issuers
generate paperwork (Schedule K-1 by mid-March; partnership UBTI in IRAs).
The 1099 issuers (PDBC, BCI) are simpler. For sleeves above 5% of
portfolio, BCI is the default.

#### 2.5 The Erb-Harvey Result: Real Return ~ Zero

Claude Erb and Cam Harvey's 2006 paper "The Strategic and Tactical Value
of Commodity Futures" decomposed commodity index returns into three
pieces:

1. **Spot price change** — over 100+ years, real spot prices of most
   commodities have been *flat to negative*. Innovation, substitution,
   and improved extraction win against scarcity over long horizons.
2. **Roll yield** — averages negative for storables (energy, base
   metals) because contango is the structural shape; positive for
   non-storables in tight supply.
3. **Collateral yield** — futures positions earn T-bill rates on the
   posted margin, which is a real rate of zero to one per cent.

Sum the three and the long-run real geometric return of a broad
commodity index is approximately zero — and twenty years of out-of-sample
data since the paper have confirmed it. BCOM's real return 1970 to
April 2026 is approximately -0.5% per year. The diversification benefit
is the entire reason to hold the asset class; the return premium is
not.

This is why size matters. A 5-10% commodity sleeve in a 60/30/10
portfolio adds Sharpe-ratio and inflation-shock resilience without
materially changing expected return. A 30% commodity sleeve drags
expected return down by about 1.5% per year for marginal diversification.
Gold is the special case inside this discipline — it earns its slot
not as a return source but as the store-of-value tier, sized as part
of the four-tranche stack rather than as part of the broad commodity
basket. Two to five percent, no more, held alongside cash, short
Treasuries, and (if you allow yourself) a smaller BTC sliver. The
sizing is small on purpose: a store of value is not an alpha bet,
it is the leg you do not want to look at when everything else is
on fire.

#### 2.6 The Supply-Shock Pattern

The historical pattern is consistent: commodities pay during *supply
shocks*, not during *demand booms* or *steady-state inflation*.

- **1973 oil embargo**: BCOM (proxy: GSCI back-cast) +75% in nominal
  terms, real +60%, while S&P 500 -23% real.
- **2007-2008 commodity supercycle**: BCOM +30% in 2007, then -36% in
  2008 as the crisis broke. Net of the round trip, modest gain.
- **2021-2022 Ukraine + post-COVID supply chains**: BCOM +27% in 2021,
  +14% in 2022 — the only major asset class with a positive 2022 real
  return when stocks lost 18% real and bonds lost 31% nominal.

The lesson is asymmetry: commodities are insurance, not income. They
pay when nothing else does, and they cost a small premium during the
long stretches between shocks.

In Horace's frame this is the vol-tail-wags-dog observation
applied to a different time series. The mean experience of holding
commodities is mild drag. The integral over the rare regime when they
spike is what justifies the slot. Sizing rules:

- Broad basket (BCI or PDBC): 5-10% of portfolio.
- Gold (GLDM/IAU): 2-5% additionally as a separate store-of-value
  sleeve, not as an "inflation hedge." It sits in
  Tranche 3.
- Single-commodity ETFs (USO, UNG, COPX): tactical only, position
  size <1%, treated as event trades not strategic holdings.

---

### 3. Common Misconceptions

1. *"USO tracks the price of oil."* It tracks the front-month WTI
   futures contract, rolled monthly. The decade-long contango drag from
   2009-2020 cost holders roughly half their capital while spot WTI was
   approximately flat.
2. *"Commodities are an inflation hedge."* They are a *supply-shock*
   hedge. During the 2010s when CPI ran 1-2% on demand-side weakness,
   BCOM lost about 35% nominal. Inflation alone is not enough.
3. *"Gold and oil behave the same way as commodities."* GLDM holds
   physical bullion (no roll, no decay). USO holds futures (continuous
   roll). The wrapper mechanics dominate the long-run return.
4. *"The Bloomberg Commodity Index is a broad inflation proxy."* It is
   38% metals, 28% energy, 31% agriculture, 3% livestock. The
   correlation with CPI is regime-dependent — strongly positive during
   supply shocks, near zero in calm periods.
5. *"Commodity ETFs are tax-efficient."* PDBC and BCI use 1099
   structures, but DBC, GSG, USO, and the older funds issue K-1
   partnership forms. UBTI in IRAs becomes a real concern for K-1
   issuers above $1,000 of UBTI.
6. *"Owning commodity-producer stocks is the same as owning
   commodities."* It is not. Producer stocks carry equity beta of
   roughly 1.0 to the market, plus the commodity exposure on top. The
   correlation of XOM to crude is about 0.55; the rest is general
   equity beta.
7. *"Real commodity prices have risen with population growth."* Erb and
   Harvey, and earlier Jacks (2013) reaching back to 1850, document that
   real commodity prices are flat to slightly negative over long
   horizons. Innovation and substitution offset scarcity.
8. *"Gold pays a yield."* Gold pays no yield. Its expected real return
   is approximately the negative of its storage cost — which the ETF
   wrappers absorb into the expense ratio. Long-run real return to gold
   is roughly +1% per year, dominated by occasional re-pricing
   episodes.

---

### 4. Q&A Section

**Q: What is the simplest commodity sleeve for a five-figure portfolio?**
A: Skip broad commodities entirely and hold 3-5% in GLDM. The diversification
benefit of a broad basket at sub-$10k allocations is dominated by transaction
costs and tracking error. Gold via GLDM is one decision, no K-1, and
captures the store-of-value half of the case.

**Q: Why is BCI preferred over DBC for the broad sleeve?**
A: BCI uses a 1099 structure (no K-1 paperwork) and has a 0.25% expense
ratio vs DBC's 0.85%. Over 10 years that 0.6% ER difference compounds to
~6% of NAV for identical exposure.

**Q: Should commodities live in the IRA or the taxable account?**
A: 1099 issuers (PDBC, BCI) are neutral. K-1 issuers should live in
taxable to keep UBTI out of the IRA. Gold ETFs are taxed as collectibles
at 28% federal LTCG when held in taxable — a meaningful penalty over
the 15-20% rate on stocks. Prefer the IRA for gold ETFs.

**Q: Does the 1973-style oil shock still work as a hedge in 2026?**
A: The mechanism is unchanged: a sudden physical-supply disruption
puts the futures curve into backwardation and pushes spot prices
higher. The US is now a net oil exporter, which mutes the *equity*
damage from an oil spike compared to the 1970s but does not change the
commodity payoff itself.

**Q: Can I just hold the producers — XOM, FCX, NEM, ADM?**
A: You can, and the long-run returns are higher than the indexed
basket. The trade-off is correlation: all four carry roughly 0.6-0.8
equity beta to the broad market, so during a recession they fall with
stocks even when commodities themselves are bid. The producers are
*equity exposure with a commodity tilt*, not a commodity hedge.

**Q: Is the Bloomberg Commodity Index investable?**
A: Yes, via BCI, PDBC, COMT, and CMDY among others. None track BCOM
exactly — each picks a slightly different roll methodology. PDBC
explicitly optimises to minimise contango bleed; BCI tracks the
mechanical schedule.

**Q: Does the Erb-Harvey "zero real return" result rule out commodity
allocation?**
A: No. It rules out *expecting* commodities to be a return source. The
case for the sleeve is the diversification benefit during supply
shocks (2008, 2022) and the rebalancing yield from holding an asset
that is occasionally negatively correlated with stocks and bonds at the
same time. Both effects are worth approximately 30-50bp of portfolio
Sharpe ratio improvement.

**Q: How does gold fit if BTC is the new digital store of value?**
A: They serve different niches in Tranche 3. Gold has 5,000 years of
acceptance, deep central-bank demand, and zero protocol risk. BTC has
21M cap and roughly 70% volatility. Sizing rule: 2-5% gold and 1-3%
BTC for the store-of-value sleeve, not one or the other. (Side 09
covers BTC sizing in detail.)

**Q: What is the right rebalancing band for a 5% commodity sleeve?**
A: Rebalance to target whenever the sleeve drifts beyond ±2 percentage
points of weight (i.e. 3% or 7%). This captures the supply-shock
upside (sell into spikes) without churning during the dead-money years.
Annual rebalancing alone misses too much of the spike.

**Q: Why are agricultural commodities barely covered in retail
portfolios?**
A: Because the retail wrapper menu is thin: WEAT, CORN, SOYB, JJG —
all small-AUM, all single-commodity, all K-1. The cleanest expression
of an agricultural view is an equity proxy (DE for ag equipment, ADM
or BG for processing) or accept it as part of a broad-basket
allocation through BCI or PDBC.

**Q: Is the OPEC+ cartel still effective in setting oil prices?**
A: As of April 2026 the answer is "less so." US shale, with break-even
costs near $50 WTI, sets the marginal supply curve. OPEC+ retains
short-term market-management power but the long-run price floor is set
by US producers. This compresses the upside of oil supply shocks
relative to the 1970s.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Commodities, Oil, and Gold — Why USO Lost 50% While
WTI Stayed Flat

**RUNTIME TARGET:** ~12 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 0:45]**

HORACE: Two charts. From January 2000 to April 2026, gold went from
$280 to roughly $3,500. A dollar in physical gold became about twelve
dollars. Same window, USO — the United States Oil Fund — turned a
dollar into less than fifty cents.

STELLA: They're both commodities.

HORACE: They're both *commodities*. They are not both *commodity
exposures*. Today's lesson is the difference, and why it dominates
every other question you have about the asset class.

STELLA: This is Side 22. Gold, oil, agriculture as portfolio
diversifiers. We have two images and one interactive lab.

---

**[SECTION 1 — Four sectors — 0:45 to 2:30]**

HORACE: The Bloomberg Commodity Index — BCOM — is the standard broad
basket. April 2026 weights, roughly: 28% energy, 38% metals, 31%
agriculture, 3% livestock.

STELLA: Each sector has a different driver?

HORACE: Yes, and that's the diversification argument. Energy is OPEC+
plus geopolitics. Industrial metals — copper, aluminium — track global
manufacturing. Agriculture is weather plus planting plus biofuel
mandates. Precious metals — gold and silver — track real rates and
central bank demand.

STELLA: So in 2022, energy was up 35%, ag up 12%, but industrial metals
down 10% and precious metals flat.

HORACE: Exactly. The basket smooths these out. Single-sector ETFs
don't. And put a pin in that forty-point dispersion — when energy
and industrial metals pull apart that hard in one year, that is one
of the cleanest sector-rotation signatures you ever see for free.
Rotation is one of the few alpha sources I have found that holds up
over decades, and the commodity sub-sectors are where the macro
thesis prints in bright colours.

---

**[SECTION 2 — Spot vs futures — 2:30 to 5:00]**

HORACE: Now the mechanics. When you buy USO, you do not own oil. You
own a basket of front-month WTI futures contracts that USO rolls every
month.

STELLA: Roll meaning sell the expiring contract and buy the next one.

HORACE: Right. And here's the problem. If the futures curve is in
contango — next month priced higher than this month — every roll is sell
low buy high. The position bleeds the contango spread.

STELLA: How big is that bleed historically?

HORACE: For oil futures from 2009 to 2020, about minus six to minus
nine per cent per year of pure roll cost. Front-month WTI started
2009 near forty dollars and ended 2020 around forty-eight. Spot was
flat. USO lost roughly half.

[VISUAL: image/side22_gold_vs_oil.png]

STELLA: The chart is brutal. Gold compounds upward, USO drifts down.

HORACE: Same asset class. Same starting capital. Wrapper mechanics
dominate. Gold ETFs hold physical bullion in a vault. There is no roll.
USO holds futures. There is always a roll. The difference compounds for
twenty-six years and produces a thirty-X gap.

STELLA: So if you want oil exposure without the bleed?

HORACE: Producer equities — XOM, CVX. Or LEAPS calls on the producers
if you want leverage with defined risk. Or accept the bleed and treat
USO as a tactical instrument with a hold horizon under three months,
never strategic.

---

**[SECTION 3 — Long-run real return — 5:00 to 7:00]**

HORACE: Now the awkward number. Erb and Harvey, 2006 paper. Decompose
commodity index returns into three pieces. Spot price change. Roll
yield. Collateral yield.

STELLA: And the result was?

HORACE: Real geometric return of a broad commodity index, over a
century-plus window, is approximately zero. Twenty years of follow-up
data have confirmed it. BCOM real return from 1970 to April 2026 is
about minus a half per cent per year.

[VISUAL: image/side22_real_commodities.png]

STELLA: So the picture shows a dollar invested in 1970 in real BCOM
ending up roughly where it started.

HORACE: With two enormous detours — up during the 1970s, up during the
2002-2008 supercycle, down everywhere else.

STELLA: Then why hold them at all?

HORACE: For the supply-shock hedge. 1973, 2007, 2022. They pay when
nothing else pays. Vol-tail-wags-dog, applied to commodities.
The mean experience is mild drag. The rare-regime payoff is what
justifies the slot.

---

**[SECTION 4 — Sizing rules — 7:00 to 9:00]**

HORACE: So how big is the sleeve?

STELLA: Broad basket?

HORACE: Five to ten per cent of total portfolio. BCI for cost and
1099 structure. PDBC if you want the optimised roll layer. Both
acceptable.

STELLA: Gold separately?

HORACE: Two to five per cent additionally. Store-of-value
slot, lives in the third tranche of the four-tranche stack, GLDM
is the default at ten basis points. The size is small on purpose.
Gold is not in the portfolio to win — it is in the portfolio for
the day nothing else does. Treat it that way and the sizing
discipline writes itself.

STELLA: Single-commodity ETFs — USO, UNG, COPX?

HORACE: Tactical only. Position size under one per cent. Treated as
event trades, never strategic holdings.

STELLA: And the rebalancing?

HORACE: Plus or minus two percentage points around the target weight.
Sell into the spike, buy back during the dead-money years. Annual-only
rebalancing misses the fast supply shocks.

---

**[SECTION 5 — Interactive — 9:00 to 11:00]**

HORACE: Pull up the commodity lab.

[VISUAL: interactive/side22_commodity_lab.html]

STELLA: Four sliders — gold weight, broad commodity weight, oil
futures weight, expected inflation regime.

HORACE: Move expected inflation up to seven per cent and watch the
real-return numbers shift. Notice that gold and broad commodities both
strengthen, but oil futures stays anchored — because the contango drag
is structural, not regime-dependent.

STELLA: And if I push the broad commodity sleeve up to thirty per cent?

HORACE: Watch the expected real return number. It compresses the
portfolio by about one and a half per cent per year because broad
commodities have approximately zero long-run real return. You bought
diversification at the cost of return.

STELLA: So the lab makes the trade-off explicit.

HORACE: Right. There is no portfolio where adding twenty-plus per cent
to commodities makes sense unless you are betting on a specific shock
regime. The default is five to ten per cent broad plus two to five
per cent gold. Anything beyond that is a directional view, not a
strategic allocation.

---

**[OUTRO — 11:00 to 12:00]**

STELLA: Three things to remember from Side 22.

HORACE: One. The wrapper dominates. GLDM holds physical bullion.
USO holds futures. The same commodity expressed two different ways
produced a thirty-X divergence over twenty-six years.

STELLA: Two. The Erb-Harvey result. Long-run real return to a broad
commodity basket is approximately zero. The diversification benefit is
real; the return premium is not.

HORACE: Three. Sizing. Five to ten per cent broad. Two to five per cent
gold. Single-commodity ETFs only as tactical event trades. Anything
larger needs a thesis and a stop.

STELLA: Next up — Side 23. See you then.
