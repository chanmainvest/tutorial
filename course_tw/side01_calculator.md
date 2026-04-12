<!-- 此檔案需要翻譯為台灣繁體中文 -->
<!-- This file needs translation to TW Traditional Chinese -->

# Side Lesson 01: Mastering the TI BA II Plus Financial Calculator

---

## PART 1: READING SECTION

---

### Why This Is Important

Every finance professional and serious investor needs to speak the language of time value of money fluently. The TI BA II Plus is the industry-standard financial calculator used by CFA candidates, financial analysts, and investment bankers worldwide. While spreadsheets can do these calculations, understanding how to work a financial calculator builds intuition about how money moves through time. You cannot fake this skill in a job interview, a client meeting, or a certification exam.

More importantly, the calculator forces you to think about cash flow sign conventions, compounding frequency, and the relationship between present and future values in a way that simply plugging numbers into a spreadsheet formula does not. When you truly understand what each key does, you understand the math behind every loan, every bond, every investment decision.

---

### What You Need to Know

#### The Five TVM Keys

The heart of the TI BA II Plus is the five Time Value of Money (TVM) keys across the third row:

- **N** -- The number of compounding periods. Not years, not months, but periods. If you have a 30-year mortgage with monthly payments, N = 360.
- **I/Y** -- The interest rate per year (expressed as a percentage, not a decimal). The calculator automatically divides this by P/Y to get the periodic rate.
- **PV** -- Present Value. The value of money today, or the starting amount. Typically entered as negative when it represents money you pay out.
- **PMT** -- Payment. The periodic cash flow that occurs at regular intervals. Negative when you pay it, positive when you receive it.
- **FV** -- Future Value. The value of money at the end of the time horizon. Negative when you pay it out, positive when you receive it.

The fundamental rule: **you must enter at least four of the five variables, then compute the fifth.** The calculator solves for the unknown.

#### The Sign Convention

This is where most beginners stumble. The TI BA II Plus uses a cash flow sign convention:

- **Negative (-)** = money leaving your pocket (outflows)
- **Positive (+)** = money coming into your pocket (inflows)

Think of it from your perspective as the investor or borrower:

- If you invest $1,000 today, PV = -1000 (money leaves you)
- If you receive $1,500 in five years, FV = 1500 (money comes to you)
- If you make monthly loan payments, PMT = -500 (money leaves you)
- If you receive monthly rental income, PMT = 2000 (money comes to you)

If you get the signs wrong, you will either get an error or a wrong answer. Every single time you enter a TVM problem, ask yourself: "Is this money going out or coming in?"

#### P/Y and C/Y Settings

Press **[2ND]** then **[I/Y]** to access the P/Y (Payments per Year) and C/Y (Compounding periods per Year) settings.

- **P/Y** -- How many payments occur per year. Set to 12 for monthly, 4 for quarterly, 2 for semi-annual, 1 for annual.
- **C/Y** -- How many times interest compounds per year. Usually matches P/Y, but not always.

**Critical habit:** Always check your P/Y setting before starting a new problem. A wrong P/Y setting is the single most common source of calculator errors. Many professionals keep P/Y = 1 at all times and manually adjust N and I/Y, which avoids confusion.

**Reset approach:** Press [2ND] [+/-] (which is the RESET function) and press ENTER to clear everything back to factory defaults (P/Y = 1, C/Y = 1).

#### Basic TVM Examples

**Example 1: Future Value of a Lump Sum**
You invest $10,000 today at 8% annual return for 20 years. What will it be worth?

- N = 20
- I/Y = 8
- PV = -10000 (money leaving you)
- PMT = 0
- CPT FV = 46,609.57

**Example 2: Monthly Mortgage Payment**
You borrow $300,000 for 30 years at 6.5% annual interest with monthly payments.

- Set P/Y = 12
- N = 360 (30 x 12)
- I/Y = 6.5
- PV = 300000 (money coming to you from the bank)
- FV = 0 (loan fully repaid)
- CPT PMT = -1,896.20 (you pay this each month)

