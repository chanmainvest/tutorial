## Part 2: YouTube Script

---

**VIDEO TITLE:** Monte Carlo Retirement Planning — Why "7% per Year" Is a Lie | Side Lesson 28

**RUNTIME TARGET:** ~13 minutes

**HOSTS:**
- **Horace** (teacher): runs the simulation.
- **Stella** (student): asks the questions every retiree has.

---

**[INTRO]**

[VISUAL: Animated logo "Side Lesson 28 — Monte Carlo & Sequence Risk"]

**Horace:** Stella, your bank's retirement planner says you will
have $7.6 million at age 95. Do you believe it?

**Stella:** Probably not, but I am not sure why. The math looks
right.

**Horace:** The math is right. The model is wrong. Today we are
going to look at why every single-number retirement projection is
lying to you, and what to use instead.

---

**[SEGMENT 1: THE LIE OF THE SINGLE NUMBER]**

[VISUAL: bar showing $1M -> $7.61M with the formula 1.07^30 = 7.61]

**Horace:** Here is the standard projection. You have $1 million
today, you do not contribute or withdraw, you compound at 7% per
year for 30 years. Result: $7.61 million.

**Stella:** That is exactly what my 401k page tells me.

**Horace:** Yes, and the number is mathematically perfect and
operationally useless. The market does not deliver 7% per year. It
delivers 30% one year and -25% the next. The compound gets you to
roughly 7%, but the *path* matters.

---

**[SEGMENT 2: THE FAN CHART]**

[VISUAL: image/side28_mc_fan.png]

**Horace:** This is the same projection done honestly. One thousand
random paths, each one drawing 30 annual returns from a Normal
distribution with 7% mean and 15% standard deviation, all starting
at $1 million, all running 30 years.

**Stella:** Wide.

**Horace:** Very wide. The median path lands around $7.6 million,
matching the textbook answer. But the 95th-percentile path ends near
$20 million, and the 5th-percentile path ends around $3 million.
Same starting balance, same return assumption, same vol. The
difference is the order in which the returns arrived.

**Stella:** $3 million is still fine though.

**Horace:** It is — for the no-withdrawal case. Now let us add
withdrawals.

---

**[SEGMENT 3: SEQUENCE OF RETURNS RISK]**

[VISUAL: image/side28_sequence_risk.png]

**Horace:** Two retirees. Both start with $1 million at age 65. Both
withdraw $40,000 per year — the famous 4% rule. Both experience the
exact same 30 annual returns. Same average. Same volatility.

**Stella:** And...

**Horace:** Retiree A gets the bad decade first. The first ten years
average -5% per year. Then years 11 through 30 deliver +13% per
year. Average over the full 30 years is 7%. Math says fine.

**Stella:** And reality says...

**Horace:** Retiree A runs out of money around year 24. Six years
before the end of the plan. Retiree B gets the *exact same returns
in reverse* — the good decades first, then the bad decade at the
end. Retiree B finishes with several million in the bank.

**Stella:** Same returns. Same withdrawals. The ordering kills one
of them?

**Horace:** The ordering kills one of them. This is sequence-of-
returns risk and it is the single most underappreciated risk in
personal finance. Withdrawing from a depressed portfolio sells more
shares than withdrawing from an inflated one. The shares you sell
at the bottom never participate in the recovery. Permanent capital
destruction.

---

**[SEGMENT 4: THE 4% RULE AND ITS UPDATE]**

[VISUAL: Title card "Bengen 1994 -> Pfau 2020"]

**Horace:** Bengen, 1994, ran this exercise on US data 1926-1976
and found that a 50/50 portfolio could safely withdraw 4.15% of the
initial balance, inflation-adjusted, for 30 years. He rounded to
4.0% and the rule stuck.

**Stella:** And the 4% rule is fine?

**Horace:** It was fine in 1994. It assumed the 1926-1976 historical
returns would persist — equity premium of 6.5%, ten-year Treasury
of 5%. In April 2026 forward-looking expected returns from sober
sources cluster at 5-7% nominal for equities and 4-4.5% for ten-year
Treasuries. Pfau ran the same Bengen exercise with these
forward-looking numbers and the safe rate fell to 3 to 3.5%.

**Stella:** That is a big difference.

**Horace:** Half a percent on $80,000 a year is $400 a month forever.
And in nest-egg terms, going from 4% to 3.5% means you need 14%
more saved for the same retirement. The market's lower forward
returns translate one-to-one into bigger required nest eggs.

---

**[SEGMENT 5: BOOTSTRAP VS PARAMETRIC]**

