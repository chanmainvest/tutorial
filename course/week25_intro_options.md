# Week 25: Introduction to options — calls, puts, premium, intrinsic and time value

---

## Part 1: Reading Section

---

### 1. Why This Is Important

For twelve weeks the course was about owning things. For the next six
weeks it is about owning *contracts on* things. An option is not a
share, not a bond, not an index — it is a piece of paper that says
*"if certain conditions hold at a certain date, money changes hands."*
That is a stranger object than it sounds, and the only way to get
comfortable with the strategies in weeks 26-30 is to spend a week
inside the contract itself.

You need this lesson for four concrete reasons.

**(1) The vocabulary is dense, and almost every word is a small trap.**
"Premium" means three different things depending on context. "ITM" is
not the same idea for a call as for a put. "Exercise" and
"assignment" are the same event seen from two sides of the trade. Most
retail blow-ups in options come from people who learned the strategy
before they learned the vocabulary, and end up holding a position
whose mechanics they cannot describe in one sentence. Spend the week
on the words; the strategies are easy after.

**(2) Premium decomposition is the engine behind every option income
strategy.** Every option price has two pieces — *intrinsic value*
(real, frozen, immune to time) and *time value* (a wasting asset). The
covered calls and cash-secured puts of weeks 26-28 are *time-value
harvesting* trades. If you cannot look at a quote and tell those two
numbers apart, you cannot tell whether a strategy is paying you to
take risk or taking risk for free. The decomposition image in this
lesson is the single most important picture in the second half of the
course.

**(3) The four basic positions are a coordinate system, not four
trades.** Long call, short call, long put, short put. Every option
strategy you will meet for the rest of your life is a combination of
those four — a vertical spread is two of them, an iron condor is four,
a covered call is one of them plus 100 shares of stock. Internalise
the four payoff shapes once and the rest of options is bookkeeping.

**(4) This is foundation for the barbell, the tax stack, and the
vol-tail-wags-dog mechanic.** The barbell holds long-dated calls on
the safety end and uses short near-dated puts/calls on the income
middle — both are option positions. The tax stack reaches for options
because they let you reshape exposure without realising a sale. The
vol-tail mechanic only makes sense once you understand that dealers
*hedge* the options they sell, and that hedging flow moves the spot.
Without this week, three pieces of the broader investing playbook
remain abstract.

---

### 2. What You Need to Know

#### 2.1 An option is a contract — right on one side, obligation on the other

An option is a contract between two parties:

- A **buyer** (also "long" or "holder") who pays a *premium* in cash
  up front, and in return receives a *right*.
- A **seller** (also "short" or "writer") who receives that premium,
  and in return takes on an *obligation*.

The right and the obligation are exact mirrors. If the buyer chooses
to use the right, the seller is forced to deliver. The whole edifice
of options pricing is just the question *"how much should the buyer
pay the seller for taking on that obligation?"*

There are exactly two flavours.

A **call** is the right to *buy* the underlying at a fixed price.
You buy a call when you want upside exposure to the stock without
putting up the full share price.

A **put** is the right to *sell* the underlying at a fixed price.
You buy a put when you want a floor under the stock — protection,
or a directional bet that it will fall.

A complete US-listed equity option is identified by five fields:

1. **Underlying** — the ticker (`SPY`, `AAPL`).
2. **Expiration date** — the last day the right can be exercised.
3. **Strike price (K)** — the fixed price at which the buy/sell
   happens if the right is exercised.
4. **Type** — call or put.
5. **Style** — American or European (covered in §2.5).

A typical broker-screen quote: `AAPL 16-Jan-2026 200 C @ 8.50 / 8.65`.
Read this as *"AAPL January-16-2026, $200 strike, call. Bid 8.50, ask
8.65."* That single line contains all five identifiers plus the live
market for the contract.

#### 2.2 The contract is for 100 shares — and the premium is per share

The most common stumble for a new options trader is the units. US
listed equity options are *standardised at 100 shares per contract*.
The premium is quoted *per share*, not per contract. To get the
dollar amount that actually moves in your account, multiply by 100.

For the AAPL example above, "ask 8.65" means **$865 per contract**
($8.65 x 100). One contract gives the buyer the right to buy 100
shares of AAPL at $200 each — a $20,000 notional position — for an
upfront payment of $865. That is the leverage.

Two consequences fall out of the 100-share spec:

- Anything below $20,000 of stock notional and you can't buy/sell
  fractional contracts. There is no half-contract. If the strategy
  needs a 50-share hedge, options are not the right tool.
- *Account size matters.* A cash-secured put at the $200 strike
  ties up $20,000 of collateral. If your whole account is $30,000,
  this strategy lives in larger names like SPY or QQQ where you can
  go far enough out-of-the-money to make a $5,000 collateral commit
  reasonable.

