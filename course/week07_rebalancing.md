# Week 7: Rebalancing — When, How, and Why

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Rebalancing is the single most boring operation in personal finance,
and it is also the only one that mechanically forces you to do the
right thing at the moment you least want to. You set a target
allocation — say, 60/40 stocks and bonds — and then once a year, or
once a drift band has been breached, you trim what has done well and
top up what has done poorly. That is the entire procedure. It takes
half an hour. It is the closest thing to an edge that does not
require a forecast, a model, or a Bloomberg terminal.

You need to understand rebalancing for four reasons.

1. **Without it, your portfolio is not the portfolio you chose.**
   A 60/40 mix that runs through the 2010s with no rebalancing ends
   the decade closer to 78/22. Your *risk* has silently re-priced
   itself by roughly fifty percent. The next bear market will then
   hit you in a portfolio you never agreed to hold.
2. **It is the cleanest implementation of "buy low, sell high" that
   exists.** The decision is mechanical. There is no view, no
   forecast, no narrative. You sell the asset that is now overweight
   *because* it has outperformed and buy the one that is now
   underweight *because* it has underperformed. The act of
   rebalancing **is** contrarianism, packaged as an annual chore.
3. **Humans cannot do this on their own.** The market
   can stay irrational longer than you can stay solvent, and
   the corollary nobody wants to hear is that *you* will turn
   irrational long before the market does. Selling NVDA after a
   triple, in your taxable account, in the year your neighbour just
   bought a Porsche on his — that is not a trade humans place
   voluntarily. A rebalancing rule places it for you.
4. **The 2022 dilemma exposed a hidden assumption.** The whole
   rebalancing premium argument rests on stocks and bonds being
   negatively correlated. In 2022 they fell together. The
   rebalancer who sold winners to buy losers in mid-2022 had no
   winners to sell. We will dissect what to do in that case.

This lesson covers the mechanics of drift, the calendar-vs-threshold
question, the rebalancing premium and where it actually comes from,
the tax cost of rebalancing in taxable accounts, the contributions-
based workaround, and the 2022 case study.

---

### 2. What You Need to Know

#### 2.1 Drift — Why a Portfolio Will Not Stay Where You Put It

Two assets with different returns and different volatilities cannot
hold their relative weights for long. Higher-return assets compound
their share of the pie; lower-return assets shrink in proportion.
Even in a single calm decade the drift is large.

The image below runs the 2010–2019 decade — stocks compounding at
roughly 13.6% per year and 10-year Treasuries at roughly 3.7% — on a
$100,000 starting 60/40 portfolio under two policies. The top panel
holds no rebalances at all over the ten years. The bottom panel
rebalances back to 60/40 every January.

![Top panel, no rebalancing over 2010-2019: starting 60/40 stock-bond mix on a $100,000 portfolio, the stock weight climbs steadily as US stocks compound at ~13.6% annually while Treasuries earn ~3.7%, ending the decade near 78/22. The bond sleeve shrinks visibly as a fraction of the total. Bottom panel, annual rebalance: the stock weight oscillates within a couple of percentage points of 60% all decade, returning each January to the target while leaving the absolute-dollar wealth path almost identical.](image/week07_drift.png)

The end-state of the no-rebalance portfolio is not 60/40 and never
was after the first year. By 2019 it sat at about 78/22 — closer to
the textbook "aggressive" allocation than to the "balanced" one the
investor originally chose. When the COVID crash arrived in March 2020
that drifted portfolio dropped roughly two percentage points more
than the rebalanced version, on a much larger asset base. The
investor who never rebalanced did not consciously become more
aggressive in 2019. They drifted there.

#### 2.2 Calendar vs Threshold — Two Triggers, One Goal

There are two principled ways to decide *when* to rebalance.

**Calendar rebalancing** picks a fixed date — typically annual
(the simplest), occasionally semi-annual or quarterly — and trims
back to target on that date regardless of how far the portfolio has
drifted. The merit is operational: it is one calendar entry per year,
it can be automated by most brokerages, and it produces no surprises
in your tax planning.

**Threshold (or band) rebalancing** ignores the calendar and triggers
a rebalance only when one asset class has drifted beyond a fixed
percentage band — say, ±5 absolute percentage points around the
target, so a 60% stock target rebalances at 55% or 65%. The merit is
efficiency: in a calm year you do nothing; in a violent year (1987,
2008, 2020) you rebalance multiple times, capturing the mean
reversion that calendar rules miss.

