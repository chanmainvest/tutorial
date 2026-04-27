# Code Review

_Generated: 2026-04-27 05:14 UTC — 19 comment(s)_

---

## SOUL.md

### `@SOUL.md:L1`
> **Highlighted text:**
> # SOUL.md — Horace's (陳馬) Investment Philosophy
>
> **Overall verdict (top-of-document summary):**
>
> This is a *very* good document — coherent, opinionated in the way investment philosophy is supposed to be opinionated, and the principles genuinely interlock (#2 sets up #7 and #14; #1 sets up #13's execution note; #6/#8/#15 form a consistent options/regime/tax thesis). The voice is consistent and earned, not LLM-laundered. As a "soul" for the course it does the job — a reviewer reading it knows exactly what lens to apply when checking lessons.
>
> **The real issues to fix, in priority order:**
>
> 1. **§13 — the "ratio call spreads" passage probably mis-names the structure.** As written it's a front ratio call spread, which doesn't bet on a burst and doesn't survive a melt-up. This one's worth pulling out a payoff diagram and confirming. Most consequential single error.
> 2. **§15 — the wash-sale "synthetic equivalents" footnote needs explicit US-tax disclaimers** (or a different mechanism). This is the kind of thing that could cost a reader real money.
> 3. **§17 — calling it "Dragon Portfolio" while running ~5x less long-vol than Cole's actual prescription is a branding mismatch.** Either rename or resize. Also the "small short tail-hedge" wording probably has a typo.
>
> **Smaller things worth a pass:**
> - §2 — the 60% threshold is unsourced and the death-spiral mechanism conflates passive ownership with marginal price-setting.
> - §5 — front-running passive flows has been arbed away in equity index changes; the principle needs tempering or restricting to less-efficient corners.
> - §7 — small-cap underperformance has multiple plausible drivers, not just passive flows.
> - §14 ↔ §16 — the barbell shape (your portfolio) and the "USD-equity-default" recommendation (the reader's portfolio) need a one-line bridge so readers don't try to skip the apprenticeship.
> - §5 ↔ §15 — sector rotation as alpha source vs. tax-cost of high turnover; needs one bridge sentence.
> - §12 — the Keynes "irrational longer than solvent" attribution is technically apocryphal (Gary Shilling 1986); say so explicitly, it'll strengthen rather than weaken the principle. Also one stray use of "trader" violates your own course-wide rule.
> - Closing section — "macro = strategy / bottom-up = tactics" is a two-layer framing; the cleaner three-layer framing (macro / security selection / execution) makes your value-add clearer.
>
> **Nothing flagged is fatal.** If you fix the §13 options structure and the §15 wash-sale advice, the rest are polish that would lift a strong document to an excellent one.

### `@SOUL.md:L3-8`
> **Highlighted text:**
> This is the personal investment philosophy that grounds this course. The
> course teaches the canonical professional curriculum (CFA and others)
> because students must know what the professional world believes. But where
> the canon conflicts with the convictions below, the lesson must say so
> explicitly. These are not academic positions — they are beliefs earned
> with real money over decades of retail investing.
>
> HC: yes, please rephase
>
> **Overall framing is strong, but consider one tightening.** The intro implies SOUL.md is *only* for places the canon disagrees. In reality, several principles below (#10 hobby/religion, #4 don't day trade, #11 no passive income, #9 personal finance scope) aren't disagreements with CFA — they're stance/temperament/scope statements that happen to define the course. Maybe rephrase to: "These are the convictions that shape what gets taught, *how* it gets taught, and where the course breaks from canon." That covers all three modes (scope, voice, disagreement) instead of just disagreement.

### `@SOUL.md:L14-19`
> **Highlighted text:**
> The market is right far more often than you are — that humility is the
> starting point. Alpha does not come from being smarter than the crowd in
> general; it comes from the rare moments when the market is wrong and you
> happen to be right, and you can articulate *exactly* where the mispricing
> is and why. If you cannot point to the mispricing, you don't have an
> edge — you have an opinion.
>
> HC: no change
>
> **This is the strongest paragraph in the whole document.** "If you cannot point to the mispricing, you don't have an edge — you have an opinion" is a great hook line — quotable, memorable, true. Don't change it. (One small thing: "the rare moments when the market is wrong and you happen to be right" is slightly tautological — you could tighten to "the rare moments when the market's price differs from what the cash flows / flows / regime actually justify, *and* you can name the gap." But honestly the original reads better aloud, leave it.)

### `@SOUL.md:L52-55`
> **Highlighted text:**
> - **Loss of price discovery.** Once passive owns more than roughly 60%
>   of the float, active price-setters are no longer numerous enough to
>   absorb dislocations. Price stops being information and becomes the
>   output of fund flows.
>
> HC: wow.. you know I read Mike Green. yes, please cite it in a footnote.   yes, rephrasing it to your suggestion
>
> **The 60% threshold is doing a lot of load-bearing work and isn't sourced.** This is essentially the Mike Green / Vincent Deluard thesis, and depending on how you count (passive AUM vs. price-insensitive ownership including target-date funds, model portfolios, etc.) the number people quote ranges from ~17% (formal index funds) to >50% (price-insensitive flow). The "60% of the float" framing also conflates ownership with marginal price-setting (a passive holder who never trades isn't setting price; a 5% active flow can still discover price). Suggest either citing where 60% comes from, or rephrasing to "once price-insensitive flow dominates the marginal trade, not just the average holding." That's the actual mechanism and it's harder to dispute.

### `@SOUL.md:L56-62`
> **Highlighted text:**
> - **Death spiral on the down leg.** Passive flows are *mechanical* in
>   both directions. On the way up they bid blindly; on the way down
>   they sell blindly. Once outflows start, the selling begets more
>   outflows, which beget more selling. The same machinery that
>   manufactured the 40-year tailwind reverses with the same indifference
>   to price. Passive is, structurally, a giant momentum machine — and
>   momentum machines work both ways.
>
> HC: yes. it is about the demographic flip.  combine them.
>
> **Mechanically slightly off.** Passive funds aren't autonomous buyers/sellers — they react to *end-investor* contributions and redemptions. The buyer/seller of last resort is still a human (or model) deciding to put money in or pull it out. So the asymmetric "sell begets selling" loop only fires if the *end investor* (the 401k participant, the retiree, the algo) actually redeems. The 40-year tailwind held even through 2008/2020 drawdowns precisely because end-investor flows kept coming via payroll deduction. The reflexive death spiral is plausible but conditional on demographic/behavioral inflows reversing — which you do cover in the bullet above. Consider tying the two bullets together: the death spiral is *contingent on* the demographic flip, not an independent risk. As written they read like two separate triggers when really #1 is what arms #2.

### `@SOUL.md:L76-87`
> **Highlighted text:**
> A store of value is also supposed to be an inflation hedge, which means
> the right yardstick is the **real interest rate**, not the nominal one.
> That drags you back to the deeper question: what *is* interest? It is
> the price of time — the time value of money, the opportunity cost of
> holding wealth in any one form rather than another. Real assets (land,
> commodities, real productive businesses) anchor purchasing power because
> they generate real cash flow, but they carry business and operational
> risk that pure stores of value do not. We live in a financial-asset
> world; for most people most of the time, the real-asset choice is
> mediated through financial wrappers, with all the consensus risk that
> implies. There is no escape from belief — only choices about which
> belief to hold.
>
> HC: Ok. cut the what is interest.  
>
> **This paragraph wanders.** It does three different jobs in 12 lines: (1) real-rate-as-yardstick, (2) "what is interest? — time value of money," (3) real-assets-vs-stores-of-value-vs-financial-wrappers. Each is interesting but together they dilute the hammer-blow ending of the principle ("They are all consensus — and consensus is mortal"). Suggest cutting the "what is interest?" digression entirely (it's covered in the curriculum already) and ending the principle on the consensus-mortality line. The real-rate point can stand alone in one tight sentence: "And because every store of value is also priced as an inflation hedge, the honest yardstick is the **real** interest rate, not the nominal one — which means each of these consensuses is judged against the same monetary tide." Then drop the mic.

### `@SOUL.md:L91-99`
> **Highlighted text:**
> 4. I don't day trade. I respect those who do and make money.
> Day trading is genuinely hard. The vast majority who try lose. The small minority who consistently win have built an edge — execution speed, infrastructure, discipline, pattern recognition — that I have not built and don't intend to build. I don't dismiss them; I tip my hat. But I stay in my own lane.
>
> "Risk comes from not knowing what you're doing." — Warren Buffett
>
> _(no comment text)_

### `@SOUL.md:L113-115`
> **Highlighted text:**
> - **Front-running passive flows.** Passive funds *must* buy what is in
>   the index, mechanically, regardless of price. Knowing what they have
>   to buy and when is a cleaner edge than guessing earnings.
>
> HC: rephase into contrarian view.  like buy Uranium when it is unloved.  buy oil when it is unloved.  change the front running passive flow into something like back running the opposite of the passive flow, like the name added to index or kicked out from are misprice, so they will revert to their true value after a few quarter.  I remember I read some paper on that.  
>
> **This claim has weakened materially since ~2018 and the lesson should reflect it.** Russell index reconstitution and S&P additions used to leave large pre-announcement drift; the academic literature (Madhavan and others) showed the front-running edge has shrunk close to zero as more participants front-run the front-runners and S&P moved to pre-disclose changes earlier. The principle is still *directionally* true (mechanical buyers do exist) but listing it alongside "liquidity" and "long-term trends" overstates how durable a personal alpha source it is in 2026. Suggest tempering: "*Was* a clean edge in the 2000s–2010s; today the alpha has been mostly arbed away on equity index changes, but the principle still applies in less efficient corners (small/mid index reconstitutions, sovereign bond index changes, ESG-mandate flows)." That's more honest and still actionable.

### `@SOUL.md:L130-152`
> **Highlighted text:**
> ## 6. Technical analysis without the options vol surface is half-blind.
>
> If your technical analysis is just price and volume, you are working
> from half of the market's information. The options market is the other
> half — implied volatility, skew, term structure, and the dealer gamma
> profile tell you what the smart money is paying to hedge. Anyone who
> refuses to look at the vol surface is, by definition, analysing
> incomplete data. The conclusion may not be wrong because the chart is
> wrong — it is unreliable because it is *partial*.
>
> Two structural changes since 2020 have made this *more* important, not
> less. Zero-days-to-expiry (0DTE) options now dominate intraday flow on
> major US indices, which means much of what looks like "price action" on
> the chart is really dealer hedging of options exposure — the option
> tail wagging the equity dog. Reading a chart in the post-COVID regime
> without the corresponding option flow is reading the surface effect
> without the cause. The cost-benefit calculation is also size-dependent:
> at the portfolio scale this course is aimed at — where individual
> position outcomes meaningfully change the year, not just the month —
> the cognitive overhead of vol-surface analysis becomes cheap relative
> to the alpha it unlocks. For a beginner with their first portfolio, the
> overhead is real; for a serious retail investor with a multi-six-figure
> or seven-figure book, ignoring the vol surface stops being a small
> junk and becomes a structural blind spot.
>
> HC: emphasis on option tail wag the dog.  remove the word half, I would say IV is more important than the delta of the price itself.  that's true, not who's smart.  remove that line.  option is an lens to see what is mispriced.  the price and volume alone can't show it.  what this paragraph really trying to say is the traditional candle stick technical analysis or moving average no longer effective in the modern option heavy market.  Rewrite this paragraph along this line.
>
> **Strong principle, two small flags.** (1) "Half" is rhetorically nice but probably overstates it — option flow is one *additional* lens, not 50% of the information. Maybe "is missing the most useful complementary data set" instead of "half-blind / half of the market's information." (2) The "smart money is paying to hedge" framing is incomplete: a lot of options flow is now retail (0DTE!) and dealer-dictated, *not* smart-money positioning. The vol surface tells you about *flow and positioning*, not *who's smart*. Worth tweaking the framing — otherwise you're teaching readers to follow what may be the dumbest money on the screen, not the smartest. Suggest: "tell you what *participants in aggregate* are paying to hedge or speculate, and where dealer hedging is forced to lean."

### `@SOUL.md:L163-173`
> **Highlighted text:**
> The textbook will tell you about a "small-cap premium" — the academic
> finding that small caps outperformed large caps from the 1970s through
> the early 2000s. That premium has not worked in the last decade, and
> the reason is the same one in #2: passive index flows mechanically
> favour the largest names. The bigger the index weight, the more
> mechanical bid you receive. In a world where a majority of the float
> in major indices is held by market-cap-weighted passive vehicles, the
> small-cap edge has been arbed away by the very mechanism that created
> the large-cap melt-up. We are in a big-cap world for the foreseeable
> future, and that is a structural condition of the current monetary and
> flow regime, not a cyclical anomaly waiting to mean-revert. Until
> passive flows reverse (see #2), the centre of gravity stays where it is.
>
> HC: ok change the passive flows are one mechanical driver.  also add a line saying too many pump and dump, insider trade in the small cap space.  a lot of fishy stock.  and most of the small cap won't survive anyway.  not suitable for long term investing.
>
> **Slight overclaim on causation.** The Russell 2000 has underperformed the S&P 500 for ~15 years and there are at least four plausible drivers: (1) passive flows favouring mega-caps (your thesis), (2) tech/growth dominance + cheap capital favouring asset-light scalable businesses, (3) low rates favouring long-duration cash-flow assets disproportionately, (4) lower-quality balance sheets in the Russell 2000 (rising share of money-losing R2K constituents). Attributing it *only* to passive flow is monocausal and weakens an otherwise sharp argument. Suggest: "passive flows are *one* mechanical driver — alongside the cheap-capital era favouring scalable big-tech and a deteriorating R2K quality mix." Then your conclusion ("until passive flows reverse, centre of gravity stays") still holds without the single-cause framing.

### `@SOUL.md:L176-191`
> **Highlighted text:**
> ## 8. Every market has two readings: momentum or mean reversion. The same applies to volatility itself.
>
> In a momentum regime, what has been working keeps working — buy strength,
> sell weakness. In a mean-reversion regime, extremes snap back — fade
> strength, buy weakness. The hard part is not learning either playbook.
> The hard part is recognising the moment the regime flips. Most blow-ups
> happen when someone runs the right playbook for the wrong regime.
>
> The same regime question applies to **volatility itself: vol-on or
> vol-off**. Vol is mathematically mean-reverting — it cannot rise to
> infinity and it cannot stay at zero forever — but it can spend long
> stretches in expansion (where buying vol works and selling vol gets
> crushed) or in compression (where selling vol harvests carry and
> buying vol bleeds). Knowing which vol regime you are in is half the
> battle in any options-based trade, and recognising the flip from
> compression to expansion is what separates the option seller who
> retires comfortably from the one who blows up in a single quarter.
>
> HC: honestly, I don't know a sure win way to identify regime change.  there are many indicators, this course will teach some that I know.  keep it vague at this point, because I haven't figure out what to say in the course yet.
>
> **This is one of the cleanest principles in the document — students will *quote* the line about "running the right playbook for the wrong regime."**
>
> One missing piece worth a sentence: *how* do you actually identify the regime change? Not in detail (that's the curriculum's job) but a one-line pointer to *what to look for*: "I lean on a few cross-checks — 50/200-day MA structure for trend regime, realised-vs-implied vol spread for vol regime, term-structure shape (contango vs backwardation) for the vol turn — covered in [Week NN]." Otherwise the principle is true but operationally a bit suspended-in-air. As written, a student knows regimes exist and matter; they don't know what to look at on Monday morning.

### `@SOUL.md:L219-260`
> **Highlighted text:**
> ## 12. The market can stay irrational longer than you can stay solvent.
>
> Being right is not enough. You must also survive long enough for the
> market to come around to your view. "Right but early" is operationally
> indistinguishable from "wrong" — both end with the position closed at a
> loss. This is why position sizing, leverage, and time horizon matter
> more than the call itself. A 2x levered position that gets stopped out
> three months before the thesis plays out is a losing trade, no matter
> how vindicated the thesis looks in the rear-view mirror. Size so you can
> hold through the drawdown that has to happen before you're proven
> right — and accept that sometimes the drawdown is bigger than you can
> hold, in which case the trade was never yours to make.
>
> > "The market can stay irrational longer than you can stay solvent."
> > — John Maynard Keynes (attributed)
>
> The deeper reason markets stay irrational so long is also Keynes's:
> the **beauty contest**. In his 1936 image, professional investors are
> not picking the face they themselves think is prettiest, nor even the
> face *average opinion* thinks is prettiest — they are picking the face
> they think average opinion will think average opinion will think is
> prettiest. The market is a recursive coordination game played on top of
> a value game. Even when you have correctly identified the "true" value
> of an asset, the price will not converge there until enough other
> participants *also* identify it *and* expect each other to act on it.
> That coordination can take quarters, years, or never; it has its own
> dynamics, only loosely tethered to fundamentals.
>
> The practical consequence: knowing what something is worth is the easy
> part. The hard part is anticipating *when the crowd will know that
> others know it*, because that is the moment price actually moves.
> Until then, your "correct" thesis is just a forecast about a coordination
> event that has not happened yet — and the longer the coordination takes,
> the more your sizing, leverage, and patience are tested. The beauty
> contest is why irrationality persists; the solvency constraint is why
> that persistence eats traders who were technically right.
>
> > "It is not a case of choosing those [faces] that, to the best of one's
> > judgment, are really the prettiest, nor even those that average opinion
> > genuinely thinks the prettiest. We have reached the third degree where
> > we devote our intelligences to anticipating what average opinion expects
> > the average opinion to be." — John Maynard Keynes, *General Theory*, 1936
>
> HC: it is ok, just give to Keynes, everyone think it is Keynes' quote anyway.  Yes change the word trader to investors
>
> **One of the strongest principles — the only nit is the Keynes attribution and a small wording issue.**
>
> (1) Top quote: "The market can stay irrational longer than you can stay solvent" is *commonly* attributed to Keynes but there is **no documented source** in his published writing. It has been catalogued by Quote Investigator as apocryphal — earliest known appearance is A. Gary Shilling in 1986. Your "(attributed)" hedges it correctly but you could be sharper: "(commonly attributed to Keynes; no documented source — the phrase first appears in print under Gary Shilling in 1986, but the idea fits Keynes's beauty-contest reasoning so cleanly that the misattribution has stuck)." That actually *strengthens* the principle by showing you've done the homework, instead of just hedging with "(attributed)."
>
> (2) "Don't use the word 'trader' — this course is for retail *investors*" is in CLAUDE.md. The last line here uses "eats traders who were technically right." Worth swapping to "eats investors" or "eats holders" for consistency with your own course-wide rule.
>
> (3) The bottom Keynes quote is real and accurate (General Theory ch.12). The bracketed [faces] insertion is correct. Good.

### `@SOUL.md:L292-305`
> **Highlighted text:**
> **Execution note for phase 3:** Never short the late-bubble explorer
> tier *naked*. Borrow disappears at the worst moment, squeeze risk is
> asymmetric, and your loss is theoretically unbounded — exactly the
> wrong payoff structure for the trade you are trying to express. Use
> options. In late bubble, replace your long stock in the speculative
> tier with **long calls** — same upside, capped downside, and you have
> already paid your maximum loss as the premium. To bet on the burst
> itself, use **ratio call spreads** (long ATM call financed by short
> OTM calls) on the most stretched tier; the OTM short calls leave
> enough right-tail open to survive a final melt-up squeeze, while the
> ATM long call gives you the positive convexity you need through the
> eventual reversal. Principle #1 applies recursively here: even if you
> have correctly identified the bubble top, the wrong execution will blow
> you up before the convergence pays you.
>
> HC: change the term to front ratio call spread.  Correct.  The losses is unbounded, it will turn into naked short when the option set expire.  it is indeed my intended strategy.  combined with only use it in high IV, it is my way to short at the peak of the bubble.   It is a essentially a short position with more price and duration to allow margin of error.  ratio put won't work, because IV is too expensive at the late stage of the bubble.   It is only useful when the price go up AND IV also go up to a ridicious level.   you make it sound easier to read.
>
> **This is the most important thing in the document for me to flag — I think the structure named here doesn't do what it claims.**
>
> A "ratio call spread" of the form long 1 ATM call / short N OTM calls (N>1) is a **front ratio call spread**. Its payoff:
> - Maximum profit *at* the short strike on expiry (collected premium + intrinsic on the long).
> - Above the short strikes: losses become unbounded as the short calls dominate (you are net short calls).
> - Below the long strike: the structure expires worthless, you keep the (small) net credit/pay the small net debit. **You do not profit on a downside burst.**
>
> So this structure does **not** "bet on the burst" — it bets on the underlying drifting up to the short strike *and stopping there*, and it gets crushed on the very melt-up squeeze you say it survives. Three things look mixed up:
>
> 1. To **bet on the burst** (sharp downside), the standard tools are: long puts, bear put spreads, or — for positive convexity to a sharp drop — a **put ratio backspread** (short 1 ITM put, long 2 OTM puts; pays asymmetrically on a sharp move down).
> 2. To **monetise late-bubble IV** while staying neutral-to-bearish, you'd use call credit spreads or put credit spreads — but with defined risk, not a ratio that re-introduces unbounded upside risk.
> 3. To **stay long the bubble with capped downside** (the prior sentence about replacing stock with long calls), long calls do that — fine.
>
> I suspect the intended structure is a **put ratio backspread** on the stretched tier, not a ratio call spread. Or possibly a **call ratio backspread** if the idea is "stay long the late melt-up but get convexity on the reversal" — but that's a different trade, with positive vega and a different P&L shape.
>
> Either way, "long ATM call financed by short OTM calls" + "leaves right-tail open" + "convexity on reversal" cannot all be true of one structure. Worth re-checking with a payoff diagram before this lesson goes into the curriculum — students will reproduce this exactly and the wrong structure here is the kind of thing that blows them up.

### `@SOUL.md:L308-323`
> **Highlighted text:**
> ## 14. Barbell, not core-and-satellite.
>
> I no longer hold passive index funds as the core of my portfolio. The
> shape I run today is a **barbell**: one end is high-conviction safety
> (cash, short-duration Treasuries, gold, deep-ITM long-dated calls on
> names I genuinely want to own); the other end is asymmetric speculation
> (specific structural-alpha trades, late-cycle option positions, single
> names where I have real edge). The middle — the broad market-cap
> weighted "diversified core" — is what I have removed.
>
> The reasoning, in short: the passive "diversified core" has, by virtue
> of its own success (#2 and #7), become its own concentration risk. A
> portfolio that is 60% market-cap-weighted index is not diversified; it
> is a concentrated bet on the top ten US mega-caps and the continued
> flow of passive money into them. The barbell — actual safety on one
> side, actual edge on the other — ends up *more* diversified than the
> "diversified" core it replaces.
>
> HC: No US equity literally means US companies.  Not the board market.  The best companies are US companies.  You can't buy the best companies of the world if you ignore US companies.    Yeap.  Make SPY entry level and barbell advance level.  You need to understand the regime change thesis to have the conviction of barbell strategy.   No... I do mean LEAP and 3x leverage on 1/3 of position is safe.   Instead of losing 100% on the down side, you keep the upside but only risk 1/3 of the principle.
>
> **Strong principle but it sits in real tension with #16, and you don't reconcile it.** #16 says "the default base currency for a serious investor should be USD-denominated equity exposure." If "USD equity" = S&P 500 in practice (which it does for most retail), then the *default* recommendation in #16 is exactly the "broad market-cap weighted diversified core" that #14 says you have *removed* from your own book. So your default for the reader and your own portfolio shape diverge — which is fine, but the document should call that out explicitly. Suggest a one-line bridge in #14: "For most readers building their first portfolio, broad US equity exposure (#16) is still the right default — the barbell is what I've migrated to *after* a long period of holding the passive core, and after building the structural-alpha and option toolkit that the satellites require. Don't skip the apprenticeship to copy the shape." Otherwise you're modelling a behaviour the principles tell readers not to do yet.
>
> Separate, smaller flag: "deep-ITM long-dated calls on names I genuinely want to own" sits on the *safety* end of the barbell, but a deep-ITM LEAP is essentially leveraged equity exposure with leverage of ~2-3x and an embedded financing cost. It's not safety in the cash/Treasuries sense — it's *capital-efficient* equity. Worth distinguishing in the bullet so readers don't put 3x equity beta on the "safe" end of their barbell thinking it's defensive.

### `@SOUL.md:L326-334`
> **Highlighted text:**
> ## 15. The largest unspoken fee is tax. Use options and margin to manage it.
>
> For a successful long-only retail investor, the largest "fee" on the
> portfolio is not management fees, not commissions, not bid-ask — it is
> **capital gains tax**. A philosophy that ignores after-tax returns
> systematically overestimates the value of high-turnover strategies
> (sector rotation, momentum rebalancing) and underestimates the value of
> position-management techniques that adjust *exposure* without
> crystallising the gain.
>
> HC: yes, you have to rotate tax efficiently.  please make the change.
>
> **Tension with #5 worth acknowledging.** Principle #5 lists "sector rotation" as a top alpha source. Principle #15 says high-turnover strategies (including sector rotation) are systematically overvalued because they ignore after-tax returns. Both can be true — sector rotation is alpha-rich *and* tax-expensive — but the document doesn't square them. A reader leaves #5 thinking "rotate sectors aggressively" and #15 thinking "stop crystallising gains." Suggest one bridge sentence in #15 like: "This is also why sector rotation (#5) should be expressed through *exposure-shifting* (futures overlays, sector-pair option spreads, paired calls/puts) rather than literally selling and rebuying the underlying lots." That makes the two principles a system, not a contradiction.

### `@SOUL.md:L350-354`
> **Highlighted text:**
> - **Harvest losses with synthetic equivalents.** Sell the losing
>   position to crystallise the loss, immediately re-establish the same
>   economic exposure with a synthetic long structured to avoid the
>   wash-sale rule (jurisdiction-permitting). The loss banks against
>   realised gains; the position stays on.
>
> HC: not straight synthetic shares, but with some gap and delta positioning, so you give up a few percentage of option friction or just expose yourself to a little bit skewness risk to avoid the tax.   you are not breaking the law on paper, just sniff on the spirit of that stupid law by working around it.  you make it sound better.
>
> **Wash-sale-rule advice here is dangerously casual.** In the US, IRC §1091 covers "substantially identical" securities, and the IRS has *not* given a bright-line exemption for options on the same underlying. Deep-ITM calls and synthetic longs (long call + short put at the same strike, which is delta ~1 to the stock) are widely regarded by practitioners as substantially identical to the stock and *would* trigger wash-sale treatment if used to replace the loss-harvested position within the 30-day window. The conservative read: replacing common stock with a synthetic long on the same name within 30 days is the textbook wash-sale violation, not a workaround for it. The "(jurisdiction-permitting)" hedge isn't enough — the dominant audience for this course is HK/TW/CN-based but a real chunk will hold US-listed stocks under US tax rules. Suggest either rewriting to use *truly* different exposures (long-dated OTM call on a correlated but not identical name; sector ETF as a temporary placeholder; >30-day re-entry), or explicitly stating "consult a tax professional in your jurisdiction; the US wash-sale rule almost certainly applies to options on the same underlying." Otherwise this is a footnote that could cost a reader their loss.

### `@SOUL.md:L372-394`
> **Highlighted text:**
> The honest geographic carve-out for a retail investor based in HK / TW
> / CN reading this course:
>
> - **Hong Kong listings and mainland Chinese stocks are uninvestable for
>   me.** Capital controls, opaque accounting, regulatory whim, and the
>   absence of meaningful minority-shareholder protection have produced
>   a discount that, in my view, is not a discount at all but a fair
>   reflection of the actual risk. I do not touch them. Many of the
>   brand-name Chinese tech and consumer names will remain headlines for
>   a long time — but headlines are not investments.
> - **Taiwan is essentially TSMC.** The TWSE has one company that
>   matters to a global portfolio. If you want exposure, hold TSMC (or
>   its US-listed ADR) directly; the rest of the index is local-cycle
>   noise.
> - **The conclusion is uncomfortable but unavoidable.** You cannot
>   meaningfully diversify a developed-market equity book without
>   holding US stocks. The default base currency for a serious investor
>   using this course should be **USD-denominated equity exposure**,
>   with the local-currency book relegated to the cash-and-bills tranche.
>
> N.B. — political sensitivity flag at end is good.
>
> HC: make it clear my personal opinion that CN/HK is uninvestable.  Double down and say you can't trust communist government won't take your win away.  They don't honor private ownership.  CN/HK are uninvestable as long as they are under communist rule, it is just logical principle.  You make it sound better.  For TW, yeah, soft the tone a bit like you suggest.  TW has TSMC and a few other world class tech companies, but that's it.  everything else is irreverent.
>
> **Politically sensitive but I think substantively defensible — one suggestion on framing.** The CN/HK uninvestability claim is going to be the most contested principle in the whole document for the audience this course targets (HK/TW/CN readers). It's worth strengthening the *evidentiary* basis, not the rhetoric. Specifically: the post-2020 regulatory wave (Ant IPO pulled Nov 2020, Didi delisting 2021, ed-tech crackdown summer 2021, VIE-structure scrutiny, HSI -50% from 2021 highs vs S&P +30% over the same window) is the kind of concrete evidence that turns "my view" into "what the price action has paid you for believing." Adding two sentences of this would make this principle harder to dismiss as "Horace doesn't like China." It would also age better — if China reopens, the empirical claim is dated and falsifiable; the rhetorical claim just ages awkwardly.
>
> Also: "Taiwan is essentially TSMC" — TSMC is ~40-45% of TWSE weight as of 2026, not 100%. Worth saying "TSMC dominates the index to the point that any other holding is a rounding error to a global book" rather than "essentially TSMC." Same conclusion, more precise.

### `@SOUL.md:L396-427`
> **Highlighted text:**
> ## 17. Dragon-portfolio shape: the Fed put is real, but cheap tail hedges are still required.
>
> I run something close to the **Dragon Portfolio** framing — a mix of
> long equity, gold, trend, and a small but persistent long-volatility
> tail hedge — designed to perform across multiple macro regimes rather
> than be optimised for any single one. Two beliefs sit underneath it,
> and they are partly in tension. That tension *is* the point.
>
> 1. **The Fed put is real.** Since the late 1990s, the Federal Reserve
>    has demonstrated, repeatedly and across multiple chairs, that it
>    will intervene with monetary stimulus when financial conditions
>    tighten beyond a threshold the market eventually learns to read.
>    This is a feature of the current monetary regime, not a guess. It
>    bounds the depth (though not the duration) of equity drawdowns and
>    biases the long-equity sleeve toward "stay invested most of the
>    time."
> 2. **Tail hedges are still required.** The Fed put is *conditional*.
>    It can be late, it can be insufficient, it can be politically
>    constrained, or the regime can change (see #2). Cheap convexity —
>    small positions in long-dated OTM puts, long volatility, or option
>    structures with positive convexity to vol — is the insurance that
>    keeps you in the game when the Fed put fails or is slow. The
>    tail-hedge sleeve is small (typically a low single-digit percentage
>    of the portfolio at any time), structured to expire worthless in
>    normal markets, and structured to pay multiples of itself when
>    needed.
>
> A portfolio built only on "the Fed will save us" has no defence the
> day it doesn't. A portfolio built only on tail hedges bleeds in the
> years when the Fed put works as advertised. The Dragon shape — long
> the regime, small short tail-hedge against the regime ending — is how
> you sit with both convictions at the same time.
>
> HC:  Say I am inspired by the dragon portfolio, but add the regime thesis.  dragon portfolio runs 100 years.  I learn there are more asset classes from Chris Cole and vol is also a asset class, but I change the weight for each asset class allocation depending on the current regime.  
>
> **Two flags, one rephrasing nit.**
>
> (1) **You're calling this "Dragon Portfolio" but the allocation you describe is materially different from Chris Cole / Artemis's original.** The canonical Dragon is roughly: 24% domestic equity, 18% international equity, 21% gold, 18% trend (CTA), 19% long volatility — i.e., **long-vol is ~19% of the book, not "low single digits."** What you describe ("a small but persistent long-volatility tail hedge", "low single-digit percentage of the portfolio") is closer to a *Universa-style cheap-convexity overlay* on top of an equity-heavy book — a different beast philosophically. Either rebrand it as "Dragon-*inspired*" / "Dragon-shape with a cheaper-convexity tail" and explicitly note your long-vol is much smaller than Cole's prescription, or move the long-vol allocation up. As written, a reader who Googles "Dragon Portfolio" will get a very different picture than what you actually run.
>
> (2) **The "long the regime, small short tail-hedge against the regime ending" framing has a typo-or-thinko.** A "short tail-hedge" reads as a *short* position in tail hedges (i.e., selling vol), which would be the opposite of what the rest of the principle says. Probably meant "small *long* tail-hedge against the regime ending." Worth checking.
>
> (3) Last sentence reads better with a slight reorder: "The Dragon shape lets you sit with both convictions at the same time — long the regime that's been paying you, with a small long-vol hedge against the day the regime stops paying."

### `@SOUL.md:L429-467`
> **Highlighted text:**
> ---
>
> ## How this philosophy interacts with the course
>
> The course teaches the canonical curriculum because students must know
> what the professional world believes. But where the canon conflicts with
> the principles above, the lesson must say so explicitly:
>
> - Teach the orthodox view first, as knowledge the student is expected
>   to know.
> - Then add Horace's view, with the reasoning above.
> - If the disagreement is large enough to deserve its own treatment,
>   refer the reader to the lesson where the topic is covered in depth.
> - Never present canon as personal conviction when it isn't, and never
>   hide a disagreement to keep the lesson tidy.
>
> ### Macro and bottom-up are complementary, not competing
>
> A natural question reading the principles above: if my real edge is
> macro / structural / flow-based, why does this course teach the
> CFA-style bottom-up curriculum at all? Because the two are
> **complementary, not substitutes**:
>
> - **Macro is strategy.** It tells you *what* to buy and *what regime*
>   you are in. It tells you whether you should be long equities at all,
>   which sector deserves the overweight, whether duration is your friend
>   or your enemy, whether to hedge the dollar.
> - **CFA-style bottom-up is tactics.** It tells you *when*, *how*, and
>   *what size* to actually express the macro view in a specific
>   instrument. DCF tells you whether the price you are paying for the
>   chosen name is sane given the cash flows. Ratios tell you whether
>   you are buying near a cyclical extreme. Valuation discipline tells
>   you when to scale in and when to take profit.
>
> Macro without the tactical toolkit to express the view profitably is
> just a talking head on TV — entertaining, useless. CFA-style tactics
> without a macro strategy is stock-picking in a vacuum — diligent,
> unprofitable. A real retail investor needs both, and that is why the
> course is built the way it is.
>
> HC: right... change it to vision, strategy, tactics.  use the military theme.  is vision the level above strategy and tactics?
>
> **Excellent closing — but one terminology problem.** You map "macro = strategy" and "CFA-style bottom-up = tactics," then say bottom-up tells you "*when, how, what size*." That's slightly off. In trading parlance:
>
> - **Strategy** = the bet (long this, short that).
> - **Tactics** = the execution (when to enter, sizing, hedge, exit).
>
> DCF/ratios/valuation discipline are not really *tactics* in that sense — they're a separate analytical layer that informs *which security* to express the macro view through. The actual *execution* layer (timing, sizing, leverage, option structure) is what your principles #1, #6, #8, #12, #13, #15 collectively cover. So the cleaner mapping is three layers, not two:
>
> 1. **Macro / regime** — what direction, what asset class, what regime.
> 2. **Security selection (CFA bottom-up)** — within the chosen direction, which name, at what valuation.
> 3. **Execution (your toolkit)** — when, how, what size, what structure.
>
> That three-layer framing also makes the case for the curriculum cleaner: CFA covers layer 2 well, very poorly on layer 1, and almost not at all on layer 3 — which is exactly what your course adds. The current two-layer "complementary" framing slightly understates how much of the value-add is layer 3 (which is the more original contribution).

---