The 100-share unit is also why every example in this course quotes
position size in *contracts* rather than dollars — saying "sell 1
$200 SPY put" is unambiguous; saying "sell $20,000 worth" requires
arithmetic at every step.

#### 2.3 Moneyness — ITM, ATM, OTM

The relationship between the strike `K` and the current spot `S`
defines the option's *moneyness*.

For a **call**, "moneyness" measures how far above the strike the
spot is — i.e. how much real value the right contains right now:

| Term | Condition (call) | Intrinsic value |
|---|---|---:|
| In-the-money (ITM) | `S > K` | `S - K` |
| At-the-money (ATM) | `S ~= K` | ~0 |
| Out-of-the-money (OTM) | `S < K` | 0 |

For a **put**, the inequalities flip — the right is to *sell* at K,
which is valuable when spot is *below* K:

| Term | Condition (put) | Intrinsic value |
|---|---|---:|
| In-the-money (ITM) | `S < K` | `K - S` |
| At-the-money (ATM) | `S ~= K` | ~0 |
| Out-of-the-money (OTM) | `S > K` | 0 |

A call ITM is a put OTM at the same strike, and vice versa. For a
call at K=100 with spot at S=110: the call is $10 ITM (intrinsic
value $10), and the corresponding put at the same strike is $10 OTM
(intrinsic value 0). They are sides of the same coin.

Three practical observations.

ATM options have *the most time value*. They are the closest to the
boundary between worth-something and worth-nothing, so the
"insurance premium" the seller charges for being on the wrong side
of a small move is largest there. For premium-sellers (weeks 26-28),
ATM contracts pay the most absolute premium per day; for tail-hedge
buyers (week 29), OTM contracts pay the most leverage per dollar of
premium.

Deep ITM options behave almost like the stock itself (delta near 1
for calls, near -1 for puts) — they are leverage substitutes more
than they are options. Deep OTM options behave almost like lottery
tickets — most expire worthless, a few pay 5-50x when the tail
event happens.

The "moneyness" axis is one of the two main axes of the option
chain (the other is expiry). Every screenshot of an options chain
in this course is a 2D grid: strikes down, expirations across.

#### 2.4 Premium = intrinsic value + time value

Every option premium decomposes into exactly two pieces.

**Intrinsic value** is what you would receive if you exercised the
option *right now*. It is the moneyness, in dollars. It cannot be
negative (you would simply not exercise) — it is `max(S - K, 0)` for
a call, `max(K - S, 0)` for a put.

**Time value** (also called *extrinsic value*) is everything else.
It is the premium paid *over* the intrinsic value, and it
compensates the seller for the risk that, between now and expiry,
the option ends up further in-the-money than it is today. Time
value depends on three things:

1. **Time to expiry (DTE).** More days until expiry = more chances
   for the spot to move, so more time value. Time value decays
   toward zero as expiry approaches; the decay accelerates in the
   final 2-3 weeks (the "theta wall").
2. **Implied volatility (IV).** A higher expected move = a wider
   future range = more time value. IV is the option market's
   forecast of the underlying's volatility through expiry.
3. **Risk-free interest rate.** Modest effect — the call is a
   deferred-purchase, so higher rates make a call slightly more
   valuable; the put is a deferred-sale, so higher rates make a
   put slightly less valuable. This effect is usually small for
   front-month options.

The image below shows premium decomposition for a 30-day call at
strike $100 with sigma=20% and r=4%, across spots from $50 to $150.
The shaded *intrinsic* area is the linear `max(S - K, 0)` payoff;
the shaded *time value* sits on top. Notice how time value is
*largest at the strike* and tapers to near-zero at both ends.

![Premium decomposition for a 30-day call at strike $100, sigma 20%, r 4%, spot $50-$150. The total premium curve sits above the linear intrinsic-value floor; the gap between the two — time value — peaks at the strike and tapers to nearly zero deep in- or out-of-the-money.](../image/week25_premium_decomposition.png)

The reason ATM time value peaks is symmetry. At spot = strike, the
option has equal odds of expiring on either side of the strike, so
the seller is taking the most actuarial uncertainty per dollar of
premium and charges accordingly. Far ITM, the option is "almost
certainly going to be exercised" — its price is mostly real
intrinsic, with a thin wrapper of optionality. Far OTM, the option
is "almost certainly going to expire worthless" — its price is a
small lottery-ticket wrapper with no intrinsic.

This decomposition is the single most useful framing in this whole
half of the course. Premium-selling strategies (weeks 26, 27, 28)
make money when the time-value piece decays to zero. Premium-buying
strategies (week 29 protective puts, week 30 long calls as
substitutes) pay for that time value up front and need the spot to
move enough to recover it.

#### 2.5 Expiry — weekly, monthly, LEAPS, and American vs European

US listed equity options come in three calendar flavours:

- **Weekly options** ("weeklies") expire every Friday. Most
  high-volume names (SPY, QQQ, AAPL, NVDA, etc.) have weeklies for
  every Friday in the next 4-8 weeks. Weeklies trade huge volumes
  and are the workhorse for short-dated hedging and gamma trades.
- **Monthly options** expire on the *third Friday of the month*.
  This is the historical default; "monthlies" have the deepest
  open interest, the tightest bid-ask, and the most strikes
  listed. The 30-45 DTE monthly is the canonical "premium-sell"
  contract for retail.
- **LEAPS** (Long-term Equity AnticiPation Securities) are
  options with more than 9 months to expiry. They go out as far as
  ~2.5 years on the most active names. LEAPS are the building
  block for the *long-call-as-stock-substitute* trades on the safe
  end of Horace's barbell — they let you control 100 shares for
  ~15-25% of the share price, with capped downside, and let the
  position age into long-term-capital-gains tax treatment.

Two **exercise styles** matter for retail:

- **American style.** The right can be exercised on *any* business
  day from purchase up to and including expiry. All US listed
  *equity* options (AAPL, SPY, QQQ, etc.) are American-style.
- **European style.** The right can only be exercised *on the
  expiry date itself*. US listed *cash-settled index* options
  (SPX, NDX, RUT) are European-style.

For most retail option strategies, the practical difference is small
because *early exercise is almost always suboptimal* — exercising
early throws away the remaining time value. The two cases where
American-style early exercise actually happens: deep-ITM puts (the
holder gets cash earlier) and the day before a large dividend on a
deep-ITM call (the holder captures the dividend). These edge cases
matter for the *seller* of those contracts — you can be assigned
unexpectedly. We treat them as they come up in week 27.

Settlement is also worth knowing. Equity options settle *physically*:
exercise of an AAPL call delivers 100 shares of AAPL. Index options
settle in *cash*: exercise of an SPX put pays out the difference
between strike and settlement value, no shares change hands. This
matters when sizing — a deep-ITM SPX put pays cash on Friday;
a deep-ITM SPY put delivers a *short stock position* that has to be
closed by Monday.

#### 2.6 The four basic positions

Strip away all the strategy names and there are exactly four
positions a retail account can take in a single contract: long call,
short call, long put, short put. Every strategy in weeks 26-30 is
either one of these four or a combination of them with the
underlying stock.

The image below is the 2x2 grid of payoff diagrams *at expiration*
for those four. Each panel shows P&L per share as a function of spot
at expiry, with breakeven, max profit, and max loss annotated.

![Four payoff diagrams in a 2x2 grid: long call (capped loss at premium paid, unbounded upside above strike+premium), short call (capped gain at premium received, unbounded loss above strike+premium), long put (capped loss at premium paid, large gain as spot falls toward zero), short put (capped gain at premium received, large loss as spot falls toward zero). Each panel has breakeven, max profit, and max loss labelled.](../image/week25_four_positions.png)

A one-line summary of each:

**Long call.** Pay premium `c` for the right to buy at K. Max loss
= `c` (option expires worthless). Breakeven at expiry: `K + c`.
Upside unbounded above breakeven. *Use case:* directional bullish
bet with capped loss; LEAPS-as-stock-substitute on the safe end of
the barbell.

**Short call.** Receive premium `c`, take on obligation to sell at
K. Max gain = `c`. Breakeven at expiry: `K + c`. Loss *unbounded*
above breakeven. **Naked** short calls are dangerous. **Covered**
calls (with 100 shares as collateral, week 27) cap the loss at
"the unrealised gain you didn't get to keep" — bounded, not
unbounded.

**Long put.** Pay premium `p` for the right to sell at K. Max loss
= `p`. Breakeven at expiry: `K - p`. Max gain = `K - p` (spot goes
to zero). *Use case:* portfolio insurance (week 29), bearish
directional bet, vol-spike trades.

**Short put.** Receive premium `p`, take on obligation to buy at K.
Max gain = `p`. Breakeven at expiry: `K - p`. Max loss = `K - p`
(spot goes to zero — the seller still has to buy at K). **Naked**
short puts are dangerous in size; **cash-secured** puts (week 28)
have the full collateral set aside and the loss is bounded — and
identical, in P&L terms, to a limit-buy order at K filled at
`K - p`. This is one of the most useful retail option positions.

The four positions plus the underlying stock (long shares, short
shares) give six primitives. Every named strategy you will see —
covered call, cash-secured put, vertical spread, iron condor,
collar, straddle, strangle, calendar — is a combination of those
six. Memorise the four payoff shapes; the rest is bookkeeping.

#### 2.7 Where this lesson fits — barbell, tax, and the vol tail

Three pieces of Horace's broader investing playbook lean directly
on the foundation laid this week.

