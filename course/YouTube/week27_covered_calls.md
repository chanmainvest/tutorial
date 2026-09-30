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
