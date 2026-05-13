# Side Lesson 23: Technical Analysis — What Works (Some), What Doesn't (Most), and the Academic Verdict

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Technical analysis is the largest cottage industry in finance. There
are tens of thousands of books, hundreds of indicators with three-letter
acronyms, dozens of YouTube channels selling pattern-recognition
courses, and a small army of CMTs (Chartered Market Technicians)
whose certification body has been around since 1973. Against all
this, the academic literature has been remarkably consistent for forty
years: **most of it doesn't work, two narrow pieces of it do.**
Side 23 is the honest survey of which is which.

1. **The "TA works" claim is mostly survivorship bias and
   pattern-fitting.** Andrew Lo, Jegadeesh, Pedersen, Bessembinder
   and others have run rigorous tests on the universe of "classical"
   chart patterns — head-and-shoulders, double tops, triangles,
   pennants, flags — and the result is consistent: after transaction
   costs, no systematic edge. The patterns are visible after the
   fact because the brain is a pattern-matching machine. They are
   not predictive in advance.
2. **But two pieces of TA *do* survive scrutiny.** Time-series
   momentum (the past 12 months of a security's own returns predicts
   the next 1-12 months) is documented in Moskowitz, Ooi and
   Pedersen 2012 across 58 markets and is the engine behind the
   $300B managed-futures industry (Week 51). The 200-day moving
   average as a risk-on / risk-off filter (Faber 2007) gives roughly
   the same long-run return as buy-and-hold but cuts the worst
   drawdowns roughly in half. These are not flashy. They are the
   exceptions, not the rule.
3. **The behavioural use is real even when the predictive use
   isn't.** A trader who says "I sell when the 50-day breaks the
   200-day" has, at minimum, a *rule* — a pre-committed binary
   trigger that overrides loss aversion (Side 15). The trigger may
   have weak predictive power, but the *discipline* is real. The
   market can stay irrational longer than you can stay
   solvent. A bad rule consistently followed beats a good thesis
   abandoned in a panic.
4. **You will see this stuff every day on financial media.** CNBC
   guests will draw trendlines on screen. X / Twitter accounts will
   post "this triangle is breaking out." YouTube channels will sell
   you a course on Elliott Wave theory for $1,997. You need to be
   able to tell the difference between the 95% that is decoration
   and the 5% that is real, especially because the decorative kind
   tends to come dressed in the language of the real kind.

This lesson covers chart-pattern claims (the failures), the two TA
strategies that replicate out-of-sample (the survivors), and the
behavioural-discipline argument for using TA-style rules even when
their predictive value is weak. The two anchors: alpha is rare, so
the default should be passive; and momentum + mean-reversion + vol-on /
vol-off are the only short-list of robust market regularities.

![Wealth-path chart: SPY $1 starting Jan 1990 through Apr 2026 under (a) buy-and-hold and (b) Faber GTAA rule — invested in SPY when SPY price is above its 200-day moving average, parked in 3-month T-bills otherwise. End wealth and max drawdown stamped on each line.](../image/side23_200dma_strategy.png)

The interactive lab on the website lets you slide the moving-average
window from 50 to 365 days and pick the risk-off asset (T-bills,
gold, or 0%-cash) and see CAGR, vol, Sharpe and max drawdown vs
buy-and-hold across the whole 1990-Apr 2026 sample.

---

### 2. What You Need to Know

#### 2.1 What Technical Analysis Actually Claims

Technical analysis is the use of past price and volume data — and
*only* past price and volume data — to predict future returns. The
underlying claims are usually some combination of:

1. Price discounts all known information (a strong-form efficient-
   markets statement, oddly enough).
2. Prices move in trends, and trends persist.
3. History repeats because human psychology is constant — the same
   patterns of fear and greed produce the same chart shapes.

The first claim is identical to what passive indexers believe and
implies you can't beat the market by *any* method. The second and
third claims are testable empirical statements. They have been
tested. The results are mixed at best.

The TA universe splits roughly into four buckets:

- **Chart patterns** — head-and-shoulders, double tops / bottoms,
  triangles, pennants, flags, cup-and-handle, wedges. Visual
  shape-based.
- **Indicators** — RSI, MACD, stochastics, Bollinger Bands, ADX,
  CCI, ATR. Mathematical transforms of price.
- **Trend / momentum rules** — moving-average crossovers, 12-month
  return ranking, Donchian channels, breakout systems. Time-series
  trend-following.
