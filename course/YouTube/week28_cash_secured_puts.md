## Part 2: YouTube Script

---

**VIDEO TITLE:** Cash-Secured Puts — Getting Paid to Bid Lower (Week 28)
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**Stella:** Welcome back. Last week we covered selling calls on stock you already own — the income side of the wheel. This week we're doing the *other* side: cash-secured puts. The one most retail investors get sold the wrong way.

**Horace:** Yeah, the YouTube version of CSPs is a guy in front of a Lambo telling you to "earn 30% on your idle cash." And I want to spend the first thirty seconds being very direct about this: that framing is wrong. The CSP is not a yield-farming trick. It's a limit-buy order with a rebate. If you remember nothing else from today, remember that line.

**Stella:** Let's open with the mental model.

---

**[SECTION 1 — THE LIMIT BUY WITH A REBATE — 1:00]**

**Horace:** Imagine SPY is at $560 today and I tell you "I'd love to own SPY, but only at $530 — that's about a 5% pullback I'm willing to wait for." If you put a regular limit-buy order at $530 in your account, two things happen. One, the order sits there until it fills or the day ends. Two, you earn nothing for waiting.

**Stella:** And you might cancel it tomorrow when you change your mind.

**Horace:** Exactly. Now replace that limit-buy with a 30-day cash-secured put at the $530 strike. Three things change. The order stays alive for 30 days, not one day. You commit the cash up front so you can't change your mind without buying the put back. And — the part everybody focuses on — the market pays you a few hundred dollars for taking that 30-day commitment. That's it. That's the entire trade. A patience price plus rent.

**Stella:** And the rent compensates you for what, exactly?

**Horace:** Volatility. If SPY went straight to $400 tomorrow, you still have to buy it at $530. The market knows that, and the more nervous people are about the next 30 days, the more they pay you to wear that obligation. That's why VIX-rich environments pay better. It's not a free yield — it's the price of being short volatility.

---

**[SECTION 2 — STRIKE BY DELTA — 3:00]**

**Stella:** Let's bring up the first chart.

[VISUAL: image/week28_csp_yield_curve.png]

**Horace:** This is the annualized premium yield on a 30-day put as a function of strike-delta, computed from Black-Scholes with sigma at 22% and rates at 4%. Read it left to right: 10-delta put, 16-delta, 25-delta, 30-delta, 40-delta, 50-delta. The 50-delta — the at-the-money put — pays the highest premium yield by a mile, easily 5-6x what the 10-delta pays.

**Stella:** And there's exactly one reason you don't sell the 50-delta.

**Horace:** Right. The 50-delta has a 50% chance of finishing in-the-money. The 30-delta has roughly a 30% chance. The 10-delta has roughly a 10% chance. Delta is approximately the assignment probability. So that yield curve is not a yield curve in the bond sense — it's a curve of *risk-paid-for*. Closer to the money, more premium, more assignment.

**Stella:** What's the standard preset?

**Horace:** Three of them. 30-delta if you genuinely want to accumulate the stock and you're willing to be assigned 30% of the time. 16-delta — one standard deviation — for most beginners; the bid is far enough below market that assignment feels like a real bargain. 10-delta if you view the put as pure rent on cash and only welcome assignment in a meaningful drawdown. I sell 16-delta on index ETFs by default. I sell 30-delta only on names I actively want to add.

**Stella:** And the most common beginner mistake?

**Horace:** Always the same one — they pick the highest-premium strike, which is closer to ATM, on a stock they don't really want, because the spreadsheet says the yield is biggest. That's not a CSP, that's a coin flip with a logo.

---

**[SECTION 3 — TENOR AND THETA — 5:30]**

**Horace:** Tenor next. You want to be camped where theta — time decay — is steep. From 60 days to 30 days, the put loses about 30% of its time value. From 30 days to expiry, it loses the other 70%. You want to live in that last 30 days.

**Stella:** Why not weeklies, then? Theta is even steeper.

**Horace:** It is. And gamma is steeper too. Weekly puts get blown out by single-day gaps far more than 30-day puts. PUTW — the institutional CSP ETF — sells one-month puts, not weeklies, and they did the math. 30-45 DTE is the sweet spot for retail. You're far enough into theta that decay is fast and far enough from expiry that one bad day doesn't eat a month of premium.

---

**[SECTION 4 — CAPITAL COST — 7:00]**

**Stella:** A point that gets glossed over in every other CSP video.

**Horace:** Yeah. The collateral cash isn't dead. In April 2026 with T-bills at roughly 4%, your $53,000 sitting against a $530 SPY put is earning about 4% just sitting in the broker's money-market sweep. The put premium is *additive* to that. So the right yield calculation is "T-bill rate plus put-premium-annualized," not just the premium piece.

**Stella:** Numbers?

**Horace:** A 30-day, 16-delta SPY put yielding maybe 0.4% in premium, annualized at 12 cycles, gives you 4.8% on the option leg. Plus 4% on the cash leg. Total 8.8% annualized in a no-assignment cycle. That's the honest number. When you see "CSP yields 25% annualized!" somewhere, that's just multiplying a 30-day premium by 12 and forgetting the cash leg already gives you most of it.

---

**[SECTION 5 — ROLLING AND DEFENDING — 8:30]**

**Stella:** What do you actually do when the trade goes against you?

**Horace:** Four moves. One, do nothing — let it get assigned. That's the *default* on stocks you wanted to buy. Two, buy back at a profit when 50-70% of the premium has decayed. Three, roll down and out — buy the threatened put, sell a lower strike further dated, for a small credit. Four, take the L — close at a loss if your thesis on the stock has changed.

