# Week 26: Options as limit orders — getting paid to leave instructions on the table

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Last week we mapped the options vocabulary — calls, puts, strikes,
expiry, premium, theta. Vocabulary on its own is inert. What turns
options from an exotic instrument into a workhorse for a long-only
retail book is the right *mental model*, and the right model is the
simplest one: **a sold option is a limit order that pays you to wait.**

A cash-secured put at the $90 strike is the same instruction you would
already give your broker — *"I'd buy 100 shares of XYZ at $90"* — except
the broker now hands you a cheque for leaving that instruction on the
table. A covered call at the $110 strike is *"I'd sell my XYZ at $110"*,
again with a cheque attached. Same trigger price, same buy-low / sell-
high discipline, plus income for the time the trigger sits unfilled.

This matters for four concrete reasons:

**(1) Idle cash is a real cost, not a free option.** Most retail
investors keep a "waiting to deploy" sleeve sitting in money market or
T-bill funds at the going short rate. That is the *opportunity cost
floor*; against an at-the-target cash-secured put on a name you
genuinely want to own, the cash works two or three times harder for the
same target entry price. The premium is not a bonus — it is what your
cash *should* be earning while it waits.

**(2) Selling decisions are emotionally expensive; getting paid to
pre-commit is cheap.** Every long-only investor knows the "I should
have sold" feeling. A covered call writes the sell ticket in advance,
at a price you chose in calm-mind, and pays you to hold yourself to it.
The premium is the institutional equivalent of paying yourself an
adviser fee for *not* moving the goalposts.

