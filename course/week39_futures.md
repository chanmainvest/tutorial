# Week 39: Futures — Micro E-mini, /MES, /MNQ, /MCL, Contango, and Section 1256

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Futures are the oldest derivatives in the world. Cotton merchants in 1860s New Orleans, wheat farmers in 1880s Chicago, and Saudi crude desks in 1990s London all priced their goods on the same fundamental contract — *I owe you 1,000 barrels (or bushels, or index points) on a fixed date at a fixed price, settled to cash daily*. For 130 years that machine was sealed off from retail. The minimum contract size on the S&P 500 e-mini was $250,000 of notional with a $12,000 margin requirement; on crude oil it was 1,000 barrels at a $5,000 margin. You needed a five-figure subaccount to even try one position. Then in 2019 the CME launched the **Micro E-mini** (MES, 1/10th the size of ES) and the **Micro WTI** (MCL, 1/10th the size of CL), and what had been an institutional product became a retail one. As of April 2026 a single MES contract has roughly $25,000 of notional exposure and about $2,000 of initial margin. That is the size where it makes sense for a $50-100k brokerage account to consider it.

There are four reasons a Level-3 student needs to learn this lesson now.

1. **Futures are the cleanest leverage in the toolkit.** A long /MES is roughly 12-13x leverage on the cash you post as margin, with no margin interest, no overnight financing line, no maintenance call against the rest of your portfolio (other than the position itself), and no ETF expense ratio. Compare to SSO at 2x with 0.9% drag plus volatility decay (week 37), or to a LEAPS at 4x with extrinsic decay. Futures are the highest-leverage, lowest-cost way to express a directional view on the major indices.
2. **Section 1256 tax treatment.** This is one of the two great tax-efficient leverage anchors in the entire course (the other is the long-LEAPS). Broad-based index futures and a small set of index options are taxed under §1256 of the IRC: **60% long-term capital gain, 40% short-term, regardless of holding period.** A day-trade in /MES is taxed *better* than a day-trade in SPY, period. For high-bracket investors that is a 7-12 percentage point structural edge per dollar of gain.
3. **Contango and backwardation explain the USO story you met in week 6.** Crude oil ETFs, natural-gas ETFs, and VIX ETFs all roll a futures position monthly. When the curve is in contango — back month higher than front — the roll is a permanent drag on return. USO lost roughly 80% of its value in real terms 2009-2020 while spot WTI was essentially flat, almost entirely because of contango roll yield. You cannot understand commodity ETFs without understanding the futures curve, and the only way to fix the problem (when you actually want commodity exposure) is to take it through the futures themselves rather than through the wrapper.
4. **The barbell needs a portable-exposure lever.** When the L1 sleeve is held in deep-ITM LEAPS and the L3 sleeve is generating cash from credit spreads (week 30), you sometimes want to flex aggregate beta up or down by 10-20 percentage points overnight. /MES is the right tool: post $2k of margin, control $25k of S&P exposure, taxed at 60/40, expires in three months. The position is sized in single-digit contracts, lasts a quarter, and rolls cleanly. SPY round-trips cost taxes; /MES round-trips do not, structurally.

This lesson is the operational manual for that fourth use case — and the cautionary tale for the first three regimes (over-leverage, contango drag, and the small-but-real path-dependence risk of daily mark-to-market).

---

### 2. What You Need to Know

#### 2.1 What a Futures Contract Actually Is

A futures contract is a standardised, exchange-traded agreement to exchange a fixed quantity of an underlying asset at a fixed price on a fixed future date. Unlike an option, **both parties are obligated**. Unlike a forward, the contract is *standardised* and *cleared centrally*, so counterparty risk runs to the exchange (CME), not to the trader on the other side.

Three concrete examples used throughout this lesson:

