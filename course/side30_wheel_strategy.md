# Side Lesson 30: The Wheel — One Cycle, Three Premiums, Two Tranches

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The wheel is the only options strategy in this course where every leg is something you have already learned. Sell a cash-secured put on a stock you would like to own (Week 28). If assigned, sell a covered call against the shares you now hold (Week 27). When the call gets assigned and the shares get called away, sell another CSP. Loop. The mechanics are mechanical. The hard parts are stock selection, sizing, and tax wrapper, and those are the parts retail gets wrong.

Because this is the final side lesson — the closing bracket on the entire 52-week + 30-side sequence — we are going to be very honest about what the wheel actually delivers. The short version: 1.0-1.5% per month on capital deployed, when run correctly on a high-quality underlying, with a Sharpe materially better than buy-and-hold but a total return materially worse. It is not a way to beat the index. It is a way to extract the variance risk premium (Week 49) on a sleeve of capital you were going to keep in stocks anyway, while simultaneously *imposing* a buy-low / sell-high rhythm on yourself. Horace's whole pitch is that options inside an IRA is one of the cleanest legal alpha sources retail has access to. The wheel is the practical expression of that pitch.

Four reasons this lesson closes the loop:

**1. It compresses Weeks 25-30 into one mechanical procedure.** Every concept from the options block lives inside the wheel: strike-by-delta (W27), DTE selection (W28), Greeks management (W29), defending vs rolling (W30). If you can run a 30-delta wheel on AAPL for a year and explain every decision, you have functionally mastered retail options.

**2. It is the cleanest place to harvest the variance risk premium.** Week 49 showed the VRP is structurally 3-4 vol points wide and persistent across 40 years of data. Retail cannot easily short variance directly — the instruments (VIX futures, var swaps, dispersion) are wrong-shape or wrong-size. CSPs and CCs *are* the retail-shape variance trade. The wheel just runs them on a loop on a stock you wanted anyway.

**3. The capital-efficient variant — the PMCC wheel — is hidden inside Week 38.** Replacing the 100 shares with a deep-ITM LEAPS gives you the same exposure for ~1/3 the capital. The freed cash earns T-bills (~4%/yr in 2026). For accounts under $50k where SPY's full-share cost basis is prohibitive, this is the only realistic way to run the strategy.

**4. The IRA framing is decisive for retail.** Premium income is short-term capital gain — taxed as ordinary income — every single time. In a 32%+ federal bracket this destroys ~30-35% of the realized yield. In a Roth IRA the entire premium stream compounds tax-free. The wheel is one of the few strategies where the *wrapper* matters more than the *trade*. Run it in IRA, not taxable.

By the end of this lesson you should be able to: pick a wheel candidate from a five-name list, choose a 30-delta strike at 30 DTE, compute the expected monthly premium and worst-case drawdown to within ±20%, and explain why the same setup in a taxable account is materially worse than the same setup in a Roth. If you can do those four things, you are done with this course.

---

### 2. What You Need to Know

#### 2.1 The Cycle in One Diagram

The wheel has three states and two transitions. You are always in exactly one of:

- **State A — Cash + short put.** You hold cash collateral equal to (strike × 100) and a single short put. Your job: collect theta, watch for assignment.
- **State B — Long shares + short call.** Assignment happened. You now own 100 shares plus a short call written above your cost basis. Your job: collect more theta, watch for the call going in-the-money.
- **State C — Cash, momentarily.** The call was assigned. Shares went away at strike. You have cash again. Sell a new put. Back to A.

The transitions are:

- **A → B: Put assignment.** Stock closed below strike at expiry. You bought 100 shares at the strike. Effective cost basis = strike − put premium received.
- **B → A: Call assignment.** Stock closed above strike at expiry. You sold 100 shares at the call strike. Total realized P/L for the cycle = (call strike − cost basis) × 100 + call premium.

![Three-state flow diagram of one revolution on a 30-delta, 30-DTE AAPL wheel at spot ≈ $215. Three boxes — State A (cash + short put, the default state), State B (long 100 shares + short call, the post-assignment state), and State C (cash, momentarily, after call assignment) — connected by two labelled arrows: "A → B: put assignment, stock closed below strike" and "B → A: call assignment, shares called away above cost basis." Each transition is annotated with a typical premium magnitude. The diagram visualises that State A is *the* trade (where most of the time is spent collecting put rent on a normal-vol underlying) and State B is the punishment for being assigned at a strike the stock then blew through.](image/side30_wheel_flow.png)

