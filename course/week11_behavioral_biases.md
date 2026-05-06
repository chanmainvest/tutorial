# Week 11: Behavioral Biases — Why Your Brain Can't Run the Strategy Your Spreadsheet Recommends

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Every portfolio in this course is two things at once: the *strategy*
written down in the spreadsheet, and the *behaviour* of the human
who has to hold it through a 35% drawdown, a screaming headline, and
a brother-in-law who just tripled his money in a meme stock. Most of
investing's documented underperformance does not come from picking
the wrong fund. It comes from the gap between what the spreadsheet
recommends and what the human actually does.

You need to understand behavioural biases for four reasons.

1. **The Dalbar gap is real, and it is measured in *your* dollars.**
   The DALBAR QAIB studies have followed actual cash flows in and out
   of US equity mutual funds for thirty years. The headline finding,
   replicated every year, is that the *average equity-fund investor*
   earns roughly 2 to 4 percentage points per year less than the
   *fund itself*. The fund didn't underperform. The investor did, by
   buying after rallies and selling after drawdowns. Compounded over
   thirty years, that gap eats *more than half* the terminal wealth.
   The strategy was fine. The hand on the keyboard was not.

2. **Markets stay irrational longer than retail can stay liquid.**
   The classic Keynes warning: even when you
   are *correctly* identifying a mispricing, the price can move
   *further* against you for *longer* than you can finance the
   position. Behavioural biases are the mechanism that *creates*
   those long irrational stretches — it is the herd's loss aversion
   and FOMO that drives a bubble for an extra two years past where
   the spreadsheet said it should have ended. If you don't understand
   herd behaviour, you don't understand why the trade you got right
   on Day 1 still blew you up by Day 500.

3. **Fat tails punish leverage, and leverage is what overconfidence
   builds.** The volatility tail wags the
   portfolio dog. Overconfident investors take more leverage than
   their conviction warrants, because the bell-curve model in their
   head puts the next −30% year at "once in a century." It isn't.
   Pre-2008 leverage was a textbook overconfidence-meets-fat-tail
   pairing, and individual investors are running the same trade
   today, just with smaller decimal points.

4. **Knowing about a bias does not eliminate it.** This is the most
   important paragraph in the lesson. Reading about loss aversion
   does *not* make you immune to loss aversion. Even Kahneman, who
   won the Nobel Prize for naming it, said in interviews that he
   still feels the asymmetry as strongly as he did at twenty. The
   bias is wired in. The only durable fix is *system design* —
   automate the contributions, automate the rebalance, *remove the
   discretion*, and accept that on the days you most want to override
   the system, the system is most right and you are most wrong.

This lesson covers loss aversion, recency bias, anchoring, herding
and FOMO, the disposition effect, narrative fallacy, and
overconfidence — the seven behaviours that, between them, account
for nearly all of the Dalbar gap. Then it shows you the systems
that work *because* they take the decision out of your hands.

---

### 2. What You Need to Know

#### 2.1 The Dalbar Gap — How Much Behaviour Costs

The DALBAR Quantitative Analysis of Investor Behavior (QAIB) study
compares two return series: the *time-weighted return* of the
average US equity mutual fund (what the fund actually delivered) and
the *dollar-weighted return* of the average investor in those funds
(what the investor actually earned, given the timing of their
contributions and redemptions). The gap between them is pure
behaviour.

![Bar chart comparing the average S&P 500 / equity-fund return to the average equity-fund-investor return over three time horizons ending December 2024 (10-year, 20-year, 30-year). The fund bar is taller than the investor bar in every window, with the gap shaded; the gap averages around 3 to 4 percentage points per year. Source: DALBAR QAIB long-run figures; representative values used for teaching.](image/week11_dalbar_gap.png)

The gap is not random fees or fund-selection. Two-thirds of it is
*sequence-of-flows*: investors put more money in *after* the market
has run, and they pull money out *after* it has fallen. The remaining
third is fund-shifting (jumping from the year's loser to the year's
winner) and panic exits. Compounded over a thirty-year career at
3.5% per year, the behavioural drag turns a 10x wealth multiple into
roughly a 4x one. **The single most expensive financial mistake the
typical retail investor makes is not which fund they pick — it is
when they buy and sell.**

#### 2.2 Loss Aversion — The 2.5x Asymmetry

The foundational bias, named by Daniel Kahneman and Amos Tversky in
their 1979 prospect-theory paper. The pain of losing $100 is roughly
**2 to 2.5x as intense** as the pleasure of gaining $100. Their value
function looks like this:

![Schematic Kahneman-Tversky value function. Horizontal axis: dollar gain or loss from a reference point, ranging from -100 to +100. Vertical axis: perceived utility (psychological value). The gain side is concave (diminishing pleasure as gains grow). The loss side is convex AND steeper, with a slope coefficient of about 2.5: a $50 loss feels worse than a $100 gain feels good. The kink at zero is sharp, not smooth.](image/week11_loss_aversion.png)

Three consequences for portfolio behaviour:

- **Holding losers, selling winners.** Closing a losing position
  *realises* the loss — converts a paper pain into a confirmed one
  — and the asymmetry makes that conversion feel intolerable. So
  you hold. Closing a winning position *realises* the gain, and
  that conversion feels good, so you do it too quickly. The
  combined effect is a portfolio that systematically over-weights
  the names that have already proved they were the wrong call.
  This is the **disposition effect**, and it is the single most
  documented behavioural pattern in retail brokerage records.
- **Aversion to drawdowns at the *strategy* level.** A 60/40 portfolio
  that loses 22% in one year (2022) feels *worse than twice* as bad
  as one that loses 11% in two consecutive years (the actual
  cumulative is similar). The temporal compression of the loss
  amplifies the pain, even when the dollars are identical. This
  is why one bad year *changes long-term allocations* far more
  than a slow grinding decade does.
- **The wrong volatility check.** Loss aversion makes investors
  check their portfolio more often during drawdowns than during
  rallies. The more you check during a drawdown, the more the
  asymmetric pain accumulates, the more likely you are to capitulate
  at the bottom. The brokerage app's red number is a behavioural
  weapon pointed at your own wealth.

#### 2.3 Recency Bias — The Last Year Predicts Forever

Recency bias is the tendency to extrapolate the most recent
experience as the new permanent state. When stocks have just
returned 25% for two years running, your brain quietly resets the
expected-return prior to "stocks return 25%." When they've been
flat for three years, the prior resets to "the era of stock returns
is over." The actual long-run distribution does neither.

This is why the worst time to *raise* your equity allocation is
after a great equity decade — the regime that produced those returns
is already priced into current valuations, and your forward expected
return is *lower*, not higher. And the worst time to *cut* equity is
after a 30% drawdown — the forward expected return after the
drawdown is *higher*, because prices fell faster than fundamentals.
Recency bias has the wrong sign in both cases. Every time.

The 1999 retail allocation to internet stocks was peak recency bias.
The 2009 retail flight to cash was peak recency bias. The 2021 retail
allocation to crypto and meme stocks was peak recency bias. The
pattern repeats because the wiring repeats.

#### 2.4 Anchoring — Why Your Cost Basis Should Not Exist on Your Screen

Anchoring is the brain's tendency to over-weight the first number it
encountered as a reference point. In investing, the anchor is almost
always your *cost basis* — the price you paid. Cost basis is
relevant for *tax* purposes. It is irrelevant for *should I hold
this* purposes.

The honest framework is the **inheritance test**: if you inherited
this position today at the *current* market price, with no cost
basis attached, would you choose to hold it? If yes, the anchor is
noise. If no, you are only holding because of the anchor — and the
anchor is a bookkeeping artefact, not a piece of investment thesis.

Other anchors that infect retail portfolios: the 52-week high
("it was 30% higher last year, so it must come back"); the IPO
price ("it must be worth at least the IPO price"); a round number
($100, $1,000); a friend's cost basis. None of these have any
information content about the *current* fair value. All of them
distort your hold/sell decision.

#### 2.5 Herding and FOMO — The Beauty Contest

Keynes' beauty-contest analogy is the cleanest
description of herding ever written: the investing game is not
picking the prettiest face, it is picking the face *the average
voter* will pick — and the average voter is in turn picking what
*they* expect the average voter to pick, all the way down. The
*correctness* of the underlying valuation is many layers removed
from the proximate driver of price.

Herding has two flavours and they reinforce each other:

- **FOMO (fear of missing out).** Watching neighbours, coworkers,
  and Twitter accounts get rich on a trade you didn't take. The
  behavioural pressure builds asymmetrically: a 50% rally in a
  position you don't own hurts more than a 50% rally in a position
  you do. The rational response is to ignore other people's
  outcomes; the behavioural response is to chase, often near the
  top, for fear of being the only one left out.
