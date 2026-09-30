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
