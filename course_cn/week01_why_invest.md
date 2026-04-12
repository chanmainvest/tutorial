<!-- 此文件需要翻译为简体中文 -->
<!-- This file needs translation to Simplified Chinese -->

# Week 1: Why Invest? The Time Value of Money

Animation reference: `animation/week01_compound_growth.py`

---

## Part 1: Reading Section

---

### a) Why This Is Important

Money sitting idle is money losing value. Every single day, inflation chips away at
the purchasing power of cash stuffed under a mattress or parked in a zero-interest
checking account. Understanding *why* you need to invest is not just a financial
skill -- it is a survival skill in a modern economy.

Consider this: in 1990, a cup of coffee cost about $0.75. By 2025, that same cup
costs $5.00 or more. The coffee did not become six times better. Your dollar became
six times weaker. That is inflation at work, and it never stops.

The time value of money (TVM) is the foundational principle of all finance. It states
that a dollar today is worth more than a dollar tomorrow. This is true for three
reasons:

1. **Inflation** -- prices rise over time, so future dollars buy less.
2. **Opportunity cost** -- money available now can be invested to earn returns.
3. **Risk** -- a promised future payment may never arrive.

If you understand TVM, you understand why investing is not optional. It is the only
way to ensure your wealth grows faster than the economy erodes it.

Here is a stark comparison:

```
  Person A: Saves $10,000/year in a bank account (0.5% interest)
  Person B: Invests $10,000/year in the stock market (avg 10% return)

  After 30 years:
  +-----------+----------------+----------------+
  |           |   Person A     |   Person B     |
  +-----------+----------------+----------------+
  | Deposited |   $300,000     |   $300,000     |
  | Value     |   $323,705     | $1,809,434     |
  | Growth    |    $23,705     | $1,509,434     |
  +-----------+----------------+----------------+
```

Person B has over five times the wealth, despite contributing the exact same amount.
The difference is entirely due to the time value of money and compound growth.

Every year you delay investing is a year of compounding you can never get back.
A 25-year-old who invests $5,000 per year until age 65 at 10% average returns
will have approximately $2.4 million. If that same person waits until age 35 to
start, they will have roughly $900,000 -- less than half, despite only missing
10 years of contributions. The math is unforgiving.

This week's lesson gives you the conceptual foundation for everything that follows
in this course. Master these ideas, and every future topic will make more sense.

---

### b) What You Need to Know

#### 1. Inflation: The Silent Wealth Destroyer

Inflation is the general increase in prices over time. Central banks (like the
Federal Reserve in the US) target about 2% annual inflation, but actual inflation
can vary widely.

```
  The Inflation Effect on $100 Over Time
  (assuming 3% annual inflation)

  Year 0:   $100.00  |========================|  100% purchasing power
  Year 10:   $74.41  |==================      |   74%
  Year 20:   $55.37  |==============          |   55%
  Year 30:   $41.20  |==========              |   41%
  Year 40:   $30.66  |========                |   31%
  Year 50:   $22.81  |======                  |   23%
```

At 3% inflation, your money loses nearly half its purchasing power in just 23 years.
This is called the "real" value of money -- what it can actually buy, as opposed to
the "nominal" value (the number printed on the bill).

**How inflation is measured:**

- **CPI (Consumer Price Index)** -- tracks the cost of a "basket" of goods and
  services that a typical household purchases (food, housing, transportation, etc.)
- **PCE (Personal Consumption Expenditures)** -- the Federal Reserve's preferred
  measure; broader than CPI.
- **Core inflation** -- excludes volatile food and energy prices to show underlying
  trends.

**Historical US inflation rates (approximate averages):**

```
  +----------------+-------------------+
  |    Period       | Avg Annual CPI   |
  +----------------+-------------------+
  | 1930-1940      |     -2.0%        |
  | 1940-1950      |     +5.6%        |
  | 1950-1970      |     +2.3%        |
  | 1970-1980      |     +7.8%        |
  | 1980-2000      |     +3.8%        |
  | 2000-2020      |     +2.1%        |
  | 2020-2025      |     +4.8%        |
  +----------------+-------------------+
```

Notice how inflation spiked in the 1970s (oil crises) and again in the early 2020s
(pandemic supply shocks). These spikes can devastate purchasing power rapidly.

#### 2. Compound Interest: The Eighth Wonder of the World

Compound interest means you earn interest on your interest. It is the single most
powerful force in personal finance.

**The compound interest formula:**

```
  FV = PV x (1 + r)^n

  Where:
    FV = Future Value (what your money grows to)
    PV = Present Value (what you start with)
    r  = interest rate per period (as a decimal)
    n  = number of periods
```

**Example: $1,000 at 8% annual return**

