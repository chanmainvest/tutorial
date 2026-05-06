# Week 34: Rate Sensitivity Across Asset Classes

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every asset on Earth is priced by discounting its future cash flows back to today. The discount rate is built on top of the risk-free rate -- the yield on a US Treasury. Move the Treasury, and you move every price in the world. That is not a metaphor. It is arithmetic.

1. **Diversification is conditional, not unconditional.** The 60/40 portfolio rests on a single assumption: that stocks and bonds zig and zag against each other. In 2022 they did not. The S&P 500 fell 18%, the 10-year Treasury fell 18%, REITs fell 24%, gold barely budged, and the dollar rallied 8%. A "balanced" portfolio dropped 16-17%. The reason was simple: the same +400bps shock hit both legs at once, and rate sensitivity dominated correlation.

2. **The 40-year tailwind reversed.** From 1981 to 2020 the 10-year Treasury yield fell from 15% to 0.5%. Falling rates lift every duration-sensitive asset: bonds, growth equity, REITs, private credit, venture capital, leveraged buyouts. That tailwind made an entire generation of "long anything" portfolios look skilled. When the tailwind reversed in 2022, the same portfolios looked panicked. The investor who does not know which assets are duration-sensitive is the investor who got blindsided.

3. **Rate shocks are not rare events.** Since 1980 the US has lived through Volcker (rates +1,000bps), 2008 (rates -400bps), 2020 (rates -150bps), and 2022 (rates +525bps). That is roughly one regime-changing rate move per decade. Designing a portfolio that ignores rate shocks is designing a portfolio for a world that does not exist.

4. **Position sizing depends on this.** Once you know that a 30-year bond falls roughly 16% on +100bps and a long-duration growth ETF like ARKK falls 12-15% on the same shock, you can stop treating them as two different assets. They are the same trade in different costumes. Rate sensitivity is a unifying lens -- the tail risks share a common root, and the volatility tail is what wags the dog.

This lesson gives you the cross-asset playbook for the next +100bps and the next -100bps. Week 47 will use it to size a tail-risk hedge.

---

### 2. What You Need to Know

#### 2.1 The Master Formula

Every asset's price equals the present value of its cash flows:

$$P = \sum_{t=1}^{\infty} \frac{CF_t}{(1+r)^t}$$

Modified duration $D$ is the percentage price change for a 1% change in $r$:

$$\frac{\Delta P}{P} \approx -D \cdot \Delta r$$

That is the entire game. The longer the cash flow timeline, the larger $D$, and the more violent the price reaction to a rate move. A 30-year zero-coupon bond has $D \approx 30$. A short-duration value stock has $D \approx 5$. A long-duration unprofitable growth name has $D \approx 30$ as well -- which is why ARKK and TLT moved together in 2022.

#### 2.2 The Rate-Shock Cheat Sheet

Estimated price impact of a parallel +100bps shock at the long end of the curve (mid-2026 starting yields, broadly representative):

| Asset class | Approx. $D$ | Δ price for +100bps |
|:--|:--:|--:|
| 3-month T-Bill | 0.25 | -0.25% |
| 5-year Treasury | 4.5 | -4.5% |
| 10-year Treasury | 8 | -8% |
| 30-year Treasury | 16 | -16% |
| Investment-grade corp (LQD) | 9 | -10% |
| High-yield corp (HYG) | 4 | -6% |
| S&P 500 broad | 18 | -7% |
| Value equity (VTV) | 10 | -3% |
| Growth equity (VUG / QQQ) | 22 | -12% |
| REITs (VNQ) | 18 | -10% |
| Gold (GLD) | -- | -2% to +5% |
| Long-duration crypto / unprofitable tech | 30+ | -20% or worse |
| US dollar (DXY) | -- | +1% to +3% |

Two assets break the duration formula. Gold has no cash flow, so you cannot compute duration directly -- its rate sensitivity comes through inflation expectations. The dollar is a relative price, not a discounted cash flow, so it moves with the *spread* between US rates and foreign rates. We handle both separately in §2.5 and §2.6.

