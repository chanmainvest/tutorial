# Week 27: Covered Calls Deep Dive — Strike Selection, IV Harvesting, the Wheel

---

## Part 1: Reading Section

---

### 1. Why This Is Important

Week 26 reframed selling a call as a paid limit-sell order. That mental
shift is necessary, but it is not sufficient. The investor who actually
runs covered calls month after month learns very quickly that the
*strategy* is easy and the *parameter selection* is everything. Two
investors writing covered calls on the same SPY position can produce
completely different five-year outcomes depending on how they pick
strike, tenor, and when they choose to write. This week is about those
choices.

**First, strike selection drives the entire payoff profile.** A
30-delta call collects roughly three times the premium of a 10-delta
call but is also assigned roughly three times as often. Neither is
"correct" in isolation. The right choice depends on whether you would
genuinely be happy to sell the shares at that strike, and whether the
extra premium compensates you for the cap on upside you are agreeing
to. Most retail investors anchor on premium yield without thinking
about the second leg of that trade, and they get systematically called
away in the months they most needed the upside.

**Second, tenor is not neutral.** Theta — the rate at which extrinsic
value decays — is non-linear. A 30-day option does not bleed twice as
fast as a 60-day option; it bleeds roughly 1.4 times as fast per day.
That non-linearity is why the 30 to 45 days-to-expiration band is the
sweet spot for income writers. Shorter than that, premium is too small
relative to gamma risk; longer than that, you give back too much theta
to hold the position open.

**Third, IV-rank tells you when to write and when to wait.** Premium is
not a free lunch. It is compensation for taking the other side of
implied volatility. When IV-rank is high you are being paid richly to
sell that volatility. When it is low — fat-and-happy markets, complacent
VIX in the low teens — covered-call premium shrinks to almost nothing
and the cap on upside is a worse trade. Horace's principle 6 lives
here: *the tail wags the dog*, and IV is the price of the tail.

**Fourth, taxes can wipe out the headline yield.** A covered-call
program in a taxable account converts what could have been long-term
capital gains (taxed at ~15-20%) into a stream of premium recognised
as short-term capital gains (taxed up to ~37%). For most readers this
strategy belongs in an IRA or other tax-advantaged sleeve. The
largest unspoken fee in long-only investing is tax, and a
high-turnover income overlay is the most tax-inefficient thing you
can do in the wrong account.

This lesson teaches the disciplined version of the strategy: how to
pick the strike with delta, how to pick the tenor with theta, how to
read IV-rank, how to roll, and where covered calls quietly fit inside
the barbell.

---

### 2. What You Need to Know

#### 2.1 Strike Selection by Delta

Strike picking by *price* is amateur hour. Strike picking by *delta* is
the institutional standard. Delta has three useful interpretations
simultaneously, which is why options desks use it as the universal
ruler:

1. **Hedge ratio.** A 0.30-delta call moves $0.30 for every $1.00 the
   stock moves (over short distances).
2. **Approximate probability of finishing in the money.** A 0.30-delta
   call has roughly a 30% chance of expiring ITM. (This is technically
   *risk-neutral* probability, not real-world probability, but for
   short-tenor strikes the difference is small.)
3. **Approximate moneyness scaled by volatility.** 0.50 delta sits at
   the money. 0.16 delta sits roughly one standard deviation out.
   0.025 delta sits roughly two standard deviations out.

That last interpretation is the key one. **0.16 delta is not a magic
number — it is 1σ.** A 1σ OTM call has, by construction, about a 16%
chance of expiring ITM. That is why "16-delta call" is the conservative
income writer's default.

The four standard delta levels for covered-call writers, on a stock at
$100 with σ=22% and 30 DTE:

| Delta | Strike (approx) | Premium (approx) | Premium / strike | Annualised | Assignment odds |
|------:|----------------:|-----------------:|------------------:|-----------:|----------------:|
| 0.50  | $100            | $2.55            | 2.55%             | ~31%       | ~50%            |
| 0.30  | $103-104        | $1.35            | 1.31%             | ~16%       | ~30%            |
| 0.16  | $107            | $0.55            | 0.51%             | ~6.2%      | ~16%            |
| 0.10  | $109-110        | $0.30            | 0.27%             | ~3.3%      | ~10%            |

