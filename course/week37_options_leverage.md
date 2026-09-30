# Week 37: Options as Leverage — Stock Replacement With Deep-ITM Calls

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Most retail investors hear "options are leverage" and picture lottery tickets — out-of-the-money calls bought into earnings, +500% one week, -100% the next. That is one corner of the option universe, and it is the corner where almost everyone loses. The institutional corner is different: a single deep-in-the-money LEAPS call can deliver roughly 90% of a stock's economic exposure for 25-35% of the capital, while leaving the remaining 65-75% of the cash to earn risk-free Treasury yield. That is not gambling. It is **stock replacement**, and it is one of the cleanest ways the barbell construction — boring core plus concentrated alpha sleeves, financed by tax-efficient option leverage — shows up in a real account.

There are four reasons this lesson sits at the centre of the L3 curriculum.

1. **Capital efficiency without margin.** A deep-ITM call has no maintenance call, no overnight financing line, and no force-liquidation risk. The most you can lose is the premium. Margin can take more than your account; a long option cannot.
2. **Tax geometry.** Holding a LEAPS call for more than one year qualifies the gain as long-term capital gain at 15-20%, identical to holding the stock. There is no dividend, but there is also no annual financing-cost drag the way there is on margin or on a 2x ETF wrapper. Options are the most tax-efficient leverage available to a US retail investor; this is the lesson that proves it.
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

![Stacked bar chart comparing the capital required to obtain $10,000 of SPY exposure across four routes — direct shares, a 0.92Δ 12-month deep-ITM LEAPS, a 0.70Δ 6-month moderately-ITM call, and a 0.30Δ short-dated near-the-money call. Shares require the full $10,000; the 0.92Δ LEAPS requires roughly $2,400 in premium, freeing ~$7,600 of cash (shaded orange) that earns risk-free T-bill yield (~4.3% in April 2026); the 0.70Δ call requires about $1,200; the 0.30Δ lottery-ticket call only ~$300 but with sharply lower delta and probability-of-profit. The chart visualises why delta is the leverage dial and why the freed cash is half the story.](../image/week37_replacement_capital.png)

#### 2.2 The Capital You Free Up Is Real Money

The quiet half of stock replacement is the cash you do **not** spend. If a 0.92Δ LEAPS replicates 92% of $52,000 of SPY exposure for $12,300, the remaining $39,700 sits in your account. In April 2026, with 3-month T-bills yielding about 4.3% and money-market funds (SGOV, BIL) tracking the same level, that cash is not idle — it pays roughly $1,700 per year in coupon, all of which is taxed at ordinary income but **all of which is incremental return** that the buy-and-hold stock investor does not capture, because their $52,000 is fully deployed.

Over a 9-month holding period the freed-cash carry adds roughly 3.0-3.3% to the position's total economic return, which fully or partially offsets the SPY dividend you forfeit (SPY's trailing-twelve-month yield in April 2026 is about 1.3%) plus the option's extrinsic decay (about 1.5-2.5% on a 0.92Δ LEAPS over 9 months). Net of all three, the deep-ITM LEAPS is approximately neutral against owning shares **on price-only return**, but it consumed one-quarter of the capital. The other three-quarters can sit in T-bills or fund the rest of the four-tranche barbell.

#### 2.3 The Risks You Are Taking On

1. **Time decay (theta).** Small for deep-ITM long-dated calls — typically 0.02-0.05% of the underlying per day — but it is real and it is the cost of the leverage. The closer the strike to spot and the closer to expiration, the bigger this number gets.
2. **Implied-volatility crush.** If you pay 25% IV for a LEAPS and IV reverts to 18%, you lose vega even if the stock is unchanged. The fix: do not buy LEAPS when VIX > 25 unless you are explicitly long vol.
3. **Dividend skip.** Long-call holders do not receive the underlying's dividend. For SPY (1.3%) this is small; for a high-yield name like KO (3%) or VZ (6%) it is structural — LEAPS replacement on a high-dividend stock is expensive in a way the model does not capture unless you check.
4. **Early assignment of a short leg.** Pure long calls cannot be assigned to you (you own them). But if you pair the LEAPS with a sold short call to cheapen it (a "diagonal"), the short leg can be assigned the day before ex-dividend on a high-dividend underlying.
5. **Liquidity.** LEAPS on SPY, QQQ, AAPL, MSFT, NVDA, AMZN are liquid. LEAPS on small-caps and most international ADRs are not. Stock-replacement on illiquid underliers loses to the bid-ask spread.

#### 2.4 The Tax Picture

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

![Cumulative-growth chart of $1 invested at the start of 2010 in three vehicles through 2024: SPY total-return (blue, ending near $7, ~13.9% CAGR), a frictionless mathematical 2x of SPY compounded annually (gold, ending near $32, ~26-28% CAGR), and the actual 2x daily-reset ETF SSO (red, ending near $21, ~22% CAGR). The gap between the gold and red lines is the volatility decay — roughly 6 percentage points per year of compounded drag from the daily reset's σ² penalty plus expense ratio and embedded financing. Over 15 years that gap compounds into roughly one-third less terminal wealth than the frictionless 2x.](../image/week37_lev_etf_decay.png)

A 0.92Δ LEAPS does not have this problem. It compounds at approximately 0.92 times the underlying's price return, plus or minus the small extrinsic decay, with no daily reset and therefore no $\sigma^2$ drag. This is the single biggest reason institutional desks running a barbell use long-dated single-name options instead of leveraged ETFs.

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

**Q5. How does this interact with the four-tranche framework?**
Stock replacement converts the L1 beta sleeve from 100% capital to roughly 25% capital, freeing 75% to fund the L2 and L3 strategy sleeves without reducing equity exposure. This is the operational mechanism behind the barbell.

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
