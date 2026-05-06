# Week 13: Long/Short — Relative Value, Alpha Extraction, and the Dollar-Neutral Book

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Up to this week the course has been about owning things. Long stocks,
long bonds, long the index, long whatever store of value you trust.
Long-only is the right default for almost every investor, and we have
spent twelve weeks defending it.

This week is the first week we add a second leg. Not "buy and hold
something else" — but **borrow it, sell it, and buy it back later**.
Shorting. The other half of the market.

You need this for four reasons.

1. **The mechanics are non-obvious and the asymmetry is real.** Long a
   stock, your loss is capped at 100% and your gain is unlimited.
   Short a stock, your *gain* is capped at 100% and your *loss* is
   unlimited. Most retail blow-ups in shorting come from people who
   do not internalise that asymmetry and size their shorts the same
   way they size their longs. The option tail wags the equity dog,
   and the asymmetric short squeeze is mostly a story about that
   dynamic. GameStop in January 2021 took a textbook-cheap short from
   $20 to $480 in three weeks and ended several professional
   short-only funds.

2. **Alpha mostly lives on the short side or in the spread.** The
   durable alpha sources are liquidity, sector rotation,
   long-term trends, and buying what passive has abandoned. None of
   those are pure long-only trades. Three of the four are spread
   trades — long the cheap leg, short the expensive leg, hold the
   relative-value position until convergence. If you only ever go
   long, you are systematically excluded from the trades where
   informed money actually earns its return.

3. **A dollar-neutral book is the cleanest way to test whether you
   have any edge at all.** When your long book and short book sum
   to zero net dollars and roughly zero net beta, the market direction
   washes out. What is left is your stock-picking. If your long-short
   spread compounds positively over a few years, you have alpha. If
   it does not, you do not — and you have spared yourself the
   embarrassment of confusing a bull market for skill.

4. **It sets up the next two weeks and the back half of the course.**
   Week 14 takes the same machinery and applies it to a single
   pair of stocks (pair trading). Week 49 applies it to volatility
   itself (vol arb). Week 23 (factors) and Week 47 (long-vol overlay)
   both rest on the long-short architecture you are about to learn.
   Without this lesson, the rest of the course's relative-value
   material has no foundation.

This is not a lesson telling you to start shorting tomorrow. Most of
you should not. It is a lesson teaching you the toolkit so that when
the course later points at a structural mispricing, you will know what
you are looking at.

---

### 2. What You Need to Know

#### 2.1 The Mechanics of a Short — Borrow, Sell, Buy, Return

A short sale is a four-step round trip.

1. **Borrow.** Your broker lends you 100 shares of XYZ. The broker
   sources those shares from another customer's margin account, from
   the firm's inventory, or from a third-party securities-lending
   desk. The lender is paid an ongoing fee (the *borrow rate* or
   *cost-to-borrow*).
2. **Sell.** You sell the borrowed 100 shares into the market at the
   current bid. The cash proceeds land in your margin account but are
   *not yours to spend* — they are pinned as collateral against the
   short.
3. **Buy back (cover).** Later — maybe a day, maybe a year — you buy
   100 shares in the market and use them to repay the lender.
4. **Return.** The borrowed shares are returned. Your P&L is
   `(sale price - cover price) * shares`, minus the cumulative
   borrow fee, minus any dividends that the lender was entitled
   to during the borrow window (the short pays them out of pocket;
   they do not come out of the collateral).

A few details that matter in practice. Brokers charge an annualised
borrow rate. For an *easy-to-borrow* (ETB) name like AAPL or SPY,
that rate is a few basis points. For a *hard-to-borrow* (HTB) name —
a small float, lots of demand to short, or stress in the borrow
market — it can be 5%, 20%, even 100% per year. A 50% borrow rate is
the market quietly telling you that the short side of the trade is
crowded and the cost of staying in it eats your return. Always check
the borrow rate before you short.

A second detail: short sales settle T+1 like long sales, but the
*locate* (proof that your broker has actually sourced the shares)
must be obtained before you transmit the sell order. Selling without
a locate is a *naked short*, which has been illegal in the US for
equities since 2008. If your broker gives you a green light, the
locate is in place.

#### 2.2 The Asymmetric Loss Profile and the Squeeze

This is the single most important paragraph in the lesson.

Long a $100 stock: best case it goes up 10x and you make $900 on
$100. Worst case it goes to zero and you lose $100. Loss is bounded.