![Horizontal bar chart showing the estimated price impact of a parallel +100bps shock at the long end of the curve across the major asset classes — 5y Treasury, 10y Treasury, 30y Treasury, IG corporates (LQD), HY corporates (HYG), S&P 500, value equity (VTV), growth equity (VUG/QQQ), REITs (VNQ), gold (GLD), long-duration crypto / unprofitable tech, and the US dollar (DXY). Bars fan out from -20% (long-duration crypto) and -16% (30y Treasury) on the left through to small positives for gold and DXY on the right. The chart is the visual companion to the cheat-sheet table above and is the unifying picture: same shock, different durations, dramatically different price reactions.](image/week34_rate_shock_grid.png)

#### 2.3 Bonds: Linear in Duration

Bonds are the textbook case. A 30-year Treasury is roughly twice as rate-sensitive as a 10-year, which is roughly twice as sensitive as a 5-year. A barbell of T-Bills + 30-year zeros has the same average duration as a bullet of 10-years but very different convexity. For most portfolios the right anchor is the 5- to 10-year intermediate Treasury (IEF, IEI). The 30-year (TLT, EDV) is a *speculative* rate trade -- it loses 16% on +100bps and gains 16% on -100bps. That belongs in the alpha sleeve, not the bond sleeve.

#### 2.4 Equities: Duration in Disguise

Growth equities are long-duration assets in everything but name. The 2022 case is the cleanest evidence we have ever had:

- 10-year Treasury yield rose from 1.5% to 4.0% (+250bps).
- ARKK (long-duration unprofitable tech) fell ~67%.
- QQQ (large-cap profitable tech) fell ~33%.
- VTV (value, short duration) fell ~5%.
- That ranking matches the duration ladder exactly.

The rule: for every doubling of the time-to-payoff of a company's cash flows, double its rate sensitivity. A bank earning $5 today and $5.20 next year has tiny duration. A SaaS company earning -$1 today and projected to earn $50 in 2035 has enormous duration. Growth multiples are duration multiples.

#### 2.5 Real Estate: Levered Duration

REITs are *highly* rate-sensitive for two compounding reasons. First, the rent stream is long-dated (cap rates compress and decompress with the 10-year). Second, the underlying properties are levered roughly 50%, so refinancing risk amplifies rate shocks. Office REITs in 2022-2024 lost 40-50% of equity value as cap rates went from 5% to 7-8% on the same rent. Residential and industrial held up better, but VNQ as a whole drew down 30%+ in 2022. Rule of thumb: REITs trade like a leveraged 15-year bond.

Mortgage rates are the second-order channel: 30-year fixed rates went from 3% to 7.8% in 2022-2023, killing housing transaction volume. Anyone with a floating-rate construction loan was forced to refinance into much higher rates -- many did not survive.

#### 2.6 Gold: A Function of *Real* Rates, Not Nominal

Gold has no cash flow, no yield, and no earnings. Its price is the inverse of confidence in fiat. The driving variable is *real* rates -- the 10-year nominal yield minus expected inflation (the TIPS breakeven). When real rates rise, gold falls (the opportunity cost of holding zero-yield gold goes up). When real rates fall, gold rises.

That is why 2022 was so unusual: nominal rates rose violently, but inflation also rose violently, so *real* rates only rose modestly. Gold ended the year at +0.4%. In 1980 the same arithmetic ran the other way: Volcker hiked nominal rates above inflation, real rates went strongly positive, and gold collapsed from $850 to $300. Gold is a store of value because enough people *believe* it is, and real rates are the mechanism of that belief.

#### 2.7 The Dollar: A Spread, Not a Level

DXY measures the dollar against a basket of trading-partner currencies. It moves with the *spread* between US rates and foreign rates, plus a risk-on/risk-off premium. When the Fed hikes faster than the ECB and BoJ (2022), the dollar rallies. When it hikes slower (2002-2004, 2017-2018), the dollar falls. A +100bps shock to US rates that is matched by foreign hikes does roughly nothing to DXY. A +100bps shock that is purely US -- the 2022 case -- pushes DXY up 5-10%.