The image below compares four policies on the full 1928–2024
Damodaran dataset of US stocks and 10-year Treasuries: never
rebalance, rebalance annually, rebalance semi-annually, and a 5%
band. The bars show the geometric annualised return, the realised
volatility, and the worst-year drawdown for each policy.

![Bar chart comparison of four rebalancing policies on the Damodaran 1928-2024 60/40 stock/bond data: 'never rebalance' delivers the highest end-state arithmetic exposure but also the largest realised volatility and deepest drawdown because it ends the period at near-90/10. The annual, semi-annual, and 5%-band policies cluster tightly together in geometric return (within ~0.1% of each other), with materially lower volatility (~10% vs ~13%) and shallower drawdowns. The 5%-band policy shows the lowest turnover-adjusted return.](image/week07_method_comparison.png)

Three readings come out of this chart.

First, **rebalancing reduces volatility and drawdowns more than it
changes the return.** All three rebalanced policies finish within
about ten basis points of each other in geometric return. The story
is in the risk columns, not the return column.

Second, **the difference between annual, semi-annual, and 5% band is
genuinely small.** Pick one, run it for thirty years, and you will
get within a few basis points of any other reasonable rule. This is
a place where over-engineering pays nothing.

Third, **never-rebalance is the worst of the four on a risk-adjusted
basis.** Higher absolute return, but realised volatility runs about
16% versus roughly 12% for the rebalanced policies — a 30% jump in
risk for a return that is itself an artefact of the portfolio having
drifted to near-90/10 by the end. The investor who refuses to
rebalance is not running a 60/40 portfolio; they are running a
slowly-creeping all-equity portfolio.

#### 2.3 The Rebalancing Premium — Volatility Harvesting

Periodic rebalancing of two volatile assets that are not perfectly
correlated produces an additional small return on top of the
weighted-average return of the components. This is the **rebalancing
premium**, sometimes also called *volatility harvesting* or the
*Shannon's Demon* effect after Claude Shannon's coin-flip thought
experiment.

The mechanism is mechanical and survives the absence of any
forecasting skill. When stocks rise and bonds fall, the rebalance
sells some stocks at the higher price and buys some bonds at the
lower price. When the move reverses, the rebalance sells bonds at
the new high and buys stocks at the new low. Each round trip
extracts a small profit purely from the *path* of the prices, not
from any view about their *level*.

The size of the premium scales roughly with the variance of the
spread between the two assets and inversely with their correlation:

$$ \text{premium} \approx \tfrac{1}{2} \, w_1 w_2 \, (\sigma_1^2 + \sigma_2^2 - 2\rho\sigma_1\sigma_2) $$

For a 60/40 of US stocks ($\sigma=16\%$) and US Treasuries
($\sigma=6\%$) at correlation $\rho = -0.3$, the premium works out
to about 0.30% per year. That is a real number, but it is small
relative to the equity risk premium itself ($\sim 4-6\%$). It is
**not** the reason to rebalance. The reason to rebalance is risk
control. The premium is a lagniappe.

Two pieces of fine print on the premium. First, it disappears as
the correlation moves toward +1, which is exactly what happened
in 2022 (see §2.6). Second, it is small enough that *transaction
costs and taxes can eat all of it*, particularly in a taxable
account with frequent rebalancing.

#### 2.4 Tax Drag — Why You Mostly Don't Want to Sell

Every rebalance trade in a taxable account is a potential
realisation of capital gains. If your stock sleeve has doubled
before the rebalance, the sale of the overweight stock realises
that gain at long-term capital-gains rates — currently 15% to 23.8%
for most US filers, including the net-investment-income tax. A 0.3%
rebalancing premium is wiped out by a single realisation event with
a meaningful unrealised gain.

The hierarchy of tax-aware rebalancing is, in increasing order of
desirability:

1. **Sell-to-rebalance in a taxable account.** Worst case. Realises
   gains, locks in tax. Use only when no other lever works.
2. **Sell-to-rebalance with tax-loss harvesting.** Pair the sale of
   appreciated overweight assets with the sale of any genuinely
   underwater positions to offset gains. Acceptable, but requires
   active record-keeping.
3. **Direct new contributions.** Funnel monthly cash inflows into
   whichever sleeve is below target. No realisation, no tax. This
   is the right answer for any investor still in the accumulation
   phase, and it is enough to keep most portfolios within a few
   percent of target indefinitely.