Short a $100 stock: best case it goes to zero and you make $100 on a
$100 collateral commitment. Worst case the stock goes up 10x — and
you lose $900 on $100 of original margin. *Loss is unbounded above*.

Worse, the same move that makes you wrong also makes the position
*larger*. As the stock rises, your short grows from a $100 obligation
to a $300 obligation to a $1,000 obligation, and your broker raises
the margin requirement on the larger position. You are forced to
post more capital exactly when the trade has gone against you. This
is how short squeezes turn into forced covers — not by choice, but
by margin call.

The classic case study is GameStop, January 2021. Short interest
exceeded 100% of the float (technically possible because shares can
be re-lent). Retail traders coordinated through r/wallstreetbets to
buy calls; the dealers hedged by buying spot, the spot rallied, the
shorts were forced to cover into a vanishing supply, and the price
ran from $20 to $480 in three weeks. Melvin Capital, a $12 billion
hedge fund, lost roughly half its assets in that single month and
shut down a year later.

The lesson is not "never short." The lesson is **size shorts at a
fraction of how you size longs, set hard stops, and never short an
illiquid name with elevated short interest unless you have a
specific structural thesis for the cover**. The mechanism is
worth remembering — in the post-COVID options market, the option
tail wags the equity dog, and a coordinated retail call buy-program
is exactly the mechanism that lights the squeeze fuse.

The image below shows the four payoff diagrams side by side.

![Four payoff diagrams in a 2x2 grid: long stock (linear, unbounded upside, 100% capped downside), short stock (linear, 100% capped upside, unbounded downside), long call (capped loss at premium paid, unbounded upside), and long put (capped loss at premium paid, capped upside at strike). The diagram shows how options are a barbell-shaped reshaping of the stock payoff: capped downside, asymmetric upside.](image/week13_payoff_diagrams.png)

#### 2.3 Gross vs Net Exposure, Dollar-Neutral, Beta-Neutral

Two long-short funds with the same headline "long $100, short $100"
can still be very different animals. The vocabulary that resolves
the ambiguity:

- **Gross exposure** = `|long $| + |short $|`. The total amount of
  capital deployed in either direction. A fund with $100 long and
  $100 short has gross exposure of $200, or 200% of capital.
- **Net exposure** = `long $ - short $`. The directional bet. The
  same fund has net exposure of zero — *dollar-neutral*.
- **Net beta** = `Σ (w_i × β_i)` over both books. Even if dollar-net
  is zero, if your long book has β = 1.3 (high-beta growth) and your
  short book has β = 0.7 (low-beta staples), your *beta-net* is
  +0.6 — when the market rallies, your net exposure rallies *with*
  it. *Dollar-neutral is not beta-neutral.*

Three canonical configurations:

| Configuration | Gross | Net dollars | Net beta | Whose book |
|---|---:|---:|---:|---|
| Long-only | 100 | +100 | ~+1.0 | retail, mutual funds |
| **130/30** | 160 | +100 | ~+1.0 | enhanced-index hedge funds |
| **Market-neutral 100/100** | 200 | 0 | 0 (targeted) | classic L/S equity hedge fund |
| **Dollar-neutral pairs** | 200 | 0 | not constrained | stat arb, pair traders |

The 130/30 fund is a popular institutional product — go 130% long,
30% short, finance the short via the borrow proceeds, end up at
100% net long but with the ability to express short ideas. It is
mostly used to relax the "long-only" constraint that prevents an
index manager from underweighting a stock by more than its index
weight.

The market-neutral 100/100 book is what most people mean when they
say "L/S hedge fund." The fund manager picks longs and shorts in
roughly equal dollar amounts and tries to keep the net beta near
zero. The headline return is *spread alpha* — long book minus
short book — which should be uncorrelated to the market.

Pair trading is the same idea applied to one trade at a time: long
Coke, short Pepsi at the same dollar amount; long the cheap oil
major, short the expensive one. Week 14 covers the math.

#### 2.4 The Cost of Borrow — ETB vs HTB and Why It Matters

Every short carries a continuous holding cost. The borrow rate is
quoted as an annualised percentage of the position's market value
and accrued daily.

| Category | Typical borrow rate | Examples |
|---|---:|---|
| **General Collateral / ETB** | 0.25 - 1% / yr | SPY, QQQ, AAPL, MSFT, mega-cap names |
| **Modest specials** | 1 - 5% / yr | Mid-cap names with concentrated holders |
| **Specials / HTB** | 5 - 30% / yr | Small floats, recent IPOs, takeover targets |
| **Severe HTB** | 30 - 100%+ / yr | Stressed names, biotech binary events |