**Example 3: Required Return**
You can buy a bond for $950 that pays $50 per year for 10 years and returns $1,000 at maturity. What is the yield?

- Set P/Y = 1
- N = 10
- PV = -950 (you pay this)
- PMT = 50 (you receive this annually)
- FV = 1000 (you receive this at maturity)
- CPT I/Y = 5.66%

#### NPV and IRR Functions

Press **[CF]** to enter the Cash Flow worksheet.

**Entering Cash Flows:**
1. CF0 = initial investment (usually negative)
2. C01 = first cash flow, F01 = frequency of that cash flow
3. C02 = second cash flow, F02 = frequency, and so on
4. Use the down arrow to move through entries

**Computing NPV:**
1. After entering cash flows, press [NPV]
2. Enter I = discount rate (as a percentage)
3. Press the down arrow, then CPT to compute NPV

**Computing IRR:**
1. After entering cash flows, press [IRR]
2. Press CPT to compute IRR

**Example: Project Evaluation**
A project requires $50,000 upfront and generates $15,000 per year for 5 years.

- CF0 = -50000
- C01 = 15000, F01 = 5
- NPV at I = 10%: press [NPV], I = 10, down arrow, CPT = $6,861.80
- IRR: press [IRR], CPT = 15.24%

Since NPV > 0 and IRR > required return of 10%, the project is acceptable.

#### Bond Calculations

Press **[2ND]** then **[9]** to access the Bond worksheet.

Key inputs:
- **SDT** -- Settlement date (when you buy the bond)
- **CPN** -- Annual coupon rate (as a percentage)
- **RDT** -- Redemption date (maturity date)
- **RV** -- Redemption value (usually 100 for par)
- **ACT/360** -- Day count convention
- **2/Y or 1/Y** -- Semi-annual or annual coupon frequency
- **YLD** -- Yield to maturity
- **PRI** -- Clean price

You can enter either YLD or PRI and compute the other.

**Example: Bond Pricing**
A bond with 5% coupon, semi-annual payments, matures in 10 years, market yield is 6%.

Using TVM keys (simpler approach):
- Set P/Y = 2
- N = 20 (10 years x 2)
- I/Y = 6
- PMT = 25 (1000 x 5% / 2)
- FV = 1000
- CPT PV = -925.61 (the price you pay)

#### Amortization Worksheet

Press **[2ND]** then **[PV]** to access the amortization worksheet after solving a TVM loan problem.

- P1 = starting period
- P2 = ending period
- BAL = remaining balance after P2
- PRN = total principal paid between P1 and P2
- INT = total interest paid between P1 and P2

This is invaluable for understanding how much of each payment goes to principal versus interest over the life of a loan.

#### Statistical Functions

Press **[2ND]** then **[7]** to access the Data worksheet. Press **[2ND]** then **[8]** for the Stat worksheet.

You can enter data points and compute:
- Mean (average)
- Sample standard deviation (Sx)
- Population standard deviation (sigma x)
- Linear regression statistics

While not as commonly tested as TVM, these functions are useful for quick portfolio return and risk calculations.

#### Key Shortcuts and Tips

1. **Clear TVM:** Press [2ND] then [FV] (which is CLR TVM) before every new problem.
2. **Clear all worksheets:** Press [2ND] then [CE/C] (which is CLR Work) when in a worksheet.
3. **Change sign:** Use the [+/-] key to toggle between positive and negative.
4. **Store and recall:** Use [STO] and [RCL] with number keys 0-9 to store intermediate results.
5. **Chain calculations:** After computing one value, you can change one or two inputs and recompute without re-entering everything.
6. **Decimal places:** Press [2ND] then [.] (FORMAT), then enter the number of decimal places you want displayed (0-9). Press ENTER.

---

### Common Misconceptions