```
  Year  |  Starting  |  Interest  |  Ending
  ------+------------+------------+----------
    1   |  $1,000.00 |    $80.00  |  $1,080.00
    2   |  $1,080.00 |    $86.40  |  $1,166.40
    3   |  $1,166.40 |    $93.31  |  $1,259.71
    5   |  $1,360.49 |   $108.84  |  $1,469.33
   10   |  $1,999.00 |   $159.92  |  $2,158.92
   20   |  $4,315.70 |   $345.26  |  $4,660.96
   30   |  $9,317.27 |   $745.38  | $10,062.66
   40   | $20,106.85 | $1,608.55  | $21,715.40
```

Notice how the interest earned in year 40 ($1,608) is more than the original
investment ($1,000). That is compounding at work.

**Visualizing compound vs. simple interest:**

```
  Value ($)
  |
  |                                              * Compound (8%)
  |                                         *
  |                                     *
  |                                 *
  |                             *
  |                         *
  |                     *
  |                  *
  |               *          ___-----  Simple (8%)
  |            *    ___-----
  |         * ___---
  |       *--
  |     *
  |   *
  |  *
  | *
  |*___________________________________________
  0    5    10    15    20    25    30    Years
```

With simple interest, you earn 8% of the original $1,000 every year ($80/year).
With compound interest, you earn 8% of the *current* balance, which grows each year.
Over long periods, the gap becomes enormous.

**The compounding frequency matters too:**

```
  $10,000 at 12% for 10 years, different compounding frequencies:

  +----------------+--------------+
  | Compounding    | Final Value  |
  +----------------+--------------+
  | Annually       | $31,058.48   |
  | Semi-annually  | $32,071.35   |
  | Quarterly      | $32,620.38   |
  | Monthly        | $33,003.87   |
  | Daily          | $33,194.62   |
  | Continuously   | $33,201.17   |
  +----------------+--------------+
```

More frequent compounding produces higher returns, but the difference diminishes.
The jump from annual to monthly is significant; from daily to continuous, negligible.

#### 3. The Rule of 72

The Rule of 72 is a mental shortcut for estimating how long it takes to double
your money:

```
  Years to double = 72 / annual return rate (%)

  Examples:
  +--------+-----------------------+
  | Return |  Years to Double      |
  +--------+-----------------------+
  |   2%   |  72 / 2  = 36 years   |
  |   4%   |  72 / 4  = 18 years   |
  |   6%   |  72 / 6  = 12 years   |
  |   8%   |  72 / 8  =  9 years   |
  |  10%   |  72 / 10 =  7.2 years |
  |  12%   |  72 / 12 =  6 years   |
  +--------+-----------------------+
```

**Why does this work?** It is a mathematical approximation derived from the
natural logarithm. The exact formula is: t = ln(2) / ln(1 + r), but 72 is close
enough for mental math and has the advantage of being divisible by many numbers.

**You can also use the Rule of 72 in reverse for inflation:**

```
  At 3% inflation, purchasing power halves in: 72 / 3 = 24 years
  At 6% inflation, purchasing power halves in: 72 / 6 = 12 years
  At 9% inflation, purchasing power halves in: 72 / 9 =  8 years
```

This makes inflation tangible. If inflation averages 4%, every 18 years your money
buys only half as much. This is why "safe" savings accounts that earn 1-2% are
actually losing you money in real terms.

#### 4. Opportunity Cost

Opportunity cost is the value of the next best alternative you give up when making
a decision. In investing, it means every dollar has competing uses, and choosing
one means forgoing another.

```
  Decision Tree: What to do with $10,000?

                         $10,000
                            |
            +---------------+---------------+
            |               |               |
       Save in bank    Invest in      Pay off credit
       (0.5% APY)     index fund       card debt
            |          (avg 10%)        (20% APR)
            |               |               |
       After 10 yrs    After 10 yrs   Saved in 10 yrs
       = $10,511       = $25,937       = $31,875
                                       (interest avoided)
```

In this example, paying off high-interest credit card debt has the highest
"return" because you are eliminating a 20% annual cost. This is why financial
advisors often recommend paying off high-interest debt before investing.

**Key insight:** Opportunity cost applies to time as well as money. Every year you
delay investing has a measurable cost, because you lose that year of compounding
forever.

```
  The Cost of Waiting: $5,000/year at 10% return

  Start Age  |  End Age 65  |  Total Invested  |  Final Value
  -----------+--------------+------------------+---------------
      20     |   45 years   |    $225,000      |  $3,616,635
      25     |   40 years   |    $200,000      |  $2,212,963
      30     |   35 years   |    $175,000      |  $1,355,122
      35     |   30 years   |    $150,000      |    $822,470
      40     |   25 years   |    $125,000      |    $491,735
      45     |   20 years   |    $100,000      |    $286,375
```

Starting at 20 instead of 30 means investing only $50,000 more, but ending up
with $2.26 million more. The early years of compounding are disproportionately
valuable.

#### 5. Real vs. Nominal Returns

**Nominal return** is the raw percentage gain on an investment, not adjusted for
inflation. **Real return** is the nominal return minus inflation, representing
actual purchasing power gained.

