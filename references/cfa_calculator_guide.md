




I got the CFA calculator, the TI one, teach me how to use it.   Not just how to press the button, but all the concerns that related to those calculations.   Make it easy to read and understand, college undergrad level.


Thought for 33s
Awesome—let’s turn your TI BA II Plus (the standard CFA-approved TI calculator) into a power tool. I’ll show you both the how (key strokes) and the why/what to watch out for (concept pitfalls). Everything below works on the BA II Plus and BA II Plus Professional.

0) One-time setup & “panic reset”
Always start each new problem clean:

Clear TVM registers (N, I/Y, PV, PMT, FV): press 2nd → CLR TVM.

Clear cash-flow & worksheet memory: press 2nd → CLR WORK.

Clear general registers (last results, stats lists): press 2nd → CLR REG.

Display precision: 2nd → FORMAT → enter 4 (or 5) → ENTER → 2nd → QUIT.
(4 decimals is a common CFA sweet spot—reduces rounding “drift”.)

Payments/Compounding per year (critical):

2nd → P/Y → set P/Y = C/Y to your compounding/payment frequency (usually 1), ENTER, then 2nd → QUIT.

If you set P/Y = 12, the calculator automatically converts I/Y to a monthly rate in TVM. For most CFA problems you’ll be safer leaving P/Y = 1 and adjusting N and I/Y yourself.

END vs BGN mode (annuity due):

2nd → BGN toggles. Keep it in END unless you know cash flows occur at the period beginning (e.g., lease/rent). The top of the screen shows BGN when it’s on.

⚠️ Biggest beginner mistakes: forgetting to clear registers, leaving BGN on, or having P/Y ≠ intended frequency.

1) Time Value of Money (TVM)
The 6 TVM keys: N, I/Y, PV, PMT, FV, CPT
Sign convention: Money out = negative, money in = positive.

Typical setups
A) Single-sum growth/discount
Given: PV, I/Y (per period), N → find FV.
Steps: Clear TVM → enter PV (negative if you invest it) PV → enter I/Y → enter N → CPT FV.

What to watch out for

I/Y must match the period in N. If it’s 8% annually for 3 years with monthly compounding:

Either set N = 36, I/Y = 8/12 (and P/Y = 1),

or set P/Y = 12 and enter I/Y = 8 (nominal), N = 36 (the calc will internally convert).

Rounding drift: keep 4–5 decimals during work; round only at the end.

B) Level annuities (PMT)
Ordinary annuity (END mode): payments at end of period.

Annuity due (BGN): payments at beginning—turn BGN on.

Example: $500 paid monthly for 2 years at 6% APR, monthly comp.
Approach 1 (manual frequency): P/Y = 1; N=24, I/Y=0.5 (6/12), PMT=500 (set sign), PV or FV unknown → CPT.
Approach 2 (automatic): P/Y=12; I/Y=6 (nominal), N=24, PMT=500.

What to watch out for

BGN vs END (leases, rent, some insurance → BGN).

Include PMT sign correctly. If PV is outflow (−), PMT often is also outflow (−); FV then comes out positive, etc.

C) Solve for rate or number of periods
Enter PV, PMT, FV, N → CPT I/Y.

Or enter PV, PMT, FV, I/Y → CPT N.

What to watch out for

If the result looks crazy (e.g., negative N), check signs and BGN/END.

D) Continuous compounding
Use e^x/LN keys.

FV = PV·e^(r·t). Compute r*t, then 2nd → e^x, multiply by PV.

2) Amortization (loan schedules)
Goal: break a level-payment loan into interest, principal, and ending balance over ranges of periods.

Steps

TVM: Enter N, I/Y, PV (−), PMT, FV=0; CPT PMT if unknown.

2nd → AMORT

Enter period range (e.g., 1 ENTER, then 12 ENTER for Year 1 if monthly payments), then scroll (↓) to see:

INT (interest paid over the range)

PRN (principal paid)

BAL (ending balance)

What to watch out for

The range is inclusive (P1 to P2).

Ensure PMT sign matches an outflow.