The second-order effects of a strong dollar matter: emerging markets weaken, US multinational earnings translation hurts (~50% of S&P 500 revenue is overseas), and gold faces a headwind. We stay US-only on the long side; the dollar is the reason that works.

#### 2.8 The 2022 Case Study: Why Diversification Failed

Calendar-year 2022 returns by asset class (Damodaran + standard data):

- S&P 500: -18%.
- 10-year Treasury: -18%.
- 30-year Treasury (TLT): -31%.
- High-yield corporates (HYG): -11%.
- REITs (VNQ): -24%.
- Gold (GLD): +0.4%.
- DXY: +8%.
- Bitcoin: -65%.

A textbook 60/40 lost 16-17%. Risk-parity portfolios (which lever bonds) lost even more. The reason was singular: a +425bps Fed shock simultaneously hit every long-duration asset. Correlation was not "broken" -- correlation was always conditional, and the condition was a benign rate environment. When the rate environment became hostile, correlation showed its true face.

![Bar chart of calendar-year 2022 total returns across the major asset classes: S&P 500 -18%, 10y Treasury -18%, 30y Treasury (TLT) -31%, high-yield corporates (HYG) -11%, REITs (VNQ) -24%, gold (GLD) +0.4%, US dollar (DXY) +8%, Bitcoin -65%. The negative bars dominate the picture; only gold and the dollar finished positive. The chart is the empirical proof that diversification is conditional on the driving variable not being shared — a +425bps Fed shock simultaneously hit every long-duration asset, regardless of label.](image/week34_2022_case.png)

The investor's takeaway is not "diversification is dead." It is "diversification is over the *driving variable*." If your six assets all share rate sensitivity, you do not own six assets -- you own one trade in six wrappers. To diversify in a rate-driven world you need exposures that respond to *different* drivers: cash, gold (real-rate hedge), short volatility (the vol tail is what wags the dog), or genuine alpha.

---

### 3. Common Misconceptions

1. **"Stocks always hedge bonds."** Only when growth shocks dominate rate shocks. In an inflation-driven regime they fall together. The 1970s and 2022 are the proof.

2. **"Growth stocks are equity, not bonds."** Mathematically false. A stock priced on cash flows 15 years out has more duration than a 15-year bond. The label does not change the math.

3. **"Gold is an inflation hedge."** Gold is a *real-rate* hedge. If inflation rises and nominal rates rise faster (1980), gold falls. If inflation rises and nominal rates lag (2020-2024), gold rises.

4. **"REITs are real assets, so they hedge rates."** No. REITs are levered long-duration cash flow streams. They are *more* rate-sensitive than the stock market, not less.

5. **"The dollar always rallies in a crisis."** True for liquidity crises (2008, 2020), false for confidence crises in the dollar itself (2002-2003, late-1970s). The driver is the rate spread, not the panic level.

6. **"+100bps is a rare event."** The Fed has moved +100bps in a single year roughly once a decade since 1970. Pricing portfolios for 0bps moves is a cognitive bias, not a calibration.

7. **"Bond duration is just the maturity."** Modified duration accounts for coupons. A 30-year zero has $D \approx 30$. A 30-year coupon bond has $D \approx 16$. Big difference.

8. **"Diversification is about owning many things."** It is about owning many *uncorrelated* things. Owning ten long-duration assets is owning one trade ten times.

9. **"Crypto is a hedge."** Bitcoin in 2022 was the highest-duration asset in the world: -65% on a +425bps shock. Hedge is the opposite of what it did.

10. **"Real estate doesn't move much because it's illiquid."** It moves the same amount, just on a lag. Public REIT prices reveal the truth in real time; private real estate marks lag by 12-18 months.

---

### 4. Q&A Section

**Q1: How do I quickly estimate the rate impact on a stock I own?**
A: Look at its forward P/E. A P/E of 30 implies most of the value is far-future cash flow, and duration is roughly P/E × 0.7. A P/E of 30 stock has $D \approx 21$, so +100bps takes off ~21%. A P/E of 12 stock has $D \approx 8$, so the same shock takes off ~8%. It is a back-of-envelope rule but it is shockingly close.

