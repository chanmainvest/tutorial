# Week 28: Cash-Secured Puts — Getting Paid to Bid Lower

---

## Part 1: Reading Section

---

### 1. Why This Is Important

A cash-secured put (CSP) is the most honest trade in retail options. You set aside cash equal to the full purchase price of 100 shares, you tell the market "I will buy this stock at $X if it ever trades there in the next 30 days," and the market pays you a few hundred dollars for leaving that bid sitting on the screen. If the stock falls to your level, you buy it — at exactly the price you wanted, minus the premium. If it does not, you keep the cash and write another one. There is no leverage, no naked exposure, no fancy theory. It is a limit-buy order with rent attached.

Most retail traders meet CSPs through bad influencers who pitch them as a yield-farming machine — "earn 30% annualized on your idle cash!" That framing is broken. The right framing, the one Horace uses in this lesson, is **CSPs are how you bid on stocks you already want to own.** The premium is not your edge. The discount-to-where-you-actually-wanted-to-buy is your edge. If you find yourself selling puts on stocks you would refuse to take delivery of, you are no longer running CSPs — you are running a casino with extra steps, and the dealer eventually catches up.

Four reasons this lesson matters:

**1. CSPs are the cleanest way to express patience.** Markets reward investors who can wait. Most retail investors cannot — they buy when CNBC is loud and freeze when the screen is red. A CSP locks in your discipline. The strike is your patience price. The 30-day expiry is your timeout. The premium is your reward for not chasing.

**2. They convert idle cash into yield without taking equity risk you didn't already plan to take.** If you were going to keep $20,000 ready to buy SPY at a 5% pullback anyway, you can do exactly that *and* collect $200-$400/month while the cash waits. The cash itself stays in T-bills earning around 4% (April 2026). The put premium is an additive layer, not a replacement.

**3. Most CSPs you'd actually want to be assigned.** This is the single insight that separates serious CSP sellers from yield-chasers. A CSP is structurally a "limit buy at strike, with a rebate." If assignment scares you, you sold the wrong put on the wrong stock. The barbell puts CSPs squarely on the safe end — they are how you accumulate the boring index/quality positions that anchor a portfolio. You are not trying to *avoid* assignment; you are trying to *price* it.

**4. They live cleanly inside the options-tax doctrine.** Like covered calls, CSP premium income is short-term capital gain regardless of how long you held the contract. That makes CSPs a tax-disaster in a taxable brokerage account if you run them at scale, and a beautiful tool inside a Roth or traditional IRA where the short-term character vanishes. Same rule we hit in Week 27: option income lives in tax-sheltered accounts. Stocks-you-want-to-own live anywhere.

This is a doer's lesson. By the end of it you should be able to look at SPY at $560, decide you'd happily own it at $530, find the 30-delta put that strikes near $530, and know within ten seconds whether the premium is worth the capital lockup.

---

### 2. What You Need to Know

#### 2.1 The Mental Model: A Limit Buy With a Rebate

Stop thinking "sell a put." Start thinking **"resting limit-buy order, paid to stay on the book."**

A regular limit-buy order at $530 on SPY does nothing for you. It sits there. If SPY trades to $530 your order fills; if not, it cancels at the end of the day and you do it again tomorrow. You pay nothing, you earn nothing.

A 30-day cash-secured put at the $530 strike is the same buy intention with three modifications:

1. The order stays alive for 30 days, not one day.
2. You commit the cash up front — it cannot be used for anything else until the put expires or you close it.
3. Someone pays you a premium for taking on that 30-day commitment.

