# Side Lesson 01: The TI BA II Plus — Your Working Tool

---

## Part 1: Reading Section

---

### 1. Why This Is Important

There is exactly one piece of hardware that shows up in CFA exam halls,
on bond-desk seats, in valuation interview rooms, and on the desks of
serious retail investors who model their own positions: the **Texas
Instruments BA II Plus**. It has been the industry default since the
1980s and remains the calculator that every certification body either
permits explicitly (CFA, CMT, CIPM) or specifies by name (CFA, again).

The honest question is: *if I can do all of this in a spreadsheet, why
should I learn the calculator?* Three reasons:

1. **You build intuition for the cash-flow sign convention.** A
   spreadsheet hides what direction the money is flowing. The BA II
   Plus refuses to let you forget. Press the keys wrong and it returns
   `Error 5` — "no solution exists." That feedback loop is precisely
   the one a beginner needs.
2. **You speak the language professionals speak.** Every finance
   conversation about *time value of money* is conducted in the
   five-key vocabulary the calculator enforces: `N`, `I/Y`, `PV`,
   `PMT`, `FV`. Once those are reflexive, every loan, every bond,
   every dividend-discount model collapses into one sentence.
3. **You catch your own spreadsheet errors.** The calculator and
   the spreadsheet are two independent implementations. If your DCF
   model in Excel disagrees with the BA II Plus on the same inputs,
   one of them is wrong — usually the spreadsheet, because it is
   easier to make an off-by-one period error there.

This side lesson teaches the calculator the way you would learn a
musical instrument: enough theory to know what you are doing, then a
lot of repetitions on canonical problems until your hands know the
keystrokes without your head having to spell them out.

![Procedurally drawn rendering of the TI BA II Plus financial calculator. The five Time Value of Money keys (N, I/Y, PV, PMT, FV) sit on the second row in dark amber. The blue secondary labels above each key (CLR TVM, BGN, P/Y, etc.) are accessed via the 2ND key.](image/side01_calculator.png)

The interactive panel on the website is a working emulator of the
device — you can run every example in this lesson directly in the
browser without buying the physical unit. The static image above is
your reference; the live calculator on the website is your practice
field.

---

### 2. What You Need to Know

#### 2.1 The Five TVM Keys — The Core Vocabulary

Every time-value-of-money problem in finance fits into the same
algebraic identity, expressed in the calculator's five keys:

$$ PV \cdot (1+i)^N + PMT \cdot \frac{(1+i)^N - 1}{i} \cdot (1 + i \cdot \text{BGN}) + FV = 0 $$

The five inputs to that equation are exactly the five keys on the
second row of the calculator:

- **`N`** — number of compounding *periods*. Not years, not months,
  but *periods* matched to the payment frequency. A 30-year mortgage
  paid monthly is `N = 360`, not `30`.
- **`I/Y`** — annual interest rate, entered as a percentage (8 for
  8%, not 0.08). The calculator divides it by `P/Y` internally to
  reach the periodic rate.
- **`PV`** — present value, the value of the money today.
- **`PMT`** — recurring periodic cash flow.
- **`FV`** — future value, the value at the end of the horizon.

The fundamental rule of the calculator: **enter any four of the five,
then press `CPT` followed by the fifth, and the calculator solves for
it.** That is the whole game.

The two auxiliary settings sit above the row:

- **`P/Y`** (`2ND` then `I/Y`) — payments per year (12 for monthly,
  4 for quarterly, 2 for semi-annual, 1 for annual).
- **`BGN`/`END`** (`2ND` then `PMT`) — does the payment happen at
  the *end* of each period (an ordinary annuity, like a mortgage
  payment) or at the *beginning* (an annuity due, like rent paid in
  advance)? The default is `END`. The display shows `BGN` when you
  toggle into begin mode.

#### 2.2 The Sign Convention — Where Beginners Stumble

The BA II Plus uses a strict cash-flow sign convention.

- **Negative** (`-`) = money leaving your pocket (an outflow).
- **Positive** (`+`) = money arriving in your pocket (an inflow).

Asked from your seat:

| Action | Sign |
|---|---|
| Invest $1,000 today | `PV = -1000` |
| Receive $1,500 in 5 years | `FV = +1500` |
| Pay $500 of mortgage every month | `PMT = -500` |
| Receive $2,000 of rent every month | `PMT = +2000` |
| Borrow $300,000 from the bank | `PV = +300000` *(money to you)* |
| Pay back the loan in full | `FV = 0` *(loan extinguished)* |

If `PV` and `FV` carry the same sign, the calculator believes money is
flowing the same direction at both ends of the timeline — which makes
no economic sense for almost any real problem — and returns `Error 5`.
That error is a *feature*: the calculator is telling you the problem
as you posed it has no solution because the cash-flow story is
contradictory. Re-read the problem and check signs.

#### 2.3 Three Canonical Problems — The Calculator's Hello World

These are the three patterns that show up endlessly. The interactive
demo on the website has each pre-loaded as a "Try it" preset so you
can watch the keystrokes execute and read the same answer.

**Problem 1 — Future value of a lump sum.**
You invest $10,000 today at 8% per year for 20 years. What does it
become?

| Step | Keystroke | Display |
|---|---|---|
| Reset | `2ND` `FV` (`CLR TVM`) | `0.00` |
| | `2ND` `I/Y` set `P/Y = 1` | `P/Y=1` |
| Periods | `20` `N` | `20.00` |
| Rate | `8` `I/Y` | `8.00` |
| Outflow today | `10000` `+/-` `PV` | `-10,000.00` |
| No periodic payment | `0` `PMT` | `0.00` |
| Solve | `CPT` `FV` | **`46,609.57`** |

That number — $46,609.57 — is the price of compounding for 20 years at
8% real, in nominal dollars. (The Week 1 lesson is about why an *8%
real* number is fictional; the *math* of the calculation, however, is
exactly this.)

**Problem 2 — Mortgage payment.**
You borrow $300,000 over 30 years at 6.5% annual interest, paid
monthly. What is the monthly payment?

| Step | Keystroke | Display |
|---|---|---|
| Reset | `2ND` `FV` | `0.00` |
| Set monthly | `2ND` `I/Y` set `P/Y = 12` | `P/Y=12` |
| Periods (30 × 12) | `360` `N` | `360.00` |
| Annual rate | `6.5` `I/Y` | `6.50` |
| Loan to you | `300000` `PV` | `300,000.00` |
| Loan paid off at end | `0` `FV` | `0.00` |
| Solve | `CPT` `PMT` | **`-1,896.20`** |

The negative sign is the calculator reminding you the payment leaves
your pocket each month. Multiply by 360 and you have paid roughly
$682,632 to retire a $300,000 loan — the rest is interest, which is
the deeper point most homeowners do not internalise the first time
they sign the papers.

**Problem 3 — Bond yield to maturity.**
A bond costs $950 today, pays a $50 coupon every year for 10 years,
and returns $1,000 at maturity. What is its yield to maturity?

| Step | Keystroke | Display |
|---|---|---|
| Reset | `2ND` `FV` | `0.00` |
| Annual | `2ND` `I/Y` set `P/Y = 1` | `P/Y=1` |
| Periods | `10` `N` | `10.00` |
| You pay today | `950` `+/-` `PV` | `-950.00` |
| Coupon to you | `50` `PMT` | `50.00` |
| Par at maturity | `1000` `FV` | `1,000.00` |
| Solve | `CPT` `I/Y` | **`5.66`** |

Why does the answer come out *higher* than the 5% coupon? Because you
bought below par. Every dollar of the $50 discount you got at purchase
($1,000 face minus $950 paid) shows up as additional yield over the
ten-year holding period. The calculator does the algebra; you supply
the intuition that *coupon ≠ yield* whenever the price is not par.

#### 2.4 The Cash Flow Worksheet — When Payments Are Uneven

The five TVM keys handle *level* annuities — same payment every period.
Real-world investing problems rarely look that clean. Project evaluation,
uneven dividends, lumpy capex schedules — these all need the **CF**
worksheet (the `CF` key, top row).

The keystroke pattern:

1. Press `CF` to enter the worksheet. The display shows `CF0`.
2. Type the initial cash flow (typically negative for an investment),
   press `ENTER`.
3. Press the `↓` arrow. The display shows `C01`.
4. Type the period-1 cash flow, press `ENTER`. Press `↓`. The
   display shows `F01` — the *frequency* of that cash flow (how many
   consecutive periods it repeats). Type `1` and `ENTER` if it
   happens once, or a higher number if a constant cash flow repeats.
5. Press `↓` again to reach `C02`, and so on, up to `C24`.

Once the cash flows are entered:

- **NPV.** Press `NPV`. The display asks for `I` — the discount rate
  per period as a percentage. Type it, press `ENTER`, press `↓`, then
  `CPT`. The displayed number is the net present value at that
  discount rate.
- **IRR.** Press `IRR`, then `CPT`. The displayed number is the
  internal rate of return — the discount rate that makes NPV equal
  zero.

**Worked example.** A project costs $1,000 today and pays $300 in
year 1, $400 in year 2, $500 in year 3. At a 10% required return,
should you take it?

- `CF0 = -1000`, `C01 = 300`, `C02 = 400`, `C03 = 500`.
- Press `NPV`, set `I = 10`, compute. The result is **$36.91**.
- A positive NPV means the project clears the 10% hurdle by
  $36.91. Take the project (assuming the inputs are right).
- Press `IRR`, then `CPT`. The result is **roughly 12.0%** — the
  discount rate at which NPV would be exactly zero. Since 12% > 10%,
  same conclusion via a different lens.

The interactive emulator on the website includes this exact problem
as a preset; click it and the tape walks you through the keystrokes.

#### 2.5 The Habits That Stop You Making Calculator Mistakes

These five habits, in this order, prevent the most common errors.

1. **Reset before every problem.** `2ND` `FV` clears the five TVM
   registers. The single most common cause of a wrong answer is a
   leftover value in `FV` or `PMT` from the last problem.
2. **Decide P/Y once and stick to a convention.** Many professionals
   keep `P/Y = 1` permanently and manually adjust `N` (multiply
   years by frequency) and `I/Y` (divide annual rate by frequency).
   Others prefer to set `P/Y` per problem. Either is fine; mixing
   the two is what blows up.
3. **Sign the cash flows before you press the keys.** Look at the
   problem. Decide which way each cash flow flows from *your* seat.
   Then enter the signs without hesitation.
4. **Check the BGN flag.** If the problem involves rent, lease, or
   any cash flow paid at the *start* of each period, you need
   `BGN` mode (`2ND` `PMT`). The display shows `BGN` when active;
   if it doesn't, you're in `END`.
5. **Sanity-check the answer.** The calculator does the algebra; it
   does not check that the algebra answers the question you meant
   to ask. A monthly payment of $-189.62 on a $300,000 mortgage
   should immediately strike you as wrong — that would be ten cents
   a day on a city apartment. You have an extra zero somewhere.

#### 2.6 Where the Calculator Stops and the Spreadsheet Begins

The BA II Plus is the right tool for *closed-form* time-value problems
— anything that fits the five-key TVM identity, plus uneven cash flows
through the CF worksheet, plus the bond worksheet (`2ND` `9`) for
clean-price-versus-yield, plus statistical functions (`2ND` `7`,
`2ND` `8`) for quick mean and standard deviation.

It is the *wrong* tool for:

- **Anything iterative or path-dependent.** Monte Carlo, scenario
  analysis, what-if tables — go to the spreadsheet.
- **Anything where you want to keep the inputs visible.** A
  spreadsheet shows you all 360 mortgage payments at once; the
  calculator shows you one number at a time.
- **Anything optimisation-shaped.** Solver in Excel, optimisation
  libraries in Python — the calculator has nothing equivalent.

The professional workflow is to use the calculator to *check* the
spreadsheet, not to *replace* it. They are independent
implementations of the same math, which is exactly why running both
catches errors that running either alone would miss.

---

### 3. Common Misconceptions

**Misconception 1: "I can just use Excel, so I don't need the
calculator."**

