# Week 37: Options as Leverage — Stock Replacement With Deep-ITM Calls

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Most retail investors hear "options are leverage" and picture lottery tickets — out-of-the-money calls bought into earnings, +500% one week, -100% the next. That is one corner of the option universe, and it is the corner where almost everyone loses. The institutional corner is different: a single deep-in-the-money LEAPS call can deliver roughly 90% of a stock's economic exposure for 25-35% of the capital, while leaving the remaining 65-75% of the cash to earn risk-free Treasury yield. That is not gambling. It is **stock replacement**, and it is one of the cleanest ways the toolkit Horace described in SOUL #14 (the barbell) and SOUL #15 (tax-efficient leverage via options) shows up in a real account.

There are four reasons this lesson sits at the centre of the L3 curriculum.

1. **Capital efficiency without margin.** A deep-ITM call has no maintenance call, no overnight financing line, and no force-liquidation risk. The most you can lose is the premium. Margin can take more than your account; a long option cannot.
2. **Tax geometry.** Holding a LEAPS call for more than one year qualifies the gain as long-term capital gain at 15-20%, identical to holding the stock. There is no dividend, but there is also no annual financing-cost drag the way there is on margin or on a 2x ETF wrapper. SOUL #15 names options the most tax-efficient leverage available to a US retail investor; this is the lesson that proves it.
3. **A clean alternative to leveraged ETFs.** Products like SSO (2x S&P 500) and QLD (2x Nasdaq) reset daily and suffer **volatility decay** in any path that is not monotonically up. Over 2010-2024 SSO compounded at roughly 22%/yr while a frictionless mathematical 2x of the S&P would have compounded at roughly 28%/yr — a 6-percent-per-year drag on terminal wealth. A deep-ITM LEAPS does not reset daily and does not decay that way.
4. **Risk literacy.** The same mechanics that make a 90Δ call efficient also create new failure modes most investors have never priced: assignment risk on the short leg of a spread, dividend-skip cost, the small-but-nonzero theta on a long-dated call, and the IV-crush risk if you buy after a vol spike. Knowing how to size and roll a stock-replacement call is what separates the lottery-ticket trader from the leveraged investor.

This lesson is the operational manual for that distinction.

---

### 2. What You Need to Know

#### 2.1 Delta Is the Leverage Dial

A call's delta is the first derivative of the option price with respect to the underlying. A 0.50Δ option moves about 50 cents for every 1 dollar in the stock. A 0.90Δ option moves about 90 cents on the dollar. For stock-replacement purposes, **delta is the leverage dial**:

- **0.90Δ deep-ITM 12-month call** ≈ 90% of stock exposure, ≈ 25-30% of stock capital.
- **0.70Δ moderately-ITM 6-month call** ≈ 70% of stock exposure, ≈ 12-18% of stock capital.
- **0.30Δ near-the-money 3-6 month call** ≈ 30% of stock exposure, ≈ 3-6% of stock capital.
- **0.10Δ OTM short-dated call** ≈ 10% of stock exposure, < 1% of stock capital — the lottery ticket.

The trade-off as you walk down the delta ladder: less capital, more leverage, but more time decay, more vega risk, and lower probability of finishing in the money. Stock-replacement strategies live almost exclusively in the 0.80-0.95Δ band on 9-15 month expirations. That is the band where extrinsic value is small relative to the dollar exposure controlled.

For a numerical anchor: SPY at $520, a January 2027 (about 9 months out in April 2026) $416 call (K = 80% of spot) prices around $123 with σ = 19%, r = 4.3%. Delta is 0.92. Per contract you control $52,000 of SPY exposure for $12,300 of premium — about 24 cents on the dollar.

[VISUAL: image/week37_replacement_capital.png]

#### 2.2 The Capital You Free Up Is Real Money

The quiet half of stock replacement is the cash you do **not** spend. If a 0.92Δ LEAPS replicates 92% of $52,000 of SPY exposure for $12,300, the remaining $39,700 sits in your account. In April 2026, with 3-month T-bills yielding about 4.3% and money-market funds (SGOV, BIL) tracking the same level, that cash is not idle — it pays roughly $1,700 per year in coupon, all of which is taxed at ordinary income but **all of which is incremental return** that the buy-and-hold stock investor does not capture, because their $52,000 is fully deployed.

