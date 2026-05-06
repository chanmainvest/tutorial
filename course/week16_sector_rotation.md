# Week 16: Sector Rotation — Which Slice of the Market Wins in Each Phase

---

## Part 1: Reading Section

---

### 1. Why This Is Important

The S&P 500 is not one thing. It is eleven things stitched together
under a single ticker. In any given calendar year, the spread between
the best-performing GICS sector and the worst can run 60-90 percentage
points. In 2022, energy returned +64% while communication services
returned -38% — a 100-point spread inside a single index. The
"market" returned -18%. None of the eleven sectors actually did that.

If you understand which slice of the market wins in each phase of the
business cycle, you have the rough outline of one of the durable
alpha sources: **sector rotation**. Capital
cycles between sectors on predictable macro and rate shifts. Ride the
rotation and the cycle pays you. Fight it and you spend a decade
underperforming a passive S&P investor who never opened the app.

Four reasons this matters even if you decide not to rotate.

1. **It is a real alpha source.** Unlike stock picking — where the
   academic evidence is ugly — sector tilts have empirical backing.
   Defensive sectors outperform in late-cycle and recession
   regimes; cyclicals outperform in early- and mid-cycle. The
   pattern is messy, the timing is hard, but the structural story
   has played out repeatedly since the data started in the 1960s.
2. **It tells you what the market is *thinking*.** When utilities
   and staples lead for three months while financials and
   discretionary lag, the market is voting on a slowdown — and
   doing it before any economist has confirmed one. Reading sector
   leadership is reading the macro bid in real time.
3. **It contextualises your equity drawdown.** When your tech
   stocks fall 30% and energy is up 50%, the issue is not "tech
   is broken." It is that the discount rate for long-duration cash
   flows just doubled. Knowing the cycle prevents you from selling
   the wrong sector at the wrong time.
4. **Most retail rotation loses.** Alpha is the rare gap, not the
   default — and the data on retail sector rotators is consistently
   worse than buy-and-hold the index. Knowing the framework is
   necessary to even attempt it, and even then most attempts fail.
   Decide honestly whether you are running rotation as a hobby or
   as a real edge.

This lesson covers the eleven GICS sectors and their SPDR ETFs, the
canonical cycle map, why the map breaks (2020 flipped the script in
four weeks), the momentum-vs-mean-reversion question at the sector
level, and the brutal honest reality of retail rotation P&L.

---

### 2. What You Need to Know

#### 2.1 The Eleven GICS Sectors and Their SPDR ETFs

The Global Industry Classification Standard (GICS), maintained jointly
by S&P and MSCI, divides every listed company into one of eleven
sectors. State Street's SPDR family runs an ETF for each, all with
expense ratios under 0.10% and combined assets above $200B. They are
the canonical retail vehicles for sector exposure.

| Sector | ETF | What's in it |
|---|---|---|
| Technology | XLK | Microsoft, Apple, NVIDIA, Broadcom, semiconductors, software |
| Financials | XLF | JPMorgan, Berkshire, banks, insurers, exchanges |
| Health Care | XLV | UnitedHealth, Eli Lilly, J&J, drugmakers, devices, hospitals |
| Consumer Discretionary | XLY | Amazon, Tesla, Home Depot, autos, hotels, restaurants, retail |
| Communication Services | XLC | Meta, Alphabet, Netflix, telecoms, media (split out from tech in 2018) |
| Industrials | XLI | GE, Caterpillar, Boeing, defense, rails, airlines, machinery |
| Consumer Staples | XLP | P&G, Costco, Walmart, Coke, Pepsi, household goods, tobacco |
| Energy | XLE | ExxonMobil, Chevron, oil and gas E&P, services, refiners |
| Utilities | XLU | NextEra, Duke, electric and water utilities, regulated monopolies |
| Real Estate | XLRE | American Tower, Prologis, REITs (split out from financials in 2016) |
| Materials | XLB | Linde, Sherwin-Williams, chemicals, metals, paper, packaging |

Two notes on the structure.

First, **XLRE and XLC are recent.** Real estate was carved out of
financials in September 2016; communication services was carved out
of technology and discretionary in September 2018. Most of the long
historical data we have is therefore on nine sectors, not eleven.
For the 2010-2024 backtests we run later, treat XLRE and XLC as
"data starts mid-decade" and don't over-fit to their short history.

