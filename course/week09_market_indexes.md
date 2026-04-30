# Week 9: Market Indexes — How the Scoreboard Is Built

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every business newscast frames the day in index points. "The S&P 500 was up half a percent. The Russell 2000 was down 1%. Tech led on the Nasdaq 100." Those four or five numbers tell millions of investors how their portfolios "did" — without anyone explaining what an index actually is. An index is not a market. It is a **recipe**: which stocks to include, how much each one counts, and when to swap names in and out. Two recipes pulling from the same kitchen can produce wildly different dishes.

There are four reasons every adult investor should be index-literate.

1. **You almost certainly own one already.** Roughly $15 trillion sits in vehicles that just buy what an index tells them to buy. The S&P 500 alone has more than $11 trillion benchmarked or directly indexed to it. The fee on your 401(k) target-date fund, the ETF in your brokerage, the closet index your "active" mutual fund secretly hugs — all live or die by some index's rules. Owning an index without understanding the rules is like owning a restaurant without ever reading the menu.

2. **The recipe quietly chooses your factor exposure.** Cap-weighting tilts you toward whatever has already won. Equal-weighting tilts you toward smaller, cheaper names. Price-weighting (the Dow) tilts you toward whichever stocks happen to have a high nominal share price — a coin-flip from corporate splits decades ago. None of these are wrong, but they are not interchangeable. A 60/40 portfolio benchmarked against the wrong index can look like a hero or a clown for purely mechanical reasons.

3. **Index plumbing creates real flows.** When a stock is added to the S&P 500 or the Russell 1000, every passive fund tracking the index has to buy on a specific day. When it is removed, they have to sell. Those forced flows reliably move prices a few percent around the rebalance — and the Russell's late-June reconstitution is one of the largest scheduled trading events on earth. If you trade around index changes, this matters; if you do not, it is still useful to know that the spike on rebalance day is mechanical, not informational.

4. **The honest version of investing accepts the index.** SOUL principle #1 in this course is that genuine alpha is rare and hard to keep. The S&P 500 net of fees has beaten 80–90% of large-cap active managers over fifteen-year windows. That is not because the index is brilliant. It is because the active managers' fees and turnover compound into a headwind they cannot beat. The default move for most readers of this course is to own the index, hold the four tranches (lesson 13), and spend the saved decision-budget on tax structure (lesson 15) rather than stock picking. To do that with eyes open, you need to know what is actually in the box.

This week is the box.

---

### 2. What You Need to Know

#### 2.1 Three Weighting Schemes — One Universe, Three Different Indexes

The single most important design choice in any index is how it weights its members. The same 30 stocks can produce three very different index series.

- **Price-weighted.** Each stock's weight is its share *price* divided by the sum of share prices. The Dow Jones Industrial Average is the only major index still built this way. A $400 stock counts ten times more than a $40 stock, even if the $40 stock is a much larger company. Splits, buybacks, and the choice of nominal share price (which is a marketing decision, not an economic one) all distort the result.

- **Cap-weighted.** Each stock's weight is its float-adjusted market cap divided by the index's total. This is the S&P 500, the Nasdaq Composite, the Russell 1000 / 2000 / 3000, the MSCI ACWI — essentially every index that runs a real fund business. The logic is sound: if NVIDIA is worth $3 trillion and a small industrial is worth $30 billion, NVIDIA represents a hundred times more of the equity-economy and should have a hundred times the weight. The cost is concentration. By April 2026, the **top 10 names in the S&P 500 sum to about 33% of the index**, and the Magnificent Seven alone are over 30%. You are not buying "500 stocks" in any meaningful sense; you are buying seven stocks plus 493 satellites.

- **Equal-weighted.** Every member gets `1/N` weight on rebalance day. The S&P 500 Equal-Weight Index (tracked by the RSP ETF) is the canonical version. Equal-weight automatically tilts toward smaller and cheaper names, since the largest names are dragged down to 0.2% and the smallest are pushed up to 0.2%. Over very long horizons it has out-earned the cap-weighted version by roughly 0–2% per year, but at the cost of more turnover, more tax drag in a taxable account, and meaningful periods of underperformance (notably 2017–2024, when mega-cap tech crushed everything else).