Over a 9-month holding period the freed-cash carry adds roughly 3.0-3.3% to the position's total economic return, which fully or partially offsets the SPY dividend you forfeit (SPY's trailing-twelve-month yield in April 2026 is about 1.3%) plus the option's extrinsic decay (about 1.5-2.5% on a 0.92Δ LEAPS over 9 months). Net of all three, the deep-ITM LEAPS is approximately neutral against owning shares **on price-only return**, but it consumed one-quarter of the capital. The other three-quarters can sit in T-bills or fund the rest of the four-tranche barbell.

#### 2.3 The Risks You Are Taking On

1. **Time decay (theta).** Small for deep-ITM long-dated calls — typically 0.02-0.05% of the underlying per day — but it is real and it is the cost of the leverage. The closer the strike to spot and the closer to expiration, the bigger this number gets.
2. **Implied-volatility crush.** If you pay 25% IV for a LEAPS and IV reverts to 18%, you lose vega even if the stock is unchanged. The fix: do not buy LEAPS when VIX > 25 unless you are explicitly long vol.
3. **Dividend skip.** Long-call holders do not receive the underlying's dividend. For SPY (1.3%) this is small; for a high-yield name like KO (3%) or VZ (6%) it is structural — LEAPS replacement on a high-dividend stock is expensive in a way the model does not capture unless you check.
4. **Early assignment of a short leg.** Pure long calls cannot be assigned to you (you own them). But if you pair the LEAPS with a sold short call to cheapen it (a "diagonal"), the short leg can be assigned the day before ex-dividend on a high-dividend underlying.
5. **Liquidity.** LEAPS on SPY, QQQ, AAPL, MSFT, NVDA, AMZN are liquid. LEAPS on small-caps and most international ADRs are not. Stock-replacement on illiquid underliers loses to the bid-ask spread.

#### 2.4 The Tax Picture (SOUL #15)

For a US taxable investor, the tax case for LEAPS-as-leverage is the cleanest in the option universe.

- **Hold > 365 days, sell at gain → long-term capital gain.** Same 15-20% rate as the stock would have received.
- **Sell at loss → ordinary capital loss**, deductible against other capital gains, with $3,000/yr against ordinary income carry-forward.
- **No mark-to-market.** Unlike Section 1256 (broad-based index futures and a small set of index options), single-stock and most ETF options follow standard equity-option tax rules — gains crystallise only when you sell.
- **No financing-cost statement.** Margin interest is deductible only against investment income and is generally not worth the friction. The implicit financing inside the LEAPS price is **not** a deduction, but it is also not income to anyone — it is a feature of the contract, not a tax event.

Compare to a 2x ETF (SSO, QLD): every year ProShares passes through phantom interest income from the swap counterparty plus capital-gain distributions, taxed at ordinary or short-term rates. The LEAPS gives you the leverage with the better tax envelope.

#### 2.5 Compared to a 2x Leveraged ETF

The most common alternative retail picks for index leverage is the daily-reset 2x ETF: SSO (2x S&P 500), QLD (2x Nasdaq-100), UPRO/TQQQ (3x). They have a single, important problem — **path dependence**.

A 2x daily-reset ETF earns approximately:
$$ r_{\text{2x},\text{annual}} \approx 2 r - \sigma^2 $$
where $r$ is the underlying's annual return and $\sigma^2$ is its realised variance. For the S&P 500 with $\sigma \approx 18\%$, the $\sigma^2$ term is about 3.2% per year of straight drag. Empirically, over 2010-2024, SSO compounded at roughly 22% per year while a frictionless 2x of SPY would have compounded at roughly 28%. SSO did not blow up — it just lagged the math by enough to make any thesis longer than 12 months expensive.

[VISUAL: image/week37_lev_etf_decay.png]

A 0.92Δ LEAPS does not have this problem. It compounds at approximately 0.92 times the underlying's price return, plus or minus the small extrinsic decay, with no daily reset and therefore no $\sigma^2$ drag. This is the single biggest reason the institutional desks Horace describes in SOUL #14 use long-dated single-name options instead of leveraged ETFs.