A 30% annual borrow rate is quietly devastating. If the stock you
shorted falls 20% over a year, you make 20%. Subtract 30% borrow,
plus any dividends paid through, and you have *lost* 10% on a
correct directional call. This is one of the cleanest examples in
all of finance of a structural cost killing an obvious-looking
trade. **The borrow market is informationally efficient: when an
ETB stock with a free borrow becomes a 50% HTB stock overnight,
the market is telling you the short is already crowded and the
expected return on the trade has already been bid down to zero.**

Borrow rates also are not contractually fixed. Your broker can
*recall* the loan at any time, forcing a buy-in at the next
available price (ouch, in a squeeze). And the rate can be repriced
mid-position. A position you opened at 2% borrow can be repriced
to 25% on a press release.

#### 2.5 Constructive Shorts via Options — the Barbell-Friendly Substitute

For most retail investors who want short exposure, *do not actually
short the stock*. Buy a put, or sell a call spread, or use a
collar. The reasons:

- **Loss is bounded.** A long put can lose at most the premium paid.
  A long call can lose at most the premium paid. The asymmetric-loss
  problem of a naked short is replaced by a known, capped expense.
- **Borrow is built in.** When you buy a put, you do not need a
  locate, do not pay borrow, do not worry about a recall. The
  market-maker who sold you the put has hedged it through the
  futures and options markets, and the cost of borrow is folded
  into the option's price (you pay it, just less obviously).
- **It is the barbell-shape, exactly.** The barbell — most of
  your wealth in safe, boring long-only positions, with a small
  fraction (2-5%) carved into asymmetric option structures that
  pay off big in tail events but cap your loss at the premium —
  is the right way to think about expressing short views.
- **Tax efficiency, sometimes.** In a US
  taxable account, options can defer or restructure realisation in
  ways a naked short cannot. A long-dated put leaves you with a
  single capital event at expiry rather than a continuous mark-to-
  market on a margin balance.

When you should *actually short the stock* rather than use options:
when you are running a market-neutral or dollar-neutral book at
institutional size, where the option's implied vol overrides the
borrow saving and where you need the straight-line P&L for
risk-budgeting purposes. For everyone else: prefer the option.

#### 2.6 Where Alpha Actually Lives — and Why Long/Short Reaches More of It

The durable alpha sources are short in number. A useful taxonomy
from the academic literature, mapped onto Horace's framing:

| Edge | What it is | Long-only access? | L/S access? |
|---|---|:---:|:---:|
| **Information edge** | You know something they don't | sometimes | sometimes |
| **Interpretation edge** | You read the same data better | yes | yes |
| **Time-horizon edge** | You can hold what they cannot | yes | yes |
| **Behavioural edge** | You exploit predictable retail/MF behaviour | partial | yes |
| **Structural edge** | You exploit forced flows (index rebal, redemption pressure, regulatory) | no | yes |

Long-only access to "structural edge" is essentially zero — by
construction, you cannot short the overpriced leg of a forced-flow
trade. The *entire* class of structural-mispricing trades requires
the ability to short. Same for behavioural: you can buy the unloved
name, but you cannot harvest the over-loved bubble name's mean
reversion without a short.

This is the single biggest structural reason that hedge funds, even
after fees, can defensibly justify their existence: they have access
to a class of return streams that long-only managers literally
cannot trade. It is also why the modern L/S fund's return profile
looks so different from a 60/40 portfolio (Week 4) — the L/S
spread alpha is intentionally orthogonal to market beta.

The chart below shows that orthogonality. It plots the cumulative
real wealth of a hypothetical L/S equity market-neutral fund
(deterministic compounding model targeting 4% annualised real and 5%
volatility) against 60/40 from 1990 through 2024.

![Cumulative real wealth of a hypothetical equity market-neutral fund (4% annualized real, 5% vol, modelled as a deterministic compound path with synthetic mean-zero noise) versus 60/40 (60% S&P 500, 40% 10-year Treasuries, annual rebalance) from 1990 through 2024. The 60/40 line is dramatically steeper but has visible drawdowns at 2000-02, 2008, and 2022. The market-neutral line is flatter but bends through every regime almost unchanged.](image/week13_market_neutral_vs_60_40.png)