**The barbell.** The safe end of Horace's barbell uses
*long-dated, deep-ITM calls* (LEAPS) as a capital-efficient share
substitute — you control the upside of 100 shares with 20% of the
capital, the loss is capped at the premium, and you free up cash
for the speculative end. The income middle (the L2 sleeve) writes
*short calls and short puts* against quality names to harvest time
value. Both ends of the barbell are options; the lesson this week
is the dictionary that lets you read either end.

**Options as a tax tool.** The covered call lets you
reduce delta on a winner *without* selling the share — the lot
keeps aging toward long-term-capital-gains treatment, no taxable
event, exposure shifts. The cash-secured put lets you build a
position at a chosen entry over multiple expiries, with each
unfilled expiration banking premium that lowers the eventual cost
basis. Both depend on the time-value/intrinsic-value split from
§2.4 — the part being harvested is the time value.

**The option tail wags the equity dog.** Dealers who sell
options to retail and institutions hedge their books in the
underlying stock. Their hedge depends on the option's *delta*,
which itself depends on spot, strike, IV, and time. When spot moves,
deltas move, dealer hedges move — and that mechanical hedging flow
*moves the spot further*. The 2021 GameStop squeeze was that
mechanism running in reverse: retail bought calls, dealers were
forced to buy spot to hedge, the spot ran, and the rally was
self-reinforcing until the calls expired. We will not work the math
of dealer hedging in this course, but you cannot understand modern
US equity microstructure without knowing that the option chain is
no longer a sideshow to the spot tape. It is increasingly the *cause*
of the spot tape.

The interactive lab for this week
([course/interactive/week25_option_explorer.html](interactive/week25_option_explorer.html))
lets you pick any of the four positions, drag the strike, expiry,
volatility, rate, and spot sliders, and watch the premium
decomposition update in real time alongside the at-expiry payoff.
Spend twenty minutes in it before reading week 26. Six weeks of
strategy material rest on those five sliders.

---

### 3. Common Misconceptions

1. **"Buying calls is how you get rich."** Calls are *time-decaying*
   instruments. The median outcome of buying an OTM front-month call
   is total loss of the premium. Single-call buyers historically
   underperform — sometimes by enormous margins — buy-and-hold
   investors in the same name. Calls are tools, not lottery
   tickets, and the cases where they make sense (LEAPS substitutes,
   targeted event trades) are narrow.

2. **"Options are too risky for retail investors."** *Naked* short
   options are risky for retail. Long calls, long puts, covered
   calls, and cash-secured puts have *bounded, fully-knowable* worst
   cases at the moment you place the trade. The biggest risk in
   options is the gap between *what the strategy actually does* and
   *what the trader thinks it does* — fix that gap and the risk
   profile is no scarier than the stock itself.

3. **"The premium is the cost of the option."** The premium is the
   cost *only if you're the buyer*. If you're the seller, the
   premium is your *income* — and the cost is the obligation you
   took on. Every dollar of premium has two signs depending on
   which side of the trade you're sitting on. Half the lesson is
   noticing that.

4. **"Out-of-the-money options are 'safer' because they're cheap."**
   Cheap and safe are different. A $0.10 OTM call is cheap in
   absolute dollars, but it has a ~95% probability of expiring
   worthless. Buying a basket of cheap OTM calls is one of the
   most consistent ways retail traders bleed capital. Cheap
   measures dollars per contract; safe measures probability of
   loss.

5. **"At-the-money options have no value because intrinsic is zero."**
   ATM options are *all time value* and time value is largest at
   the strike. An ATM 30-day option on SPY is one of the most
   valuable single contracts in the chain — not despite zero
   intrinsic, *because* of maximum time value. Don't confuse "no
   intrinsic value" with "no value."

6. **"Exercising the option is what makes you the money."** For
   retail traders, exercising is almost always wrong. Exercising
   throws away the remaining time value; instead you *sell to
   close* the option in the market and capture both intrinsic
   *and* time value. Exercise is a settlement event handled by
   the broker on the few cases where it's optimal. Beginners who
   reflexively exercise ITM longs leave money on the table.

7. **"American options are more valuable because you can exercise
   any time."** Slightly more valuable in theory; in practice
   essentially identical to European on equity. The American-style
   premium is real for deep-ITM puts and dividend-day calls; for
   most front-month at- or near-the-money positions, it is a
   rounding error.

8. **"One contract = one share."** One contract = 100 shares. The
   single most common rookie mistake is reading "premium 8.50" as
   "$8.50 to buy" rather than "$850 to buy." Always multiply.

9. **"LEAPS are basically the same as monthly options, just longer."**
   LEAPS behave very differently. Most of their value is intrinsic
   (or near-intrinsic with low theta). Vega is the dominant Greek,
   not theta. They are leverage instruments far more than they are
   pure optionality. Strategies that work with monthlies
   (premium-selling, gamma scalping) often don't work with LEAPS,
   and vice versa.