```
  Real Return (approximate) = Nominal Return - Inflation Rate

  More precisely:
  Real Return = ((1 + Nominal) / (1 + Inflation)) - 1

  Example: 10% nominal return, 3% inflation
  Approximate real return = 10% - 3% = 7%
  Exact real return = (1.10 / 1.03) - 1 = 6.80%
```

**Historical real returns by asset class (US, approximate):**

```
  +---------------------+-----------+-----------+-----------+
  | Asset Class         | Nominal   | Inflation | Real      |
  +---------------------+-----------+-----------+-----------+
  | US Stocks (S&P 500) |  ~10.0%   |   ~3.0%   |  ~7.0%   |
  | US Bonds (10-yr)    |   ~5.0%   |   ~3.0%   |  ~2.0%   |
  | Gold                |   ~7.0%   |   ~3.0%   |  ~4.0%   |
  | Savings Account     |   ~2.0%   |   ~3.0%   |  ~-1.0%  |
  | Cash (mattress)     |   0.0%    |   ~3.0%   |  ~-3.0%  |
  +---------------------+-----------+-----------+-----------+
```

**Critical takeaway:** A savings account earning 2% in a 3% inflation environment
is *losing* 1% of purchasing power per year. Cash under the mattress is losing 3%
per year. Only assets that earn above the inflation rate grow your real wealth.

#### 6. Future Value and Present Value

These are the two core TVM calculations.

**Future Value (FV):** What a sum of money today will be worth in the future.

```
  FV = PV x (1 + r)^n

  Example: What will $5,000 be worth in 20 years at 8%?
  FV = $5,000 x (1.08)^20
  FV = $5,000 x 4.6610
  FV = $23,305
```

**Present Value (PV):** What a future sum of money is worth today.

```
  PV = FV / (1 + r)^n

  Example: What is $50,000 in 15 years worth today at 7%?
  PV = $50,000 / (1.07)^15
  PV = $50,000 / 2.7590
  PV = $18,126
```

**This means:** If someone offers you $50,000 in 15 years, and you could earn 7%
on your money, that offer is only worth $18,126 to you today. If they also offer
you $20,000 right now, the $20,000 today is the better deal.

**Future Value of an Annuity (regular contributions):**

```
  FV = PMT x [((1 + r)^n - 1) / r]

  Where PMT = regular payment amount

  Example: $500/month for 30 years at 8% annual (0.667% monthly)
  FV = $500 x [((1.00667)^360 - 1) / 0.00667]
  FV = $500 x 1,491.57
  FV = $745,785

  Total contributed: $500 x 360 = $180,000
  Total growth: $745,785 - $180,000 = $565,785
```

Your investment growth ($565,785) is more than triple what you actually put in
($180,000). That is the power of consistent investing combined with compounding.

**Present Value diagram -- discounting future cash flows:**

```
  Today     Year 1    Year 2    Year 3    Year 4    Year 5
    |         |         |         |         |         |
    |         $100      $100      $100      $100      $100
    |         |         |         |         |         |
    |    $93.46    $87.34    $81.63    $76.29    $71.30
    |<--------|         |         |         |         |
    |<------------------|         |         |         |
    |<----------------------------|         |         |
    |<------------------------------------|         |
    |<-------------------------------------------------|
    |
    PV = $93.46 + $87.34 + $81.63 + $76.29 + $71.30 = $410.02

    (Discount rate = 7%)
```

Each future $100 is worth less today because of the time value of money. The
further in the future a payment is, the less it is worth today.

#### 7. Putting It All Together: The Investing Imperative

```
  The Three Paths Over 30 Years ($10,000 starting, $5,000/yr added)

                        Do Nothing     Savings Acct    Invest (S&P)
                        (0% return)    (1.5% return)   (10% return)
  +--------------------+-------------+--------------+---------------+
  | Total Contributed  |  $160,000   |   $160,000   |   $160,000    |
  | Final Value        |  $160,000   |   $192,760   |   $987,174    |
  | Real Value (3% inf)|  $65,890    |    $79,379   |   $406,392    |
  | Purchasing Power   |   Lost 59%  |    Lost 50%  |   Gained 154% |
  +--------------------+-------------+--------------+---------------+
```

Only the investor actually grows their wealth in real terms. The saver barely
keeps up. The person who does nothing loses more than half their purchasing power.

---

### c) Common Misconceptions

**Misconception 1: "Investing is gambling."**

Gambling has a negative expected return (the house always wins). Investing in
diversified assets has a historically positive expected return. The S&P 500 has
returned roughly 10% annually over the past century, including the Great Depression,
World War II, the 2008 financial crisis, and COVID-19. Short-term speculation on
individual stocks can resemble gambling, but disciplined long-term investing in
diversified funds is fundamentally different.

**Misconception 2: "I need a lot of money to start investing."**

Many brokerages now offer $0 minimums and fractional shares. You can buy $10 worth
of an S&P 500 index fund. The most important factor is not how much you start with,
but how early you start and how consistently you contribute. Even $50 per month
invested from age 22 grows to over $350,000 by age 65 at 10% average returns.

