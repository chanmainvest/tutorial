# Side Lesson 15: Trading Psychology — The Seven Biases That Bleed Money

---

## Part 1: Reading Section

---

### 1. Why This Is Important

You can run every spreadsheet in this course, you can quote the
Sharpe ratio of every factor, you can recite Damodaran's equity-risk
premium update from memory — and you can still lose money. The reason
is that the keyboard is connected to a biological brain that evolved
to keep a primate alive on a savannah, not to underwrite cash-flow
risk over thirty years. Trading psychology is the discipline of
spotting your own brain's defaults and overriding them with rules.
Four reasons to take it seriously:

1. **The behaviour gap is real, even if the exact number is debated.**
   Dalbar's *Quantitative Analysis of Investor Behavior* has reported
   for thirty years that the average equity-fund investor earns
   3-5 percentage points per year less than the funds they own. The
   methodology has been picked apart (Vanguard, Morningstar, and
   academics have written critiques) — and even the corrected,
   conservative reads still find a 1.5-2 pp/yr drag from poorly-timed
   buys and sells. Compounded across a 30-year career on a $100k
   starting balance, a 3 pp/yr gap turns roughly $1.0M into roughly
   $400k. The gap pays for someone else's vacation home.
2. **Bias is invisible in real time.** Confirmation bias does not
   announce itself. You do not feel anchored to your buy price; you
   feel rational. The whole problem of behavioural finance is that
   the brain's bugs *feel like* the brain's normal output. The only
   defence is structural — pre-commitment, written plans, automation
   — because in-the-moment introspection is exactly when you cannot
   trust yourself.
3. **The damage compounds asymmetrically.** Per Kahneman-Tversky
   prospect theory, a $100 loss feels roughly twice as bad as a $100
   gain feels good (lambda ~ 2.0-2.25). That asymmetry biases every
   decision: you cut winners early to lock in the good feeling, you
   hold losers because realising them hurts. You end up with a
   portfolio of losers — the disposition effect, the most documented
   bias in retail brokerage data.
4. **The market is a beauty contest.** The market can
   stay irrational longer than you can stay solvent. Every bias that
   blows up an individual blows up *more spectacularly* when you have
   leverage, a margin call, or a deadline. Behavioural discipline is
   not a soft skill; it is the precondition for compounding.

Side 15 lays out the seven biases that do the most damage, gives the
counter-measures that actually work, and shows the cumulative wealth
gap from buying-and-selling-emotionally on real S&P data.

![Bar chart: S&P 500 annualised return vs average equity investor return per Dalbar across 10y / 20y / 30y trailing windows ending 2024, with the cumulative wealth gap on a $100k initial.](../image/side15_dalbar_gap.png)

The interactive lab on the website lets you walk through three
scenario decisions — *stock down 30% — sell or hold?*, *stock up 50%
— sell or hold?*, *missed the rally — chase or wait?* — and read
both the rational answer and the typical behavioural answer side by
side.

---

### 2. What You Need to Know

#### 2.1 Loss Aversion — The 2:1 Asymmetry

Daniel Kahneman and Amos Tversky's 1979 prospect theory paper, and
the 1992 cumulative refinement, established the empirical *value
function*:

$$ v(x) = \begin{cases} x^{0.88} & x \geq 0 \\ -\lambda \, (-x)^{0.88} & x < 0 \end{cases} $$

The two pieces of that function tell you almost everything about
investor behaviour:

- **Concave in gains.** The pleasure of going from $1,000 to $2,000
  is bigger than the pleasure of going from $10,000 to $11,000, even
  though the dollar gain is identical. Diminishing marginal utility.
- **Convex in losses, AND steeper.** The pain of losing $100 is
  *roughly twice* the pleasure of gaining $100 (lambda ~ 2.0-2.25 in
  most replications). The kink at zero is the entire reason markets
  have crashes — no one wants to realise a loss, until everyone
  decides to realise the loss at once.