The shape tells you what L/S buys you and what it costs. It buys
you regime-independence: the line slopes up through every macro
environment because it is not making a directional bet on the
economy. It costs you compounding: you give up the long-run equity
risk premium because you are not net long the market. Pick L/S as
a sleeve, not as a substitute for your long-only stack — the same
barbell logic from Week 4.

The interactive panel below lets you slide your long-side beta,
short-side beta, and idiosyncratic alpha to see how the resulting
portfolio's wealth path compares to the S&P 500.

---

### 3. Common Misconceptions

**Misconception 1: "Shorting is gambling."**

Going long is also gambling, by the same definition. Both are bets
on the future price of a security. The difference is the loss
profile and the cost structure, not the moral character of the
trade. Treating shorting as taboo systematically excludes you from
the entire structural-edge alpha class.

**Misconception 2: "I'll just short the obvious bubble names."**

A bubble can stay irrational longer than you can stay solvent.
Shorting an obvious bubble name is the single most expensive trade
in all of retail finance — borrow rates spike, margin requirements
expand, and the squeeze risk is asymmetric. If you must take the
trade, take it as a long-dated put (capped loss), not a naked
short (uncapped loss).

**Misconception 3: "Dollar-neutral means no risk."**

Dollar-neutral books still have factor risk, sector risk, gross
exposure to liquidity events, and exposure to idiosyncratic
blow-ups in the names you are short. Long-Term Capital Management
(1998) ran a market-neutral book and lost 90% of its capital in
two months on a correlated factor unwind. Net dollars zero is not
net risk zero.

**Misconception 4: "If my long book and short book have the same
beta, I'm hedged."**

Beta is one risk dimension. You can be beta-neutral and still
massively long-tech-short-staples, long-small-short-large,
long-high-quality-short-low-quality. Each of those is a *factor*
exposure. Modern L/S risk management hedges multiple factor
exposures (beta, size, value, momentum, quality, volatility) — not
just beta.

**Misconception 5: "Short sellers cause the price to fall."**

Short sellers contribute to price discovery; they do not move
prices on their own beyond the marginal selling pressure. The fall
in price of an overvalued stock is caused by the realisation of
overvaluation, which the short seller's research often *reveals*
but does not *manufacture*. The historical record on
short-selling bans (US 2008, EU 2011, China 2015) is consistent:
bans reduce price discovery, widen spreads, and do not prevent the
fundamental fall.

**Misconception 6: "If I sell a covered call, that's the same as a
short position."**

It is not. A covered call is long stock plus short call. Your
exposure to the upside is capped at the call's strike price, but
you are still net long the stock. A true short position is "short
the stock" or "long a put." Don't conflate yield-enhancement
overlays with directional shorts.

**Misconception 7: "Hedge funds always make money on shorts."**

They do not. Most professional L/S funds historically derive most
of their gross alpha from the long book and use the short book
primarily as a hedge — i.e., the short book often *loses* money
over long periods because it is short the secularly-rising market.
A fund earns its keep by losing less on its shorts than the market
makes, and adding spread alpha on top.

**Misconception 8: "I'll short to hedge my long portfolio."**

For most retail investors, hedging via shorts is too expensive
(borrow), too risky (asymmetric loss), and too operationally
demanding (margin calls). Use puts, put spreads, or simply hold
more cash. Hedging-via-shorting is institutional plumbing, not a
retail tool.

**Misconception 9: "130/30 is a hedged version of long-only."**

A 130/30 fund is *more* market-exposed than a 100% long-only fund
in dollar terms (160% gross), and roughly equally market-exposed
in beta terms (~1.0 net). It is not a hedge; it is a relaxation of
the long-only constraint. The marginal benefit comes from the
ability to express short ideas.

**Misconception 10: "If the borrow is free, the short is free."**

Free borrow today does not mean free borrow tomorrow. Borrow rates
reprice. Stocks get recalled. And the dividend obligation and the
opportunity cost of the collateral are real costs even when the
explicit borrow rate is 0.25%. The short is never free.

---

### 4. Q&A

**Q1: As a retail investor with a $100k portfolio, should I ever
short stocks?**

A: For directional bearish views, no — use puts. For relative-value
trades (long one stock, short the related one) you can, but do it
in tiny size, in liquid names with cheap borrow, with hard stops.
You will spend the first few trades learning that the operational
overhead is real. If you do not have a specific structural thesis
that requires the short, do not take it.

