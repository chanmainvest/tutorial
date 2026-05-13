# Week 24: Multi-Strategy — Combining Beta, Factor, and Alpha Sleeves into One Book

---

## Part 1: Reading Section

---

### 1. Why This Is Important

This is the L2 capstone. For twenty-three weeks the course has been
handing you parts. Beta in week 4. Factor tilts in week 23.
Long/short alpha in week 13. Sector rotation in week 16. Tactical
overlays in week 10 and week 18. This week is where you put them
back together into one book that you actually run.

You need this synthesis lesson for four reasons.

1. **Most retail investors who try to combine strategies do it
   wrong.** They stack five 100%-equity ideas — total market plus
   value tilt plus dividend tilt plus mega-cap growth plus
   "concentrated picks" — and call the result "diversified." It
   isn't. It is one big beta book with five different fee structures.
   True multi-strategy means combining return drivers that are
   *fundamentally different* — broad market beta, smart-beta factor
   premia, and market-neutral alpha — not five flavours of the same
   beta exposure.

2. **The institutional template is well-defined and worth
   imitating — partially.** Endowment-style allocators run roughly
   70-80% beta + 10-15% smart beta + 10-15% absolute return. The
   structure is sound; the *implementation* is what most retail
   investors cannot replicate without paying themselves into the
   ground in fees. The L2 question is which pieces translate down
   to a six-figure retail book and which pieces should stay on the
   institutional cutting-room floor.

3. **Alpha is rare and most retail should not pursue
   it.** This lesson is honest about that. The default
   recommendation will be that 80% or more of you should run pure
   beta — week 4's 60/40 or week 12's lifecycle archetypes — full
   stop. The multi-strategy template is for the 10-20% who have the
   temperament, the time, and the size to run an alpha sleeve *and*
   the discipline to stop running it when it doesn't work.

4. **The four-tranche framework reapplies one level up.**
   In week 16 the four tranches were sector-cycle exposures. Here
   they are *strategy* exposures: beta (the physical / index core),
   smart beta (the seniors — established factor premia), alpha (the
   juniors — earned by skill), and tactical / discretionary (the
   exploration tier — the sleeve where things get interesting and
   risky). Same shape, different domain.

This week pulls together everything. There is one new chart — the
sleeve-breakdown stacked bar — and one new tool — the strategy
blender that lets you size each sleeve and see the resulting
expected return, vol, and Sharpe in real time. The lesson is short
on new theory and long on synthesis.

---

### 2. What You Need to Know

#### 2.1 The Three (Plus One) Sleeves

A multi-strategy book has up to four sleeves. Knowing which is
which keeps you honest about what each piece is being paid to do.

| Sleeve | Return driver | Typical vehicle | Expected return | Expected vol | Fee budget |
|---|---|---|---:|---:|---:|
| **Beta** | The market itself | VTI + BND, or 60/40 | ~7% nominal | ~10-12% | 0.03-0.05% |
| **Smart beta / factor** | Persistent factor premia (value, momentum, quality) | VLUE, MTUM, QUAL, AVUV | ~8-9% (~1-2% over beta) | ~13-15% | 0.15-0.30% |
| **Alpha** | Manager / process skill — market-neutral | L/S equity, merger arb, market-neutral funds | ~3-5% absolute | ~3-5% | 1-2% (often plus performance fee) |
| **Tactical** | Discretionary regime / sector / cycle bets | Sector ETFs (XLE, XLF, …), CTA-style trend | wide range, often 0% net | 8-15% | 0.10-1.0% |

Two structural things to internalise.

**Beta is the cheapest return on the table.** Forty years of
index investing have paid most of the bill. Every
dollar you move out of beta into a more expensive sleeve has to
*earn its fee* — net of every cost — before it has earned a right
to be in your book.

**Alpha is uncorrelated, not high-return.** The reason institutional
shops pay 2-and-20 for absolute-return strategies is *not* because
those strategies have a higher expected return than equities. They
do not. The math works because the alpha sleeve has near-zero
correlation to the rest of the book — a 3% return at 4% vol with
zero correlation to a 7% / 16% beta book lifts the *portfolio*
Sharpe materially even though the alpha sleeve in isolation has a
worse return than equity index.

#### 2.2 The Institutional Template — Why 70/10/10/10 Works

