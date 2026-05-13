# Week 44: Market Microstructure — Order Types, NBBO, Dark Pools, and Payment for Order Flow

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every "buy" click on a brokerage app sets in motion a routing machine that costs more than the zero commission suggests. The plumbing of US equity markets — exchanges, dark pools, wholesalers, smart-order routers, microwave links between New Jersey and Chicago — was redesigned by Reg NMS in 2007, and it has been quietly siphoning a few basis points out of every retail and institutional fill for two decades. Most investors never see it. That ignorance is the problem.

1. **Hidden costs eat returns more reliably than fees do.** The advertised commission is $0. The bid-ask spread, the price impact of size, the half-tick the wholesaler captures, the timing risk while a TWAP works through the day — those add up to 5-30 basis points on a typical retail equity round-trip and 30-80 bps on a $1M institutional ticket. Over a 30-year compounding career a constant 20 bps drag costs roughly 6% of terminal wealth. You don't see the bill, but it is paid.
2. **Order type selection is one of the few free levers a retail investor actually has.** A market order in AAPL at 3:59 PM behaves differently from a marketable limit at the NBBO, which behaves differently from a midpoint peg in a dark pool. Structural alpha exists but is rare and mostly arbed out by HFT firms — what is left for retail is the *defensive* version of microstructure literacy: stop being the dumb flow.
3. **Liquidity disappears at the worst possible moment.** The 2010 Flash Crash, the August 2015 ETF dislocation, the March 2020 COVID gap, the 2024 yen-carry unwind — every regime episode rhymes with the same fact: market makers widen quotes or pull them entirely when realised vol spikes. The vol tail wags the dog here. If your stop-loss is a market order parked in an illiquid name during a volatility event, you will be the print at the bottom.
4. **The retail-vs-institutional routing gap is real, and the rules favour you only on small size.** PFOF wholesalers (Citadel Securities, Virtu, Susquehanna, Jane Street) actually price-improve sub-1,000-share retail orders by a fraction of a cent, because retail flow is uninformed and profitable to internalise. The same machinery taxes you the moment your order grows large enough to look informed — at roughly 5,000-10,000 shares the price improvement vanishes and slippage shows up. Knowing where the inflection is keeps you from accidentally walking the book.

This week is not about becoming a trader. It is about understanding what happens after you click, so that your fills stop being a tax on your savings.

---

### 2. What You Need to Know

#### 2.1 Reg NMS, the NBBO, and why fragmentation exists

Regulation NMS (National Market System), effective 2007, is the rulebook that holds modern US equity markets together. The two pieces you must know are the **Order Protection Rule (Rule 611)** — no exchange may execute a trade at a price worse than the best displayed quote on any other exchange — and the **NBBO (National Best Bid and Offer)**, the consolidated top-of-book across all 16 lit exchanges.

The unintended consequence of forcing every venue to honour every other venue's quote is that it became economically rational to spin up *more* venues. As of April 2026 the US has 16 registered stock exchanges (NYSE, Nasdaq, BATS/Cboe BZX/EDGX/BYX/EDGA, IEX, MEMX, MIAX, Long-Term Stock Exchange, etc.) plus roughly 30 alternative trading systems (ATSs, i.e. dark pools). Each exchange charges different maker/taker rebates, and brokers' smart-order routers slice your order across them based on rebate economics, latency, and fill probability. You see one fill at one price; the order may have touched five venues in 200 microseconds. Reg NMS guarantees you weren't filled *worse* than NBBO; it guarantees nothing about whether you got the *midpoint*, which is where the spread cost lives.

![Schematic limit order book showing bid and ask ladders, NBBO spread, and the price impact of a market order eating through three ask levels.](../image/week44_order_book.png)

#### 2.2 Order types: market, limit, stop, stop-limit, IOC, FOK, and the algos

The retail menu has six standing-order types and roughly four institutional algos. Internalise the trade-offs once and you'll never use the wrong one again.

- **Market order.** "Fill me now at whatever clears." Guaranteed fill, zero price guarantee. Fine for 100 shares of SPY at 11 AM. Catastrophic for 5,000 shares of a $30 small-cap or a $200 illiquid options contract.
- **Limit order.** "Fill at $X or better, or don't fill." Default for any retail trade larger than 200 shares or in any name with a spread wider than a penny. A *marketable* limit (buy limit at the offer) gets you the certainty of a market order with a hard ceiling.
- **Stop / stop-loss.** "Trigger a market order when last trade hits $X." Do not use in illiquid names. In a gap-down open at -10%, a stop at -5% sells you at -10%, not at -5%.
- **Stop-limit.** Trigger a limit order instead of a market order on the same condition. Protects against terrible fills, but may not fill at all in a gap.
- **IOC (Immediate-Or-Cancel).** Fill what you can right now at the limit price; cancel the rest. Used by smart-order routers to ping multiple venues without leaving residual exposure.
- **FOK (Fill-Or-Kill).** Fill the entire size at the limit, immediately, or cancel everything. Rare for retail; used for block prints and arbitrage legs that must execute together.