3) Cash Flow worksheet: NPV/IRR
Open with CF. You’ll enter CF0, then C01 with F01 (frequency), C02 with F02, etc.

Example

CF0 = −1000 ENTER

C01 = 300 ENTER, F01 = 3 ENTER (meaning 300 for 3 consecutive periods)

C02 = 500 ENTER, F02 = 1 ENTER

Then NPV: enter I (discount rate), ENTER, ↓, CPT NPV.

For IRR: IRR → CPT.

What to watch out for

Sign convention (initial outflow negative).

Discount rate I is per period (must match your cash-flow spacing).

Multiple IRRs: can occur with non-conventional cash flows (sign flips more than once). CFA may ask you to recognize this possibility; NPV profiles or MIRR address it conceptually.

Reinvestment assumptions: IRR assumes interim cash flows reinvested at IRR; NPV assumes reinvestment at the discount rate (WACC/opportunity cost)—more realistic in many CFA contexts.

4) Bonds (price ↔ yield)
You can price bonds either with the BOND worksheet (on BA II Plus/Professional) or with TVM using periodized coupons.

Using TVM (robust for exams)
Map a coupon bond to an annuity + lump sum:

N = total coupon periods (e.g., 10 years, semiannual → N=20)

I/Y = yield per period (e.g., 6% YTM, semiannual → I/Y=3)

PMT = coupon per period (e.g., 8% annual coupon, $1,000 par, semiannual → PMT=40)

FV = par (usually 100 or 1,000 per question statement)

CPT PV (it returns a negative price—take absolute value as price)

Clean vs Dirty price

TVM gives the present value at the coupon date. If settlement is between coupon dates, the BOND worksheet handles accrued interest and day-count.

CFA may ask clean price (without accrued) vs dirty/full price (clean + accrued). Make sure you know which one the question wants.

Day-count/frequency

BOND worksheet takes coupon frequency (annual/semi/quarterly) and day-count convention (e.g., 30/360 or actual/actual). Choose what the problem states.

Yield measures

YTM: solve with TVM or BOND CPT yield.

YTC/Realized yield: adjust N to the call date and FV to call price; include reinvestment rate for realized yield questions.

5) Interest rate conversions (nominal ↔ effective)
Open ICONV (Interest Conversion worksheet):

Set NOM% (nominal annual), C/Y (compounds/year), then ↓ to see EFF% (effective annual).

