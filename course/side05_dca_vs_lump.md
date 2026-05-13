# Side Lesson 05: DCA vs. Lump Sum — The Math, the Behavior, and When Each Wins

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Sooner or later every investor stares at a pile of cash and asks the
same question: *put it all in at once, or spread it out?* An
inheritance lands. A bonus arrives. A house sells. A 401(k) rolls
over. The cash sits in a money-market fund earning 4.2% and the
question gets sharper every Monday morning.

This is one of the few corners of investing where the textbook answer
and the human answer genuinely diverge. The mathematics are
unambiguous: **lump sum wins about two-thirds of the time** over the
following twelve months, and the long-run *expected* terminal wealth
is higher. The behavioural picture is just as clear: dollar-cost
averaging into the market lowers regret variance, reduces the
probability of buying right at the top, and — most importantly —
helps the cash actually *get invested* instead of sitting on the
sidelines for three more years waiting for "a better time."

Four reasons this lesson earns a slot:

1. **The framing is wrong for most retail investors.** If you are a
   salaried worker contributing from each paycheck, you are already
   doing forced DCA — that is the only option you have. The
   lump-vs-DCA question only really applies to *windfalls.*
2. **The "I'll wait for a dip" alternative is the worst of all.**
   Cash on the sidelines is not a third strategy; it is a *failure*
   to choose between the first two.
3. **The 33% of the time DCA wins includes the periods that scar
   investors for life** — 2000-2002 and 2008. That bias toward
   nightmare scenarios is exactly why the behavioural story matters.
4. **Stay solvent before being right** — the rational investor who
   panics out at the bottom has already lost. DCA is the rational
   behavioural hedge that keeps the irrational version of you
   solvent.

---

### 2. What You Need to Know

#### 2.1 Defining the Two Strategies Cleanly

**Lump sum (LSI).** You receive $120,000. On day one, you buy your
target allocation in full. Day two onward, you do nothing.

**Dollar-cost averaging (DCA).** You receive $120,000. You divide it
into equal slices — $10,000 a month for twelve months is the
canonical version — and buy the target allocation slice by slice on
a fixed schedule. The cash not yet invested earns money-market yield
(currently around 4.2% on T-bills, April 2026).

**What DCA is *not*.** Putting $1,000 of every paycheck into your
401(k) is *systematic investing,* not DCA. You do not have a lump
sum to deploy; you have a steady drip of new income. The
lump-vs-DCA question genuinely does not apply. Calling
paycheck-investing "dollar-cost averaging" is a marketing trope from
the mutual-fund industry — useful as a sales line, useless as a
decision framework. And while we are here: the 401(k) drip is the
cleanest proof that there is no truly passive income — the
*input*, the bit you scraped out of the paycheck before you ever
got to the timing question, is doing all the work. The schedule is
automatic; the saving was not.

The problem this lesson addresses is narrow:

> *I have a sum of money I am ready to invest, today, in my target
> allocation. Should I buy it all on Monday, or split the purchase
> across N months?*

#### 2.2 The Math: Lump Sum Wins on Expected Value

If your expected return on the target allocation is positive — which
it has to be, otherwise why are you investing at all — then the
expected terminal wealth from lump sum is **strictly higher** than
the expected terminal wealth from DCA. The proof is one line:

$$
\mathbb{E}[\text{LSI}] = P (1 + \mu)^N \quad > \quad \mathbb{E}[\text{DCA}] = \frac{P}{N} \sum_{k=1}^{N} (1 + \mu)^{N-k+1}
$$

For positive $\mu$, every dollar deployed earlier compounds for
longer. DCA holds half the money in cash on average over the deploy
window; that half earns the cash rate, not the equity rate. The
spread between the equity expected return (~7-9% nominal) and the
cash rate (~4%) is the *cost* of DCA on the average outcome.

How big is the cost in dollars? On $120,000 deployed over 12 months
into a 60/40 portfolio (expected ~6.5% over cash), DCA gives up
roughly **0.5-0.7% of terminal wealth in expectation,** or about
$600-$850 on $120k. Small in absolute dollars, but it compounds
forever — that gap never closes.

![Lump vs. DCA monthly winner from 1928-2024. Each thin vertical bar is one starting month: blue means $120k lump sum beat $10k x 12 DCA over the next 12 months, red means DCA won. Roughly 67% of starts are blue. The visible red clusters are the famous nightmare entries: 1929-30, 1937, 1973-74, 2000-02, 2008.](../image/side05_winrate_history.png)