Excel is more powerful and more flexible, but it abstracts away the
sign convention that the calculator forces you to face. Beginners who
skip the calculator and go straight to `=PMT()` and `=NPV()` in Excel
routinely build models with reversed signs that produce
plausible-looking but wrong answers. The calculator is a discipline.
Once it is reflexive, the spreadsheet becomes safer.

**Misconception 2: "`N` is the number of years."**

`N` is the number of *compounding periods*, matched to the payment
frequency. A 5-year auto loan with monthly payments has `N = 60`,
not `5`. A 10-year semi-annual coupon bond has `N = 20`, not `10`.
Mismatch this and every TVM answer comes out wrong.

**Misconception 3: "`I/Y` is the periodic interest rate."**

`I/Y` is the *annual* rate. The calculator divides by `P/Y`
internally. If you have a monthly problem with `P/Y = 12` and the
annual rate is 6%, you enter `I/Y = 6`, not `0.5`. (If you instead
keep `P/Y = 1` and adjust manually, then yes, you would type `0.5`.
Pick a convention and stick to it.)

**Misconception 4: "The sign doesn't matter as long as the magnitude
is right."**

The sign is the entire mechanism the calculator uses to know which way
the cash flows. Same-signed `PV` and `FV` will routinely produce
`Error 5`, or worse, plausible-looking gibberish. Never enter a TVM
problem without writing down the sign of every cash flow first.

**Misconception 5: "BGN mode is rarely used and I can ignore it."**

`BGN` matters whenever payments occur at the *start* of each period:
rent paid in advance, lease payments, retirement annuities that pay
at the start of each year, insurance premiums paid up front. The
default is `END`. If the problem says "annuity due" or "payments at
the beginning of the period," toggle `BGN` on (`2ND` `PMT`). The
display will show `BGN` when active.

**Misconception 6: "NPV and IRR always agree on the accept/reject
decision."**

For independent projects with conventional cash flows (one outflow
followed by inflows), they agree. For *mutually exclusive* projects or
for non-conventional cash flows (multiple sign changes), they can
disagree — and IRR can also produce *multiple* roots, none of which
is the "right" rate of return. **When NPV and IRR disagree, trust
NPV.** The orthodox CFA answer to this is the same as the practical
finance answer.

**Misconception 7: "A higher IRR is always a better project."**

IRR has three structural problems: it implicitly assumes intermediate
cash flows are reinvested *at the IRR itself* (rarely true), it can
produce multiple solutions when cash flows change sign more than once,
and it ignores project scale. A 50% IRR on $100 of capital is not
better than a 20% IRR on $1,000,000 — the second project earns more
dollars by orders of magnitude.

**Misconception 8: "The calculator is less accurate than a
spreadsheet."**

The BA II Plus carries 13 digits of internal precision, which matches
or exceeds spreadsheet calculations for ordinary financial problems.
Display rounding to 2 decimals is presentation, not calculation. Where
the two ever disagree on an everyday TVM problem, the spreadsheet is
wrong far more often than the calculator is.

---

### 4. Q&A

**Q1: My calculator returns `Error 5` when I press `CPT I/Y`. What is
wrong?**

A: `Error 5` means *no solution exists for the inputs as you have
entered them*. In nine cases out of ten, the cause is a sign error:
`PV` and `FV` (or `PV` and `PMT`) carry the same sign, telling the
calculator that money flows the *same* direction at every point in
time. That is impossible for an interest-bearing instrument. Reverse
one of the signs and recompute.

**Q2: Should I keep `P/Y = 1` permanently or change it per problem?**

A: Either works. The "permanent `P/Y = 1`" convention is more robust
because it prevents the most common error in the entire calculator:
forgetting to change `P/Y` *back* after a monthly problem and then
computing the next problem at the wrong frequency. Many professionals
adopt it for that reason alone. The cost is that you must manually
multiply `N` by frequency (`30 years × 12 = 360 months`) and divide
`I/Y` by frequency (`6.5% / 12 = 0.5417%`) yourself.

**Q3: How do I price a semi-annual-coupon bond?**

A: Two ways, both correct.