**(3) This is the L2 income tactic in the barbell.**
Horace's barbell holds high-conviction safety on one end and asymmetric
speculation on the other; the question is what the names *between*
those two ends do all day. They sit in the L2 ("high-quality long-only,
permanent compounders") tranche and earn premium by writing covered
calls and cash-secured puts at the edges of where the holder would
already act. The L2 sleeve is the income engine of the barbell, and
the income is engineered, not hoped-for.

**(4) Options are a tax tool first, a leverage tool second.**
Selling a covered call lets you reduce delta on a winner *without*
selling the share — exposure shifts, the tax lot doesn't. Selling a
cash-secured put lets you build a position at a chosen entry *over
multiple expiries*, with each unfilled expiration banking premium that
lowers the eventual cost basis. For a successful long-only investor
the largest unspoken fee is capital gains tax; the order-replacement
view of options is how you start managing it.

This week we walk through the mechanics in slow motion. Week 27 takes
covered calls deep — strike selection, theta capture, when to roll.
Week 28 does the same for cash-secured puts and the wheel.

---

### 2. What You Need to Know

#### 2.1 The reference book — $50k account, 100 shares of XYZ at $100

To keep every example anchored to one balance sheet, picture a
**$50,000 account** holding **100 shares of XYZ**, a SPY-equivalent ETF
trading at $100/share. That is $10,000 of stock and $40,000 of cash.
This account is large enough to demonstrate both strategies side by
side: there are 100 shares to write a covered call against, and there
is plenty of cash to secure a put at almost any strike.

For the lesson we will work with two specific strikes:

- **$90 cash-secured put** (10% below spot). Collateral required:
  $90 x 100 = **$9,000** out of the $40k cash sleeve.
- **$110 covered call** (10% above spot). Collateral required:
  the 100 shares already owned.

XYZ has reasonable implied volatility, so the front-month options pay
roughly $2.00 for the put and $1.50 for the call. Those numbers carry
through every example below. See the payoff diagrams in
[course/image/week26_csp_payoff.py](course/image/week26_csp_payoff.py)
and [course/image/week26_cc_payoff.py](course/image/week26_cc_payoff.py),
and the interactive walk-through in
[course/interactive/week26_orders_lab.html](course/interactive/week26_orders_lab.html).

#### 2.2 The cash-secured put as a limit buy order

A cash-secured put (CSP) is an instruction you have already used in
plain-vanilla form. The plain-vanilla version is a limit buy order:
*"Buy 100 XYZ at $90 or below, good-til-cancelled."* While the order
sits unfilled, the $9,000 you set aside earns the broker's cash sweep
rate.

The CSP version is the same instruction with a maturity date and a
cheque:

> *"I will buy 100 shares of XYZ at $90. Here is $9,000 in collateral.
> Pay me $200 to leave that instruction open for 30 days."*

Three outcomes, and only three:

1. **XYZ closes above $90 at expiry.** The put expires worthless. You
   keep the $200 premium and the $9,000 collateral is released.
   Annualised yield-on-cash: $200 / $9,000 x (365/30) ~ **27.0%**. You
   can write the next month's put.
2. **XYZ closes between $88 and $90.** You are assigned: you buy 100
   shares at $90. Effective cost basis = $90 - $2 = **$88/share**, which
   is below where the stock actually printed. You bought at a discount
   to your own limit price.
3. **XYZ closes below $88.** Same assignment, same effective $88 cost
   basis, but now sitting on a mark-to-market loss. The downside is
   identical to having had a limit order fill at $90, *minus* the $2
   cushion. Worst case (XYZ -> $0): -$8,800 vs. the limit-order's
   -$9,000 — strictly better.

![Payoff diagram for a single short $90 cash-secured put on XYZ for $2.00 premium with 30 days to expiry, plotted from $60 to $140 of XYZ price at expiry. The curve is flat at +$200 (max profit, premium kept) above the $90 strike, slopes diagonally down through the $88 breakeven, and reaches -$8,800 at XYZ = $0. The green-shaded region above zero marks "premium kept"; the red region below marks "below breakeven." Footer notes $9,000 cash collateral and ~27% annualised yield-on-cash if the put expires worthless.](../image/week26_csp_payoff.png)

The image script `week26_csp_payoff.py` shades this exact P&L profile
from $60 to $140 with breakeven, max profit and tail loss labelled.

The honest framing: a cash-secured put **never does worse than a limit
order at the same strike** in P&L terms, in exchange for a single
cost — the option has an expiry, the limit order doesn't. If your
trigger price is a hard line you would still want to act on six months
from now, the CSP just becomes a rolling discipline: write the new one
the day the old one expires.

#### 2.3 The covered call as a limit sell order

The covered call (CC) is the exit-side mirror image. Plain-vanilla
version: limit sell 100 XYZ at $110, GTC. Option version:

> *"I will sell my 100 shares of XYZ at $110. The shares themselves are
> the collateral. Pay me $150 to leave that instruction open for 30 days."*

The three outcomes:

1. **XYZ closes below $110.** Call expires worthless. You keep both the
   100 shares and the $150 premium. The $150 is income on top of
   dividends; the shares are unmoved. Yield-on-position: $150 / $10,000
   x (365/30) ~ **18.3%** annualised on the share value.
2. **XYZ closes at $110.** You are called away (your shares are sold)
   at $110. Total proceeds: $110 + $1.50 premium = **$111.50/share**, or
   $11,150 on the position. That is $1,150 above your $10,000 cost.
3. **XYZ closes above $110.** Same assignment, same $111.50 proceeds.
   Anything XYZ does above $111.50 you do not capture — that is the
   trade-off you accept for getting paid. The image
   `week26_cc_payoff.py` shows the payoff capping at +$1,150 for any
   stock price >= $110.

![Payoff diagram for the covered-call package — long 100 shares of XYZ at $100 entry plus one short $110 call sold for $1.50 — plotted across XYZ expiry prices from $60 to $140. The blue solid line is the package P&L; a dashed grey line shows the long-stock-only reference for comparison. The package caps at +$1,150 for any price at or above the $110 strike, crosses zero at the $98.50 breakeven, and slopes down to -$9,850 at XYZ = $0. The two lines run almost parallel on the downside — the $150 premium is cushion, not hedge.](../image/week26_cc_payoff.png)

The downside is unchanged from owning the stock outright, *minus* the
$1.50 cushion: at XYZ -> $0, the position is worth -$10,000 + $150 =
**-$9,850**, vs. -$10,000 for a no-call holder. The covered call is
not a hedge — the premium is not nearly large enough — but it is
cushion, income, and a pre-committed exit, all in the same ticket.

#### 2.4 Walking the mechanics in slow motion

Day 0 of the lesson month:

1. **Account snapshot.** $50,000: 100 XYZ at $100 (= $10k stock) + $40k
   cash. XYZ front-month $90 put bid $2.00, $110 call bid $1.50, both
   30 days to expiry.
2. **Sell-to-open the $90 put.** Click "sell to open"; broker reserves
   $9,000 of cash as collateral; $200 lands in the account immediately.
   Cash sleeve is now $40k - $9k reserved + $0.2k premium = $31.2k free
   + $9k locked + $0.2k income.
3. **Sell-to-open the $110 call.** Broker freezes the 100 shares as
   collateral; $150 lands. The 100 shares cannot be sold while the
   call is open (you would be naked-short the call), but they can still
   collect dividends and gain/lose in price. Income to date: **$350**
   on a $50k book in one click — that's 70 bps on net liq, or roughly
   8.4% annualised, and the "trades" are sitting at the same prices you
   would already have wanted to act on.
4. **Wait 30 days.** During the wait you check positions weekly, not
   daily. At $98 you do nothing. At $92 you do nothing. At $115 — the
   call is in the money; the share is going to be called away on
   expiry day, exactly as instructed. At $86 — the put is in the money;
   you will be assigned the 100 shares at $90, exactly as instructed.
5. **Expiration day.** Brokers settle automatically. Call assignment:
   shares delivered, $11,000 lands. Put assignment: $9,000 leaves, 100
   shares of XYZ arrive. Either, both, or neither happens, depending
   on where XYZ closed.

There is no continuous monitoring, no chart-staring, no stop-losses to
manage. The orders execute themselves. The only active step is writing
the next pair of orders the following month.

#### 2.5 Yield-on-cash: what "getting paid to wait" actually pays

The honest income comparison is yield on the **specific capital each
trade ties up**, not yield on the whole account.

For the $90 CSP at $2 over 30 days:

- Capital tied up: $9,000 collateral.
- Premium: $200.
- Period yield: 200 / 9000 = **2.22%** in 30 days.
- Annualised (simple, 365 days): 2.22% x (365/30) ~ **27.0%**.

That headline yield is what option-selling literature loves to quote.
It is also misleading on two counts:

1. **The 27% is paid only when the option expires worthless.** When you
   are assigned, the "yield" is no longer on cash — it has converted
   into a stock position whose return depends on the share, not the
   premium. A more honest figure is **expected** annualised yield: the
   premium yield x probability of expiring worthless, plus the
   expected return on the assigned stock x probability of assignment.
2. **The 27% does not survive the assignment month.** If you are
   assigned at $90 in a month when XYZ printed $80, the position now
   has a $1,000 mark-to-market loss against the $200 income — the
   month was net negative, not 27% positive.

For the $110 CC at $1.50 over 30 days:

- Capital tied up: $10,000 of stock value.
- Premium: $150.
- Period yield: 150 / 10000 = **1.50%** in 30 days.
- Annualised: 1.50% x (365/30) ~ **18.3%**.

The right way to read these numbers: they are an **upper bound** on
the income contribution from the option overlay — what you collect
in the months where nothing happens — and they only describe the full
return when nothing happens. The covered call does not add anything in
the assignment scenario beyond the premium itself; the CSP turns
straight into the underlying share return.

#### 2.6 Where this fits in the barbell

Horace's portfolio is a barbell: safety on one end (cash, T-bills,
gold, deep-ITM long-dated calls), structural-alpha speculation on the
other. The middle — the diversified market-cap-weighted "core" — has
been removed. But that does not mean nothing sits between the two
ends. The high-quality long-only names you are *willing to own and to
sell at known prices* live in an L2 income sleeve, and the L2 income
sleeve is run almost entirely on covered calls and cash-secured puts.