4. **Rebalance in tax-advantaged accounts only.** If your full
   portfolio is split across IRA, 401(k), and taxable brokerage,
   the rebalance trades happen *inside* the IRA where all gains
   are tax-deferred, while the taxable account holds whichever
   slice of the allocation needs the least turnover (typically the
   long-term equity sleeve).
5. **Use dividends and interest.** In retirement, the cash thrown
   off by the bond sleeve and dividend stocks naturally lands in
   cash. Direct that cash to whichever sleeve is below target
   before reinvesting on autopilot.

For most readers of this course, the working answer is a
combination of (3) during the working years and (4) once
contributions slow. (1) is reserved for the quinquennial cleanup
when bands have stretched too far for contributions alone to fix.

#### 2.5 The Mechanics of Why It Works When the Investor Does Not

Keynes' warning: **the market can stay irrational longer than you
can stay solvent.** The polite version of that statement; the
impolite version is that *you* will turn irrational first, and the
market will then continue running until you have liquidated at the
worst possible moment. Every behavioural-finance study from the past
forty years says the same thing: individual investors, on average,
sell after declines and buy after rallies. The same ones. The same
direction. Every time.

A rebalancing rule does the opposite. In March 2009, with the S&P
down 56% from its 2007 high, the textbook 60/40 rebalancer was a
mechanical buyer of stocks at the cycle low. They did not have a
view. They did not call a bottom. They were *forced* by the rule
to top up the bond-heavy portfolio with cheap equity. Five years
later that purchase had doubled.

In December 2021, with the S&P up 28% on the year and bonds soft,
the same rebalancer was a mechanical seller of stocks at what turned
out to be a cycle peak. Again no view, no call. The rule sold; the
investor did not have to summon courage they did not possess.

This is why we run a rule. Not because the rule is smart. Because
*we* are not, in the moments that matter most.

#### 2.6 The 2022 Dilemma — When There Is Nothing to Rebalance Into

The neat machinery breaks when both assets fall together. In 2022
the S&P 500 returned −18.1%, the 10-year Treasury returned −17.8%,
and the 60/40 portfolio finished at roughly −18.0%. The naive
rebalancer asks: do I sell stocks to buy bonds, or sell bonds to
buy stocks? Both are down nearly equally. There is no winner to
trim and no loser to top up.

The mechanical answer is unsatisfying but correct: **rebalance
back to target weights anyway.** If at year-end you sit at, say,
59% stocks and 41% bonds (because stocks fell slightly less in
total return after dividend reinvestment), trim 1% off bonds and
buy 1% of stocks. The trade is small and the rebalancing premium
that year is essentially zero, but you are still placing the
correct trade for the *next* year. A regime change in the
correlation does not change the rule; it just changes the size of
the premium the rule earns.

The deeper lesson from 2022 is the one Week 4 already foreshadowed:
when stocks and bonds are positively correlated, neither sleeve
is hedging the other, and the rebalancing premium falls toward
zero. The practical response is not to abandon the rule but to
broaden the asset menu — the barbell shape of more
cash, some gold, an equity tilt, and an asymmetric speculative
sleeve has a higher cross-asset variance to harvest from in the
inflation regime than the classic two-asset 60/40 does.

The interactive lab below lets you choose the target stock weight,
the band width (or "calendar only" mode), and the starting year, and
plots both the weight drift and the wealth path. Watch the
rebalance-events count and the total turnover when you flip from a
1% band to a 20% band. Watch what 2022 does to the wealth path.
That is the lesson.

---

### 3. Common Misconceptions

**Misconception 1: "Rebalancing always increases return."**

It does not. The rebalancing premium is small (typically 0.1%–0.4%
per year for a 60/40 of stocks and bonds) and disappears entirely
when the correlation between the two sleeves runs positive. The
*reason* to rebalance is risk control, not return enhancement.

**Misconception 2: "More frequent rebalancing is better."**

There is essentially no difference in long-run outcomes between
quarterly, semi-annual, and annual rebalancing on a stock-bond
portfolio. Daily or weekly rebalancing is actively worse because
trading costs and bid-ask spreads dominate the negligible
incremental premium. Annual is the institutional default for a
reason.

**Misconception 3: "Threshold rebalancing always beats calendar."**

In tax-deferred accounts with no transaction costs the band
approach has a slight edge in violent years and a slight lag in
calm ones. Net of fifty years it is a wash. The choice is mostly
a matter of operational preference.

**Misconception 4: "Rebalancing is market timing."**