![Kahneman-Tversky value function with the +$100 / -$100 asymmetry annotated and the 2.25 loss-aversion coefficient marked.](../image/side15_loss_aversion.png)

Loss aversion in practice produces three predictable mistakes:
holding losers too long (because realising the loss hurts), selling
winners too early (the *disposition effect*), and being too
conservative about position sizing right after a drawdown. The fix is
not to feel less pain — you can't — but to *pre-commit* to the
sell rule before the loss happens.

#### 2.2 Recency Bias and Performance-Chasing

Recency bias is the brain's habit of weighting the last 12 months as
if it were the eternal future. After a year like 2023 (S&P +26%) or
2009 (S&P +27%), retail flows pile into US large-cap. After 2008
(-37%) or 2022 (-18%), retail flows leave. Morningstar's flow data
and the Investment Company Institute time-series both show the same
pattern: buy-high, sell-low at scale.

The math punishes recency. A simple back-of-envelope: if you switch
from cash to equities after a +20% year and switch back to cash
after a -20% year, you systematically miss the mean-reversion that
follows both extremes. Damodaran's 1928-2024 dataset shows that the
five years following a -20% calendar year averaged +14%/yr and the
five years following a +30% year averaged +6%/yr. The recency-driven
investor catches the wrong tail of every distribution.

#### 2.3 Confirmation Bias and Overconfidence

Confirmation bias is the tendency to seek and over-weight information
that supports your existing position, while ignoring or rationalising
contrary evidence. You bought TSLA at $400, the price falls to $200,
and you find five articles explaining why this is a buying opportunity
and zero articles explaining why your thesis is broken. The brain's
filter is doing its job — keeping the existing model stable — and
the portfolio pays for it.

Overconfidence is the close cousin and gets worse after streaks. A
2001 study by Brad Barber and Terrance Odean (*Boys Will Be Boys*)
showed that men trade 45% more than women and underperform by ~1.4
pp/yr; the gap is mostly explained by overconfidence after winning
trades. After a few wins, the brain *attributes* the wins to skill
and the losses to luck — even when the actual ratio is reversed.
The fix: pre-trade *journalling* (write the thesis, the entry, the
stop, and the time horizon before pressing the button) so that
post-hoc rationalisation has a paper trail to argue against.

#### 2.4 Anchoring, the Disposition Effect, and FOMO

Three closely-related biases that warp the *exit* decision:

- **Anchoring to the buy price.** The buy price has zero economic
  meaning to anyone except your tax form. The market does not know
  what you paid. But your brain treats "I bought at $80" as a magic
  reference point — green above $80, red below $80. The right
  reference is *forward expected return from here*, not "did I make
  my money back yet." If you were handed the position today as a gift
  with no cost basis, would you hold it? If no, sell.
- **Disposition effect.** The empirical pattern, documented by
  Hersh Shefrin and Meir Statman in 1985 and replicated in every
  retail brokerage dataset since, is that investors realise gains
  about 1.5x as often as they realise equally-sized losses. The
  result is a portfolio that is, on average, a collection of stocks
  that have gone *down* since purchase — the worst possible
  selection mechanism.
- **FOMO and revenge trading.** FOMO (fear of missing out) is
  recency bias dressed up as opportunity: the market ran 30% in
  three months without you, you chase, the rally tops, you take the
  drawdown. *Revenge trading* is the doubly-broken cousin — taking
  a bigger position right after a loss to "get it back," which
  converts a manageable drawdown into a catastrophic one. Said
  another way: you do not get to negotiate with the market.

#### 2.5 Anchoring's Cousin: The Gambler's Fallacy