**Q2: Should I avoid long bonds entirely?**
A: No -- you should own them deliberately. A 30-year Treasury (TLT, EDV) is one of the only assets that *positively* benefits from a recession-driven rate cut. In a recession scenario stocks fall and TLT rises 20-30%. The trick is sizing it small enough that the 16% loss on +100bps is survivable. Treat TLT as a tail-risk hedge, not a bond holding.

**Q3: What about TIPS?**
A: Treasury Inflation-Protected Securities have *lower* duration than nominal Treasuries because part of the cash flow comes from CPI accruals. A 10-year TIPS has $D \approx 7$ and reacts to *real* rates only. They are the cleanest rate hedge if you specifically fear stagflation.

**Q4: Why did my "balanced" 60/40 fund lose 17% in 2022?**
A: Both legs shared the same driver (long-duration discounting). When the discount rate jumped 250bps, both legs marked down at once. The same fund made money in 2008 because that was a *growth* shock, not a *rate* shock -- bonds rallied while stocks fell. Different driver, different outcome.

**Q5: How do I hedge rate risk without selling everything?**
A: Three options: (1) shorten bond duration by replacing TLT with IEI or even SHV; (2) buy puts on TLT or QQQ (cheap when realized vol is low, and the option wrapper is the most tax-efficient way to take leverage in a US taxable account); (3) hold cash equivalents (BIL, SGOV) which have zero duration and earn the front-end rate. We will cover put-spread tail hedges in Week 47.

**Q6: Does this apply internationally?**
A: Yes, but with the dollar overlay. A foreign bond hit by +100bps in the local rate falls by its local duration in local currency. If the dollar simultaneously rallies, the dollar-translated loss is amplified. This is one reason we keep the long sleeve US-only.

**Q7: Why are utilities and consumer staples called "bond proxies"?**
A: Their dividends are stable and slow-growing, so most of their value is far-future cash flow. They have duration similar to a 15-year bond. In 2022 utilities fell 1% (resilient); in 2008 they fell 30% (credit shock dominated). They behave like bonds *as long as the rate channel is the only channel firing*.

**Q8: What is the "rate sensitivity" of my emergency fund?**
A: Zero, by construction. T-Bills (BIL, SGOV), money-market funds, and savings accounts have $D < 0.25$. That is the point: the cash sleeve is the only sleeve that does not move with rates, which makes it the only true diversifier in a rate-driven world. The barbell construction has cash on one end for exactly this reason.

**Q9: How much can the +100bps move actually be?**
A: Historically, the Fed has moved +400 to +525bps in a single tightening cycle (1981, 1994, 2004-2006, 2022-2023). Pricing your portfolio for "+100bps" is the *modest* scenario. The interactive lab lets you push the shock to ±300bps to see what the tail looks like.

**Q10: Where does this fit in the four-tranche framework?**
A: Cash tranche: zero rate sensitivity. Beta tranche: holds the unavoidable rate exposure of the equity index ($D \approx 18$). Factor tranche: tilted toward shorter-duration value (lower $D$) for partial hedging. Alpha tranche: deliberately uses TLT, options on TLT, and gold to take rate views actively. Knowing the duration of each tranche is the first step in deciding how much rate risk you actually carry.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Rate Sensitivity Across Every Asset Class -- The Hidden Variable That Moves Everything (Week 34)
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

### INTRO (00:00-01:30)

**STELLA:** Welcome back. I'm Stella, and I'm here with Horace. Today is Week 34, and the topic is one of those things that sounds dry until you realize it secretly explains every market crisis of the last fifty years.

**HORACE:** Rate sensitivity. The single hidden variable that connects bonds, stocks, real estate, gold, and even the dollar.

**STELLA:** Why is this so important?

**HORACE:** Because in 2022 a lot of people learned that diversification is not a free lunch. The 60/40 portfolio lost 17%. Risk-parity funds lost more. People who thought they were spread across uncorrelated assets discovered that *one* variable -- the discount rate -- was driving everything they owned.

**STELLA:** And that is what we are going to unpack today. By the end of this video you will be able to estimate, in your head, how much each asset class moves on a +100bps Fed shock.