The 2x ETF does have one advantage: it pays its (tiny) dividend, it can sit in any account, and you do not have to roll. For a passive investor who wants modest leverage and will not pay attention, SSO is fine. For anyone running the L2/L3 sleeve actively, LEAPS dominates on capital efficiency, tax, and path-independence.

#### 2.6 How to Size a Stock-Replacement Position

Three rules from the desk.

1. **Notional, not premium.** Size by the dollar exposure the contract controls (delta × 100 × spot), not by the cash outlay. A single 0.92Δ SPY LEAPS controls roughly $48,000 of SPY exposure. If your sleeve target is $100k of SPY, you buy 2 contracts, not 8.
2. **Match expiration to thesis.** If your view is 12-18 months, buy a 15-month LEAPS. If your view is 3 months, buy 5-month and accept 30% extrinsic. Do not buy a weekly call and call it leverage; that is a directional bet with theta as the carrying cost.
3. **Roll on a calendar, not a price.** Roll forward when the LEAPS has 90 days left, never less. The last 60 days of any option's life is where extrinsic decay is fastest and the gamma risk is largest. Rolling at 90 DTE preserves the deep-ITM character.

Try the [Replacement Lab](interactive/week37_replacement_lab.html) interactive — pick a target equity exposure and watch capital, breakeven, freed-cash yield, and total return shift across shares, three LEAPS deltas, and SSO.

---

### 3. Common Misconceptions

1. **"Options leverage is gambling."** Out-of-the-money short-dated calls are gambling. Deep-ITM long-dated calls are leverage with a defined maximum loss. The same instrument family contains both; the strike and expiration determine which one you bought.
2. **"I should buy ATM calls because they're cheaper."** ATM has the highest extrinsic value as a percentage of premium — you are paying maximum time-decay for the same exposure a 0.90Δ call gives you with 1/3 the extrinsic.
3. **"LEAPS are for buying-and-holding for years."** LEAPS are for **rolling** every 9-15 months at 90+ DTE. A LEAPS held to expiration is just an expensive way to buy stock.
4. **"SSO is the same as a LEAPS, easier."** SSO has 3-6%/year volatility decay over multi-year horizons. A LEAPS does not. Over 5-10 years that gap dominates everything else.
5. **"Margin is the same as options leverage."** Margin can blow up your account; a long option cannot. Margin is taxed differently. Margin requires a maintenance ratio. They are not substitutes — they are different instruments.
6. **"I'll just buy a leveraged call into earnings."** Earnings IV crush typically removes 30-50% of an option's price the morning after the print, even on a stock that moved in your direction. The instrument is wrong for that thesis.
7. **"LEAPS are illiquid."** On SPY, QQQ, the top 50 single names, and most large ETFs, LEAPS spreads are 1-3%. On anything outside that universe they can be 10-20%.
8. **"Freed-up cash should sit in checking."** SGOV and BIL are 1-day-settlement T-bill ETFs at 4.3% in April 2026. Cash that does not earn the risk-free rate is a permanent yield giveaway.
9. **"The dividend doesn't matter."** On a 6% yielder over a one-year LEAPS, you skip 6% of return. That is more than the option's extrinsic. Stock replacement is for low-yield underliers.
10. **"If I hold the LEAPS one day past 365 it's long-term."** True for a long-only LEAPS held in isolation. Combined with any short option leg or wash-sale across a related stock position, the holding-period rules can reset. If you wheel, document.

---

### 4. Q&A Section

**Q1. How deep-ITM should the strike be?**
80-85% of spot is the sweet spot. That puts delta at roughly 0.85-0.95 on a 12-month expiration with normal vol, which is the band where you are paying minimal extrinsic for near-stock exposure.

**Q2. What if the stock falls 10% the day after I buy the LEAPS?**
Your 0.92Δ LEAPS loses about 92% of that 10%, ie roughly 9.2% of the underlying value. Your dollar loss as a percentage of premium is larger than 10% — that is the leverage. The maximum loss remains the premium paid.

