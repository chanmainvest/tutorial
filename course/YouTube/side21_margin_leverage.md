## Part 2: YouTube Script

---

**VIDEO TITLE:** Margin and Leverage — Reg T, Portfolio Margin, and How Not to Blow Up | Side Lesson 21

**RUNTIME TARGET:** ~13 minutes

**HOSTS:**
- **Horace** (teacher): Retail investor with a portfolio-margin account he uses for spreads, not for stock leverage.
- **Stella** (student): Has a Schwab account, just realised it's a margin account.

---

**[INTRO]**

[VISUAL: Title card "Side Lesson 21 — Margin and Leverage"]

**Horace:** Stella. Open your brokerage app. Look at the account
type. Tell me what it says.

**Stella:** *(looking)* It says... "margin account."

**Horace:** Right. You did not pick that. The default account type
at every major US retail broker is a margin account, and you
signed the agreement when you onboarded. So today we are going to
read what you signed, and then talk about whether you should use
the leverage or not — because the answer is mostly not, but it's
a useful not once you understand the math.

**Stella:** What did I sign?

**Horace:** Three things, mainly. The broker can lend your shares
to short sellers. The broker can liquidate your positions without
calling you first. And the broker can change house margin rules
on any stock at any time. None of those matter while you are
unlevered. All of them matter the day after you lever up.

---

**[SEGMENT 1: REG T AND THE 33% RULE]**

[VISUAL: Title card "Reg T: 50% Initial / 25% Maintenance"]

**Horace:** The Federal Reserve sets the initial margin at 50%.
You put up half, the broker lends you the other half. FINRA sets
the maintenance margin at 25% — your equity must stay at least a
quarter of the position value, or you get a call. Brokers stack
their own rules on top, usually 30 to 35%.

**Stella:** OK. So if I buy 2x, when do I get called?

**Horace:** Do the algebra. 2x means 50% equity at entry. Drop to
25% equity and you call. The price level where that happens is
two-thirds of the entry price.

[VISUAL: image/side21_margin_call_path.png]

**Horace:** This chart shows a 2x SPY position riding through
2008. The unlevered SPY was awful — down 38% — but it recovered.
The 2x line crossed the maintenance threshold at minus 33%, was
forced to liquidate at the bottom, and never participated in the
recovery. That is the structural problem with retail leverage:
you eat the loss but not the rebound.

**Stella:** Why didn't they just hold through it?

**Horace:** They didn't get to choose. The broker chose. The market
can stay irrational longer than you can stay
solvent. Leverage cuts your "longer than" in half.

---

**[SEGMENT 2: THE 2022 CRYPTO LIQUIDATION CASCADE]**

**Horace:** The recent textbook case is crypto, 2022. Celsius,
Voyager, BlockFi, 3AC — all running 3 to 5x on stablecoin loans
collateralised by ETH and BTC. ETH went from $4,800 in November
2021 to $880 in June 2022. Each margin call on the way down
forced selling into a thinning order book. The selling pushed the
price lower. The lower price triggered the next call. Eight weeks.
$24 billion of margin debt unwound. Vol-tail-wags-dog.
None of those firms would have failed unlevered.

**Stella:** And this could happen with stocks?

**Horace:** It does happen with stocks. March 2020, August 2024
yen carry unwind, every individual-name earnings disaster.
Different products, same mechanic.

---

**[SEGMENT 3: THE BORROW-RATE TABLE NOBODY ADVERTISES]**

[VISUAL: image/side21_box_vs_broker.png]

**Horace:** Now look at the price tag. Treasury bills are paying
4.3%. The risk-free rate. Interactive Brokers Pro on a small
account: 6.6%. Fidelity small account: 11%. Schwab small account:
12%. The broker is not lending you anything; the broker is
borrowing at SOFR and re-lending the same dollar to you at SOFR
plus five.

**Stella:** Why is anyone paying 11%?

**Horace:** Because they don't read the table. And because the
alternatives — box spreads, portfolio margin, futures — require a
$100k account, options approval, and reading the manual. The
brokers count on that friction.

**Horace:** A box spread on SPX, today, finances at SOFR plus 30
to 50 basis points — about 4.7%. Two hundred basis points cheaper
than IB's small-account margin desk. Four hundred basis points
cheaper than Fidelity. Same dollar, same loan, completely
different price.

---

**[SEGMENT 4: THE MATH THAT KILLS THE LEVERAGE PITCH]**

[VISUAL: Title card "Geometric return = L mu minus (L-1) b minus 0.5 L^2 sigma^2"]

**Horace:** Here is the calculation that kills most leveraged-
equity sales pitches. Equity returns historically: about 10% a
year. Equity vol: about 16%. Borrow at IB small-balance: 6%.
Plug into the geometric return formula.

**Horace:** Unlevered: 8.6%. 1.5x: 9.0%. 2x: 8.7%. 3x: 6.3%.

**Stella:** They're all... almost the same?

**Horace:** That's the point. The expected geometric return is
flat across reasonable leverage. What changes monotonically with
leverage is volatility — three to four times the unlevered
amount. You are taking quadruple the variance for the same
expected wealth. That is not a trade. That is a tax. Alpha is rare.
Cheap leverage on no edge just rents you variance.

---

**[SEGMENT 5: THE INTERACTIVE LAB]**

**Horace:** The lab on the website lets you tune four things —
account size, leverage, market move, and borrow rate — and watch
the equity, the distance to the call, and the after-cost
annualised return move in real time.

[VISUAL: cut to interactive/side21_margin_lab.html]

**Horace:** Default: $100k account, 2x leverage, market down 20%,
IB small-balance 6.6% borrow. Equity: $60k. Distance to call:
minus 13 percentage points — you have already been called.
After-cost return: minus 46.6%.

**Horace:** Slide leverage to 1.25x with the same minus 20% move.
Equity: $73k. Distance to call: still alive, 14 percentage points
of buffer. After-cost return: minus 26.7% — bad, but recoverable.

**Stella:** And if I go to 3x?

**Horace:** *(slides to 3x)* You are wiped. 3x with a minus 20%
move means minus 60% of equity plus borrow drag. The call fired
at minus 17%; you don't get to participate in the recovery.
Permanent loss of capital.

---

**[SEGMENT 6: WHEN LEVERAGE ACTUALLY WORKS]**

**Horace:** Leverage is not always wrong. Two cases where it
makes sense at retail:

One: defined-risk options spreads under portfolio margin. An
iron condor on SPX (week 30) has a known maximum loss; PM
margins it correctly; you get five times the buying power
without the path risk. The barbell.

Two: index futures (week 39). /MES at $5 a point, $26k notional,
$2k margin, financing implicit in the basis at SOFR plus 30.
Section 1256 60/40 tax. Best leverage tool retail has. The tax wrapper matters.

**Horace:** Both have a defined dollar risk per position. Both
finance near risk-free. Neither requires the broker to call you
on a Tuesday morning.

---

**[OUTRO]**

**Horace:** The summary in three sentences. Default brokerage
accounts are margin accounts and the agreement is not written to
protect you. Reg T plus FINRA plus house rules will force-
liquidate a 2x retail position on roughly every 10-year drawdown.
The expected geometric return on levered equity is flat to
negative once you pay the broker's spread, while the variance
quadruples — so the only intelligent retail leverage is
defined-risk options or index futures, not stock on margin.

**Stella:** I'm going to set up a cash account.

**Horace:** That is the conservative answer and it is the right
answer for most people. The lab is here when you change your
mind on a specific spread trade.

---

**END SCREEN:** "Next: Side 22 — Behavioural Audits and Pre-Mortems"