Yale, Harvard, the Norwegian sovereign wealth fund, the Canada
Pension Plan, every large endowment-style allocator converges on
roughly the same shape:

| Sleeve | Target weight | Why this size |
|---|---:|---|
| Beta (broad equity + duration) | 70-80% | Cheapest expected return, the baseline you are trying to beat |
| Smart beta / factor tilts | 10-15% | Documented premia, low fees, scalable, low alpha-decay risk |
| Absolute-return (alpha) | 10-15% | Diversifier, lifts Sharpe via low correlation, not via high return |
| Tactical / opportunistic | 0-5% | Discretionary overlays the CIO actually has conviction on |

The interactive at the bottom of this lesson lets you set these
weights and see the resulting expected return and Sharpe.

The reason the institutional template is *this* shape and not, say,
50/25/25 is governance. Even a very smart investment team only has
so many high-conviction views per year. Pushing the alpha sleeve
above 15% means either taking discretionary bets the team does not
have, or paying performance fees on capital they can't deploy
profitably. The 70-80% beta core is the honest admission that even
sophisticated allocators cannot beat the market with most of their
capital. The 10-15% alpha sleeve is the part where they think they
can.

#### 2.3 Translating to Retail — The 80/10/10 Default

The institutional template translates to retail with one important
modification: the alpha sleeve is **harder** to run with a
six-figure book than with a six-billion-dollar book. The retail
equivalent is not "find a hedge fund." It is one of three things:

1. **A market-neutral mutual fund or ETF** (BTAL, MERFX, FTLS).
   The cleanest way to express the alpha sleeve at retail. Fees
   are 1-2%, returns are 2-4% over rolling 5-year windows, and
   the correlation to SPX is genuinely low.
2. **A concentrated long-only sleeve** (5-15 names you actively
   research, sized 1-3% each). Strictly speaking this is a
   high-active-share equity sleeve, not market-neutral alpha. It
   works only if you actually have the edge — alpha is rare.
3. **A defined long/short pair book** (pair trades from week 14,
   plus an overlay or two). Real alpha, but takes time to manage
   and a margin account.

The default retail multi-strategy template:

| Sleeve | Weight | Vehicle | Approx fee |
|---|---:|---|---:|
| Beta — broad US equity | 60% | VTI | 0.03% |
| Beta — bonds | 20% | BND or short-duration treasuries | 0.03% |
| Smart beta — factor tilt | 10% | One of VLUE, MTUM, QUAL, AVUV | 0.15-0.25% |
| Alpha sleeve | 10% | Concentrated long picks **or** a market-neutral fund | 0.5-2% |

If you cannot articulate a thesis for the factor tilt and the alpha
sleeve, both go to zero and you run a 75/25 split between VTI and
BND. That is not a failure. That is the honest answer. Most people
don't have alpha; nothing in this lesson is arguing they should
pretend they do.

The image below shows this template alongside four other archetypes
(conservative, moderate, aggressive, institutional, FIRE-style
barbell). Each row is one archetype's sleeve breakdown.

![Stacked horizontal bar chart of five archetype multi-strategy portfolios. Conservative (90% beta, 0% factor, 0% alpha, 10% cash). Moderate (80% beta, 10% factor, 5% alpha, 5% cash). Aggressive (65% beta, 15% factor, 15% alpha, 5% cash). Institutional (70% beta, 15% factor, 13% alpha, 2% cash). FIRE / barbell (70% beta, 5% factor, 10% alpha, 15% cash). Bars segmented in site palette colours; legend at the bottom; x-axis 0-100%.](image/week24_sleeve_breakdown.png)

#### 2.4 What Each Sleeve Actually Adds — The Layered-Returns View

The arithmetic of a multi-strategy book is simpler than it looks.
Expected portfolio return is the weighted sum of sleeve expected
returns; expected vol is the matrix calculation of weighted vols
adjusted for correlations. The intuition is in the pieces.

For the moderate retail template above (80% beta / 10% factor /
10% alpha / 0% cash), with assumptions of 7% beta return, 9%
factor return (7% beta + 2% factor premium), 4% market-neutral
alpha:

```
Sleeve contribution to portfolio return:
  Beta sleeve:    80% × 7%  = 5.60% (gross)
  Factor sleeve:  10% × 9%  = 0.90% (gross)
  Alpha sleeve:   10% × 4%  = 0.40% (gross)
                  -------
  Gross return:             = 6.90%
  Less fees:
    Beta fee 0.04% × 80%    = -0.03%
    Factor fee 0.20% × 10%  = -0.02%
    Alpha fee 1.50% × 10%   = -0.15%
                  -------
  Net return:               = 6.70%
```

Compare that to the all-VTI 100% beta book: 7% gross, 7%-0.04% =
6.96% net. The multi-strategy version is **0.26% per year worse on
expected return** before any benefit from correlation. The benefit
shows up in volatility:

```
Vol of all-VTI (one sleeve, vol=16%):                  16.00%
Vol of moderate template (corr beta-factor=0.95,
   beta-alpha=0.05, factor-alpha=0.10):               ~12.85%
```

That is the bargain. A 0.26% return concession in exchange for a
3-percentage-point drop in vol. Sharpe goes from ~7%/16% = 0.44 to
~6.7%/12.85% = 0.52. The portfolio is *better* despite earning
less in raw return — because the alpha sleeve does its
diversification job and the factor sleeve nudges the expected
return up enough to mostly offset its own fee.

The image below decomposes the layered returns for four archetypes.

![Four-archetype stacked bar chart of expected return decomposition. Each bar shows beta contribution (largest, blue), factor add (gold, smaller), alpha add (green), and fee drag (red, plotted negative). Net return shown as a black tick mark. Conservative bar nets to ~5.5%; moderate to ~6.7%; aggressive to ~6.4%; institutional to ~6.5%. The aggressive and institutional portfolios pay back more in fees but contribute more from the alpha and factor sleeves.](image/week24_layered_returns.png)

The point of the image: **most of the return comes from the beta
sleeve, regardless of how clever the other sleeves are.** Factor
adds a couple of dozen basis points. Alpha adds another couple of
dozen. Fees take back roughly half of that. The net win is on the
order of zero to 30 bps of expected return — and the entire reason
to do it is the *vol* improvement, not the *return* improvement.

#### 2.5 Why Most Retail Investors Should Not Do This

Alpha is rare. Most retail investors who set up a
multi-strategy book make at least one of the following mistakes.

1. **They run an alpha sleeve they don't have alpha in.** If your
   long-short P&L over three years is not statistically distinct
   from zero — and at retail size it almost never is — you are
   paying real fees and real attention for a return drag.
2. **They confuse complexity for diversification.** Owning ten funds
   does not mean ten return drivers. Three of them might all be S&P
   500 in different costumes.
3. **They cannot stop.** When the alpha sleeve underperforms by 3%
   in one year, the discipline is to keep running it (or to shut it
   down on a pre-defined criterion). Most retail will do neither —
   they double down or panic-shut, both wrong.
4. **They underestimate the tax cost.** Alpha sleeves turn over
   more than beta sleeves. At 30%+ marginal tax brackets, the tax
   drag is often larger than the gross alpha edge.

The honest decision tree:

- Do you have a multi-six-figure book and meaningful free time
  every week to manage it? If not, run pure beta. Stop.
- Do you have a pre-committed statistical criterion for "the alpha
  sleeve is not working, shut it down"? If not, you do not have a
  sleeve, you have a hobby.
- Are you tracking after-fee, after-tax, after-time-cost
  performance — not gross? If not, see point 1.

If all three answers are yes, the template in §2.3 is reasonable.
If any answer is no, week 24 was the lesson where you should have
put the multi-strategy book down. That is not a failure. The same
humility that keeps L1 graduates wealthy is what sends most
L2 dabblers home with less than they started with.

#### 2.6 The Four-Tranche Framework Reapplied

In week 16 the four tranches were *sector-cycle* exposures —
physical, senior, junior, exploration — staged through a commodity
bull market. Here the same shape reappears one level up, applied
to *strategies* themselves.

| Tier | Sector cycle (week 16) | Strategy stack (this week) |
|---|---|---|
| **Physical** | The commodity itself | The market — broad-index beta |
| **Senior** | Established producers | Smart beta — documented factor premia |
| **Junior** | Mid-tier producers | Alpha — market-neutral skill sleeves |
| **Exploration** | Pre-revenue speculators | Tactical — discretionary regime / sector bets |