Second, **GICS classifications are not always intuitive.** Amazon is
discretionary, not tech. Tesla is discretionary, not industrials.
Visa and Mastercard are tech, not financials. Walmart is staples,
Costco is staples, but Target is discretionary. The mental model
"tech = software + chips" is tighter than the actual XLK basket;
the mental model "financials = banks + insurers + exchanges" is
roughly right after XLRE was carved out.

#### 2.2 The Canonical Cycle Map

The folk wisdom — repeated in every CFA textbook and most strategist
notes — is that sectors lead and lag in a predictable order through
the four phases of the business cycle. The map looks like this:

![Schematic four-quadrant cycle map. Horizontal axis is the business cycle phase from early recovery on the left, through mid-expansion, late expansion, to recession on the right. Vertical axis distinguishes cyclical sectors (top) from defensive sectors (bottom). The four quadrants are filled with the sectors that historically lead in each phase: early = financials and consumer discretionary and industrials; mid = technology and communication services and industrials; late = energy and materials and health care; recession = consumer staples and utilities and health care. A thin grey arrow loops through the four quadrants in clockwise order to indicate the rotation.](image/week16_cycle_map.png)

The story behind the map.

- **Early recovery** — rates have been cut hard, the yield curve is
  steep, credit is loosening, consumer pent-up demand starts
  spending. **Financials** earn on the steep curve and on falling
  loan losses. **Consumer discretionary** rides the wage and
  confidence rebound. **Industrials** ride the inventory restock.
- **Mid-expansion** — growth is broad, capex turns on, business
  software and infrastructure spending accelerates. **Technology**
  and **communication services** lead as long-duration cash flows
  re-rate higher under still-low rates. **Industrials** keep working.
- **Late expansion** — capacity is tight, inflation lifts, the Fed
  is hiking. **Energy** and **materials** lead because their input
  is the inflation. **Health care** starts working because investors
  begin reaching for quality and stable demand.
- **Recession** — earnings are falling, rates are being cut, fear is
  the dominant emotion. **Consumer staples**, **utilities**, and
  **health care** lead — the products people need rather than want.
  Long Treasuries, gold, and cash are the cross-asset winners.

The map is real. It is also not nearly as clean as the textbook
draws it, which is the next subsection.

#### 2.3 The Yearly Heatmap — The Map Versus Reality

The chart below is the actual 2010-2024 record: each year's annual
total return for each SPDR sector ETF, coloured by decile within
that year. A green cell means the sector was in that year's top
decile; a red cell means it was in the bottom decile.

