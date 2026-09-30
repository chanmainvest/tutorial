## Part 2: YouTube Script

---

**VIDEO TITLE:** Bonds — Coupons, Prices, and Yields | Week 5

**RUNTIME TARGET:** ~18 minutes

**HOSTS:** Horace, Stella

---

**[INTRO]**

**Horace:** Last week was the 60/40 portfolio. We treated the 40 as
a black box called "Treasuries." This week we open the box.

**Stella:** And inside the box is...

**Horace:** Four numbers and a calendar. That's it. A bond is the
simplest financial instrument on earth. Face value, coupon rate,
maturity, payment frequency. Done. Stocks have nothing this clean.

**Stella:** So why did the simplest instrument blow up the worst in
2022?

**Horace:** Because the *price* of a bond isn't one of the four
numbers. The price is what falls out when you discount those four
numbers at today's market yield. And in 2022, the discount rate
moved more in twelve months than it had in any previous twelve
months on record.

---

**[SEGMENT 1: THE FOUR NUMBERS]**

**Horace:** Let's get concrete. A 10-year US Treasury, 4% coupon,
$1,000 face, semi-annual payments. The contract says: every six
months for ten years, you get $20. At the end, you get the $1,000
back. Twenty payments of $20 plus a balloon of $1,000.

**Stella:** And the price I pay today is not necessarily $1,000.

**Horace:** Correct. The price is whatever today's buyers are willing
to pay for that exact stream of cash. If today's market yield on
ten-year risk is 4%, you pay exactly $1,000 — par. If today's
yield is 5%, you pay less than $1,000, because the $20 coupons
aren't generous enough at 5%. If today's yield is 3%, you pay more
than $1,000, because $20 every six months is more than the market
demands.

**Stella:** And someone always exists on the other side.

**Horace:** That's the part people miss. Every traded bond is
someone agreeing the price is right *and* someone disagreeing.
Nobody is forced to trade. The price is just the level where the
two sides meet.

---

**[SEGMENT 2: THE PRICING FORMULA]**

**Horace:** Here's the equation. Price equals the present value of
every coupon, plus the present value of the face. Discounted at
yield divided by the payment frequency. That's it.

It looks ugly written out — sum from t=1 to mN of C divided by
(1 plus y over m) to the t, plus F divided by (1 plus y over m)
to the mN. It looks ugly. It is not ugly. It is a geometric series
plus a balloon. The sum has a closed form, but you don't need to
memorise the closed form. You need to internalise the *shape*.

**Stella:** Which is?

**Horace:** A bond is one stream of small coupons plus one big
balloon at the end. The coupons together are an *annuity*. The
balloon by itself is a *zero-coupon bond*. Every fixed-income
security in the world is some weighted sum of those two pieces.

---

**[SEGMENT 3: PRICE AND YIELD GO OPPOSITE WAYS]**

**Horace:** The most asked-about feature of bonds. The cash flows
are fixed at issue. Coupons are $20 per period forever. Face is
$1,000 forever. The only thing that changes day to day is the
discount rate the market applies to those fixed cash flows.

**Stella:** Higher discount rate means lower present value.

**Horace:** Right. So higher yield means lower price. Lower yield
means higher price. Always. Without exception. And the relationship
isn't a straight line — it's *convex*. The curve bows toward the
origin. Which means a 1% drop in yield raises price *more* than a
1% rise in yield lowers it. That asymmetry is convexity, and for
long bonds it's substantial.

**Stella:** That sounds like a free lunch.

**Horace:** It's a paid-for lunch. The market knows about convexity
and prices it in. You collect the convexity benefit at the cost of
slightly lower coupon. Week 32 does the math. For now, just notice
the curve in the interactive bends.

---

**[SEGMENT 4: DURATION — THE ONE NUMBER YOU MUST KNOW]**

**Horace:** Not all bonds respond equally to a 1% rate move. Duration
tells you *how much* a given bond's price moves for a 1% yield
change. Here are the three numbers I want you to memorise.

Two-year Treasury: duration about 1.9. Ten-year: about 8.5.
Thirty-year: about 19.