The lesson is the same in both directions. The bulk of your money
sits in the lowest-vol, most-liquid, most-fundamental tier
(physical / beta). Each higher tier is smaller, more
skill-dependent, more vol-rich. The exploration / tactical tier is
where the fun is and where most of the blow-ups happen, and you
size it as a fraction of your book that you can lose entirely
without changing your life. The pyramid shape — wide base, narrow
top — is the robust shape. The inverted pyramid — most of the book
in the exploration tier — is how the market staying irrational
longer than you can stay solvent becomes a personal
autobiography.

The barbell is a special case of this pyramid where the
"mid" tiers (factor and alpha) collapse to near-zero and the book
splits between the safest (cash + bonds) and the most aggressive
(concentrated long or alpha) sleeves. A FIRE-curious investor with
high human-capital risk often runs this shape: 30% cash + 50% VTI
+ 20% concentrated names. That is not multi-strategy in the
institutional sense, but it is a coherent strategy stack — and an
honest one for the situation.

---

### 3. Common Misconceptions

1. **"More sleeves means more diversification."** Not unless the
   sleeves have low cross-correlation. Five flavours of US equity
   is not five sleeves; it is one sleeve in five wrappers.

2. **"Alpha sleeves boost returns."** They lift Sharpe via lower
   correlation, not higher return. The alpha sleeve usually has a
   *worse* expected return than the beta sleeve.

3. **"The fee is worth it if the manager is good."** True only if
   net-of-fee, net-of-tax, net-of-correlation alpha is positive.
   Most active management fails at least one of these tests.

4. **"Smart beta is alpha."** No. Smart beta is a documented factor
   premium (value, momentum, quality, low-vol). It is a beta to a
   *factor*, not a manager-skill alpha. The fee should be 0.15-0.30%,
   not 1-2%.

5. **"Endowments beat the market because of alternatives."**
   Endowments beat 60/40 partly through alternatives, partly
   through illiquidity premia, and partly through scale. Retail
   investors get the alternatives without the illiquidity premium
   and without the scale, which is why retail "alts" funds usually
   underperform their institutional namesakes.

6. **"I'll just run my alpha sleeve until it stops working."** Most
   investors cannot tell when an alpha sleeve has stopped working
   versus when it is in a normal drawdown. Without a pre-committed
   criterion, "stops working" gets renegotiated indefinitely.

7. **"The institutional template is universally optimal."** It is
   optimised for institutional governance — long horizons, large
   size, professional management, performance fees that align
   incentives. None of those apply at retail. Copying the shape
   without copying the conditions is cargo-culting.

8. **"Market-neutral funds aren't really market-neutral."** Many
   aren't — their factor exposures and short-vol exposures show up
   as hidden beta in stress periods. Read the holdings. Look at
   the 2008, 2020, and 2022 drawdowns. If the fund moved with SPX
   in any of those, the "neutral" claim is suspect.

9. **"Tactical sleeves should be 30%+ if you have an edge."** They
   shouldn't, and you don't. Even managers with documented
   tactical edge size their tactical book at single-digit percent.
   The reason is governance: your conviction is over-stated and
   your hit rate is over-stated, and a smaller sleeve is the cheap
   correction.

10. **"Multi-strategy means you can't lose money."** It means you
    can lose less *in expectation* per unit of vol. In a stress
    period — 2008, March 2020 — correlations go to one and the
    multi-strategy book draws down nearly as hard as the beta book.
    The diversification works in normal times and fails exactly
    when you need it most. The vol tail wags the dog and the market
    stays irrational longer than you stay solvent — both live in
    those windows.

---

### 4. Q&A Section

**Q: How big does my book need to be before multi-strategy makes sense?**
A: Roughly $250k+. Below that, the fee drag and time cost dominate.
A $50k book with a 10% alpha sleeve is paying $75-150 a year on
$5,000 of capital — the fees ate the alpha before the trade started.

**Q: Should retirees run multi-strategy?**
A: Mostly no. The alpha sleeve adds vol uncertainty and tax drag at
exactly the wrong life stage. A retiree who wants the
diversification benefit should get it from bonds and TIPS (week 5,
week 18), not from a market-neutral hedge fund.