- **Esoteric** — Elliott Waves, Gann angles, Fibonacci retracements,
  candlestick patterns (doji / hammer / engulfing). Highly subjective.

The literature finds: bucket 3 has some real signal. Buckets 1, 2,
and 4 do not, after costs.

#### 2.2 The Failure: Chart Patterns and Indicators

The most rigorous chart-pattern study is Lo, Mamaysky and Wang
(*Foundations of Technical Analysis*, Journal of Finance 2000).
They wrote a *kernel-regression* algorithm to detect 10 classical
patterns (head-and-shoulders, broadening tops, triangles, etc.) on
US equities 1962-1996 — taking subjectivity out by formalising
"what counts as a pattern" mathematically. Result: a few patterns
showed weak statistical signals (head-and-shoulders had a
*non-zero* difference of conditional vs unconditional return
distributions), but the magnitudes were small and the differences
disappeared after transaction costs. Subsequent out-of-sample tests
(Bessembinder & Chan, Brock-Lakonishok-LeBaron extensions) found
the weak signals didn't replicate post-1996.

Indicators have fared no better. Park & Irwin's 2007 survey of 95
academic studies on technical trading found that 56 reported
positive results, 20 negative, 19 mixed — but the positive-result
studies were heavily weighted toward FX and commodities pre-1990
(when frictions were huge and the signal was almost certainly cost-
related), and the failure rate climbed sharply for post-1990 equity
samples. By the 2010s, the consensus view was that classical
indicators (RSI, MACD, stochastics) had no robust out-of-sample
edge in liquid US equities.

Candlestick patterns — Marshall, Young & Rose 2006, then Horton
2009 — were tested on the full Japanese-defined set across US large-
caps and showed no profits net of costs. The "doji means
indecision" claim turns out to mean roughly the same thing as
"a coin flip means indecision." It does, but it doesn't help you.

![SPY 2024 daily candlestick chart with five 'head and shoulders' patterns highlighted. Only one of the five played out as the textbook predicts; the other four broke up through the neckline rather than down. The 1-of-5 hit rate is consistent with the academic finding that classical chart patterns have no out-of-sample predictive edge.](../image/side23_pattern_failure.png)

Elliott Waves and Fibonacci retracements have effectively zero
academic support. The Elliott Wave principle requires you to
identify the current "wave count" — but the methodology allows
re-counting after any reversal, which means it cannot be falsified
in real time. The Fibonacci retracement levels (38.2%, 50%, 61.8%)
are tested in Bhattacharya & Kumar 2006 and others; result, in the
authors' words: "no statistically significant predictive content."

#### 2.3 The Survivor #1: Time-Series Momentum (Moskowitz-Ooi-Pedersen)

The first TA-adjacent finding that has replicated robustly across
markets and decades is **time-series momentum** — the observation
that *a security's own past 12-month return predicts the next 1-12
months of returns, on average, in the same direction*. Moskowitz,
Ooi and Pedersen's 2012 paper *Time Series Momentum* tested 58
liquid futures markets (equity indexes, currencies, commodities,
bonds) from 1985-2009 and found that buying assets up over the last
12 months and shorting assets down over the last 12 months produced
a Sharpe ratio of roughly 1.0-1.2 at the diversified-portfolio level
— far higher than the underlying assets in isolation.

This is the engine that drives the **managed-futures / CTA** industry
(Week 51). DBMF, KMLM, FMF, AHLT all run some flavour of time-series
trend on a diversified futures basket. The 2008 +13.1% and 2022
+20.5% returns of the SocGen CTA index were essentially the time-
series momentum signal capturing extended trends in rates, FX and
equities while everything else was selling off.

Time-series momentum is a TA strategy in the strict sense — the only
input is past prices. But it is the *opposite* of "head-and-shoulders
on a daily chart." It works on long horizons (3-12 months), across a
diversified basket (not single stocks), with explicit rules
(rank-by-12-month-return-and-rebalance-monthly), and almost certainly
captures a behavioural under-reaction to information that takes time
to be priced in. Momentum is one of the two robust market
regularities. This is where it shows up.

#### 2.4 The Survivor #2: The 200-Day Moving Average (Faber GTAA)

The second survivor is the **200-day moving average as a risk-on /
risk-off filter**, popularised by Mebane Faber's 2007 SSRN paper
*A Quantitative Approach to Tactical Asset Allocation* (the most-
downloaded paper in SSRN history at one point).

The rule:

- At month-end, check whether SPY's price is above its 10-month
  (~200-day) simple moving average.
