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