Above standing orders sit the institutional **execution algorithms**: TWAP (time-weighted average price — equal slices across a window), VWAP (volume-weighted — heavier near open and close where volume is), Implementation Shortfall (front-loaded against urgency), and POV (percent-of-volume — track a target participation rate). These exist because clicking a 500,000-share market order would print a fill 50-200 bps worse than the day's VWAP and tip off every HFT in Secaucus that someone is moving size.

#### 2.3 Dark pools and the 15-45% off-exchange share

A **dark pool** is an ATS that accepts orders without displaying quotes pre-trade. Trades print to the consolidated tape after execution but before then no one outside the pool knows a buyer at $X exists. As of 2025 roughly 15% of US equity volume executes inside formal dark pools (Goldman SIGMA-X, UBS ATS, Credit Suisse Crossfinder, IEX, Liquidnet) and another 30% executes off-exchange via wholesalers and single-dealer platforms — together "off-exchange" volume runs 40-45% of consolidated tape on most days.

Why dark pools exist: a $50M institutional buy program shown openly on a lit exchange invites HFT front-running. Cross the same size at the midpoint inside a pool with another natural seller and both sides save the spread plus avoid the impact. Why they're controversial: pool operators historically routed customer orders against their own prop trades, and post-trade tape latency means dark-pool prints can be used to update lit quotes faster than retail can react. The SEC has fined every major pool operator at least once for misrepresenting how the pool actually worked.

Practical retail takeaway: when your broker says "executed at the midpoint" or "PFOF rebate," your order touched a wholesaler's internal pool, not an exchange. That is not necessarily bad — for sub-1,000-share retail flow, midpoint internalisation is often cheaper than crossing the spread on a lit venue.

#### 2.4 Payment for order flow (PFOF)

PFOF is the deal where a retail broker (Robinhood, Schwab, Webull, Public, Fidelity for options) routes its customer orders to a wholesale market maker (Citadel Securities, Virtu, Susquehanna, Jane Street, G1X) in exchange for a per-share payment. Industry-wide PFOF revenue ran roughly **$3.0-3.5 billion in 2024** across equities and options, with options paying ~10× equities per contract because options spreads are wider and the wholesaler's profit per fill is larger.

The economic claim that defenders make is that retail flow is *uninformed* — when a Robinhood user buys 25 shares of NVDA, the trade carries no negative selection for the market maker. Citadel Securities can internalise the order at NBBO + 0.0002 (a fraction of a cent of price improvement), pay Robinhood half a penny per share for routing it there, and still make money from the spread because the trade is uncorrelated with short-term price moves. The math works because retail is dumb flow in the technical, non-pejorative sense.