The CSP / CC pair is what gives the L2 sleeve its yield. Without that
overlay, the L2 sleeve is just a slow compounder paying dividends in
the 1-2% range. With the overlay it pays the dividend *plus* 8-15%
in option premium when nothing happens, and reverts to passive long
exposure exactly at the prices the holder pre-committed to act on
when something does.

This is why we treat this lesson as foundational rather than advanced.
The barbell shape requires this engine to make economic sense; without
it, the safety end's drag would dominate the asymmetric end's payoff.

#### 2.7 Where this fits in the tax stack

The covered call has a second job that is at least as valuable as the
income, and is rarely advertised: it lets you **reduce effective
exposure on a winner without selling**. A 100-share position with a
3-year embedded gain has a covered call written against it — the
share is not sold, no taxable event is realised, but the delta of the
package is now ~0.3 instead of 1.0. You are short volatility while
the lot continues to age toward long-term-capital-gains treatment (or,
in a tax-advantaged account, while it continues to compound tax-free).

The cash-secured put plays the entry-side equivalent: it lets you
build a position at a chosen price *across multiple expiries*. Each
expiry that closes the option worthless banks short-term income (taxed
at ordinary rates, ideally inside an IRA) and lowers the effective
cost basis of the eventual fill. The dollar of premium banked today
is more valuable than the dollar of capital gain crystallised in five
years only if you bank the income inside a sheltered account — which
is also why this strategy and the IRA wrapper were practically made
for each other.