**"I can just use Excel, so I don't need a calculator."**
Excel is powerful, but it does not build intuition. When you manually set up a TVM problem on a calculator, you are forced to think about what each variable means, what the sign should be, and how many periods are involved. This understanding transfers directly to building better spreadsheet models and catching errors in other people's work.

**"N always equals the number of years."**
No. N is the number of compounding periods. A 5-year loan with monthly payments has N = 60, not 5. A 10-year bond with semi-annual coupons has N = 20, not 10. Always match N to the payment frequency.

**"I/Y is the periodic interest rate."**
No. I/Y is the annual interest rate. The calculator divides it by P/Y internally to get the periodic rate. If you have a monthly problem with P/Y = 12 and the annual rate is 6%, you enter I/Y = 6, not 0.5.

**"The sign doesn't matter as long as the magnitude is right."**
The sign is everything. If PV and FV have the same sign, the calculator thinks money flows in the same direction at both times, which makes no sense for most problems and will produce an error or a wrong answer.

**"BGN mode is rarely used."**
BGN (Begin) mode matters whenever payments occur at the start of each period rather than the end. Annuities due (like rent or insurance premiums paid in advance) require BGN mode. Forgetting to switch between BGN and END is a common exam mistake. Check the display -- if you see "BGN" in the upper right, you are in begin mode.

**"NPV and IRR always give the same accept/reject decision."**
For independent projects with conventional cash flows (one outflow followed by inflows), they agree. But for mutually exclusive projects or non-conventional cash flows (multiple sign changes), NPV and IRR can conflict. Always trust NPV when they disagree.

**"A higher IRR always means a better project."**
IRR has limitations: it assumes reinvestment at the IRR itself, it can produce multiple solutions with non-conventional cash flows, and it does not account for project scale. A project with 50% IRR on a $100 investment is not necessarily better than 20% IRR on a $1,000,000 investment.

---

### Q&A Section

**Q: My calculator gives me an "Error 5" when I try to compute I/Y. What's wrong?**
A: Error 5 means "no solution exists." This almost always means your signs are wrong. Check that PV and FV/PMT have opposite signs. If you are investing money (PV is negative), then you should receive money back (FV or PMT should be positive), or vice versa.

**Q: Should I keep P/Y at 1 or change it for each problem?**
A: Many experienced users keep P/Y = 1 at all times. When you do this, you manually adjust N (multiply years by frequency) and I/Y (divide annual rate by frequency). This approach avoids the confusion of forgetting to change P/Y back. Others prefer to set P/Y to match the problem. Either approach works, but be consistent.

**Q: How do I compute the yield to maturity on a bond that pays semi-annual coupons?**
A: Set P/Y = 2, enter N = (years to maturity x 2), PV = -(current price), PMT = (annual coupon / 2), FV = 1000 (or par value), then CPT I/Y. The result is the annual YTM (the calculator adjusts for the semi-annual compounding internally).

**Q: What's the difference between the CF worksheet and the TVM keys?**
A: The TVM keys handle level annuities (equal, regular payments). The CF worksheet handles uneven cash flows. Use TVM for loans, standard bonds, and regular savings. Use CF for project evaluation, uneven income streams, and any situation where cash flows change from period to period.

**Q: How do I handle a problem where payments start in the future (deferred annuity)?**
A: Break it into two steps. First, calculate the PV of the annuity as of the date payments begin. Then discount that PV back to today using a separate TVM calculation. The calculator does not have a built-in deferred annuity function.

**Q: Can I compute Modified Duration or Convexity on this calculator?**
A: The bond worksheet gives you duration (Macaulay) and modified duration directly. After entering bond details and computing price or yield, scroll down to see DUR (duration). For convexity, you would need to calculate it manually or use the stored memory registers.

**Q: What is the difference between ordinary annuity and annuity due on this calculator?**
A: Press [2ND] then [PMT] to toggle between END (ordinary annuity -- payments at end of period) and BGN (annuity due -- payments at beginning of period). The display shows "BGN" when in begin mode. Most problems assume END mode unless stated otherwise.