[VISUAL: Title card "Two Flavours of Monte Carlo"]

**Horace:** Two ways to generate the random returns. Parametric:
assume Normal distribution with given mean and vol, draw samples.
Bootstrap: sample with replacement from actual historical returns.

**Stella:** And the difference?

**Horace:** Real equity returns are fat-tailed. Kurtosis of monthly
S&P returns is 7 to 15 — Normal predicts 3. Parametric Normal
under-models the tail. Bootstrap captures it directly. The academic
standard is **block bootstrap** — sample 5- or 10-year blocks at a
time so you preserve correlations and serial structure.

**Stella:** Which does the lab use?

**Horace:** Parametric Normal, for speed and simplicity in the
browser. The take-away difference at 30-year horizons is roughly 1
to 2 percentage points on the success rate. The return *assumption*
matters far more than the sampling method.

---

**[SEGMENT 6: THE INTERACTIVE LAB]**

[VISUAL: cut to interactive/side28_mc_lab.html]

**Horace:** Five sliders. Starting balance, monthly contribution or
withdrawal — positive for accumulation, negative for retirement —
expected return, volatility, and horizon.

*(types: balance $1M, withdrawal -$3,333/mo i.e. -$40k/yr, return 7%, vol 15%, horizon 30y)*

**Horace:** That is the Bengen baseline. Look at the success rate.

*(reads the dashboard)*

**Horace:** Around 85-90%. Below the 95% comfort threshold. The 5th
percentile ending balance is zero — that is what Pfau warned about.

*(adjusts withdrawal to -$3,000/mo / -$36k/yr)*

**Horace:** Now into the low 90s. Adjust to -$2,917 — that is 3.5%
— and the success rate moves toward 95%. That is the modern safe
rate.

**Stella:** What if I want to go to 4% and stay safe?

**Horace:** Two ways. Reduce vol — 60/40 instead of 100% equities.
Or build flexibility — variable withdrawals. The Guyton-Klinger
guardrails I mentioned in the reading. Both lift the safe rate by
50-100 basis points without changing the success target.

---

**[SEGMENT 7: PITFALLS]**

[VISUAL: Title card "Three Modeling Mistakes"]

**Horace:** Three things any honest practitioner will tell you the
parametric Monte Carlo gets wrong. One: assumes Normal returns when
reality is fat-tailed. Two: assumes constant volatility when real
vol clusters and shifts regime. Three: assumes constant correlations
between asset classes when 2022 just demonstrated that those
correlations can flip in a quarter.

**Stella:** So why use it at all?

**Horace:** Because it is honest about what it can model — the
distribution of paths under the assumed dynamics — and that is
already infinitely better than a single-number projection. Run
parametric MC. Then run bootstrap MC. Then stress-test against the
1966 cohort. If the plan survives all three, you have a real plan.
If it only survives one, you have a wish.

---

**[SEGMENT 8: THE BARBELL APPLIED]**

[VISUAL: Title card "Sequence-Risk Defenses"]

**Horace:** Three structural defences. Cash buffer — two years of
expenses outside the equity sleeve so you do not have to sell during
a drawdown. Variable withdrawals — let spending flex with balance.
Equity glidepath — start retirement at 40% equities, ramp *up* to
70% over 15 years.

**Stella:** Up, not down?

**Horace:** Up. Counterintuitive but right. The first decade is when
sequence risk is fatal — that is when you want *less* equity
exposure. The second and third decades are when sequence risk has
attenuated — that is when you want *more* equity exposure for the
the return. The barbell applied to retirement: cash
ironclad on one side, equity aggressive on the other, and reduce
the middle.

---

**[OUTRO]**

[VISUAL: Summary card with three bullets:
- Single-number projections lie about sequence risk
- 95th percentile bad case is 30-40% below median
- Bengen 4% is now closer to 3.5% on forward returns]

**Horace:** Three takeaways. One: any retirement projection that
gives you a single number is hiding sequence risk. Get a tool that
shows you a distribution. Two: the median is a coin flip; plan to
the 5th percentile of the distribution. Three: the 4% rule is a
1994 result on 1926-1976 data; the modern equivalent is closer to
3.5%, and the gap is real money.

**Stella:** Got it. Run the distribution, look at the bad tail, plan
to a 3.5% withdrawal, build the cash buffer, run the glidepath up.

**Horace:** That is the lesson. Markets do not deliver averages.
They deliver paths. Plan for the path, not the average.

[END CARD: "Side Lesson 28 — Monte Carlo & Sequence Risk"]