**Q: How do I pick the factor for the smart beta sleeve?**
A: Pick the one whose mechanism you can articulate in a sentence
and whose drawdown profile you have looked at. Value (VLUE, AVUV)
for sustained mean-reversion. Momentum (MTUM) for sustained
trend-following — but accept the 2009 / 2020 momentum crashes.
Quality (QUAL) for the lowest-fee, lowest-drawdown factor with the
weakest premium. Multi-factor (USMV, BAB) for diversification
across factors at the cost of factor purity.

**Q: Can I use leverage to amplify the alpha sleeve?**
A: Technically yes. Operationally no, unless you have run an
unlevered version through a stress period and survived. Markets
can stay irrational longer than your levered book can stay
solvent — that's the warning. Leverage on a strategy you don't
yet trust is the classic blow-up.

**Q: What's the simplest way to run the alpha sleeve at retail?**
A: A single market-neutral fund (BTAL, MERFX, FTLS, JNK-style
merger arb) at 5-10% of the book. Fee is high but predictable, the
correlation to equities really is low, and you don't have to make
trade-by-trade decisions.

**Q: Does this template work in 2026's market?**
A: The shape works; the inputs need updating. With T-bills at 4%+,
the cash sleeve is no longer a return drag — and the bond sleeve
yields more than it did in the 2010s. The alpha-sleeve hurdle is
correspondingly higher: a market-neutral fund returning 3% net
beats 5% cash by *negative* 200 bps. The cash hurdle changes the
arithmetic; revisit it whenever the front end re-prices.

**Q: How do I rebalance a multi-strategy book?**
A: Calendar rebalance once a year, plus a tolerance band (e.g.
re-balance if any sleeve drifts more than 5 percentage points
from target). Do not rebalance on intuition. Week 11 covers the
mechanics.

**Q: What if my alpha sleeve has a great year — should I increase it?**
A: No. Single-year performance has almost zero predictive content
for next year's alpha. The institutional discipline is to *reduce*
an alpha sleeve after a great year (because you've mean-reverted
closer to the cap on what you can deploy profitably), not increase
it.

**Q: How does this interact with US-only investability?**
A: Cleanly. The beta sleeve is VTI + BND, both US. The factor
sleeve is US-listed factor ETFs (VLUE, MTUM, QUAL). The alpha
sleeve uses US-listed market-neutral funds or US single-name
long/short. No part of the template requires foreign-listed
exposure, which keeps custody, tax, and disclosure clean.

**Q: How much time per week should I spend running this?**
A: Realistically, 2-4 hours per week if you are running an active
alpha sleeve, 30 minutes per month if the alpha sleeve is a single
market-neutral fund, and zero if you have decided to
run pure beta. Be honest about which bucket you are in.

**Q: What's the L3 version of this?**
A: L3 layers in derivatives — option overlays for tail hedging
(week 47), volatility arbitrage (week 49), and tax-aware
expression of the same exposures via options and margin. The L3
book has the same four-sleeve shape; it just expresses each
sleeve more capital-efficiently. L2 first.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Multi-Strategy Portfolios — How Endowments Layer Beta, Factor, and Alpha (and Why Most Retail Investors Should Not)

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**INTRO (0:00-1:30)**

[VISUAL: title card "Week 24 — Multi-Strategy: The L2 Capstone"]

**Stella:** Twenty-four weeks in. Horace, this is the week we promised would tie everything together.

**Horace:** It is. We've spent six months handing out parts. Beta in week four. Factor tilts in week twenty-three. Long-short alpha in week thirteen. Sector rotation in week sixteen. This week we put the parts back together into one book that you actually run. This is the L2 capstone.

**Stella:** And the headline warning — let's get it out of the way first.

**Horace:** Alpha is rare. The honest answer for most of you watching is that you should stop at the beta sleeve. Run VTI plus BND, rebalance once a year, go live your life. Everything else this episode covers is for the ten or twenty percent of L2 graduates who have the size, the time, and — most importantly — the discipline to run the more complicated book without lying to themselves about whether it's working.

**Stella:** Got it. With that on the table, let's start with the institutional template that everybody's trying to copy.

---

**SECTION 1 — THE THREE PLUS ONE SLEEVES (1:30-4:30)**

[VISUAL: image/week24_sleeve_breakdown.png]

**Horace:** Every multi-strategy book has up to four sleeves. Beta, smart beta, alpha, tactical. The bar chart on screen is five archetype portfolios — conservative, moderate, aggressive, institutional, and a FIRE-style barbell — each broken out by sleeve.