- If yes, hold SPY.
- If no, hold 3-month T-bills.

That's it. No discretion, no filters, no overlays.

The result, on US large-caps 1990-Apr 2026 (the exact backtest in
the image script for this lesson, using ^GSPC price-only AdjClose for
the equity leg and 3-month T-bills via FRED DGS3MO when out):

- Buy-and-hold S&P 500: ~8.6% CAGR, max drawdown -57% (2009).
- Faber 200-DMA rule: ~9.0% CAGR, max drawdown -24%.
- Sharpe ratio: ~0.32 buy-hold vs ~0.52 Faber.

(Adding the ~1.8 pp/yr SP500 dividend yield brings buy-and-hold's
total-return CAGR closer to ~10.4%. The rule's CAGR rises in similar
proportion when applied to a dividend-reinvested ETF; the *gap on
max-drawdown* is what matters and is robust either way.) The CAGR is
in the same ballpark; the maximum drawdown is less than half the
size. The risk-adjusted return is meaningfully better.

This is the only piece of "technical analysis" most academics will
defend in print. It is robust across decades, across markets
(it works on EAFE and EEM too), and across reasonable parameter
choices (any MA window from 100 to 250 days gives similar results
— the result is not parameter-fitted to "200" specifically).

What it does *not* do: produce excess return in a long bull market.
From 2010-2019, buy-and-hold beat the 200-DMA rule by ~1.5 pp/yr
because the rule sat in T-bills during the August 2011, August 2015,
February 2016 and December 2018 false breaks. The rule pays for
itself in the once-or-twice-per-decade event where it cuts a -55%
into a -20%. Vol-tail-wags-dog is the framing. You're
not paying for upside; you're paying to truncate the left tail.

#### 2.5 Why It Works: The Behavioural Story

The cleanest behavioural explanation for both survivors is *under-
reaction*. New information takes time to be priced in — partly
because attention is limited (Hong & Stein 1999), partly because
disposition-effect selling caps gains early (Frazzini 2006), partly
because institutional flows are slow (rebalance lag, mandate
constraints, mutual-fund cash buffers).

When information is being slowly priced in, prices trend. A stock
that beat earnings two months ago is still being upgraded by sell-
side analysts, still being added to growth-strategy mandates, still
being chased by retail. A stock that missed earnings two months ago
is still being downgraded, dropped, sold. Time-series momentum and
the 200-DMA both ride that trend.

When the information is fully digested, prices stop trending — and
mean-reversion takes over (the *other* robust market
regularity). This is why the trend rules whipsaw in flat / choppy
markets and shine in directional ones.

The contrast with chart patterns is instructive. A "double top" is a
*shape*, not a flow. There is no behavioural story under it — no
mechanism by which the *visual symmetry* of the high produces a
predictive signal. The pattern catches the brain's eye; it does not
catch institutional capital. That is why it doesn't replicate.

#### 2.6 The Behavioural Use Case: TA as Discipline

Here is the honest case for TA even where its predictive value is
weak.

A retail investor with no rules tends to do the following:
- Buy when the stock is ripping (recency / FOMO from Side 15).
- Hold when the stock is down 30%, hoping for a bounce (loss-
  aversion / disposition).
- Sell at the bottom when the news is darkest (capitulation, cf.
  Dalbar 1.5-2 pp/yr behaviour gap).

A retail investor who follows even a *weak* technical rule —
"I sell when the 50-day breaks the 200-day, no exceptions; I buy
back when the 50-day crosses back above" — does the following:
- Sells in the early innings of major drawdowns (the rule fires in
  Aug 2008, Feb 2020, Jan 2022 — early-to-middle of each crash).
- Buys back partway through the recovery (June 2009, May 2020,
  Mar 2023).
- Has zero discretion in the moment, which is the moment when
  discretion is worst.

The technical rule may be only weakly predictive, but it is *binary
and pre-committed* — the two things that defeat behavioural bias
(Side 15 §2.5). A bad rule consistently followed beats a good
discretionary thesis abandoned at the bottom. The market
can stay irrational longer than you can stay solvent — the rule is
your insurance against your own brain when both you and the market
are tilted.

This is also why the **tactical-allocation industry** ($150B+ AUM
in 200-DMA-style rules) has staying power despite the modest CAGR
edge. Clients are buying the *behaviour insurance*, not the
return enhancement.

#### 2.7 The Honest Verdict

Putting the literature together:

