## Part 2: YouTube Script

---

**VIDEO TITLE:** Week 44 — Inside the Black Box: How Your Order Actually Gets Filled (NBBO, Dark Pools, PFOF, and the Microsecond Economy)
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00 to 1:30]**

[VISUAL: title card, then quick montage of an order ticket, a Nasdaq tower shot, and a server rack in Carteret NJ]

**Horace:** Welcome back to Chan Main Investment. Forty-three weeks ago we started with the simple act of clicking "buy." This week we open up the trapdoor underneath that button and look at the gears.

**Stella:** Microstructure. The actual machine that takes your order and turns it into a print on the tape.

**Horace:** Most retail investors never think about it. The commission is zero, the fill price looks reasonable, the trade settles two days later, life moves on. But somewhere between your click and the tape, somebody made money on you. Not a lot — measured in basis points. Multiplied by trillions of shares a year, it adds up to industry revenue of about three billion dollars in 2024 just from payment for order flow alone.

**Stella:** And the fact that you can't see it doesn't mean it isn't there.

**Horace:** Alpha is rare, and the structural alpha sources — speed, queue position, latency arbitrage — are mostly arbed out by Citadel and Virtu and Jane Street co-located in Mahwah and Carteret. We are not going to teach you to compete with them. We're going to teach you to stop being their counterparty by accident.

**Stella:** Today: NBBO and Reg NMS, the six order types you actually need, dark pools, payment for order flow, the latency arbitrage gap, and what the 2010 flash crash taught us about how this whole machine breaks.

---

**[SECTION 1 — Reg NMS and the NBBO — 1:30 to 4:00]**

[VISUAL: image/week44_order_book.png — limit order book schematic]

**Horace:** Start with the rulebook. Reg NMS, 2007. Two pieces matter. One: the Order Protection Rule says no exchange may execute your trade at a price worse than the best displayed quote on any other exchange. Two: that "best quote" is consolidated into something called the National Best Bid and Offer — the NBBO.

**Stella:** Sounds protective.

**Horace:** It is, on price. But forcing every venue to honour every other venue's quote made it economically rational to spin up *more* venues, because each new venue can collect routing fees from the rest. As of April 2026 we have sixteen registered stock exchanges and roughly thirty alternative trading systems. The same AAPL trades on all of them simultaneously.

**Stella:** Walk me through the order book on screen.

**Horace:** Here's a synthetic top-five-deep limit order book in some name trading around fifty bucks. Left side, in red, the asks — sellers. Top of the ask stack — the *inside offer* — is fifty-zero-five for two hundred shares. The next level up is fifty-zero-eight for five hundred shares. Then fifty-ten, fifty-twelve, fifty-fifteen with bigger size higher up.

**Stella:** And the bids on the right.

**Horace:** Bids in blue, descending. Best bid fifty-zero-three for three hundred shares, then fifty-zero-one, forty-nine ninety-eight, forty-nine ninety-six, forty-nine ninety-four. Spread is two cents. NBBO midpoint is fifty-zero-four.

**Stella:** Now somebody fires a one-thousand-share market buy.

**Horace:** It eats the inside offer entirely. Two hundred shares fill at fifty-zero-five. The router moves to the next level — five hundred at fifty-zero-eight. Then it walks into the third level and partial-fills three hundred at fifty-ten. Volume-weighted fill price comes out at fifty-zero-eight-point-seven. Almost five cents over the original midpoint. That's price impact. Walking the book.

**Stella:** Visible from the diagram — the order eats through the red shaded levels in sequence.

**Horace:** And this is in a name with a normal-looking book. In a thin small-cap with twenty shares deep at each level, a thousand-share market order can move the print a full percent.

---

**[SECTION 2 — Order types — 4:00 to 6:30]**

[VISUAL: switch to interactive — interactive/week44_order_lab.html]

**Stella:** This is where the choices matter. The order type menu.

**Horace:** Six standing orders, four institutional algos. The menu. Market — fill now, no price guarantee. Limit — fill at this price or better, or don't fill. Stop — trigger a market when the print hits X. Stop-limit — trigger a limit when the print hits X. IOC — fill what's available now and cancel the rest. FOK — fill the whole thing now or cancel everything.

**Stella:** And if I'm a normal retail investor.

**Horace:** Default is limit. Marketable limit when you want immediate execution — buy at the current offer. That's a market order with a hard ceiling, in case the offer just moved. Use a stop-limit for stop-losses, never a plain stop, especially in anything illiquid.

**Stella:** Tell me about the algos.

**Horace:** TWAP — time-weighted, equal slices across a window. VWAP — volume-weighted, heavier near the open and close where actual volume is. Implementation shortfall — front-loaded, used when urgency matters. POV — percent-of-volume, stay under a target participation rate so you don't move the print.

**Stella:** Retail doesn't get those.

**Horace:** Retail gets the equivalent by manually splitting orders across a few sessions. Anything over half a percent of the name's ADV — average daily volume — should be sliced. For SPY, ADV is eighty million shares; you could ticket forty million dollars and barely register. For a two-hundred-million-cap small-cap with two hundred thousand share ADV, a five thousand share order is two and a half percent — material.