**Stella:** So if rates go up 1%, the long bond falls 19%.

**Horace:** Approximately, yes. And here is the punchline of 2022.
The ten-year yield went from 1.5% to 3.9%. That's a 2.4% move.
Multiply by duration of 8.5. You get an 18% loss.

**Stella:** Which is exactly what happened.

**Horace:** Exactly. Last week we said "bonds had their worst year
since 1937." Now you know *why* in one multiplication. Duration
times yield change. The 60/40 chart isn't mysterious; it's
arithmetic.

---

**[SEGMENT 5: COUPON, CURRENT YIELD, YTM — THREE THINGS, NOT ONE]**

**Horace:** Three numbers people confuse constantly.

Coupon rate. The contract. Fixed at issue. Never changes. Used to
compute the dollar coupon.

Current yield. Coupon dollars divided by current price. What the
income stream alone pays. Ignores the gain or loss at maturity.

Yield to maturity. The internal rate of return on the bond.
Discount rate that makes price equal the sum of present values.
This is the headline yield. Always compare bonds on YTM, not
coupon.

**Stella:** And when the bond trades at par...

**Horace:** All three are equal. When the bond trades at a
discount — price below face — YTM is the highest of the three.
At a premium, YTM is the lowest. The interactive shows you all
three simultaneously.

---

**[SEGMENT 6: CREDIT RATINGS — THE LETTERS THAT LIE TO YOU]**

**Horace:** Quick segment before we look at the chart. When a
company issues a bond, three rating agencies — Moody's, S&P,
Fitch — stamp it with a letter grade. Triple-A at the top.
Down through double-A, single-A, triple-B. That's the bottom of
*investment grade*. Below that is *speculative* or *junk*.

**Stella:** And the chart we're about to look at uses BAA?

**Horace:** Right. BAA is just Moody's spelling for the lowest
investment-grade rung. S&P writes the same thing as BBB.

**Stella:** OK. So I should trust those letters?

**Horace:** Funny you ask. The agencies are paid by the company
*issuing* the bond, not by you, the buyer. The issuer goes
shopping for the best rating it can get. That conflict of
interest has blown up several times. Enron carried
investment-grade ratings until four days before bankruptcy.
Lehman was rated single-A on the morning it failed in 2008. The
entire 2008 housing crisis was driven by tens of thousands of
subprime mortgage securities stamped triple-A and then losing
60 to 100 percent of value. Greek government debt was
investment-grade right up until it traded at 30 cents.

**Stella:** So the rating means nothing.

**Horace:** Not nothing. It's a rough sort. But the *yield
spread* — what real traders are paying to lend to that issuer
right now — is the live signal. When the spread blows out while
the rating is still investment grade, the market is telling you
the rating is wrong. Read the spread, not the letter.

---

**[SEGMENT 7: CREDIT — YIELD SPREAD VS REALISED EXCESS RETURN]**

[VISUAL: image/week05_credit_spreads.png]

**Horace:** A US Treasury is the textbook default-free asset.
Anything else is riskier. The market prices that extra risk by
demanding a higher yield. The *yield difference* — BAA corporate
yield minus 10-year Treasury yield, or option-adjusted spread on
an investment-grade index — that is the credit spread proper.
It's quoted live every day in basis points, and it widens *upward*
when things break.

**Stella:** Okay. So what's this chart?

**Horace:** Different number. Pay attention. This is *realised
annual excess return* — BAA corporate total return minus 10-year
Treasury total return, year by year, since 1928. Same data
family, different question. The yield spread tells you what
traders are pricing today. The bars on this chart tell you what
a buy-and-hold investor actually *earned* holding corporates
instead of Treasuries each year.

**Stella:** And the long-run mean?

**Horace:** Small and positive. About 1 to 2 percent per year on
average. That is the realised credit premium investment-grade
corporate debt has paid above Treasuries over the last century.

**Stella:** And the spikes?