**HORACE:** Let's start with the master formula.

[VISUAL: image/week34_rate_shock_grid.png]

---

### SECTION 1 -- THE MASTER FORMULA (01:30-03:30)

**HORACE:** Every asset on Earth is priced as the present value of its future cash flows. Stella, you remember the formula?

**STELLA:** Price equals the sum of cash flow at time t, divided by 1 plus the discount rate, raised to the t.

**HORACE:** Exactly. And modified duration is just the percentage price change for a 1% change in r. The longer the cash flow timeline, the larger the duration, the more violently the asset moves on a rate shock.

**STELLA:** So duration is not just a bond concept.

**HORACE:** Right. It applies to anything with future cash flows. Stocks, real estate, infrastructure, private equity. The trick is most people stop teaching duration after the bond chapter, so they never realize that QQQ has the duration of a 22-year bond.

**STELLA:** OK, so let's go through the asset classes.

---

### SECTION 2 -- THE BAR CHART (03:30-07:00)

[VISUAL: image/week34_rate_shock_grid.png]

**HORACE:** This bar chart shows the estimated price impact of a parallel +100bps shock across eight asset classes.

**STELLA:** Walk me through it from left to right.

**HORACE:** 5-year Treasury: down 4.5%. 10-year: down 8%. 30-year: down 16%. That is the bond ladder, and the relationship is roughly linear in duration.

**STELLA:** Then equities.

**HORACE:** Growth equity, the QQQ-style basket: down 12%. Value equity, the VTV-style basket: down only 3%. Why the gap?

**STELLA:** Different durations.

**HORACE:** Exactly. A growth company's value lives 15-20 years out. A value company's value lives 3-5 years out. Same shock, four times the impact on growth.

**STELLA:** Then REITs.

**HORACE:** Down 10%. REITs are basically a leveraged 15-year bond -- long-dated rent streams, levered roughly 50% on debt. They are *more* rate-sensitive than the broad market.

**STELLA:** Gold and the dollar?

**HORACE:** Gold is mixed: anywhere from -2% to +5% depending on whether the rate move is real or nominal. We will get to that. The dollar typically rallies 1-3% on a hawkish surprise.

**STELLA:** So if I held a "diversified" portfolio of growth stocks, REITs, and 30-year bonds, I'm not actually diversified.

**HORACE:** You own one trade three times.

---

### SECTION 3 -- BONDS AND EQUITIES, ONE LADDER (07:00-09:30)

**HORACE:** This is the conceptual jump that fixes most of people's portfolio mistakes. Stocks and bonds are on the *same* duration ladder.

**STELLA:** Show me the proof.

**HORACE:** 2022 was the cleanest natural experiment we have ever had. The 10-year Treasury yield rose from 1.5% to 4%. ARKK fell 67%. QQQ fell 33%. VTV fell 5%. That ranking is a perfect duration ladder. The labels say "tech ETF" and "value ETF," but the math says "long-duration cash flow" and "short-duration cash flow."

**STELLA:** And the bond ladder ran in parallel.

**HORACE:** TLT fell 31%. The 10-year fell 18%. The 5-year fell 9%. Stocks and bonds were not "decoupled" or "broken" -- they were behaving exactly the way the duration formula predicts.

---

### SECTION 4 -- REAL ESTATE AND THE LEVERAGE AMPLIFIER (09:30-11:30)

**HORACE:** Real estate deserves its own callout because it has a leverage amplifier.

**STELLA:** What does that mean?

**HORACE:** Most commercial real estate is financed roughly 50% with debt. So when rates rise, two things happen at once. First, cap rates expand, which means future rents are discounted at a higher rate. Second, refinancing the existing debt becomes more expensive. Both effects push equity value down.

**STELLA:** And the office sector got hit worst.

**HORACE:** 2022-2024, some office buildings lost 40 to 50% of equity value. Cap rates went from 5% to 7 or 8% on the same rent. That is duration plus leverage -- a brutal combination.

**STELLA:** So if I want real estate exposure with less rate risk?