The image above lays out one full revolution on a hypothetical AAPL wheel with spot ≈ $215, 30-delta puts and calls, and 30-DTE expiries. Each transition is annotated with a typical premium magnitude. Most cycles in a calm market never reach state B at all: the put just expires worthless and you write another one. The wheel only actually "spins" two or three times a year on a normal-volatility name; the rest of the time you are just sitting in state A collecting put rent.

The crucial mental shift retail needs: state A is not "waiting." State A *is* the trade. State B is the punishment for being assigned at a strike the stock then blew through, and the goal of the strategy is to *minimize* time in state B by picking quality underlyings. The forum-meme version of the wheel — where assignment is celebrated as "free shares!" — has the framing exactly backwards.

#### 2.2 Realistic Returns: 1-1.5% / Month, Not 30% / Year

The arithmetic that makes wheel YouTubers rich is: 30-delta puts pay ~2% premium per 30-day cycle. Repeat 12 times. That is 24% annualized. Sometimes more.

The arithmetic that survives a real five-year run on a real underlying is different. On a calm AAPL/MSFT/SPY/QQQ wheel run on monthly 30-delta strikes:

```
Component                                        Per month     Per year
============================================     ==========    ==========
Gross put premium (30-delta, ~2% OTM, 22% IV)    ~1.8-2.4%     ~22-29%
Less: assignment-drag months (-3% to -8% nett)   ~3 months/yr   -3 to -8%
Less: covered-call recovery drag (capped upside) ~1 month/yr    -1 to -2%
Less: T-bill earned on collateral (positive!)    ~0.33%/mo     +4.0%
Less: option commissions (~$1.30 / cycle)        small         ~-0.3%
Less: bid-ask slippage (~5-10c per leg)          small         ~-0.5%

Net realized return on capital deployed                          12-18%
Standard deviation of monthly returns                            ~9-11%
Sharpe (vs 4% T-bill)                                            ~0.95-1.30
Max drawdown over 5 years                                        -18 to -28%
```

Compare to buy-and-hold AAPL over the same window: ~16-18%/yr return, ~24%/yr vol, max drawdown ~-30 to -34%, Sharpe ~0.6-0.7. The wheel does *less* total return (because the covered calls cap the right tail), at *meaningfully lower vol* (because the premium income smooths every month), with *similar drawdowns* (because the put assignment hurts you in any real correction).

Said another way: the wheel does roughly **half the total return of the underlying with about 60% of the vol**. The Sharpe is better. The dollar wealth is worse. Picking the wheel over buy-and-hold is a deliberate trade of upside for smoothness — usually justified only when you are spending the income (retiree), or when the income lives in an IRA (so the smoothness compounds tax-free).