- *With `P/Y = 2`*: `N` = years × 2, `I/Y` = annual yield, `PMT` =
  half the annual coupon, `FV` = par value (typically 1000), then
  `CPT PV`. The result is the dirty (or clean, depending on your
  convention) price.
- *With `P/Y = 1`*: `N` = years × 2, `I/Y` = annual yield ÷ 2, `PMT`
  = half the annual coupon, `FV` = par. Same answer, different
  bookkeeping.

**Q4: How is the CF worksheet different from the TVM keys?**

A: TVM is for *level* (constant) annuities. CF is for *uneven* cash
flows. Use TVM for mortgages, standard bonds at par or premium,
regular savings plans. Use CF for project evaluation, dividend streams
that change year to year, real-estate cash flows with lumpy capex,
and any situation where the period-by-period number is not constant.
NPV and IRR live exclusively in the CF worksheet.

**Q5: How do I handle a deferred annuity (payments start in year 5)?**

A: Two TVM steps. Step one: compute the present value of the annuity
*as of the date payments begin* — that is the value of the annuity at
year 4, the period before the first cash flow. Step two: discount
that value back to today across the deferral period using a separate
TVM calculation with `PMT = 0`. The calculator has no built-in
deferred-annuity function; the two-step decomposition is how every
practitioner handles it.

**Q6: Can the BA II Plus compute Macaulay duration and modified
duration?**

A: Yes — through the bond worksheet (`2ND` `9`). Enter settlement
date, coupon rate, maturity date, redemption value, day count, and
either yield or price. Scrolling down past `YLD`/`PRI` reveals `AI`
(accrued interest), `DUR` (modified duration), and other fields.
Convexity is *not* exposed directly; you compute it manually from two
price points around the current yield, or do it in a spreadsheet.

**Q7: What is the difference between ordinary annuity and annuity due
in calculator terms?**

A: Ordinary annuity = payments at the *end* of each period = `END`
mode (the default). Annuity due = payments at the *beginning* of each
period = `BGN` mode (toggle with `2ND` `PMT`). For a positive interest
rate, an annuity due is always worth slightly more than the same
nominal annuity in `END` mode, by exactly one period of interest —
that is the discount the bondholder pays for the convenience of
getting the money at the start of the period.

**Q8: Why does my mortgage payment come out negative?**

A: Because it leaves your pocket every month. The negative sign is
the calculator telling you the direction of flow. The dollar
*magnitude* is what you write the cheque for; the *sign* is the
calculator's bookkeeping. If you typed `PV` as positive (the bank
hands you the money), then `PMT` must be negative (you hand the bank
the money). If both came out positive or both negative, you have a
sign error somewhere.

**Q9: How accurate is the BA II Plus compared to Excel?**

A: 13 internal digits, matching or beating typical spreadsheet
precision on TVM problems. The display rounds to your chosen format
(2 decimals by default; `2ND` `.` lets you set 0–9). Where the
calculator and Excel disagree on a routine TVM problem, the bug is
almost always in the spreadsheet — usually an off-by-one period or a
misplaced sign in a cell formula.

**Q10: Is there a free way to practise without buying the device?**

A: Yes. The interactive panel embedded in this lesson on the website
is a working emulator of the BA II Plus, including the five TVM keys,
the cash-flow worksheet, NPV, IRR, P/Y settings, BGN/END toggle, and
the canonical examples from this lesson pre-loaded as one-click
presets. It is sufficient for every problem in the rest of the
course. The physical unit is still worth owning if you intend to sit
a CFA exam — they only allow the real device in the hall.

---

## Part 2: YouTube Script

---

**VIDEO TITLE:** The Only Calculator a Serious Investor Actually Needs | Side Lesson 1

**RUNTIME TARGET:** ~14 minutes

**HOSTS:**
- **Horace** (teacher): Experienced retail investor, holding the actual BA II Plus.
- **Stella** (student): Recent graduate seeing the device for the first time.

---

**[INTRO SEQUENCE]**

[VISUAL: Animated logo "Side Lesson 1 — The BA II Plus"]

