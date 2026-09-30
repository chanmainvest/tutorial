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