The bend in that table is where this lesson lives. Going from 0.10
to 0.16 delta nearly doubles the premium, but only adds 6 percentage
points of assignment risk. Going from 0.30 to 0.50 delta only doubles
the premium again but adds another 20 points of assignment risk. **The
30-delta call is the standard income strike** because it sits at the
favourable bend of that curve. The 16-delta call is the conservative
default for a writer who genuinely does not want to part with the
shares.

![Premium yield by strike](image/week27_strike_yield.png)

The image renders the full curve for a $100 stock at σ=22%, 30 DTE.
Notice how flat the curve becomes past 110% of spot — once you push
beyond 1σ OTM you are working very hard for tiny premium.

#### 2.2 Tenor — Why 30 to 45 DTE

Theta is the hidden engine of every short-premium strategy. A short
option's value decays roughly with the square root of time-to-expiry,
which means a 30-day option carries about 70% as much extrinsic value
as a 60-day option. The implication: by writing 30-day calls and
rolling monthly, you collect roughly *1.4 times* the annualised
premium that you would by writing 60-day calls and rolling
bi-monthly, even though the headline premium per contract is smaller.

But you cannot push that logic to weekly options without paying for
it. Weekly calls have huge gamma — a small move in the stock will
double or triple the option's delta in a day, which means a stock
that briefly pierces your strike on Wednesday and then closes back
below it on Friday can still leave you assigned. The mechanical
sweet spot, agreed on by both BXM index methodology and most income
desks I have spoken to, is **30 to 45 days to expiration**.

Within that band the two reasonable defaults are:

- **Monthly cycle (28-35 DTE).** Write the next monthly expiry on
  expiration Friday. Twelve writes per year. Aligns with monthly
  earnings calendars on most names.
- **45 DTE rolling.** Write 45 DTE, roll out at 21 DTE. About nine
  writes per year, slightly less assignment risk per write, but
  also slightly less annualised premium.

Both are defensible. Pick one and stay disciplined.

#### 2.3 IV-Rank — When to Write and When to Wait

IV-rank measures where current implied volatility sits inside the
trailing 52-week range. IV-rank of 50 means current IV is exactly at
the median; IV-rank of 90 means current IV is near the high; IV-rank
of 10 means current IV is near the low.

The rule is cleaner than most people realise. **Sell premium when
IV-rank is above 30. Wait when it is below.** Premium is compensation
for taking the other side of vol. When vol is cheap (IV-rank low),
you are accepting the cap on upside for almost nothing. When vol is
rich (IV-rank high), you are being paid richly for the same cap.

A practical implication: covered-call yield on SPY in calm 2017 was
about 4% annualised. The same overlay in late-2022, with VIX in the
high 20s, was paying about 14% annualised. Same strikes, same deltas,
completely different trades. Investors who blindly write every month
ignoring IV-rank are mechanically harvesting a *worse* edge than the
one they think they have.

This is the practical version of "the tail wags the dog": the tail
(IV) is the dog. Watch the IV-rank, not the stock price. The covered-call writer
who ignores IV-rank is the equivalent of the value investor who
ignores price — they are placing the same trade regardless of what
the market is offering them.

#### 2.4 Rolling — The Two Rules

When the stock approaches your strike, you have three choices: take
assignment, buy the call back, or roll. Rolling is buying the current
call back and simultaneously writing a new one further out in time
and possibly further out in strike. Done well, rolling lets you
maintain the position without realising the gain on the underlying
shares (relevant for tax planning — you want to preserve the
long-term-capital-gains treatment on the equity leg).