![Heatmap of annual total returns for the eleven SPDR sector ETFs from 2010 through 2024. Rows are the eleven sectors (XLY, XLP, XLE, XLF, XLV, XLI, XLB, XLRE, XLK, XLC, XLU); columns are years. Each cell is shaded by where that sector ranked within that year's eleven returns: the top-ranked sector is the deepest green, the bottom-ranked is the deepest red, with neutral colours in between. Numbers inside each cell show the actual annual return percent. The S&P 500 row at the bottom (SPY) sits in the middle of every year by construction. Visible features: tech (XLK) leads most of 2013-2020 and 2023-2024; energy (XLE) is the worst sector for years 2014-2020 then explodes to the top in 2021-2022; 2022 is the year nearly every cell is red except XLE, XLU, XLP; 2023 reverses sharply with tech and communication services on top.](image/week16_sector_winners.png)

Read the chart with three questions.

First, **does the canonical map hold?** Pick any clean cycle phase
on the chart and check. 2010-2011 was textbook early recovery, and
financials *underperformed* badly (XLF -17% in 2011) because the
European debt crisis hit US banks hard. That is not in the cycle
map. 2018-2019 was textbook late-cycle, and energy was the
worst-performing sector both years. Also not in the map.

Second, **what years does the map fit?** 2017 — mid-expansion —
tech leads, materials and industrials work, staples lag. Clean.
2022 — inflation shock that rhymes with late-cycle — energy
crushes everything, materials and staples hold up, tech and
discretionary collapse. Also clean.

Third, **what years break it?** 2020 broke it in four weeks. The
COVID recession started in February 2020 with utilities and staples
leading, exactly as the map says. By April, with the Fed at zero
and Congress having passed $5T of fiscal stimulus, technology had
flipped to the year's leadership and energy was finishing -33%.
The recession was officially over in April. The "recession sector"
playbook had three months of validity in a downturn that re-rated
in weeks rather than years.

The honest read: **the cycle map is a statistical tendency, not a
calendar.** It works in the average year of the average cycle.
Individual years are dominated by individual catalysts — the 2008
financial-system crisis, the 2014-2016 oil collapse, the 2020 COVID
shock, the 2022 rate shock, the 2023 AI mania — and these
catalysts override the cycle whenever they show up.

#### 2.4 Momentum vs Mean Reversion at the Sector Level

This is the momentum-vs-mean-reversion question, scaled down from the
whole market to the eleven slices. Two playbooks both have empirical
support:

- **Momentum.** Buy the sector that has been working. Hold for 3-12
  months. Sell when it stops working. The trend-following literature
  shows positive risk-adjusted returns at the sector level over
  decades — the same way it does at the asset-class level.
- **Mean reversion.** Buy the sector everyone hated last year, sell
  the one everyone loved. At horizons longer than a year, sector
  rankings revert. Energy in 2020 (worst sector, then best in 2021).
  Tech in 2022 (worst, then best in 2023). The cycle of leadership.

Both are true. The hard part — exactly as in #8 — is recognising
which regime is active. Some markets reward momentum; others reward
mean reversion. Most of the academic evidence points to **3-12 month
momentum and 3-5 year mean reversion** as the rough horizons that
have separated. Inside that band, the strategies cancel.

Practically, the retail investor who buys "the sector that just had
a great year" is usually expressing mean-reversion-as-mistake — they
are buying at the top of a 12-month momentum run that is about to
reverse. The investor who buys "the sector that just had its worst
year in a decade" is more often right than wrong, *if* they can hold
through the additional drawdown that frequently comes before the
revival. Either playbook needs the discipline to size for survival
and a clear stop on what proves the thesis wrong.

#### 2.5 The Brutal P&L of Retail Rotation

Here is the part the textbooks leave out. The interactive lab below
this lesson lets you pick up to four sectors and plot their
2010-2024 cumulative return against the S&P 500 with a single
toggle. Run a few combinations:

- **All-tech rotation (XLK only).** Beats SPY handily over the full
  window. End wealth roughly 2.0x the index. Looks like genius.
  Until you check the year-by-year, where 2022 cost you -28% while
  the index lost -18%, and most retail attention-driven rotation
  trades happen *after* the +50% year, not before it.
- **Buy the previous year's winner, every year.** Trail the
  S&P 500 by 4-6 percentage points annually over 2010-2024. The
  textbook momentum trade, executed naively, loses to passive.
- **Buy the previous year's loser, every year.** Roughly matches
  the S&P, with much higher volatility. The textbook
  mean-reversion trade, executed naively, ties.
- **Equal-weight all eleven.** Slightly lags SPY (which is
  cap-weighted) over the window. Works in years where the
  mega-caps are not running away (2014-2016, 2022); lags in years
  when they are (2020-2021, 2023-2024).

The decade's retail rotators have lost not because rotation is
wrong, but because the version they ran was: chase last quarter's
winner, sell on the first 10% drawdown, repeat. That is not
rotation. That is performance-chasing in fancy clothes.

The professional version of rotation — overlay on top of a passive
core, tilt by a few percentage points based on the cycle and
positioning data, never bet the portfolio on a single sector — is
where the alpha lives. The retail version, run as a substitute for
the passive core, almost always underperforms.

The honest framing: **most retail readers are better off with the
S&P 500 and a 10-15% sector tilt at most.** That tilt can give you
the win-some flavour of the cycle without the structural risk of
betting the portfolio on next year's leadership map.

#### 2.6 The Practical Toolkit

Three ways retail investors actually use sector ETFs:

1. **Tilt, don't bet.** Overweight one or two sectors by 5-10% of
   the portfolio relative to S&P weights. If the tilt is wrong by
   5 percentage points of return, the portfolio impact is 25-50bps
   — survivable. If the tilt is right, you get a modest premium
   over the cycle. This is the only rotation discipline that
   survives most retail temperaments.
2. **Defensive flip on hard signals.** The yield curve invert, the
   PMI drop below 50, jobless claims trend up — these are
   late-cycle signals. Some investors run the rotation only at
   these triggers: tilt to staples, utilities, health care, and
   reduce equity beta. Hold the defensive tilt until the curve
   un-inverts and the Fed cuts. This is Horace's preferred shape:
   asymmetric risk-on / risk-off rather than continuous rotation.
3. **Alpha tranches in conviction sectors.** Within a
   sector you understand, you can own the seniors (the cap-weighted
   ETF), the juniors (mid-cap names), and the explorers (small-cap
   options or single names). When the sector cycles into favour,
   the tranches re-rate in order, and the explorers carry the
   biggest payoff. Energy 2020-2022 was the textbook example —
   XLE up 1.6x, mid-cap E&Ps up 3-5x, distressed shale survivors
   up 10-30x. This is the playbook for sector conviction, *not* a
   recipe for blanket rotation.

The interactive lab below lets you mix the sectors and see how
each combination behaves against SPY. Run a few. The discipline
the chart will teach you, faster than any textbook, is that
beating SPY by tilt is harder than the cycle map makes it look.

---

### 3. Common Misconceptions

1. **"The cycle map is a calendar."** It is a statistical tendency.
   In any individual year, sector returns are dominated by the
   year's specific catalyst (oil shock, banking crisis, COVID, AI
   mania). The cycle is one variable; it is rarely the dominant one.