[VISUAL: cursor moves to interactive, picks "1,000,000 shares" and "Market" — shows red impact bar]

**Stella:** Look at the slippage bar when I click market on a million shares.

**Horace:** A hundred and sixty basis points expected impact on this synthetic book. Now switch to TWAP across the day.

**Stella:** Drops to about thirty bps.

**Horace:** Five times cheaper, at the cost of taking six hours to fill. That's the trade-off.

---

**[SECTION 3 — Dark pools — 6:30 to 9:00]**

**Horace:** About fifteen percent of US equity volume executes inside formal dark pools. Goldman SIGMA-X, UBS ATS, Credit Suisse Crossfinder, IEX, Liquidnet — those are the big ones. Another thirty percent executes off-exchange via wholesalers and single-dealer platforms. Together, "off-exchange" volume runs forty to forty-five percent of consolidated tape on a normal day.

**Stella:** Why do they exist?

**Horace:** Imagine you're a pension fund and you want to buy fifty million dollars of some name. If you put that order on the lit exchange, every HFT algo in Carteret sees it and front-runs you. By the time you're done, the price is twenty-five basis points higher and they pocketed the difference.

**Stella:** Ugly.

**Horace:** Right. So instead, you cross the order at the midpoint of NBBO inside a dark pool, ideally with another natural seller — maybe a hedge fund unwinding the same position. Both sides save the spread. Both sides avoid impact. The trade prints to the tape after execution, after it's too late to game.

**Stella:** Sounds clean.

**Horace:** The concept is clean. The execution wasn't always. Every major dark pool operator has been fined at least once for misrepresenting how the pool actually worked — usually because they let their own prop desk see customer order flow before the customer's order executed. Goldman, Credit Suisse, Barclays, ITG — all paid SEC settlements in the 2014-2016 window.

**Stella:** And retail.

**Horace:** Retail can't access dark pools directly. But your broker's smart-order router probably pings them on your behalf before going to the exchange — looking for midpoint crosses. When your fill comes back marked "PI" — price improvement — that's where it usually came from.

---

**[SECTION 4 — Payment for order flow — 9:00 to 12:00]**

[VISUAL: image/week44_pfof_flows.png — Sankey-style retail-broker-wholesaler-exchange flow]

**Horace:** Now the controversial part. Payment for order flow.

**Stella:** Robinhood and Citadel.

**Horace:** Robinhood, but also Schwab, Webull, Public, Fidelity for options. The deal: a retail broker routes its customer orders to a wholesale market maker — Citadel Securities, Virtu, Susquehanna, Jane Street, G1X — in exchange for a per-share payment. Industry-wide PFOF revenue ran about three to three-and-a-half billion dollars in 2024 across equities and options.

**Stella:** Look at the diagram. Customer to broker, broker to wholesaler, wholesaler to exchange or internalisation. And the dollar arrows.

**Horace:** Retail click generates an order. Broker routes it — and gets paid roughly half a cent per equity share or fifty cents per options contract from the wholesaler. Wholesaler internalises about seventy percent of equity flow against its own inventory at NBBO or slightly better, prints the trade to the tape, pockets the spread.

**Stella:** Why does the wholesaler pay for it?

**Horace:** Because retail flow is *uninformed*. When a Robinhood user buys twenty-five shares of NVDA, that trade carries no negative selection. Citadel can fill at NBBO plus two-hundredths of a penny price improvement, pay the broker, and still make money on the spread because the trade is uncorrelated with where NVDA is going in the next five minutes.

**Stella:** Retail gets a tiny bit of price improvement.

**Horace:** Right. On a hundred-share order in AAPL, you might save half a cent — fifty cents total. Beats paying a four-dollar commission. The math actually works for small uninformed flow.

**Stella:** Where does it stop working?

**Horace:** Two places. One: order size. Above five to ten thousand shares the wholesaler stops improving — your flow starts to look informed and the spread cost becomes real. Two: options. Options PFOF is roughly ten times equities per share-equivalent because options spreads are wider and the wholesaler's edge per fill is bigger. Eighty percent of retail options flow goes to about five wholesalers. The cost shows up as five to fifteen cents per contract relative to the NBBO midpoint.

**Stella:** And the tax angle.

**Horace:** Exactly the point I'd make. Taxes via options and margin. Options trades are where PFOF actually starts to matter for cost. If you're writing covered calls or cash-secured puts every month, the cumulative drag from suboptimal options execution can eat fifty to a hundred basis points off your annual yield. That's a real number.

---

**[SECTION 5 — Latency arbitrage — 12:00 to 14:00]**

**Horace:** The microsecond economy.

**Stella:** Reg NMS guarantees the NBBO at execution. But the NBBO is a moving target.

**Horace:** Right. The SIP — the Securities Information Processor — is the consolidator that produces the official NBBO. SIP latency runs three hundred to five hundred microseconds in 2026. Direct exchange feeds — the proprietary feeds each exchange sells to HFT firms — are about fifty microseconds.