| Bucket | Verdict | Notes |
|---|---|---|
| Time-series 12-mo momentum (futures basket) | **Works** | MOP 2012, Sharpe ~1.0 diversified, basis of $300B CTA industry |
| 200-DMA / 10-month MA risk-on/off | **Works (modestly)** | Faber 2007 — same return, half the max drawdown |
| Cross-sectional momentum (single stocks) | **Works (academic)** | Jegadeesh-Titman 1993; -45% crash 2009; -1 pp/yr decay since |
| Chart patterns (H&S, double tops, triangles) | **No edge** | Lo-Mamaysky-Wang 2000; replicated post-2000 |
| RSI / MACD / stochastics | **No edge** | Park-Irwin 2007 survey |
| Candlestick patterns | **No edge** | Marshall-Young-Rose 2006 |
| Elliott Waves / Gann / Fibonacci | **No evidence** | Unfalsifiable in real time |
| TA as discipline mechanism | **Real value** | Behavioural insurance — beats discretion in crisis |

If you are going to use technical analysis, use it for what works:
trend-following on diversified baskets, 200-DMA on broad indexes,
and *as a rule-set* to defeat your own behavioural biases. Skip the
patterns and the indicator soup. They are decoration.

#### 2.8 The Post-COVID Regime: Why the Vol Surface Beats the Chart at Size

One thing the rest of this lesson does not say loudly enough.
Classical technical analysis — every chart pattern, every indicator
in the textbook, the entire candlestick canon — was built in a
market where the options book was a small derivative *of* the cash
equity. That market is gone. Since roughly 2020, zero-days-to-expiry
options have come to dominate intraday flow on the major US
indices, and a meaningful share of what looks like "price action"
on a chart is really dealer hedging of options exposure pushing
the underlying around. The option tail wags the equity dog. Reading
the chart in the post-COVID regime without the corresponding option
flow is reading the surface effect without the cause, and the older
the pattern in your toolkit, the weaker its signal in the new
regime.

The implication is uncomfortable for chartists, and I say this as
someone who used to draw the lines: implied volatility, skew, term
structure, and the dealer gamma profile are now more informative
than the delta of the price itself. The vol surface tells you who
*has to do what* at which level, regardless of whether the
positioning is smart or dumb. The chart shows you the dog wagging.
The vol surface shows you why. Side 20 is the deep dive on Greeks
and the surface; this paragraph is the pointer that tells you when
to go read it.

The cost-benefit is size-dependent, and that matters because most
readers of this course are not yet at the size where the new
toolkit pays for itself. For a beginner with their first portfolio,
the cognitive overhead of vol-surface analysis is real and not
yet earning its keep — start with the chart, run the 200-DMA rule,
let the discipline do the work. For the serious retail investor
with a multi-six-figure or seven-figure book, where individual
position outcomes meaningfully change the year and not just the
month, ignoring the vol surface stops being a small handicap and
becomes a structural blind spot. Below that threshold, the chart
still earns its keep — mostly as a behavioural anchor, the
binary-and-pre-committed thing that defeats your own brain in
March 2020. Above it, the chart is the appetiser and the surface
is the main course.

---

### 3. Common Misconceptions

1. **"All technical analysis is bunk."** Not quite. Time-series
   momentum and the 200-DMA filter both replicate out-of-sample
   across decades and markets. Two narrow pieces of it work. The
   other 95% does not. The honest position is "mostly bunk, two
   exceptions" — not blanket dismissal.
2. **"Technical analysis works because everyone watches it — self-
   fulfilling prophecy."** This is the most common defence and it
   doesn't hold. If a level were truly self-fulfilling, sophisticated
   traders would front-run it, eliminating the edge. The empirical
   tests show no edge net of costs at the levels traders actually
   watch (50-day, 200-day, prior highs / lows). The story is
   appealing; the data don't confirm it.
3. **"Head-and-shoulders is reliable — I see it work all the time."**
   You see it work because of confirmation bias (Side 15). When the
   pattern works, you remember it. When it doesn't, you say "that
   wasn't a *real* head-and-shoulders." Lo-Mamaysky-Wang formalised
   pattern definition exactly to defeat this — and the edge
   disappeared.
4. **"RSI < 30 means oversold and the stock will bounce."** RSI
   tested across US equities since 1990 shows no statistically
   significant edge after costs. RSI < 30 in a downtrend tends to
   stay < 30. The "bounce" is the brain pattern-matching to a few
   high-profile cases.