**Q2: How much capital do I need to short?**

A: A margin account at any major broker enables you to short. The
initial margin requirement is typically 50% of the short value
(Reg T), with a maintenance requirement of 25-30% beyond that. So
a $10,000 short needs at least $5,000 of equity tied up at entry,
and broker-specific maintenance buffers on top. Practically, do
not take a short position bigger than 5-10% of your liquid net
worth even if the broker allows more.

**Q3: What does a hedge fund's "net" and "gross" actually look like
in practice?**

A: A typical L/S equity hedge fund runs roughly 50-80% net long,
130-170% gross. A market-neutral fund runs roughly 0% net and
150-200% gross. A "low-net" fund runs 10-30% net. The variation in
gross is mostly a leverage decision; the variation in net is a
view decision.

**Q4: How do hedge funds size their shorts?**

A: Smaller than their longs, usually by half. The reasons: shorts
have asymmetric loss; squeeze risk demands hard stops; and the
expected long-run drift of the market is up, so a 1% short is a
larger negative-skew bet than a 1% long. The institutional rule of
thumb is "long sizes can be conviction-weighted; short sizes must
be additionally squeeze-weighted."

**Q5: When does a short get recalled?**

A: When the lender wants the shares back — usually because the
lender's account holder is selling, or because the borrow has
become more profitable to redirect to a different short. You get
a notice (typically 24-48 hours) to either close the short or have
the broker buy it in for you. If the stock is in a squeeze, the
buy-in price is the worst price of your week.

**Q6: How do dividends work on a short?**

A: You pay them. If you are short XYZ on the ex-dividend date, the
dividend is debited from your account and credited to the lender.
There is no offset and no tax benefit (the payment is treated as
ordinary expense, not a qualified dividend). This is why shorting
dividend-rich stocks is structurally expensive even when the
borrow rate looks cheap.

**Q7: Can I short via an ETF?**

A: Yes. Inverse ETFs (SH, PSQ, SDS) are the simplest way to
express a bearish market view without a margin account. They
re-balance daily, which produces *path-dependent decay* over
multi-day holds — over a year of choppy markets they can lose
material value even when the index is roughly flat. Use them for
short-term tactical hedges, not multi-month positions.

**Q8: What's the difference between a "short squeeze" and a "gamma
squeeze"?**

A: A short squeeze is forced covering by short sellers driving the
price up. A gamma squeeze is forced *hedging* by option dealers
who are short calls and must buy spot to stay delta-hedged as the
stock rises. The two often happen together (GameStop, AMC), and
that combined dynamic is what makes meme-stock squeezes so violent.
The "option tail wags the equity dog" pattern is precisely this
mechanism.

**Q9: Why don't I just short the worst stocks I can find and go
long the best ones?**

A: That is the canonical L/S equity strategy and the answer is
"because everyone else does too." The trade is crowded, the names
that look obviously short are already expensively borrowed, and
the names that look obviously long are already expensively priced.
Real L/S alpha comes from the *spread* — picking better longs
*relative to* better shorts within the same factor — not from the
levels.

**Q10: If I want to learn L/S, what should I paper-trade first?**

A: Start with pair trades (Week 14): long Coke / short Pepsi, long
Lowe's / short Home Depot. The relative-value pair has roughly
zero net beta by construction and lets you learn the operational
mechanics (borrow, dividends, margin) on a low-net-risk position.
Once you can run a pair without operational mistakes for three
months, scale up the gross. Don't ever do this in size before you
have done it small.

**Q11: How does L/S fit with the four-tranche structure?**

A: L/S sits in the *opportunistic* tranche. The bedrock (passive
index, long-bond, cash) and the *core* (factor tilts, core L/S
beta) are long-only. The *opportunistic* tranche is where specific
structural trades — pairs, sector rotation, special situations —
live. The fourth tranche (asymmetric speculation) is where the
constructive-short option positions sit. L/S is *not* a substitute
for the bedrock; it is a small sleeve that complements it.

**Q12: What does this lesson set up for the rest of the course?**

A: Week 14 is pair trading — one specific application of the L/S
framework. Week 23 is factors, where the "long the cheap factor /
short the expensive factor" architecture is the same machinery.
Week 47 is long-volatility overlays, where the short leg is short
in a different sense (short variance). Week 49 is volatility
arbitrage, the most sophisticated relative-value application. All
of those build on the mechanics in this lesson.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Long/Short Investing — The Other Half of the Market | Week 13

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** Twelve weeks of this course we've been talking about
owning things. Long stocks, long bonds, long an index fund. That's
a fine default for almost every investor and we've defended it
hard. This week we add a second leg.