The cumulative-wealth chart for the cap-weighted vs equal-weighted S&P, 1928 to 2024, is in `image/week09_cap_vs_equal.png`. Both lines climb. Equal-weight ends a little higher. Neither dominates in every decade.

![Cap-weighted vs equal-weighted S&P 500](image/week09_cap_vs_equal.png)

#### 2.2 The Mag-7 Concentration Problem

In April 2026 the S&P 500's top ten weights look approximately like this:

- Apple ~6.8%
- Microsoft ~6.4%
- NVIDIA ~5.6%
- Amazon ~3.7%
- Meta ~2.7%
- Alphabet (GOOGL+GOOG) ~3.7% combined
- Berkshire Hathaway ~1.7%
- Tesla ~1.5%
- Broadcom ~1.5%

That is roughly 33% of the index in ten companies, with the Mag-7 (Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet, Tesla) at about 30%. It is the highest concentration the S&P 500 has carried since the late 1960s' "Nifty Fifty" peak. The bar chart in `image/week09_top_concentration.png` shows the shape: a steep cliff for the top 10, then 490 stocks splitting the remaining two-thirds.

![Top-10 concentration in the S&P 500](image/week09_top_concentration.png)

This is not automatically a problem. It is the index doing exactly what cap-weighting tells it to do: let winners compound. But it has three practical consequences.