**Horace:** *(picking up the calculator, holding it to camera)* This
is the most important $40 of finance hardware on the planet. Every
CFA candidate in the world owns one of these. Every bond desk has two
— one in use, one in the drawer because it dies on a coffee spill.
And by the end of this lesson, you will own one too — or at least
know the keystrokes well enough that the version on the website does
the same job.

**Stella:** It looks like the calculator from my high-school maths
class.

**Horace:** That's deliberate. Texas Instruments has changed almost
nothing about the layout since 1991. The silver screen calculator on
your phone has had thirty redesigns; this one has had zero, because
it is already the right shape for the job. Let me show you the *one*
row that earns it the right to live on a finance professional's desk.

[VISUAL: Camera pushes in on the second row of keys.]

**Horace:** Five keys. `N`, `I/Y`, `PV`, `PMT`, `FV`. That row is the
entire vocabulary of time-value-of-money. Mortgages. Bonds. Pension
calculations. Discounting. Compounding. Every retirement projection
your bank will ever sell you. All of it lives in those five keys.

**Stella:** Five keys for everything?

**Horace:** Five keys, plus the rule that you enter four of them and
the calculator solves for the fifth. Watch.

---

**[SEGMENT 1: THE CORE EQUATION]**

[VISUAL: Title card "The Five-Key Identity"]

**Horace:** Mathematically, all five keys plug into one equation.

[ANIMATION: animation/side01_tvm_identity.mp4 — the five-key equation
builds up term by term, each variable replaced by the corresponding
calculator key colour-highlighted as it appears.]

**Horace:** `PV` times `(1+i)^N` is the lump sum growing. `PMT` times
the annuity factor is the stream of regular cash flows growing. `FV`
is the value at the end. The whole identity sums to zero — that is
just the accounting saying *what you put in must equal what you take
out, time-adjusted.*

**Stella:** And the calculator solves for whichever piece I leave
blank?

**Horace:** Correct. Type four of them, press `CPT`, then press the
fifth, and the algebra runs. You don't have to derive anything. You
just have to *sign the cash flows correctly*. Which is the part that
breaks beginners.

---

**[SEGMENT 2: THE SIGN CONVENTION]**

[VISUAL: Title card "Negative = Money Out. Positive = Money In."]

**Horace:** Think of it from your seat. Money leaving your pocket is
negative. Money arriving in your pocket is positive. That is the
entire convention.

**Stella:** What if I get it wrong?

**Horace:** The calculator returns `Error 5` — "no solution exists."
Which is not a bug. It is the calculator telling you the problem you
typed is impossible because the cash flows can't go the same
direction at both ends of time. Re-read the problem, flip the
offending sign, recompute.

[ANIMATION: animation/side01_sign_demo.mp4 — three example cash-flow
timelines (mortgage, bond, retirement annuity) with the signs
colour-coded green for inflow, red for outflow.]

---

**[SEGMENT 3: THREE PROBLEMS YOU WILL SOLVE A THOUSAND TIMES]**

[VISUAL: Title card "Three Hello-World Problems"]

**Horace:** I am going to walk through three problems on the
emulator. *Every* TVM question you ever face is a variation of one of
these.

[VISUAL: cut to the interactive emulator on the website, full screen.]

**Horace:** Problem one. You invest $10,000 today at 8% per year for
20 years. Solve for `FV`.

*(types keystrokes; the LCD reads each value as he goes)*

`20` `N`. `8` `I/Y`. `10000` `+/-` `PV`. `0` `PMT`. `CPT` `FV`.
Result — $46,609.57.

**Stella:** That's almost five times the original deposit.

**Horace:** That's compounding. And it is also Week 1's lie — you
cannot get a steady risk-free 8% in real life. The math is real; the
*availability* of an 8% real yield is the fairy tale. You will see
this calculation in every personal-finance book. Now you know how to
*do* it. Whether to *believe* the inputs is a separate problem.

**Stella:** Got it. Next?

**Horace:** Problem two. Mortgage. Borrow $300,000 over 30 years at
6.5% per year, paid monthly. Solve for `PMT`.

*(types keystrokes)*

`2ND` `I/Y` to set `P/Y = 12`. `360` `N`. `6.5` `I/Y`. `300000` `PV`
— *positive* because the bank hands me the money. `0` `FV` — the
loan is paid off at the end. `CPT` `PMT`. Result — *minus* $1,896.20
every month for thirty years.