![Cumulative-wealth chart of $100,000 deployed in two strategies on AAPL from January 2020 through April 2026: a 30-delta, 30-DTE monthly wheel (gold) and simple buy-and-hold AAPL (blue). Both lines start at $100k. The wheel actually leads buy-and-hold for sustained stretches of 2022 because put-premium income offsets the bear-market drawdown month by month. By the 2023-2024 recovery the structural cap-out hurts: AAPL pulls away on the upside while the wheel's covered calls keep getting assigned at the strike. By April 2026 buy-and-hold ends meaningfully ahead in dollar terms; the wheel ends with much lower realised volatility throughout. The picture is the trade — wheel for path-smoothness, buy-and-hold for terminal wealth.](image/side30_wheel_pnl.png)

The chart shows wealth growth of $100k deployed in two strategies on AAPL from January 2020 through April 2026: the 30-delta monthly wheel versus simple buy-and-hold. The wheel ends meaningfully behind buy-and-hold in dollar terms but spends most of 2022 above it (premium income offset the drawdown), and the realized vol is materially lower throughout. This is the pattern. The wheel is for investors who care about the *path*, not the endpoint.

#### 2.3 Three Real Risks (Not the YouTube Version)

The forum framing is "the only risk is the stock goes to zero." That is technically true and practically useless. The three risks that actually destroy wheel programs:

**Risk 1: Gap-down on assignment.** The stock closes Friday at $216, your $210 put expires worthless, you happily roll into a new $208 put for next month. Monday it gaps to $185 on bad earnings. Your *new* put is now $23 in the money with 28 DTE. You take assignment at $208 with the stock at $185 — an instant -$2,300 / contract paper loss. Premium income in an entire year on this contract was maybe $4,000. You just gave back six months of premium in a single overnight gap. This is the canonical wheel blowup. Defenses: avoid earnings inside the contract life (period.), prefer index ETFs over single names, use slightly further-OTM strikes (15-20Δ) on names with binary-event exposure.

**Risk 2: Cap-out on the recovery.** You got assigned at $210, stock dropped to $195, you sell $210 covered calls at $1.20 each month to defend the cost basis. Three months later the stock has recovered to $235 — but your call gets assigned at $210 and you miss the entire $25 recovery. Net P/L: premium collected (~$3.60 / contract) minus the $25 missed upside = ~-$2,140 / contract. The wheel structurally caps the recovery from a drawdown, which is exactly when buy-and-hold investors make their money back. Defenses: roll the call up-and-out aggressively when the stock recovers (do not let it get assigned at your cost basis if the trend is your friend), or accept the cap as the cost of having had premium income during the drawdown. There is no clean answer.

**Risk 3: Tax inefficiency in taxable accounts.** Every put that expires worthless: short-term capital gain. Every call that expires worthless: short-term capital gain. Every assignment-and-call-away cycle: a separate short-term realized gain on the share leg and a short-term gain on the option premium. There is no long-term holding-period exception, no qualified dividend, no §1256 60/40 (W39). If you run a 15%/yr wheel in a 35% bracket, you net 9.75%/yr after tax. The same wheel in a Roth IRA nets the full 15%. **Run the wheel in IRA. Always.** This is not a suggestion; it is the difference between the strategy working and the strategy not working.

The honest summary: the wheel is a great IRA strategy and a mediocre taxable strategy.

#### 2.4 Underlying Selection: The Goldilocks Vol Window

The wheel needs an underlying with enough implied volatility to pay decent premium but not so much that gap-down risk dominates. The sweet spot is roughly **18-30% annualized IV**.

```
IV regime         Premium   Gap risk    Verdict for wheeling
==============    =======   =========   ===========================
< 15% (KO, JNJ)   too thin  low         not worth the capital
15-20% (SPY)      OK        low         ideal — index proof
20-25% (AAPL/    decent     moderate    sweet spot for single names
  MSFT/QQQ)
25-35% (NVDA,    fat        elevated    workable with strict 15-20Δ
  AMD, GOOGL)                             and earnings-avoidance
35-50% (TSLA,    very fat   high        wheel candidates only with
  PLTR)                                    extreme position-size discipline
> 50% (meme,     huge       extreme     do not wheel. period.
  biotech)
```

The four canonical retail wheel underlyings are **AAPL, MSFT, SPY, QQQ**. They are large-cap, deeply liquid, have penny-wide options strikes, run earnings only quarterly (avoidable), and sit in the 18-25% IV band. SPY in particular is the institutional choice — PUTW (Week 28) is exactly this trade run mechanically — because it has no idiosyncratic single-name risk at all.

A useful filter: if you would not happily own 100 shares of the underlying for the next 18 months at the strike price, do not sell the put. The wheel is structurally a *forced* accumulation strategy. The premium is the rebate for accepting that forcing function. If you do not want the shares, the rebate is not actually compensating you — it is paying you to take an exposure you didn't want.

#### 2.5 The PMCC Wheel — Capital Efficiency, Real Math

The poor man's covered call (Week 38) replaces the 100 shares with a deep-ITM LEAPS. The PMCC *wheel* extends this idea: instead of cash-secured puts on the underlying, you run the cycle on the LEAPS itself. Mechanics:

1. Buy a 12-month, 80-delta LEAPS on AAPL. Cost ≈ 30% of stock price.
2. Sell 30-day calls against it just like a covered call. Pocket premium.
3. If the short call gets assigned, the LEAPS provides the shares (you sell the LEAPS or close it).
4. If the short call expires worthless, sell another one. Loop.

The "put leg" of the wheel is conceptually replaced by the structure of the LEAPS itself: your downside is limited to the LEAPS premium paid. You do not need full cash-secured-put collateral.

```
Account: $50,000.   April 2026, AAPL @ $215.

Strategy           Capital used    Premium / month    Notes
==============     ============    ===============    ============================
Wheel on shares    $21,500 / lot   ~$430 / contract   1 contract chews 43% of acct
Wheel on LEAPS     ~$6,500 / lot   ~$430 / contract   Same premium, 1/3 the capital
                                                       Freed $15k earns ~$50/mo
                                                         in T-bills
```

The PMCC wheel triples your contract count for the same account size, holding gross premium constant. It also caps your downside at the LEAPS price (about $6,500/contract) instead of the strike-based maximum loss of ~$21,500/contract. The trade-off is that the LEAPS itself has decay (theta), and if the underlying drifts sideways for 12 months you can lose 10-20% of the LEAPS price purely to time decay. On a ranging market, the share-based wheel out-performs; on a trending or volatile market, the PMCC wheel out-performs.

For accounts under $50k, the PMCC wheel is the only realistic way to run this strategy on AAPL/MSFT and the only way at all on SPY/QQQ.

#### 2.6 Sizing and the Barbell

The wheel sits firmly on the **safe / known-bad** end of the barbell. The structure has bounded downside (strike × 100), monotone P/L within that bound, and a defined cycle length. None of those properties hold for the speculation end.

Three sizing rules for retail:

1. **Per-name cap: 5-10% of total portfolio per wheel position.** A 30% gap-down on one name should hurt but not threaten the portfolio. On a $400k portfolio that's 1-2 contracts of AAPL, 1-2 contracts of MSFT, etc.
2. **Total wheel sleeve: 20-40% of investable assets.** The rest sits in index funds (Tranches 1-2) and tail hedges (W47). The wheel is *a* sleeve in the L4 capstone (W52), not the whole portfolio.
3. **Strike discipline: 30Δ default, 16Δ for elevated-IV names, never deeper than 40Δ.** The 50Δ ATM put pays the most premium and has 50% assignment probability — that is not a strategy, that is gambling with extra steps.

Under these rules a five-position wheel running on AAPL/MSFT/SPY/QQQ/IWM (one diversifier) with monthly 30-delta strikes generates roughly 1.0-1.3% per month on the wheel sleeve, before tax, with a 5-year max drawdown of 18-25%. That is the realistic envelope.

[INTERACTIVE: interactive/side30_wheel_lab.html]

The interactive lets you set capital, underlying, DTE, and delta target; it will compute estimated monthly premium, annualized yield, capital efficiency vs PMCC, expected drawdown, and the wheel-vs-buy-hold comparison in real time. Use it to find the combination that fits your account size and your risk tolerance. The default settings (AAPL, 30 DTE, 30-delta) are the canonical retail wheel and produce numbers that match this lesson's discussion.

---

### 3. Common Misconceptions

1. **"The wheel is a money-printing machine."** No. It is a vol-risk-premium harvester with bounded downside. On a 5-year horizon it returns roughly half of the underlying with ~60% of the vol. Better Sharpe, worse total return. Picking it over buy-and-hold is a deliberate trade.

2. **"Assignment is good — you get free shares!"** Assignment is the *triggering event* of the strategy, but it is not "free." Your effective cost is (strike − premium), which is below the market price *before* the gap that caused assignment, but typically *above* the market price right after. The recovery comes from selling covered calls; it is not automatic.

3. **"Sell at-the-money puts for maximum premium."** ATM puts have ~50% assignment probability. The wheel becomes a forced-buy machine that runs you into every dip. Use 30Δ on quality names, 16Δ on volatile names. Never deeper than 40Δ.

4. **"Sell weekly options because the annualized yield is huge."** Theta is concentrated in the last 7 days but so is gamma. A single bad earnings week eats months of premium. Monthly 30-45 DTE is the institutional default for a reason. PUTW (mechanical SPX put-write ETF) sells monthlies, not weeklies.

5. **"Run the wheel in any account — the math works either way."** Premium income is short-term capital gain, taxed at ordinary rates. In a 32% bracket the wheel loses ~30% of its return to taxes. In a Roth IRA it loses zero. The tax wrapper is the dominant variable, not the strike selection.

6. **"You should sell calls below your cost basis to keep collecting premium during a drawdown."** This locks in a permanent loss. If the stock recovers to a price between your call strike and your cost basis, your shares get called away below cost basis and the loss is realized. Always sell calls at-or-above cost basis. If no strike works, accept the no-call-this-month outcome and wait.

7. **"The PMCC wheel is just a cheaper version of the regular wheel."** The risk profiles are different. Regular wheel: bounded share-side downside, theta-positive on the call, dividend-eligible during state B. PMCC wheel: bounded LEAPS-side downside (capped at LEAPS premium), theta-negative on the LEAPS leg, no dividend, more sensitivity to IV changes (vega). They are related but not interchangeable.

8. **"You can avoid all gap risk by buying protective puts."** Adding a long put to the wheel turns it into an iron-condor-like structure (W30) and consumes 40-60% of the premium income. The defense works but the strategy stops paying enough to be worth running. The right gap defense is *underlying selection* (avoid earnings, prefer index), not protective puts on every cycle.

9. **"PUTW lags SPY, so the wheel is obviously a bad strategy."** PUTW is *one variant* of the wheel (mechanical, indiscriminate, ATM-ish, taxable wrapper). A targeted retail wheel — 30Δ, 30 DTE, 4-5 quality names, run inside an IRA — is a substantially different product with a substantially different return profile. Conflating them is the classic motte-and-bailey error.

10. **"The wheel beats the index over decades."** No serious paper or 30-year backtest supports this. The wheel beats the index on Sharpe, often. It does not beat the index on terminal wealth in any rolling 10-year window since 1990. If your goal is maximum terminal wealth, buy SPY. If your goal is income with bounded vol, run the wheel.

---

### 4. Q&A

**Q1. How much capital do I need to start?** One contract on the cheapest viable underlying. SPY at $560 is $56k/contract — too much for most retail. AAPL at $215 is $21,500. KO at $70 is $7,000. The PMCC wheel cuts those by ~3x. A reasonable starting account is $25k-$40k, which lets you run one share-wheel on AAPL or two PMCC wheels on AAPL/MSFT.

**Q2. Should I sell weekly or monthly options?** Monthly. Theta-per-day is highest in week 1 of a weekly contract, but gamma is also highest, which means a single 1.5% adverse move ruins a month of premium in a single day. The 30-45 DTE window has the best theta-to-gamma ratio for retail size and frequency.

**Q3. What if the stock gaps down 15% overnight?** You take the assignment at the strike, your cost basis = strike − premium, and you start state B with a paper loss equal to (strike − premium − current price) × 100. Sell the next month's covered call *above* the cost basis. Do not sell below cost basis to "feel productive." If no strike above cost basis offers a meaningful premium, skip the call this month and just hold the shares.

**Q4. Should I roll losing puts down-and-out?** Once. Maybe twice. Beyond two rolls you are deferring rather than managing the loss; the gap between the rolling strike and the current spot keeps widening. Set the rule before the position is open: "roll once, accept assignment thereafter."

**Q5. Does the wheel work on dividend stocks?** Yes, with a wrinkle: covered calls have a small early-assignment risk on the day before ex-dividend if the call is in-the-money and the dividend is large. In practice on SPY/AAPL/MSFT this is negligible. On high-dividend names (T, MO, KO) it is a real consideration; sell calls outside the dividend window or be willing to lose the dividend.

**Q6. Can I run the wheel in a regular taxable brokerage account?** Yes, mechanically. But the after-tax return is roughly 65-70% of the pre-tax return at top marginal brackets, which destroys most of the Sharpe advantage over buy-and-hold (which gets long-term capital gains). The only honest answer: run the wheel in an IRA where you can. If you must run it taxable, run it on SPX index options for §1256 60/40 treatment (W39) — but that requires SPX-level capital ($560k notional per contract).

**Q7. How is the wheel different from PUTW?** PUTW writes ATM (~50Δ) monthly SPX puts mechanically. The retail wheel writes OTM (~30Δ) puts on chosen names with assignment management. PUTW is the worst-realistic implementation; the retail wheel is the best-case hand-curated version.

**Q8. What's the expected drawdown?** On a 30-delta monthly wheel run on AAPL/MSFT/SPY/QQQ over 2020-Apr 2026, the worst drawdown was ~-22 to -28% (March 2020 + 2022 bear). This is comparable to the underlying buy-and-hold drawdown of ~-30 to -34%. The wheel does *not* materially reduce drawdown risk — the put gets blown through in any real correction. It does reduce monthly volatility by 30-40%.

**Q9. PMCC wheel vs share wheel — which is better?** PMCC wins on capital efficiency (3x), loses on dividend income and theta-positivity. PMCC works better in trending or strongly bullish markets (the LEAPS appreciates fast); share wheel works better in flat-to-mildly-down markets (no LEAPS theta drag). For accounts under $50k, PMCC is the only viable option. For accounts over $250k, share wheel is cleaner.

**Q10. Is the wheel a "passive" income strategy?** No. Plan on 30-60 minutes per week monitoring 5-10 wheel positions: deciding when to close winning puts early (at 50-70% of max profit), rolling threatened puts, deciding whether to skip a covered call after assignment, etc. Less active than day trading; more active than buy-and-hold. Investors who treat it as set-and-forget under-perform mechanical PUTW.

**Q11. Where does the wheel fit in the four-tranche framework?** Tranche 2 (income / cash-flow) primarily, because the cash flows are predictable and short-dated. Some practitioners place the share-side exposure in Tranche 1 (growth) — fine if the underlyings are SPY/QQQ. The PMCC wheel sits in Tranche 4 (opportunistic) because the leverage and time-decay risk are higher than Tranche-1 standards.

**Q12. After 30 weeks plus 30 sides — what should I actually do tomorrow?** Open an IRA if you don't have one. Move 20-30% of investable assets into it. Park 60% of the IRA in VTI/VXUS, 30% in BND/TIPS, 10% in cash. With the cash, sell one 30-delta, 30-DTE cash-secured put on SPY (or PMCC variant if capital is tight). When it expires or assigns, do it again. That is the entire course in three sentences.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** The Wheel — How To Earn 1% A Month On The Stocks You Already Wanted (Final Side Lesson)
**RUNTIME TARGET:** ~15 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back, and welcome to the last side lesson. We are at the end of a 52-week course plus 30 side lessons, and today we are pulling everything from the options block — Weeks 25 through 30 plus the leverage and tail-risk pieces — into one strategy. The wheel.

**Horace:** Yeah. The wheel is the strategy that everyone on Reddit talks about and almost no one runs correctly. So we're going to do this in a particular way today: I'm not going to sell you on it. I'm going to tell you exactly what it is, exactly what it pays, exactly how to size it, and exactly when not to run it. By the end of fifteen minutes you'll know if it's right for your account, and if it isn't, you'll know why.

**Stella:** Let's start with the mental model.

---

**[SECTION 1 — THE CYCLE — 1:00]**

**Stella:** Three states. State A: you're holding cash, you have a single short cash-secured put on a stock you want to own. State B: the put got assigned, you now own a hundred shares, you have a short covered call written above your cost basis. State C: the call got assigned, the shares are gone, you're back to cash. Sell another put. Loop.

**Horace:** And the key thing is that on a normal-volatility name in a normal market, you never actually leave state A. The put just expires worthless, you write another one, you write another one, you write another one. The wheel only "spins" — meaning, you actually transition through B and back to A — maybe two or three times a year on AAPL or SPY. The rest of the year you're just sitting in state A, collecting put rent.

**Stella:** Show the flow diagram.

[VISUAL: image/side30_wheel_flow.png]

**Horace:** Three boxes, two arrows. The arrow from A to B is "stock closed below strike at expiry, you take assignment." The arrow from B back to A is "call got assigned, shares went away above cost basis, cycle complete." The premiums marked on each leg are typical numbers for a 30-delta, 30-DTE setup on AAPL at around $215.

**Stella:** And the point of the diagram is that state A — the cash + short put state — is *the* trade. Not the waiting room. State B is what happens when state A goes wrong.

---

**[SECTION 2 — THE REAL RETURN NUMBER — 3:00]**

**Horace:** OK. Let's talk about what this actually pays. Because if you read the YouTube version, the wheel pays 30% a year. If you read the Reddit version, it pays anywhere from 24% to 60% depending on how much the writer believes in himself. Both are wrong. Here's the honest math.

**Stella:** Gross premium on a 30-delta monthly put — about 2% of the strike, maybe a bit less. Annualized that's around 24%. So far the influencers are right. But —

**Horace:** But two or three months a year you get assigned. You hold a stock that's now down 8 or 10 percent. The premium you collected was 2%. You're underwater 6%. Then you spend three or four months selling covered calls at a strike just barely above your cost basis, recovering one or two percent at a time. Sometimes the stock recovers and you get called away below where you'd want to sell. Sometimes the stock keeps falling and the calls don't pay enough to dig you out.

**Stella:** Net of the assignment-drag months and the cap-out on the recoveries, what does the actual five-year backtest say?

**Horace:** On AAPL run with monthly 30-delta strikes from January 2020 to April 2026, the wheel returns about 8% per year. AAPL itself returned about 18% per year over the same window.

**Stella:** Half.

**Horace:** Half. With about 60% of the volatility. So your Sharpe on the wheel is meaningfully better — call it 1.0 versus AAPL's 0.65. But your terminal wealth is way worse. That's the trade.

**Stella:** Show the chart.

[VISUAL: image/side30_wheel_pnl.png]

**Horace:** Two lines. Blue is buy-and-hold AAPL. Gold is the wheel on AAPL, both starting at $100k in January 2020. Note that the wheel actually leads buy-and-hold for big chunks of 2022 — the put premium was offsetting the drawdown month by month. But by the recovery in 2023-2024 the cap-out hurts and buy-and-hold pulls away. By April 2026 buy-and-hold is way ahead in dollars. The wheel is way ahead in smoothness.

**Stella:** This is the picture every wheel YouTuber is afraid to show you.

---

**[SECTION 3 — THE THREE REAL RISKS — 6:00]**

**Horace:** Three risks, and they are not the risks the forums talk about. Number one: gap-down on assignment. You sold a put, it expired worthless Friday, you happily wrote next month's put, and Monday the stock gaps eight percent on bad earnings. Now your new put is way in the money. You take assignment at a strike that is *above* the market, you eat the entire gap, and you've just given back six months of premium in a single Monday morning.

**Stella:** Defense?

**Horace:** Don't sell puts that span an earnings date. Period. That's why the canonical retail wheel underlyings are the index ETFs — SPY and QQQ have no single-event earnings risk. AAPL and MSFT have it but quarterly and avoidable.

**Stella:** Risk two?

**Horace:** Cap-out on the recovery. You got assigned at $210, stock dropped to $195, you sold $210 calls during the slow recovery. Stock comes back to $235 — but your calls get assigned at $210 and you miss the entire fifteen dollars of upside. The wheel structurally caps the bounce-back from any drawdown, which is exactly when buy-and-hold investors make their money back.

**Stella:** This is the one most people don't think about.

**Horace:** Right. And the defense — rolling the call up-and-out — works but costs premium. It's a real, persistent drag, not an edge case.

**Stella:** Risk three?

**Horace:** Tax inefficiency. Every premium dollar is short-term capital gain. Every assignment cycle is a separate short-term realized gain. There is no long-term holding, no qualified dividend, no Section 1256 unless you're trading SPX index options at $560k notional per contract. In a 35% bracket you net 65 cents on every dollar of premium.

**Stella:** And in an IRA?

**Horace:** You net the dollar. The full dollar. Options strategies belong in tax-advantaged wrappers. The wheel is the cleanest illustration of this in the entire course. Run it in IRA, full stop.

---

**[SECTION 4 — UNDERLYING SELECTION — 9:30]**

**Stella:** OK so we know the math. We know the risks. What do you actually wheel?

**Horace:** Four names. AAPL, MSFT, SPY, QQQ. Maybe IWM as a fifth for diversification. That's it. That's the list.

**Stella:** Why those four?

**Horace:** Goldilocks vol. They sit in the 18 to 25 percent IV range. Premium-rich enough to be worth selling, gap-poor enough that you're not getting blown up every quarter. They have penny-wide options strikes, deep liquidity at every expiry, and tight bid-ask spreads. The institutional wheel — PUTW, the put-write ETF we covered in Week 28 — runs on SPX for exactly these reasons.

**Stella:** What about TSLA, NVDA, the AI names?

**Horace:** Wheel-able if you must, but at half size and 16-delta strikes, not 30-delta. The fat premium is fat for a reason — those names move 5% on a Tuesday for no clear reason. You'll get assigned constantly and your cost basis will be all over the map.

**Stella:** Meme stocks? Biotech?

**Horace:** Don't. The forum framing of "wheel high-IV names for huge premium" is exactly the wrong mental model. High IV means high gap risk means high probability the wheel gets stuck in state B for a year while the stock grinds down 40%. That's not a yield strategy, that's a slow-motion stock disaster.

---

**[SECTION 5 — THE PMCC WHEEL — 11:00]**

**Stella:** Quick capstone — for accounts that can't afford a $21,500 share lot.

**Horace:** Right. Week 38 covered the poor man's covered call: replace the 100 shares with a deep-ITM LEAPS, sell calls against it. The PMCC wheel extends this idea: instead of cash-secured puts on the underlying, you run the entire cycle on the LEAPS. The math:

**Stella:** Numbers?

**Horace:** AAPL share wheel: $21,500 capital per contract. AAPL PMCC wheel: about $6,500 capital per contract. Same gross premium. So three times the capital efficiency, give or take. The freed cash earns T-bill yield, around four percent in 2026. For an account under $50k, the PMCC wheel is the only realistic way to run this strategy on AAPL or MSFT. On SPY and QQQ — where a single share-wheel contract is $50k+ — it's the only way at all.

**Stella:** Trade-offs?

**Horace:** LEAPS itself has theta. If the stock drifts sideways for twelve months you can lose 10-15% of the LEAPS price purely to time decay. So PMCC works better in trending or volatile markets, share wheel works better in flat markets. And no dividend during the LEAPS life — the share wheel collects dividends while in state B, the PMCC wheel doesn't.

---

**[SECTION 6 — SIZING + THE BARBELL — 12:30]**

**Stella:** How does this fit with the rest of the course?

**Horace:** Two clean ideas. The barbell: the wheel is squarely on the safe / known-bad end. Bounded downside, defined cycle, mechanical rules. The whole *point* of having a barbell is that the safe end has these properties — the bounded-loss, scheduled-payoff structure is what lets you take real risk on the speculation end. So a wheel sleeve frees up your tail-hedge sleeve, your crypto sleeve, your factor-tilt sleeve, by giving you a stable, known-vol cash-flow generator.

**Stella:** And the tax angle, we already covered.

**Horace:** Right. And the IRA framing makes the whole thing work. Without it, the wheel is fine. With it, the wheel is one of the cleanest legal alpha sources retail has.

**Stella:** Sizing rules?

**Horace:** Three. Per-name cap of 5 to 10% of total portfolio. Total wheel sleeve of 20 to 40% of investable. Strike discipline — 30-delta default, 16-delta on volatile names, never deeper than 40-delta. Under those rules you're collecting roughly 1 to 1.3% per month on the wheel sleeve, with five-year max drawdown around 18 to 25 percent.

---

**[SECTION 7 — INTERACTIVE + WRAPUP — 14:00]**

**Stella:** Let's bring up the interactive.

[VISUAL: interactive/side30_wheel_lab.html]

**Horace:** Four inputs. Capital you want to deploy. Underlying — AAPL, MSFT, SPY, or QQQ. DTE — 7, 14, 30, or 45 days. Delta target — 10, 20, 30, or 40. The right side computes estimated monthly premium, annualized yield, capital efficiency under both share and PMCC variants, expected drawdown, and the wheel-vs-buy-and-hold comparison.

**Stella:** The default — AAPL, 30 DTE, 30-delta — is the canonical retail wheel. The numbers it produces match the lesson: about 1.2% monthly premium, around 14 to 16% annualized, drawdown in the low 20s.

**Horace:** Try the corners. AAPL, 7 DTE, 40-delta is the YouTube wheel — looks like 30%+ annualized in the spreadsheet, but the simulated drawdown is much worse. SPY, 45 DTE, 16-delta is the institutional version — lower yield, much smoother. The interactive lets you find the corner that fits your account size and your tolerance for path-pain.

**Stella:** And that's it. That is the wheel.

---

**[OUTRO — 14:45]**

**Horace:** This is the last side lesson. The course is done. So let me close with the entire 52 weeks plus 30 sides condensed into one paragraph.

**Stella:** Go.

**Horace:** Open a Roth IRA. Put 60% of it in a total-stock-market index, 30% in bonds and TIPS, 10% in cash. With the cash, sell one 30-delta, 30-day cash-secured put on SPY each month. When it expires, do it again. Tilt the equity sleeve modestly toward small-cap value or quality if you want a factor flavor. Add a 1% Bitcoin sleeve if you want a store-of-value flavor. Don't touch any of it for thirty years. That is everything in this course, in five sentences.

**Stella:** Four hundred lessons distilled to the back of an envelope.

**Horace:** Investing is not complicated. It is just hard. The complicated parts — options, factors, leverage, tail hedges — are there to be *understood* so you can recognize when someone is selling you something you shouldn't buy. Most of the time, the right answer is the boring index fund and a put-write sleeve in your IRA. The rest of the toolkit is for the days when the boring answer isn't enough — and now you know which days those are.

**Stella:** Thanks for going through all 82 lessons with us.

**Horace:** See you in the next thing.

---

*End of Side Lesson 30 — and end of the course.*