**Misconception 3: "Saving is the same as investing."**

Saving means putting money aside. Investing means putting money to work. A savings
account earning 0.5% while inflation runs at 3% means you are losing 2.5% of
purchasing power annually. Saving is important for emergency funds and short-term
goals, but for long-term wealth building, investing is essential.

**Misconception 4: "I should wait for the 'right time' to invest."**

Market timing is extraordinarily difficult. Studies consistently show that "time in
the market" beats "timing the market." A Schwab study found that even someone who
invested at the worst possible time each year (the market peak) still significantly
outperformed someone who kept their money in cash waiting for a better entry point.

**Misconception 5: "Compound interest only matters for large sums."**

The percentage works the same regardless of the amount. $100 growing at 10% for
40 years becomes $4,526. The multiplier (45x) is identical whether you start with
$100 or $100,000. The key is the growth rate and the time horizon.

**Misconception 6: "Inflation is always around 2-3%."**

While central banks target 2%, actual inflation can be much higher. The US
experienced 13.5% inflation in 1980. Argentina has seen 100%+ inflation in recent
years. Even in stable economies, inflation can spike due to supply shocks, monetary
policy changes, or geopolitical events. Your investment strategy needs to account
for variable inflation scenarios.

**Misconception 7: "A 10% gain followed by a 10% loss gets you back to even."**

This is mathematically incorrect. $100 + 10% = $110. Then $110 - 10% = $99. You
are actually down 1%. Losses hurt more than equivalent gains help, which is why
managing downside risk matters in investing. A 50% loss requires a 100% gain just
to break even.

```
  Loss/Gain Asymmetry:
  +----------+----------------------------+
  | Loss     | Gain Needed to Recover     |
  +----------+----------------------------+
  |   -10%   |         +11.1%             |
  |   -20%   |         +25.0%             |
  |   -30%   |         +42.9%             |
  |   -40%   |         +66.7%             |
  |   -50%   |        +100.0%             |
  |   -75%   |        +300.0%             |
  |   -90%   |        +900.0%             |
  +----------+----------------------------+
```

**Misconception 8: "The Rule of 72 is exact."**

It is an approximation. It works best for interest rates between 6% and 10%.
At very low or very high rates, it becomes less accurate. For 2%, the actual
doubling time is 35.0 years (Rule of 72 says 36). For 20%, the actual time is
3.8 years (Rule of 72 says 3.6). Close enough for quick mental math, but do not
use it for precise financial planning.

---

### d) Q&A

**Q1: What is the time value of money in simple terms?**

A: A dollar today is worth more than a dollar in the future because (1) inflation
reduces what that future dollar can buy, (2) you could invest today's dollar and
earn a return, and (3) there is always some risk that a promised future payment will
not materialize. This is why lenders charge interest and why investors demand returns
-- they are being compensated for giving up the use of their money now.

**Q2: How does compound interest differ from simple interest?**

A: Simple interest is calculated only on the original principal. If you invest $1,000
at 5% simple interest, you earn $50 every year, regardless of how much has
accumulated. Compound interest is calculated on the principal plus all accumulated
interest. So in year 2, you earn interest on $1,050, not just $1,000. Over long
periods, this difference becomes dramatic. After 30 years, $1,000 at 5% simple
interest becomes $2,500. At 5% compound interest, it becomes $4,322.

**Q3: Why does the Rule of 72 work?**

A: It is derived from the mathematical relationship ln(2) / ln(1 + r), where ln is
the natural logarithm and r is the interest rate. For rates near 8%, 72/r closely
approximates this formula. The number 72 was chosen because it is easily divisible
by 2, 3, 4, 6, 8, 9, and 12, making mental math convenient. Some people use the
"Rule of 70" for lower rates or the "Rule of 69.3" for continuous compounding,
but 72 is the most practical for everyday use.

**Q4: What is the difference between nominal and real returns?**

A: Nominal return is the headline number -- "the stock market returned 10% this
year." Real return adjusts for inflation to show your actual increase in purchasing
power. If the market returned 10% but inflation was 4%, your real return was
approximately 6%. Always think in real terms when evaluating long-term investment
performance, because nominal returns can be misleading in high-inflation environments.

**Q5: How do I calculate the present value of a future sum?**

A: Use the formula PV = FV / (1 + r)^n. Decide on an appropriate discount rate (r)
-- this is typically the return you could earn on alternative investments. For example,
if someone promises you $10,000 in 10 years and you could earn 7% elsewhere:
PV = $10,000 / (1.07)^10 = $10,000 / 1.9672 = $5,083. That future $10,000 is only
worth about $5,083 to you today.

**Q6: What is a good annual return to expect from investing?**

A: The US stock market (S&P 500) has historically returned about 10% per year
nominally, or about 7% after inflation. However, returns vary enormously year to
year. In any given year, the market might return +30% or -30%. The 10% average only
emerges over long time horizons (20+ years). Bond returns have historically been
about 5% nominal (2% real). A balanced portfolio might target 7-8% nominal. Never
assume any specific return is guaranteed.