That is it. The premium compensates you for two things the regular limit order does not give the market: a **time commitment** (you can't cancel without buying back the contract) and a **firm floor under price** (you must take delivery at the strike if it trades through, even if the stock is much lower).

The first commitment is real but small in dollar terms. The second is the one that matters: you are short volatility. If SPY goes to $400 in a crash, you still buy at $530 — and the market knows this, which is why VIX-rich environments pay much more premium than calm ones. The vol tail wags the equity dog directly here: the price you get for a CSP is not really about your stock thesis, it is about how scared *other* people are about the next 30 days.

![Bar chart of annualized premium yield (in %) on a 30-day cash-secured put as a function of target put-delta — 10Δ, 16Δ, 25Δ, 30Δ, 40Δ, 50Δ — computed from Black-Scholes on a $100 stock with sigma = 22% and r = 4%. Each bar is colored cool-to-hot from blue (10Δ, deepest OTM, lowest yield) through to red and purple (40Δ, 50Δ, near-the-money, highest yield), and is annotated with both the yield and the implied strike with OTM%. The 50-delta bar is roughly 6× the height of the 10-delta bar; the footer makes explicit that higher yield is the price of higher assignment risk, not edge.](../image/week28_csp_yield_curve.png)

The image above shows the annualized premium yield on a 30-day SPY-like put as a function of strike-delta, computed from Black-Scholes with sigma = 22% and r = 4%. The bars climb steeply as you move closer to the money: the 50-delta (at-the-money) put pays roughly 6x the annualized yield of a 10-delta put. But that 50-delta put has a ~50% chance of finishing in-the-money. The yield is not free; it is the probability of assignment, dressed up.

#### 2.2 Strike Selection by Delta

Delta in this context approximates the option's probability of finishing in-the-money. A 30-delta put has roughly a 30% chance of being assigned at expiry, and (loosely) sits around 5% out-of-the-money for a 30-day contract on a normal-volatility stock.

Three working presets, each tied to a temperament:

```
30-delta CSP (standard):
  - About 5-7% out-of-the-money for 30-day, sigma=22%
  - ~30% assignment probability
  - Highest premium of the three presets
  - For: investors who actually want to accumulate the stock

16-delta CSP (one standard deviation):
  - About 9-11% OTM, ~16% assignment probability
  - Roughly half the premium of the 30-delta
  - Sweet spot for most beginners — your bid is far enough below
    the market that assignment feels like a real bargain

10-delta CSP (conservative):
  - About 13-15% OTM, ~10% assignment probability
  - About one-third the premium of the 30-delta
  - For: investors who view the put as pure rent on cash and would
    only welcome assignment in a meaningful drawdown
```

Beginners almost always start with the 30-delta because the premium is largest and the temptation is to maximize income. This is the single most common mistake in retail CSP-land. The 30-delta put on a stock you do not really want to own is not income — it is a loaded coin flip where heads pays $200 and tails costs you $5,000. Start at 16-delta and only move closer when you have a stock and price you are *eager* to be filled at.

#### 2.3 Tenor: Why 30-45 Days

Theta (time decay) is non-linear. In the last 30 days of an option's life, decay accelerates sharply. From 60 days out to 30 days out, a put loses roughly 30% of its time value; from 30 days to expiry, it loses the remaining 70%. As a seller, you want to be camped in the steep part of the curve.

```
Tenor          Premium    Daily Theta    Annualized Yield-on-Cash
=========      =======    ===========    ========================
7 days         lowest     highest        very high (but unstable)
14 days        low        high           high
30 days        medium     medium-high    sweet spot
45 days        higher     medium         sweet spot
60 days        higher     lower          mediocre
90 days        highest    lowest         poor
```

The 7-day weeklies look attractive in spreadsheets — you're rolling four times per month, theta is screaming — but the realized P/L is brutal because gap-risk is concentrated. One earnings miss or one Fed surprise inside that week, and you eat a full month of premium in a single move. The 30-45 day window is where the decay/gap-risk tradeoff is best for retail, and it happens to match the natural monthly options expiration cycle.

#### 2.4 Capital Cost — The Hidden Half of the Yield

Every CSP locks up cash equal to (strike x 100). That cash is *not* dead. Inside any modern broker (IBKR, Fidelity, Schwab as of April 2026), the cash collateral on a short put earns one of:

- T-bill yield in a money-market sweep (~4.0%, April 2026 SOFR)
- Margin-account credit interest (varies)
- A government MMF position the broker permits as collateral

So the **total** yield-on-cash for a CSP is:

```
Total yield = T-bill yield (cash collateral) + put premium yield (option)
            ~= 4.0%/yr + (premium / strike) * (365 / DTE)
```

A 30-day, 16-delta SPY put yielding 0.4% in premium therefore returns roughly 4.0% + 0.4% x 12 = **8.8% annualized** on a no-assignment cycle. This is the number you compare against. It is not 4.8% (premium only, ignoring cash interest), and it is not 30%-something (annualizing the premium without subtracting taxes and assignment cost). Always quote yields *including* the T-bill leg.

This matters for the regime you live in: in the 1990s when T-bills paid 0%, CSP yields looked huge by comparison. In 2026 with T-bills at 4%, the *incremental* yield from selling puts is the only thing worth measuring, and it is much smaller than uninformed YouTubers claim.

#### 2.5 Rolling and Defending — Rules, Not Vibes

A put is "threatened" when the underlying drops to (or below) your strike with significant time left. You have four moves at any moment:

1. **Do nothing — accept assignment.** This is correct if you genuinely want the stock at the effective price (strike - premium). It is the *default* answer for index CSPs.

2. **Buy to close at a profit.** Once the put has lost 50-70% of its premium with significant time left (typically before the last 7 days), close it. You have captured most of the theta; the remaining premium is not worth the gamma risk.

3. **Roll down and out.** If assignment looks likely but you still don't want the stock at this strike, buy back the threatened put and sell a new put at a *lower* strike, *further* dated, for a small net credit. You have moved your bid lower and bought time. Do this at most once or twice — endless rolling turns CSPs into a pyramid scheme of deferred losses.

4. **Take the L and close at a loss.** If your thesis on the stock has changed and you no longer want to be assigned, close the put at whatever loss the market gives you. Cash-secured puts have *bounded* losses (strike x 100 is the worst case), but bounded does not mean small.

```
Defensive playbook (mechanical version):

  Trigger                              Action
  =================================    ===============================
  Put at 50% of max profit, >7 DTE     Buy to close, redeploy
  Put at 80% of max profit             Always close
  Stock at strike, 14+ DTE             Hold; let it work
  Stock 5% below strike, 7 DTE         Decide: take assignment or roll
  Stock 10% below strike, any DTE      Take the assignment unless thesis dead
  Earnings inside the contract life    Avoid in the first place
```

Notice: there is no rule that says "double down" or "average into a losing put." Selling another put at the same strike when the first one is underwater is doubling exposure to a stock that the market disagrees with you about. The market can stay below your strike longer than you can stay willing to wear the loss, especially if you keep adding — irrationality outlasts solvency more often than the spreadsheet admits.

#### 2.6 Assignment Psychology — You're Buying, Not Losing

For most retail CSP traders the panic moment is the morning after assignment, when 100 shares of stock appear in the account at a price that is now above the market. The mental frame matters here.

Assignment is **not** a loss event. It is the buy order you placed 30 days ago, executing exactly as designed.

If your 16-delta SPY $530 put was assigned because SPY closed at $528, you bought 100 shares of SPY at $530, pocketed $300 in premium for the trouble, and your effective cost is $527 — *better* than the market price the day you wrote the put, *better* than the market price the day you were assigned. You executed your patience plan exactly. The only loss scenario is if you panic-sell those shares the next day at $520. The shares are not the loss; the panic is.

The right next move after assignment is almost always to **start writing covered calls on the assigned shares** — Week 27's playbook. The wheel (CSP -> assignment -> covered call -> call-away -> CSP) is the natural cycle. You bought the dip and now collect rent on the way back up.

The only stocks where assignment is genuinely bad are the ones you should not have written CSPs on in the first place: meme stocks, single biotechs, leveraged ETFs, anything you would not buy outright at the strike.

#### 2.7 PUTW: The CSP Strategy as an ETF

WisdomTree PUTW (CBOE S&P 500 PutWrite Index Fund) is the institutional version of this lesson. It mechanically sells 1-month, ~2% out-of-the-money SPX puts, fully cash-secured, every month. It exists to settle the question "does systematically writing puts beat just owning the index?"

![Line chart comparing cumulative growth of $1 invested at year-end 2015 in WisdomTree PUTW (gold line, systematic 1-month ~2% OTM SPX put-write) vs SPY (blue line, S&P 500 total-return ETF), 2016 through 2024. Markers at each year-end; major drawdown years (2018, 2020, 2022) shaded in light red. SPY ends near $3.10 (CAGR ~12%/yr); PUTW ends near $1.85 (CAGR ~7%/yr). Final wealth and CAGR are labelled at the right end of each line. PUTW lags in melt-up years and loses less in drawdowns, but trails SPY by roughly 5%/yr over the full cycle.](../image/week28_putw_vs_spy.png)

The chart shows cumulative growth of $1 invested in PUTW vs SPY from January 2016 to December 2024. The numbers (April 2026 vintage):

- PUTW: ~7% per year, max drawdown about -22% in March 2020
- SPY: ~12% per year, max drawdown about -34% in March 2020

PUTW captured the put premium consistently and weathered 2018, 2020, and 2022 with smaller drawdowns than SPY. But in the 2017, 2019, 2021, and 2023 melt-ups, the cap on upside is structural: the put premium is a few percent per month, but SPY can rip 5%+ in a month and PUTW only collects the put premium, not the underlying gain. Over a full cycle PUTW lags SPY in total return, lags more in bull years, and outperforms only in flat or modestly down years.

The takeaway: systematic CSP-writing is real, defensible, and inferior to plain index ownership in a normal expansion. The reason a thoughtful investor still does CSPs is **not** to beat SPY on total return. It is to (a) build cash positions into specific names you want to own, (b) generate income inside an IRA where the tax drag of the equivalent stock-trade strategy would be worse, and (c) lower portfolio volatility while accepting a modest return drag.

If you are tempted to think "PUTW lags SPY -> CSPs are bad," you have misunderstood the trade. PUTW is mechanical, indiscriminate, and pays a fixed expense ratio. Targeted CSPs on stocks you want to own at prices you want to own them at are a different animal.

#### 2.8 Tax Treatment — Same Rule as Week 27

Premium from short puts is short-term capital gain when the option expires worthless or is bought to close, regardless of how long the put was open. There is no long-term holding-period exception.

```
Outcome                         Tax treatment
============================    ==============================
Put expires worthless           STCG on full premium received
Put bought to close at profit   STCG on (received - paid)
Put bought to close at loss     STCL (offsets STCG/long-term gains)
Put assigned -> stock taken     Premium reduces cost basis of the
                                  shares; holding period for the
                                  shares starts on assignment day
```

In a taxable account at a 35-37% top bracket, a CSP yielding 5% per year in premium is netting ~3.2% after tax. Inside a Roth IRA, it's netting 5%. The entire short-vol toolkit only makes sense in a tax-sheltered wrapper for high earners. In a regular brokerage, you are running options strategies for the IRS's benefit.

The interactive below walks the math for any combination of underlying, delta, and DTE in real time.

[INTERACTIVE: interactive/week28_put_writer.html]

---

### 3. Common Misconceptions

1. **"CSPs are free money / yield-farming."** They are not. The premium is the market's price for taking on a defined drawdown risk. Annualizing 30-day premium and quoting "30% yield!" hides the fact that the realized yield includes the assignment outcomes, which are negative when they happen.

2. **"You should never let a put get assigned."** Backwards. On a stock you want to own, assignment is the *intended* outcome. Aggressively rolling away from assignment on every dip turns a buy-the-pullback strategy into a perpetual-rent strategy that eventually catches a 20% drop you can't roll out of.

3. **"30-delta is the standard, so I should sell 30-deltas."** 30-delta is the standard for a reason — the premium is meaningful — but only on names you genuinely want to own. On an index where you would happily accumulate at any pullback, sure. On a single stock you are lukewarm about, 16-delta is more honest.

4. **"Selling weeklies is more profitable because you do it 4x as often."** Daily theta is highest in the last 7 days, but so is gamma. Weekly puts get destroyed by single-day gaps far more than monthlies, which is why systematic put-writers (including PUTW) almost always sell ~30-day, not 7-day.

5. **"PUTW lags SPY, so CSPs are useless."** PUTW is a mechanical indiscriminate seller of OTM SPX puts. A thoughtful CSP program is targeted, opportunistic, and used to acquire shares — not to maximize total return. They are different products solving different problems.

6. **"The put premium is my profit."** The premium is your gross income. Your *profit* is premium net of (a) the cost of capital tied up in collateral, (b) the realized losses from assignments at strikes above market, and (c) taxes. Most retail CSP traders track only the premium and are confused by their account balance two years in.

7. **"Cash-secured means there's no risk."** Cash-secured means you cannot lose more than (strike x 100) per contract. That is *bounded* risk, not zero risk. A $530 SPY put has $53,000 of capital at risk if SPY goes to zero. Bounded does not equal small.

8. **"I can just roll forever if it goes against me."** Rolls work for one or two cycles and only against shallow moves. In a real correction (2008, 2020, 2022) put strikes get blown through so fast that the rolls keep moving lower without ever recovering, and you end up with the original loss plus several months of additional theta you paid to defer it.

9. **"Selling puts is the same as buying stock at the strike."** Almost, but not quite. The put seller does not benefit from upside above the strike. The stock buyer does. This is why CSPs in a melt-up market lag long stock by exactly the missed upside.

10. **"IV crush is good for me."** Yes, if you are already short the put. But the implication that you should write puts whenever VIX is high is dangerous — VIX is high because realized vol is *also* high, and your put is more likely to be assigned. The right framing is "premium is fairly priced; sell what you actually want to own."

---

### 4. Q&A

**Q1. How much capital do I need to start running CSPs?**
At least enough to cover 100 shares of one underlying you want to own. For SPY at $560 that's $56,000 per contract. For KO at $70 that's $7,000. Beginners should start with one underlying, one contract, and an account size where one assignment doesn't dominate the portfolio — a rough rule is no contract should require more than 10-15% of total portfolio cash.

**Q2. How is a CSP different from a naked put?**
Mechanically the option position is identical. The difference is the collateral. A cash-secured put has 100% of the strike-exposure in cash. A naked put uses margin — you might post only 20-25% of the notional, leveraging 4-5x. Naked puts magnify both income and assignment risk; they are not a beginner trade and not what this lesson covers.

**Q3. What underlyings work best?**
Liquid index ETFs (SPY, QQQ, IWM), large-cap quality names you would actually own (AAPL, MSFT, KO, JPM, BRK.B), and ideally with weekly+monthly options chains. Avoid: single-name biotech, recent IPOs, stocks under $20, leveraged/inverse ETFs, anything with binary catalysts inside the contract life.

**Q4. Should I avoid earnings?**
Generally yes for single names. Earnings inflate IV and pay you more premium, but they also inflate the gap risk. Selling a put through earnings is a directional bet on the earnings reaction — fine if you actually wanted that bet, dangerous if you thought you were collecting "rent." Index CSPs don't have this problem (no single earnings).

**Q5. What if the stock gaps below my strike overnight?**
You take the assignment at the strike. Your effective cost is still (strike - premium), and you bought 100 shares at exactly the price you committed to 30 days ago. Yes, the market is now below that, which is uncomfortable, but it is not different from your original plan. Either you wanted the stock at that price or you didn't.

**Q6. Can I sell CSPs in a margin account?**
Yes, and most modern brokers will route the cash collateral to a money-market sweep so it earns T-bill yield while it's tied up. You can also sell *naked* puts in a margin account, which is different — see Q2.

**Q7. How do CSPs interact with the wash-sale rule?**
If you take a loss on shares and within 30 days sell a put on the same security with a strike close to the original purchase price, the IRS may treat it as a wash sale and disallow the loss. The exact line depends on facts and circumstances. Consult a tax pro if you are running CSPs alongside loss-harvesting on the same names.

**Q8. Is there any scenario where a CSP outperforms just buying the stock?**
Yes — flat or modestly down markets. If SPY ends the month exactly where it started, the long-stock holder made $0 and the CSP-seller made the full premium. If SPY drops 1%, long stock is down 1% and the CSP-seller is up roughly (premium - 1%). In strongly up markets (above strike + premium) long stock wins; in strongly down markets both lose, with CSP losing slightly less by the premium.

**Q9. Why is the 30-day implied volatility relevant when I only care about the premium?**
The premium *is* the IV — Black-Scholes with everything else fixed maps premium to vol one-to-one. When you compare CSPs across names, you are implicitly choosing which IV you are short. Higher IV = higher premium = higher realized vol = higher chance of assignment. There is no free yield-arbitrage here.

**Q10. What's a sensible starting cadence?**
One contract per month per underlying you want to accumulate, on a 30-45 DTE 16-delta strike. Re-evaluate after 6-12 months. The point is *not* to maximize the number of trades; it is to systematically accumulate target positions at target prices while collecting incremental yield.

**Q11. Do I need to actively manage these or can I let them expire?**
You can let them expire if your thesis hasn't changed and the put is far out of the money near expiry. The half-decent rule is: if at 7 DTE the put has lost 80%+ of its initial premium, just close it for the small remaining cost — you free up capital and remove gamma risk for the last week.

**Q12. How does this fit into the barbell?**
CSPs on index ETFs and quality compounders are unambiguously **safe-end** activity. They build positions you wanted anyway, pay you to wait, and have bounded downside. CSPs on volatile single names with binary outcomes are **speculation-end** activity. The mistake is mixing the two — using safe-end framing to justify selling 30-delta puts on a meme stock. Separate them in your head and in your account.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Cash-Secured Puts — Getting Paid to Bid Lower (Week 28)
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. Last week we covered selling calls on stock you already own — the income side of the wheel. This week we're doing the *other* side: cash-secured puts. The one most retail investors get sold the wrong way.

**Horace:** Yeah, the YouTube version of CSPs is a guy in front of a Lambo telling you to "earn 30% on your idle cash." And I want to spend the first thirty seconds being very direct about this: that framing is wrong. The CSP is not a yield-farming trick. It's a limit-buy order with a rebate. If you remember nothing else from today, remember that line.

**Stella:** Let's open with the mental model.

---

**[SECTION 1 — THE LIMIT BUY WITH A REBATE — 1:00]**

**Horace:** Imagine SPY is at $560 today and I tell you "I'd love to own SPY, but only at $530 — that's about a 5% pullback I'm willing to wait for." If you put a regular limit-buy order at $530 in your account, two things happen. One, the order sits there until it fills or the day ends. Two, you earn nothing for waiting.

**Stella:** And you might cancel it tomorrow when you change your mind.

**Horace:** Exactly. Now replace that limit-buy with a 30-day cash-secured put at the $530 strike. Three things change. The order stays alive for 30 days, not one day. You commit the cash up front so you can't change your mind without buying the put back. And — the part everybody focuses on — the market pays you a few hundred dollars for taking that 30-day commitment. That's it. That's the entire trade. A patience price plus rent.

**Stella:** And the rent compensates you for what, exactly?

**Horace:** Volatility. If SPY went straight to $400 tomorrow, you still have to buy it at $530. The market knows that, and the more nervous people are about the next 30 days, the more they pay you to wear that obligation. That's why VIX-rich environments pay better. It's not a free yield — it's the price of being short volatility.

---

**[SECTION 2 — STRIKE BY DELTA — 3:00]**

**Stella:** Let's bring up the first chart.

[VISUAL: image/week28_csp_yield_curve.png]

**Horace:** This is the annualized premium yield on a 30-day put as a function of strike-delta, computed from Black-Scholes with sigma at 22% and rates at 4%. Read it left to right: 10-delta put, 16-delta, 25-delta, 30-delta, 40-delta, 50-delta. The 50-delta — the at-the-money put — pays the highest premium yield by a mile, easily 5-6x what the 10-delta pays.

**Stella:** And there's exactly one reason you don't sell the 50-delta.

**Horace:** Right. The 50-delta has a 50% chance of finishing in-the-money. The 30-delta has roughly a 30% chance. The 10-delta has roughly a 10% chance. Delta is approximately the assignment probability. So that yield curve is not a yield curve in the bond sense — it's a curve of *risk-paid-for*. Closer to the money, more premium, more assignment.

**Stella:** What's the standard preset?

**Horace:** Three of them. 30-delta if you genuinely want to accumulate the stock and you're willing to be assigned 30% of the time. 16-delta — one standard deviation — for most beginners; the bid is far enough below market that assignment feels like a real bargain. 10-delta if you view the put as pure rent on cash and only welcome assignment in a meaningful drawdown. I sell 16-delta on index ETFs by default. I sell 30-delta only on names I actively want to add.

**Stella:** And the most common beginner mistake?

**Horace:** Always the same one — they pick the highest-premium strike, which is closer to ATM, on a stock they don't really want, because the spreadsheet says the yield is biggest. That's not a CSP, that's a coin flip with a logo.

---

**[SECTION 3 — TENOR AND THETA — 5:30]**

**Horace:** Tenor next. You want to be camped where theta — time decay — is steep. From 60 days to 30 days, the put loses about 30% of its time value. From 30 days to expiry, it loses the other 70%. You want to live in that last 30 days.

**Stella:** Why not weeklies, then? Theta is even steeper.

**Horace:** It is. And gamma is steeper too. Weekly puts get blown out by single-day gaps far more than 30-day puts. PUTW — the institutional CSP ETF — sells one-month puts, not weeklies, and they did the math. 30-45 DTE is the sweet spot for retail. You're far enough into theta that decay is fast and far enough from expiry that one bad day doesn't eat a month of premium.

---

**[SECTION 4 — CAPITAL COST — 7:00]**

**Stella:** A point that gets glossed over in every other CSP video.

**Horace:** Yeah. The collateral cash isn't dead. In April 2026 with T-bills at roughly 4%, your $53,000 sitting against a $530 SPY put is earning about 4% just sitting in the broker's money-market sweep. The put premium is *additive* to that. So the right yield calculation is "T-bill rate plus put-premium-annualized," not just the premium piece.

**Stella:** Numbers?

**Horace:** A 30-day, 16-delta SPY put yielding maybe 0.4% in premium, annualized at 12 cycles, gives you 4.8% on the option leg. Plus 4% on the cash leg. Total 8.8% annualized in a no-assignment cycle. That's the honest number. When you see "CSP yields 25% annualized!" somewhere, that's just multiplying a 30-day premium by 12 and forgetting the cash leg already gives you most of it.

---

**[SECTION 5 — ROLLING AND DEFENDING — 8:30]**

**Stella:** What do you actually do when the trade goes against you?

**Horace:** Four moves. One, do nothing — let it get assigned. That's the *default* on stocks you wanted to buy. Two, buy back at a profit when 50-70% of the premium has decayed. Three, roll down and out — buy the threatened put, sell a lower strike further dated, for a small credit. Four, take the L — close at a loss if your thesis on the stock has changed.

**Stella:** And the thing not on the list?

**Horace:** Doubling down. Selling another contract at the same strike when the first is underwater. That's how a small CSP loss becomes a 30%-of-portfolio loss. The market can stay below your strike longer than you can stay willing to add. Irrationality outlasts solvency — that's the trap, in reverse.

**Stella:** And how often do you actually roll?

**Horace:** Once, maybe twice. After the second roll you're admitting your original thesis was wrong. The third roll is denial. Take the loss.

---

**[SECTION 6 — ASSIGNMENT PSYCHOLOGY — 10:30]**

**Horace:** This is the part I want to spend extra time on. Assignment is not a loss event. It's the buy order you placed 30 days ago, executing exactly as designed.

**Stella:** Walk us through the morning after.

**Horace:** You wake up, your account has 100 shares of SPY where there used to be cash, and SPY is trading $2 below your strike. The instinctive reaction is panic. The correct reaction is: "I just bought 100 shares at $530, I collected $300 in premium, my effective cost is $527, and the market is at $528. I'm slightly *up* on the trade."

**Stella:** And then?

**Horace:** You start writing covered calls on those shares. That's the wheel — Week 27's playbook. CSP, assigned, covered call, called away, CSP again. Each turn of the wheel collects premium twice. The only way the wheel breaks is if you panic-sell the assigned shares the next morning. The shares are not the loss. The panic is.

**Stella:** And the only stocks where assignment is genuinely bad?

**Horace:** The ones you should never have written CSPs on. Meme stocks. Single biotechs. Leveraged ETFs. Anything you wouldn't buy outright at the strike. If you can't say "I'd be happy to take delivery," you're not running a CSP, you're running a casino with extra steps.

---

**[SECTION 7 — PUTW VS SPY — 12:30]**

**Stella:** Bring up the second chart.

[VISUAL: image/week28_putw_vs_spy.png]

**Horace:** PUTW is the WisdomTree CBOE PutWrite ETF. It mechanically sells 30-day, ~2% out-of-the-money SPX puts every month, fully cash-secured. It's the institutional answer to "does systematic put-writing beat just owning the index?"

**Stella:** And the answer is?

**Horace:** No. From January 2016 through December 2024, PUTW returned about 7% annualized. SPY returned about 12%. PUTW had a smaller drawdown in March 2020 — about 22% versus 34% for SPY — and weathered 2018 and 2022 with less pain. But in 2017, 2019, 2021, 2023 — every melt-up year — PUTW lagged badly because it doesn't capture upside above the strike.

**Stella:** So why would anyone do CSPs?

**Horace:** Three reasons. One, you don't want maximum return; you want to build a specific position at a specific price. PUTW is mechanical and indiscriminate. Targeted CSPs aren't. Two, you're inside an IRA where the option income is tax-free, and the equivalent stock-trading strategy would be tax-disastrous — the option wrapper is a tax tool first. Three, you want lower portfolio volatility and you'll accept a small return drag for it. But anyone who thinks "sell puts, beat SPY" is starting from a wrong premise. PUTW is a public counter-example.

---

**[SECTION 8 — TAX — 14:30]**

**Horace:** Tax is identical to Week 27. Put premium is short-term capital gain. Every closed contract, every expired contract. The only exception is when the put is assigned — then the premium reduces the cost basis of the assigned shares, and the holding period for *those shares* starts on the assignment day.

**Stella:** Same conclusion as covered calls?

**Horace:** Same conclusion. In a top-bracket taxable account at 35-37%, your CSP yield is netting two-thirds of headline. Inside a Roth IRA, it's netting all of it. Run the wheel — CSPs and covered calls — inside the IRA. Run the buy-and-hold pieces wherever. Don't run a wheel strategy in a regular brokerage if you can avoid it.

---

**[SECTION 9 — INTERACTIVE WALKTHROUGH — 15:30]**

**Stella:** And the interactive.

[INTERACTIVE: interactive/week28_put_writer.html]

**Horace:** Pick an underlying — SPY, QQQ, AAPL, MSFT, KO. Each has embedded vol and price defaults from April 2026. Pick a target delta — 10, 16, 25, 30. Pick a DTE — 21, 30, 45. The Black-Scholes premium pops out, plus the breakeven, the discount-from-current, the annualized yield-on-cash including the T-bill leg, and the probability of finishing OTM.

**Stella:** And the assignment ladder?

**Horace:** Below the big numbers, there's a scenario ladder: "if you're assigned at $X, your effective cost is $Y, an X% discount from spot." Run it across a couple of strikes for the same underlying — you'll see how the discount-from-spot grows as you move further OTM, and the premium-yield shrinks. That trade-off is the entire game.

---

**[OUTRO — 17:00]**

**Stella:** One-line summary?

**Horace:** A cash-secured put is a 30-day limit-buy order with rent attached. Sell them on stocks you want to own at prices you want to own them at. Don't use the rent to talk yourself into bids you don't believe in.

**Stella:** And the takeaways for the wheel?

**Horace:** Three. CSPs on index ETFs and quality compounders are safe-end activity, never speculation-end — that is the barbell. Run them inside a Roth or traditional IRA, not a taxable account — the option wrapper is a tax tool first. And the premium you collect is a function of how nervous *other* people are, not how clever you are — the option tail wags the equity dog.

**Stella:** Next week we step into spreads — bull-put credit spreads as the leveraged sibling of the CSP, where you don't post the full collateral. See you then.

**Horace:** See you next week.