**Horace:** 1932. 1974. 2008. 2020. The four worst credit blow-ups
of the modern era. In each one, yield spreads blew *out* —
upward — corporate prices got marked *down*, and Treasuries
rallied on the flight-to-safety bid. So realised excess return
for that year goes sharply negative on this chart. Corporates
underperformed Treasuries by 10 to 25 percent in a single year.
Fat left tail.

**Stella:** So selling credit insurance...

**Horace:** ...is a structurally negatively-skewed payoff. Steady
small income, rare large losses. Not free yield.

One caveat on this chart: it's annual. Don't use it as a
timing tool. Daily yield spreads can move ahead of equity
bottoms during a credit cycle, and traders watch them live for
exactly that reason. The annual realised-return chart you're
looking at here is too coarse for that job; it tells you the
shape of the long-run payoff, not when the next blow-up starts.

The retail takeaway: hold Treasuries for the diversification
job, not corporates. If you want yield, take it on the equity
side.

---

**[SEGMENT 8: THE FORTY-YEAR BULL MARKET AND THE 2022 BREAK]**

[VISUAL: image/week05_yield_history.png]

**Horace:** This is the most important chart in the entire bond
universe. Ten-year Treasury yield from 1962 through April 2026.

Three regimes. From 1962 to 1981, yields rose. Inflation, Vietnam,
Bretton Woods, the oil shocks. Volcker breaks the back of inflation
in 1981 with a 15.8% peak in the ten-year. From 1981 to 2020, yields
fell. Forty years. Almost uninterrupted. Every shock met with lower
terminal rates than the previous shock. The ten-year hit 0.5% in
2020.

**Stella:** And then?

**Horace:** Then 2022 happened. Yields ran from 0.5% to roughly 5%
in thirty months. As of April 2026 we're sitting around 4.2%, and
the market is debating whether this is a 1980s-style normalisation
or the start of something more durable.

**Stella:** Can yields keep grinding higher from here?

**Horace:** That's the live question. The argument for *higher
for longer* is mechanical. US federal debt is around 120 percent
of GDP. Deficits are running 6 to 7 percent of GDP in peacetime.
And every year the Treasury has to roll over trillions of dollars
of old debt. When a 10-year note issued in 2020 at 0.7 percent
matures in 2030, the Treasury has to refinance it at whatever the
10-year is *that* day. So the average interest rate the
government pays grinds higher year by year. The federal interest
bill has already crossed a trillion dollars annually — more than
the defence budget. That's not a forecast, that's accounting. It
puts upward pressure on the supply of new bonds and downward
pressure on Treasury prices. And the rating agencies have noticed:
S&P pulled the AAA in 2011, Fitch in 2023, Moody's in 2025.

**Stella:** What's the lesson?

**Horace:** This is the regime point, and it isn't original to me.
Howard Marks wrote a memo called *Sea Change* in December 2022
laying out exactly this argument. Ray Dalio's *Changing World
Order* makes the longer-cycle version. Lyn Alden's *Broken Money*
makes the monetary-plumbing version. Druckenmiller has been
shouting about the deficit version since 2022. Different lenses,
same conclusion: the rate regime that made buy-and-hold look easy
is over, or at minimum no longer the safe default.

We have been forty years inside a regime that made passive index
investing look like a free lunch. The regime had a specific macro
signature: falling yields, rising bond prices, expanding equity
multiples, benign correlation between the two. The trigger that
breaks the regime is a *sustained* rise in long yields. We are
watching that trigger fire right now.

It is too early to say the regime is over. It is too late to
pretend nothing has changed. The bond chart is the regime backdrop
to everything else we cover from Week 31 onward.

---

**[SEGMENT 9: TIPS, FLOATERS, AND THE BOND-MARKET PLUMBING]**

**Horace:** Two more pieces and we're done. First: not every
bond is a fixed-rate nominal bond. The two variants you'll meet
fastest as a retail investor are TIPS and floaters.

