# Review: course/week44_microstructure.md

## Overall Assessment

Week 44 is practical and valuable. It teaches one of the highest-ROI behaviours for retail investors: stop using careless market orders, understand spread and size, and avoid becoming forced liquidity during volatility events.

The lesson needs factual cleanup around market structure details, less overconfident cost estimates, and tighter alignment between the script and interactive. The most important fixes are IEX/dark-pool classification, the GameStop clearing-risk description, and the interactive ADV mismatch.

## Content Critique

- The framing is useful: zero commission does not mean zero execution cost.
- The phrase that Reg NMS has been "quietly siphoning" basis points is too one-sided. Reg NMS and fragmentation created routing complexity, but equity spreads also tightened meaningfully over the same period.
- Retail cost estimates are inconsistent. The opening says 5-30 bps round-trip; misconceptions say 3-15 bps. For small liquid US equity orders, costs can be near zero or even price-improved; for options and thin names, they can be much larger.
- Institutional cost estimates should be tied to order size as percentage of ADV, not a fixed `$1M institutional ticket` label.
- The order-type section is strong, but the default limit-order rule should be based on spread, not only share count.
- Stop-loss triggering by "last trade" depends on broker/product; bid/ask/last-trigger nuance should be added.
- IEX should not be listed as a formal dark pool. IEX is a registered exchange with a speed bump and certain hidden order types.
- Credit Suisse Crossfinder should be checked/updated given UBS acquisition and current ATS naming.
- "SEC has fined every major pool operator at least once" is too broad unless sourced.
- PFOF section needs more precise economics: price improvement for a buy order means a fill better than the offer, not simply `NBBO + 0.0002`.
- The GameStop explanation says Robinhood's "PMCC default risk" forced restrictions. This is incorrect terminology; the issue was clearinghouse/NSCC deposit and collateral requirements, not Poor Man's Covered Call risk.
- The Jane Street wholesaler reference should be verified in the retail-equity/PFOF context.
- SIP/direct-feed latency numbers need source/date labels.
- The latency-arbitrage discussion is directionally right, but should avoid implying retail can routinely choose routers that ping IEX/dark pools first unless broker controls are actually available.
- Flash Crash explanation is vivid, but should note the Waddell & Reed sell program and later spoofing/legal debate if giving a complete post-mortem.

## Cross-Reference And Consistency Issues

- Week 43 previews Week 44 as attribution, but Week 44 is market microstructure.
- Week 44 outro previews Week 45 as regulation and securities law; verify actual Week 45 before publication.
- The file repeatedly uses "retail trader" in Q&A/outro language despite repository guidance to write for retail investors.
- The script says stop-limit, never plain stops; the reading section is more nuanced and correctly notes stop-limit may not fill.

## Presentation Improvements

- Add a simple "execution cost stack" visual: spread, market impact, timing risk, fees/rebates, taxes.
- Add a table mapping order type to best use, risk, and retail example.
- Add a source box for PFOF revenue, off-exchange share, SIP latency, IEX volume, and Flash Crash facts.
- Define NBBO, midpoint, spread, and price improvement in one clean glossary-style block.
- Replace share-count rules with percentage-of-ADV and spread-based rules.
- Use `retail investor` instead of `retail trader` unless discussing actual short-term trading behaviour.

## YouTube Script Critique

The script is lively and likely watchable. The "trapdoor under the buy button" hook is good.

Specific issues:

- The script says Week 44 comes after Week 43 but Week 43 promised attribution, not microstructure.
- It repeats the PMCC/GameStop error.
- It says AAPL has 50M ADV in the interactive, but the interactive default uses 5M.
- The SPY dollar/ADV example mixes dollars and shares. A `$1M` SPY order should be compared with SPY dollar ADV, not 80M shares directly.
- The million-share market-order example and quoted 160 bps impact should be recalculated after fixing ADV assumptions.
- "Stop-limit, never plain stops" should be softened to "understand what each one fails at."
- Add a Stella question about options spreads, because retail options execution is where many students will actually lose money.

## Chart And Visual Feedback

Existing visuals are useful:

- Order book schematic.
- PFOF flow diagram.

Recommended upgrades:

- Add a before/after marketable-limit example.
- Add a stop versus stop-limit gap scenario.
- Add a PFOF economics diagram showing broker payment, price improvement, spread capture, and customer fill.
- Add a Flash Crash timeline.

## Interactive Demo Feedback

The `week44_order_lab.html` interactive is a good idea but needs numerical and UI corrections.

Issues and improvements:

- AAPL button says `50M ADV`, but `data-adv` is `5000000`, ten times smaller.
- The model uses shares rather than dollar ADV while examples often use dollar order sizes. Add price and dollar-ADV handling.
- The synthetic book is always `$50 mid`, so it does not match high-price names like SPY/AAPL unless explicitly framed as generic.
- Limit orders do not expose non-fill probability, queue position, or adverse-selection risk clearly enough.
- TWAP/VWAP reduce impact by fixed percentages but do not quantify timing risk, even though the lesson says timing risk matters.
- The order-book chart does not visibly show the order consuming levels, despite the script describing eaten levels and an impact bar.
- Add options execution mode: spread width, midpoint fills, PFOF drag per contract.
- Add open/midday/close time-of-day control.
- Add a route choice/preset: market order, marketable limit, midpoint peg, IEX, broker default.

## New Interactive Demo Ideas

- Stop-loss gap simulator.
- PFOF execution-quality comparison using Rule 605/606-style fields.
- Options spread and midpoint-fill trainer.
- Dark-pool midpoint crossing demo.
- Flash Crash liquidity withdrawal animation.

## Make It More Entertaining Without Watering It Down

The best narrative is "the same buy button, three different outcomes." Show Stella buying 1,000 shares by market order, marketable limit, and patient limit, then reveal the hidden receipt.

## Money-Making Usefulness

This is highly useful because it directly reduces avoidable trading friction. The best money-saving rules are: use marketable limits, avoid illiquid stops, size by ADV, and treat options execution as expensive.

## SOUL Consistency Flags

- Strong alignment with SOUL's structural-alpha framing: speed and routing are real alpha sources, but they are mostly captured by specialized firms.
- Needs repository wording cleanup from "retail trader" to "retail investor."
- The lesson should stress defensive execution literacy for investors, not active trading glamour.