5. **"Moving averages don't work because by the time the signal
   fires, the move is over."** Wrong empirically. The Faber 200-DMA
   rule fired in October 2008 (-25% from peak, before the worst
   -30% to come), in March 2020 (-15% from peak before the -34%
   bottom), and in January 2022 (-5% from peak before the -25%
   trough). The rule got out *early*, not late.
6. **"Trend-following only works in trending markets."** True, but
   trending markets are the ones where buy-and-hold has the largest
   drawdowns. The trend rule's job is exactly to capture the down-
   trends that buy-and-hold can't avoid. It will lose 1-2 pp/yr in
   choppy bull markets — that's the premium you pay for the
   left-tail insurance.
7. **"Cross-sectional momentum (Jegadeesh-Titman) is dead."** Not
   dead, but decayed. The premium has compressed since the 2003
   academic-publication date (McLean-Pontiff 2016, ~50% post-pub
   decay). The 2009 momentum crash was -45% in one quarter as
   beaten-up cyclicals snapped back. Single-stock momentum is real
   but expensive to harvest at retail (high turnover, big drawdowns,
   tax-inefficient). Time-series momentum on futures is more robust.
8. **"Volume confirms price."** Sometimes. The On-Balance-Volume
   indicator (Granville 1963) has no statistical edge in modern US
   equities. Volume *patterns* around earnings and corporate events
   carry information, but generic "volume up on green days = buy" is
   not predictive after costs.
9. **"Elliott Wave theory works if you count the waves correctly."**
   The unfalsifiability is the giveaway. Any methodology that lets
   you re-count after any move can be fitted to anything in
   hindsight. Robert Prechter (the most prominent Elliott Wave
   advocate) was in print calling for a Dow at 1,000-3,000 from the
   late 1990s through 2010s while the Dow went from 7,000 to 14,000
   to 36,000.
10. **"You can't backtest TA because the patterns are subjective."**
    Lo-Mamaysky-Wang's contribution was specifically to make the
    patterns objective via kernel regression. Once formalised, the
    patterns become testable. The tests showed no edge. Subjectivity
    is the *defence* of TA against falsification, not its strength.

---

### 4. Q&A Section

**Q1. So is technical analysis worth learning at all?**
Two pieces of it: yes. (a) Time-series momentum on a diversified
basket — read Moskowitz-Ooi-Pedersen 2012, then look at DBMF / KMLM
as the implementation (Week 51). (b) 200-day moving average as a
risk-on / risk-off filter on broad indexes — Faber 2007, the
implementation in Side 23 §2.4 above. The rest — chart patterns,
RSI / MACD soup, candlesticks, Elliott Waves — is decoration. Skip
it.

**Q2. The 200-DMA rule has slightly lower CAGR than buy-and-hold.
Why use it?**
You're not buying CAGR. You're buying a left-tail insurance. The
rule cuts max drawdown roughly in half (~-19% vs ~-55% in 2008-09).
For an investor close to retirement or one whose behaviour falls
apart at -40%, that left-tail truncation is worth the 1-1.5 pp/yr
of foregone upside. Vol-tail-wags-dog is the framing.

**Q3. Is cross-sectional momentum (long winners / short losers among
individual stocks) the same as time-series momentum?**
Related but distinct. Cross-sectional ranks stocks against each
other — buy the top decile by trailing 12-month return, short the
bottom. Time-series ranks each asset against itself — long when
its own 12-month return is positive, short when negative. The
cross-sectional version had a -45% crash in Q1-Q2 2009 (the famous
"momentum crash"), the time-series version on diversified futures
did not. Time-series is more robust for retail / smaller funds.

**Q4. Why do so many CMTs and chartists make money if the methods
don't work?**
Several reasons. (1) Some run *fundamentally* and use TA only for
entry-timing — the alpha is the fundamental call, not the chart.
(2) Some use trend rules (which work, modestly) and call it
"technical." (3) Survivorship — the ones who blew up don't have
podcasts. (4) For floor traders pre-2000, the edge was *liquidity
provision*, not pattern recognition; charts were the visible part of
a market-making operation. (5) Some are simply selling courses;
their P&L is the course revenue, not the trading.