2. **"Tech is always the winner."** Tech led 2013-2021 and 2023-2024
   and was the *worst* sector in 2022, the *worst* sector in 2008,
   and one of the worst over 2000-2002. The "always" is a recency
   bias from a decade of falling rates.
3. **"Defensives never grow."** Healthcare returned 200%+ over
   2010-2019 with materially lower volatility than the S&P. "Defensive"
   means lower beta, not zero growth. The compounding is real, just
   smoother.
4. **"Energy is dead."** Energy was the worst sector for most of
   2014-2020 and the *best* sector in 2021 and 2022. ESG mandates
   that dumped it on the way down had to buy it back at higher
   prices on the way up. Buying what passive flows have abandoned
   was the trade.
5. **"I'll rotate based on the headlines."** Headlines lag price by
   3-6 months. By the time CNBC is running "the recession is here"
   on the chyron, defensives have already led for two quarters.
   Rotation works only if you front-run the consensus, which is
   most retail traders' weakness, not strength.
6. **"All sectors revert to the mean."** Energy didn't from 2014
   to 2020 — it kept being the worst sector for six straight years.
   Mean reversion is a long-horizon tendency that can take a
   decade to play out, and "right but early" is operationally
   indistinguishable from "wrong" — the market can stay irrational
   longer than you can stay solvent.
7. **"Sector ETFs are diversified."** XLK is 45% Microsoft + Apple +
   NVIDIA. XLC is 40% Meta + Alphabet. XLY is 25% Amazon + Tesla.
   The "sector" is often a leveraged bet on three names. The S&P
   500 is more diversified than most of its sector slices.
8. **"Sector rotation is the same as factor investing."** It isn't.
   Factors (value, momentum, quality, low-vol) cut across sectors.
   You can be long the value factor and own all eleven sectors.
   Sector rotation is one specific tilt; factor investing is a
   different framework that often produces *opposite* sector bets
   from the cycle map.

---

### 4. Q&A Section

**Q: What's the simplest sector tilt I can run on top of an S&P 500 core?**
A: Hold 80-90% in SPY (or VOO), and use the remaining 10-20% to
overweight one or two sectors by conviction. If you think we're
late-cycle, that 10-20% goes to XLV and XLP. If early-cycle, XLF
and XLY. Rebalance annually. The portfolio risk impact stays
modest, and you participate in the rotation at the margin.

**Q: How do I tell which phase of the cycle we're in?**
A: Yield curve slope, PMI level, jobless claims trend, and Fed
policy direction together give you a 70%+ confident read. We cover
the indicators in detail in Week 10. Roughly: yield curve inverted
+ PMI below 50 + claims rising + Fed cutting = late-cycle into
recession. Curve steep + PMI rising + claims falling + Fed cutting
hard = early recovery. Most signals never give you the textbook
configuration; you go with the majority of indicators.

**Q: Can I just buy whatever sector worked last year?**
A: That is the naive momentum trade and over 2010-2024 it has
slightly underperformed the S&P. The reason is selection bias —
the previous year's winner is often the one most likely to mean-revert
in the next year. The 12-month momentum signal that academics
document works at 1-3 month rebalancing horizons, not annual.

**Q: What about leveraged sector ETFs?**
A: Avoid. Daily-rebalanced 2x and 3x ETFs decay over time due to
volatility drag, often losing money even when the underlying sector
is roughly flat. They are intraday speculation tools, not investments.