1. **Your equity sleeve is a Mag-7 bet.** If you hold VOO or SPY and nothing else, roughly a third of your equity dollar is in seven tech-adjacent megacaps. The diversification narrative ("500 companies!") understates the actual factor risk.
2. **Reversals concentrate.** The 2022 drawdown was driven mainly by the same top names that drove the 2020–2021 rally; equal-weight fell less. The 2000–2002 dot-com unwind is the textbook precedent.
3. **Equal-weight is now the obvious diversifier.** Holding RSP alongside VOO does not change your sector exposure dramatically, but it does cut your top-10 concentration from ~33% to ~17%. This matters more for retirees in the spending phase (SOUL principle #13's "tranche 1") than for younger accumulators.

#### 2.3 Free-Float Adjustment — Why "Market Cap" Isn't Quite Market Cap

Every modern cap-weighted index uses the **float-adjusted** market cap, not the total market cap. Float is the count of shares actually available to public trading — total shares outstanding minus blocks held by founders, governments, parent companies, and other strategic holders.

A few examples, April 2026 estimates:

- Meta has two share classes; Class A has ~99% float, but Mark Zuckerberg's super-voting Class B is locked up. The S&P uses Class A only.
- Alphabet's GOOGL (Class A) and GOOG (Class C) trade publicly; the Class B held by founders is excluded. The two listed classes are both in the index.
- Berkshire Hathaway's float adjustment trims the index weight by a few hundred basis points relative to its total market cap, because Buffett's holdings are not deemed available.

The reason for float adjustment is liquidity, not fairness: an index that asks tracking funds to buy 100% of total shares would force them to demand stock that is not for sale. Float-weighting matches the "what can I actually buy?" question that index funds need to answer.

#### 2.4 The Russell Reconstitution — A Real Trading Day

The Russell index family (Russell 3000 / 1000 / 2000) reconstitutes once a year, on the last Friday of June. The cutoff for which company sits in which size bucket is rank order on the prior May 31, with a buffer band to limit churn. Between the buffer-day announcement (mid-June) and the Friday close, two things happen:

1. Hedge funds estimate which names will be added to the Russell 2000 and which will be promoted to the Russell 1000, and they bid those names up.
2. On the rebalance day itself, every passive Russell fund — and every "closet Russell" active fund worried about benchmark deviation — must execute the change. Single-day turnover in some affected names exceeds 30% of average daily volume.

This is the largest scheduled trading event in U.S. equities. It is also one of the cleanest examples of "irrational > solvent" (SOUL #12): the price moves are mechanical, but they can persist for weeks because shorting them costs borrow fees and mark-to-market pain. The S&P 500's quarterly rebalances and the Nasdaq 100's annual rebalance are smaller but rhyme.

#### 2.5 Survivorship Bias — What the Index Throws Away

Indexes silently drop names. A company that goes bankrupt, gets acquired, or falls below the size threshold is removed; a fresh name takes its slot. The historical index series — what you see in the chart books — is a series of *survivors plus replacements*. The dead stocks are gone.

For long-run return claims this matters more than people realise:

- The "stocks return 9–10% per year since 1928" headline already excludes the railroads that vanished in the 1930s, the conglomerates that imploded in the 1970s, and Enron, WorldCom, Lehman, GE-as-was. Their full drawdowns are in the historical record but their post-failure performance (zero) is not blended into a "what if I had bought everything in 1928" series.
- Empirical studies put the survivorship overstatement at roughly 1–2% per year for the longest-running indexes. The Damodaran dataset used in Week 3 already corrects for this on the broad-market level, which is why its returns are a little lower than the S&P-500-since-inception headline.
- For individual stock-picking decisions, the bias is much worse. A "buy what worked in 2000–2010" strategy back-tested on today's index members will look heroic, because the actual losers from that decade aren't in the test universe at all.

The practical takeaway: **always ask what got dropped**, especially when someone shows you a back-test. SOUL principle #1 again — a clean back-test is much rarer than a clean look.

#### 2.6 The Big Indexes — A Field Guide

- **S&P 500.** ~500 large-cap U.S. companies, committee-selected on profitability and float thresholds, float-adjusted cap-weighted, quarterly rebalance. Roughly 80% of U.S. investable equity by market value. Tracked by VOO (Vanguard, 0.03% expense ratio), SPY (State Street, 0.0945%), IVV (BlackRock, 0.03%). The default U.S. equity exposure.

- **S&P 500 Equal Weight.** Same 500 names, equal weights, rebalanced quarterly. RSP (Invesco, 0.20% expense ratio). About 7× the turnover of the cap-weighted version, which translates to a small but real tax drag in a taxable account.

- **Russell 2000.** The 2,000 stocks ranked roughly 1,001–3,000 by U.S. market cap. The canonical small-cap benchmark. IWM (BlackRock, 0.19%) is the main vehicle. Earnings quality is dramatically lower than the S&P 500 — a sizable share of Russell 2000 companies have negative net income — which is partly why small-cap returns have lagged large-cap since 2014.

- **Nasdaq 100.** The 100 largest non-financial Nasdaq-listed stocks, modified-cap-weighted with a re-weighting rule that caps individual names so a single stock cannot drift past ~24%. QQQ (Invesco, 0.20%). Heavily tech-tilted, but it is *not* a tech index; it is a Nasdaq-listing index.

- **Dow Jones Industrial Average.** 30 stocks, price-weighted, committee-selected. Cultural artifact more than a serious benchmark. DIA (State Street, 0.16%). Not recommended as a portfolio building block.

- **MSCI ACWI.** ~3,000 large- and mid-cap stocks across 47 developed and emerging markets, float-adjusted cap-weighted. ACWI (BlackRock, 0.32%) is the main ETF. **Caveat per SOUL principle #16:** for a Hong Kong / Mainland China reader of this course, the only investable slice of ACWI is the ~60% U.S. weight plus the developed-non-U.S. component you can hold via the ETF. Direct exposure to A-shares, mainland developers, and most EM-listed names is either capital-controlled or operationally hostile. The course's default is to overweight U.S.-listed exposure, hold ACWI as a small diversifier if at all, and not try to engineer a "global cap-weighted" portfolio that the plumbing won't actually deliver.

#### 2.7 Index Futures — The Liquid Truth

If you want to know where the index "really is" between cash-market opens, look at the front-month futures: ES (E-mini S&P 500), NQ (E-mini Nasdaq 100), RTY (E-mini Russell 2000), YM (E-mini Dow). They trade roughly 23 hours a day at tens of billions of notional. ETFs can trade away from net asset value briefly during stress; futures cannot drift far from the index without arbitrage closing the gap.

For a long-term reader, the reason to know this is not to trade futures (you almost certainly should not). It is to understand that:

- Pre-market price moves quoted on financial TV are usually the front-month future, not the index.
- During a crisis (March 2020, August 2024), the futures often print prices that the cash ETFs only catch up to at the next open. The futures are not lying — they are just open while the underlying is closed.
- For very large allocations (institutional scale), futures plus T-bills are often a cheaper way to hold S&P 500 exposure than holding SPY, because the financing rate embedded in the future is sometimes below the all-in cost of the ETF. SOUL principle #15 (tax via options/margin) sits on the same hook.

#### 2.8 Build Your Own Index — Try the Interactive

The interactive demo for this lesson, `interactive/week09_index_builder.html`, is a sandbox. It gives you 30 representative S&P 500 components with realistic prices, share counts, and trailing 12-month returns. You toggle between cap-weighted, equal-weighted, and price-weighted, and watch:

- the **composition pie** redraw (concentrated for cap, flat for equal, price-distorted for price-weighted), and
- the **12-month index return** recompute.

The point is to see, with your hands on the dials, that the same 30 underlying stocks produce three different return numbers — sometimes diverging by several percent — purely because of the recipe. That is the lesson.

---

### 3. Common Misconceptions

1. **"The Dow tells me what the market did."** The Dow is 30 names, price-weighted by an arbitrary nominal-price quirk. On any given day it can disagree with the S&P 500 by 50+ basis points for purely structural reasons. Treat it as a cultural data point, not a portfolio benchmark.

2. **"The S&P 500 is diversified across 500 stocks."** It is diversified across the *names* of 500 stocks. By April 2026 it is concentrated in the Mag-7 to the tune of ~30%, with the top 10 at ~33%. Your equity dollar is doing a lot less spreading than the headline implies.

3. **"Equal-weighting always beats cap-weighting."** Long-term yes by a small margin, but with multi-year stretches of underperformance — most recently 2017–2024 — and higher turnover. It is a different bet, not a free lunch.

4. **"Index funds are passive."** The fund is passive *to its rules*, but those rules are a committee's active choice. The S&P committee actively decides who gets added. Russell's reconstitution is mechanical but the timing creates predictable trading. There is no truly passive index — there is only "the active decisions are baked in upstream."

5. **"Adding to the S&P 500 is just paperwork."** Empirically the announcement causes a 3–8% pop in the added stock between announcement and effective date, sustained for weeks. Deletions cause a corresponding drop. This is one of the most reliably documented anomalies in equity finance.

6. **"NASDAQ = tech."** NASDAQ is a *listing exchange*. The Nasdaq 100 is heavily tech because tech companies historically chose to list there, and they have grown into the size that dominates a cap-weighted index. PepsiCo and Costco are also Nasdaq-100 names.

7. **"Survivorship bias only applies to active funds."** It applies to the indexes themselves. The 1928 S&P series silently substitutes new names for old ones; the dead names' post-failure trajectory does not appear.

8. **"MSCI ACWI gives me real global exposure."** It gives you global exposure in a backtest. Operationally, for a non-U.S.-resident investor working through a Hong Kong or Singapore broker, large parts of the EM weight are not easily, cheaply, or tax-efficiently held. SOUL #16 — only what is actually investable counts.

9. **"Float adjustment is a minor technicality."** For names with concentrated insider holdings (META, BRK, founder-led companies) it is the difference between a 4% index weight and a 1.5% index weight. It is not minor.

10. **"My active manager beats the index."** They might, in any given year. Over fifteen years, after fees, roughly one in seven large-cap active U.S. equity funds beat the S&P 500. The base rate on alpha is bad — that is SOUL principle #1, top of the list.

---

### 4. Q&A Section

**Q1. Should I own RSP instead of VOO to avoid the Mag-7 concentration?**
A. Probably not the whole sleeve. A common compromise is 70–80% VOO plus 20–30% RSP, which trims your top-10 concentration from ~33% toward ~25% without giving up the natural cap-weighted compounding. RSP also has 7× the turnover and an extra 17 bps of expense ratio. In a tax-deferred account the cost is small; in a taxable account it eats into the diversification benefit.

**Q2. Why do active managers struggle to beat the S&P 500?**
A. Three structural reasons. First, fees: average large-cap active is ~70 bps versus 3 bps for VOO, so the manager is starting 67 bps behind every year. Second, the index's cap-weighting lets winners compound automatically; managers tend to trim winners (rebalancing discipline) and reinvest in laggards, which underperforms in trending markets. Third, the index does not pay capital gains taxes; the active fund's turnover does. Compounded over fifteen years, the gap is enormous.

**Q3. What happened to "the next Apple" stocks that didn't make it?**
A. They left the index. Polaroid, Eastman Kodak, Sears, Lehman, GE (downsized out), Bear Stearns, MCI, Enron, WorldCom, Pacific Gas (in and out), AIG (in 2004, out in 2008, back later) — every one of those was once a multi-percent S&P 500 weight. Their losses are reflected in the historical series only up to the day they left. After that, the slot is taken by a fresher name and the dead one's continued zero is not in the line.

**Q4. Can I invest directly in the S&P 500 itself?**
A. No. The index is a calculation. You can buy ETFs (VOO, SPY, IVV) that hold the underlying stocks, mutual funds that track the index (VFIAX), or futures (ES) that settle to the index. All three are wrappers around the same recipe; the wrapper you choose is a fee, tax, and access decision.

**Q5. How does the S&P 500 committee decide additions?**
A. Eligibility rules — U.S. domicile, market cap above the floor (~$18 billion in April 2026), at least four consecutive quarters of GAAP profit, public float ≥ 50% — get you onto the candidate list. From there the committee picks based on sector balance and replacement need (a deletion creates the slot). The committee's discretion is the reason Tesla took years longer than expected to be added, and is the reason the Nasdaq Composite (rules-based on listing exchange) and Russell 1000 (pure market-cap ranking) move differently from the S&P at the margin.

**Q6. Why isn't the Hang Seng Index in this lesson?**
A. SOUL principle #16. For a Hong Kong / mainland reader of this course, Hang Seng exposure via 2800.HK is technically holdable, but the underlying is dominated by mainland-listed banks and developers whose accounting and political risk are categorically different from anything U.S. investors price. The course's stance is: if you live in HK, buy a small Hang Seng tracker for currency-of-spending hedging, but do not pretend it is a substitute for the U.S. index. The S&P 500 is the engine; HK exposure is hedging the gas tank.

**Q7. What is the Mag-7 weight likely to be in five years?**
A. Nobody knows, and that is the honest answer. Two historical analogies: the Nifty Fifty top weight peaked in 1972 at a similar concentration and was cut roughly in half by 1974–75; the dot-com mega-caps peaked in early 2000 and the index spent a decade rotating into other names. Both unwinds were painful. A third possibility — the one cap-weighting *bets on* — is that AI productivity gains keep these companies' earnings growth ahead of the rest of the index, in which case the concentration grows. Hold both VOO and RSP if you don't want to bet on which.

**Q8. How do I benchmark a 60/40 portfolio?**
A. The cleanest benchmark is 60% VTI (or VOO) and 40% AGG (or BND), rebalanced quarterly. You compute that benchmark's return, then compare to your actual portfolio. If you want to be more sophisticated, blend in a small International allocation (5–15% of the equity sleeve via ACWX) to match what you actually hold. Comparing a 60/40 against 100% S&P will make you feel terrible in good equity years and falsely heroic in bad ones; that is the wrong benchmark.

**Q9. Why don't professional traders just trade the Russell rebalance?**
A. They do, and the trade is well-known enough that the easy money has been arbitraged out. The remaining risk premium is for taking bidirectional inventory (you don't know exactly which names will be added until two weeks before, and you carry borrow costs to short the deletions). Hedge funds with the right infrastructure still earn a few hundred basis points a year on this — but they pay for it with risk and complexity that retail traders cannot replicate.

**Q10. What is the single most important index for me to understand?**
A. The S&P 500. It is the benchmark for ~$11 trillion of U.S. equity capital, the default in every 401(k), the comparison every active fund is judged against, and the cleanest expression of SOUL principle #1: own the index, accept the market return, and spend your scarce decision budget elsewhere — on the four tranches, on tax structure, on not panicking. Everything else in this lesson is texture around that core fact.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** What Is Actually In an Index Fund — Cap, Equal, Price Weighting Explained
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

HORACE: Welcome back. Today, week nine. Market indexes. The S&P 500. The Russell 2000. The Nasdaq 100. The Dow. MSCI ACWI. What they actually are, how they're built, and why two indexes pulling from the same kitchen can serve you very different dishes.

STELLA: I want to start with a confession, because I think most viewers will share it. I owned VOO for two years before I had a clear mental picture of what's inside it. I knew "S&P 500." I knew "big U.S. companies." I didn't know that as of this April, the top ten companies are roughly a third of the index. That changed how I think about it.

HORACE: And that's the right opening. Because the headline — five hundred companies! diversified! — quietly papers over the fact that the recipe matters more than the ingredient list. Same five hundred companies, three different weighting recipes, three different funds.

**[SECTION 1: THE THREE RECIPES — 1:30]**

STELLA: Three weighting schemes. Let's walk through them.

HORACE: Price-weighted. Each stock counts in proportion to its share price. That's the Dow. A four-hundred-dollar stock counts ten times more than a forty-dollar stock — even if the forty-dollar stock is a bigger company. Why does anyone still use this? Inertia. The Dow was built in 1896, before computers, before market-cap data was easy to compute. Adding share prices was what you could do with a pencil.

STELLA: And the share price itself is not really an economic number. A company can split its stock four-for-one tomorrow. Same company, share price drops by four. Its weight in the Dow drops by four. Nothing real has changed.

HORACE: Right. So price-weighting is a historical artifact. It's why the Dow is a cultural reference, not a serious portfolio benchmark. Treat it as financial-television flavor text.

STELLA: Cap-weighted. Each stock counts in proportion to its market value — share price times the number of shares the public can actually buy. That's the S&P 500, the Nasdaq Composite, the Russell family, MSCI ACWI. Almost every real index fund is cap-weighted.

HORACE: The logic is sound. Apple is worth three trillion dollars. A small industrial is worth thirty billion. Apple represents a hundred times more of the equity-economy. Cap-weighting says: weight it a hundred times more. Winners compound automatically. Nobody has to make a buy or sell decision.

STELLA: That's the elegance. Now the cost.

HORACE: Concentration. As of April 2026, the S&P 500's top ten names are about thirty-three percent of the index. The Mag-7 — Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet, Tesla — is about thirty percent. Equal-weight, on the other hand, says every member of the index gets one over N. Five hundred stocks, each gets two-tenths of a percent. The S&P Equal Weight, the RSP ETF, is the canonical version. Same five hundred companies, dramatically flatter recipe.

STELLA: Let's look at the concentration chart.

**[VISUAL: image/week09_top_concentration.png]**

HORACE: This is a bar chart. On the left, the top ten S&P 500 weights, April 2026. Apple six-eight, Microsoft six-four, NVIDIA five-six, Amazon three-seven, Meta two-seven, Alphabet about three-seven combined across GOOGL and GOOG, Berkshire one-seven, Tesla one-five, Broadcom one-five. Sum that up — roughly thirty-three percent.

STELLA: And then the bar on the right, "Other 490," is everything else. About sixty-seven percent of the index, split across four hundred and ninety companies.

HORACE: When somebody tells you the S&P 500 is diversified, this is what they mean. Diversified across the *names*. The actual dollar exposure is heavily concentrated. If the Mag-7 has a bad year, your VOO has a bad year, regardless of what the other 493 companies do.

STELLA: Is that bad?

HORACE: It's not automatically bad. It's the index doing exactly what cap-weighting tells it to do — let winners run. Two thousand twenty was a great year for that. So was 2023, 2024, most of 2025. The cost is asymmetric drawdowns. When the same names that drove the rally lead the decline — like late 2021 into 2022 — equal-weight falls less. We saw it. RSP outperformed VOO by about six percent in 2022.

STELLA: And the long-run picture?

**[VISUAL: image/week09_cap_vs_equal.png]**

HORACE: Cumulative return, log scale, 1928 to 2024. Cap-weighted S&P 500 in dark blue. Equal-weighted in gold. They both climb. They climb together for most of the run, with equal-weight finishing slightly higher — about a one-percent-per-year edge on the geometric average. But notice the multi-year stretches where one or the other is ahead. There's no permanent winner. There's a small long-run tilt and a lot of regime-dependent noise.

**[SECTION 2: THE MAG-7 PROBLEM — 6:30]**

STELLA: Let's go deeper on the concentration question. Because this is the live issue right now.

HORACE: The Mag-7 weight has been rising for a decade. In 2014 they were maybe twelve percent of the index combined. In 2020 about twenty-two. April 2026, around thirty. That's the highest single-cohort concentration since the Nifty Fifty peak in 1972.

STELLA: For viewers who don't know, the Nifty Fifty was the early-1970s set of "one-decision" growth stocks — IBM, Polaroid, Xerox, Coca-Cola, McDonalds. They were ferociously dominant in the cap-weighted indexes.

HORACE: And then the 1973–74 bear market cut them roughly in half over two years. Coca-Cola and McDonalds came back. Polaroid and Xerox effectively never did. The point isn't to predict the same outcome for the Mag-7 — the underlying earnings story is genuinely better, AI is real, these companies have real profitability that the Nifty Fifty leaders sometimes did not. The point is that high concentration is a recurring pattern, and high concentration unwinds are also a recurring pattern. SOUL principle one — alpha is rare. Don't bet on permanent dominance. Don't bet against it either.

STELLA: So what's the practical move for a viewer holding VOO?

HORACE: Three options. One: do nothing, accept the concentration, accept that you're underwriting a Mag-7 bet inside what feels like a diversified ETF. Two: hold VOO and RSP together, maybe seventy-thirty or eighty-twenty. That cuts your top-ten concentration roughly in half without changing your sector mix dramatically. Three: hold VOO plus a separate small-cap or international piece, which is what most target-date funds do.

STELLA: I lean option two right now, in this concentration regime. In a different regime where the top is flatter, I'd be content with just VOO.

**[SECTION 3: HOW INDEXES MAINTAIN THEMSELVES — 9:00]**

HORACE: Indexes aren't static. They have to add and drop names. There are two mechanisms. Reconstitution and rebalancing.

STELLA: Reconstitution is the big one — it's when names get added or removed. Rebalancing is just adjusting the weights of existing members.

HORACE: For the Russell family, reconstitution is once a year, the last Friday of June. They rank every U.S. stock by market cap on the prior May 31. The top thousand are the Russell 1000. Numbers 1,001 through 3,000 are the Russell 2000. There's a buffer band so a stock at exactly the cutoff doesn't oscillate every year, but otherwise it's mechanical.

STELLA: And on that Friday in June, every passive fund tracking those indexes has to execute the changes simultaneously. That creates flows.

HORACE: It is the largest scheduled trading event in U.S. equities. Single-name turnover on rebalance day can exceed thirty percent of average daily volume. Hedge funds that anticipate which names will be added or moved between size buckets bid them up in the weeks before. The added names spike. The removed names drop. Some of the move reverses in July, some persists.

STELLA: For the S&P 500 it's more case-by-case, right?

HORACE: Right. The S&P committee adds and removes names as needed — usually triggered by an existing member being acquired, or no longer meeting the rules. They announce the change about a week before the effective date. Same flow effect — the added stock pops three to eight percent between announcement and effective date, sustained.

STELLA: This is one of the most documented anomalies in equity finance.

HORACE: Documented and persistent. Which is interesting because in theory documented anomalies should arbitrage away. The reason this one doesn't fully disappear is that the forced flow is real — passive funds have to buy on a specific day at the close. Front-running it works until enough capital is doing it that the spread compresses. We're at a stable equilibrium where some premium exists, but not a free lunch.

**[SECTION 4: FREE FLOAT — 11:30]**

STELLA: Let's talk about float adjustment. This sounds technical but it matters.

HORACE: Total shares outstanding minus the shares held by founders, governments, parent companies, and other strategic holders. What's left is the float — what an index fund could actually buy.

STELLA: Why do indexes care?

HORACE: Because if they didn't, the index would tell tracking funds to buy stock that isn't for sale. Take Meta. Mark Zuckerberg's super-voting Class B shares are locked. The float is only the Class A. If the S&P weighted Meta by total cap, every passive fund would be told to buy more Meta than the public market can deliver. Float adjustment matches the recipe to what actually exists.

STELLA: And it shows up in real weights. Berkshire's float-adjusted weight is meaningfully smaller than its total-cap weight, because Buffett's holdings are excluded.

HORACE: Right. For founder-led companies — Meta, Berkshire, a lot of recent IPOs — float adjustment can cut the index weight by a third or more relative to total cap. It's not a footnote. It's the actual recipe.

**[SECTION 5: SURVIVORSHIP — 13:00]**

HORACE: One more concept before we get to the interactive. Survivorship bias.

STELLA: This one is sneaky.

HORACE: When you see a chart showing "the S&P 500 returned ten percent a year since 1928," that is a chart of survivors plus replacements. The companies that went bankrupt left the index on the day they left. The slot got a new occupant. The dead company's continued performance — usually zero — is not blended into the line.

STELLA: So the headline overstates reality by some amount.

HORACE: Empirically, one to two percent per year for the longest-running broad indexes. Damodaran's dataset, which is what we use in this course, corrects for this on the broad-market level. That's why his "stocks since 1928" returns are a hair lower than the headline.

STELLA: For individual back-tests it gets way worse.

HORACE: Way worse. If somebody shows you a back-test of "the best ten stocks of the last twenty years" — they're cherry-picking from today's surviving winners. The losers you would have actually bought aren't in the universe. The back-test always looks heroic. The lesson, as always: ask what got dropped.

**[SECTION 6: THE INTERACTIVE — 15:00]**

STELLA: Let's go to the interactive demo for this week.

**[VISUAL: interactive/week09_index_builder.html]**

HORACE: We've embedded thirty representative S&P 500 components — real names, plausible April 2026 prices, share counts, and trailing twelve-month returns. Three buttons at the top: cap-weighted, equal-weighted, price-weighted.

STELLA: I'll start in cap-weighted. The pie chart on the left shows our index composition. Apple is the biggest slice — about ten percent of our thirty-stock toy index. NVIDIA, Microsoft, the other megacaps. The bottom fifteen names together are maybe a quarter of the pie.

HORACE: Now click equal-weighted. Watch the pie redraw.

STELLA: Every slice becomes one-thirtieth. Three-and-a-third percent each. The chart looks completely different, but it's the *same thirty companies*.

HORACE: And the index return on the right changes. Because in this sample, the megacaps had a strong twelve months, the cap-weighted version returns higher. The equal-weighted version pulls in more contribution from the smaller names — some of which had a tougher year. The two numbers can differ by several percentage points.

STELLA: Now price-weighted. This is the Dow recipe.

HORACE: The biggest slice of the pie now is whichever company has the highest nominal share price. In our sample that's Berkshire, even though it's not even close to the largest market cap. Apple drops in the rankings because its share price is moderate even though its market cap is huge.

STELLA: This is the lesson. Same kitchen, three recipes, three different dishes.

**[OUTRO — 17:30]**

HORACE: The bottom line for this week. Indexes are recipes, not markets. The S&P 500 is the recipe most readers of this course should default to — it is the cleanest expression of SOUL principle one. Own the index, accept the market return, spend your decision budget on tranching and tax structure rather than stock picking.

STELLA: Layer in some equal-weight if the concentration regime worries you. Use the Russell 2000 cautiously — the small-cap quality is not what it was twenty years ago. Treat the Dow as television flavor text. Avoid the temptation to engineer a "global cap-weighted" portfolio that the plumbing won't actually deliver if you live in Hong Kong or the mainland — SOUL principle sixteen, only what's investable counts.

HORACE: Next week, week ten — bonds. What you're actually buying when you buy a Treasury, when you buy investment-grade corporate, when you buy high-yield. Why the duration is more dangerous than the credit, most of the time. See you then.

STELLA: See you.