In a Roth IRA, none of the premium is taxed, and the strategy
compounds tax-free. In a traditional IRA, the same income is
tax-deferred. In a taxable account, the option-selling income lands
as short-term capital gains at ordinary income rates, and you have to
pencil that drag into the headline yield before deciding whether the
overlay is worth it.

---

### 3. Common Misconceptions

1. **"Selling a put is bearish, like shorting the stock."** It is the
   opposite. A short stock makes money when the share falls and loses
   on a rally; a short put makes money when the share is *flat or up*
   and loses on a sharp fall, with the floor pegged at the strike
   minus the premium. Short put = neutral-to-bullish, not bearish.

2. **"The premium on a put is free money — sell as far OTM as you
   like."** Far-OTM puts pay almost nothing relative to the capital
   they tie up. The premium / collateral ratio collapses as you move
   the strike further from spot, and the only time those tail puts
   matter is when they get hit hard. Do not chase the lottery-ticket
   end of the chain.

3. **"A covered call hedges the downside."** It does not. $1.50 of
   premium is a $1.50 cushion — useful, not protective. If XYZ drops
   from $100 to $80, the covered-call writer is down $1,850 instead
   of $2,000. That is barely a difference. If you want a hedge, buy a
   put (Week 29); if you want income with a pre-committed exit, write
   a call.

4. **"You should never get assigned."** Assignment is *the limit order
   filling*. If you genuinely wanted to buy at $90 or sell at $110, the
   assignment is the trade you came for — not a failure mode. Treating
   assignment as something to avoid at all costs leads to rolling
   options forever to dodge the very fill you set up to capture.

5. **"Annualised yield = real yield."** A 27% annualised number on a
   30-day put is not 27% returned per year. It is what you receive
   *in months where nothing happens*, multiplied as if those months
   continued forever. The realised yield over a year always includes
   the months where you *were* assigned, and those net out to a
   stock-return-plus-cushion, not a 27% premium.

6. **"You need to watch the screen all day."** The opposite is true.
   Every step that requires a decision is a separate ticket: sell-to-
   open, then optionally close-early, then expiration. Most CSP / CC
   writers spend 15-30 minutes per month and let the broker settle the
   rest. Continuous monitoring is *bad practice* here — it tempts you
   to manage a working trade out of the win.

7. **"Selling options is unlimited risk."** Naked options are. Cash-
   secured puts and covered calls are not — both are bounded. The CSP's
   maximum loss is `(strike x 100) - premium`; the CC's maximum loss
   is the underlying stock going to zero, *minus* the premium received.
   Both numbers are fully knowable when you place the trade.

8. **"Options income makes long-term investing irrelevant."** The
   premium yield is real but it is a *complement*, not a substitute.
   The bulk of long-term wealth still comes from the share's price
   appreciation and dividends. Options overlay turns a 7% expected
   return into 9-12%; it does not turn it into 30%.