It is the opposite of market timing. Market timing forms a view
on near-term direction. Rebalancing has no view; it mechanically
restores a fixed target. The two strategies do opposite trades at
exactly the moments they disagree.

**Misconception 5: "If the rule says to sell my winners, I am
giving up alpha."**

A position that grew because of an idiosyncratic alpha source
is a position you should consider sizing through a
*conviction* lens, not a strict 60/40 lens. But the moment you
treat a holding as part of the 60/40 sleeve, the rebalance applies.
Mixing the two — calling the rebalance off because "I still believe
in this stock" — is how taxable accounts end up at 90/10 four years
later.

**Misconception 6: "Rebalancing is expensive."**

In a tax-deferred account with commission-free ETFs (the modern
default) the cost is essentially zero. In a taxable account it can
be material if done incorrectly; with contributions-based
rebalancing it can still be near zero. The cost is a function of
*how* you rebalance, not *whether* you do.

**Misconception 7: "I should not rebalance during a bear market."**

This is the most expensive misconception on the list. The bear
market is exactly when the rebalance trade is most valuable —
because that is when you are buying the lower-priced asset.
Investors who suspended rebalancing in 2008–09 and resumed in 2010
locked in a permanent underperformance against rule-followers.

**Misconception 8: "I should rebalance when something dramatic
happens in the news."**

News is a poor trigger. By the time something is dramatic, the
asset prices have already moved and the rebalance trigger (calendar
or threshold) has either already fired or has not. Trade the rule,
not the headline.

**Misconception 9: "Tax drag makes rebalancing not worth it in a
taxable account."**

Untrue if you use new contributions to redirect inflows toward the
underweight sleeve. The rule is the same; the implementation is
just less invasive. The argument only holds for someone who has
fully stopped contributing and has no tax-advantaged account in
which to do the rebalance trades.

**Misconception 10: "Rebalancing destroys the rebalancing premium
in 2022-style years."**

In a year where both assets fall together the premium that year is
essentially zero, regardless of whether you rebalance or not.
Rebalancing does no harm; it just earns no premium that year.

---

### 4. Q&A

**Q1: What is the optimal rebalancing frequency?**

A: For tax-deferred accounts, annual is the conventional answer
and dominates by simplicity. For taxable accounts, *event-driven*
rebalancing — only when a 5%–10% band has been breached — minimises
realisations. Either is fine. The least good answer is "monthly,"
which adds friction without adding return.

**Q2: What is the right band width for threshold rebalancing?**

A: 5 absolute percentage points around the target is a standard
default for a 60/40. 10pp is reasonable for an investor who values
inactivity. 1pp is too tight — the band fires constantly and the
turnover eats the premium. The choice depends on tax cost and
brokerage friction more than on theory.

**Q3: Should I rebalance my 401(k), my IRA, and my brokerage
account separately or jointly?**

A: Jointly. Treat the *household* portfolio as one allocation.
Place the high-turnover trades inside the IRA or 401(k), where they
are tax-free, and keep the taxable account as the long-term
buy-and-hold sleeve. This single decision saves more in lifetime
taxes than nearly any other portfolio choice.

**Q4: Can I just rebalance with new monthly contributions and never
sell anything?**

A: Yes, as long as the contributions are large relative to the
drift. A working professional contributing 15% of salary into a
balanced portfolio rarely needs to do a sell-rebalance trade in
the accumulation phase. Once contributions slow (retirement, sale
of a business), supplementary calendar or band rebalancing kicks in.

**Q5: What about rebalancing in a year like 2022 when both assets
fell?**

A: Trade the rule. The premium that year is near zero, but the
trade still positions you correctly for the *next* year. Skipping
the rebalance is a discretionary act and exactly the kind of
discretion the rule exists to prevent. (See §2.6.)

**Q6: Does rebalancing make sense for a 100% stock portfolio across
many ETFs?**

A: Yes — the same logic applies between sleeves of stocks (US large,
international, small cap). The premium is smaller because the
sleeves are more correlated, but the discipline of restoring target
weights still works. Once a year is plenty.

**Q7: What if I have a position with a strategic conviction — say,
a single stock I believe will continue compounding — that has now
drifted to 30% of my portfolio?**

A: Two answers. (1) Then it is *not* part of your 60/40 allocation
sleeve; it is a concentrated active position, and you should
account for it separately. (2) Concentration risk in a single name
above 10% of household wealth is its own problem (we cover it in
Week 21). The rebalancing rule applies to the *passive* sleeves; a
conviction trade lives outside them and is sized by a different
process.

