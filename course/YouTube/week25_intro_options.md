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