10. **"If I learn the Greeks I'll understand options."** Backwards.
    The Greeks are calculus on top of the four payoff shapes; if
    the four shapes aren't second nature, the Greeks are
    incomprehensible. Learn the four positions first. Greeks come
    in week 26 onward, in context, when they matter.

---

### 4. Q&A Section

**Q1: I keep getting confused by "long" and "short" in options. Can
you give me a one-line rule?**

A: *Long = paid the premium up-front and now hold a right. Short =
received the premium and now hold an obligation.* Long anything (call
or put) means you are the *buyer*; short anything means you are the
*seller/writer*. The direction of the underlying view is independent
— "long the stock" goes up means up; "long a put" goes up means the
stock went down. Don't merge the two dimensions.

**Q2: Why do options expire? Wouldn't they be more useful if they
didn't?**

A: Without expiry there would be no time-value premium and no
seller would write contracts at a positive price. Expiry is what
turns an option from a permanent right (which would be priceless)
into a finite, tradeable contract. The seller is being paid for the
finite window of risk; without that window there is nothing to be
paid for.

**Q3: How do I read a chain quote like `AAPL 1/16/26 200C 8.50/8.65`?**

A: Underlying = AAPL; expiry = January 16, 2026; strike = $200; type
= Call; bid = $8.50, ask = $8.65 *per share*. To trade one contract
the buyer pays the ask x 100 = $865; the seller receives the bid x
100 = $850. The $15 spread is the market-maker's compensation for
quoting both sides.

**Q4: Why does ATM have the most time value?**

A: Because at the strike, the option has equal odds of expiring on
either side of the strike, so the *uncertainty per dollar of
premium* is largest there. Move spot $20 above K — the call is now
"almost certainly exercised" and the time-value wrapper shrinks.
Move spot $20 below K — the call is now "almost certainly worthless"
and the time-value wrapper shrinks. The peak is at the strike for
the same reason a flipped coin's outcome is most uncertain when it's
spinning.

**Q5: Should I exercise or sell my in-the-money long option?**

A: Almost always *sell*, never exercise. Exercising throws away the
remaining time value; selling captures both intrinsic and time
value. The only retail exception is if you actually want the 100
shares of stock and the option is past the ex-dividend date or
nearly at expiry — and even then, "exercise + immediately sell" and
"sell the option" net to roughly the same dollars after spreads.

**Q6: What does it mean to "be assigned"?**

A: Assignment is the seller-side event where the buyer chose to
exercise. As the seller, you are *forced* to deliver the underlying
(short call -> forced to sell 100 shares; short put -> forced to buy
100 shares). Assignment can happen any business day for American-
style equity options, but in practice almost always at or near
expiry. Cash-secured puts and covered calls treat assignment as the
*intended outcome*, not a failure mode.

**Q7: Can I lose more than I put in?**

A: It depends on the position. Long calls and long puts: max loss
is the premium paid — full stop. Short *covered* calls: max loss is
"the upside you didn't capture" — bounded. Short *cash-secured*
puts: max loss is `(strike x 100) - premium`, fully collateralised.
Naked short calls: theoretically unlimited (don't do it without
deep training and clear risk limits). Naked short puts: bounded but
larger than the collateral typically posted on margin (also avoid
without training).

**Q8: How is implied volatility different from realised volatility?**

A: Realised vol = how much the stock has *actually* moved over a
recent window (a backward-looking measurement). Implied vol = the
volatility figure that, plugged into the Black-Scholes formula,
returns the option's *current market price* (a forward-looking
forecast embedded in the price). When IV > recent realised, the
options market expects movement to pick up; when IV < realised, the
market expects calm to return. The gap between the two is one of
the oldest signals in derivatives.

**Q9: Why 30-45 days to expiry for retail premium-selling?**

A: Theta — the rate of time-value decay — is fastest in the 21-45
DTE band. Shorter than 21 days and the daily premium is small per
contract for the capital tied up; longer than 45 days and the daily
decay slows down meaningfully and you're locking up collateral for
a smaller daily yield. The 30-45 DTE band has been the empirical
sweet spot for retail premium-sellers for decades; SPY weeklies and
30-day monthlies are the workhorse contracts.

**Q10: What's the smallest options account that makes sense?**

A: Roughly $25,000-$50,000 to do cash-secured puts and covered
calls on liquid US ETFs (SPY, QQQ, IWM) with one or two contracts at
a time. Below that, the 100-share contract size forces you into
penny names where the bid-ask spread eats the premium. Below
$10,000, options are not the right tool — stick to share-buying
discipline. The contracts are not scaled for very small accounts.

**Q11: I've heard "options trading is zero-sum." Is that true?**