**Q8: How does the rebalancing premium compare to other "free
lunches" in investing?**

A: It is among the smallest. The factor premia (size, value,
momentum) historically delivered 1%–3% annualised; the volatility
risk premium (Week 47) delivered 2%–4%; the equity risk premium
itself delivered 4%–6%. The rebalancing premium at 0.1%–0.4% is
real but minor. Frame it correctly: it is the icing, not the cake.

**Q9: Is there a "wrong" rebalance trade?**

A: Yes — a partial rebalance that just trims the most-overweight
sleeve down to the upper band but does not bring it back to target.
That preserves drift in the same direction it already had and
captures none of the premium. If you are going to rebalance, go to
target; if you are not, do not rebalance. The middle ground is
operationally the worst of both worlds.

**Q10: What does Horace personally do?**

A: A January calendar rebalance for the IRA sleeve (auto-rebalanced
by the broker, cost: zero, time: zero), contributions-based
rebalancing for the taxable equity sleeve, and a 10pp band check
for everything in between, fired only if the January look-through
shows the portfolio out of the band. The total annual time
commitment is under an hour. Anything more complex is a hobby, not
a portfolio.

**Q11: How does this connect to the rest of the course?**

A: Rebalancing is the operational layer underneath every
allocation we have introduced or will introduce — 60/40 (Week 4),
the diversified mixes (Week 5), the factor sleeves (Week 23), the
barbell (Week 14), the long-volatility overlay (Week 47). Pick an
allocation, pick a rebalance rule, and the rest of the course is
about choosing the right allocation. The rebalance rule is the part
you decide once and never revisit.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Rebalancing — The Boring Discipline That Makes 60/40 Actually Work | Week 7

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** This week is the most boring lesson in the course, and
it is also the one that does the most work for you. Rebalancing.
Setting a target allocation, and then once a year — or once a band
has been breached — trimming what has done well and topping up
what has done poorly.

**Stella:** Why is it boring?

**Horace:** Because it is mechanical. There is no view. No
forecast. No story. You set a 60/40 target and a year later the
portfolio is at 65/35 and you sell 5% of stocks to buy 5% of bonds.
That is the entire procedure.

**Stella:** And that is the whole alpha?

**Horace:** That is not even alpha. That is risk control. The alpha
piece — what people call the rebalancing premium — is real but
small. The reason to do it is to stay in the portfolio you actually
chose, instead of drifting into a portfolio you didn't.

---

**[SEGMENT 1: DRIFT]**

[VISUAL: image/week07_drift.png]

**Horace:** Look at the top panel. 100,000 dollars, 60/40, January
2010. We do nothing for ten years. Stocks compound at 13.6% a year
through the decade, bonds at about 3.7%. By December 2019 the
portfolio is at 78/22.

**Stella:** That's an eighteen-percentage-point drift.

**Horace:** Right. The investor who started with a balanced
portfolio in 2010 ended the decade running an aggressive one. They
did not consciously decide to add stock risk. The market did it for
them. And then in March 2020, the COVID crash hits, and that
drifted portfolio drops more than the rebalanced one would have, on
a much bigger asset base.

**Stella:** And the bottom panel?

**Horace:** Same starting portfolio, same returns, but every January
the investor trims back to 60/40. The stock weight oscillates
within two or three percentage points of 60% all decade. The
absolute wealth path is almost identical to the no-rebalance one —
in a calm decade rebalancing barely changes the return — but the
risk profile is exactly the one the investor chose.

---

**[SEGMENT 2: CALENDAR VS THRESHOLD]**

[VISUAL: image/week07_method_comparison.png]

**Horace:** This bar chart compares four policies on the full
1928 to 2024 dataset. Never rebalance. Annual rebalance. Semi-annual.
And a 5% band — meaning you only rebalance when one sleeve is more
than five points off target.

**Stella:** What jumps out?

**Horace:** Two things. First, the three rebalanced policies all
finish within about a tenth of a percent of each other on
geometric return. The choice between annual, semi-annual, and 5%
band is operational, not financial.

**Stella:** And the never-rebalance bar?

**Horace:** Higher absolute return, but realised volatility about
16% versus 12% for the rebalanced policies. The extra return is an
artefact — by the end of ninety-six years the never-rebalance
portfolio is almost 90/10. That investor is not running 60/40.
They are running an aggressive equity portfolio that drifted there
over a lifetime.