**Stella:** Walk through the institutional row.

**Horace:** Seventy percent beta. Fifteen percent factor. Thirteen percent alpha. Two percent cash. That's roughly the shape Yale, Harvard, the Norwegian sovereign fund, and the Canada Pension Plan all converge on. It's not a coincidence — they're all answering the same question with the same constraints.

**Stella:** Why does it converge on that shape?

**Horace:** Because beta is the cheapest return on the table. Three to five basis points for index access. Every dollar you move out of beta has to earn its higher fee net of correlation effects, and only the first ten or fifteen percent of a smart beta sleeve and the first ten or fifteen percent of an alpha sleeve do that math. After that, you're paying premium fees for diminishing diversification.

**Stella:** And the tactical row?

**Horace:** That's the discretionary overlay. The CIO's actual high-conviction views. It stays single-digit percent because no investment team has more than a few real convictions per year, and pretending otherwise is just expensive noise.

---

**SECTION 2 — TRANSLATING TO RETAIL (4:30-7:30)**

**Stella:** Now the honest part. Retail can't replicate Yale's alpha sleeve. So what does the institutional template actually look like at six figures?

**Horace:** Same shape, different vehicles. The default retail template is sixty percent VTI, twenty percent BND for your beta core. Ten percent factor — pick one, value or momentum or quality, don't stack three. Ten percent alpha sleeve — and at retail, alpha is one of three things: a market-neutral mutual fund or ETF, a concentrated long-only sleeve of names you actually research, or a defined long-short pair book.

**Stella:** Which of those three is most realistic?

**Horace:** For most people, the market-neutral fund. BTAL, MERFX, FTLS — names like that. Fees are one to two percent, returns are two to four percent over rolling five-year windows, correlation to SPX is genuinely low. You're not picking trades, you're paying a manager to do it, and the diversification benefit shows up in the portfolio Sharpe.

**Stella:** What about the concentrated long-only sleeve?

**Horace:** That works if you actually have an edge — alpha is rare. If you can articulate a thesis on five to fifteen names, size them one to three percent each, and you have time to keep up with them, that's a legitimate alpha sleeve. Most people who try this don't actually have the edge they think they have. Three years of P&L will tell you. If your concentrated sleeve isn't beating SPX after fees and taxes over a three-year window, the sleeve doesn't have alpha — it's a hobby.

---

**SECTION 3 — WHAT EACH SLEEVE ADDS (7:30-11:00)**

[VISUAL: image/week24_layered_returns.png]

**Stella:** This chart breaks expected return into contributions per sleeve. Walk us through it.

**Horace:** Four archetypes — conservative, moderate, aggressive, institutional. For each, the bar segments are: beta contribution, factor add, alpha add, and fee drag. The black tick is the net return.

**Stella:** And the surprise?

**Horace:** Most of the return comes from the beta sleeve regardless of the rest. Look at the moderate row. Beta contributes about five point six percent. Factor adds twenty basis points. Alpha adds forty basis points. Fees take back about twenty basis points. Net return is around six point seven, versus seven percent for pure beta minus four basis points fee — call it six point ninety-six.

**Stella:** So the multi-strategy version earns *less* on expected return?

**Horace:** Twenty-six basis points less. The trade isn't return, it's vol. The all-VTI book is sixteen percent annualised vol. The moderate template is roughly thirteen percent vol. You give up a quarter point of return for three points of vol, which lifts your Sharpe from zero point four-four to zero point five-two. That's the entire bargain.

**Stella:** And aggressive and institutional?

**Horace:** Same shape, more amplified. More fees paid, more diversification gained. Net return is roughly the same — that's not a coincidence either. After fees, after correlation, the spread between portfolios at the same risk-tier is small. The thing you're optimising is risk-adjusted return, not raw return.

---

**SECTION 4 — WHY MOST RETAIL SHOULD NOT (11:00-14:00)**

**Stella:** Let's get to the discipline part. Why most retail investors should not do this.

**Horace:** Four reasons, and they're not theoretical — they're what I see actually happen.

**Stella:** Number one.

**Horace:** They run an alpha sleeve they don't have alpha in. Three years of P&L is the test. If you can't beat the index after fees and taxes for three years, you don't have an alpha sleeve, you have an expensive hobby.

