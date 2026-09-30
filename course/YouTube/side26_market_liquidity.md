## Part 2: YouTube Script

---

**VIDEO TITLE:** Market Liquidity — How Spreads, Depth, and Crises Actually Work
**RUNTIME TARGET:** ~12 minutes
**HOSTS:** Horace, Stella

---

**[INTRO — 0:00]**

**HORACE:** Welcome back. Today is a side lesson on liquidity, and
it's the lesson that nine out of ten retail investors skip until it
costs them. I'm not going to start with a definition. I'm going to
start with a fact.

**STELLA:** On March 12, 2020, the bid-ask spread on the 30-year
US Treasury — the cleanest, deepest, most liquid security on
Earth — went from under half a basis point to over forty basis
points. That's an eighty-fold blow-out in eight trading days.

**HORACE:** And the Federal Reserve had to put $1.5 trillion of repo
into the market that same week to put it back together. If that can
happen to the 30-year on-the-run, it can happen to whatever you own.
Today we're going to install the vocabulary, the math, and the
historical case studies so you can price liquidity *before* you need
it.

**[VISUAL: image/side26_liquidity_by_size.png]**

---

**[§1 — THREE DIMENSIONS — 1:30]**

**STELLA:** Liquidity has three dimensions. Tightness, depth,
resilience. Tightness is the bid-ask spread. Depth is how much
size is resting at that spread. Resilience is how fast the book
rebuilds after you trade.

**HORACE:** Most retail investors only see tightness — the spread
on their trade ticket. That's like judging a car by its colour. The
deeper questions are: *if I had to sell five times my displayed
size, what price do I get?* — that's depth — and *how long until the
quote comes back?* — that's resilience.

**STELLA:** A normal day, the three move together. A crisis, they
decouple. The spread might still print 2 bps but the depth at that
spread is one share. The first real seller takes the price 10%
lower.

---

**[§2 — THE SIZE-LIQUIDITY CURVE — 3:30]**

**HORACE:** Bid-ask spreads scale with the inverse square root of
market cap. AAPL — a $4 trillion stock — costs you a single basis
point round-trip. A $500 million small-cap costs 50 to 100 basis
points. A $200 million micro-cap can cost 300 basis points just on
the spread, before any market impact.

**STELLA:** That's a 100x to 300x liquidity tax. If two stocks have
the same expected return, the small one needs to outperform the
large one by 200 bps a year just to pay the rebalancing cost.

**[VISUAL: image/side26_liquidity_by_size.png]**

**HORACE:** Look at the chart. Mega-caps cluster at 1 bp.
Large-caps at 3 to 5. The cliff starts at the small-cap line —
$2 billion. Below that the spread is no longer a line; it's a
distribution with a long right tail and a non-trivial mass above
100 bps.

---

**[§3 — ETFs AND THE AP BACKSTOP — 5:00]**

**STELLA:** ETFs are the great liquidity hack. The wrapper trades
1000x more liquidly than the underlying bonds inside it. LQD —
the IG corporate bond ETF — trades two to three billion dollars a
day on screen. The median bond it owns trades on TRACE maybe twice
a week.

**HORACE:** That works because authorised participants — usually
big bank prop desks — arbitrage any gap between the ETF price and
the basket NAV. Buy the cheap leg, sell the rich leg, deliver the
basket for redemption. The arbitrage keeps premium and discount
inside a few basis points.

**STELLA:** Until it doesn't. March 2020. LQD detached from NAV
by 4.6%. HYG by 7%. The AP balance sheets were full — every prop
desk was already long credit, every hedge fund was deleveraging,
nobody had room to take on more inventory.

**HORACE:** The Fed's announcement on March 23 of corporate credit
facilities — SMCCF and PMCCF — closed those discounts in 48 hours.
The Fed barely had to *spend* anything. The announcement was the
backstop. Owning bond ETFs is fine, but don't size them as if they
have stock-grade liquidity in a crisis.

---

**[§4 — THE THREE CANONICAL CRISES — 6:30]**

**STELLA:** Three case studies. Each shows liquidity disappearing
in exactly the regime when investors most needed it.

**HORACE:** August 2007 — the quant unwind. Five long-short equity
hedge funds running similar value and momentum factors all started
selling at the same time. Renaissance lost 6% in 48 hours. Goldman
Global Equity Opportunities lost 30% over a week.

**STELLA:** Nobody's "fundamentals" had changed. The market hadn't
moved much. It was pure liquidity withdrawal in a crowded trade.
The lesson: when you pick factors, you're sharing the trade with
every other quant who picked the same factors.

**HORACE:** May 2010 — the flash crash. A single $4 billion sell
algorithm hit the e-mini S&P at 2:42 PM Eastern. No price
discretion. Liquidity providers — including bona-fide
market-makers — withdrew. The S&P fell 9% in five minutes.

**[VISUAL: image/side26_2020_treasury.png]**

**STELLA:** And March 2020 — the chart on screen. The 30-year
Treasury, the bedrock of the global risk-free curve, with a
40-basis-point bid-ask. Foreign central banks dumping bonds,
hedge funds unwinding basis trades, primary dealer balance sheets
full. The Fed had to put unlimited QE on the table on March 23.

**HORACE:** Three different triggers. Same mechanism. Liquidity
withdraws in a regime that already has too many sellers.
*Vol-tail-wags-dog* is a liquidity statement.
When vol doubles, exit cost quintuples, and it's that second leg
that does the damage.

---

**[§5 — THE FED LIQUIDITY MENU — 9:30]**

**STELLA:** The Fed has built a liquidity toolkit since 2008.
PDCF for primary dealers. MMLF for money market funds. CPFF for
commercial paper. SMCCF and PMCCF for corporate credit. BTFP for
banks holding underwater Treasuries.

**HORACE:** Each facility maps to a specific drained pool. When a
new one is announced, it tells you which pool the Fed is willing
to backstop and which it isn't. In 2023 the BTFP backstopped the
Treasury collateral that was crushing SVB — but the Fed left SVB
equity holders to go to zero. Read the press release.

**STELLA:** And empirically the announcement *is* the bottom on the
liquidity-stressed asset. From March 23, 2020 to year-end LQD
returned 14% and the S&P returned 67% from the March low.

---

**[§6 — INTERACTIVE WALKTHROUGH — 10:30]**

**HORACE:** The interactive lab on the website lets you set three
dials — your order size, your market-cap bucket, and the
volatility regime — and it returns three numbers: effective spread,
market impact, and liquidity-adjusted return.

**STELLA:** Try a $50,000 order in a small-cap during a crisis vol
regime. The lab will show you a 250-basis-point round-trip cost,
which is 2.5% of the trade gone before any view of the underlying.
That's the cost of being wrong about liquidity.

**HORACE:** Now try the same order in SPY at calm vol. Five basis
points. That's the liquidity premium — in reverse. You don't pay it
when you don't need it; you pay it ten-fold when you do.

---

**[OUTRO — 11:30]**

**STELLA:** Three takeaways. One — liquidity is three things, not
one. Spread, depth, resilience. Two — it scales with size:
mega-caps are 100x cheaper to trade than micro-caps and that
matters for any rebalancing strategy. Three — it disappears in
crises, including in markets you would bet your life are immune.

**HORACE:** The four-tranche framework exists for
exactly this reason. You match liability liquidity to asset
liquidity. The cash you need next month sits in T-bills. The
cash you need in twenty years can sit in private credit. Get
that match wrong and the most expensive number on your statement
is the one you didn't see — the spread you paid to exit at the
wrong time.

**STELLA:** Next side lesson, we look at currency hedging. See
you there.