**Rule 1: When the call is ITM and you do not want to be assigned,
roll up and out.** Buy back the current ITM strike, sell a higher
strike further out in time. This usually requires the new tenor to
be at least one cycle longer (e.g., a 30-day ITM rolled to a 60-day
strike one or two strikes higher) to roll for a credit, not a
debit. If you cannot roll for a credit, accept assignment instead —
paying to defend a covered call is almost always a worse trade than
being called away at your original strike.

**Rule 2: When the stock has fallen significantly and the call is
deep OTM, roll down and out.** Buy the current near-worthless call
back for a few cents, sell a lower strike further out. This locks
in most of the original premium and resets the position to collect
fresh premium against the now-lower stock. This is also the move
that makes covered calls work in flat-to-down markets — you keep
re-striking lower as the stock drifts.

The third option — rolling out only, same strike — is rarely the
right move. If the call is ATM or close to it, rolling same-strike
just defers the assignment decision by 30 days, usually for a tiny
credit. Better to either accept assignment (your shares were going
to get called anyway) or roll up-and-out for genuine breathing
room.

#### 2.5 Tax Treatment and Account Choice

Premium received from selling calls is treated as short-term capital
gain in U.S. taxable accounts unless the contract is held open for
more than a year — which essentially never happens with 30-45 DTE
writing. For a top-bracket investor the federal rate is 37% plus
state, versus the 20% (plus 3.8% NIIT) long-term cap gains rate the
underlying shares would earn if simply held. That is roughly half
the headline premium gone to taxes.

There are also the **assignment mechanics** to worry about. If your
shares are called away, the gain on the equity leg is realised
according to the holding period of *those shares*, not the option.
If the shares had a long-term holding period you keep LTCG treatment
on the equity gain. The premium itself, however, is still STCG.

There is a further trap: a covered call written on a stock you have
held less than one year *can suspend the holding-period clock* under
the IRS "qualified-covered-call" rules if the strike is too far ITM.
The mechanical fix is to write only OTM calls on shares you have not
yet held for a year.

The clean solution is the tax-account anchor: **run the covered-call
program in an IRA or 401(k), not in a taxable account.** All premium
is tax-deferred (or tax-free in a Roth), assignments do not generate
taxable events, and the entire strategic flexibility — rolling,
re-striking, accepting assignment — is freely available without tax
friction. For a taxable account, the calculus tilts much harder
toward simply holding the shares and harvesting LTCG over multiple
years.

#### 2.6 Buy-Write ETFs vs. DIY — Why QYLD Underperforms QQQ

The biggest covered-call ETFs in the U.S. are QYLD (Global X NASDAQ
100 BuyWrite, ~$8B AUM) and JEPI (JPM Equity Premium Income, ~$33B
AUM). They sell the strategy as "high yield with downside cushion."
The yield is real — QYLD distributes about 11-12% per year. The
problem is the ETF mechanics quietly destroy the upside.

QYLD writes **at-the-money calls every month** on the entire NASDAQ
100 portfolio. ATM means delta ~0.50 — the strategy caps almost the
full upside in any given month. Over 2014-2024 that produced roughly
6%/yr total return for QYLD versus roughly 17%/yr for plain QQQ.
The investor in QYLD received their headline yield, and the fund's
NAV slowly bled lower over a decade as the math compounded. QYLD's
NAV in 2014 was about $25; in early 2026 it is about $17.

![QYLD vs QQQ since 2014](image/week27_qyld_vs_spy.png)

JEPI is structurally less aggressive — it writes equity-linked notes
that approximate selling 5-10% OTM calls on the S&P 500 — so the
upside cap is gentler. Its 11-year arc has been about 9-10%/yr
versus SPY's roughly 13%/yr, with materially lower drawdown. JEPI
is a defensible product for a retiree wanting a smoother ride; QYLD
is, in my opinion, a structurally bad product wearing a high-yield
hat.

The point of running the strategy yourself is precisely that **you
control the strike and the tenor.** The buy-write ETFs use a fixed
mechanical rule because they have to — they are managing billions
of dollars of someone else's money and cannot pause writing in
low-IV-rank months. You can. That optionality is the entire reason
DIY covered calls beat the buy-write ETFs over a long horizon.