- **/ES (E-mini S&P 500):** $50 per index point. With the S&P 500 at 5,200 in April 2026, one /ES contract has notional $50 × 5,200 = **$260,000**. Initial margin: about $14,000 (5.4%). Tick size: 0.25 index points = $12.50.
- **/MES (Micro E-mini S&P 500):** $5 per index point. Notional $26,000. Initial margin: about $2,000 (7.7%). Tick: 0.25 points = $1.25. **This is the contract a $50-100k account uses.**
- **/MNQ (Micro E-mini Nasdaq-100):** $2 per index point. With the Nasdaq-100 at 19,000, notional $38,000. Initial margin: about $3,300. Tick: 0.25 points = $0.50.
- **/MCL (Micro WTI Crude Oil):** 100 barrels per contract. With WTI at $72/bbl, notional $7,200. Initial margin: about $750. Tick: $0.01 = $1.00.
- **/MGC (Micro Gold):** 10 troy ounces per contract. With gold at $2,400/oz, notional $24,000. Initial margin: about $1,500. Tick: $0.10 = $1.00.

Equity-index futures are **cash-settled** at expiration — there is no physical delivery of 500 stocks. Crude and gold are **physically deliverable**; you must close or roll before the last trading day or you will be assigned a barge of barrels (in practice, every retail broker auto-liquidates 2-3 days before expiration).

#### 2.2 Notional vs Initial Margin — Why Leverage Is 12-15x by Default

In stocks, when you "buy on margin," your broker lends you cash; the security itself is collateral, and you pay interest on the loan. **Futures margin is not a loan.** It is a *performance bond* — a refundable deposit the exchange holds to ensure you can settle the day's loss. The CME sets *initial margin* (what you must post to open) and *maintenance margin* (what you must keep above to avoid a call). Brokers can charge slightly more.

![Bar chart comparing the capital required to obtain $50,000 of S&P 500 economic exposure across four vehicles — direct SPY shares, two /MES Micro E-mini contracts, one full /ES E-mini contract (oversized at $260k notional), and a 0.92Δ 12-month SPY LEAPS. SPY shares require the full $50,000 (1.0x leverage). Two /MES require ~$4,000 of posted margin for ~$52,000 of exposure (~12.5x leverage). One /ES is oversized for the target. The LEAPS uses ~$10,000 of premium for ~$52,000 of exposure (~5x). The orange overlay on each non-share bar shows the freed cash that earns risk-free T-bill yield. The chart is the visual proof that futures are the highest-leverage, lowest-capital path to S&P exposure.](image/week39_micro_compare.png)

The chart above asks one question: *what is the cheapest way to control $50,000 of S&P 500 economic exposure?*

- **SPY shares:** $50,000. 1.0x leverage. Direct cost.
- **One MES contract:** notional $26,000 × ~2 contracts ≈ $50,000 exposure for ~$4,000 of margin. **~12.5x leverage.**
- **One ES contract:** $260,000 of notional, oversized for a $50k target — uses ~$14,000 of margin to control 5x the exposure. The wrong tool below $200k of intended position size; you cannot dial in finely.
- **One LEAPS at 0.92Δ on SPY (week 37):** ~$10,000 of premium for $52,000 of exposure. ~5x leverage.

The futures path uses 1/12th the capital of the share path. The freed cash sits in T-bills earning 4.3% (April 2026), exactly as in the LEAPS chapter — but with a 60/40 tax envelope on the futures gain rather than long-term capital gains on the shares.

The cost: **mark-to-market**. Every trading day at 4 p.m. CT, the exchange computes your gain or loss and sweeps it from your account in cash, even if you have not closed. If MES drops 100 points overnight (a 2% move) on a 2-contract position, your account loses $1,000 by the next morning's open. With a $4,000 margin balance that is a 25% drawdown of the posted collateral; if the move is 200 points you receive a margin call before lunch. **Leverage works in both directions, and the daily settlement is real cash — not a paper number.**

#### 2.3 The Futures Curve: Contango and Backwardation

The price of the December crude contract is rarely the same as the price of the October contract, even when both reference the same barrel of West Texas Intermediate. The shape of that **term structure** is the most important thing a commodity-futures investor watches.