**Stella:** And the practical advice?

**Horace:** Pick one. Annual is the simplest. The 5% band is fine
if you want to pay attention less often. Both work. Don't
over-engineer the rule.

---

**[SEGMENT 3: THE REBALANCING PREMIUM]**

**Horace:** When you sell the asset that just outperformed and buy
the one that just underperformed — over and over, for thirty years
— the *path* of the prices generates a small additional return on
top of the weighted-average return of the components. That is the
rebalancing premium.

**Stella:** Where does it come from?

**Horace:** Pure mean reversion. Each round trip — sell stocks high,
buy bonds; later sell bonds high, buy stocks — extracts a small
profit purely from oscillation. For a 60/40 of stocks and bonds at
correlation negative 0.3 the premium is about 0.3% per year.

**Stella:** Three tenths of one percent.

**Horace:** Right. Real. But small. Frame it correctly: the equity
risk premium is four to six percent. The factor premia are one to
three. The rebalancing premium is icing, not cake.

**Stella:** And it disappears when correlation goes positive.

**Horace:** Like 2022. We will get there.

---

**[SEGMENT 4: TAX]**

**Horace:** In an IRA or 401(k), the rebalance trade is free. In a
taxable account it is a realisation. Fifteen to twenty-three percent
of the gain, gone. A 0.3% premium does not survive that on its own.

**Stella:** So how do real people do it?

**Horace:** Hierarchy. First — direct new contributions to whichever
sleeve is below target. No sale, no tax. Second — rebalance inside
the IRA, where the trades are tax-free, and let the taxable account
hold the long-term buy-and-hold sleeve. Third — pair sales of
appreciated assets with sales of underwater positions to harvest
losses. Fourth, last resort, a clean-up sale-to-rebalance once a
year if the bands have stretched too far.

**Stella:** What about a retiree without contributions?

**Horace:** Then the dividends and bond coupons land in cash, and you
direct *that* cash to whichever sleeve is below target. Same logic,
different fuel.

---

**[SEGMENT 5: WHY HUMANS CAN'T DO THIS]**

**Horace:** The Keynes line. The market can stay irrational
longer than you can stay solvent. And the corollary nobody wants to
hear is — *you* will turn irrational first.

**Stella:** Meaning?

**Horace:** Every behavioural finance study from the last forty
years says the same thing. Retail investors, on average, sell after
declines and buy after rallies. Same direction, every time. The
exact opposite of what they should be doing.

**Stella:** And rebalancing fixes that?

**Horace:** It does the opposite trade for you, mechanically. March
2009. S&P down 56% from its 2007 high. Every fibre of the human
investor is screaming sell. The 60/40 rule says: portfolio is at
50/50, you need to buy 10% more stocks. The investor does not have
to find courage they don't possess. The rule places the trade.

**Stella:** And five years later?

**Horace:** That purchase had doubled. Not because the investor
called the bottom. Because the rule is dumb enough to buy into a
panic.

---

**[SEGMENT 6: 2022]**

**Horace:** Now the harder case. 2022. Stocks down 18%. Bonds down
17.8%. There is no winner to sell. There is no loser to buy. The
neat machinery breaks.

**Stella:** What do you do?

**Horace:** Trade the rule anyway. If you are at 59/41, do the small
rebalance back to 60/40. The premium that year is essentially zero.
The point is not to earn the premium that year. The point is to set
up the *next* year.

**Stella:** So 2022 doesn't change the rule.

**Horace:** It changes the *expected return* of the rule. When
correlations turn positive — like in the 1970s, like in 2022 — the
rebalancing premium falls toward zero. That is a regime fact. The
response is not to abandon rebalancing. The response is to broaden
the asset menu — barbell shape, more cash, some gold, some
asymmetric speculation — so there is more cross-asset variance to
harvest from. We cover that in Week 14.

---

**[OUTRO]**

**Horace:** Pick an allocation. Pick a rebalance rule. Stick to it
for thirty years. The rule does the work the human cannot do alone.
That is the whole lesson.

**Stella:** And the interactive?

**Horace:** Three sliders. Stock weight target. Band width — or flip
to calendar-only. Starting year. The chart shows you the weight
drift and the wealth path. Watch what happens to the rebalance
count when you go from a 1% band to a 20% band. Watch what 2022
does. Slide it.

---

**END SCREEN:** "Next: Week 8 — Asset Location and Tax Optimisation"