**Q3. Should I do this on individual stocks or only on indexes?**
Single-name LEAPS works on the top 50 US large-caps where liquidity is good. Indexes (SPY, QQQ, IWM) are the canonical use case because liquidity is best and idiosyncratic gap risk is lower.

**Q4. What's the right expiration?**
12-18 months at purchase, rolled forward when 90 days remain. Anything shorter than 9 months has too much theta; anything longer than 24 months has too little liquidity at typical strikes.

**Q5. How does this interact with the four-tranche framework (SOUL #13)?**
Stock replacement converts the L1 beta sleeve from 100% capital to roughly 25% capital, freeing 75% to fund the L2 and L3 strategy sleeves without reducing equity exposure. This is the operational mechanism behind the barbell SOUL #14 describes.

**Q6. What's the all-in cost of running this strategy on SPY?**
Approximately: SPY dividend skipped (1.3%/yr) + LEAPS extrinsic decay (2-3%/yr) - freed-cash T-bill yield earned (~3.0%/yr on the 75% freed) = net cost ~0-0.5%/yr. Plus commissions and one bid-ask round trip per 12 months (~0.3%).

**Q7. Can I do this in a Roth IRA?**
Yes — long calls including LEAPS are permitted in IRAs at most brokers (Schwab, Fidelity, IBKR). You cannot trade naked calls or use margin in an IRA, but stock-replacement long calls are allowed, and the freed cash earns Treasury yield tax-free inside the Roth.

**Q8. Is implied volatility worth tracking?**
Yes. Buy LEAPS when the underlying's IV rank is below 50 (preferably below 30). High-IV LEAPS embed an expensive vol premium that decays as IV mean-reverts, even if the stock is unchanged.

**Q9. Should I sell a short call against the LEAPS to cheapen it?**
That is a poor-man's covered call (PMCC) — covered in week 30. It does cheapen the position but it caps upside and introduces assignment risk on the short leg. For pure stock replacement, keep the LEAPS naked.

**Q10. How does this compare to running margin at IBKR's portfolio margin?**
Portfolio margin can get to 4-6x leverage but charges 6-7% on debit balances in 2026 and exposes the account to forced liquidation in a gap-down. LEAPS does not have a margin call. For investors who can tolerate margin call risk and trade large enough to qualify for portfolio margin, the cost-per-leverage can be similar; for everyone else, LEAPS wins on operational risk.

**Q11. What about TQQQ / UPRO (3x)?**
Same story as SSO but worse. Annual decay is approximately $3 \sigma^2 - \text{financing}$, which on the Nasdaq-100 means 8-12%/year drag. Over 5+ years TQQQ underperforms a 3x LEAPS basket on QQQ by a wide margin. Use 3x ETFs only as short-term tactical instruments.

**Q12. When does this strategy fail?**
Three regimes: (1) sustained multi-year drawdown — your LEAPS can go to zero before you can roll; (2) high-vol whipsaw markets where IV crush after a vol-spike purchase removes 20-30% of premium; (3) anything illiquid where the bid-ask spread eats the freed-cash carry. Stick to top-50 underliers and IV rank < 50.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Replacing Stock With Deep-ITM Calls — Real Capital, Real Math, Real Risks

**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Welcome back to the Chan Investing tutorial. I'm Stella, and today we're on Week 37 — using options as leverage. Specifically, the trade where you replace 100 shares of stock with one deep-in-the-money call. Horace, this is one of the topics in SOUL.md you've described as "the cleanest piece of leverage a retail investor can run." Why is that?

**Horace:** Because it's the rare leverage trade that does not require margin, does not blow up on a gap-down, and is taxed almost identically to owning the stock. Most retail investors have heard "options are leverage" and they think they know what that means — buy a weekly call, hope for a moonshot. That's gambling. The institutional version is different. It's called stock replacement, and the math is just very compelling once you sit with it.

**Stella:** Today we'll walk through three things: what the trade actually is, the capital math compared to shares and to leveraged ETFs, and the risks that come with it. We have two charts and one interactive. Let's start with the capital chart.

**[SECTION 1 — REPLACEMENT CAPITAL CHART, 1:30-5:00]**

**[VISUAL: image/week37_replacement_capital.png]**

**Horace:** This chart asks a single question. If I want $10,000 of SPY exposure, what does it cost me? The first bar — shares — is the obvious one. $10,000 of exposure costs $10,000. You own 19 shares of SPY at $520 and that's it.

**Stella:** And the second bar?

**Horace:** A 12-month deep-in-the-money call. Strike at 80% of spot, so $416. Delta around 0.92. Premium for one contract is about $123 a share, $12,300 for the contract, which controls $52,000 of SPY. Scale that back to $10,000 of exposure and you're paying roughly $2,400. That's 24 cents on the dollar to capture 92% of the move.

**Stella:** And the freed-up $7,600?

**Horace:** Treasury bills. SGOV is paying 4.3% on its trailing distribution as of April 2026. So that $7,600 earns you about $325 over the next year — completely separately from the SPY position. That's the orange shading on each bar.

**Stella:** The third bar is the 70-delta 6-month call.

**Horace:** Right. Less capital — about $1,200 per $10,000 of exposure — but you're holding less delta, you're paying more extrinsic as a percentage of premium, and the position needs more attention because it's shorter-dated. This is a cheaper version of the same idea but it's not a buy-and-hold; it's a 6-month tactical position.

**Stella:** And the 30-delta short-dated call?

**Horace:** That's the lottery-ticket band. $300 of premium per $10,000 of nominal exposure, but the option only moves 30 cents on the dollar, the probability of finishing in the money is around 30%, and time decay is fast. That's not stock replacement. That's a directional bet with theta as the cost. I'd never label that "leverage" in the way I'd label the 90-delta LEAPS.

**Stella:** So the takeaway from this chart is that the leverage dial is delta, and the delta you choose determines whether you're running stock replacement or running a directional speculation.

**Horace:** Yes. And the freed cash matters. If you ignore the orange portion of each bar, you're missing half of why the trade works. The capital you didn't deploy isn't sitting in checking earning zero — it's earning the risk-free rate in a money fund or T-bill ETF. That's a structural piece of the return that the buy-and-hold stock investor does not have access to because their $10,000 is fully deployed.

**[SECTION 2 — LEVERAGED ETF DECAY, 5:00-9:30]**

**Stella:** Let's pull up the second chart. This one compares SSO — the 2x S&P 500 ETF — to a hypothetical frictionless 2x of the S&P, and to plain SPY.

**[VISUAL: image/week37_lev_etf_decay.png]**

**Horace:** This is one of the most important charts in the L3 curriculum. The blue line is SPY total return from 2010 through 2024 — fifteen years, dollar grew to about seven dollars, that's about 13.9% compounded.

**Stella:** And the gold line?

**Horace:** That's the mathematical 2x — at the end of each year, take twice the SPY return that year and compound it. No friction, no daily reset, no expense ratio. A dollar grew to roughly thirty-two dollars. About 26-28% compounded.

**Stella:** And the red line is the actual SSO ETF.

**Horace:** Yes. SSO over the same window, with its daily reset and 0.90% expense ratio and embedded financing, compounded a dollar to about twenty-one dollars — call it 22% per year. Drag versus the frictionless 2x: roughly six percentage points per year of compounded return. Over fifteen years that compounded into a third less terminal wealth.

**Stella:** Where does the drag come from?

**Horace:** Two sources. The smaller one is the expense ratio plus the embedded swap financing, maybe 1.5% per year. The bigger one is the volatility decay. Daily-reset 2x leverage earns approximately twice the annual return minus the realised variance. For the S&P with a 17-18% annualized vol, that variance term is roughly 3% per year of mechanical drag. It's not anyone's fault — it's how daily-reset leverage works.

**Stella:** And the LEAPS does not have this problem?

**Horace:** Not in the same way. The LEAPS moves at delta times the underlying's price return, with a small extrinsic decay over time. There's no daily reset. There's no variance penalty. If you hold a 0.92Δ LEAPS for a year and SPY went up 20% with realised vol of 25%, your LEAPS captured roughly 18.4% of that — not "2*20% - 25%²" which is the SSO formula.

**Stella:** What's the takeaway?

**Horace:** SSO is fine for short-term tactical leverage. For 12-month-plus exposure, deep-ITM LEAPS dominates on path-independence and on tax. SOUL #15 — leverage via options is the most tax-efficient form of leverage available to a US retail investor — that's what this chart is showing you in dollars.

**[SECTION 3 — INTERACTIVE WALKTHROUGH, 9:30-13:30]**

**Stella:** Let's open the Replacement Lab. The interactive lives at `interactive/week37_replacement_lab.html`.

**Horace:** Top of the lab is a single slider — target equity exposure in dollars. Default $50,000 of SPY. Below that you see five rows: shares, 0.90Δ 12-month LEAPS, 0.70Δ 6-month call, 0.30Δ 3-month call, and SSO 2x ETF.

**Stella:** Each row shows capital required, breakeven move, max upside, max downside, freed-cash T-bill yield, and net expected return.

**Horace:** Right. The LEAPS row is the most informative. At default settings — SPY $520, σ=19%, r=4.3%, K=80% of spot, 12-month expiration — the lab shows about $11,800 of capital required for $50,000 of exposure, freed cash of $38,200 earning $1,640/yr in T-bills, breakeven on the underlying of about +3.4% over the year, max downside equal to the premium paid.

**Stella:** Compare it to the SSO row.

**Horace:** SSO needs $25,000 for $50,000 of equivalent exposure (because it's 2x, you put up half), so freed cash is $25,000 earning $1,075. But SSO eats roughly 3% per year in vol decay on top of the 0.90% expense ratio. The lab models that as a -3.9% drag. Net of the freed-cash carry, SSO is approximately -1.7% versus shares per year on price-only return. The LEAPS is approximately -0.3%.

**Stella:** The 30-delta short-dated row?

**Horace:** Don't run that as stock replacement. The lab will show you a maximum upside of several hundred percent and a probability-of-profit of roughly 30%. That's a speculation, not a replacement. It's there for contrast, not for use.

**Stella:** Theme observer and four-locale.

**Horace:** Yes. Switch the parent page theme — the lab re-renders. Switch language with `?lang=cn` or `?lang=hk` and all labels translate. postMessage resize works for the parent iframe so it embeds cleanly into the lesson page.

**[SECTION 4 — RISK + TAX, 13:30-16:30]**

**Stella:** Risks. The big ones.

**Horace:** Five things to track. Theta — small for deep-ITM LEAPS, but it's the carrying cost; check it monthly. IV crush — don't buy LEAPS when VIX is above 25; you'll watch the position lose 5-10% on vol mean-reversion alone. Dividend skip — material for high-yield names; not material for SPY. Assignment of any short leg — only relevant if you've added a short call; covered in week 30. Liquidity — stick to top-50 underliers and indexes.

**Stella:** And the tax case from SOUL #15.

**Horace:** A LEAPS held more than a year qualifies for long-term capital gains, same rate as the stock. A 2x ETF passes through ordinary-income distributions every year, and your basis adjusts every distribution. The LEAPS gives you the leverage with the better tax envelope. In a Roth IRA, the freed cash earns the risk-free rate tax-free — that's the cleanest version of the trade.

**Stella:** And how does this fit the four-tranche framework?

**Horace:** L1 is your beta sleeve — VTI, SPY, whatever you use as the index core. Stock replacement converts that sleeve from 100% capital to roughly 25% capital. The freed 75% funds L2 strategy sleeves — covered calls, cash-secured puts, factor tilts — without reducing your beta exposure. That's the operational mechanism behind the barbell from SOUL #14. The barbell only works if you can hold full beta with less than full capital.

**[OUTRO — 16:30-18:00]**

**Stella:** Three things to take with you. First — delta is the leverage dial; the trade we covered today is the 0.85-0.95 delta band. Second — the freed cash is real money; do not let it sit in checking. Third — leveraged ETFs decay; LEAPS don't. The LEAPS is the institutional default for a reason.

**Horace:** And one principle — do this only on liquid underliers when IV is reasonable, do this only with discipline on rolling at 90 DTE, and do not confuse stock replacement with the lottery-ticket trade. They use the same instrument family. They are not the same trade.

**Stella:** Next week we tackle the poor-man's covered call — the natural pairing of the LEAPS we built today with a sold short call. See you then.

**Horace:** See you next week.