![Two-line chart of WTI crude prices ~2010 through 2024: a blue line for the front-month CL contract (essentially spot oil) and an orange line for the 12-months-out deferred contract, with the area between them shaded as the contango/backwardation spread. When orange sits above blue (most of the period) the curve is in contango — the shaded area is positive and is the per-month roll cost USO eats. The April 2020 super-contango spike — when storage at Cushing ran out and front-month CL settled at -$37 while December-2020 traded near $30 — appears as a vertical blowout of the spread. The 2022 Russia–Ukraine episode shows orange briefly diving below blue (deep backwardation, +$30+ spot premium). The chart is the mechanical explanation for why USO compounded at -8%/yr through 2009-2020 while spot WTI was roughly flat.](image/week39_contango_uso.png)

- **Contango:** back-month price > front-month price > spot. The market is paying you to delay delivery. This is the "normal" shape for storable commodities — the back-month price has to compensate the seller for storage cost, financing cost, and the lost opportunity of selling spot today. Crude oil is in contango about 60-70% of the time historically. The chart above shows the canonical 2015-2016 oil-glut episode and the 2020 super-contango — back-month minus front-month spread blew out to $30/bbl in April 2020 when storage at Cushing OK ran out and the front-month CL contract famously settled at *negative* $37 at expiration.
- **Backwardation:** spot > front-month > back-month. The market is paying you to take delivery *now*. This happens when there is an immediate physical shortage — the **convenience yield** of holding the actual barrel in your tank exceeds the cost of carry. Crude was deeply backwardated in 2022 when Russia invaded Ukraine and prompt-month physical traded $20+ above the 12-month contract.

The relationship between curve shape and commodity-ETF performance is exact and unforgiving. USO, the largest oil ETF, holds rolling front-month CL futures. Every month it sells the expiring contract and buys the next one. **In contango, that round-trip is a guaranteed loss** — you sell the cheap front for the expensive back, and pay the spread every roll. The 2009-2020 USO chart is the single best illustration of this drag in financial history: spot WTI averaged roughly $60/bbl across that period, but USO compounded *negatively* at -8% per year. Contango ate roughly 4-6% per year, persistent and unrecoverable, year after year.

The fix, if you actually want crude exposure: hold the **December-2027 contract** (or even further out), not the front month. The deferred contract has a flatter roll. Better yet, hold it in the futures account itself — no ETF wrapper, no expense ratio, and the §1256 tax treatment instead of the K-1 partnership tax form USO ships out every year.

#### 2.4 Section 1256: The 60/40 Rule

This is the tax-efficient-leverage capstone. Almost all retail-tradeable index futures (/ES, /MES, /NQ, /MNQ, /YM, /RTY, /CL, /MCL, /GC, /MGC) and a narrow set of broad-based index options (SPX, RUT, NDX) are classified under Section 1256 of the Internal Revenue Code. The treatment is unique and entirely favourable:

1. **All gains are taxed 60% long-term, 40% short-term, regardless of holding period.** A two-day swing trade in /MES is taxed at the same blended rate as a multi-year position. For a 32% ordinary / 15% LTCG investor, the blended rate is 0.60 × 15% + 0.40 × 32% = **21.8%**. Compare to a short-term equity gain at 32%, or a single-stock option gain held under a year at 32%. The structural edge is roughly 10 percentage points per dollar.
2. **Mark-to-market at year-end.** All open §1256 positions are marked to market on December 31 and the unrealised P&L is reported on Form 6781 as if the positions were closed and reopened. This is the same treatment as the broker reports daily; you do not pick up a phantom gain you did not see.
3. **Loss carryback.** §1256 losses can be carried back **three years** (rare in tax) against §1256 gains, in addition to forward-carry. Equity capital losses can only carry forward.

For a worked example: a $20,000 gain in /MES held over six months. Under §1256, $12,000 is taxed at LTCG (15-20%) and $8,000 at ordinary (32-37%). Total tax at 32% bracket: $12,000 × 15% + $8,000 × 32% = $1,800 + $2,560 = **$4,360**, an effective rate of 21.8%. The same $20,000 gain on SPY held six months would be all short-term at 32% = $6,400. **Difference: $2,040, or 10.2% of the gain itself.** Over a career of active trading that compounds into real money, and it is the single biggest reason desks that trade index exposure structurally do it through futures rather than through ETFs.