#### 2.7 The Wheel — Preview of Week 30

Here is the strategy that ties Weeks 26, 27, and 28 together. It is
called "the wheel," and Week 30 will dedicate a full lesson to it.

1. Identify a stock you would be happy to own at a discount.
2. Sell a cash-secured put (Week 28) at your target buy price.
3. **If assigned** (you bought the shares), now sell covered calls
   against them every month until called away.
4. **If called away** (the shares were sold above your strike), go
   back to step 2.

The wheel is the institutional version of what value investors have
always done by hand: buy below intrinsic value, sell above. The
options just pay you to wait at both ends. On a stock you genuinely
want to own at $90 and sell at $115, the wheel can produce 12-18%
annualised yield purely from premium, plus the equity P&L on the
intervening price movement. That is the destination Weeks 25-30 are
quietly walking toward.

The covered-call leg of the wheel is exactly the strategy this
lesson teaches. Master it here, master cash-secured puts in Week 28,
and Week 30 is just the assembly instructions.

#### 2.8 A Worked Example, End to End

You own 100 shares of SPY at $480, current price $510. IV-rank is 45,
which is fine — not rich, not cheap.

- **Strike choice.** SPY 30-delta call, 30 DTE, is the $522 strike.
  Premium ~$5.80. Yield = 5.80 / 522 = 1.11% in 30 days = ~13.5%
  annualised.
- **What you have agreed to.** If SPY closes above $522 in 30 days,
  your shares are called away at $522. Combined with $5.80 premium,
  effective sale price is $527.80. That is a +9.96% gain from the
  $480 cost basis — a gain you would happily take.
- **What happens if SPY stays below $522.** You keep the $580 in
  premium and write a new 30-day call against the same shares. Twelve
  writes per year × 1.11% = roughly 13% annualised yield from premium
  alone, layered on top of SPY's normal price appreciation and
  dividend.
- **What happens if SPY rallies hard to $545 in two weeks.** Your
  call is now deep ITM with about 14 days left. You roll up-and-out
  to the next month's $540 strike for a small credit. You have
  given up the rally between $522 and $540 (about 3.4% of upside),
  but kept the position open and avoided assignment.
- **What happens if SPY drops to $470.** Your call goes near-zero.
  You buy it back for $0.20, lock in $5.60 of premium realised,
  and write a new call against your shares at the $485 strike for
  the next month. You are now collecting fresh premium against the
  lower stock, which is exactly the cushion the strategy advertises.

That is the whole strategy. The interactive at the end of the lesson
lets you spin all of these knobs.

---

### 3. Common Misconceptions

1. **"30-delta is the right strike for everyone."** It is the right
   strike for an income-focused writer with no strong directional
   view. If you would be unhappy to part with the shares, write 16-
   delta. If you bought the stock specifically to write calls
   against it and would happily sell at the strike, write 50-delta.
   Strike is not universal.
2. **"Weekly options give the highest annualised yield, so I should
   write weeklies."** They give the highest theta-per-day, but they
   also give the highest gamma. Realised assignment risk and slippage
   on weeklies is far worse than on monthlies. Most retail backtests
   that show "weeklies dominate" ignore execution costs and gamma
   blow-ups.
3. **"Covered calls are downside protection."** They are not. The
   premium you collect cushions about 1-2% of decline. In a 20%
   drawdown, your shares lose 18% net. Buying a put would protect
   you. Writing a call is income, not insurance. Stop conflating
   the two.
4. **"QYLD's 12% yield is real return."** It is real cash distribution.
   It is not real total return. Total return for QYLD is ~6%/yr; the
   distribution is partly funded by NAV erosion. Read the total
   return chart, not the yield headline.
5. **"I should always roll my calls instead of taking assignment."**
   No. If you cannot roll for a credit, taking assignment is
   strictly better than paying to defend a position. Sometimes
   the right answer is to let the shares get called away.