**Stella:** Shorting.

**Horace:** Shorting. Borrow, sell, buy back, return. The other
half of the market. By the end of this lesson you'll know the
mechanics, the asymmetric risk, what dollar-neutral and beta-
neutral mean, when to use options instead of a naked short, and
why most of the durable alpha in finance lives on the short side
or in the spread.

---

**[SEGMENT 1: THE FOUR-STEP MECHANIC]**

**Horace:** A short sale is a four-step round trip. Step one,
borrow. Your broker lends you a hundred shares of XYZ. Step two,
sell. You sell those hundred borrowed shares into the market at
the bid. The cash sits in your account but it's pinned as
collateral — you can't spend it.

**Stella:** Step three?

**Horace:** Buy back. Later — could be a day, could be a year —
you buy a hundred shares in the market. Step four, you return
those shares to the broker. Your P&L is sale price minus cover
price, times shares, minus the borrow fee, minus any dividends
that came due during the borrow window — those, you pay.

**Stella:** And the fee?

**Horace:** Annualised, accrued daily. Cheap stocks like AAPL or
SPY — 0.25 to 1 percent a year. Hard-to-borrow names — call it
5 to 30 percent. Stressed-name biotech — up to 100. The borrow
rate is the market's quiet signal that the short is crowded. If
something costs 50% a year to short, the trade is already priced.

---

**[SEGMENT 2: THE ASYMMETRIC PAYOFF]**

[VISUAL: image/week13_payoff_diagrams.png]

**Horace:** Look at this 2x2. Top-left, long stock. Linear upside.
Loss capped at 100% — the stock can't go below zero.

Top-right, short stock. Linear inverted. Gain capped at 100% —
that's all you can make if the stock goes to zero. But the *loss*
is unbounded. The stock can run 5x, 10x, 50x against you. Your
loss scales with it.

**Stella:** And the bottom row?

**Horace:** Bottom-left, long call. The barbell shape. Capped loss
at the premium you paid, asymmetric upside. Bottom-right, long
put — the constructive short. Capped loss at the premium, capped
upside at the strike, but you got short exposure without ever
having to borrow the stock.

**Stella:** That's the barbell shape.

**Horace:** Exactly. For most retail investors who want bearish
exposure, do not actually short the stock. Buy a put. The loss is
capped. The borrow is built in. Operationally it's clean. The barbell
in one sentence: small premium, big asymmetric payoff. That's the
constructive-short. Naked shorts are a tool for institutions
running market-neutral books at scale.

---

**[SEGMENT 3: THE SQUEEZE]**

**Horace:** GameStop, January 2021. Twenty bucks a share at New
Year. Four hundred and eighty by month-end. The math: short
interest above 100% of the float. Coordinated retail call buying.
Dealers had to hedge by buying spot. Spot rallied. Margin calls
hit the shorts. Shorts forced to cover into a vanishing supply.
Price ran 20x in three weeks. Melvin Capital, 12 billion AUM
hedge fund, lost half its assets that month.

**Stella:** That's the option tail wagging the equity dog.

**Horace:** Exactly that. The post-COVID options market is large
enough that retail call-buying campaigns can move the underlying
through dealer hedging flow. Naked shorts in any name with
elevated short interest plus retail option chatter — don't.
Don't. Don't.

---

**[SEGMENT 4: GROSS, NET, BETA-NEUTRAL]**

**Horace:** Now the vocabulary you need to read any hedge fund
fact sheet.

Gross exposure: long dollars plus short dollars. Net exposure:
long minus short. Net beta: the same long minus short but weighted
by each name's beta to the market.

**Stella:** Why does the distinction matter?

**Horace:** Two funds can both be "100 long, 100 short" — same
gross 200, same net dollar zero — and have totally different
exposures. If your long book has beta 1.3 and your short book has
beta 0.7, your *net beta* is plus 0.6. Dollar-neutral, not
beta-neutral. When the market rallies you rally with it.

**Stella:** And the 130/30 fund?

**Horace:** 130 long, 30 short. Gross 160, net 100, beta still
roughly one. It's not a hedged product — it's just a relaxed
long-only mandate. The benefit is the ability to express short
ideas. Mainstream institutional product.