#### 2.5 Roll Mechanics

Futures expire. The active /MES contract rolls quarterly: March, June, September, December (the "front month" letters H, M, U, Z respectively). About a week before expiration, **liquidity migrates** from the expiring contract to the next quarterly. The roll itself is mechanical: sell the expiring contract, buy the next quarterly, in a single calendar-spread order that pays the (usually small, for index futures) basis differential.

For equity-index futures the roll cost is structurally tiny — typically 5-15 basis points per quarter (driven by the cost-of-carry: short-rate minus dividend yield × 0.25). On /MES at 5,200, that is 2-8 index points. For an investor holding /MES as portable beta exposure, the all-in annual roll friction is roughly **0.20-0.60% per year** — far cheaper than the LEAPS extrinsic (~2-3%/yr) or the SSO drag (~3-4%/yr).

For commodities, roll cost depends entirely on curve shape. In contango, every roll is a loss (you saw this above for USO). In backwardation, every roll is a gain — which is exactly why commodity hedge funds prefer to be long oil only when the curve is backwardated. The signal is observable on the screen; you do not have to forecast it.

#### 2.6 /MES vs SPY for Portable Equity Exposure

A practical comparison for a $100,000 account that wants $30,000 of S&P 500 beta as part of its L2 strategy sleeve.

| Vehicle | Capital used | Tax on 1-year +20% gain | Annual carry cost |
|---|---|---|---|
| 30 SPY shares × $520 | $15,600 (need $30k) | LTCG 15% on $6,000 = $900 | None (small div) |
| 1 /MES at 5,200 | ~$2,000 margin (controls $26k) | §1256 21.8% on $5,200 = $1,134 | Roll ~0.30% × $26k = $78 |
| 1 LEAPS 0.92Δ SPY | ~$5,000 premium (controls $30k) | LTCG 15% on $6,000 = $900 | Extrinsic ~2.5% × $30k = $750 |

For one-year hold periods, all three are within ~$300 of each other on after-tax-and-cost return. For *under-one-year* hold periods, /MES dominates: §1256 is the only one of the three that does not pay short-term capital gains rates. This is why active rotation across the L2 sleeve uses /MES and not SPY — you are making 6-8 round trips a year and the tax math is different by 10 percentage points each one.

The honest caveat: /MES requires a Tier 2 futures-cleared brokerage account (CME-approved broker, separate margin paperwork, $5-25k minimum at most retail brokers), an understanding of the 24-hour session (most volume is during the 9:30 a.m.-4:00 p.m. ET overlap with cash equities; off-hours liquidity gets thin and slippage gets ugly), and the discipline to not over-size. The leverage is 12-15x by default. If you treat a 2-contract /MES position the way you treat a 10-share SPY position, you will lose your account on a normal Tuesday.

Try the [Futures Lab](interactive/week39_futures_lab.html) to see how product, contract count, account size, and a single monthly move shape your notional exposure, margin used, gross P&L, leverage ratio, and after-tax 60/40 P&L. The §1256 box is the lever that matters most over a career of active trading.

---

### 3. Common Misconceptions