**Q5. Should I use stop-losses based on technical levels?**
On individual stocks, sized at 2-3 ATR (average true range) below
entry, yes — they enforce position-level risk discipline. On index
funds, no — indexes mean-revert, and stops on indexes typically
get whipsawed into selling at the bottom. The right risk control
on index sleeves is *position sizing*, not stops (Side 15 §3 #6).

**Q6. Does the 200-DMA rule still work in 2026?**
Through Apr 2026 the answer is yes — the rule fired correctly out
of the Jan 2022 -25% drawdown (sat in T-bills earning 4-5%, re-
entered in Mar 2023), and through 2024-25 it stayed long. CAGR and
max-drawdown on the rule remain materially better than buy-and-hold
on max-drawdown and slightly worse on CAGR, consistent with the
historical record. The interactive lab on the website lets you
re-run the backtest and verify the numbers yourself.

**Q7. Why does the academic literature treat trend-following as
"different from TA" when it's clearly TA?**
Branding. Academics call trend-following "time-series momentum"
because the term has clean econometric definitions and the literature
runs through journals (Journal of Finance, Review of Financial
Studies). Practitioners call the same thing "trend-following" and
publish in trade journals. The mechanics — buy if rising, sell if
falling — are identical. The literature is less hostile when it's
called by its academic name.

**Q8. What about volume / OBV / accumulation-distribution
indicators?**
Volume around *event* moments (earnings, M&A, FDA approvals) is
informative — it reflects information flow. Volume on quiet days
filtered through indicator transforms (OBV, A/D line) shows no
robust predictive edge. The question to ask of any volume claim:
*what is the behavioural mechanism by which this signals price
direction?* If there isn't one, treat the claim with scepticism.

**Q9. Are chart patterns useful at all?**
Two narrow uses. (1) As a *risk-management* prompt — if a stock
breaks decisively below a multi-year support level on heavy volume,
that *is* information about institutional selling, even if the
specific "head and shoulders" framing is decoration. (2) As a
*mental shorthand* for trend and volatility regimes. Neither use
generates alpha per se — they help you not lose money in obvious
ways. The pattern-as-prediction claim is the part that doesn't
replicate.

**Q10. How does TA fit into the four-tranche framework?**
Tranches 1-3 (growth, income, stores of value) are passively
allocated and benefit from no TA whatsoever — buy-and-hold the
index funds and rebalance annually. Tranche 4 (opportunistic / 5%
slot) is where TA-style rules can earn their keep — the 200-DMA
overlay on the equity sleeve, time-series momentum exposure via DBMF
or KMLM, or rule-based entry timing on individual positions.
Confine TA to the small slice and you can't blow up the whole
portfolio with a bad chart read.

**Q11. What's the single rule a retail investor should adopt from
this lesson?**
Either none (just hold the index — default passive, alpha is rare), or
one: the 200-day moving average filter on your equity sleeve,
applied at month-end on the SP500 index price, with no
discretionary overrides. That single rule cuts max-drawdown in half
historically, costs ~1 pp/yr in foregone CAGR, and gives you a
behavioural anchor in crisis. Anything beyond that is incremental
at best, distracting at worst.

**Q12. Where does this leave Elliott Waves and the CMT certification?**
Elliott Waves: zero academic support, unfalsifiable methodology,
treat as financial astrology. The CMT (Chartered Market Technician)
designation: the *content* covers the full TA universe including
the bunk; the *credential* signals seriousness about market
microstructure but not predictive skill per se. If you're hiring a
CMT, ask them which of the four buckets in §2.1 they trade. If they
say buckets 1, 2, or 4, run.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** "Technical Analysis: What Works (Some), What Doesn't (Most) — Side 23"
**RUNTIME TARGET:** ~12 minutes
**HOSTS:** Horace, Stella

---

**[00:00 — COLD OPEN]**

**HORACE:** Stella, here's a stat. There are tens of thousands of
books on technical analysis. There are hundreds of indicators with
three-letter acronyms — RSI, MACD, ADX, CCI, ATR. There's a
certification, the CMT, that's been around since 1973.

**STELLA:** And the academic verdict on most of it is?

**HORACE:** Doesn't work. After forty years of testing, two narrow
pieces of TA replicate out of sample. The rest is decoration. We're
going to walk through which is which.

**STELLA:** Honest answer, no soft-pedalling.

**HORACE:** No soft-pedalling.

**[00:50 — INTRO]**

**HORACE:** Side 23. Technical analysis. The honest survey. We'll
cover four buckets — chart patterns, indicator soup, trend-momentum
rules, and the esoteric — and tell you which buckets the literature
actually defends.

**STELLA:** Spoiler: bucket three.

**HORACE:** Spoiler bucket three. The other three are not where the
edge lives, regardless of how loud the influencer on your timeline
is shouting "head-and-shoulders forming on QQQ."

**[02:00 — THE FAILURE: CHART PATTERNS]**

**STELLA:** Start with chart patterns. Head-and-shoulders, double
tops, triangles, flags, pennants. The classic stuff.

[VISUAL: image/side23_pattern_failure.png]

**HORACE:** This is SPY 2024. We marked five places where the chart
*looks* like a head-and-shoulders top — left shoulder, head, right
shoulder, neckline, predicted breakdown. Four of the five broke
*upward* through the neckline instead of down. One of five played
out as the textbook says.

**STELLA:** One out of five. Which is roughly what you'd get from a
coin flip after costs.

**HORACE:** Roughly. The rigorous version of this is Lo, Mamaysky
and Wang's 2000 paper *Foundations of Technical Analysis*. They
formalised pattern detection mathematically — kernel regression —
so it's not subjective. They found a few patterns had statistically
detectable signals, but the magnitudes were small, and out-of-
sample replication post-2000 wiped them out.

**STELLA:** What about the indicator soup — RSI, MACD,
stochastics?

**HORACE:** Park and Irwin 2007 surveyed 95 academic studies. The
positive results were heavily concentrated in pre-1990 commodities
and FX, when transaction costs were huge. In post-1990 liquid US
equities, the indicators have no robust edge.

**STELLA:** And candlesticks?

**HORACE:** Marshall-Young-Rose 2006 tested the full Japanese-defined
candlestick set on US large-caps. No profits net of costs. The
"doji means indecision" claim is true in the same sense that "a
coin flip means indecision" is true. Doesn't help you trade.

**[04:30 — THE SURVIVOR #1: TIME-SERIES MOMENTUM]**

**HORACE:** Now the part that *does* work. Bucket three —
time-series momentum. Moskowitz, Ooi, Pedersen 2012, *Time Series
Momentum*. They tested 58 liquid futures markets — equity indexes,
currencies, commodities, bonds — from 1985 to 2009. The rule: buy
the asset if its own past 12-month return is positive, short it if
negative.

**STELLA:** And the result?

**HORACE:** Diversified Sharpe ratio of about 1.0 to 1.2. Far
higher than the underlying assets. Replicated robustly across
decades and across the post-2009 sample.

**STELLA:** This is the engine behind the CTA industry.

**HORACE:** This is the engine. DBMF, KMLM, FMF, AHLT — all running
some flavour of time-series trend on a diversified futures basket.
2008 plus 13 percent for the SocGen CTA index when the S&P was
down 37. 2022 plus 20.5 percent when the 60-40 was down 17.

**STELLA:** Momentum and mean-reversion are the
two robust market regularities. Momentum is where it shows up.

**HORACE:** Right. Time-series momentum is *the* TA strategy that
has the cleanest academic record.

**[06:30 — THE SURVIVOR #2: 200-DAY MA]**

[VISUAL: image/side23_200dma_strategy.png]

**HORACE:** Survivor number two is the 200-day moving average rule.
Mebane Faber, 2007, *A Quantitative Approach to Tactical Asset
Allocation*. The rule is one line. At month-end, if SPY is above its
10-month — about 200-day — moving average, hold SPY. If not, hold
T-bills.

**STELLA:** That's it?

**HORACE:** That's it. No discretion. No filters. No overlays.

**STELLA:** And the 1990 to April 2026 result?

**HORACE:** Buy-and-hold S&P, eight-point-six percent CAGR price-only,
max drawdown minus fifty-seven in 2009. Faber rule, nine-point-zero
CAGR, max drawdown minus twenty-four. Sharpe ratio zero-point-three-
two buy-and-hold versus zero-point-five-two Faber. Add back the
one-point-eight points of dividend yield to both sides and the
dividend-reinvested numbers slot a couple of points higher, but the
drawdown gap is the same.

**STELLA:** Slightly lower CAGR, much lower drawdown.

**HORACE:** Slightly lower CAGR, *much* lower drawdown. Vol-tail-wags-dog. You're not buying upside; you're buying
the truncation of the left tail. For an investor close to retirement
or one whose behaviour falls apart at minus forty, that left-tail
insurance is worth the one-and-a-half points of foregone CAGR.

**STELLA:** And it's the only piece of TA most academics will defend
in print.

**HORACE:** The only piece. Robust across decades, across markets —
works on EAFE and EEM too — and across reasonable parameter choices.
Any window from 100 to 250 days gives similar results. It's not
parameter-fitted to "200" specifically.

**[09:00 — WHY IT WORKS]**

**STELLA:** What's the mechanism? Why do the survivors survive?

**HORACE:** Under-reaction. New information takes time to be priced
in. Attention is limited, sell-side analyst upgrades are slow,
mutual-fund flows are slow, retail rebalancing is slow. While the
information is being absorbed, prices trend in the direction of the
news.

**STELLA:** And once it's fully priced?

**HORACE:** Mean-reversion takes over. The
*other* robust market regularity. Which is why trend rules whipsaw
in flat markets and shine in directional ones.

**STELLA:** And chart patterns?

**HORACE:** A double top is a *shape*. There's no behavioural story
that says "the visual symmetry of a high" causes the next move
down. The pattern catches the brain's eye. It does not catch
institutional capital. That's why it doesn't replicate.

**[10:30 — THE BEHAVIOURAL USE CASE]**

**STELLA:** Even if most TA doesn't predict, you've argued elsewhere
that it has *value*.

**HORACE:** It does. As behavioural insurance. A retail investor
with no rules sells at the bottom and buys at the top — the Dalbar
gap, Side 15. A retail investor with a *bad rule consistently
followed* — say "I sell when 50-day breaks 200-day" — sells in the
early innings of major drawdowns, buys back partway through the
recovery, and crucially has *zero discretion* in the moment.

**STELLA:** The moment when discretion is worst.

**HORACE:** The moment when discretion is worst. The market can stay irrational longer than you can stay solvent.
A weak rule *is* the insurance against your own brain. The rule may
have only modest predictive power, but it is binary and pre-
committed, which is what defeats loss-aversion and FOMO.

**[11:00 — THE POST-COVID REGIME]**

**STELLA:** One thing we have not said loudly enough. Classical TA
was built before zero-days-to-expiry options dominated the tape.

**HORACE:** Right. Every chart pattern in the textbook, every
indicator, the entire candlestick canon — all of it was built when
the options book was a small derivative of the cash equity. Since
roughly 2020, that has flipped. A meaningful share of intraday
"price action" on the major indices is dealer hedging of options
exposure pushing the underlying around. The option tail wags the
equity dog. Reading the chart in this regime without the option
flow is reading the surface effect without the cause.

**STELLA:** And the implication?

**HORACE:** Implied volatility, skew, term structure, dealer gamma
— the vol surface — is now more informative than the delta of the
price itself. The chart shows you the dog wagging. The surface
shows you *why* it is wagging. Side 20 is the deep dive.

**STELLA:** Is that for everybody?

**HORACE:** No, and this is the honest part. The cost-benefit is
size-dependent. For a beginner with their first portfolio, the
cognitive overhead of vol-surface analysis is real and not yet
earning its keep. Start with the chart, run the 200-DMA, let the
discipline do the work. For the retail investor with a
multi-six-figure or seven-figure book, where one position can move
the year and not just the month, ignoring the surface stops being
a small handicap and becomes a structural blind spot. Below the
threshold the chart earns its keep, mostly as a behavioural
anchor. Above it the chart is the appetiser and the surface is the
main course.

**[VISUAL: course/interactive/side23_ma_lab.html]**

**STELLA:** And we have a lab on the site where you can play with
this. Slide the moving-average window from 50 to 365 days. Pick the
risk-off asset — T-bills, gold, or zero-percent cash. See the CAGR,
volatility, Sharpe, and max drawdown side-by-side with buy-and-
hold across the full 1990 to 2024 sample.

**HORACE:** Try the 200-day default first. Then push it to 50 — too
short, lots of whipsaws. Push it to 350 — too long, slow to react,
larger drawdowns. The 150-to-250 range is the sweet spot, which is
why the literature converged on roughly the 200.

**[11:30 — OUTRO]**

**STELLA:** So what should a retail investor do with all this,
Horace?

**HORACE:** One of two things. Option one — do nothing. Just hold
the index. The default is passive, alpha is rare.
Option two — adopt one rule, the 200-day MA filter on your equity
sleeve, applied at month-end with no discretionary overrides.
Cuts max-drawdown roughly in half historically, costs about one
point per year in CAGR, gives you a behavioural anchor in crisis.

**STELLA:** And anything beyond that?

**HORACE:** Skip it. Time-series momentum if you want exposure, buy
DBMF or KMLM and let them run it on a diversified basket — that's
Week 51. Skip the chart patterns, the indicator soup, the candle-
sticks, the Elliott Waves. They are decoration. The two narrow
pieces that work are the only pieces you need.

**STELLA:** Two pieces work. Most of the rest is decoration.
Honest answer.

**HORACE:** Honest answer.

[END]