- **Capitulation.** The mirror image: when everyone else is
  selling, the social proof of mass exit overrides any analytical
  view that the sell-off is overdone. The 2008 March bottom and
  the 2020 March bottom both saw record retail redemptions; both
  were near-perfect bottoms. The herd was wrong, the herd was
  loud, and following the herd cost you the recovery.

The reason herding behaviour creates the long irrational stretches
that bankrupt good traders is exactly the beauty-contest mechanism:
even *correct* contrarians can be early by years, and being right
on Day 1 doesn't help if you can't finance the position to Day 500.

#### 2.6 Narrative Fallacy and Overconfidence

Two related biases that compound each other.

**Narrative fallacy** — the brain's preference for a clean causal
story over a noisy statistical one. Every 1% market move on the
news is paired with a confidently-stated reason. *"Stocks rose on
strong earnings."* *"Stocks fell on rate fears."* These narratives
are post-hoc fits to noise. The actual driver of any given day's
move is rarely a single clean reason; usually it is the chaotic
sum of millions of independent decisions, some on data, some on
flows, some on liquidity, most on nothing in particular. Treating
the day's narrative as causally informative builds a false picture
of how markets work.

**Overconfidence** — the tendency to over-estimate one's own
prediction precision. The classic finding: when investors say they
are 90% sure of a forecast, they are right 70% of the time.
Combined with narrative fallacy, this builds a portfolio of high
conviction in stories that are mostly noise. Two specific manifestations:

1. **Excessive trading.** Barber and Odean's work on retail
   brokerage records found that the highest-turnover quintile
   underperformed the lowest by roughly 6 percentage points per
   year. Every trade is an act of confidence; over-confidence
   manifests as over-trading.
2. **Under-diversification.** "I know what I own" becomes a license
   to hold ten names instead of five hundred. The ten names carry
   the same expected return as the index but vastly more
   idiosyncratic risk — the textbook free-lunch *anti*-portfolio.

#### 2.7 Why Knowing Doesn't Cure — System Design Beats Willpower

This is the part of the lesson that survives the rest. The biases
are not solved by being smarter. They are solved by *taking the
decision out of your hands at the moments your hands are worst*.

Concrete system designs:

- **Automatic monthly contributions** that bypass the brain. The
  decision to invest was made once, when you set up the transfer.
  The behavioural decision *not* to invest after a 30% drawdown
  never gets made because there is no decision to make.
- **Rules-based rebalancing** on a fixed calendar (annually or
  semi-annually). Drift back to target. No view-based timing. The
  rebalance trade mechanically buys the loser and sells the
  winner — the *opposite* of the recency-bias trade you'd make
  by hand.
- **Long horizons announced in advance.** "I will not look at this
  account for thirty years" is a behavioural commitment device,
  not an investment thesis. The strategy is the same; the
  behavioural drag falls because you have removed the surveillance
  that activates loss aversion.
- **Position-sizing rules instead of conviction-sizing.** A
  maximum-2%-per-name rule, applied mechanically, removes the
  overconfidence channel by which "I really like this one" turns
  into a 30% portfolio bet that blows up.
- **A written investment policy statement** that pre-commits how
  you will respond to common scenarios (a 20% drawdown, a 50%
  rally, a job loss, an inheritance). Pre-committed responses
  beat in-the-moment responses because the in-the-moment brain is
  the System-1 brain Kahneman warned about.