9. **"This is just selling insurance — it always loses in the end."**
   This is the classic insurance-company critique, and it would be
   right if you were writing tail risk on an unhedged book. CSP and
   CC are not naked tail-writes — both are fully collateralised, and
   the CSP collateral is at a strike *you chose* on a stock *you want
   to own*. The asymmetry is on your side.

10. **"You can do this on any stock."** No. You can do this on stocks
    with (a) liquid options chains (tight bid/ask, decent open
    interest), (b) prices and quality you would actually want to own
    in your underwear at 3am, and (c) realistic IV (not so low that
    the premium isn't worth the time, not so high that the assignment
    risk dominates). For most retail books that universe is twenty
    names, mostly large-cap US ETFs and household-name single stocks.

---

### 4. Q&A Section

**Q1: What's the difference between a "cash-secured" put and a "naked" put?**

A: Collateral. A cash-secured put has the full strike-times-100 in
cash set aside in the account; if assigned, the cash buys the share
without margin. A naked put has only the broker's margin requirement
posted, which is far less than the full collateral. Cash-secured puts
are allowed in IRAs; naked puts require a margin account and a higher
options approval level. For retail investors learning this strategy,
always cash-secured.

**Q2: Why 30 days? Why not 7 or 90?**

A: Theta — option time decay — is fastest in the 21-45 day window. A
7-day option pays much less premium for the capital tied up; a 90-day
option pays more dollars but has worse daily decay and locks the
collateral up longer. The 30-45 day band has been the empirical sweet
spot for retail premium-sellers for decades, and there is no strong
reason for it to change.

**Q3: What if my CSP gets assigned and I don't want the stock anymore?**

A: That is a portfolio-management question, not an options question.
You sell the assigned shares immediately, take the loss (or gain) net
of premium, and stop writing puts on that name. The discipline is set
*before* selling the put: only write CSPs on stocks you would actively
welcome owning at the strike. If your conviction has changed, close
the put before expiry instead of being assigned.

**Q4: Can I close the option early instead of waiting for expiry?**

A: Yes, you "buy to close" at any time. A common heuristic: if the
option has lost 50-80% of its value with weeks still to go, buy it
back, lock in the realised gain, and write the next one. The opposite
case — option price has doubled against you — is the moment to think
hard about whether you still want assignment at the strike. If not,
buy it back at a loss and reset.

**Q5: Why does the lesson keep saying "100 shares" instead of any
quantity?**

A: One US equity options contract represents 100 shares. That is the
contract spec — there is no smaller unit. If you want 50-share
exposure, options are not the right tool; use a limit order. If you
want 250-share exposure, you sell two contracts and use a 50-share
limit order for the residual.

**Q6: Does this strategy work better in a bull market or a bear market?**

A: Both, differently. In a slow-grind bull market, neither side is
assigned often: the puts expire worthless (you keep premium), the
calls are sometimes called away at your target (you sell at your
target plus premium). In a bear market the puts get assigned at
strikes that look expensive in hindsight, but the assignment was
exactly the trade you set up; the calls expire worthless and pay
income to cushion the drawdown. Where it works *poorly* is a vertical
melt-up — your covered calls cap you below the rally — or a sharp
crash — your CSPs assign at strikes far above market.

**Q7: Why "$50k account with 100 shares of XYZ" — is that a typo?**

A: Anchored deliberately. One options contract controls 100 shares; you
cannot write a covered call against fewer. The "$50k account" framing
is the realistic retail balance sheet — $50k can comfortably support
one covered call and one cash-secured put on a $100 stock with $30k of
free cash to spare. Smaller accounts typically write only the call OR
only the put, not both at once.

**Q8: What about taxes — short-term capital gains every month?**

A: Yes, every premium banked in a taxable account is short-term
capital gain at ordinary income rates, every month. This is why the
strategy belongs mostly in tax-advantaged accounts (IRA,
Roth IRA), where the premium income compounds untaxed. In a taxable
account the after-tax yield is 30-40% lower than the headline.

**Q9: My broker rejected my "sell-to-open put" order. Why?**