A: Yes, *in dollars before fees*. Every dollar a buyer makes is a
dollar a seller loses, and vice versa, for any single contract.
This is different from the stock market, which is positive-sum
(companies generate cash flows). In options, you are negotiating who
takes which slice of an existing risk. After fees and bid-ask
spreads, options are *negative-sum*. This is why the strategy
matters more than the prediction — being on the right side of the
asymmetry beats being right about direction.

**Q12: When does this lesson stop being theoretical and start being
useful?**

A: Week 26. Every concept introduced this week — premium = intrinsic
+ time, the four positions, ITM/ATM/OTM, weekly vs monthly vs LEAPS
— gets used immediately in week 26 (options as limit orders), week
27 (covered calls), week 28 (cash-secured puts), week 29
(protective puts), week 30 (LEAPS-as-stock). This is the dictionary
week. Keep the interactive open in another tab while you read the
next five.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Options 101 — Calls, Puts, and the Two Pieces of
Every Premium

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**HORACE:** Welcome back. Twenty-five weeks in, and this is the
week we add the strangest object in the retail toolkit — the
option contract. Six weeks of strategy material rest on the
vocabulary we're going to build today, and almost every
options-related blow-up Stella and I have seen in our careers
came from someone who skipped this week.

**STELLA:** I'll add — the strategies in weeks 26 through 30
are not hard. The vocabulary is hard. By the end of today,
you'll be able to read any options chain on any broker screen,
decompose any quote into its real and time components, and
explain in one sentence what either side of the trade is
agreeing to.

**HORACE:** Three pieces today. First, what an option contract
*is* — the right-and-obligation structure. Second, the premium
decomposition into intrinsic and time value, which is the
single most important picture in the second half of this
course. Third, the four basic positions, which are the
coordinate system every strategy lives in.

**STELLA:** Let's start at the beginning.

---

**[SECTION 1 — THE CONTRACT — 1:00]**

**HORACE:** An option is a contract between two parties. Buyer
on one side. Seller — also called the *writer* — on the other.
The buyer pays a *premium* up front, in cash. In exchange,
the buyer gets a *right*. The seller takes the cash, and in
exchange, takes on an *obligation*.

**STELLA:** And the right and the obligation are exact mirrors.
If the buyer chooses to use the right, the seller is forced to
deliver. The whole question of options pricing is: how much
should the buyer pay the seller for taking on that obligation?

**HORACE:** Two flavours, and only two. *Calls* — the right to
*buy* the underlying at a fixed price. You buy a call when you
want upside in the stock without paying the full share price.
*Puts* — the right to *sell* the underlying at a fixed price.
You buy a put when you want a floor under the stock —
protection, or a directional bet that it falls.

**STELLA:** A complete US listed equity option is identified by
five fields. Underlying — the ticker. Expiration date — the last
day the right can be used. Strike price — the fixed price at
which the buy or sell happens. Type — call or put. Style —
American or European, which we'll come back to.

**HORACE:** A typical broker screen quote: AAPL, January
sixteenth twenty-twenty-six, two hundred dollar strike, call,
bid eight-fifty, ask eight-sixty-five. That single line has all
five fields and the live two-sided market.

---

**[SECTION 2 — 100 SHARES, AND THE PREMIUM IS PER SHARE — 3:30]**

**STELLA:** Critical point — and the most common rookie
stumble. US listed equity options are standardised at *one
hundred shares per contract*. The premium is quoted *per
share*, not per contract. Always multiply by one hundred to
get dollars.

**HORACE:** So in our AAPL example, "ask 8.65" means eight
hundred sixty-five dollars to buy one contract. That contract
gives the buyer the right to buy one hundred shares of AAPL at
two hundred dollars each — a twenty-thousand-dollar notional
position — for an upfront payment of eight hundred sixty-five.

**STELLA:** That ratio — eight hundred sixty-five against
twenty thousand — is the leverage. About four percent of
notional buys you the upside.

**HORACE:** Two consequences. First, no fractional contracts.
If your strategy needs a fifty-share hedge, options are not
the tool. Second, account size matters. A cash-secured put on
the AAPL two-hundred strike ties up twenty thousand dollars of
collateral. If your whole account is thirty thousand, this
strategy lives in larger, more liquid names like SPY or QQQ
where you can go far enough out-of-the-money to make a
five-thousand-dollar collateral commitment reasonable.

---

**[SECTION 3 — MONEYNESS — 5:00]**

**STELLA:** Next concept — *moneyness*. The relationship
between the strike, K, and the current spot price, S. Three
buckets.

**HORACE:** For a call, in-the-money means spot is *above*
the strike. The right to buy at a hundred is valuable when
the stock is at a hundred ten — you're getting a ten-dollar
discount. *In-the-money* means real, intrinsic value.
At-the-money means spot equals strike — the right is on the
threshold. Out-of-the-money means spot is below the strike —
the right to buy at a hundred when the stock is at ninety
isn't worth anything *today*, only the chance it might be
worth something later.