**Q: Is energy a buy in 2026?**
A: This course doesn't pick names. The framework: energy has
underperformed since the 2022 peak, oil is range-bound, ESG
selling has eased, and the S&P 500 weight is below 4%. By the
principle of buying what passive flows have abandoned, the
structural setup is more attractive than the ten years from
2010 to 2020. Whether that translates to next year's return
depends on demand, geopolitics, and the dollar.

**Q: How does sector rotation interact with the four-tranche framework?**
A: Once you have a sector conviction, the tranches tell you *how* to
express it. ETF for the senior exposure. Mid-cap names you've
researched for the junior leg. Long-dated calls on small-cap names
or pre-revenue specs for the explorer leg, sized so the loss is
survivable. The cycle gives you the sector; the tranches give you
the expression.

**Q: What's wrong with rotating into staples and utilities for the
recession?**
A: Two things. One, by the time the recession is the consensus
narrative, those sectors have already had their move; you're
late. Two, in a deflationary recession (1929-1932, 2008-2009)
even staples and utilities sell off; they only outperform on a
*relative* basis. The defensives playbook works best in shallow
recessions with quick Fed responses (2001, 2020). It can hurt
in long bear markets where everything goes down together.

**Q: Why did the 2020 cycle break the map?**
A: COVID was a four-week recession from a markets perspective.
The Fed cut to zero in 9 days, Congress passed $5T of stimulus
in 6 weeks, and the discount rate on long-duration cash flows
collapsed. Tech (long-duration) re-rated immediately; energy
(short-duration commodity demand) collapsed because nobody was
driving. The map assumes a multi-quarter transition. 2020 didn't
give one. Future shocks may also not give one.

**Q: How do US sector classifications differ from international?**
A: GICS is global. The same eleven sectors exist in Europe and
Asia. Sector weights differ — the US is roughly 30% tech,
Europe is 5%; Europe is heavier in financials and industrials.
But the framework transports. We restrict to US-only across this
course; ex-US sector tilts are out of scope here.

**Q: Should I use sector ETFs in a tax-advantaged account or
taxable?**
A: Either works. Sector ETFs are tax-efficient — most are organised
as RICs with low turnover. The tradeable advantage is that
rotating between sector ETFs in a taxable account triggers
capital-gains events; in a 401(k) or IRA, it doesn't. If you
plan to actually rotate, do it in the tax-deferred account.

**Q: What's the single highest-conviction sector tilt for someone
who follows the structural-flow argument?**
A: Horace's bias is toward what passive flows have abandoned.
In April 2026 that is a coin-flip among energy (post-2022
peak, ESG-divested), small-cap value (a decade out of favour), and
the financial sector (post-2023 regional bank scare). None of these
are textbook recommendations; they are positions taken on top of a
broad-index core, sized so being wrong for two years doesn't
threaten the rest of the portfolio. The core is still the S&P 500.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Sector Rotation — Which Slice of the Market Wins in Each Phase
**RUNTIME TARGET:** ~18 minutes
**HOSTS:** Horace, Stella

---

### INTRO (0:00 – 1:30)

**[VISUAL: title card "Week 16 — Sector Rotation"]**

**Stella:** Welcome back to *Investing for Beginners*. Last week we
talked about correlation between asset classes — stocks versus bonds,
bonds versus gold, all of that. This week we drop one level deeper.
We open the equity box, and we look at what's inside.

**Horace:** Inside the S&P 500 there are eleven different machines.
Each one runs on a different fuel. In a year where the index returns
fifteen percent, those eleven machines may have produced returns from
plus fifty to minus thirty. The "fifteen percent" is just the
weighted average. None of the machines actually did fifteen.

**Stella:** And the question for today is — can we predict which
machine wins in which year? Or which phase of the cycle?

**Horace:** Partially. Statistically. With a lot of caveats. Let's
get into it.

### PART 1 — The Eleven Slices (1:30 – 4:00)

**Stella:** Eleven sectors, organised by GICS. Tell me what each one is.

**Horace:** Three big ones first — tech, financials, healthcare.
Tech is XLK, ticker. Microsoft, Apple, NVIDIA, software, chips. About
30% of the S&P. Financials is XLF — JPMorgan, Berkshire, banks,
insurers. About 13%. Healthcare is XLV — UnitedHealth, Eli Lilly,
J&J, drugmakers, devices. Around 12%.

**Stella:** That's already 55% of the index in three sectors.