6. **"Covered calls work in any market."** They underperform sharply
   in strong rallies (the cap on upside dominates the premium
   collected) and break even or slightly outperform in flat and
   mildly down markets. They do *not* save you in a hard bear
   market.
7. **"Premium is risk-free income."** It is compensation for tail
   risk and capped upside. The upside foregone in good months funds
   the premium you keep in flat months. There is no free lunch.
8. **"I can ignore IV-rank because I am writing every month
   anyway."** You cannot, if you care about expected return. Skipping
   the bottom-quintile IV-rank months historically improves the
   strategy's Sharpe by about 25%.
9. **"The wheel is a different strategy from covered calls."** It is
   the same strategy, just with the buying decision (cash-secured
   put) bolted onto the front. Master one, you have nearly mastered
   the other.

---

### 4. Q&A Section

**Q: How do I find delta on my broker's screen?**
A: Most retail platforms (Fidelity, Schwab, IBKR, ThinkOrSwim) show
delta as a column in the option chain when you switch the chain view
to "Greeks" or "Analytics." If you do not see it, the chain is
showing only price columns — change the view. Robinhood and Webull
both expose delta on the option detail page.

**Q: What if my stock pays a dividend during the option's life?**
A: The option market prices in expected dividends already, so the
strike yield you see in the chain is *after* the expected dividend
ex-date drop. If the dividend is unexpectedly raised, your call may
be exercised early the day before ex-dividend — this is the only
common early-exercise scenario for American calls. Watch for it.

**Q: Can I write covered calls on ETFs?**
A: Yes, and for most retail income writers the right vehicles are
SPY, QQQ, and IWM. Single-name covered calls add idiosyncratic risk
without enough premium pickup to justify it for most readers.

**Q: How much capital do I need to start?**
A: One contract = 100 shares. At SPY $510, that is $51,000 of
shares. At QQQ $440, that is $44,000. IWM is the cheapest of the
three at about $22,000 per contract. If your account is smaller than
that, the closest substitute is the XSP (mini-SPX) options, which are
1/10 the size of SPX.

**Q: What if I do not own 100 shares — can I still write a call?**
A: Not as a covered call. Without the shares it is a *naked* call,
which has theoretically unlimited risk and requires margin. Most
brokers will not let retail accounts write naked calls. Buy 100
shares first, or use a vertical call spread (Week 29) to construct
a defined-risk equivalent.

**Q: Should I close winners early?**
A: Industry rule of thumb: close at 50% of max profit. If you sold
a call for $2.00 and you can buy it back for $1.00, you have
captured half the premium with much less than half the time elapsed
(theta accelerates near expiry). Closing early frees the shares to
write a new call sooner and removes the gamma risk of holding the
short option into expiration week.

**Q: Does this work on cheap stocks?**
A: Mechanically yes, but the premium is usually too small to be
worth the effort. A $20 stock writing a 30-delta monthly call might
yield $0.20-0.30. After commissions and bid-ask, the realised yield
is barely there. Stick to underlyings above $80-100 per share.

**Q: How does this fit the barbell?**
A: Covered calls live on the *passive-equity* end of the barbell,
not the speculative end. They convert long equity exposure into
slightly-less-equity-with-income — they do not replace the
speculative-options sleeve. If you write covered calls on your SPY
holding, that SPY position is doing what it always did, just with
an income overlay.

**Q: Why not just buy QYLD or JEPI?**
A: If you genuinely have no time to manage the strategy, JEPI is a
reasonable buy. QYLD is not, because the at-the-money strike rule
caps too much upside. DIY beats both because you can flex strike
and tenor with IV-rank, which neither ETF can do.

**Q: What is the worst-case scenario?**
A: A V-shaped recovery where the stock crashes 30% then rallies 50%.
Your covered calls did not protect you on the way down (premium
covers maybe 2% of the 30% drop) and the new lower-strike calls you
wrote on the way back up cap your recovery at 10-15%. You lock in
losses while giving away the recovery. This is exactly what
happened to QYLD investors in 2020-2021 and is the strongest
argument for the IV-rank gating rule from §2.3.