**Q: How accurate is the calculator compared to Excel?**
A: The TI BA II Plus uses 13-digit internal precision, which matches or exceeds most spreadsheet calculations for financial problems. Any differences you see are typically due to rounding in the display, not calculation errors.

---

## PART 2: YOUTUBE SCRIPT

---

### "Your Calculator Is Your Best Friend: Mastering the TI BA II Plus"

**Target Length:** 15-20 minutes
**Tone:** Encouraging, practical, demystifying

---

**[VISUAL: Close-up shot of TI BA II Plus calculator on a clean desk. Title card: "Mastering the TI BA II Plus"]**

**Alex:** Alright Sam, today we are doing something a little different. We are going hands-on with the financial calculator. And I know what people are thinking -- "It is 2026, why do I need a calculator when I have Excel?"

**Sam:** Right, I thought the same thing. But then I started studying for the CFA and realized that the calculator is not just a tool -- it actually teaches you how to think about money over time.

**Alex:** Exactly. And honestly, once you get comfortable with it, you can solve problems faster on this thing than you can in a spreadsheet. No booting up, no file management, just punch and go.

**[VISUAL: Calculator laid flat with all keys visible. Arrows pointing to the five TVM keys: N, I/Y, PV, PMT, FV]**

**Alex:** So let us start with the five most important keys on this calculator. The TVM keys -- Time Value of Money. They sit right here in the third row. N, I/Y, PV, PMT, FV. These five keys handle probably 80% of everything you will ever do on this calculator.

**Sam:** Can you walk through what each one means in plain English?

**Alex:** Sure. N is the number of periods -- not years, periods. I/Y is the interest rate per year. PV is how much money is worth right now. PMT is a regular payment that happens every period. And FV is how much money is worth in the future.

**[ANIMATION: A timeline showing $1,000 at time 0, growing with arrows to $1,500 at time 5. Labels appear: PV = -1000 at left, FV = +1500 at right, N = 5 above the timeline]**

**Sam:** Okay, but here is where I always got confused when I started. The negative signs. Why is PV negative sometimes?

**Alex:** This is the number one thing to understand. The calculator uses a cash flow sign convention. Negative means money is leaving you. Positive means money is coming to you. So if you invest a thousand dollars today, that money is leaving your wallet. PV equals negative one thousand.

**Sam:** And when you get money back in the future?

**Alex:** That is positive. FV equals positive fifteen hundred. Think of yourself standing in the middle. Money going away from you is negative. Money coming toward you is positive.

**[VISUAL: Person icon in center. Arrows going left labeled "NEGATIVE (outflows)" and arrows going right labeled "POSITIVE (inflows)"]**

**Sam:** What happens if you mess up the signs?

**Alex:** You either get Error 5 -- which means no solution exists -- or you get a number that looks plausible but is completely wrong. And that is actually more dangerous because you might not catch it.

**[VISUAL: Calculator screen showing "Error 5" with a red X]**

**Alex:** Let me show you a real example. Say you want to know how much ten thousand dollars grows to in twenty years at eight percent per year.

**[VISUAL: Hands on calculator, each keystroke shown with on-screen caption]**

**Alex:** First, I always clear the TVM registers. Second, then FV -- that is CLR TVM. Clean slate. Now: two, zero, N. Eight, I/Y. Negative ten thousand, PV. Zero, PMT -- because there are no additional contributions. Now CPT, FV. And we get forty-six thousand, six hundred nine dollars and fifty-seven cents.

**Sam:** That is the power of compound interest right there. Your money more than quadrupled.

**Alex:** In twenty years at eight percent, yes. And notice I entered PV as negative because the ten thousand is money I am investing -- it is leaving me. The calculator gives me a positive FV because that is money coming back to me.

**[ANIMATION: Bar chart showing $10,000 growing year by year to $46,609.57 over 20 years, with compound interest highlighted in a different color from the original principal]**

**Sam:** Okay, let us try something people actually deal with. Mortgages.