**Horace:** Right. The next batch — discretionary XLY, communication
XLC, industrials XLI. Discretionary is Amazon and Tesla and Home
Depot. Communication is Meta and Alphabet and Netflix; that one
got carved out of tech and discretionary in 2018, which is why if
you read pre-2018 sector data you won't see XLC.

**Stella:** And the small ones?

**Horace:** Staples XLP — Costco, Walmart, P&G, Coke. Energy XLE —
Exxon, Chevron, oil and gas. Utilities XLU — NextEra, Duke. Real
estate XLRE — REITs; that one got carved out of financials in 2016.
Materials XLB — chemicals, metals, packaging. Each of those last
five is between 2 and 6% of the index.

**[VISUAL: image/week16_cycle_map.png]**

### PART 2 — The Canonical Cycle Map (4:00 – 7:00)

**Stella:** OK, so the textbook story is each of these eleven leads
the market in a different phase of the business cycle.

**Horace:** Right. Here's the map. Early recovery — the Fed has cut,
the economy is bottoming, the curve is steep. Banks borrow short and
lend long, so the steep curve is great for them. Pent-up consumer
demand spends — discretionary works. Industries restock — industrials
work. Real estate rallies because rates have collapsed. So the
left-side quadrant is XLF, XLY, XLI, XLRE.

**Stella:** And mid-expansion?

**Horace:** Growth is broad, capex turns on, businesses upgrade
their software and infrastructure. Tech and communication services
lead. Industrials keep working. That's XLK, XLC, XLI on the top
right.

**Stella:** Late cycle.

**Horace:** Late cycle is the inflation phase. Capacity is tight,
wages are rising, the Fed is hiking. Energy and materials are the
input to the inflation, so they win. Healthcare starts working
because investors reach for quality. XLE, XLB, XLV at the top of
the right side.

**Stella:** And recession.

**Horace:** Recession is the products-people-need phase. Staples,
utilities, healthcare. XLP, XLU, XLV. People still buy toothpaste
and electricity even when they're laid off. The earnings of those
sectors are roughly stable while the cyclicals collapse. That's
the bottom right of the map.

**Stella:** Beautiful diagram. Now tell me why it doesn't work.

### PART 3 — The Heatmap That Breaks the Map (7:00 – 10:30)

**[VISUAL: image/week16_sector_winners.png]**

**Horace:** This is fifteen years of actual sector returns,
2010 through 2024. Each row is a sector, each column is a year.
Green cells are the year's top performers, red cells are the
bottom. Read it across.

**Stella:** OK, 2011 first. Was that early-cycle?

**Horace:** Roughly. Two years out of the 2008-2009 trough. Map
says financials should lead. What happened?

**Stella:** XLF down 17%.

**Horace:** Worst sector that year. The European debt crisis hit
US bank stocks hard. Stress on Italian and Spanish sovereigns,
contagion to US bank balance sheets. The cycle map didn't see
that coming. The cycle map can't see *anything* coming — it's a
long-run average.

**Stella:** What about 2017?

**Horace:** 2017 is the textbook mid-expansion year. Tech up 34%,
financials up 22%, industrials up 23%, materials up 24%. Staples
up 13%, utilities up 12% — defensives lag. Map works.

**Stella:** And 2020?

**Horace:** 2020 is where the map breaks. February: COVID, market
crashes 35%, utilities and staples lead exactly as the map says.
By April, the Fed is at zero, Congress has passed five trillion
dollars of stimulus. By December, tech is up 44% on the year, energy
is down 33%, and the recession that started in February officially
ended in April. The whole "recession sectors lead" playbook had
about ten weeks to be right. The map assumes a multi-quarter
transition. The 2020 cycle didn't give one.

**Stella:** And 2022?

**Horace:** 2022 was the inflation shock. Energy +64%. Communication
services -38%, tech -28%, discretionary -36%. The S&P returned
-18%. None of the eleven sectors actually returned -18%. Six were
worse, five were better.

**Stella:** So the map is — what, half right?

**Horace:** The map is a statistical tendency. It works in the
average year of the average cycle. Individual years are dominated
by individual catalysts — oil shocks, banking crises, pandemics,
rate shocks, AI manias. When the catalyst is bigger than the cycle,
the catalyst wins.

### PART 4 — Momentum vs Mean Reversion (10:30 – 13:00)

**Stella:** Every market has two readings, momentum or
mean reversion. Same applies to sectors?