**Stella:** And if I multiply that by 360 months…

**Horace:** $682,632. So I borrowed $300,000 and paid back nearly
seven hundred. The other $382,000 is interest. That single
calculation is what every prospective homeowner should look at
*before* they sign.

**Stella:** Last one?

**Horace:** Bond yield. I pay $950 today for a bond, it pays me $50
every year for ten years, and gives me back $1,000 at maturity. What
is my yield?

*(types keystrokes)*

`10` `N`. `950` `+/-` `PV`. `50` `PMT`. `1000` `FV`. `CPT` `I/Y`.
Result — 5.66%.

**Stella:** The coupon was 5%, but the yield is 5.66%? Why?

**Horace:** Because I bought below par. The $50 discount on the
purchase price gets amortised over the ten-year holding period and
shows up as extra return. That is why coupon and yield are not the
same number whenever the price is not par. It's also the entire
intuition for *bond pricing* — which gets a whole week of its own
later.

---

**[SEGMENT 4: UNEVEN CASH FLOWS — THE CF WORKSHEET]**

[VISUAL: Title card "When Payments Are Uneven: NPV and IRR"]

**Horace:** The five TVM keys assume the periodic cash flow is *the
same* every period. Real life isn't like that. So there's a second
worksheet — the `CF` key, top row.

*(walks through entering CF0=-1000, C01=300, C02=400, C03=500 on the
emulator, then NPV at 10% returning $36.91)*

**Horace:** $36.91 of NPV at a 10% discount rate. That means at a
10% required return this project clears the hurdle by $36.91 of
present-value dollars. The IRR — the rate at which NPV is exactly
zero — comes out around 12%, telling me the project earns about 12%
per year if I take it.

**Stella:** And if I had a higher hurdle rate?

**Horace:** Then the NPV would shrink. Above 12% it would go
negative — same project, same cash flows, but no longer worth doing
because my opportunity cost is higher than what the project delivers.

---

**[SEGMENT 5: THE FIVE HABITS THAT KEEP YOU OUT OF TROUBLE]**

[VISUAL: numbered list builds on screen as Horace says them]

**Horace:** Five habits. Drill them.

1. Reset before every problem. `2ND` `FV`. Clears all five
   registers. The single most common error is leftover values from
   the prior problem.
2. Pick a `P/Y` convention and stick with it. I keep mine on
   `P/Y = 1` permanently and adjust `N` and `I/Y` manually.
3. Sign the cash flows *before* you press a key. Negative for
   outflow, positive for inflow.
4. Check the `BGN` flag if the problem mentions rent, lease,
   premium, or "beginning of period."
5. Sanity-check the answer. Does the magnitude make sense? A $189
   mortgage on a $300k loan is wrong by a factor of ten.

---

**[SEGMENT 6: WHEN TO USE THE CALCULATOR, WHEN TO USE EXCEL]**

**Stella:** When does the calculator stop being the right tool?

**Horace:** Anything iterative or path-dependent — Monte Carlo,
scenario tables, optimisation — go to Excel or Python. Anything where
you want to see all the periods at once — the full amortisation
schedule of a mortgage, year-by-year — go to a spreadsheet. The
professional workflow uses both: the calculator *checks* the
spreadsheet on closed-form problems, because they are independent
implementations and any disagreement points to a bug. The bug is
almost always in the spreadsheet.

---

**[OUTRO]**

**Horace:** This is the most boring side lesson in the course, and
it is also the one with the highest leverage. Spend a weekend with
the emulator on the website. Run through the three preset problems.
Then make up your own — sketch a savings goal, sketch a mortgage,
sketch a bond — and run them. Once your hands know the keystrokes
without your head having to spell them out, finance will be easier
for you for the rest of your investing life.

**Stella:** And next lesson, the website has the actual emulator?

**Horace:** Right there beneath the static image. Click any of the
"Try it" presets and watch the keystrokes execute. Then play.

---

**END SCREEN:** "Next: Side 2 — Reading a 10-K Filing"