The gambler's fallacy is the belief that independent outcomes are
*due* to balance — five red roulette spins in a row "must" be
followed by black. In markets, it shows up as: "the S&P has gone up
five years in a row, it's *due* for a crash." The market does not
owe you a crash, and prior calendar-year returns have near-zero
predictive power on the next calendar year's return (the
auto-correlation at the annual horizon is statistically
indistinguishable from zero in the 1928-2024 series). Long horizons
do mean-revert (10-year forward returns are negatively correlated
with 10-year trailing returns at r ~ -0.4) but one-year horizons do
not. Sizing trades from "we are due" is a coin-flip dressed up as
analysis.

#### 2.6 Behavioural Counter-Measures That Actually Work

The literature is clear: in-the-moment willpower does not work, but
*structure* does. Six counter-measures, ordered by leverage:

1. **Pre-commitment, in writing.** Before the trade, write down
   the thesis, the entry price, the stop level, the size, and the
   review date. Sign and date it. The behavioural literature
   (Ariely, Thaler, Sunstein) is unanimous: commitments made when
    you are calm bind you when you are emotional. The useful
   format: one paragraph for the thesis, one number for the size,
   one number for the stop.
2. **Automation.** Auto-deduct contributions to your IRA and 401(k)
   every paycheck. Auto-rebalance the index fund sleeve on a date
   schedule (quarterly or annually) or a drift-band trigger
   (rebalance when any sleeve drifts more than 5 pp from target).
   Automation removes the moment of decision, and the moment of
   decision is when you make the mistake.
3. **Checklists.** A 6-item pre-trade checklist (thesis written?
   size below 5% of portfolio? correlation to existing positions
   below 0.7? options assignment understood? tax lot identified?
   stop-loss set?) catches 80% of impulse trades. Borrow the format
   from Atul Gawande or the airline industry — the evidence base is
   the same as for surgery.
4. **Kill switches.** Set a max daily loss (e.g., 2% of account) and
   a max weekly loss (e.g., 5%). When hit, you flat the active
   sleeve and walk away from the screen for 24 hours. The kill
   switch works precisely because it is binary and pre-committed —
   no judgement call required when you are already tilted.
5. **The 24-hour rule.** For any new position above 2% of the
   portfolio, write the thesis today and place the trade tomorrow.
   24 hours is enough for most FOMO impulses to dissipate. If the
   thesis still holds tomorrow, the trade is probably real. If it
   doesn't, you saved yourself a bad print.
6. **Position-sizing rules.** No single position above 5% at cost,
   no sector above 25%, no leverage above 2.0x portfolio-wide. These
   are barbell anchors that keep one bad print from
   ending the run. From the Kelly literature: even if your edge is
   real, half-Kelly is empirically optimal because the brain's
   probability estimates are biased upward.

#### 2.7 The Compound Cost of the Behaviour Gap

Take the conservative end of the academic range: a 2 pp/yr drag from
behaviour on a $100,000 starting balance, 30 years, vs an 8%/yr
buy-and-hold benchmark. The math:

$$ \text{B\\&H: } \$100{,}000 \cdot 1.08^{30} = \$1{,}006{,}266 $$

$$ \text{Behavioural: } \$100{,}000 \cdot 1.06^{30} = \$574{,}349 $$

The gap is $432,000 — more than four times the starting balance, in
forfeited terminal wealth, from a drag that *feels invisible
year-to-year*. At the Dalbar headline number of 3-5 pp/yr the gap
becomes catastrophic ($1.0M vs ~$330k at 4 pp/yr). The behaviour gap
is the single largest fixable cost in retail investing — larger than
expense ratios, larger than tax drag (Side 4), larger than fund
selection. Fix it first, then optimise everything else.

---

### 3. Common Misconceptions

1. **"I'm too rational for this to apply to me."** The literature
   says no. Lab experiments find that *more sophisticated* investors
   are if anything *more* susceptible to overconfidence, because
   their priors are more strongly held. The fix is structural, not
   intellectual.
