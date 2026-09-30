## Part 2: YouTube Script

---

**VIDEO TITLE:** Replacing Stock With Deep-ITM Calls — Real Capital, Real Math, Real Risks

**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00-1:30]**

**Stella:** Welcome back to the Chan Investing tutorial. I'm Stella, and today we're on Week 37 — using options as leverage. Specifically, the trade where you replace 100 shares of stock with one deep-in-the-money call. Horace, you've described this as the cleanest piece of leverage a retail investor can run. Why is that?

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

**Horace:** SSO is fine for short-term tactical leverage. For 12-month-plus exposure, deep-ITM LEAPS dominates on path-independence and on tax. Leverage via options is the most tax-efficient form of leverage available to a US retail investor — that's what this chart is showing you in dollars.

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

**Stella:** And the tax case.

**Horace:** A LEAPS held more than a year qualifies for long-term capital gains, same rate as the stock. A 2x ETF passes through ordinary-income distributions every year, and your basis adjusts every distribution. The LEAPS gives you the leverage with the better tax envelope. In a Roth IRA, the freed cash earns the risk-free rate tax-free — that's the cleanest version of the trade.

**Stella:** And how does this fit the four-tranche framework?

**Horace:** L1 is your beta sleeve — VTI, SPY, whatever you use as the index core. Stock replacement converts that sleeve from 100% capital to roughly 25% capital. The freed 75% funds L2 strategy sleeves — covered calls, cash-secured puts, factor tilts — without reducing your beta exposure. That's the operational mechanism behind the barbell. The barbell only works if you can hold full beta with less than full capital.

**[OUTRO — 16:30-18:00]**

**Stella:** Three things to take with you. First — delta is the leverage dial; the trade we covered today is the 0.85-0.95 delta band. Second — the freed cash is real money; do not let it sit in checking. Third — leveraged ETFs decay; LEAPS don't. The LEAPS is the institutional default for a reason.

**Horace:** And one principle — do this only on liquid underliers when IV is reasonable, do this only with discipline on rolling at 90 DTE, and do not confuse stock replacement with the lottery-ticket trade. They use the same instrument family. They are not the same trade.

**Stella:** Next week we tackle the poor-man's covered call — the natural pairing of the LEAPS we built today with a sold short call. See you then.

**Horace:** See you next week.