1. **"Futures are gambling."** Naked /ES at 50x leverage is gambling. Sized /MES at 1-3 contracts on a $100k account at 0.3-0.8x portfolio leverage is portable beta exposure. Same instrument family — same difference between a 0.30Δ weekly and a 0.92Δ LEAPS in the option world.
2. **"Futures margin is a loan."** It is not. It is a performance bond held by the exchange. There is no interest charge. The "leverage" is a function of position size relative to posted margin, not borrowing.
3. **"Contango is a temporary thing."** Crude has been in contango for roughly two-thirds of its history since 1983. It is the *normal* shape of a storable commodity curve. Backwardation is the rarer state.
4. **"USO went to zero because of fraud."** USO's underperformance is mechanical: roll yield in a chronically contangoed curve. No fraud, no fund-level mistake — the wrapper itself is structurally short the futures basis. Same with UNG (natural gas) and VXX (VIX).
5. **"Section 1256 only applies if I hold for a year."** False. Section 1256 60/40 applies regardless of holding period. A trade open for 30 minutes and closed at a profit is taxed identically to a position held three years. That is the entire point.
6. **"I should use /ES because it's more liquid than /MES."** /MES is plenty liquid (>1M contracts/day) for any retail-sized position. The "more liquid" argument matters when you need to move 1,000 contracts at once. For 1-10 contracts, /MES vs /ES is a tick or two of slippage difference, and the position-sizing flexibility of /MES is worth it.
7. **"Futures don't pay dividends, so they're worse than stocks."** The dividend is *embedded* in the price difference between the futures and the spot index. The futures curve discounts forward expected dividends; you do not lose them, you just receive them as price-return rather than cash.
8. **"24-hour markets means I can trade anytime."** Most off-hours liquidity is institutional hedging flow. Spreads widen 3-10x outside the 9:30-16:00 ET window. Trade in the cash session unless you have a specific reason not to.
9. **"§1256 means I never owe ordinary tax on futures."** False. 40% of §1256 gain is ordinary. The benefit is the 60% LTCG portion regardless of holding period — which on multi-year holds is *worse* than equity LTCG (where 100% would be long-term).
10. **"A leveraged ETF is the same thing as a futures position."** Wrong on three counts: ETFs reset daily and decay (week 37); ETF gains are taxed at equity rates with no §1256; ETF expense ratios are 0.7-1.0% drag while futures roll cost is 0.2-0.6%. Futures dominate for active rotation.

---

### 4. Q&A Section

**Q1. How much account size do I need to trade /MES?**
Most brokers (TastyTrade, IBKR, Schwab Futures) require $2,000-5,000 minimum to enable futures trading and clear ~$2,000 initial margin per /MES contract. Practical floor is roughly $25,000 — that gives you room for 2-3 contracts plus the discipline buffer to absorb a 10% drawdown without margin call.

**Q2. What's the daily mark-to-market mean for my taxes?**
On the brokerage statement you see daily P&L sweeps. For tax purposes, only year-end positions are mark-to-market under §1256 (Form 6781). Closed trades are realised normally. The two reports reconcile.

**Q3. Can I trade futures in a Roth IRA?**
Yes — TastyTrade, IBKR, Schwab all offer futures-cleared IRAs. There is no margin call risk in an IRA the way there is in a regular margin account, but you cannot replenish a margin shortfall mid-day, so brokers typically require 1.5-2x normal margin in IRAs. The §1256 tax benefit is moot in an IRA (no tax on anything), but the leverage and execution are still useful.

**Q4. What's the difference between /MES and SPX (the index option)?**
SPX is a European-style cash-settled index option, also taxed under §1256. /MES is the futures contract. SPX is for option-strategy exposure (spreads, condors); /MES is for delta-1 directional exposure. Both are 60/40 taxed.

**Q5. How often should I roll /MES?**
On the Thursday before the third Friday of expiration month — that is when liquidity has migrated to the next quarterly contract. Your broker will warn you a week in advance. Do not let it expire; the cash settlement to the index print will lock in whatever the open print happens to be.

**Q6. What happens if I get a margin call on /MES?**
The broker will liquidate enough of your position to bring you back above maintenance margin, often the same day, often without warning. Futures margin calls are not the 30-day "send a check" calls of the equities world. Maintain at least 1.5x initial margin in your account and you will essentially never see one.

**Q7. Why is contango worse for some commodities than others?**
Storage cost dominates. Crude (storable, but expensive to store offshore) is moderately contangoed. Natural gas (very expensive to store, seasonal demand) is severely contangoed in summer. Metals (cheap to store) are mildly contangoed. Live cattle (impossible to store cheaply) is often backwardated. The cost-of-carry formula tells you the magnitude.