2. **"The Dalbar number is fake — I read the methodology critique."**
   The headline 3-5 pp/yr number is fragile and over-states the gap
   for the *median* investor. But every honest replication
   (Vanguard's "Putting a value on your value", Morningstar's "Mind
   the Gap" annual study) finds a 1.0-1.7 pp/yr drag from poor
   timing. The number is real, just smaller than Dalbar prints. At 1
   pp/yr over 30 years that is still a $200k loss on $100k starting.
3. **"Loss aversion just means I'm conservative."** No. Loss
   aversion makes you *more aggressive* on losing positions (you
   refuse to sell, you double-down to recover) and *more conservative*
   on winning positions (you book the gain to lock in the good
   feeling). It distorts both sides asymmetrically.
4. **"If I just knew more, the biases would go away."** Education
   reduces some biases (gambler's fallacy, base-rate neglect) but
   *amplifies* others (overconfidence, confirmation bias). Knowing
   you have a bias does not protect you from acting on it in real
   time. Pre-commitment does.
5. **"Dollar-cost averaging is just behavioural — the math says lump
   sum wins."** Dollar-cost averaging is *consciously* trading 0.5-0.7
   pp/yr of expected return (per Vanguard's 2012 / 2023 studies) for
   *guaranteed* removal of regret risk. If the alternative is "stare
   at the lump sum, panic, and never deploy," DCA's expected-value
   loss is small relative to the expected-value loss of doing nothing.
   Behavioural insurance has a price.
6. **"Stop-losses are for traders, not investors."** Stop-losses on
   *individual stocks* can be helpful if you size them at 2-3 ATR
   (well outside daily noise). Stop-losses on *index funds* are
   destructive because indexes mean-revert. The right tool for index
   exposure is *position sizing*, not stops — keep the index sleeve
   small enough that you can hold through a 50% drawdown without
   capitulating.
7. **"Revenge trading is just bad discipline — it's not a real
   bias."** It is a real bias. Brain-imaging studies show that the
   loss-of-money signal activates the same threat regions as physical
   pain, and the limbic response biases toward immediate
   risk-seeking. The brain is *engineered* to chase losses; calling
   it bad discipline is like calling fight-or-flight bad discipline.
   The fix is the kill switch, not willpower.
8. **"FOMO is fine when the rally is real."** The problem with
   FOMO is not that the rally is fake — sometimes it isn't. The
   problem is that you *size* the position by the strength of the
   feeling, not by the strength of the evidence. A real rally with a
   sized-too-large position becomes the next drawdown disaster.
9. **"Meditation / journaling / breathing exercises won't move the
   needle."** Self-reported and brokerage-paired studies disagree.
   Investors who keep a written trade journal show measurably
   smaller behaviour gaps in the follow-up data. The mechanism is
   not the journaling itself — it is that journaling *forces*
   pre-trade pre-commitment.
10. **"The behaviour gap is just for active traders — index
    investors are immune."** Wrong. The Dalbar gap is largest in
    *active* fund flows, but the same study shows a 1-2 pp/yr gap
    even among index-fund investors who panic-sell during drawdowns.
    The vehicle is not the protection; the *behaviour* is.

---

### 4. Q&A Section

**Q1. If loss aversion is hard-wired, what's the point of learning
about it?**
You can't turn it off, but you can route around it. Pre-commitment
(write the stop before you enter), automation (rebalance on a
schedule, not on a feeling), and position sizing (small enough that a
loss isn't existential) all attack the *consequences* of loss
aversion without requiring you to feel less pain. The brain stays
broken; the portfolio is fine.

**Q2. How big is the behaviour gap in dollars?**
Conservative (1.5 pp/yr) on $100k starting, 30y, 8% benchmark:
~$1.0M vs ~$650k → $350k forfeited. Aggressive (4 pp/yr per Dalbar):
~$1.0M vs ~$330k → $670k forfeited. Either way, larger than any
other fixable cost in retail investing.

**Q3. What's the single most useful behavioural counter-measure?**
Automation — specifically, paycheck-deducted contributions to an
IRA / 401(k). It removes the decision moment entirely. Every other
counter-measure (checklists, journals, kill switches) is incremental;
automation is structural.

**Q4. Should I check my portfolio less often?**
Yes. The behavioural finance literature broadly finds that more
frequent portfolio checking → more loss-realisation pain
(loss-aversion fires) → more bad trades. Quarterly is enough for most
retail investors. Daily is actively harmful.

**Q5. The Dalbar number is suspect — should I ignore the behaviour gap?**
No. The number is suspect at 4-5 pp/yr; it is robustly defensible at
1-2 pp/yr. Even at the conservative end the cost over 30 years is
multiples of the starting balance. The fix is the same regardless of
the exact magnitude.

**Q6. How do I handle a position that's down 30% and I think the
thesis is still right?**
Re-read the original written thesis (you wrote one — see §2.6).
If the thesis is intact and the size is below 5% of the portfolio,
hold. If the thesis broke (the company missed earnings, the
catalyst evaporated, the risk you didn't anticipate showed up),
sell — even at the 30% loss. The buy price is irrelevant; the
forward expected return is everything.

**Q7. What's the difference between conviction and confirmation
bias?**
Conviction is a position you hold *while actively looking for
disconfirming evidence* and updating your sizing on what you find.
Confirmation bias is the position you hold *while filtering out
disconfirming evidence*. The test: can you state, in writing, the
specific data point that would make you sell? If yes, conviction.
If no, bias.

**Q8. Are kill switches realistic for retail investors?**
Yes — but easier with brokerages that let you pre-set them
(IBKR, ThinkOrSwim). Manual kill switches require more discipline
("if my account is down 5% this week, I close all active positions
on Monday morning"), but they are still better than nothing.
Pre-committed in writing, reviewed weekly.

**Q9. How does the irrational-longer-than-solvent rule relate to all this?**
That rule — *the market can stay irrational longer than you can stay
solvent* — is the meta-rule. Every behavioural bias gets amplified
by leverage and by deadlines. If your time horizon is 30 years and
you have no leverage, you can survive your own brain. If you have
3:1 leverage and a margin clock, your brain's biases will compound
into a forced liquidation before the thesis is right. Strict position sizing
is the cheapest behavioural insurance you can buy.

**Q10. What role does meditation / breathwork play?**
Marginal but non-zero. The mechanism, where it works, is reducing
the amplitude of the limbic response to a loss — so the kill switch
fires before the revenge trade. It is a complement to structural
counter-measures, not a substitute. If you have to choose: write the
thesis first, breathe second.

**Q11. Can I just hire someone to manage this for me to avoid the
biases?**
Partially. A fee-only fiduciary advisor at 0.5-1.0%/yr is buying you
*one* counter-measure — the friction of having to call them before
trading. Worth it for some people, not for others. Robo-advisors at
0.25%/yr buy you automation (the most useful counter-measure)
without the human friction. Either is better than self-managing
without a structure.

**Q12. What's the one thing I should do tomorrow?**
Set up a paycheck-deducted IRA / 401(k) contribution at the highest
amount you can afford, automatically rebalanced annually.
Everything else in this lesson is incremental compared to that one
structural change. Automate the contribution; the contribution is
the trade you can never time wrong.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** "The 7 Biases That Bleed Money — Trading Psychology, Side 15"
**RUNTIME TARGET:** ~12 minutes
**HOSTS:** Horace, Stella

---

**[00:00 — COLD OPEN]**

**HORACE:** Stella, here's a number that should bother you. The
average equity-fund investor has earned 3 to 5 percentage points per
year less than the funds they own. Every year. For thirty years.

**STELLA:** That's the Dalbar number, right?

**HORACE:** That's the Dalbar number. The methodology has critics,
the size of the gap is debated, but every honest replication —
Vanguard, Morningstar, the academic crowd — finds at least 1 to 2
points per year of pure behavioural drag. On a hundred grand starting
balance over thirty years, that gap turns a million-dollar
buy-and-hold into roughly half that. We are going to talk about why
that happens.

**STELLA:** And how to stop it.

**HORACE:** And how to stop it.

**[00:50 — INTRO]**

**HORACE:** Side 15. Trading psychology. Seven biases that bleed
money, and the counter-measures that actually work. We are going to
build the lesson on top of the most important behavioural-finance
result in the literature, which is Kahneman and Tversky's prospect
theory.

[VISUAL: image/side15_loss_aversion.png]

**STELLA:** This is the value function. Gains are concave — going
from a thousand to two thousand feels better than going from ten to
eleven, even though the dollar amount is the same. Diminishing
marginal utility, classical economics is fine with that.

**HORACE:** Right. The departure from classical economics is the
loss side. Look at the slope. The pain of losing a hundred dollars
is roughly twice the pleasure of gaining a hundred. Lambda equals
2.25 in the original Kahneman-Tversky paper. Most replications put
it between 2.0 and 2.5.

**STELLA:** So if I show you a fair coin flip — heads you win
$100, tails you lose $100 — most people decline.

**HORACE:** Most people decline. The expected value is zero, the
behavioural value is negative. To get the average person to take
that bet, you need to offer them roughly $200 on heads against
$100 on tails. That is the loss-aversion coefficient.

**[02:30 — BIAS 1: LOSS AVERSION + DISPOSITION]**

**HORACE:** Bias one is loss aversion, and it produces what is
called the disposition effect. Documented by Shefrin and Statman in
1985 and replicated in every retail brokerage dataset ever assembled.
Investors realise gains about 1.5 times as often as they realise
equally-sized losses.

**STELLA:** Translation: you sell winners and you hold losers.

**HORACE:** Exactly. And after enough years, your portfolio is, on
average, a collection of stocks that have gone *down* since you
bought them. The worst possible selection mechanism.

**STELLA:** What's the fix?

**HORACE:** Pre-commitment. Before you enter the trade, write
down the price at which you sell. Both directions. The right
reference point is *forward expected return from here*, not "did I
make my money back yet."

**[04:00 — BIAS 2: RECENCY + BIAS 3: CONFIRMATION + BIAS 4:
OVERCONFIDENCE]**

**STELLA:** Bias two — recency.

**HORACE:** Recency is the brain treating the last twelve months
as if they were the eternal future. After 2023, the S&P up 26%, the
flows pile in. After 2008, the S&P down 37%, the flows leave.
Morningstar's flow data, the ICI's, every database tells the same
story.

**STELLA:** Buy high, sell low.

**HORACE:** At scale. And the cruel part is that the math
mean-reverts. Damodaran's data, 1928 to 2024 — the five years
following a *down 20% calendar year* averaged plus 14 percent per
year. The five years following an *up 30% calendar year* averaged
plus 6 percent.

**STELLA:** The recency-driven investor is on the wrong side of the
distribution every time.

**HORACE:** Bias three — confirmation. You buy TSLA at $400, the
price falls to $200, and your news feed somehow only shows you
articles explaining why this is a buying opportunity. The brain's
filter is doing its job — keeping the existing model stable. The
portfolio pays for it.

**STELLA:** Bias four — overconfidence. Especially after streaks.

**HORACE:** Brad Barber and Terrance Odean, *Boys Will Be Boys*,
2001. Men trade 45% more than women and underperform by 1.4 points
per year. The gap is overconfidence. After a few wins, the brain
attributes the wins to skill and the losses to luck. Even when the
actual ratio is reversed.

**[06:30 — BIAS 5: ANCHORING + BIAS 6: FOMO + BIAS 7: GAMBLER'S]**

**HORACE:** Bias five — anchoring. To your buy price. The market
does not know what you paid. Your tax form knows; nobody else cares.

**STELLA:** But the brain treats "I bought at $80" as a magic line.

**HORACE:** Green above, red below. The cure is the *gift test*.
If somebody handed you the position today, free, no cost basis,
would you hold it? If no, sell. Doesn't matter that you paid more.

**STELLA:** Bias six — FOMO and revenge trading.

**HORACE:** FOMO is recency dressed up as opportunity. The
market ran 30% in three months without you, you chase, the rally
tops, you take the drawdown. Revenge trading is the doubly-broken
cousin — taking a bigger position right after a loss to "get it
back." That converts a manageable drawdown into a catastrophic one.

**STELLA:** Bias seven — the gambler's fallacy.

**HORACE:** The S&P has gone up five years in a row, it's "due"
for a crash. Wrong on two counts. One, calendar-year returns are
near-zero auto-correlated. Two, the market does not owe you a
crash. It will hand you one when it feels like it.

**[09:00 — COUNTER-MEASURES]**

**STELLA:** OK, biases identified. Counter-measures.

**HORACE:** In order of leverage. One — pre-commitment, in
writing. Before the trade, write the thesis, the entry, the stop,
the size, and the review date. Sign and date it. Two — automation.
Auto-deduct the IRA contribution every paycheck. Auto-rebalance
quarterly. Automation removes the decision moment, and the decision
moment is when the bias fires.

**STELLA:** Three — checklists.

**HORACE:** A six-item pre-trade checklist catches 80% of impulse
trades. Borrow the format from Atul Gawande or the airline
industry. Same evidence base.

**STELLA:** Four — kill switches.

**HORACE:** Max daily loss, say 2% of account. Max weekly loss,
say 5%. When hit, you flat the active sleeve and walk away from the
screen for 24 hours. Pre-committed and binary. No judgement call
required when you are already tilted.

**STELLA:** Five — the 24-hour rule.

**HORACE:** For any new position above 2% of the portfolio, write
the thesis today, place the trade tomorrow. 24 hours is enough for
most FOMO impulses to dissipate.

**STELLA:** Six — position sizing.

**HORACE:** No single position above 5% at cost. No sector above
25%. No leverage above 2.0x portfolio-wide. The
barbell. The cheapest behavioural insurance you can buy is keeping
each position small enough that one bad print does not end the run.

**[11:00 — DALBAR + COMPOUND COST]**

[VISUAL: image/side15_dalbar_gap.png]

**HORACE:** Here is the gap on real numbers. Three trailing
windows ending December 2024 — ten years, twenty years, thirty
years. The fund bar is the S&P 500. The investor bar is the
dollar-weighted return of the average investor in those funds. The
gap is roughly 4 percentage points per year on the headline Dalbar
read, 1.5 to 2 on the conservative replications.

**STELLA:** And the cumulative wealth gap?

**HORACE:** On a hundred grand starting balance, thirty years, the
S&P at 10.2% per year takes you past 1.8 million. The average
investor at 6.8% gets you to roughly 720 thousand. The difference is
over a million dollars — ten times your starting balance, in
forfeited terminal wealth, from a drag that *feels invisible
year-to-year*.

**[VISUAL: course/interactive/side15_bias_lab.html]**

**STELLA:** And on the website we have a scenario lab. Three
choices — stock down 30% sell or hold, stock up 50% sell or hold,
missed the rally chase or wait. For each one we show the rational
choice, the typical behavioural choice, and the typical empirical
outcome.

**HORACE:** Walk through them once. Then walk through them again
when you are about to make the decision in real life.

**[12:00 — OUTRO]**

**HORACE:** Final note. The market can stay irrational longer
than you can stay solvent. Every bias on this list gets amplified
by leverage and by deadlines. The biases are hard-wired; they will
not go away. The fix is structural — pre-commitment, automation,
checklists, kill switches, position sizing.

**STELLA:** Automate one thing tomorrow. Paycheck-deducted IRA
contribution. Quarterly rebalance.

**HORACE:** That single change beats every other thing in this
lesson. Then the rest of the structure goes on top.

**STELLA:** See you in Side 16.

**[END.]**