#### 2.3 The Empirical Record: ~67% Lump-Sum Wins

The Vanguard 2012 study (Shtekhman, Tasopoulos, and Wimmer) ran the
trade in three markets — the US 1926-2011, the UK, and Australia —
and found lump sum beat 12-month DCA in **about two-thirds** of all
rolling 12-month windows. The exact print depends on the asset mix:

| Allocation | LSI win rate | Average outperformance |
|---|---|---|
| 100% stocks | 66% | +2.4% |
| 60/40 | 67% | +2.3% |
| 100% bonds | 70% | +1.6% |

The 2023 Vanguard refresh (Aliaga-Diaz et al, *Cost Averaging: An
Analysis...*) using 1976-2022 data confirmed the same range. The
result is robust across the bond-heavy 1980s, the equity boom of the
1990s, the 2000s lost decade, and the post-2010 bull. It does not go
away.

The win rate is not 100% for an obvious reason: a third of all
12-month windows in market history go *down*, and in down markets
DCA — by holding cash longer — loses less. This is just the mirror
image of the expected-value argument. Lump sum has higher *mean*
outcome because it has higher *variance* of outcome. DCA truncates
the left tail by holding cash; in exchange it truncates the right
tail too.

#### 2.4 The 33% Where DCA Wins: The Nightmare Calendar

The third of the time DCA wins is not random. It clusters tightly
around the worst entry points in market history:

- **1929-1932.** Lump in October 1929 = -68% terminal wealth at end
  of year 1; DCA splits losses across the crash and finishes far
  less down.
- **1937-1938.** Roosevelt recession; lump-sum -38% in 12 months.
- **1973-1974.** Stagflation bear; -42% lump vs. -22% DCA.
- **2000-2002.** Dot-com unwind; lump entries in early 2000 finished
  -25% at twelve months.