Or reverse: input EFF% and C/Y, compute **NOM%`.

What to watch out for

EAR vs APR: When discounting annual cash flows, use EAR if the problem cares about effective annual returns; otherwise periodize precisely.

6) Statistics & regression (common for CFA Level I/II)
One-variable stats

2nd → DATA. Make sure LIN (linear) appears at top (press 2nd → STAT to choose LIN).

Enter x1, ENTER, ↓; FREQ1 (usually 1) ENTER, ↓; repeat.

2nd → STAT → scroll for: n, mean (x̄), Sx (sample stdev), σx (population stdev), min, max, etc.

Two-variable stats / regression (LIN)

In DATA, enter pairs as x1, ENTER, ↓, y1, ENTER, ↓, Freq (usually 1).

2nd → STAT → view r, a, b for regression y = a + b·x.

What to watch out for

Clear old lists: 2nd → CLR WORK before entering new data.

Sample vs population stdev: CFA typically uses sample (S) unless stated otherwise.

7) Depreciation (DEPR worksheet)
Open DEPR, input:

LIFE (useful life), COST, SALV, START month; choose method (SL, SOYD, DB with factor like 200% for DDB).
Then scroll through DEPn, BVn per period.

What to watch out for

Switch to straight-line convention for some accelerated methods when it yields higher depreciation—DB methods in the calculator handle this if configured.

8) Date math (DATE worksheet)
Compute days between dates or add/subtract days (useful for accrued interest, T+2 settlement approximations when problems give exact dates).

9) Rounding & exam-style precision
Carry 4–5 decimals internally; report to the question’s requested precision (often 2 decimals for prices/NPV, 3–4 for rates in %).

If the stem gives an “assume 30/360” or specific EAR/APR interpretation, follow it even if it feels non-standard.

10) Quick practice (with keystrokes + commentary)
A) FV of a deposit
Invest −1,000 today at 8% (annual), for 5 years. What’s FV?

Reset; set P/Y=1.

1,000 ± PV; 8 I/Y; 5 N; 0 PMT; CPT FV → 1,469.33
Why: FV = PV·(1+0.08)^5. Sign: PV is outflow, FV is inflow.

B) Price a semiannual 8% bond at 6% YTM, 10 years, $1,000 par
Semiannual periods: N=20; I/Y=3; PMT=40; FV=1,000; CPT PV → 1,148.77 (clean at coupon dates)
Why: Coupon > yield ⇒ price > par. Periodize everything consistently.

C) NPV/IRR with repeated cash flows
CF0=−1,000; Years 1–3: 300 each; Year 4: 500; discount 9%.

CF: CF0 = −1000 ENTER; C01 = 300 ENTER → F01 = 3 ENTER; C02 = 500 ENTER → F02 = 1 ENTER.

NPV: I = 9 ENTER, ↓, CPT NPV → ~−8.06 (slightly negative).

IRR: CPT → ~8.86%
Why: IRR < discount rate ⇒ slightly negative NPV (consistent).

D) Loan amortization snippet
$250,000 mortgage, 6% APR, monthly, 30 years. What’s payment and first-year interest?

P/Y = 12 (or keep P/Y=1 and use I/Y=0.5, N=360). Let’s use P/Y=12.

N=360; I/Y=6; PV=−250000; FV=0; CPT PMT → −1,498.88

2nd → AMORT; set P1 = 1, P2 = 12; scroll to INT → ~14,929. (year-1 interest)
Why: Early payments are interest-heavy; AMORT totals a range.

11) Fast troubleshooting checklist
Result nonsensical? CLR TVM and re-enter.

Payment timing odd? Check BGN indicator.

Wrong scale? Check P/Y and that I/Y matches the period.

IRR won’t compute? Ensure at least one sign change in the cash-flow stream and that CFs are entered correctly.

Bond price off by a few dollars? You might be mixing clean/dirty or day-count.

12) Muscle-memory mini-cheat sheet
Clear everything for a new problem: 2nd CLR TVM → 2nd CLR WORK → 2nd CLR REG

Set decimals: 2nd FORMAT → 4 ENTER

Set annual mode: 2nd P/Y → 1 ENTER → 2nd QUIT

Annuity due: 2nd BGN (toggle on/off)

NPV/IRR: CF → enter CFs → NPV (set I) or IRR

Amortization: compute PMT in TVM → 2nd AMORT

EAR/APR: ICONV

Logs/exponentials: LN, 2nd e^x

If you want, I can tailor a 1-page printable reference with your preferred settings (e.g., always P/Y=1) and a few practice sets in your favorite topic (bonds, IRR traps, or amortization).







I got the CFA calculator, the TI one, teach me how to use it. Not just how to press the button, but all the concerns that related to those calculations. Make it easy to read and understand, college undergrad level.

Perfect — you’ve got the Texas Instruments BA II Plus, the official calculator allowed in CFA exams. Let’s go through how to really use it, not just press buttons, but also why you’re doing things and the common pitfalls.
This will be written in plain, easy college-level English with short sections, examples, and quick notes.

🧭 Overview: Why the BA II Plus Matters
The BA II Plus isn’t just for number crunching — it’s for financial logic. The CFA exam assumes you understand:

What inputs mean (e.g., PV, FV, I/Y, N)

How compounding and time value of money work

When to reset memory or switch modes (like degrees vs. radians, decimals, etc.)

You’ll mostly use it for:

Time Value of Money (TVM) problems

Cash flow analysis (NPV, IRR)

Bond pricing and yield

Depreciation and breakeven

Statistics (mean, standard deviation, regression)

⚙️ Step 1. Basic Setup (Always Do This!)
Before you start any CFA-style question, reset your calculator.

🔁 Reset
Press:

2nd → CLR TVM
2nd → CLR WORK
2nd → CLR ALL
This clears previous data so you don’t mix old values into new problems.

🧮 Decimal Settings
Set your decimal display:

2nd → FORMAT → 9 ENTER → 2nd → QUIT
That gives you 9 decimal places of internal precision and shows 2 on screen.

📅 P/Y and C/Y (Payments per year)
Most CFA problems assume 1 payment per year:

2nd → P/Y → 1 ENTER → ↓ → 1 ENTER → 2nd → QUIT
Otherwise, your interest rates will come out wrong.

💰 Step 2. Time Value of Money (TVM)
The core keys are:

N = number of periods
I/Y = interest rate per year
PV = present value
PMT = payment each period
FV = future value
Example:
You invest $1,000 for 3 years at 8% compounded annually. What’s the FV?

N = 3
I/Y = 8
PV = -1000
PMT = 0
FV = ?
Press:

CPT → FV
→ FV = 1,259.71

Why the minus sign?
Finance convention: money you pay (outflow) is negative, money you receive (inflow) is positive. This keeps your answers logically consistent.

🧾 Step 3. Annuities and Payments
Example:

You deposit $1,000 each year for 5 years at 6% interest. What’s the FV?

N = 5
I/Y = 6
PV = 0
PMT = -1000
FV = ?
CPT → FV
→ FV = 5,637.09

Ordinary vs. Annuity Due
If payments are at the end of each period (most common): END mode
If payments are at the beginning (like rent): BEGIN mode

2nd → BGN → 2nd → SET → 2nd → QUIT
Then switch back to END later.

💵 Step 4. Bonds
You’ll use TVM again here.

Example:

A bond has 8% annual coupon, $1,000 face value, 10 years to maturity, and yields 10%. Find its price.

Each year you get $80 coupon.

N = 10
I/Y = 10
PMT = 80
FV = 1000
CPT → PV
→ PV = -875.38 (price)

📈 Step 5. Cash Flow, NPV, IRR
For uneven cash flows:

CF → CF0 = -1000 ENTER ↓
C01 = 300 ENTER ↓
C02 = 400 ENTER ↓
C03 = 500 ENTER
Then:

NPV → I = 10 ENTER → ↓ → CPT → NPV
→ NPV = 64.20

Then for IRR:

IRR → CPT → IRR
→ IRR = 12.3%

🪙 Step 6. Depreciation (MACRS, SL, DB)
Depreciation mode:

2nd → DEPR
Then set:

LIFE = asset life

COST = initial cost

SALV = salvage value

DB = declining-balance rate (e.g., 2 for double declining)

Use arrows to compute DEPR (depreciation), BV (book value), and so on.

📊 Step 7. Statistics Mode (1-Var, 2-Var)
One-variable stats
Enter data:

2nd → DATA
Input:

X01 = 10
X02 = 12
X03 = 14
Then:

2nd → STAT → 2 → ENTER
You’ll get:

Mean (x̄)

Sample std dev (Sx)

Population std dev (σx)

Two-variable regression
2nd → DATA
Enter pairs (X1, Y1), (X2, Y2)...
Then:

2nd → STAT → 5 → ENTER
You’ll get slope (b), intercept (a), correlation (r).

🧠 Step 8. Common Mistakes and Fixes
Mistake	What Happens	Fix
Forgot to clear TVM	Random wrong results	2nd → CLR TVM
Wrong P/Y setting	Interest rates off	P/Y = 1
Sign confusion	Negative FV	Flip sign of PV or PMT
Forgot to switch END/BEGIN	Payment timing errors	2nd → BGN → 2nd → SET
Wrong I/Y (monthly vs. annual)	Unrealistic results	Adjust N and I/Y properly
🎯 Pro Tips for CFA Exam
Always double-check modes: P/Y, END/BEGIN, and decimals.

Label your TVM inputs — write “N=, I/Y=, PV=” on scratch paper first.

Practice speed entry: You’ll save minutes per question.

Know signs logic: Outflow negative, inflow positive.

Use memory carefully: Store interest rates or results with STO and recall with RCL.

Would you like me to make a “CFA exam quick reference sheet” (a one-page summary PDF you can print or save on your phone)? It would include all essential steps, formulas, and shortcut keys neatly formatted.







I got the CFA calculator, the TI one, teach me how to use it.   Not just how to press the button, but all the concerns that related to those calculations.   Make it easy to read and understand, college undergrad level.


Reasoned for 6m 51s

Answer now
Below is a friendly, exam‑ready guide to the Texas Instruments BA II Plus (and BA II Plus Professional). It goes beyond “which button to press” to the why, the common pitfalls, and quick checks so you can trust your answers on CFA-style problems.

0) Big‑picture habits (save you from 80% of mistakes)
Always clear before you solve

TVM registers: 2nd → CLR TVM

Worksheets (CF, BOND, STAT, etc.): 2nd → CLR WORK

Set once for the exam

Decimals: 2nd → FORMAT → set 4–5 decimals (prevents rounding drift).

P/Y (payments per year): 2nd → P/Y → set P/Y = 1 and C/Y = 1.
Why? You’ll manually convert N and I/Y to the periodic values. This avoids hidden conversions and errors.

END mode (not BGN): 2nd → BGN → (if it shows BGN) 2nd → SET to toggle to END → 2nd → QUIT.
Use BGN only for annuity‑due problems (payments at the beginning of each period).

Cash‑flow sign convention: Money you pay (outflow) = negative; money you receive (inflow) = positive. If you violate this, you’ll get nonsense (or errors).

Units & periods: Convert everything to per period consistently.

N = number of compounding/payment periods (not years!)

I/Y = rate per period (not a decimal; enter 6% as 6, not 0.06).

Rounding: Keep calculator at 4–5 decimals; round only in your final written answer.

1) The TVM keys (N, I/Y, PV, PMT, FV)
These five registers solve most CFA time‑value questions.

N: number of periods

I/Y: interest rate per period (enter as a percent)

PV: present value

PMT: payment each period (sign matters)

FV: future value

After entering knowns, press CPT and the unknown key.

End vs Begin (BGN) mode

END mode = payments at period end (ordinary annuity).

BGN mode = payments at period start (annuity‑due). Toggle only when the problem says “payments at the beginning.”

Quick example (ordinary annuity, END mode)

Deposit $500 at the end of each quarter for 5 years at 6% APR, compounded quarterly. Find FV.

We convert to period values:

N = 5 years × 4 = 20

I/Y = 6%/4 = 1.5

PMT = –500 (outflow)

PV = 0

Then CPT → FV → 11,561.83 (≈).
Check: Annuity due? If the question said beginning of quarter, switch to BGN mode or multiply by (1 + 1.5%).

Common pitfalls (TVM)

P/Y not 1 (hidden conversions)—fix by setting P/Y = 1 and doing all conversions yourself.

Wrong sign on PMT/PV/FV (e.g., both PV and FV positive).

Using years for N instead of periods.

2) Amortization (loans and schedules)
Workflow

Solve the loan with TVM (PMT, PV, N, I/Y set correctly).

Open AMORT worksheet (2nd → AMORT).

Enter P1 and P2 (start and end payment numbers to summarize).

CPT to see:

INT (interest paid),

PRN (principal paid),

BAL (ending balance).

Example

$250,000 mortgage, 4% APR, monthly, 30 years. Find the monthly payment and totals for year 1.

Set P/Y = 1; manually convert:

N = 30 × 12 = 360

I/Y = 4%/12 = 0.333333… (enter 0.333333)

PV = 250000, FV = 0, PMT = ?

CPT → PMT → –1,193.54 (payment; negative = outflow)

Amortize P1 = 1, P2 = 12 (first 12 payments):

INT ≈ 9,919.87

PRN ≈ 4,402.59

BAL ≈ 245,597.41

Sanity checks: Payment covers interest + some principal; balance falls.

3) Cash flows, NPV, and IRR (irregular streams)
Use the CF worksheet for uneven cash flows and for capital budgeting.

Steps

CF → enter CF0 (usually negative initial outlay).

Enter C01, C02, … and their F (frequency) if repeated.

NPV → enter discount rate I (as a percent) → ↓ → CPT to compute NPV.

IRR → CPT to compute IRR (be mindful of multiple IRR possibility for non‑conventional cash flows).

Example

CF0 = –1,000; CF1 = 400; CF2 = 350; CF3 = 300; CF4 = 250.
Find NPV at 8% and the IRR.

NPV @ 8% = 92.35

IRR ≈ 12.44%

Concerns & tips

Multiple IRRs occur when signs switch more than once. NPV profile or MIRR might be more informative.

Always check that CF0 sign matches “investment” (negative).

For big data sets, use F (frequency) to avoid re‑typing repeated flows.

4) Bonds (price, yield, accrued interest)
Use the BOND worksheet (labels vary slightly by model; steps are the same).

You’ll typically enter

Settlement date and Maturity date

Coupon rate (annual, as a percent)

Yield (YTM) or Price (solve for the other)

Redemption (par) (e.g., 100 or 1000)

Frequency (1 = annual, 2 = semiannual, 4 = quarterly)

Day‑count (commonly 30/360 or Actual/Actual per the problem)

Example (clean price estimate with standard compounding)

5‑year, 4% annual coupon, semiannual payments, YTM 5%, par $1,000.

Semiannual:

n = 10, coupon per period = $20, periodic y = 2.5%

Price ≈ $956.24 (clean, ignoring accrual in this rough calculation).

Important bond concerns

Clean vs full (dirty) price: Dirty = clean + accrued interest. Know which the question wants.

Day‑count convention changes accrual; match the problem’s stated convention.

Coupon frequency must match compounding in YTM.

5) Depreciation (SL, SYD, DDB)
Use the DEP (depreciation) worksheet or compute directly.

Example asset
Cost = $10,000, Salvage = $1,000, Life = 5 years.

Straight‑line (SL): Depreciation each year = 
(
10
,
000
–
1
,
000
)
/
5
=
$
1
,
800
(10,000–1,000)/5=$1,800.

Double‑declining balance (DDB): Rate = 
2
/
5
=
40
%
2/5=40%

Year 1: $10,000 × 40% = $4,000 (End BV = $6,000)

Year 2: $6,000 × 40% = $2,400 (End BV = $3,600)

Year 3: $3,600 × 40% = $1,440 (End BV = $2,160)

Year 4: $2,160 × 40% = $864 (End BV = $1,296)

Year 5: adjust so BV ends at salvage: $296 (End BV = $1,000)

Concerns:

Some problems specify half‑year or other conventions—follow the prompt.

DDB shouldn’t push book value below salvage; the last year is an adjustment.

6) Statistics (1‑Var, 2‑Var, regression)
Data entry

Press DATA to enter/edit datasets.

For 1‑Var stats, enter each 
x
x (and optional frequency).

For 2‑Var, enter pairs 
(
x
,
y
)
(x,y).

Calculate via STAT (choose 1‑Var or 2‑Var).

What you can get

Mean 
x
ˉ
x
ˉ
 , 
S
x
S 
x
​
  (sample stdev), 
σ
x
σ 
x
​
  (population stdev), n, sums.

Regression (usually returns slope 
b
b, intercept 
a
a, correlation 
r
r).

Example (1‑Var)
Data: 2, 4, 4, 4, 5, 5, 7, 9

Mean = 5.000

Population stdev 
σ
σ = 2.000

Sample stdev 
S
S ≈ 2.1381

Weighted mean
If returns are 10%, 5%, –2% with weights 0.5, 0.3, 0.2:
Weighted mean = 6.10%.
(On the BA II Plus, use frequency to mimic weights if they are integers/proportions, or compute manually.)

Concerns: Clear the DATA set (or CLR WORK) when starting a new problem; mixing datasets corrupts results. Distinguish sample vs population stdev.

7) Interest rate conversions (APR ↔ effective)
If you don’t have a dedicated conversion worksheet, just use the formula:

EAR from APR with m compounding periods:
EAR
=
(
1
+
APR
m
)
m
−
1
EAR=(1+ 
m
APR
​
 ) 
m
 −1

Example
APR = 12%, monthly compounding → EAR ≈ 12.6825%.

Tip: On the BA II Plus, you can use the power key 
y
x
y 
x
  for exponentiation.

8) Percent, growth, and “sanity” checks
Percent change = 
(
new
/
old
−
1
)
×
100
%
(new/old−1)×100%.

Growth to multi‑period FV/PV: Use TVM with PMT = 0 when it’s a single lump sum growing/discounting.

Quick reasonableness

Higher discount rate ⇒ lower PV.

Longer time ⇒ higher FV for deposits; lower PV for discounting.

Loan payment must exceed interest each period (else balance wouldn’t fall).

9) Mini cheat sheet (keystroke flow, model‑neutral)
Exam setup: 2nd FORMAT → 4–5 decimals; 2nd P/Y → P/Y=1, C/Y=1; END mode; 2nd CLR TVM; 2nd CLR WORK.

TVM
Enter N, I/Y, PV, PMT, FV (per‑period values; pay attention to signs).

CPT + the unknown.

Amortization
Solve TVM first (find PMT or PV, etc.).

2nd AMORT → set P1, P2 → CPT to get INT, PRN, BAL.

Cash flows (NPV/IRR)
CF → enter CF0, then C01, F01, C02, F02, …

NPV → set I → ↓ → CPT (NPV).

IRR → CPT (IRR). Watch out for multiple IRRs.

Bonds
Open BOND worksheet.

Enter Settlement, Maturity, Coupon%, Yield or Price, Par, Frequency, Day‑count.

CPT for missing item(s). Know whether you need clean or full price.

Depreciation
Use DEP worksheet (SL, SYD, DDB) or compute manually. Ensure salvage and life match the prompt.

Statistics
DATA to input; STAT to compute. Clear between problems.

10) What to worry about on CFA‑style problems
Wrong mode (BGN/END): Big source of point loss. Confirm before annuities.

Hidden P/Y settings: Set P/Y = 1 and control periods yourself.

Sign convention: Outflows negative; inflows positive. This matters in TVM and CF.

Rounding: Keep 4–5 decimals. CFA answers typically accept a tolerance; rounding early can push you out of range.

Day‑count & price type for bonds: The question tells you; follow it.

Multiple IRRs / Non‑conventional cash flows: Don’t force a single IRR; use NPV judgment or MIRR (if asked).

Mismatched frequency: If coupons are semiannual, your discounting must be semiannual unless stated otherwise.

11) Short practice set (with answers to check yourself)
Ordinary annuity FV
Deposit $500 at end of each quarter for 5 years at 6% APR, quarterly.
Answer: $11,561.83.

Loan payment
PV $250,000, 4% APR monthly, 30 years.
Answer: $1,193.54 per month. Year‑1 totals: INT ≈ $9,919.87, PRN ≈ $4,402.59, BAL ≈ $245,597.41.

Bond price
5‑year, 4% coupon (semiannual), YTM 5%, par $1,000.
Answer (clean, rough): $956.24.

NPV & IRR
–1,000; 400; 350; 300; 250 at t = 0…4.
NPV @ 8% ≈ 92.35, IRR ≈ 12.44%.

EAR
APR 12% compounded monthly.
Answer: 12.6825%.

12) If you have the BA II Plus Professional
All of the above applies. The Pro model adds a few convenience worksheets (e.g., break‑even, percent change, etc.), but the core CFA workflows are identical. Stick to the same exam‑safe habits (P/Y=1, END mode unless annuity‑due, clear registers, watch signs).

Want a custom one‑pager?
Tell me which topics you use most (TVM, bonds, CF/NPV, stats, depreciation), and I’ll condense just those into a printable quick‑reference tailored to you.