**Stella:** And the thing not on the list?

**Horace:** Doubling down. Selling another contract at the same strike when the first is underwater. That's how a small CSP loss becomes a 30%-of-portfolio loss. The market can stay below your strike longer than you can stay willing to add. Irrationality outlasts solvency — that's the trap, in reverse.

**Stella:** And how often do you actually roll?

**Horace:** Once, maybe twice. After the second roll you're admitting your original thesis was wrong. The third roll is denial. Take the loss.

---

**[SECTION 6 — ASSIGNMENT PSYCHOLOGY — 10:30]**

**Horace:** This is the part I want to spend extra time on. Assignment is not a loss event. It's the buy order you placed 30 days ago, executing exactly as designed.

**Stella:** Walk us through the morning after.

**Horace:** You wake up, your account has 100 shares of SPY where there used to be cash, and SPY is trading $2 below your strike. The instinctive reaction is panic. The correct reaction is: "I just bought 100 shares at $530, I collected $300 in premium, my effective cost is $527, and the market is at $528. I'm slightly *up* on the trade."

**Stella:** And then?

**Horace:** You start writing covered calls on those shares. That's the wheel — Week 27's playbook. CSP, assigned, covered call, called away, CSP again. Each turn of the wheel collects premium twice. The only way the wheel breaks is if you panic-sell the assigned shares the next morning. The shares are not the loss. The panic is.

**Stella:** And the only stocks where assignment is genuinely bad?

**Horace:** The ones you should never have written CSPs on. Meme stocks. Single biotechs. Leveraged ETFs. Anything you wouldn't buy outright at the strike. If you can't say "I'd be happy to take delivery," you're not running a CSP, you're running a casino with extra steps.

---

**[SECTION 7 — PUTW VS SPY — 12:30]**

**Stella:** Bring up the second chart.

[VISUAL: image/week28_putw_vs_spy.png]

**Horace:** PUTW is the WisdomTree CBOE PutWrite ETF. It mechanically sells 30-day, ~2% out-of-the-money SPX puts every month, fully cash-secured. It's the institutional answer to "does systematic put-writing beat just owning the index?"

**Stella:** And the answer is?

**Horace:** No. From January 2016 through December 2024, PUTW returned about 7% annualized. SPY returned about 12%. PUTW had a smaller drawdown in March 2020 — about 22% versus 34% for SPY — and weathered 2018 and 2022 with less pain. But in 2017, 2019, 2021, 2023 — every melt-up year — PUTW lagged badly because it doesn't capture upside above the strike.

**Stella:** So why would anyone do CSPs?

**Horace:** Three reasons. One, you don't want maximum return; you want to build a specific position at a specific price. PUTW is mechanical and indiscriminate. Targeted CSPs aren't. Two, you're inside an IRA where the option income is tax-free, and the equivalent stock-trading strategy would be tax-disastrous — the option wrapper is a tax tool first. Three, you want lower portfolio volatility and you'll accept a small return drag for it. But anyone who thinks "sell puts, beat SPY" is starting from a wrong premise. PUTW is a public counter-example.

---

**[SECTION 8 — TAX — 14:30]**

**Horace:** Tax is identical to Week 27. Put premium is short-term capital gain. Every closed contract, every expired contract. The only exception is when the put is assigned — then the premium reduces the cost basis of the assigned shares, and the holding period for *those shares* starts on the assignment day.

**Stella:** Same conclusion as covered calls?

**Horace:** Same conclusion. In a top-bracket taxable account at 35-37%, your CSP yield is netting two-thirds of headline. Inside a Roth IRA, it's netting all of it. Run the wheel — CSPs and covered calls — inside the IRA. Run the buy-and-hold pieces wherever. Don't run a wheel strategy in a regular brokerage if you can avoid it.

---

**[SECTION 9 — INTERACTIVE WALKTHROUGH — 15:30]**

**Stella:** And the interactive.

[INTERACTIVE: interactive/week28_put_writer.html]

**Horace:** Pick an underlying — SPY, QQQ, AAPL, MSFT, KO. Each has embedded vol and price defaults from April 2026. Pick a target delta — 10, 16, 25, 30. Pick a DTE — 21, 30, 45. The Black-Scholes premium pops out, plus the breakeven, the discount-from-current, the annualized yield-on-cash including the T-bill leg, and the probability of finishing OTM.

**Stella:** And the assignment ladder?

**Horace:** Below the big numbers, there's a scenario ladder: "if you're assigned at $X, your effective cost is $Y, an X% discount from spot." Run it across a couple of strikes for the same underlying — you'll see how the discount-from-spot grows as you move further OTM, and the premium-yield shrinks. That trade-off is the entire game.

---

**[OUTRO — 17:00]**

**Stella:** One-line summary?

**Horace:** A cash-secured put is a 30-day limit-buy order with rent attached. Sell them on stocks you want to own at prices you want to own them at. Don't use the rent to talk yourself into bids you don't believe in.

**Stella:** And the takeaways for the wheel?

**Horace:** Three. CSPs on index ETFs and quality compounders are safe-end activity, never speculation-end — that is the barbell. Run them inside a Roth or traditional IRA, not a taxable account — the option wrapper is a tax tool first. And the premium you collect is a function of how nervous *other* people are, not how clever you are — the option tail wags the equity dog.

**Stella:** Next week we step into spreads — bull-put credit spreads as the leveraged sibling of the CSP, where you don't post the full collateral. See you then.

**Horace:** See you next week.