**Stella:** Market-neutral?

**Horace:** 100 long, 100 short, beta-neutral by construction. The
classic L/S equity hedge fund. Whatever return it delivers is
spread alpha — long book minus short book. Theoretically
uncorrelated to the market.

---

**[SEGMENT 5: THE MARKET-NEUTRAL CHART]**

[VISUAL: image/week13_market_neutral_vs_60_40.png]

**Horace:** Here's what that uncorrelated-to-market property buys
you. Hypothetical equity market-neutral fund — assume 4% real
annualised, 5% volatility, modelled as a deterministic compound
path with mean-zero noise — versus 60/40 from 1990 through 2024.

**Stella:** 60/40 finishes way higher.

**Horace:** Right. 60/40 has the equity risk premium working for
it. Market-neutral by construction does not. You give up the
long-run drift in exchange for regime independence. Look at 2008.
Look at 2022. The market-neutral line barely flinches at either.
It is not making a bet on the economy.

**Stella:** So the Sharpe is better but the CAGR is worse.

**Horace:** Sharpe ratio is roughly 0.8 for the market-neutral
sleeve, 0.55 for 60/40 — better risk-adjusted. CAGR is the other
way around — 60/40 wins on raw compounding. That's the L/S
trade-off in one chart. You buy regime independence with
compounding.

---

**[SEGMENT 6: WHERE ALPHA LIVES]**

**Horace:** Here's the philosophical payoff for the lesson. The
durable alpha sources are liquidity, sector rotation,
long-term trends, and buying what passive flows have abandoned.
Map those onto the academic taxonomy: information edge,
interpretation edge, time-horizon edge, behavioural edge,
structural edge.

**Stella:** And shorting?

**Horace:** Long-only access to *structural edge* is essentially
zero. By construction, you can't short the overpriced leg of a
forced-flow trade. The entire class of structural-mispricing trades
— index rebalances, redemption-pressure unwinds, regulatory forced
selling — requires the ability to short. Same for the behavioural
class. You can buy the unloved, but you cannot harvest the
over-loved bubble's mean reversion without a short.

**Stella:** So that's why hedge funds exist after fees.

**Horace:** That's the structural justification. They have access
to a class of return streams that long-only managers literally
cannot trade. Doesn't mean any individual fund earns its fees —
most don't — but the architectural reason for the asset class is
real.

---

**[SEGMENT 7: THE INTERACTIVE]**

**Horace:** Below the video, the interactive panel lets you build
your own L/S book. You set the long-side beta, the short-side
beta, and the idiosyncratic alpha you think you can extract in
basis points per year. The chart shows you the cumulative wealth
versus the S&P 500.

**Stella:** And the stat strip?

**Horace:** Net beta, gross exposure, Sharpe, max drawdown. Slide
the long-beta and short-beta to the same number and watch the
Sharpe collapse — when net beta is zero and idio alpha is zero,
you have a flat line minus your trading costs. Slide the idio
alpha up and the line tilts. That's all alpha is in the L/S
world: the slope you add to a flat line.

---

**[SEGMENT 8: WHEN TO ACTUALLY SHORT]**

**Horace:** Last segment, prescriptive. When should you actually
short something?

One. Never naked-short an illiquid name with elevated short
interest. Just don't. Use a put.

Two. Never short a stock you don't have a structural thesis for
the cover. "It's overvalued" is not a thesis. "There's a forced
selling event in March from index rebalance" is a thesis.

Three. Always check borrow rate before entry. If the borrow is
20% per year, the trade has to make 20% just to break even. Almost
always, it won't.

Four. Size shorts at half what you'd size longs. The asymmetric
loss is real. Margin calls are real.

Five. Set hard stops. The stock running against you grows the
position size. Set a percent-of-capital stop, not a price stop.

---

**[OUTRO]**

**Horace:** Long/short is the toolkit for the back half of this
course. Week 14 is pair trading. Week 23 is factors. Week 47 is
long-vol. Week 49 is vol arb. All of them rest on the mechanics
you just learned.

**Stella:** And for most retail investors?

**Horace:** Stay long-only for your bedrock. Use long puts when
you want bearish exposure. Save the actual L/S book for when you
have a specific structural trade and the operational discipline
to run it small. The lesson isn't "go short tomorrow." The lesson
is "know what you're looking at when the trade arrives."