**Q7: Should I pay off debt or invest?**

A: Compare the interest rate on your debt to the expected return on your investments.
If your debt charges 20% interest (credit cards), paying it off is like earning a
guaranteed 20% return -- better than any investment. If your debt is at 4% (mortgage),
and you expect 10% from investments, investing may be more profitable, though debt
payoff is a guaranteed "return" while investment returns are not. A common strategy:
pay off all debt above 6-7% interest, then invest the rest.

**Q8: Does inflation affect all goods equally?**

A: No. Different categories inflate at different rates. Over the past 20 years in the
US, healthcare and education costs have risen much faster than the overall CPI, while
technology and clothing have often gotten cheaper. The CPI is an average across a
basket of goods, so your personal inflation rate depends on what you actually spend
money on. Retirees, for instance, often face higher effective inflation because
healthcare is a larger share of their spending.

**Q9: What happens if I invest a lump sum vs. regular monthly contributions?**

A: Statistically, lump-sum investing beats dollar-cost averaging (regular
contributions) about two-thirds of the time, because markets tend to go up. However,
dollar-cost averaging reduces the risk of investing everything at a market peak, and
it is more practical for most people who earn a regular paycheck. The best strategy
is usually: invest each paycheck as you receive it. Do not hold cash waiting for a
"better time."

**Q10: Can compound interest work against me?**

A: Absolutely. Compound interest on debt is the mirror image of compound interest on
investments. A $5,000 credit card balance at 24% APR, if unpaid, grows to $14,615 in
just 5 years. This is why high-interest debt is a financial emergency. The same
mathematical force that builds wealth through investing destroys wealth through
unpaid debt.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** Why Invest? The Time Value of Money | Investment Course Week 1

**RUNTIME TARGET:** ~25 minutes

**HOSTS:**
- **Alex** (teacher): Experienced investor, explains concepts clearly
- **Sam** (student): Curious beginner, asks questions the audience is thinking

---

**[INTRO SEQUENCE]**

[VISUAL: Animated logo with text "Investment Fundamentals - Week 1"]

[ANIMATION: A clock ticking while dollar bills slowly shrink in size]

**Alex:** Welcome to Week 1 of our investment fundamentals course. I am Alex, and
this is the lesson that changes how you think about money forever.

**Sam:** And I am Sam. I will be asking all the beginner questions, so do not worry
if you are brand new to this. I am right there with you.

**Alex:** Today we are answering one of the most important financial questions you
will ever face: Why should you invest at all?

**Sam:** Right, because honestly, investing feels risky. Why not just save money in
a bank account where it is safe?

**Alex:** That is exactly where we are going to start. Because the surprising truth
is that keeping your money "safe" in a bank account is one of the riskiest things
you can do with it.

**Sam:** Wait, how is that possible?

[VISUAL: Title card -- "Part 1: The Invisible Thief -- Inflation"]

---

**[SEGMENT 1: INFLATION]**

**Alex:** Let me tell you about the invisible thief that is robbing you right now.
It is called inflation.

[ANIMATION: A basket of groceries. The price tag starts at $50 and slowly ticks
up to $75, then $100, while the basket stays the same size. Reference:
animation/week01_compound_growth.py -- inflation_scene()]

**Sam:** Inflation. I have heard the word, but what does it actually mean for my
wallet?

**Alex:** Inflation means prices go up over time. Not because products get better,
but because the currency loses value. In 1995, a movie ticket cost about four
dollars. Today, it costs fifteen. Same movie experience. But your dollar buys
less.

**Sam:** So my money is getting weaker even if I do not spend it?

**Alex:** Exactly. And here is what makes it dangerous.

[VISUAL: Split screen showing two jars. Left jar labeled "$10,000 in 2005."
Right jar labeled "$10,000 in 2025." The right jar shows items being removed
one by one to represent lost purchasing power.]

**Alex:** If you had put ten thousand dollars under your mattress in 2005 and
pulled it out in 2025, you would still have ten thousand dollars. But that ten
thousand dollars would only buy what about six thousand dollars bought in 2005.
You lost roughly forty percent of your purchasing power by doing absolutely
nothing.

**Sam:** Forty percent? That is huge. But banks pay interest, right? Does that
help?

**Alex:** Let me show you the math.

[ANIMATION: Bar chart comparing "Savings Account Rate: 0.5%" vs
"Inflation Rate: 3%" with a gap labeled "Real Loss: -2.5% per year"]

**Alex:** The average savings account in the US has paid about half a percent
interest in recent years. Meanwhile, inflation has averaged around three percent.
That means every year, your savings account loses about two and a half percent
in real purchasing power.

**Sam:** So I am actually losing money by saving it?

**Alex:** In real terms, yes. And that brings us to the most important concept in
all of finance.

[VISUAL: Title card -- "Part 2: The Time Value of Money"]