**Alex:** Perfect. Let us say you are borrowing three hundred thousand dollars for a thirty-year mortgage at six point five percent. What is your monthly payment?

**[VISUAL: House icon with price tag $300,000, "30 years", "6.5%"]**

**Alex:** First thing -- this is a monthly problem. So we need to deal with P/Y. Press second, then I/Y -- that takes you to the P/Y setting. Enter twelve, press ENTER. Then press second, CPT to quit out of there.

**Sam:** And this tells the calculator that payments happen twelve times a year?

**Alex:** Exactly. Now the calculator knows to divide the annual rate by twelve internally. So: N equals three sixty -- that is thirty times twelve. I/Y equals six point five -- the annual rate, not the monthly rate. PV equals three hundred thousand -- positive, because the bank is giving you this money.

**Sam:** Wait, the loan amount is positive?

**Alex:** Yes! The bank is handing you three hundred thousand dollars. That money is coming to you. It is an inflow. Your payments going back to the bank will be negative -- outflows.

**Sam:** That is counterintuitive at first but it makes sense when you think about the direction of the cash flow.

**Alex:** FV equals zero because by the end of thirty years, the loan is fully paid off. Now CPT PMT, and we get negative one thousand eight hundred ninety-six dollars and twenty cents.

**[VISUAL: Calculator screen showing -1,896.20]**

**Sam:** Almost nineteen hundred a month. And it is negative because that is money leaving your pocket.

**Alex:** Every single month for thirty years. And here is something eye-opening. Let me show you the amortization. Press second, PV -- that is the AMORT function. Set P1 to one and P2 to twelve. Now scroll down.

**[VISUAL: Split screen showing calculator and a pie chart of first year payments]**

**Alex:** In the first year, you pay about twenty-two thousand seven hundred in total payments. Of that, about nineteen thousand three hundred goes to interest and only about thirty-four hundred goes to principal.

**Sam:** So in the first year, eighty-five percent of your payment is just interest?

**Alex:** Welcome to amortization. Now check the last year -- set P1 to three forty-nine and P2 to three sixty. Almost the entire payment is principal. That is how amortization works. Early on, you are mostly paying interest. Later, you are mostly paying down the loan.

**[ANIMATION: Stacked bar chart showing the interest vs principal split over 30 years, with interest shrinking and principal growing over time]**

**Sam:** This is why people say the first few years of a mortgage are "expensive."

**Alex:** Now let us shift gears to something every investor needs. NPV and IRR.

**[VISUAL: Title card "NPV and IRR: Making Investment Decisions"]**

**Alex:** Say a friend offers you a business opportunity. You invest fifty thousand dollars today and expect to get back fifteen thousand per year for five years. Is this a good deal if your required return is ten percent?

**Sam:** So we need to figure out if those future cash flows are worth more than fifty thousand in today's dollars.

**Alex:** Right. Press CF to enter the cash flow worksheet. CF0 is your initial investment -- negative fifty thousand. Then C01 is fifteen thousand, F01 is five -- meaning that fifteen thousand repeats five times. Now press NPV. Enter I equals ten. Scroll down and CPT.

**[VISUAL: Cash flow timeline showing -$50,000 at time 0, then $15,000 at times 1 through 5]**

**Alex:** NPV equals six thousand eight hundred sixty-one dollars and eighty cents. It is positive, which means this deal creates value above and beyond your ten percent requirement.

**Sam:** And IRR?

**Alex:** Press IRR, then CPT. We get fifteen point two four percent. That is the actual rate of return on this investment. Since it is above your required ten percent, the project is a go.

**[VISUAL: Comparison showing "NPV = $6,861.80 > 0 = ACCEPT" and "IRR = 15.24% > 10% = ACCEPT" with green checkmarks]**

**Sam:** Do NPV and IRR always agree?

**Alex:** For simple projects like this one -- one upfront cost followed by positive inflows -- yes, they always agree. But for more complex scenarios, like comparing two mutually exclusive projects of different sizes, they can disagree. When they do, always trust NPV. It measures actual value creation in dollars.