**STELLA:** For a put, the inequalities flip. The right to
*sell* at a hundred is valuable when the stock has dropped to
ninety. So put ITM is spot below strike. Put OTM is spot
above strike. ATM is the same — spot equals strike.

**HORACE:** A call ITM is a put OTM at the same strike, and
vice versa. Same coin, two sides.

**STELLA:** And ATM options have the *most time value*, which
brings us to —

---

**[SECTION 4 — THE PREMIUM DECOMPOSITION — 6:30]**

**[VISUAL: image/week25_premium_decomposition.png]**

**HORACE:** This image. Spend a minute on this one. It's the
premium of a thirty-day call at strike one hundred, twenty
percent volatility, four percent rate, plotted against spot
price from fifty to one fifty. Two layers shaded.

**STELLA:** The lower wedge — the band starting at spot one
hundred and rising linearly — that's *intrinsic value*. It's
`max(spot minus strike, zero)` for a call. Real value, frozen,
immune to time. If you exercised right now, that's what you'd
get.

**HORACE:** The bump on top — the gold band that arches above
the intrinsic floor, peaks somewhere right around the strike,
and tapers off as the call goes deep-in or far OTM — that's
*time value*. Everything paid above intrinsic. It compensates
the seller for the risk that, between now and expiry, the spot
moves further into the money than it is today.

**STELLA:** Notice three things. One, time value peaks *at
the strike*. That's not a coincidence. At the strike, the
option has equal odds of expiring on either side, so the
seller is taking the most actuarial uncertainty per dollar of
premium and prices accordingly.

**HORACE:** Two, deep ITM, the time value is small. The call
is "almost certainly going to be exercised" — its price is
mostly real, frozen intrinsic, with a thin wrapper of optionality
on top.

**STELLA:** Three, deep OTM, the time value is also small —
because the call is "almost certainly going to expire
worthless." A small wrapper of lottery-ticket optionality.

**HORACE:** This decomposition is the engine of every
income strategy in the next five weeks. Selling covered
calls, selling cash-secured puts — those are *time-value
harvesting* trades. The seller gets paid the time-value
piece up front and pockets it as the option decays toward
expiry. If you cannot look at a quote and tell the intrinsic
piece from the time-value piece, you cannot tell whether
the strategy is paying you to take risk or taking risk for
free.

---

**[SECTION 5 — TIME VALUE DEPENDS ON THREE THINGS — 9:30]**

**STELLA:** Time value depends on three inputs. Days to
expiry, implied volatility, and the risk-free rate.

**HORACE:** More days = more time value. More chances for the
spot to move = bigger insurance premium. As expiry approaches,
time value decays toward zero, and the decay accelerates in
the final two to three weeks — the so-called *theta wall*.

**STELLA:** Implied vol — the option market's forecast of how
much the stock will move through expiry. Higher IV = wider
expected range = more time value. IV is its own animal — when
something scary is coming, like an earnings report, IV spikes.
When the market is calm, IV collapses.

**HORACE:** And rates — modest effect on equity options.
Higher rates make a call slightly more valuable (it's a
deferred-purchase contract — your cash earns interest while
you wait), and a put slightly less valuable. Don't lose sleep
over it for front-month options. We'll show the magnitude in
the interactive.

---

**[SECTION 6 — EXPIRY FLAVOURS — 11:00]**

**STELLA:** Three calendar flavours of expiry.

**HORACE:** *Weeklies* expire every Friday. The big names —
SPY, QQQ, AAPL, NVDA — have weeklies for every Friday in the
next eight weeks. Workhorses for short-dated hedging and gamma
trades.

**STELLA:** *Monthlies* expire on the third Friday of the
month. The historical default. Most open interest, tightest
spreads, most strikes listed. The thirty-to-forty-five DTE
monthly is the canonical contract for retail premium-sellers.

**HORACE:** And *LEAPS* — Long-term Equity Anticipation
Securities, options with more than nine months to expiry. They
go out as far as two and a half years on active names. LEAPS
are the building block for the *long-call-as-stock-substitute*
trade on the safe end of the barbell. Control a hundred shares
for fifteen to twenty-five percent of share price, with capped
downside, and let the position age into long-term capital
gains. We do that explicitly in week thirty.

**STELLA:** Two exercise styles. *American* — exercise any
business day up to and including expiry. All US listed equity
options. *European* — exercise only on the expiry date. US
listed cash-settled index options like SPX, NDX, RUT.

**HORACE:** For most retail strategies, the practical
difference is small, because early exercise is almost always
suboptimal — you throw away time value by exercising early.
Two cases where it matters: deep-ITM puts and dividend-day
calls. We come back to those in week 27.