**Q: How much does this lesson assume from Week 26?**
A: It assumes you accept that selling a call is a paid limit-sell
order. Re-read Week 26 if that framing has not internalised. This
lesson is the parameter-tuning layer on top of that mental model.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Covered Calls Done Right — Strike, Tenor, and Why
QYLD Quietly Loses to QQQ
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. Last week Horace walked us through the
mental model: selling a call is a paid limit-sell order, selling a
put is a paid limit-buy order. This week we are going one level
deeper. How do you actually pick the strike? How do you pick the
tenor? When do you write, and when do you wait?

**Horace:** And we are going to spend a fair amount of time on a
question that comes up almost every week in my inbox: why does QYLD
yield 12% but make 6% a year? Because that gap explains everything
about why DIY covered calls beat the buy-write ETFs.

**Stella:** Big lesson. Let us start with the strike question.

---

**[STRIKE BY DELTA — 1:30]**

**Stella:** Horace, when I look at an option chain on SPY, there are
literally thirty strikes available. How do I pick?

**Horace:** Stop picking by price. Pick by delta. Delta is the
universal ruler. A 30-delta call has roughly a 30% chance of
finishing in the money. A 16-delta call has about a 16% chance —
that is one standard deviation. A 10-delta call is two standard
deviations out. Once you think in delta, the strikes become
comparable across stocks, across volatilities, across whatever.

**Stella:** And the conventional choices are?

**Horace:** Three of them. 50-delta — that is at the money,
maximum premium, maximum assignment risk. 30-delta is the income
writer's standard. 16-delta is the conservative writer who really
does not want to part with the shares.

[VISUAL: image/week27_strike_yield.png]

**Horace:** This is a $100 stock, 30 days to expiry, σ=22%. The
y-axis is the call premium divided by the strike — what you
collect per dollar of strike committed. Look at the curve. From
the at-the-money strike out to about 110% of spot, the curve falls
fast. Past 110%, it bends almost flat. That bend is the entire
story.

**Stella:** So past 1σ OTM, you are working hard for almost nothing.

**Horace:** Exactly. The 30-delta call sits right at the favourable
bend. The 50-delta call collects more, but you cap your full
upside half the time. The 16-delta sits one sigma out, gives up
roughly two-thirds of the 30-delta premium, but is assigned half
as often. Pick one of those three. Stop picking by price.

---

**[TENOR — 5:00]**

**Stella:** What about how far out to write?

**Horace:** Theta is non-linear. A 30-day option does not bleed
twice as fast as a 60-day option — it bleeds about 1.4 times as
fast per day. That non-linearity is the entire reason monthly
writing dominates bi-monthly writing on annualised yield.

**Stella:** And weeklies?

**Horace:** Weeklies sound great in theory and are awful in
practice. They give you the highest theta-per-day, but they also
give you huge gamma — a one-day move in the stock can double your
delta overnight. Real-world realised assignment risk on weeklies
is much worse than the math suggests. The institutional sweet spot
is 30 to 45 DTE, and that is what you should use.

**Stella:** Two reasonable defaults?

**Horace:** Either monthly cycle — write the next monthly on
expiration Friday — or rolling 45 DTE, close at 21 DTE. Pick one
and stick with it.

---

**[IV-RANK — 7:30]**

**Stella:** When do you write?

**Horace:** Watch IV-rank. It tells you where current implied
volatility sits inside the trailing year's range. IV-rank above
30, write. Below 30, wait or scale down. Premium is compensation
for taking the other side of vol — when vol is cheap, the
compensation is too small to be worth the cap on upside.

**Stella:** This is the same logic as everything else you teach —
don't trade when the price is bad.

**Horace:** That is exactly right. The tail wags the dog — the tail
is implied vol. If you ignore IV-rank you
are mechanically getting a worse deal than the market is offering
you in any given month. The covered-call writer who skips the
bottom-quintile IV-rank months has historically improved their
Sharpe by about 25%.