- **2008.** This is the one investors remember. **Jan 2008 lump =
  -38%** at end-December. **Jan 2008 DCA = -27%** at end-December
  (cash earning 0%; closer to -19% if idle cash earns the
  T-bill rate the way Vanguard's original study assumed).

![Two-panel comparison of lump-sum vs. DCA over 2008. Left panel shows the wealth curves diverging through the year: lump-sum tracks the S&P 500 down about 38% by end-December while DCA, holding cash at zero through 2008, ends down about 27% (and would be closer to -19% with cash earning the T-bill rate). Right panel shows the contribution timing — DCA's monthly purchases at progressively lower prices give it a lower average cost basis.](../image/side05_worst_case.png)

The math is straightforward: by buying in twelfths, the DCA investor
purchases the last $10k tranche in December 2008 at prices about 40%
below the January starting point. Their average cost basis is roughly
20% below the lump-sum investor's. When the recovery begins in March
2009, the DCA investor recovers to break-even faster.

That said: even DCA-2008 was painful. The DCA investor still
finished 2008 down somewhere between 19% (with T-bill yield on
idle cash) and 27% (with cash yielding zero) on paper. Both strategies recovered by 2012-13
in nominal terms (longer in real). Neither one *avoided* the bear
market; one merely softened it.

#### 2.5 The Behavioural Case for DCA — Regret Variance

Pure expected-utility theory says lump sum wins. Behavioural
finance, which actually models how humans *experience* outcomes,
adds two terms the textbook leaves out:

1. **Regret aversion.** The pain of buying at the top and watching
   the position drop 30% is felt asymmetrically — far more
   painfully than the corresponding pleasure of buying at the bottom
   and watching it rise 30%. Loss aversion has been measured at
   roughly 2:1 — Kahneman & Tversky's number — meaning the felt
   cost of being wrong is twice the felt benefit of being right.
2. **Sequence anxiety.** A lump-sum investor who watches their
   $120,000 mark down to $90,000 in three months will, in many
   cases, *sell* — locking in the loss precisely when DCA would
   still be buying. The behavioural failure mode is not the
   strategy; it is the strategy being *abandoned* at the worst
   possible moment.

DCA is a rational hedge against the *irrational version of yourself.*
The expected-value cost of 0.5-0.7% terminal wealth is the premium
you pay so that the version of you in March 2009 is still in the
market at all. Say it again: irrational and solvent beats rational
and bankrupt.

If you can *honestly* say you are the kind of investor who would not
panic out of a 30% lump-sum drawdown — and Week 11 has the data on
how few people actually pass that test — go lump. If you have any
doubt, the 0.6% expected-value cost of DCA is a cheap insurance
policy on your own future behaviour.

#### 2.6 The Real Anti-Pattern: Cash on the Sidelines

The serious failure mode is not lump-vs-DCA. It is *neither.* The
median retail investor with a windfall does not lump or DCA — they
sit on the cash for 18-36 months, waiting for "a better entry." Then
the market goes up another 30% during the wait. Then they decide the
market is "too high." Then they wait some more.

The Vanguard 2012 paper makes this point in a single number: cash
underperforms a 60/40 portfolio over rolling 12-month windows
**roughly 67% of the time** — the same number as lump-vs-DCA — but
with a much wider spread. Holding cash for a year while waiting for
the dip costs about 4% of terminal wealth in expectation, and that
cost compounds while you procrastinate.

A note on *what* you are lumping into. For the reader this lesson is
written for — first portfolio, apprenticeship phase — the target
allocation on the receiving end of the lump is SPY (or the
equivalent broad-US-equity index ETF), not a barbell of cash, gold,
and option structures. The barbell is the shape I run today, but
it earns its keep only after you have internalised the regime
thesis and built the toolkit the speculative end demands. Skip the
apprenticeship and you have dropped the index core for nothing on
one side and a sleeve you cannot operate on the other. Lump into
the index, do the apprenticeship, *then* migrate the shape — in
that order.

The decision framework is:

1. **You will invest the money** — that is the prior, before any
   timing question.
2. **Lump if you can stomach the volatility.** Math says you will be
   richer 2/3 of the time and richer in expectation always.
3. **DCA over 6-12 months if you cannot.** Pay the small expected
   cost in exchange for behavioural stability. Set the schedule on
   day one and do not adjust it based on market moves.
4. **Never wait.** Cash sitting in a money-market fund "until the
   market settles" is not a strategy. It is procrastination wearing
   a financial-advisor costume.

#### 2.7 Practical Rules — If You Are Going to DCA, Do It Right

If you choose DCA, three rules make it work:

1. **Pick the deployment window in advance and *automate it.***
   $10k on the first business day of each month for N months. Set
   it as a recurring transfer. Do not let yourself "skip" months
   when prices look high or "double up" when prices look low — that
   is market timing dressed as DCA, and it has an even worse track
   record than either pure approach.
2. **Six to twelve months is the sweet spot.** Longer than 12
   months and the cash drag dominates — you are mostly just holding
   cash. Shorter than 3 months and you might as well lump.
3. **The interactive lab on this page lets you replay any starting
   year from 1928 to 2024** with any deployment window from 3 to 24
   months. Try the bad ones — Jan 1973, Oct 1987, Jan 2000, Jan
   2008. Try the good ones — Jan 1995, Jan 2009, Jan 2020. The
   pattern is exactly what the math says: lump usually wins, DCA
   wins in the disasters, and the disasters cluster.

The interactive panel gives you the full backtest. The two static
images above tell the same story in compressed form: the empirical
win-rate over a century of monthly starts, and the iconic 2008
playbook where DCA's behavioural value showed up.

---

### 3. Common Misconceptions

**1. "DCA reduces risk."** It reduces *deployment-window* risk only.
Once you are fully deployed at month 12, you hold the same risk as
the lump-sum investor. DCA is a transition strategy, not a portfolio
strategy.

**2. "DCA gives you a lower average cost."** Only in down markets.
In up markets — which is two-thirds of all 12-month windows — DCA
gives you a *higher* average cost than buying everything at the
start.

**3. "Spreading purchases across the year smooths out volatility."**
The volatility of your terminal wealth at 12 months is lower under
DCA, but only by roughly 30%. It is not zero. The strategy is more
dampened, not insulated.

**4. "I'll do half lump, half DCA."** This is a reasonable hedge
that captures most of the behavioural benefit of DCA at half the
expected cost. Vanguard's data has a 50/50 hybrid landing roughly
midway between the pure strategies on both expected return and
regret.

**5. "DCA works because of buying more shares when prices are low."**
This is the standard sales pitch, and it is true *only* when the
average price over the deploy window is below the starting price —
i.e., in a falling market. It is not a magic property; it is just
the arithmetic of buying low.

**6. "I should DCA my paycheck contributions."** Your paycheck
contributions are *already* DCA — they have to be, because the
income arrives in pieces. You are not choosing to DCA; you have no
lump sum to deploy. The lump-vs-DCA question genuinely does not
apply to systematic 401(k) contributions.

**7. "Waiting for a better entry is the same as DCA."** It is not.
DCA is a fixed schedule, decided in advance, executed mechanically.
Waiting for a dip is discretionary market timing — by far the
worst-performing of all three approaches in every rolling-window
study ever run.

**8. "If lump sum wins on expected value, I should always lump."**
Only if you are confident that the *behavioural* version of you will
not abandon the strategy in a drawdown. That is a much higher bar
than most investors realise. The 0.6% expected-value cost of DCA
buys behavioural insurance — sometimes worth it, sometimes not.

---

### 4. Q&A

**Q1: What is the exact win rate for lump sum versus DCA?**

About **67%** over rolling 12-month windows in US data 1928-2024,
deploying into either 100% stocks or a 60/40 portfolio. The Vanguard
2012 paper reported 66-67% across US/UK/Australia; the 2023 update
reconfirmed it on 1976-2022 data.

**Q2: How much does lump sum outperform on average?**

About **2.3% of terminal wealth** over the 12-month deploy window
under a 60/40 portfolio. In dollar terms, that is roughly $2,300 on
$100,000 deployed, persisting forever as a level shift in the
account balance.

**Q3: What is the worst case for lump sum?**

January 1929 lump entry: terminal wealth at end of year 1 was around
*-68%* of starting capital after the late-1929 crash. Even
splitting across 12 months would not have saved you fully — that is
a 30% loss instead of a 60% loss. The bigger lesson from 1929 is
about leverage and concentration, not lump-vs-DCA.

**Q4: What if my windfall is huge — say, $5 million?**

The math is identical at every scale. The behavioural concerns are
worse — a 30% drawdown on $5M *feels* very different from a 30%
drawdown on $50k. For large windfalls, a longer DCA window (18-24
months) is more defensible specifically as behavioural insurance,
even though the expected-value cost is higher. Most private banks
default to 6-12 month deployment plans for exactly this reason.

**Q5: Should I use VWAP or fixed-date scheduling?**

Fixed-date. The first business day of each month is the standard.
VWAP-style "price-aware" deployment turns DCA into a market-timing
exercise, which is exactly what DCA was supposed to protect you
from.

**Q6: What about deploying *out* of the market — should I lump-sell
or DCA-sell?**

Symmetric math: lump-selling has higher expected value (your cash
earns less than your equity exposure on average), DCA-selling has
lower regret variance. The behavioural calculus is reversed though,
because the default state (holding) is the *risky* state when you
are trying to de-risk. Most retirees choose DCA-out for the same
behavioural reasons others choose DCA-in.

**Q7: Does the answer change for international stocks or bonds?**

Lump still wins on expected value because the expected return is
positive. The win rate is slightly lower for assets with lower
expected returns over cash — for 100% bonds it was about 70% in
Vanguard's data, for 100% stocks about 66%. Higher-return assets
have a wider spread between the equity rate and cash, so the
*magnitude* of lump's win is bigger.

**Q8: How does this interact with tax?**

Lump-sum starts the holding-period clock for long-term capital gains
treatment 12 months earlier on the entire position. For taxable
accounts that matters: if you sell after 13 months, lump's gains are
all LTCG; DCA has roughly half the position still at short-term
rates. Long-term-gains treatment is the cheapest free money in US
tax law, and lump grabs it earlier.

**Q9: Is "DCA out of cash that I had been waiting with" a thing?**

It is what most people *actually* do, and it is fine. It is just
late DCA. The cost is the months you spent in cash before starting
the deployment plan. Start the plan, follow it, and stop the
"waiting for a better entry" loop.

**Q10: What does the interactive lab show me?**

Pick an amount, a DCA window (3 / 6 / 12 / 24 months), and a start
year (1928 to 2024). The lab runs the backtest using monthly returns
derived from the Damodaran annual dataset and reports four numbers:
lump-sum terminal wealth, DCA terminal wealth, the dollar
difference, and the maximum drawdown that occurred *during* the
deployment window. Pick start years that match the disasters in this
lesson — 1929, 1973, 2000, 2008 — and watch the only times DCA
actually wins line up exactly with where the textbooks said they
would.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Lump Sum vs. Dollar Cost Averaging — What 96 Years of Data Says | Side Lesson 5

**RUNTIME TARGET:** ~13 minutes

**HOSTS:**
- **Horace** (teacher): Holds the windfall hypothetical.
- **Stella** (student): Asks what most retail investors actually ask.

---

**[INTRO]**

[VISUAL: Animated logo "Side Lesson 5 — DCA vs. Lump Sum"]

**Horace:** Stella, you just inherited $120,000. Tomorrow morning,
the cash hits your account. What do you do — invest it all on
Monday, or spread it out over twelve months?

**Stella:** Honestly? I would probably leave it in the savings
account for six months while I "thought about it."

**Horace:** That is the most common answer, and it is also the worst
of the three available choices. Today we are going to do the math
on the other two — buy it all on day one versus split it across the
year — and then we are going to talk about why the textbook answer
is not always the right one for an actual human.

---

**[SEGMENT 1: THE WIN RATE]**

[VISUAL: image/side05_winrate_history.png]

**Horace:** Every thin bar on this chart is one starting month from
January 1928 through the end of 2023. Blue means lump sum won over
the next twelve months. Red means DCA won.

**Stella:** Looks like a lot of blue.

**Horace:** Two-thirds of all months. About 67%. That is the
Vanguard number — they ran this study in 2012, refreshed it in 2023,
and the result has not budged. Lump sum beats DCA in roughly
two-thirds of all 12-month windows in market history.

**Stella:** Why?

**Horace:** Because markets go up two-thirds of the time. If the
market is going up, money you deploy earlier compounds for longer.
DCA holds half the cash in T-bills on average over the deployment
window — that half earns 4%, not 8%. The spread is the cost.

**Stella:** And the red clusters?

**Horace:** Those are the disasters. 1929. 1937. 1973-74. 2000-02.
2008. The 33% of the time DCA wins is not random — it is a tightly
clustered set of nightmare years that scarred entire generations of
investors. Which is exactly why the behavioural story matters.

---

**[SEGMENT 2: WHY THE MATH SAYS LUMP]**

[VISUAL: equation overlay $E[\text{LSI}] = P(1+\mu)^N$ vs. the DCA sum.]

**Horace:** The expected-value math is a one-liner. If your expected
return is positive — which it has to be, otherwise you would not be
investing — then deploying the full sum on day one earns the equity
return on every dollar from day one. Deploying it across N months
earns the equity return on the part that is invested and the cash
rate on the part that is not.

**Stella:** And the difference is...

**Horace:** On $100k deployed over 12 months into 60/40, you give up
about $2,300 in expected terminal wealth. Forever. That gap
compounds for the rest of the holding period.

**Stella:** $2,300 on $100k is not nothing.

**Horace:** It is not. But it is also not catastrophic — and
crucially, it is the *expected* cost. Two-thirds of the time it is
actually higher; one-third of the time DCA wins outright.

---

**[SEGMENT 3: THE 2008 PLAYBOOK]**

[VISUAL: image/side05_worst_case.png]

**Horace:** Let's look at the famous bad year. 2008. Imagine on
January 2nd you have $120,000 in cash. Strategy A: buy the S&P 500
all at once. Strategy B: $10k on the first of every month for
twelve months.

**Stella:** I already know how this ends.

**Horace:** Lump sum: down 38% by end of December. DCA: down
roughly 27% with idle cash earning zero — and closer to -19% if
you park the un-deployed slices in T-bills the way Vanguard's
original study assumed. The DCA investor's last $10k in December 2008
bought shares at roughly 40% off the January price. Their average
cost was about 20% lower than the lump-sum investor's.

**Stella:** So DCA is the right answer if you start in a crash.

**Horace:** It is the right answer *if you start in a crash*. The
problem is you do not know in advance that you are starting in a
crash. If you knew, you would not be having this conversation. You
would just wait. The data says 67% of the time you would be wrong
to wait.

---

**[SEGMENT 4: THE BEHAVIOURAL CASE]**

[VISUAL: Title card "Regret Variance"]

**Horace:** Here is where the textbook stops and the real world
begins. Kahneman and Tversky, 1979 — loss aversion is roughly 2 to
1. The pain of losing $30k feels twice as bad as the pleasure of
gaining $30k.

**Stella:** So a 30% drawdown right after I lump in...

**Horace:** Feels twice as bad as a 30% gain. And the behavioural
failure mode is not the strategy itself — it is the investor
abandoning the strategy at the worst possible time. The lump-sum
investor in March 2009 who panic-sold at the bottom locked in a 50%
loss. The DCA investor who was *still buying* in March 2009 ended
up with the recovery.

**Stella:** So DCA is insurance against me?

**Horace:** Exactly. The rule is simple: irrational and solvent
beats rational and bankrupt. DCA is the rational hedge against the
irrational version of you that exists in March 2009. You pay
0.6% of terminal wealth in expectation; in exchange the version of
you that wakes up in a bear market is still in the market.

---

**[SEGMENT 5: THE REAL ANTI-PATTERN]**

[VISUAL: Title card "Cash on the Sidelines"]

**Horace:** The serious mistake is not lump versus DCA. It is
*neither.* The median retail investor with a windfall sits on the
cash for two years waiting for "a better time." During those two
years the market is up another 30% — because the market goes up two
thirds of the time, remember.

**Stella:** And then they think the market is too high.

**Horace:** And then they wait some more. Vanguard's number on this:
holding cash beats a 60/40 portfolio about 33% of the time —
exactly the inverse of the lump-versus-cash trade. Two thirds of the
time, sitting in cash for the year is the worst of the three
available choices.

---

**[SEGMENT 6: THE INTERACTIVE LAB]**

[VISUAL: cut to interactive/side05_dca_lab.html in the browser.]

**Horace:** The lab on the website lets you replay any starting year
from 1928 to 2024. Pick an amount, pick a DCA window — 3, 6, 12, or
24 months — pick a start year. Try the disasters first.

*(types: $120k, 12 months, start 2008)*

**Horace:** Lump terminal: $74k. DCA terminal: $97k. DCA wins by
$23k. That is the 33%-of-the-time scenario.

*(types: start 1995)*

**Horace:** Lump: $158k. DCA: $148k. Lump wins by $10k. That is the
67% scenario.

*(types: start 2020)*

**Horace:** Lump: $156k. DCA: $138k. Lump wins by $18k — the COVID
recovery rewarded the people who bought before they knew the
recovery was coming.

**Stella:** So play with it for ten minutes and the pattern is
obvious.

**Horace:** That is the point. The numbers are not abstract — they
are exactly the same monthly equity returns that produced the actual
historical outcomes.

---

**[SEGMENT 7: THE PAYCHECK QUESTION]**

[VISUAL: Title card "If You Are Salaried, You're Already Done"]

**Horace:** One last point. If you are a salaried worker
contributing to a 401(k) or an IRA from each paycheck, this whole
debate does not apply to you.

**Stella:** Why not?

**Horace:** Because you do not have a lump sum. The income arrives
in twenty-six pieces a year, and you invest each piece as it comes
in. That is *forced* DCA, and it is the only choice you have. The
lump-versus-DCA question only matters for windfalls — inheritance,
bonus, house sale, retirement-account rollover.

**Stella:** Got it. So this lesson is for the windfall day.

**Horace:** Right. For the day someone hands you a check large
enough that the question stops being theoretical. And one footnote
on the paycheck case before we move on — that monthly drip is also
the cleanest reminder that there is no truly passive income. The
schedule is automatic; the savings rate that *fed* the schedule was
not. The input precedes the timing question every single time.

**Stella:** And the lump itself — what am I lumping into?

**Horace:** For someone reading this lesson, building a first
portfolio, the answer is SPY. The broad index. Cheap, tax-efficient,
works as long as the forty-year passive consensus keeps working. I
run a barbell shape these days — cash and gold on one end, asymmetric
option positions on the other — but that shape only works after you
have internalised why the consensus might break and built the toolkit
the speculative end actually requires. Don't skip the apprenticeship
to copy the shape. Lump into the index, learn for a few cycles, and
then think about migrating.

---

**[OUTRO]**

[VISUAL: Summary card with three bullets:
- ~67% lump sum wins
- DCA wins clusters in disasters
- Cash on sidelines is the real loser]

**Horace:** Three takeaways. One: lump beats DCA roughly two thirds
of the time, and the expected-value cost of DCA is real but small —
about half a percent of terminal wealth on a 12-month deploy. Two:
the times DCA wins are precisely the disasters investors most fear,
which is what makes it a defensible behavioural hedge. Three: the
strategy that loses to *both* of the others, two thirds of the
time, is sitting in cash waiting for a better moment. Pick lump if
you can stomach it. Pick DCA if you cannot. Just do not pick
neither.

**Stella:** Got it. Lump if I can take a 30% paper loss without
panicking. DCA if I cannot. Never sit in cash.

**Horace:** That is the lesson.

[END CARD: "Side Lesson 5 — DCA vs. Lump Sum"]