**Stella:** A three-hundred-microsecond gap.

**Horace:** That's where latency arbitrage lives. HFT sees a buy print on Nasdaq's direct feed at fifty-zero-five. The SIP NBBO still reads fifty-zero-four offer because the SIP hasn't propagated. HFT fires across all the other exchanges and lifts the stale fifty-zero-four offers everywhere — picking off orders that are two hundred microseconds out of date. By the time the SIP updates, those orders are gone.

**Stella:** That's not theoretical.

**Horace:** No, it's industrial-scale. Estimates put latency-arb-related profits at one to two billion dollars a year. IEX — the speed-bump exchange that the *Flash Boys* book is about — installed a three-hundred-fifty-microsecond physical coil of fibre to delay inbound orders, neutralising the gap. Three to four percent of US volume routes there. The other ninety-six percent still runs the speed-favours-the-fast model.

**Stella:** Retail can't compete.

**Horace:** Cannot. Same point again — structural alpha source, captured by the fastest. What retail can do is route to IEX when possible, avoid trading the open and close where SIP-vs-direct gaps are widest, and — most importantly — use limit orders so you're the one quoting, not the one being picked off.

---

**[SECTION 6 — Slippage on size — 14:00 to 15:30]**

**Stella:** The square-root impact rule.

**Horace:** Almgren-Chriss, calibrated for liquid US equities in 2026: expected slippage in basis points is roughly ten times the square root of order size as a percentage of ADV.

**Stella:** Let's plug in.

**Horace:** One percent of ADV — ten bps. Four percent — twenty bps. Twenty-five percent — fifty bps. So a million dollars of SPY at eighty million ADV is one-eightieth of one percent of ADV. Slippage rounds to zero.

**Stella:** A million dollars of a two-hundred-million-cap small-cap.

**Horace:** Two hundred thousand share ADV. A million-dollar ticket at, say, twenty bucks a share is fifty thousand shares — twenty-five percent of ADV. Square-root model says fifty bps. In practice probably more, because the model is calibrated on average days, not on the day a previously-uncovered investor moves a quarter of the daily volume.

**Stella:** Hence break it up.

**Horace:** Break it across days. Use limit orders. Avoid the open and close. The interactive on screen lets you punch in different sizes and order types and see the trade-off live.

---

**[SECTION 7 — Flash Crash — 15:30 to 16:45]**

**Horace:** May sixth, 2010, 2:32 PM Eastern. The Dow fell roughly nine percent — a thousand points — in minutes.

**Stella:** And recovered most of it by 3:08.

**Horace:** Right. The post-mortem identified a single four-point-one-billion-dollar sell program in E-mini S&P futures, run with no price floor by a Kansas mutual fund. That program drained futures liquidity, triggered cross-asset HFT arbitrage selling in equities, and as realised volatility spiked, equity market makers withdrew their quotes simultaneously to avoid adverse selection.

**Stella:** With no resting bids.

**Horace:** Stub-quote sells — placeholder one-cent bids that nobody intended to actually trade — became the actual prints. Accenture printed at one cent. Sotheby's at ninety-nine-thousand-nine-hundred-ninety-nine dollars. For a few seconds.

**Stella:** Vol-tail-wags-dog, again.

**Horace:** Exactly. The fragility wasn't the algo that kicked it off — those exist by the thousand. The fragility was that *every* market maker withdrew at the same moment because the same risk model told all of them to. When the providers of liquidity all pull at once, there is no liquidity.

**Stella:** And the regulators responded.

**Horace:** Single-stock circuit breakers — Limit Up Limit Down bands. Market-wide breakers at minus seven, thirteen, twenty percent. The consolidated audit trail. Those have prevented a literal repeat. The underlying fragility — market makers withdrawing in tail volatility — is unchanged. We saw it again in March 2020, in a smaller form.

---

**[OUTRO — 16:45 to 18:00]**

**Stella:** What's the takeaway for someone who is not going to start a market-making firm?

**Horace:** Three rules.

One. Limit orders by default. Marketable limits when you need immediate fills. Stop-limit, never plain stops. The order ticket is the one place you have actual control over execution quality, and most retail traders give it away by clicking market.

**Stella:** Two.

**Horace:** Size relative to ADV is the variable that matters. Small in liquid equity names, you're invisible — costs round to zero. Large or in thin names, you walk the book. Know which side of that line your tickets are on.

**Stella:** Three.

**Horace:** PFOF and dark pools are not the enemy at retail size. They're the actual mechanism delivering you the surprisingly-good fills. The enemy is your own choice of order type and size.

**Stella:** Two ideas combined: structural alpha is rare, and the tail breaks the system.

**Horace:** Right. One — structural alpha is real and almost entirely arbed out by HFTs. Two — the fat tail is where the system breaks, and your stops are where you become the print. Don't be the print.

**Stella:** Next week: regulation, securities law, and how the SEC actually functions in 2026. Subscribe, see you then.

[END]