The interactive panel at the bottom of this lesson lets you toggle
on and off four classic bias-driven actions ("sell after a 20%
drawdown", "buy after a 20% rally", "switch to bonds after two
down years", "chase last year's winner") and watch what they do to
a 1928–2024 backtest against simple buy-and-hold. The pattern in
every combination is the same: the bias-driven version
underperforms, by roughly the Dalbar-gap-size or worse, in nearly
every parameter combination. Behaviour is the most expensive line
item in the portfolio.

---

### 3. Common Misconceptions

**Misconception 1: "I'm a rational investor; biases are for amateurs."**

The biases are wired. They affect Nobel laureates, professional
traders, and institutional allocators just as they affect retail.
The professional difference isn't immunity — it's *system design
that constrains* the bias. If you don't have such systems, you have
the biases at full strength.

**Misconception 2: "Loss aversion is just risk aversion."**

It is not. Risk aversion is a smooth preference for less variance
at a given expected return. Loss aversion is a *kink* at zero — a
discontinuity where losses are weighted ~2.5x as heavily as
equivalent gains. The kink causes path-dependent behaviour (the
disposition effect) that pure risk aversion does not predict.

**Misconception 3: "If I check my portfolio more often I'll catch
problems sooner."**

The opposite. Checking more often *amplifies* loss aversion, because
you experience more individual loss events (every red day) without
gaining much new information. The optimum frequency for a long-term
portfolio is roughly *once a year for a rebalance*. More often is
behavioural exposure, not improved decision-making.

**Misconception 4: "I held through 2008/2020/2022, so I won't
panic-sell next time."**

Survivorship of past drawdowns is a weak predictor. The next
drawdown will have a different cause, a different narrative, a
different speed, and you will be at a different stage of life with
a different account size. Past discipline is comforting but the
correct prior is "I will face the same temptation again."

**Misconception 5: "The Dalbar gap is just fees."**

It is not. The fund-level returns DALBAR cites are *net* of fund
fees. The gap between fund and investor is purely the timing of
flows. Eliminating fees does not close it.

**Misconception 6: "If I read more news, I'll be better-informed."**

Almost the opposite. More news exposes you to more narrative
fallacy, more recency bias (the headlines are by definition
"what just happened"), and more herding signals. The best
portfolios in the long-run sample are run by people who don't
follow market news daily.

**Misconception 7: "FOMO can be controlled with willpower."**

FOMO is a social-comparison loop, and the loop is now in a phone
in your pocket. Willpower lasts minutes; the loop runs years.
The structural fix is to mute, unfollow, and set portfolio rules
that don't require you to react to what your network is doing.

**Misconception 8: "If I diversify enough, behaviour doesn't matter."**

A perfectly diversified portfolio still has full equity-market
volatility (~16-20% σ), which means a 30% drawdown is roughly
once-per-decade. Diversification limits idiosyncratic risk; it
does not remove the behavioural temptation to sell during a
systematic drawdown.

---

### 4. Q&A

**Q1: Is overconfidence really worse for men than women?**

A: Yes — Barber and Odean's "Boys Will Be Boys" (2001) study
found men trade roughly 45% more than women, and that the extra
turnover translates into about 1.4 percentage points per year of
*lower* net return. The mechanism is overconfidence: men are more
likely to believe they have an edge, so they trade more on it.
The behavioural cost is the trade itself, not the gender.

**Q2: What's the single most useful system to install today?**

A: Automatic monthly contributions to a broad-market index ETF in
a tax-advantaged account, with a one-time annual calendar reminder
to rebalance. That single system bypasses recency bias (you don't
time entries), bypasses loss aversion at the contribution level
(no decision to make in drawdowns), and dramatically reduces FOMO
exposure (you're already invested, so you can't miss out).

**Q3: How do I design a written investment policy statement?**

A: Three sections, one page each. (1) Allocation: target weights
and rebalance rule. (2) Triggers: pre-committed responses to
specific events (drawdown of X%, allocation drift of Y%, life
event Z). (3) Forbidden actions: things you commit to *not* doing
(e.g., "I will not move >5% of the portfolio based on a single
news headline"). Sign it. Date it. Re-read it during drawdowns
*before* trading.

**Q4: How does the disposition effect interact with taxes?**

A: It compounds the damage. Holding losers and selling winners is
exactly the *opposite* of optimal tax behaviour. Tax-loss
harvesting says realise losers (use the loss against gains) and
defer winners (let them compound untaxed). The disposition effect
makes you do the inverse, costing both behavioural alpha and tax
alpha simultaneously.

**Q5: If I know a bubble is forming, should I short?**

A: No. Markets stay irrational longer than
you can stay solvent. Even if you correctly identify a bubble in
year 1, the bubble can run another 2–3 years. A short position
financed with margin will be stopped out long before the
fundamentals matter. The behavioural fix is to *avoid* bubbles
(don't add new money in), not to bet against them.

**Q6: What do I do when my brother-in-law triples his money on a
meme stock?**

A: Congratulate him sincerely. Do not change your strategy. The
sample of one is not data; the strategy you can articulate the
risk of has positive expectancy and the strategy he ran (single
name, no edge, lottery payoff distribution) does not. Survivorship
bias makes the lottery winners visible; the losers are silent.

**Q7: Is dollar-cost averaging just a behavioural trick?**

A: Largely yes. Mathematically, lump-sum investing beats DCA in
roughly 70% of historical entry windows because markets trend up.
But behaviourally, DCA reduces the *regret* of bad timing, which
makes investors more likely to actually *invest* the money rather
than hold it in cash forever. A behavioural trick that gets the
money into the market is worth more than a mathematical optimum
that leaves the money in cash.

**Q8: How does fat-tail awareness intersect with overconfidence?**

A: Directly. Vol tail wags dog. Overconfident
sizing assumes the realized volatility distribution looks like the
recent quiet sample. Fat tails mean the *next* extreme event is
larger than your sized-for sample suggested. Overconfidence-built
leverage gets crushed when the fat tail materialises. The fix is
to size for the *tail* you have not yet seen, not the *centre*
you have already lived through.

**Q9: How does this lesson connect to the barbell?**

A: The barbell (covered Week 14) is in part a
*behavioural* design: by holding extreme safety on one end (cash,
T-bills) and small concentrated speculation on the other (long
calls, asymmetric bets), the middle — where loss aversion is
loudest, where the Dalbar gap is largest — gets stripped out. You
cannot panic-sell cash; you cannot panic-sell a position that is
already at its maximum loss. The barbell removes the fuel that
behaviour burns.

**Q10: Is automation actually a substitute for understanding?**

A: It is a substitute for *willpower*, not for *understanding*.
You still need to understand the strategy well enough to set it up
correctly and to recognise the genuinely rare moments when the
system needs to be adjusted (a regime shift, a major life event,
a tax-law change). Automation is "trust the spreadsheet most of
the time"; understanding is "know which 1% of the time the
spreadsheet is wrong."

The interactive panel below lets you toggle on and off four
classic bias-driven actions and watch the resulting wealth path
versus simple buy-and-hold of the S&P 500 from 1928 to 2024. The
pattern repeats: every bias rule loses to "do nothing." The
strategy your spreadsheet recommends beats almost any version
of you that overrides it.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Behavioral Biases — Why Your Brain Can't Run the Strategy Your Spreadsheet Recommends | Week 11

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** This is the most uncomfortable lesson in the course.
The previous ten weeks we've taught you portfolios, allocations,
risk metrics, the math of diversification. Today we tell you that
none of it survives contact with your own brain unless you build
systems around the brain.

**Stella:** That sounds dramatic.

**Horace:** It's measured. The DALBAR study has tracked actual
mutual-fund cash flows for thirty years. The average equity-fund
investor underperforms the fund itself by three to four percentage
points per year. Every year. The fund is fine. The investor is
the problem.

**Stella:** And that compounds.

**Horace:** Over thirty years, that gap turns a ten-x wealth
multiple into roughly four-x. The single most expensive financial
mistake the typical retail investor makes is not which fund they
pick. It is when they buy and sell.

---

**[SEGMENT 1: THE DALBAR GAP]**

[VISUAL: image/week11_dalbar_gap.png]

**Horace:** Here it is. Three windows ending December 2024.
Ten-year, twenty-year, thirty-year. In every window, the fund
delivers more than the investor in the fund earned. Three to four
points a year, every window, every period.

**Stella:** What's causing the gap?

**Horace:** Two-thirds is sequence-of-flows. People put money in
*after* the market has run, and they pull money out *after* it
has fallen. The remaining third is fund-shifting — chasing last
year's winner — and panic exits in drawdowns. It's all behaviour.
None of it is fund quality.

---

**[SEGMENT 2: LOSS AVERSION]**

[VISUAL: image/week11_loss_aversion.png]

**Horace:** This is the foundation. Kahneman and Tversky, 1979.
The horizontal axis is dollars. The vertical axis is psychological
value — how good or bad it feels.

**Stella:** The gain side is concave.

**Horace:** Right. Diminishing marginal pleasure of gains. The
second hundred dollars feels less than the first.

**Stella:** And the loss side?

**Horace:** Convex *and* steeper. Roughly 2.5 times steeper. Losing
fifty dollars feels worse than gaining a hundred feels good. That
2.5-to-1 ratio is the engine behind the disposition effect — the
documented retail pattern of holding losers and selling winners
— and it's the engine behind capitulation at market bottoms.

**Stella:** Why?

**Horace:** Because closing a losing position *converts* paper pain
into confirmed pain, and the asymmetry makes that conversion
intolerable. So you don't close it. You hold and hope. Until the
loss gets so bad you can't hold any more, and you sell — at the
bottom.

---

**[SEGMENT 3: RECENCY AND ANCHORING]**

**Horace:** Two more biases that hand-in-hand drive most retail
mistakes.

Recency bias. Your brain treats the most recent two or three years
as the new permanent state. After a great equity decade, you raise
allocation. After a 30% drawdown, you cut. Both are wrong. Forward
expected returns are *lower* after a great decade — valuations got
expensive. Forward expected returns are *higher* after a 30%
drawdown — prices fell faster than fundamentals.

**Stella:** And anchoring?

**Horace:** The price you paid. Cost basis. Relevant for taxes,
irrelevant for hold-or-sell. The honest test is the inheritance
test. If you inherited this position today at the current price
with no cost basis attached, would you choose to hold it? If yes,
the anchor is noise. If no, you're only holding because of a
bookkeeping artefact.

---

**[SEGMENT 4: HERDING, FOMO, AND THE BEAUTY CONTEST]**

**Horace:** Keynes wrote it best. The investing game isn't picking
the prettiest face. It's picking the face the average voter will
pick — and the average voter is picking what they expect the
average voter to pick. The valuation, the underlying, the
fundamentals — those are many layers removed from the price.

**Stella:** That's why bubbles last.

**Horace:** That's exactly why. Markets stay irrational longer than
retail can stay solvent. Even if you correctly identify a bubble in
year one, the bubble runs another two or three years. Anyone who
shorted with margin is already gone before the fundamentals
matter.

**Stella:** And FOMO?

**Horace:** Fear of missing out is the modern face of herding. A
50% rally in a position you don't own hurts more than a 50% rally
in a position you do. Asymmetric. Builds pressure to chase. Almost
always near the top.

---

**[SEGMENT 5: OVERCONFIDENCE AND THE FAT TAIL]**

**Horace:** Overconfidence is the bias that makes the others
expensive. When you say you're 90% sure, you're right about 70%
of the time. Combined with narrative fallacy — your brain's love
of clean causal stories — overconfidence builds a portfolio of
high-conviction bets that are mostly noise.

**Stella:** And the leverage piece?

**Horace:** Connects to the volatility-tail point. Vol tail wags dog.
Overconfident investors take more leverage than their conviction
warrants, because the bell-curve model in their head puts the
next 30% drawdown at "once a century." It isn't. Once-a-decade
is the better prior, and once-a-decade leverage gets blown up by
the once-a-decade move.

---

**[SEGMENT 6: THE INTERACTIVE]**

**Horace:** The interactive at the bottom of the page lets you
toggle four classic bias rules on and off. *Sell after a 20%
drawdown.* *Buy after a 20% rally.* *Switch to bonds after two
down years.* *Chase last year's winner.* Each toggle runs a
backtest from 1928 to 2024 against simple buy-and-hold S&P.

**Stella:** And the punchline?

**Horace:** Every combination underperforms buy-and-hold. Every
single one. The strategy your spreadsheet recommends beats
almost any version of you that overrides it.

---

**[SEGMENT 7: WHAT TO ACTUALLY DO]**

**Horace:** Five concrete system designs.

One. Automatic monthly contributions. The decision was made once,
when you set up the transfer. After that there's no decision to
make in drawdowns, because there's no decision to make.

Two. Calendar-based rebalancing. Annually or semi-annually. Drift
back to target. No view-based timing. The rebalance trade
mechanically buys the loser and sells the winner — the opposite of
the recency-bias trade you'd make by hand.

Three. A written investment policy statement. One page. Three
sections. Allocation rule, trigger responses, forbidden actions.
Sign it. Re-read it during drawdowns *before* you trade.

Four. Position-sizing limits. Maximum two percent per single
name. Removes the overconfidence channel by which one
high-conviction bet eats the portfolio.

Five. Mute the noise. Unsubscribe from market news that updates
multiple times a day. Check the portfolio annually for the
rebalance, not daily. The brokerage app's red number is a
behavioural weapon pointed at your own wealth.

---

**[OUTRO]**

**Horace:** Reading about loss aversion does not make you immune
to loss aversion. Even Kahneman, who named it, said in interviews
he still feels it as strongly as he did at twenty. The bias is
wired. The fix is system design, not willpower.

**Stella:** Strategy beats discretion.

**Horace:** Strategy beats *you*. That's the lesson. Build the
systems that take the decision out of your hands at the moments
your hands are worst. The systems work. You, on a bad day, do
not.

---

**END SCREEN:** "Next: Week 12 — Inflation and the Real Return"
