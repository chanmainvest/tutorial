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