**[ANIMATION: Two project timelines side by side. Project A: small investment, high IRR. Project B: large investment, lower IRR but higher NPV. Arrow pointing to Project B labeled "NPV says choose B"]**

**Sam:** Let us do bonds. That is where I see a lot of people struggle.

**Alex:** Bonds are just a specific type of TVM problem. You pay a price today, receive coupon payments along the way, and get your principal back at maturity. Let me show you.

**[VISUAL: Bond diagram showing price paid at left, coupon payments as arrows going up at regular intervals, and face value returned at the end]**

**Alex:** Say you are looking at a bond with a five percent coupon, semi-annual payments, ten years to maturity, and the market requires a six percent yield. What should you pay?

**Alex:** Set P/Y to two because coupons are semi-annual. N equals twenty -- ten years times two. I/Y equals six -- the annual yield. PMT equals twenty-five -- that is one thousand times five percent divided by two. FV equals one thousand -- the face value you get back at maturity. CPT PV.

**[VISUAL: Calculator keystrokes with annotations]**

**Alex:** Negative nine hundred twenty-five dollars and sixty-one cents. So this bond trades at a discount because the coupon rate of five percent is below the market yield of six percent.

**Sam:** It makes intuitive sense. If the market demands six percent but the bond only pays five percent in coupons, the price has to drop to make up the difference.

**Alex:** And the reverse is true. If the coupon were seven percent and the market wanted six percent, the bond would trade at a premium above one thousand.

**[ANIMATION: See-saw diagram. Coupon rate on one side, market yield on the other. When yield > coupon, price dips below par. When yield < coupon, price rises above par.]**

**Sam:** What about finding the yield when you know the price?

**Alex:** Same setup, but instead of computing PV, you enter PV as negative nine fifty -- say that is the market price -- and compute I/Y. You get the yield to maturity.

**Alex:** Before we wrap up, let me give you my top five calculator tips that will save you hours of frustration.

**[VISUAL: Numbered list appearing one by one]**

**Alex:** Number one -- always clear TVM before a new problem. Second then FV. Make it a habit. Number two -- always check P/Y. Press second then I/Y and verify before every problem. Number three -- write down your inputs before touching the calculator. N equals what, I/Y equals what, and so on. This catches sign errors before they happen.

**Sam:** What about number four?

**Alex:** Number four -- when in doubt about signs, draw a timeline. Put yourself at time zero. Arrows going down are negative, arrows coming up are positive. And number five -- practice with problems where you know the answer. Take a simple savings account problem, solve it by hand, then verify on the calculator. Build confidence.

**[VISUAL: Timeline drawing with person icon, downward arrow labeled "PV (-)" at left, upward arrows labeled "PMT (+)" in middle, upward arrow labeled "FV (+)" at right]**

**Sam:** Any advice for people preparing for the CFA or other exams?

**Alex:** Set your calculator to four decimal places for the exam -- second, dot, four, enter. Learn the keystrokes so well that you do not have to think about them. And remember, on exam day, you are solving dozens of TVM problems. Speed comes from practice, not from shortcuts.

**Sam:** Great stuff. The calculator seems intimidating at first but once you get the logic of signs and periods, it becomes second nature.

**Alex:** Exactly. It is like learning to drive. At first you are thinking about every little action. After a while, it is just muscle memory. Go practice the examples we covered today. Try changing the inputs and see how the outputs change. That is how you build real intuition.

**[VISUAL: Recap screen listing key topics: "TVM Keys | Sign Convention | P/Y Settings | NPV & IRR | Bond Calculations | Amortization"]**

**Sam:** Next time we will use these skills on real-world cases. But for now, grab your calculator and start punching numbers. See you in the next one.

**[VISUAL: End card with channel info and "Next: Side Lesson 02 -- Reading a 10-K Filing"]**

---

**END OF SIDE LESSON 01**