---

**[ROLLING — 10:00]**

**Stella:** When the stock approaches your strike, what do you do?

**Horace:** Two rules. If the call goes in the money and you do not
want to be assigned, roll up and out — buy back the current strike,
sell a higher one further out in time. The new tenor has to be at
least one cycle longer or you cannot roll for a credit. If you
cannot roll for a credit, accept assignment — paying to defend a
covered call is almost always worse than letting the shares go.

**Stella:** And the other direction?

**Horace:** If the stock has fallen and the call is deep
out-of-the-money, roll down and out — buy it back for pennies, sell
a lower strike further out. That locks in most of the original
premium and resets the position. This is the mechanic that makes
covered calls work in flat-to-down markets — you keep re-striking
lower as the stock drifts.

---

**[TAX — 12:00]**

**Stella:** Tax implications?

**Horace:** Premium is short-term capital gain in a U.S. taxable
account. Top-bracket rate is 37% federal plus state. So if your
headline yield is 12%, your after-tax yield is roughly 6-7%. The
largest unspoken fee in long-only investing is tax. A
high-turnover income overlay in a taxable account is the
most tax-inefficient thing you can do.

**Stella:** The fix?

**Horace:** Run the strategy in an IRA or 401(k). Premium is
tax-deferred or, in a Roth, tax-free. Assignments do not generate
taxable events. You get the full strategic flexibility for free.
For most readers covered calls belong in retirement accounts, not
taxable accounts.

---

**[BUY-WRITE ETFS — 14:00]**

**Stella:** People ask: why not just buy QYLD or JEPI?

**Horace:** Look at this chart.

[VISUAL: image/week27_qyld_vs_spy.png]

**Horace:** $1 in QYLD in 2014 versus $1 in QQQ. QYLD ended at
about $1.85, QQQ ended at about $5.50. QYLD distributed 11-12% a
year — that is real cash — but the NAV slowly bled lower because
QYLD writes at-the-money calls every month. ATM means delta 0.50,
which means the strategy caps almost the full upside in any given
month. Over a decade that math is brutal.

**Stella:** And JEPI?

**Horace:** JEPI is structurally less aggressive. It uses
equity-linked notes that approximate selling 5-10% OTM calls on the
S&P 500 — so the upside cap is gentler. Roughly 9-10% per year
versus SPY's 13% per year, with materially lower drawdown. It is a
defensible product for a retiree wanting a smoother ride. QYLD I
do not recommend. But neither beats running the strategy yourself,
because the buy-write ETFs cannot pause in low-IV-rank months and
you can.

---

**[INTERACTIVE WALKTHROUGH — 16:00]**

**Stella:** Tell us about the call writer.

**Horace:** The interactive at the end of the lesson lets you pick
SPY, QQQ, or IWM, pick a target delta — 10, 16, 30, or 50 — and
pick a tenor — 7, 14, 30, 45, or 60 DTE. It computes the premium
using Black-Scholes with the historical implied vol, the
annualised yield-on-cash, the breakeven, and the probability OTM
at expiry. Below the calculator there is a delta ladder showing
how the same five strikes compare side by side.

**Stella:** Spin the knobs.

**Horace:** Spin them. Notice how 50-delta on QQQ at 30 DTE shows
about 30% annualised yield but a 50% chance of assignment. That is
what the buy-write ETF is doing every month. Then look at 16-delta
30 DTE — 5-7% annualised, 16% assignment odds, full retained
upside on most months. That is what disciplined retail writing
looks like.

---

**[OUTRO — 17:30]**

**Stella:** The wheel?

**Horace:** Week 30. We bolt the cash-secured put from Week 28 onto
the front of the covered call from this week, and we have the
strategy I genuinely think most retail accounts should run inside
their IRAs. Sell puts at the price you would happily buy. If
assigned, sell calls at the price you would happily sell. Repeat.
Covered calls are half of that wheel, and now you know how to run
that half properly.

**Stella:** Next week — cash-secured puts. See you then.