---

**[SECTION 7 — THE FOUR POSITIONS — 13:00]**

**[VISUAL: image/week25_four_positions.png]**

**STELLA:** This is the second image to spend a minute on.
Two-by-two grid. Four payoff diagrams at expiration.

**HORACE:** Top-left — *long call*. You paid the premium for
the right to buy at K. Below the strike, max loss is the
premium — flat horizontal line. Above the strike plus
premium, the payoff is linear and unbounded above. Breakeven
at K plus the premium paid.

**STELLA:** Top-right — *short call*. You sold the right.
Mirror image, flipped vertically. Above strike plus premium,
loss is linear and unbounded. Below, you keep the premium —
flat horizontal line. *Naked* shorts are how people blow up.
*Covered* short calls — with a hundred shares of stock as
collateral — are how people generate income, week 27.

**HORACE:** Bottom-left — *long put*. Paid premium for the
right to sell at K. Above strike, max loss is the premium.
Below strike minus premium, payoff is linear, capped on the
downside at "stock goes to zero." Use cases: portfolio
insurance, week 29; bearish bets; vol-spike trades.

**STELLA:** Bottom-right — *short put*. Sold the right. Above
strike, you keep the premium. Below strike, loss accumulates
as the stock falls — capped at "stock at zero." *Naked* short
puts are dangerous in size. *Cash-secured* puts — full
collateral set aside — are bounded, and *identical, in P&L
terms, to a limit-buy order at K filled at K minus premium*.
That's week 26.

**HORACE:** Memorise these four shapes. Every strategy in this
course — covered calls, cash-secured puts, vertical spreads,
collars, iron condors, calendar spreads, you name it — is a
combination of those four positions plus shares of stock. Six
primitives. The rest is bookkeeping.

---

**[SECTION 8 — WHERE THIS FITS — 15:30]**

**STELLA:** Three big pieces of Horace's playbook lean directly on
this week. Quick tour.

**HORACE:** First — the barbell. The safe end
uses long-dated, deep-ITM LEAPS calls as a capital-efficient
share substitute. The income middle writes short calls and
short puts against quality names to harvest time value. Both
ends are options. This week is the dictionary.

**STELLA:** Second — options as a tax tool. The
covered call lets you reduce delta on a winner without
selling. The cash-secured put lets you build a position at a
chosen entry over multiple expiries, with each unfilled
expiration banking premium. Both depend on knowing the
intrinsic-versus-time-value split — the part being harvested
is the time value.

**HORACE:** Third — the vol tail wags the equity dog.
Dealers hedge the options they sell. Spot moves, deltas move,
hedges move, hedges *move the spot further*. GameStop 2021 ran
that mechanic in reverse — retail bought calls, dealers were
forced to buy spot, the spot ran, the rally was self-reinforcing.
You can't read modern US equity microstructure without knowing
the option chain isn't a sideshow anymore.

**STELLA:** Three big pieces of the playbook *require* this week
to make sense. That's why we built a whole lesson on the contract
before we built any strategies.

---

**[SECTION 9 — THE INTERACTIVE — 16:30]**

**[VISUAL: course/interactive/week25_option_explorer.html]**

**HORACE:** The interactive lab pulls all of this together.
Pick one of the four positions. Drag the strike, the days to
expiry, the implied vol, the rate, and the spot. Watch the
premium decomposition update — intrinsic, time value, total —
in real time. Watch the at-expiry payoff overlay shift with
the strike.

**STELLA:** Things to play with. Hold strike at a hundred,
spot at a hundred, drag DTE from one day to three sixty-five.
Watch the time-value peak grow from almost nothing to several
dollars. That's the *theta curve* you'll meet again in week 27.

**HORACE:** Then drag IV from five percent to eighty percent
at the same DTE. Watch the time-value bump grow proportionally.
That's *vega* — sensitivity to vol — in pictures.

**STELLA:** Then move spot away from strike with everything
else fixed. Watch the time-value bump die at both ends and
peak at the strike. That's the symmetry argument from Section
4 made concrete.

**HORACE:** Twenty minutes in this lab before week 26. Six
weeks of strategy material rest on those five sliders.

---

**[OUTRO — 17:30]**

**STELLA:** Recap. An option is a right on one side, an
obligation on the other. Premium equals intrinsic plus time
value. Four positions — long call, short call, long put,
short put — are the coordinate system. Hundred shares per
contract, premium quoted per share, multiply by a hundred for
dollars. Weeklies, monthlies, LEAPS for calendar; American or
European for style.

**HORACE:** Next week — options as limit orders. The single
most useful mental model in retail options. Once you see
covered calls and cash-secured puts as orders that *pay you to
wait*, the whole income side of the barbell falls into place.

**STELLA:** Read the lesson, click around the interactive,
and we'll see you next week.

**[END]**
