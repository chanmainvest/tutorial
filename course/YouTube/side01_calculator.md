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