TIPS — Treasury Inflation-Protected Securities — have a principal
that indexes to CPI. So your dollar coupons grow with inflation.
The yield quoted on a TIPS is the *real* yield, above CPI. The
difference between the regular Treasury yield and the TIPS yield
at the same maturity is the *breakeven* — the inflation rate the
market is pricing in. If actual inflation comes in higher than
breakeven, TIPS win. Lower, nominals win. Two warnings: TIPS
index to *official* CPI, which we already saw in Week 1 has its
own problems, and TIPS lost money in 2022 even with high
inflation because the Fed hiked rates and the duration loss
wiped out the inflation accrual. They're a *relative* trade
against nominals, not a free upgrade. Worth knowing: Canada
stopped issuing new inflation-protected bonds in November 2022
citing weak demand at auction — a useful reminder that even the
sovereign can pull inflation protection off the menu.

Floaters — floating-rate notes — reset their coupon to a
benchmark like SOFR every quarter. So when rates move, the
coupon moves with them and the price barely changes. You're
trading duration risk for reinvestment risk. Floaters were the
right bond to own in 2022 and the wrong bond to own in 2024 once
rates peaked.

**Stella:** And callable, convertible, perpetual...

**Horace:** All real, all add complications, all in the reading
section. Headlines: *callable* means the issuer can redeem
early when rates fall — that's the issuer's option, you wrote
it, so callable bonds yield more. *Convertibles* bundle a bond
with an equity call option — we'll meet those properly in the
options weeks. *Perpetual bonds* never mature — the UK's old
*consols* ran for over 250 years. *Century bonds* run 50 to 100
years — Argentina issued a 100-year US-dollar bond in 2017 and
defaulted on it three years later, which tells you everything
about reaching for yield on long sovereign credit.

**Stella:** Last piece?

**Horace:** How retail actually owns bonds. Almost nobody buys
individual corporates. The bid-ask is wide, the lots are big,
and single-name default risk is real. So retail buys ETFs. LQD
for investment grade, HYG for high yield, BND or AGG for the
broad market. Those solve the diversification problem but
introduce one of their own: most bond indices are *weighted by
amount of debt outstanding*. The biggest weight goes to the
issuer that has *borrowed the most*. That is structurally
different from market-cap-weighted equities, where the biggest
weight goes to the company the market values most. "Buy a
bond ETF and forget it" is not as benign a default as the same
strategy in stocks. Worth knowing.

---

**[SEGMENT 10: THE INTERACTIVE]**

**Horace:** Open the bond pricer panel. Five inputs: face value,
coupon, years to maturity, market yield, and payments per year.
Slide them. Watch the price update.

**Stella:** What should I look for?

**Horace:** Three things. First, set yield equal to coupon. Confirm
the price is exactly face. Second, hold everything constant and
move maturity from 2 years to 30 years. Watch the price-yield curve
bend much harder. That's convexity becoming visible. Third, watch
the duration readout. Notice that as you raise the coupon, duration
falls — high-coupon bonds return cash faster, so they're less
sensitive to the discount rate.

**Stella:** And the duration prediction?

**Horace:** Pick a bond. Read duration off the panel. Move yield by
1%. Multiply. Compare to the actual price change. The approximation
is excellent for small moves and breaks for large moves. That's
where convexity comes in. Save the rigorous version for Week 32.

---

**[OUTRO]**

**Horace:** Bonds are four numbers and a calendar. The price is
discounted cash flow. Yield and price move opposite ways. Duration
is the linear sensitivity. Credit spread is what the market
charges you for taking default risk — small steady premium most
years, big losses in the bad ones, just like writing insurance.
Ratings give you a rough sort but the spread tells you the
truth. The forty-year bull market is the regime that built passive
investing's reputation, and it ended in 2022.

That's the entire bond universe in one paragraph. We will spend
Week 31 on the yield curve, Week 32 on the deeper duration math,
Week 33 on credit, and Week 34 on rate sensitivity across asset
classes. Tonight, slide the interactive until the four-number
contract feels obvious.

**Stella:** Next week?

**Horace:** Gold — the five-thousand-year store of value. Why it
sits in a portfolio at all when it doesn't pay you a coupon or
earn an ROE, and what's actually different about a gold ETF, a
gold futures contract, and a coin in your safe.

---

**END SCREEN:** "Next: Week 6 — Gold: The 5,000-Year Store of Value"