**Q8. Can I express a "long volatility" view through /MES?**
No — /MES is delta-1 on the index. For long-vol exposure you need /VX (VIX futures) or VIX options. /VX has its own contango problem (futures price > spot VIX about 80% of the time), which is why VXX bleeds 30-60%/year in normal markets.

**Q9. How does this fit with the four-tranche framework?**
/MES is a portable-beta lever for the L1 sleeve: when the 60/40 portfolio is at 55% equity and you want 65% for a quarter, post $4-6k of margin and add 2 /MES contracts. Cheaper than rebalancing into SPY (taxes), faster than waiting for the next contribution.

**Q10. What's a reasonable position size in /MES?**
A useful rule: size such that a 5% adverse move in the underlying index does not exceed 10% of your liquid net worth. For a $100k account that means roughly 4 /MES contracts max ($104k notional), and most active retail traders I respect run 1-2.

**Q11. Why does Horace mention tax treatment specifically here?**
Because §1256 60/40 is the cleanest tax treatment any retail US investor can get on directional speculation. You do not have to hold for a year. You do not have to harvest losses. You do not have to navigate wash-sale rules. The 21.8% blended rate at the 32% bracket is a structural gift from the 1981 tax code, and it has not been touched since — it is the single most under-appreciated thing in the US retail tax code.

**Q12. When does this strategy fail?**
Three regimes. (1) **Over-leverage:** sizing /MES based on margin posted instead of notional controlled — the classic blow-up. (2) **Holding commodity futures long-term in contango:** /MCL or /MNG decay through roll just like USO/UNG. (3) **Off-hours trading on news:** spreads widen 5x+ at 3 a.m. ET; the slippage on a 50-point /MES move during off-hours can exceed the move itself.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Futures, Contango, and the 60/40 Tax Trick — /MES, /MNQ, /MCL Explained

**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Welcome back to the Chan Investing tutorial. I'm Stella, and today we're on Week 39 — futures markets. Specifically the micro contracts that opened this universe up to retail since 2019: /MES, /MNQ, /MCL, /MGC. Horace, you've called §1256 60/40 tax treatment "one of the most under-appreciated gifts in the US tax code." That's a strong claim. Walk me through why we care.

**Horace:** Three reasons that all matter at once. First, leverage. A single Micro E-mini S&P contract controls $26,000 of index exposure on $2,000 of posted margin. That is 13x, with no interest charge. Second, the tax treatment — 60% of every gain is long-term capital gain, 40% is short-term, regardless of how long you hold. Even if you close in 30 minutes. There is no other instrument family in the US that gets that treatment. And third, the contango lesson — once you understand how the futures curve shapes the price of contracts month-to-month, the entire commodity-ETF universe becomes legible. USO's eighty-percent underperformance from 2009 to 2020 was not a mystery; it was contango, every month, working against the wrapper.

**Stella:** Today we'll work through two charts and one interactive. The first chart shows what $50,000 of S&P 500 exposure costs through different vehicles. The second is the contango story applied to crude oil. Let's start with the capital-required chart.

**[SECTION 1 — MICRO COMPARE CHART, 1:30-5:30]**

**[VISUAL: image/week39_micro_compare.png]**

**Horace:** This chart asks a simple question. I want $50,000 of S&P 500 economic exposure. What is the cheapest way to get it? The first bar is shares — the obvious one. SPY at $520, ninety-six shares, $50,000. One-to-one capital deployed. No leverage.

**Stella:** And the second bar?

**Horace:** Two MES contracts. Each one controls about $26,000 of index. Two contracts gets us to $52,000 of exposure for about $4,000 of posted margin. That is roughly 12-and-a-half times leverage on the cash. The remaining $46,000 of capital sits in T-bills earning 4.3 percent — a structural return the share-buyer does not capture, because their fifty grand is fully deployed.

**Stella:** The third bar is one /ES contract.

**Horace:** Right. One full E-mini controls $260,000 of notional. Way oversized for a $50k target. You cannot dial in finely with /ES. Below about $200,000 of intended position size, /ES is the wrong tool — the granularity is one contract, and one contract is too big. /MES exists to solve that exact problem.