**Horace:** Yes. And the empirical answer is: at three to twelve
months, momentum works. At three to five years, mean reversion
works. In between, the strategies cancel.

**Stella:** Translate that.

**Horace:** If a sector has been beating the market for the last
six months, the academic evidence says it tends to keep beating
the market for another six months. That's sector momentum. If a
sector has been the worst for three straight years, it tends to
be one of the best over the next three years. That's mean
reversion.

**Stella:** So the retail trade of "buy whatever did best last
year" — what is that?

**Horace:** That is performance chasing. It uses the wrong horizon.
Twelve-month momentum captured at calendar-year boundaries is
mostly already mean-reverting by the time you buy it. The
academic momentum signal works at three-month rebalancing.
Annual rebalancing on the previous year's winner has slightly
underperformed the S&P over the last fifteen years.

**Stella:** And buying last year's loser?

**Horace:** Roughly matches the S&P, with much higher volatility.
The classic mean-reversion trade, executed naively. Better than
performance chasing, but no better than buy and hold.

### PART 5 — The Brutal Honest P&L (13:00 – 16:00)

**[VISUAL: course/interactive/week16_sector_lab.html]**

**Stella:** Show me the lab.

**Horace:** This interactive lets you toggle on up to four sectors
and see their cumulative return against SPY from 2010 through
2024. Click XLK only.

**Stella:** XLK alone over the period — about 6.2x your money.

**Horace:** SPY is roughly 4.5x. So XLK alone beats SPY by a
meaningful amount cumulatively over fifteen years. Looks like a
winning rotation.

**Stella:** What's the catch?

**Horace:** Two things. One, this is hindsight — you didn't know
in 2010 that tech would dominate. Picking it now is easy. Two,
that 6.2x has a -28% year inside it (2022) that most retail tech
holders sold near the bottom of. The drawdowns of single-sector
holdings are deeper than the index, and the behavioural exit rate
is higher.

**Stella:** Toggle on XLE.

**Horace:** Energy alone over 2010-2024 — about 1.7x your money.
The S&P 500 was 4.5x. Energy was the worst sector for most of
the decade. Then it had a +54% year, +65% year sequence in 2021
and 2022 that pulled it from way underneath up to roughly even
with the cumulative index over the last three years. The rotation
trade in energy was real — but you had to wait six years of
underperformance to get paid.

**Stella:** Add XLU and XLP.

**Horace:** Now you're up to four sectors. Defensives plus tech
plus energy. Equal-weight rebalanced annually, that combination
returned roughly the same as SPY over the period, with similar
volatility. So the four-sector tilt added basically nothing
relative to just buying the index.

**Stella:** That's the take-home, isn't it.

**Horace:** That's the take-home. The cycle map is real. It works
in the long-run average. But the retail version of rotation —
chase last year's winner, sell on the first 10% drawdown, repeat —
loses to buy and hold by 4 to 6 percentage points per year. The
professional version — small tilts, multi-sector, signal-driven —
might add 1 to 2 percentage points of alpha. Most retail readers
don't have the discipline for the professional version.

### PART 6 — Practical Use (16:00 – 17:30)

**Stella:** OK so what do I actually do with this lesson?

**Horace:** Three things. One — know the map. Read sector
leadership in real time as a macro signal. When utilities lead
for a quarter, the market is telling you it's afraid. Listen.
Two — tilt, don't bet. Five to ten percent overweight in one or
two sectors based on the cycle. The risk impact is bounded; the
upside is real. Three — when you have genuine conviction in a
sector, use the four-tranche framework. ETF for the senior leg,
mid-caps for the junior leg, options or single-name specs for the
explorer. The cycle gives you the sector. The tranches give you
the expression.

**Stella:** And what we're not telling people to do?

**Horace:** Don't run sector rotation as a *replacement* for the
S&P 500 core. The data is brutal. Most retail rotation
underperforms, and the underperformance is larger when the
investor is most active. Run rotation as a 10-20% overlay. Keep
the core boring and broad.

### OUTRO (17:30 – 18:00)

**Stella:** Next week — we look at the small-cap premium. Or what
*used* to be a premium, and isn't really anymore. Spoiler: the
small-cap premium has eroded, and we'll explain why.

**Horace:** Until then — read the cycle map, but don't worship it.

**Stella:** See you next week.

**[VISUAL: outro card with "Next week: Small-cap premium — alive
or dead?"]**