**Stella:** Number two.

**Horace:** They confuse complexity for diversification. Owning ten funds doesn't mean ten return drivers. I've seen retail books that look diversified on the dashboard and have correlation point nine to SPX in every drawdown.

**Stella:** Number three.

**Horace:** They can't stop. The alpha sleeve is doing badly, and the discipline is either to keep running it through the drawdown or to shut it down on a pre-defined criterion. Most retail does neither — they double down or panic-shut, both wrong, often in the same year.

**Stella:** Number four.

**Horace:** They underestimate the tax cost. Alpha sleeves turn over. Concentrated picks turn over. At a thirty-percent marginal bracket, the tax drag on a five-percent alpha sleeve eats one and a half percent of the gross. Compared to the buy-and-hold beta sleeve which defers everything indefinitely, alpha is fighting both fees *and* taxes. The fix is the same one that runs through the rest of the book — express what you can through long-dated options and margin so the tax timing works for you. It applies here as much as it does in the derivatives lessons.

---

**SECTION 5 — THE FOUR-TRANCHE FRAMEWORK REAPPLIED (14:00-15:30)**

**Horace:** The four tranches. We taught it as a sector-cycle framework in week sixteen — physical, senior, junior, exploration. The same shape reappears here, one level up, applied to strategies themselves.

**Stella:** Map them.

**Horace:** Physical is the market itself — the index, beta. Senior is smart beta — established factor premia. Junior is alpha — manager skill sleeves. Exploration is tactical — the discretionary overlay.

**Stella:** And the lesson?

**Horace:** The pyramid shape. Wide base, narrow top. Most of the money in the most fundamental, lowest-vol, lowest-fee sleeve. Each higher tier smaller, more skill-dependent, more vol. The exploration tier is where the fun is and where the blow-ups are, and you size it so you can lose the entire sleeve without changing your life. Inverted pyramid — most of the book in tactical — is how the market-can-stay-irrational-longer-than-you-can-stay-solvent line becomes your personal autobiography.

---

**SECTION 6 — THE INTERACTIVE (15:30-17:00)**

[VISUAL: switch to the interactive at course/interactive/week24_strategy_blender.html]

**Stella:** Tool of the week — the strategy blender.

**Horace:** Four sliders. Beta, factor, alpha, cash. Sum to one hundred. The page recomputes expected portfolio return, expected vol, and expected Sharpe in real time, with the fee drag on the alpha sleeve baked in. The point of the tool is for you to play with the trade-offs and confirm the intuitions from the chart — that the beta sleeve does most of the lifting, that the alpha sleeve buys vol reduction not return, and that pushing the alpha sleeve above twenty percent breaks the math because the fees overwhelm the diversification benefit.

**Stella:** Try the institutional preset and the FIRE preset.

**Horace:** Institutional — seventy beta, fifteen factor, thirteen alpha, two cash. Sharpe lands around zero point five-five. FIRE barbell — seventy beta, five factor, ten alpha, fifteen cash. Sharpe is similar, vol is materially lower, expected return is materially lower, because you're carrying that cash drag. Different optimum for different problem.

---

**OUTRO (17:00-18:00)**

**Stella:** Capstone wrap.

**Horace:** Three takeaways. One — the institutional template is real, well-defined, and translatable. Seventy to eighty percent beta, ten to fifteen smart beta, ten to fifteen alpha. Two — the math says most of the return comes from beta, and the alpha sleeve buys you vol reduction, not return. Three — most retail investors who try this lose the trade to fees, taxes, and the discipline gap. Alpha is rare; that's the rule. Don't run an alpha sleeve unless you have the size, the time, and the pre-committed shutdown criterion.

**Stella:** And next week?

**Horace:** Week twenty-five — the L3 launch. We start the derivatives material. Options. Futures. The toolkit for expressing all of this more capital-efficiently. The same four sleeves, expressed differently.

**Stella:** End-of-L2 milestone.

**Horace:** End of L2. If you've made it here, you have the toolkit to run a full multi-strategy book. Now spend a year *not* running one — run pure beta, watch your discipline, and come back to L3 only after you can prove you didn't blow up the simple version. The market can stay irrational longer than you can stay solvent. End the L2 with that one in your pocket.

[VISUAL: end card "Week 25 — L3 starts: Options I"]