The critique: the routing decision optimises for *broker revenue*, not customer execution quality. SEC Rule 605/606 disclosures show measurable variation in execution quality across wholesalers. The 2021 GameStop episode (Robinhood's PMCC default risk forced trading restrictions) revealed how concentrated this plumbing is — a single wholesaler clearing 40%+ of a broker's volume creates structural fragility.

![Schematic of retail order flow routing: customer to broker to wholesaler (Citadel/Virtu) to exchange or internalisation, with annotated dollar flows.](../image/week44_pfof_flows.png)

#### 2.5 Latency arbitrage and the microsecond economy

Reg NMS guarantees the NBBO at the moment of execution, but the NBBO is a moving target updated by the SIP (Securities Information Processor) consolidator. The SIP runs on a fibre path with consolidation latency of roughly **350-500 microseconds** as of 2026. Direct exchange feeds (the proprietary feeds each exchange sells to HFT firms) update the same data in **~50 microseconds**. The 300-microsecond gap between SIP and direct feeds is where latency arbitrage lives.

Concrete pattern: an HFT firm sees a buy print on Nasdaq's direct feed at $50.05. The SIP-consolidated NBBO still reads $50.04 / $50.06 because the SIP hasn't propagated yet. The HFT crosses the SIP-quoted offer on every other exchange before those exchanges update — picking off orders that were stale by 200 microseconds. IEX (the "speed bump" exchange founded by the *Flash Boys* protagonists) responded with a 350-microsecond physical coil that delays inbound orders, neutralising the gap. Roughly 3-4% of US equity volume routes to IEX as of 2026; the rest of the market still runs on the speed-favours-the-fast model.

Microstructure sits in the "structural" bucket of alpha sources — a real source, almost entirely captured by the fastest co-located firms. As a retail or even mid-tier institutional trader, you cannot win this race; you can only stop bleeding to it by using limit orders, avoiding the open and close where SIP latency widens, and using brokers whose routers ping IEX and dark pools first.

#### 2.6 Slippage on size: the $1M-trade reality

For trades under ~$10,000 in liquid names, microstructure costs are roughly the half-spread (1-3 bps) plus possibly a fraction of a cent of *negative* impact (i.e. price improvement) from PFOF. Above that, slippage scales roughly with the **square root of size relative to ADV (average daily volume)**, the so-called Almgren-Chriss square-root impact model.

A back-of-envelope April-2026 calibration for liquid US equities: expected total slippage in basis points ≈ 10 × √(order size / 1% of ADV). A 1%-of-ADV order costs ~10 bps; a 4%-of-ADV order ~20 bps; a 25%-of-ADV order ~50 bps. SPY at 80M ADV absorbs $40M+ orders almost invisibly; a $1M order in a $200M-mcap small-cap with 200k ADV is 50%+ of the day's volume and will move the print 100-300 bps.

The institutional response is to break large orders into a TWAP/VWAP across hours or days. The retail equivalent is: scale into positions over multiple sessions if your ticket is more than 0.1% of the name's ADV. The interactive lets you feel this scaling first-hand.

#### 2.7 The 2010 Flash Crash and what it taught the plumbing

May 6, 2010, 2:32 PM ET: the Dow falls roughly 9% (about 1,000 points) in minutes and recovers most of it by 3:08 PM. The post-mortem identified a single $4.1B sell program in E-mini S&P futures executed by a Kansas mutual fund, run via a poorly-parametrised algo with no price floor. That program drained futures-market liquidity, triggered cross-asset HFT arbitrage selling in equities, and as realised volatility spiked, equity market makers withdrew quotes simultaneously to avoid adverse selection. With no resting bids, a thin layer of stub-quote sells (placeholder $0.0001 bids) became actual prints — Accenture traded at $0.01 and Sotheby's at $99,999.99 — for a few seconds.

The regulatory response: single-stock circuit breakers (LULD bands — Limit Up/Limit Down — that pause trading when a stock moves 5% / 10% / 20% off its 5-minute average), market-wide breakers at -7% / -13% / -20% from the prior close, and the consolidated audit trail (CAT) for forensic reconstruction. These have prevented a repeat but the *underlying* fragility — market makers withdrawing in tail volatility — is unchanged. The fat tail is what wags the system.

---

### 3. Common Misconceptions

1. **"Zero commission means zero cost."** False. PFOF + spread + slippage typically run 3-15 bps for retail equity round-trips, paid invisibly.
2. **"Market orders always fill at the displayed price."** False. They fill at whatever clears the book at that microsecond; in a 500-share order through a 100-share-deep top of book, you walk down to the next level.
3. **"Dark pools are for shady trades."** Misleading. They exist primarily to let institutions cross size without telegraphing intent to HFT. The shadiness is in how *some* operators ran them, not in the concept.
4. **"PFOF brokers give worse execution."** Mostly false for sub-1,000-share retail orders. Wholesalers actually price-improve small retail orders. PFOF gets economically harmful only at larger size or in options.
5. **"HFTs are pure parasites that add no liquidity."** Empirically false on average. HFT-provided liquidity has tightened equity spreads from ~5 cents pre-2007 to ~1 cent in liquid names. They withdraw in stress, which is the legitimate critique.
6. **"My stop-loss order protects me against gaps."** False. A stop becomes a market order on trigger; a gap-down opens you at the gap. Use stop-limit (with the cost that it may not fill).
7. **"The SIP NBBO is the real-time price."** False. SIP runs ~300 microseconds behind direct feeds. The "real" market price is the direct-feed NBBO, available only to firms paying for direct connectivity.
8. **"Big institutions get better prices than retail."** False on small size, true on large. A 100-share retail order gets midpoint; a 100,000-share institutional order pays 20-50 bps of impact.
9. **"VWAP execution is risk-free."** False. VWAP is exposed to *all* intraday market moves during the execution window; if the stock rallies 2% during a 6-hour VWAP, you bought at average +1%, not at the open.
10. **"Microstructure alpha is available to retail."** Mostly false — the structural alpha sources are arbed out by co-located HFTs. What is left for retail is *defensive* — not being the dumb counterparty.

---

### 4. Q&A Section

**Q1: Should I always use limit orders instead of market orders?**
A: Almost always yes for any order over 100 shares or in any name with a spread wider than a penny. The exception is highly liquid SPY/QQQ/AAPL-style names at mid-day where the spread is one tick and the cost of a possible non-fill is higher than the half-tick spread cost. Even then, a marketable limit (buy at the offer) is strictly safer.

**Q2: How much does PFOF actually cost me as a retail trader?**
A: On sub-1,000-share equity orders in liquid names, roughly nothing — possibly slightly negative cost (price improvement). On options, about 5-15 cents per contract relative to the best alternative. On larger equity orders (5,000+ shares), the wholesaler stops improving and the spread cost becomes real. So: small + liquid = fine; large or options = scrutinise.

**Q3: Can I trade through IEX to avoid latency arbitrage?**
A: Yes — most major brokers let you specify IEX as a routing destination, often as part of a "speed bump" or "long-term investor" routing preset. IEX accounts for ~3-4% of US equity volume and its 350-microsecond delay neutralises the SIP-vs-direct-feed gap. The cost is occasionally slower fills.

**Q4: What is the practical difference between a stop and a stop-limit on a long position?**
A: A stop becomes a market sell when triggered — you will fill, possibly at a much worse price in a gap. A stop-limit becomes a limit sell — you may not fill at all if the price gaps through the limit. Stop is for "I want out, full stop." Stop-limit is for "I want out at a defined price or I'm willing to ride it out."

**Q5: How do I size a TWAP order for retail?**
A: As a rough rule, slice anything that exceeds 0.5% of the name's ADV into 4-8 sub-orders across the trading day, leaving the open and close (highest spreads) thin. Most retail brokers don't expose true TWAP, but you can manually approximate. For S&P 500 names this only kicks in around $1M+ tickets.

**Q6: Why does my fill price differ from the price I see on the screen at click time?**
A: Three sources: (1) your screen shows the SIP NBBO with ~300 µs latency; (2) your order took 50-500 ms to reach the broker, who routed it across multiple venues; (3) within those latencies the NBBO moved. For 100 shares of a liquid name, the variance is usually a fraction of a cent. For thinner names it can be 5-50 cents.

**Q7: Are dark pools available to retail investors?**
A: Indirectly, yes — your broker's smart-order router likely pings several dark pools on your behalf before routing to a lit venue. You don't choose the pool, but execution may already happen there. Direct dark-pool access is institutional-only.

**Q8: What is the harm in market-on-close (MOC) orders?**
A: MOC orders execute at the official closing auction price, which is well-defined for liquid names but can be heavily influenced by index rebalancing flows in the last 5 minutes. For routine retail use it's fine; for sensitive entries near earnings or rebalances, prefer a marketable limit before the auction.

**Q9: How does payment for order flow interact with options?**
A: Heavily. Options PFOF is roughly 10× equity PFOF per share-equivalent because options spreads are wider, retail-options flow is more uninformed, and there are fewer competing market makers. Rule 606 reports show ~80% of retail options flow goes to ~5 wholesalers. The cost shows up as the difference between your fill and the option's NBBO midpoint, often 5-15 cents per contract.

**Q10: Did the 2010 Flash Crash actually result in retail losses?**
A: Mostly no for resting positions — the recovery within 30 minutes meant buy-and-hold positions barely budged. The losers were investors with active stop-loss orders that triggered and filled at the ridiculous prints; many of those trades were busted (cancelled by the exchanges) under the "clearly erroneous" rule, but the busts were inconsistent and some retail traders were left with locked-in losses. The lesson is barbell-shaped: never let a stop-loss order be the line between solvent and not.

**Q11: What is "internalisation"?**
A: When your broker's wholesaler executes your order against its own inventory rather than routing to an exchange. Wholesaler captures the spread; you get NBBO or slightly better; the trade prints to the tape but never touched a public order book. Roughly 30% of US equity volume is internalised in 2026.

**Q12: Is microstructure something I need to think about for buy-and-hold investing?**
A: For sub-$50k positions in liquid US equities held for years, no — costs are negligible relative to total return. For accumulation phases where you're buying $5k of a small-cap monthly, yes — bid 30 bps below NBBO with a limit order rather than market-buying. For decumulation in retirement where you're selling 6-figure tickets, definitely — break orders into multi-day TWAPs.

---

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