---

**[SEGMENT 2: TIME VALUE OF MONEY]**

**Alex:** The Time Value of Money -- TVM for short -- is the idea that a dollar
today is worth more than a dollar tomorrow.

**Sam:** Why? A dollar is a dollar, right?

**Alex:** Think of it this way. If I offer you a thousand dollars right now or a
thousand dollars one year from now, which would you take?

**Sam:** Right now, obviously.

**Alex:** Why?

**Sam:** Because... I could use it now? And who knows what happens in a year?

**Alex:** You just named two of the three reasons.

[VISUAL: Three pillars graphic:
Pillar 1 -- "Opportunity: Invest it now, earn returns"
Pillar 2 -- "Inflation: Future dollars buy less"
Pillar 3 -- "Risk: Future payment might not come"]

**Alex:** First, opportunity. If you have the money now, you can invest it and
earn a return. Second, inflation. That future dollar will buy less than today's
dollar. Third, risk. The person promising you money in the future might not
follow through.

**Sam:** So time literally makes money less valuable?

**Alex:** Unless you put it to work. And that is where investing comes in. Investing
is how you fight the time value of money. Instead of letting time erode your
wealth, you harness time to grow it.

**Sam:** How?

**Alex:** Two words: compound interest.

[VISUAL: Title card -- "Part 3: Compound Interest -- The Eighth Wonder"]

---

**[SEGMENT 3: COMPOUND INTEREST]**

[ANIMATION: Reference animation/week01_compound_growth.py -- compound_scene().
Starting with a single coin, it duplicates. Then each duplicate duplicates.
The pile grows slowly at first, then explosively.]

**Alex:** Albert Einstein reportedly called compound interest the eighth wonder
of the world. Whether he actually said it or not, the math backs it up.

**Sam:** What makes compound interest different from regular interest?

**Alex:** Great question. Simple interest means you earn a fixed percentage on your
original amount every year. Compound interest means you earn interest on your
interest.

[ANIMATION: Side-by-side comparison.
Left side: "Simple Interest" -- $1,000 grows by exactly $80 each year, shown
as equal-sized blocks stacking up.
Right side: "Compound Interest" -- $1,000 grows by increasing amounts each
year, blocks get larger as they stack.]

**Alex:** Let us say you invest one thousand dollars at eight percent. With simple
interest, you earn eighty dollars every year. After ten years, you have one
thousand eight hundred dollars.

**Sam:** That seems fine.

**Alex:** Now with compound interest, in year one you still earn eighty dollars.
But in year two, you earn eight percent of one thousand eighty dollars, which
is eighty-six dollars and forty cents. In year three, you earn eight percent of
one thousand one hundred sixty-six dollars and forty cents.

**Sam:** So each year the interest payment gets bigger?

**Alex:** Exactly. And after ten years, instead of one thousand eight hundred
dollars, you have two thousand one hundred fifty-nine dollars.

[VISUAL: Table on screen:
Simple: $1,000 -> $1,800 after 10 years
Compound: $1,000 -> $2,159 after 10 years
Difference: $359]

**Sam:** Three hundred and fifty-nine dollars more. That is nice but not exactly
life-changing.

**Alex:** You are right. After ten years, it is a nice bonus. But here is where
it gets wild. Let us extend the timeline.

[ANIMATION: Graph showing both curves extending to 40 years. The compound curve
begins to separate dramatically from the simple interest line around year 20,
and by year 40, it is far above.]

**Alex:** After twenty years, the compound interest total is four thousand six
hundred sixty-one dollars versus two thousand six hundred dollars for simple.
After thirty years, it is ten thousand sixty-three versus three thousand four
hundred. And after forty years...

**Sam:** Let me guess -- it gets crazy?

**Alex:** Twenty-one thousand seven hundred fifteen dollars. Compared to four
thousand two hundred for simple interest. Your money has grown to over twenty-one
times what you started with.

**Sam:** From just one thousand dollars?

**Alex:** From just one thousand dollars. And that is without adding a single extra
penny. Just letting compound interest do its thing for forty years.

[VISUAL: Final comparison graphic:
$1,000 at 8% for 40 years:
Simple Interest: $4,200
Compound Interest: $21,715]

**Sam:** Okay, that is genuinely impressive. But who has forty years?

**Alex:** Anyone who starts in their twenties and retires in their sixties. And most
people are not investing just a one-time lump sum. They are adding money regularly.
Let me show you what happens when you combine regular contributions with compound
interest.

[ANIMATION: A piggy bank receiving coins monthly. A growth meter next to it
accelerates upward. Numbers tick from $0 to $500,000 to $1,000,000.]

**Alex:** If you invest five hundred dollars a month starting at age twenty-five,
at an average return of ten percent per year, by age sixty-five you will have
approximately two million six hundred thousand dollars.

**Sam:** Two point six million? From five hundred a month?

**Alex:** Your total contributions would be two hundred forty thousand dollars. The
remaining two point three six million is pure compound growth.