A: Almost certainly an options approval level. Brokers tier options
permissions: Level 1 is covered calls only; Level 2 adds long puts /
calls; Level 3 adds cash-secured puts and credit spreads; Level 4 adds
naked options. You need at least Level 2 or 3 for cash-secured puts.
Apply for the level once, mention this strategy, and approval is
typically routine for a retail account with experience.

**Q10: Is the wheel — alternating CSP and CC — the same thing?**

A: Yes, the wheel is exactly the strategy in this lesson, run on a
loop: CSP until assigned, then CC on the assigned shares until called
away, then CSP again. We will deep-dive the wheel in Week 28 once both
sides are individually well understood (CC in Week 27, CSP in Week 28).
This week is the conceptual unlock; the next two weeks are the
operating manuals.

**Q11: Implied volatility just spiked — should I sell more options?**

A: Carefully. High IV means premiums are larger, which is the obvious
attraction. But high IV also means the market is pricing in a real
move, and the assignment probability is correspondingly higher. A
useful framing: high IV is the market paying you a fair price for the
extra risk you're underwriting, not a free lunch. Size accordingly.

**Q12: Do dividends complicate covered calls?**

A: They can. American-style call options can be exercised early —
particularly the day before an ex-dividend date if the dividend is
larger than the call's remaining time value. The shares are then
called away early, and the dividend goes to the new owner. To avoid
this, either roll the call forward before ex-div, or only write
covered calls on stocks where the time-value cushion comfortably
exceeds the upcoming dividend. Most ETFs (SPY etc.) pay quarterly
dividends well below typical option time value, so this is rarely an
issue.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Options as Limit Orders — Getting Paid to Leave Instructions on the Table (Week 26)
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

[INTRO — 0:00]

[VISUAL: Title card. "Week 26 - Options as Limit Orders - Getting paid to wait." Soft-coloured background with a $90 put and a $110 call ticket overlay.]

**Stella:** Welcome back. We are in week 26, the second week of the
options arc. Last week was vocabulary — calls, puts, strikes, time
decay. This week we unlock the mental model that turns vocabulary into
something you can actually run on a real account.

**Horace:** And the model is one sentence. A sold option is a limit
order that pays you to wait. A cash-secured put is a limit *buy*
order with a cheque attached. A covered call is a limit *sell* order
with a cheque attached. Same trigger price, same buy-low / sell-high
discipline, plus income for the time the trigger sits unfilled.

**Stella:** That is much less scary than "selling options."

**Horace:** It is the same thing, just stated honestly. Most retail
investors already know how to place a limit order. We're going to
show that the option version is a strict upgrade in P&L terms — never
worse, sometimes better — at one specific cost we'll be very clear
about: the option has an expiry, the limit order doesn't.

---

[THE REFERENCE BOOK — 1:30]

**Stella:** Set the stage with the example we'll use all the way
through.

**Horace:** Picture a $50,000 account. We're going to keep the math
clean: 100 shares of XYZ — think of it as a SPY-equivalent ETF —
trading at $100 a share. That's $10,000 of stock and $40,000 of cash.
Big enough to write one covered call and one cash-secured put without
breaking a sweat.

**Stella:** And the two strikes we're picking?

**Horace:** Ten percent above and ten percent below. We're willing to
buy more XYZ at $90, and we're willing to sell our 100 shares at $110.
Those are not random numbers — they are the prices we already set as
"the prices I would happily transact at" before the lesson started.

**Stella:** Premiums?

**Horace:** Front-month, 30 days to expiry. The $90 put pays $2.00 a
share, so $200 a contract. The $110 call pays $1.50, so $150. Two
clicks, $350 in income on a $50k book, against trigger prices we
already wanted to act on.