**Stella:** And the fourth bar — the LEAPS.

**Horace:** A 0.92-delta LEAPS at the 80%-of-spot strike, twelve months out — which is what we covered in Week 37. Roughly $10,000 of premium for $52,000 of exposure. About five-times leverage, with the trade-off of a small extrinsic decay over the year and a lower tax efficiency than the futures path.

**Stella:** So the punchline of this chart is that futures are the highest-leverage, lowest-capital way to control S&P exposure.

**Horace:** Yes — and the lowest-tax-rate, if you actively rotate the position. The cost of that leverage is daily mark-to-market. Every day at 4 p.m. Central, the exchange sweeps your gain or your loss in cash. There is no holding through a 10-percent drawdown the way you can with shares; if you have not posted the margin, the broker liquidates. Leverage is a tool. It cuts both ways. But the *cost-per-unit-of-leverage* is unambiguously the lowest of any instrument in the retail toolkit.

**[SECTION 2 — CONTANGO AND THE USO STORY, 5:30-10:30]**

**Stella:** Let's pull up the second chart. This one is the contango story.

**[VISUAL: image/week39_contango_uso.png]**

**Horace:** The blue line is front-month WTI crude — what spot oil is trading at today, basically. The orange line is the twelve-months-out crude contract. The shaded area between them is the spread — back-month minus front-month. When orange is above blue, the curve is in contango. When orange is below blue, it is in backwardation.

**Stella:** And the giant spike in early 2020.

**Horace:** That is the famous super-contango of April 2020. Storage at Cushing, Oklahoma — the delivery point for WTI — was full. There was nowhere to put physical barrels. Front-month crude actually settled at *negative* $37 a barrel for one day, while the December contract was at $30. The spread blew out to $30+ a barrel. That episode, more than any other, is why USO had to restructure its holdings — they could no longer hold the front month without taking actual physical delivery they had no place to store.

**Stella:** And the backwardation in 2022?

**Horace:** Russia invaded Ukraine, the prompt-month physical market was tight, refiners needed barrels *now*, the December contract was at $80 while front-month was at $115. Orange below blue. Anyone holding deferred contracts during that period had a structural tailwind — you sell the cheap deferred and buy the expensive front, every roll is a gain.

**Stella:** And the takeaway for retail investors who want oil exposure?

**Horace:** Three options. One, USO and its peers — never. The wrapper is structurally short the basis. Over the entire 2009-2020 period, spot WTI was roughly flat in real terms while USO compounded at minus 8 percent per year. That's contango eating the wrapper, every month, without recovery. Two, energy equities — XLE, XOM, CVX — which give you operational leverage to oil but also management quality, capital allocation, and dividend yield. Different exposure. Three, hold the futures yourself — buy the December-2027 contract instead of the front-month, and the roll is much flatter. The deferred curve compresses. That is the institutional way to express a long-oil view.

**Stella:** And §1256 makes that third path tax-efficient even if you are rotating quarterly.

**Horace:** Exactly. Sixty percent long-term, forty percent short-term, regardless of holding period. That is the tax-efficient-leverage capstone — the most tax-efficient leverage available to a US retail investor is either deep-ITM LEAPS or §1256-eligible futures. Those are the two instruments. Everything else has worse tax geometry.

**[SECTION 3 — INTERACTIVE WALKTHROUGH, 10:30-15:30]**

**Stella:** Let's go to the interactive — the Futures Lab.

**[VISUAL: interactive/week39_futures_lab.html]**

**Horace:** Pick a product. Default is /MES. You can switch to /MNQ for Nasdaq, /MCL for crude, /MGC for gold. Each one has its own contract size, tick value, and typical margin. The lab knows them.

**Stella:** And the sliders?

**Horace:** Number of contracts traded. Account size — your total liquid brokerage balance. Expected monthly move in the underlying as a percentage. The lab computes notional exposure, margin used as percent of account, gross P&L on the move, leverage ratio, and the after-tax P&L using the 60/40 split at your bracket.