**HORACE:** Pick lower-leverage REITs, shorter-lease sectors like industrial or self-storage, and size the position smaller than you would for the broad market. Or just hold the broad VNQ and treat it as the leveraged 15-year bond it actually is.

---

### SECTION 5 -- GOLD AND THE REAL-RATE LENS (11:30-13:30)

**HORACE:** Gold breaks the duration formula because it has no cash flow.

**STELLA:** So how do we price it?

**HORACE:** As a function of *real* rates. The 10-year nominal yield, minus the breakeven inflation rate. When real rates rise, gold falls -- the opportunity cost of holding zero-yield gold went up. When real rates fall, gold rises.

**STELLA:** What about 2022 then? Rates rose, but gold barely moved.

**HORACE:** Because nominal rates rose violently *and* inflation rose violently. Real rates only edged up. So gold ended the year at +0.4%. It is the case study that proves the real-rate framework. Compare that to 1980 when Volcker pushed nominal rates above inflation -- real rates went sharply positive and gold collapsed from $850 to $300.

**STELLA:** And gold is a store of value only because enough people believe it is.

**HORACE:** Real rates are the mechanism of that belief. When real rates are positive and stable, the gold story weakens. When real rates are negative, the story gets stronger.

---

### SECTION 6 -- THE DOLLAR AS A SPREAD (13:30-14:30)

**HORACE:** The dollar is the last piece. DXY is not a level, it is a relative price -- US rates versus foreign rates.

**STELLA:** So a +100bps shock to the world doesn't move DXY.

**HORACE:** Right. A +100bps shock to *just* the US, with the ECB and BoJ on hold, pushes DXY up 5-10%. That is what 2022 was. We stay US-only on the long side, and the dollar is exactly the reason that works -- when the dollar rallies, we are paid in the strong currency while foreign markets get hit by both their own rate move and the FX translation.

---

### SECTION 7 -- THE 2022 CASE STUDY (14:30-16:30)

[VISUAL: image/week34_2022_case.png]

**HORACE:** Here is the bar chart of calendar-year 2022 returns. S&P 500: -18%. 10-year Treasury: -18%. TLT: -31%. REITs: -24%. Gold: +0.4%. DXY: +8%. Bitcoin: -65%.

**STELLA:** Diversification looks dead in this picture.

**HORACE:** Diversification was always conditional on the *driving variable* not being shared. In a rate-driven year, every long-duration asset moves together. The only things that worked in 2022 were the assets with low or negative rate sensitivity: cash, gold, the dollar, and certain commodities.

**STELLA:** So the lesson is...

**HORACE:** Diversify over drivers, not over labels. Owning ten long-duration ETFs is owning one trade ten times.

---

### SECTION 8 -- THE INTERACTIVE LAB (16:30-17:30)

[VISUAL: interactive/week34_shock_lab.html]

**HORACE:** The interactive this week is a stress-test lab. Three sliders: rate shock from minus 300 to plus 300 basis points, inflation shock from minus 3 to plus 3 percent, and dollar shock from minus 10 to plus 10 percent. Move them and watch the eight asset-class bars update in real time.

**STELLA:** And you have presets for famous regimes.

**HORACE:** 1981 Volcker, 2008 GFC, 2020 COVID, 2022 inflation shock, and a 2026 mild scenario. Click each one and you can see what each historical episode did to a balanced portfolio.

**STELLA:** The Volcker preset is shocking.

**HORACE:** That is the regime the parents of most of our viewers lived through. After a forty-year falling-rate tailwind, it is the regime we have to take seriously again.

---

### OUTRO (17:30-18:00)

**HORACE:** Three takeaways. One: every asset's duration is its rate sensitivity, not just bonds. Two: in a rate-driven year, all long-duration assets correlate to one. Three: the only true diversifiers are cash, gold via real rates, and assets with genuinely different drivers.

**STELLA:** Next week is Week 35 -- Treasury Inflation-Protected Securities. The clean rate hedge.

**HORACE:** And in Week 47 we will use the framework from today to size a tail-risk hedge against the next 2022.

**STELLA:** See you next week.