[VISUAL: account balance sheet appearing. Stock $10k, Cash $40k. Two
tickets sliding in: "Sell $90 put -> +$200" and "Sell $110 call ->
+$150". Total income ticker: $350.]

---

[THE CSP WALKTHROUGH — 3:30]

**Stella:** Take the cash-secured put first. What just happened
mechanically when I clicked sell-to-open?

**Horace:** Three things. One: the broker reserved $9,000 of your
$40,000 cash sleeve. That's the strike, $90, times 100 shares. Two:
$200 of premium landed in your account, immediately, today. Three:
you now owe a contract — if XYZ closes below $90 at expiry, you must
buy 100 shares at $90.

**Stella:** And in plain English, that's...

**Horace:** ...the same instruction you would already give your
broker for free. "Buy 100 XYZ at $90 or below." The limit order does
this for $0. The CSP does it for +$200.

[VISUAL: image/week26_csp_payoff.png — the shaded payoff diagram from
$60 to $140, max profit $200 above $90, breakeven at $88, max loss
$8800 at $0.]

**Stella:** Walk the three scenarios in slow motion.

**Horace:** Scenario one, by far the most common: XYZ closes at $96.
The put expires worthless, the $9,000 collateral releases, you keep
$200. Annualised yield on the cash that was actually tied up: $200 on
$9,000 over 30 days is 2.22%, times twelve, call it 27%. That's the
headline number — and we'll be honest that it only describes months
where nothing happens.

**Stella:** Scenario two?

**Horace:** XYZ closes at exactly $89. You're assigned: you buy 100
shares at $90, $9,000 leaves the account, 100 XYZ arrive. But your
*effective* cost basis is $90 minus the $2 premium — so $88. You just
bought XYZ for less than where it actually printed. The CSP gave you
a discount versus the limit order at the same strike.

**Stella:** Scenario three — the bad one?

**Horace:** XYZ closes at $80. Same assignment, same effective $88
cost basis. Now you are sitting on a mark-to-market loss of $800. But
look: the limit-order buyer at $90 is in *exactly the same situation*,
just $200 worse. The CSP never does worse than the limit order. The
worst case — XYZ to $0 — is minus $8,800 instead of minus $9,000.

[VISUAL: side-by-side comparison. "Limit buy at $90 / fill price $90 /
worst case -$9,000" vs. "CSP $90 strike / effective $88 / worst case
-$8,800." A green arrow points from limit order to CSP labelled "+$200
in every scenario."]

---

[THE CC WALKTHROUGH — 7:30]

**Stella:** Now flip it. The covered call.

**Horace:** Same conceptual move on the exit side. You own 100 shares
of XYZ at $100. You'd be happy to sell at $110. The plain-vanilla
version is a limit sell order — costs nothing, pays nothing. The
option version says: I'll sell at $110, the shares are the collateral,
pay me $1.50 a share to hold that instruction for 30 days.

**Stella:** And the three scenarios?

**Horace:** XYZ at $105. Call expires worthless. You keep the 100
shares, you keep the $150. That $150 on a $10,000 stock position is
1.5% in 30 days, or 18% annualised — assuming nothing happens, which
again we'll caveat in a minute.

[VISUAL: image/week26_cc_payoff.png — payoff diagram capping at $1,150
above strike, breakeven at $98.50, downside slope down to -$9,850 at
$0.]

**Stella:** XYZ at $112?

**Horace:** Called away. Shares delivered at $110, you keep the $150
premium. Total proceeds $111.50 a share, $11,150 on the position.
That's a $1,150 gain on a $10,000 stock — 11.5% — which is the
maximum the covered-call package can ever earn on this trade.

**Stella:** And if XYZ goes to $130?

**Horace:** Same $11,150. The $20 above $110 belongs to whoever bought
your call. That is the cost of running this strategy: you cap your
upside at the strike-plus-premium. The trade-off is, you collected
income for capping it.

**Stella:** And the downside?

**Horace:** Stock to $80, position is worth $8,000 plus $150 premium,
so net $8,150 against your $10,000 cost — minus $1,850. Without the
call you'd have been minus $2,000. The covered call is *cushion*, not
hedge. $150 doesn't save you in a 20% drawdown — but it is real, and
it accumulates if you write one every month.

[VISUAL: cushion vs. hedge graphic. "Cushion: $150 in the worst-case
month. Hedge: a long put — Week 29." Arrows differentiate the two.]

---

[THE DOUBLE-WRITE — 11:00]

**Stella:** OK, walk the *combined* trade. Both options open at once.

**Horace:** Day zero, same $50k account. Two clicks. Sell-to-open the
$90 put — $9,000 cash reserved, $200 in. Sell-to-open the $110 call
— 100 shares frozen as collateral, $150 in. Total income: $350. The
account balance hasn't changed in *exposure* — you still own 100 XYZ,
you still have $40k cash — but you've handed over two pre-commitments
the market will execute for you for free.

**Stella:** And then what does the next 30 days look like?

**Horace:** You check positions weekly, not daily. XYZ at $98 — do
nothing. XYZ at $103 — do nothing. XYZ at $115 — the call's in the
money, you'll be called away on expiry; don't panic, that's the trade
you set up. XYZ at $86 — the put's in the money, you'll be assigned;
again, that's the trade you set up.

**Stella:** And on expiration day?

**Horace:** Brokers settle automatically overnight. Either, both, or
neither contract assigns. You wake up with whatever combination of
cash and stock the price action wrote out, plus the $350 you booked
on day zero. Then you write the next month's pair.

[VISUAL: timeline graphic. Day 0: two tickets sold, $350 in. Days 1-29:
"check weekly, do nothing." Day 30: settlement — four panels showing
each combination of (assigned/not) x (called/not).]

---

[THE INTERACTIVE — 13:00]

**Stella:** Show the lab.

**Horace:** This is `week26_orders_lab.html` in the interactive folder.
Pick CSP or CC at the top. Move the spot price, the strike, the
premium and the days-to-expiry sliders. The payoff diagram redraws,
breakeven and max profit recalculate, and the "annualised yield-on-
cash" number updates in real time.

[VISUAL: interactive/week26_orders_lab.html on screen. Toggle from CSP
to CC; slide strike from $90 down to $85, watch the premium-implied-
yield drop. Slide days-to-expiry from 30 down to 7, watch annualised
yield rise but realised dollar income fall.]

**Stella:** What's the lesson from playing with the sliders?

**Horace:** Two things. One: yield-on-cash *rises* as you shorten the
expiry — that's the fast-theta corner of the chain — but the dollar
income *falls*, so you trade more often for less per ticket. Two:
moving the strike further out of the money collapses the premium
faster than it lowers the assignment risk. There's a sweet spot
around 30-45 days, ~5-10% out of the money, that has been the retail
premium-seller's home base for decades. The lab lets you see why with
your own hands.

---

[BARBELL & TAX FRAME — 15:30]

**Stella:** Where does this fit in the broader philosophy?

**Horace:** Two places. First, the barbell. The barbell
holds high-conviction safety on one end and asymmetric speculation on
the other; the L2 sleeve in between is the high-quality long-only
names you're willing to own and to sell at known prices. That sleeve
is run almost entirely on covered calls and cash-secured puts. The
CSP/CC pair is the income engine of the L2 tranche.

**Stella:** And the second place?

**Horace:** Tax. The largest unspoken fee in long-only
investing is capital gains. Covered calls let you reduce *exposure*
on a winner without selling the *share*; the tax lot keeps aging,
the delta drops. Cash-secured puts let you build a position over
multiple expiries — each expiration that closes worthless banks income
that lowers the effective entry. Pair both with a Roth or traditional
IRA wrapper and the income compounds without the tax drag. In a
taxable account you have to pencil in the ordinary-income hit before
the headline yield is real.

[VISUAL: barbell illustration with "Safety," "L2 income (CC + CSP),"
"Asymmetric edge." Arrow points at L2: "this lesson lives here."]

---

[OUTRO — 17:00]

**Stella:** What's the one-line takeaway?

**Horace:** A sold option is a limit order with a cheque. The cheque
is the income. The price is the expiry. The discipline is — only
write puts on names you actually want to own at the strike, and only
write calls at exit prices you'd already pre-commit to. If you're
willing to act, get paid for the willingness.

**Stella:** Next week?

**Horace:** Week 27, covered calls deep dive. Strike selection, when
to roll, what to do when the call goes deep ITM, and how to size CCs
across a portfolio of L2 names. Then week 28 takes the same scalpel
to cash-secured puts, and week 29 closes the arc with protective
puts and collars.

**Stella:** See you next week.

[VISUAL: closing card. "Next: Week 27 — Covered Calls Deep Dive."]

[END — 17:55]