**Stella:** Walk me through a realistic example.

**Horace:** Sure. Account: $100,000. /MES, three contracts. Each contract $26,000 notional, so $78,000 of S&P exposure. Margin used: about $6,000, six percent of the account. That is the leverage I would call sane for a Level-3 retail account — call it 0.78x portfolio leverage, modest. Now move the monthly slider to plus 4 percent. P&L is 4 percent of $78,000 = $3,120. After tax at 60/40 in the 32 percent bracket: roughly $2,440 net. That is 2.4 percent on the account in a single month, on what was originally a sleep-at-night position.

**Stella:** And the same trade in SPY?

**Horace:** $78,000 of SPY shares. Same 4 percent gain — $3,120. But all of that, if you close inside a year, is short-term gain at 32 percent. Tax: about $1,000. Net: $2,120. The futures path delivers about $320 more on the same gain — and that is just one trade. Run that math six times a year and the futures path is a structural couple-of-points-per-year better than the shares path on after-tax return.

**Stella:** Now drag the move slider to minus 4 percent.

**Horace:** Same arithmetic in reverse. P&L of negative $3,120, marked to market the next morning, swept from the account in cash. Margin used is still six percent of the account, so you are nowhere near a margin call. But the cash hits your statement immediately — there is no "I'll wait for the position to come back" in futures. Every morning you wake up to either a positive or a negative cash entry from the exchange, and that is the discipline futures forces on you that shares do not.

**Stella:** What happens if I dial up the contracts to ten?

**Horace:** Notional jumps to $260,000 against a $100,000 account. That is 2.6x portfolio leverage. Margin used is now 20 percent of the account. A 4 percent adverse move in the index is a $10,400 loss — 10 percent of the account in one day. A 7 percent move is essentially the rest of your margin buffer. Ten contracts on a $100k account is the fast lane to a margin call. The lab makes that visible without you having to actually take the loss.

**[SECTION 4 — RISKS AND WHEN NOT TO USE FUTURES, 15:30-17:00]**

**Stella:** Talk me through the failure modes. This is leverage.

**Horace:** Four. First, position sizing by margin instead of notional. New futures traders see the $2,000 margin number and think "I can afford ten of those." No. You can afford ten of those by *posting* margin. You cannot afford ten of those when the index drops 3 percent on a Sunday-night ES gap. Always size by notional relative to net worth. Second, holding commodity futures long-term in contango. /MCL works for a directional view across a few months when the curve is favourable; it does not work as a buy-and-hold the way SPY does. Third, off-hours trading on news. Spreads widen 5 to 10x outside the cash session. The slippage on a fifty-point /MES move at 3 a.m. Eastern can be larger than the move itself. Trade in the regular session. Fourth, treating the §1256 tax benefit as a reason to over-trade. The structural edge is real — but if you turn over your portfolio twenty times a year just to capture it, you will spend it on commissions and bid-ask. The tax benefit is a passive feature; do not let it drive trading frequency.

**Stella:** And when does futures *clearly* belong in the toolkit?

**Horace:** Three situations. One, portable beta — flexing the L1 equity allocation up or down by 5 to 15 percentage points for a quarter without rebalancing the underlying portfolio and triggering capital gains. Two, hedging a concentrated position — short /MES against a tech-heavy portfolio for the duration of a specific event. Three, expressing a tactical commodity view — long /MGC for a quarter on a real-rates thesis, where the §1256 envelope makes the tax cost roughly half what a comparable equity rotation would be. Outside those three, futures are a curiosity, not a sleeve.

**[OUTRO — 17:00-17:30]**

**Stella:** Next week we get to Week 40, which is forex and the dollar trade. After that, the L4 alternatives chapters — REITs, MLPs, crypto, private equity. Stay tuned.

**Horace:** And remember — leverage is a tool. The §1256 tax envelope is a gift. Position size is the discipline. The first two only matter if you respect the third.

**Stella:** Thanks for watching. See you next week.