**Sam:** That is ninety percent growth and only ten percent contributions. That is
unbelievable.

**Alex:** That is the power of time plus compounding. And this is exactly why
starting early matters so much.

[VISUAL: Title card -- "Part 4: The Cost of Waiting"]

---

**[SEGMENT 4: THE COST OF WAITING]**

[ANIMATION: Two characters walking side by side. "Early Emma" starts at age 25.
"Waiting Will" starts at age 35. Both walk toward age 65. Emma's wealth bar
grows much taller than Will's.]

**Alex:** Let me introduce you to two hypothetical investors. Early Emma starts
investing five thousand dollars per year at age twenty-five. Waiting Will starts
the same amount at age thirty-five. Both invest until age sixty-five, both earn
ten percent per year on average.

**Sam:** So Emma invests for forty years and Will for thirty years?

**Alex:** Right. Emma invests a total of two hundred thousand dollars. Will invests
a total of one hundred fifty thousand dollars. So Emma puts in fifty thousand
more. But look at the results.

[VISUAL: Comparison bars:
Emma (starts at 25): Invested $200,000 -> Final value $2,212,963
Will (starts at 35): Invested $150,000 -> Final value $822,470]

**Sam:** Emma has almost three times as much money? From only fifty thousand dollars
more in contributions?

**Alex:** One point four million dollars more in final value from fifty thousand
more in contributions. That is a twenty-eight to one ratio. Every dollar Emma
invested in those first ten years multiplied enormously over the next thirty years.

**Sam:** So the early years are the most valuable?

**Alex:** By far. The first dollars you invest have the longest time to compound.
A dollar invested at age twenty-five has forty years to grow. A dollar invested
at age fifty-five only has ten years. The twenty-five-year-old dollar could grow
to forty-five dollars. The fifty-five-year-old dollar only grows to about two
dollars and sixty cents.

[VISUAL: Title card -- "Part 5: The Rule of 72"]

---

**[SEGMENT 5: RULE OF 72]**

**Sam:** This is all great, but doing compound interest math in my head sounds
impossible.

**Alex:** It would be, except there is a beautiful shortcut called the Rule of 72.

[VISUAL: Large "72" on screen with a division sign]

**Alex:** To estimate how many years it takes to double your money, just divide
seventy-two by the annual return rate.

**Sam:** That is it?

**Alex:** That is it. At six percent, your money doubles in twelve years. At eight
percent, nine years. At twelve percent, just six years.

[ANIMATION: A $1 bill doubling into $2, then $4, then $8, then $16, with
timestamps showing the years at 8% return: 0, 9, 18, 27, 36 years]

**Sam:** So at eight percent, one dollar becomes two in nine years, four in
eighteen years, eight in twenty-seven years, and sixteen in thirty-six years?

**Alex:** Exactly. Four doublings in thirty-six years. And here is a great use of
this rule in reverse. You can estimate how fast inflation destroys your money.

**Sam:** How?

**Alex:** At three percent inflation, seventy-two divided by three is twenty-four.
Your money loses half its value every twenty-four years.

**Sam:** So if I am thirty years old and retirement is thirty-five years away, my
money could lose more than half its value if I just hold cash?

**Alex:** More than half. At three percent inflation over thirty-five years, a
dollar is worth about thirty-five cents. You would lose about sixty-five percent
of your purchasing power.

[VISUAL: Dollar bill with 65% of it shaded out/faded, labeled "Lost to Inflation
Over 35 Years (3% annual)"]

**Sam:** That is terrifying.

**Alex:** It should be motivating. Because once you understand this, you understand
that not investing is the real risk.

[VISUAL: Title card -- "Part 6: Real vs. Nominal Returns"]

---

**[SEGMENT 6: REAL VS. NOMINAL RETURNS]**

**Alex:** Before we wrap up, I want to clarify something that trips up a lot of
people. When you hear that the stock market returns ten percent per year, that
is the nominal return.

**Sam:** Nominal meaning the headline number?

**Alex:** Right. The actual number before adjusting for inflation. But what matters
for your purchasing power is the real return -- the nominal return minus inflation.

[ANIMATION: A thermometer-style graphic. "Nominal Return" shows 10%.
"Inflation" shows 3% being subtracted. "Real Return" shows 7%.]

**Alex:** If the stock market returns ten percent and inflation is three percent,
your real return is about seven percent. That seven percent represents your
actual increase in purchasing power -- the additional goods and services you can
now afford.

**Sam:** So I should always think about returns after inflation?

**Alex:** For long-term planning, absolutely. And here is why it matters. Look at
this comparison.

[VISUAL: Table on screen:
Asset           | Nominal Return | After 3% Inflation | Real Return
Stocks          |     10%        |                     |    7%
Bonds           |      5%        |                     |    2%
Savings Account |      2%        |                     |   -1%
Cash            |      0%        |                     |   -3%]

**Alex:** A savings account with a two percent return seems like it is growing your
money. But after three percent inflation, you are actually losing one percent per
year. Cash under the mattress is losing three percent per year.

**Sam:** So stocks are really the only option that significantly grows your wealth?

**Alex:** Over long periods, stocks have been the strongest wealth-building tool
available to ordinary investors. Bonds play an important role too, and we will
cover asset allocation later in the course. But yes, for long-term growth, equities
are the primary engine.

[VISUAL: Title card -- "Part 7: Future Value and Present Value"]

---

**[SEGMENT 7: FV AND PV]**

**Alex:** Let me give you two formulas that will come up again and again.

[VISUAL: Two formula cards side by side:
Left: "Future Value: FV = PV x (1 + r)^n"
Right: "Present Value: PV = FV / (1 + r)^n"]

**Alex:** Future value answers the question: "If I invest this money now, how much
will I have later?" Present value answers the reverse: "What is a future payment
worth to me today?"

**Sam:** Can you give me a real example?

**Alex:** Sure. Say you have ten thousand dollars and you can earn eight percent per
year for twenty-five years. The future value is ten thousand times one point oh
eight to the power of twenty-five. That equals sixty-eight thousand four hundred
eighty-five dollars.

[ANIMATION: $10,000 growing in a bar chart over 25 years, reaching $68,485.
Key milestones highlighted: $21,589 at year 10, $46,610 at year 20.]

**Sam:** Almost seven times the original amount. Nice.

**Alex:** Now the reverse. Your company offers you a bonus of one hundred thousand
dollars payable in twenty years. What is that worth today, assuming you could earn
eight percent investing on your own?

**Sam:** Let me think. One hundred thousand divided by one point oh eight to the
twentieth power...

**Alex:** Which equals...

**Sam:** I have no idea how to calculate that in my head.

**Alex:** It is twenty-one thousand four hundred fifty-five dollars. That future
hundred thousand is only worth about twenty-one thousand today.

[VISUAL: $100,000 shrinking backward through time to $21,455]

**Sam:** So if someone offered me twenty-five thousand dollars right now instead, I
should take the cash?

**Alex:** From a pure time-value-of-money perspective, yes. Twenty-five thousand
now is worth more than one hundred thousand in twenty years, if you can earn eight
percent.

**Sam:** This completely changes how I think about money.

**Alex:** And that is exactly the point of this lesson.

[VISUAL: Title card -- "Key Takeaways"]

---

**[SEGMENT 8: RECAP AND TAKEAWAYS]**

[ANIMATION: Summary slide building point by point]

**Alex:** Let us recap what we learned today.

[VISUAL: Bullet points appearing one by one]

**Alex:** Number one: Inflation silently destroys your purchasing power. At three
percent inflation, money loses half its value in about twenty-four years.

**Sam:** The invisible thief.

**Alex:** Number two: Compound interest is the most powerful force in building
wealth. You earn interest on your interest, and over decades, this creates
exponential growth.

**Sam:** The eighth wonder.

**Alex:** Number three: The Rule of 72. Divide seventy-two by your return rate to
estimate doubling time. Quick, easy, and surprisingly accurate.

**Sam:** Seventy-two divided by the rate. Got it.

**Alex:** Number four: Starting early is more important than investing large amounts.
The first dollars you invest have the most time to compound and create the most
wealth.

**Sam:** Early Emma beat Waiting Will by a mile.

**Alex:** Number five: Always think in real returns, not nominal. What matters is
your purchasing power after inflation, not the raw number in your account.

**Sam:** Ten percent minus three percent inflation equals seven percent real growth.

**Alex:** And number six: Future value and present value are the foundational tools
for evaluating any financial decision. Every investment, every loan, every financial
offer can be evaluated using these concepts.

[VISUAL: Animated graphic showing a timeline from "Today" to "Future" with arrows
showing FV going forward and PV coming back]

**Sam:** So what should someone do right now, today, after watching this video?

**Alex:** Three things. First, check what your savings account is paying. If it is
less than inflation, understand that you are losing money. Second, open an
investment account if you do not have one. Many brokerages have zero minimums and
zero commissions. Third, start investing, even if it is just fifty dollars a month.
The amount matters less than the habit.

**Sam:** Because time is the most important ingredient.

**Alex:** Exactly. Every day you wait is a day of compounding you will never get
back.

[VISUAL: End card with course logo]

**Alex:** Next week, we are going to talk about the easiest, most proven way for
beginners to invest: index funds and ETFs. You will learn why most professional
fund managers cannot beat a simple index fund, and how you can get started with
one for practically nothing.

**Sam:** That sounds great. See you all next week.

**Alex:** Thanks for watching. If you found this helpful, subscribe and hit the
notification bell so you do not miss Week 2. See you then.

[ANIMATION: Outro animation with subscribe button graphic and "Next Week:
Index Funds and ETFs" preview card]

**[END]**

---

*Animation reference for this episode: `animation/week01_compound_growth.py`*
*Next lesson: `course/week02_index_funds_etfs.md`*
