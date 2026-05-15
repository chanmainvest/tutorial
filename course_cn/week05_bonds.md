<function_calls>
<invoke name="view">
<parameter name="path">C:\Users\hevan\AppData\Local\Temp\tmpk8cosai1.md</parameter>
</invoke>
</function_calls>
<function_response>
# Week 14 Part 1: Bond Risk Metrics – Duration and Convexity

## Overview

**Course:** Foundations of Investing
**Hosts:** Horace and Stella
**Format:** YouTube educational video script
**Length:** ~15 minutes
**Week:** 14, Part 1 of 2

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Explain what duration measures and why it matters for bond investors
2. Calculate Macaulay duration and modified duration
3. Interpret how duration predicts price changes when interest rates shift
4. Understand the limitations of duration and why convexity is needed
5. Calculate and apply convexity to improve price-change predictions

---

## Script

### Cold Open

[ANIMATION: A seesaw balancing coins on one side and a clock on the other]

**Horace:** Imagine you lend someone money for 10 years at 5%. Suddenly, market rates jump to 7%. Your bond's price just dropped — but by how much, exactly?

**Stella:** The answer isn't just "a lot." There's a precise mathematical framework for this — and today we're diving into two of the most important bond risk metrics: duration and convexity.

[CUT TO: Title card – "Bond Risk Metrics: Duration and Convexity"]

---

### Section 1: Why Bond Prices Move

[ANIMATION: Bond price vs. yield curve showing inverse relationship]

**Stella:** Let's start with the foundation. Bonds have an inverse relationship with interest rates — when rates go up, bond prices go down, and vice versa.

**Horace:** But not all bonds are equally sensitive. A 30-year bond drops far more than a 1-year bond when rates rise by 1%. Why?

**Stella:** Because of time. The longer you're locked into a fixed payment, the more exposed you are to rate changes.

**Horace:** And that's exactly what duration captures — the sensitivity of a bond's price to changes in interest rates.

[VISUAL: Show a 1-year bond vs 30-year bond side by side, with arrows showing different price changes for the same rate increase]

---

### Section 2: Macaulay Duration

[ANIMATION: Timeline with cash flows weighted by time]

**Stella:** There are a few versions of duration. Let's start with the original — Macaulay duration.

**Horace:** Macaulay duration is the weighted average time to receive a bond's cash flows. The weights are the present values of each cash flow as a fraction of the total bond price.

**Stella:** Think of it like a balance point. If you laid all the cash flows out on a timeline, Macaulay duration tells you where the "center of gravity" is.

**Horace:** Let's walk through an example.

[VISUAL: Table showing cash flows for a 3-year bond]

| Year | Cash Flow | PV of Cash Flow | Weight | Year × Weight |
|------|-----------|-----------------|--------|---------------|
| 1    | $50       | $47.62          | 0.0476 | 0.0476        |
| 2    | $50       | $45.35          | 0.0454 | 0.0907        |
| 3    | $1,050    | $907.03         | 0.9070 | 2.7211        |
| **Total** | | **$1,000** | **1.0000** | **2.859** |

**Stella:** So for a 3-year bond with a 5% coupon, priced at par, with a 5% yield — the Macaulay duration is approximately 2.86 years.

**Horace:** Notice it's less than 3 years — the maturity. That's because you're receiving coupon payments before maturity that pull the "center of gravity" forward.

**Stella:** A zero-coupon bond would have a Macaulay duration exactly equal to its maturity, since there's only one cash flow — at the end.

---

### Section 3: Modified Duration

[ANIMATION: Arrow showing rate change → price change, with a magnification lens on the formula]

**Horace:** Now, Macaulay duration is elegant, but what investors really care about is: if rates change, how much does my bond's price change?

**Stella:** That's what modified duration tells us.

**Horace:** The formula is simple:

$$\text{Modified Duration} = \frac{\text{Macaulay Duration}}{1 + \frac{y}{m}}$$

Where *y* is the yield and *m* is the number of compounding periods per year.

**Stella:** For our example — Macaulay duration of 2.86 years, yield of 5%, annual compounding:

$$\text{Modified Duration} = \frac{2.86}{1.05} \approx 2.724$$

**Horace:** And here's the key interpretation: a modified duration of 2.724 means that for every 1% increase in yield, the bond price falls by approximately 2.724%.

**Stella:** The formula for price change is:

$$\Delta P \approx -\text{Modified Duration} \times \Delta y \times P$$

**Horace:** Let's say rates rise by 0.5%. The estimated price change would be:

$$\Delta P \approx -2.724 \times 0.005 \times \$1000 = -\$13.62$$

**Stella:** So our $1,000 bond would drop to about $986.38 — that's duration in action.

---

### Section 4: Dollar Duration and DV01

[ANIMATION: Dollar sign merging with a bond certificate]

**Horace:** Traders often talk about dollar duration — which is just modified duration multiplied by the bond price.

**Stella:** Dollar Duration = Modified Duration × Price

**Horace:** A closely related concept is DV01 — the Dollar Value of a 1 Basis Point move. It tells you exactly how much a bond's price changes when yields move by 0.01%.

$$\text{DV01} = \frac{\text{Modified Duration} \times P}{10,000}$$

**Stella:** For our bond:

$$\text{DV01} = \frac{2.724 \times \$1000}{10,000} = \$0.2724$$

**Horace:** So for every basis point rates move, this bond gains or loses about 27 cents. That seems small, but for a portfolio of millions, it adds up fast.

**Stella:** DV01 is incredibly useful for hedging — you can match the DV01 of your portfolio to a hedge instrument and neutralize your rate exposure.

---

### Section 5: Duration of a Bond Portfolio

[ANIMATION: Multiple bonds combining into a single portfolio, with weighted average calculated]

**Horace:** When you hold multiple bonds, the portfolio duration is the weighted average of the individual durations.

**Stella:** Specifically:

$$D_{portfolio} = \sum_{i} w_i \times D_i$$

Where *w_i* is the market value weight of bond *i* in the portfolio.

**Horace:** Let's say you have:
- 40% in a bond with duration 2
- 35% in a bond with duration 5
- 25% in a bond with duration 10

**Stella:** Portfolio duration = 0.40×2 + 0.35×5 + 0.25×10 = 0.80 + 1.75 + 2.50 = **5.05**

**Horace:** So the portfolio behaves like a single bond with a duration of about 5 years.

---

### Section 6: Limitations of Duration

[ANIMATION: Duration prediction vs actual price change — a straight line vs a curve]

**Stella:** Duration is powerful, but it has a critical limitation — it assumes a linear relationship between yield changes and price changes.

**Horace:** In reality, that relationship is curved. Let's illustrate.

[VISUAL: Price-yield curve with tangent line (duration estimate) vs actual curve]

**Stella:** Look at this price-yield graph. The actual bond price curve is convex — it curves upward. The duration estimate is just a tangent line at the current yield.

**Horace:** For small rate changes, the tangent line is a great approximation. But for large moves — say 2% or 3% — the error becomes significant.

**Stella:** Here's the key insight: the tangent line always *underestimates* the actual bond price. That means duration always overpredicts price drops and underpredicts price gains.

**Horace:** This is actually good news for bond investors — it means bonds outperform the duration estimate in both directions.

---

### Section 7: Convexity

[ANIMATION: Parabola fitting to the bond price-yield curve]

**Stella:** To fix this, we add a second-order correction term — that's convexity.

**Horace:** Mathematically, think of it like a Taylor expansion. Duration gives you the first derivative (slope), and convexity gives you the second derivative (curvature).

**Stella:** The full price change formula with convexity is:

$$\Delta P \approx -D_{mod} \times \Delta y \times P + \frac{1}{2} \times C \times (\Delta y)^2 \times P$$

Where *C* is the convexity.

**Horace:** Convexity is always positive for regular bonds — so the second term always adds to the price, improving the estimate.

**Stella:** Let's calculate convexity for a simple case.

[VISUAL: Convexity calculation table]

$$C = \frac{1}{P \times (1+y)^2} \sum_{t=1}^{n} \frac{t(t+1) \times CF_t}{(1+y)^t}$$

**Horace:** For most practical purposes, you can approximate convexity as:

$$C \approx \frac{P_{up} + P_{down} - 2P_0}{P_0 \times (\Delta y)^2}$$

**Stella:** Where *P_up* and *P_down* are the bond prices when yields go up and down by some small amount Δy.

**Horace:** Let's say our bond:
- *P_0* = $1,000 (current price)
- *P_up* = $973.77 (yield + 1%)
- *P_down* = $1,027.75 (yield − 1%)

$$C = \frac{973.77 + 1027.75 - 2(1000)}{1000 \times (0.01)^2} = \frac{1.52}{0.10} = 15.2$$

**Stella:** So the convexity is approximately 15.2.

---

### Section 8: Putting It All Together

[ANIMATION: Side-by-side comparison of duration-only estimate vs duration + convexity estimate]

**Horace:** Now let's use both duration and convexity to estimate the price change when yields rise by 2%.

**Stella:** We have:
- Modified Duration = 2.724
- Convexity = 15.2
- Δy = 0.02
- P = $1,000

**Horace:** Duration-only estimate:

$$\Delta P_{dur} = -2.724 \times 0.02 \times 1000 = -\$54.48$$

**Stella:** Adding convexity correction:

$$\Delta P_{conv} = \frac{1}{2} \times 15.2 \times (0.02)^2 \times 1000 = \$3.04$$

**Horace:** Total estimated price change:

$$\Delta P \approx -\$54.48 + \$3.04 = -\$51.44$$

**Stella:** Compare that to the duration-only estimate of −$54.48. The convexity correction gives us a more accurate, more favorable estimate.

**Horace:** And the more convex a bond, the better it performs relative to its duration in both rising and falling rate environments.

---

### Section 9: Negative Convexity

[ANIMATION: Mortgage-backed security vs regular bond, showing different price-yield curves]

**Stella:** Not all bonds have positive convexity. Bonds with embedded options — like callable bonds or mortgage-backed securities — can exhibit negative convexity.

**Horace:** With a callable bond, when rates fall, the issuer can call the bond and refinance at lower rates. This caps the price upside.

**Stella:** The result: the price-yield curve bends the *wrong* way in a falling rate environment — that's negative convexity.

**Horace:** Mortgage-backed securities are the classic example. When rates fall, homeowners refinance — effectively "calling" the mortgage early. This creates prepayment risk and negative convexity.

**Stella:** So investors in mortgage-backed securities demand higher yields to compensate for this negative convexity.

---

### Section 10: Practical Applications

[ANIMATION: Portfolio manager at a desk with rate change scenarios]

**Horace:** So how do professional bond managers actually use these metrics?

**Stella:** First — **immunization**. If you have a liability due in 5 years, you can match your portfolio duration to 5 years. This hedges your interest rate risk.

**Horace:** Second — **risk measurement**. Duration and convexity tell you exactly how sensitive your portfolio is to rate movements.

**Stella:** Third — **relative value**. A bond with higher convexity is more valuable, all else equal, because it outperforms in both rising and falling rate environments.

**Horace:** Fourth — **hedging**. Using DV01, you can hedge your portfolio against rate movements using Treasuries, interest rate futures, or interest rate swaps.

---

### Closing Summary

[ANIMATION: Visual recap of all concepts]

**Horace:** Let's recap.

**Stella:** Duration measures how sensitive a bond's price is to interest rate changes. Macaulay duration is the weighted average time to receive cash flows. Modified duration gives you the percentage price change per 1% yield change.

**Horace:** DV01 tells you the dollar price change per basis point. Portfolio duration is the weighted average of individual durations.

**Stella:** Convexity captures the curvature of the price-yield relationship, improving the duration estimate — especially for large rate moves.

**Horace:** Positive convexity is good — it means the bond outperforms its duration estimate in both directions. Negative convexity, seen in callable bonds and mortgage-backed securities, is a risk.

**Stella:** These metrics are foundational for any serious bond investor or portfolio manager. In Part 2, we'll look at real bond portfolios and how managers use duration targeting and convexity optimization in practice.

**Horace:** If this was helpful, hit subscribe and we'll see you in Part 2!

[CUT TO: End screen with subscribe button and links to Week 14 Part 2 and Week 13]

---

## Key Formulas Reference

| Formula | Description |
|---------|-------------|
| $D_{mac} = \sum \frac{t \cdot PV(CF_t)}{P}$ | Macaulay Duration |
| $D_{mod} = \frac{D_{mac}}{1 + y/m}$ | Modified Duration |
| $\Delta P \approx -D_{mod} \cdot \Delta y \cdot P$ | Duration price approximation |
| $DV01 = \frac{D_{mod} \cdot P}{10000}$ | Dollar value of 1bp |
| $D_{port} = \sum w_i D_i$ | Portfolio Duration |
| $C \approx \frac{P_{up} + P_{down} - 2P_0}{P_0 \cdot (\Delta y)^2}$ | Convexity approximation |
| $\Delta P \approx -D_{mod} \cdot \Delta y \cdot P + \frac{1}{2} C (\Delta y)^2 P$ | Duration + Convexity approximation |

---

## Visual Assets Required

1. **Seesaw animation** – coins vs. clock (cold open)
2. **Price-yield curve** – inverse relationship illustration
3. **1-year vs 30-year bond comparison** – different sensitivities
4. **Macaulay duration timeline** – cash flows on a timeline with balance point
5. **Modified duration arrow diagram** – rate change → price change
6. **Dollar duration / DV01 animation** – dollar sign merging with bond
7. **Portfolio duration bar chart** – three bonds with weights
8. **Price-yield curve with tangent line** – showing limitation of duration
9. **Parabola overlay on price-yield curve** – convexity correction
10. **Callable bond vs regular bond curve** – negative convexity
11. **Portfolio manager scenario** – practical applications

---

## Instructor Notes

- Emphasize the intuition of Macaulay duration as "center of gravity" — students find this visual very helpful
- The Taylor expansion analogy for convexity resonates with students who have calculus backgrounds; for others, just focus on "first-order vs second-order correction"
- Negative convexity is often the most surprising concept — use the mortgage refinancing story to make it concrete
- The immunization application is directly relevant to pension fund management — worth emphasizing for students interested in institutional investing
</parameter>
</invoke>
</function_calls>
<function_response>
Successfully read file: C:\Users\hevan\AppData\Local\Temp\tmpk8cosai1.md
</parameter>
</invoke>
</function_calls>

# 第14周 第1部分：债券风险指标——久期与凸性

## 概述

**课程：** 投资基础
**主持人：** 陳馬 和 小魚
**形式：** YouTube 教育视频脚本
**时长：** 约15分钟
**周次：** 第14周，第1部分（共2部分）

---

## 学习目标

完成本课后，学员将能够：

1. 解释久期的衡量内容及其对债券投资者的重要意义
2. 计算麦考利久期和修正久期
3. 解读久期如何预测利率变动时的价格变化
4. 理解久期的局限性以及为何需要凸性
5. 计算并运用凸性来改善价格变动预测

---

## 脚本

### 冷开场

[ANIMATION: A seesaw balancing coins on one side and a clock on the other]

**陳馬：** 想象一下，你以5%的利率把钱借给别人，期限10年。突然，市场利率跳升至7%。你的债券价格刚刚下跌了——但究竟跌了多少？

**小魚：** 答案不只是"跌了很多"。这背后有一套精确的数学框架——今天我们将深入探讨两个最重要的债券风险指标：久期和凸性。

[CUT TO: Title card – "Bond Risk Metrics: Duration and Convexity"]

---

### 第一节：为什么债券价格会波动

[ANIMATION: Bond price vs. yield curve showing inverse relationship]

**小魚：** 我们先来打好基础。债券与利率之间存在反向关系——利率上升，债券价格下跌，反之亦然。

**陳馬：** 但并非所有债券的敏感度都一样。利率上升1%，30年期债券的跌幅远大于1年期债券。为什么？

**小魚：** 因为时间。你被锁定在固定支付上的时间越长，就越容易受到利率变化的影响。

**陳馬：** 这正是久期所捕捉的——债券价格对利率变化的敏感程度。

[VISUAL: Show a 1-year bond vs 30-year bond side by side, with arrows showing different price changes for the same rate increase]

---

### 第二节：麦考利久期

[ANIMATION: Timeline with cash flows weighted by time]

**小魚：** 久期有几个版本。我们先从最原始的——麦考利久期开始讲起。

**陳馬：** 麦考利久期是收到债券现金流的加权平均时间。权重是每笔现金流的现值占债券总价格的比例。

**小魚：** 把它想象成一个平衡点。如果你把所有现金流摆在时间轴上，麦考利久期就告诉你"重心"在哪里。

**陳馬：** 我们来看一个例子。

[VISUAL: Table showing cash flows for a 3-year bond]

| 年份 | 现金流 | 现金流现值 | 权重 | 年份 × 权重 |
|------|--------|------------|------|-------------|
| 1    | $50    | $47.62     | 0.0476 | 0.0476   |
| 2    | $50    | $45.35     | 0.0454 | 0.0907   |
| 3    | $1,050 | $907.03    | 0.9070 | 2.7211   |
| **合计** | | **$1,000** | **1.0000** | **2.859** |

**小魚：** 对于一只3年期、票息率5%、按面值定价、收益率为5%的债券，麦考利久期约为2.86年。

**陳馬：** 注意，这比3年的到期期限要短。原因是你在到期前就已经收到了票息支付，这些支付将"重心"向前拉动了。

**小魚：** 零息债券的麦考利久期则恰好等于其到期期限，因为只有一笔现金流——在最末端。

---

### 第三节：修正久期

[ANIMATION: Arrow showing rate change → price change, with a magnification lens on the formula]

**陳馬：** 麦考利久期固然优雅，但投资者真正关心的是：利率变动时，我的债券价格会变化多少？

**小魚：** 这正是修正久期所告诉我们的。

**陳馬：** 公式很简单：

$$\text{修正久期} = \frac{\text{麦考利久期}}{1 + \frac{y}{m}}$$

其中 *y* 为收益率，*m* 为每年的复利次数。

**小魚：** 以我们的例子为例——麦考利久期2.86年，收益率5%，按年复利：

$$\text{修正久期} = \frac{2.86}{1.05} \approx 2.724$$

**陳馬：** 关键解读是：修正久期为2.724，意味着收益率每上升1%，债券价格约下跌2.724%。

**小魚：** 价格变动的公式为：

$$\Delta P \approx -\text{修正久期} \times \Delta y \times P$$

**陳馬：** 假设利率上升0.5%，预计价格变动为：

$$\Delta P \approx -2.724 \times 0.005 \times \$1000 = -\$13.62$$

**小魚：** 所以我们这只1,000美元的债券将跌至约986.38美元——这就是久期的实际应用。

---

### 第四节：美元久期与DV01

[ANIMATION: Dollar sign merging with a bond certificate]

**陳馬：** 交易员常常谈到美元久期——它就是修正久期乘以债券价格。

**小魚：** 美元久期 = 修正久期 × 价格

**陳馬：** 一个密切相关的概念是DV01——即1个基点变动的美元价值。它精确地告诉你，当收益率变动0.01%时，债券价格的变化幅度。

$$\text{DV01} = \frac{\text{修正久期} \times P}{10,000}$$

**小魚：** 对于我们这只债券：

$$\text{DV01} = \frac{2.724 \times \$1000}{10,000} = \$0.2724$$

**陳馬：** 因此，利率每变动一个基点，这只债券的价格变化约为27美分。看似不多，但对于数百万规模的投资组合而言，累积起来相当可观。

**小魚：** DV01在对冲上极为实用——你可以将投资组合的DV01与对冲工具进行匹配，从而消除利率风险敞口。

---

### 第五节：债券投资组合的久期

[ANIMATION: Multiple bonds combining into a single portfolio, with weighted average calculated]

**陳馬：** 持有多只债券时，投资组合的久期是各只债券久期的加权平均值。

**小魚：** 具体公式为：

$$D_{投资组合} = \sum_{i} w_i \times D_i$$

其中 *w_i* 是债券 *i* 在投资组合中的市值权重。

**陳馬：** 假设你持有：
- 40%配置在久期为2的债券
- 35%配置在久期为5的债券
- 25%配置在久期为10的债券

**小魚：** 投资组合久期 = 0.40×2 + 0.35×5 + 0.25×10 = 0.80 + 1.75 + 2.50 = **5.05**

**陳馬：** 所以该投资组合的表现就像一只久期约为5年的单只债券。

---

### 第六节：久期的局限性

[ANIMATION: Duration prediction vs actual price change — a straight line vs a curve]

**小魚：** 久期很强大，但有一个关键局限——它假设收益率变动与价格变动之间是线性关系。

**陳馬：** 而实际上，这种关系是曲线型的。我们来直观说明一下。

[VISUAL: Price-yield curve with tangent line (duration estimate) vs actual curve]

**小魚：** 看这张价格-收益率图。实际债券价格曲线是凸形的——它向上弯曲。而久期估计只是当前收益率处的切线。

**陳馬：** 对于小幅利率变动，切线是很好的近似。但对于大幅变动——比如2%或3%——误差就会变得相当大。

**小魚：** 关键洞察在于：切线总是*低估*实际债券价格。这意味着久期总是高估价格跌幅、低估价格涨幅。

**陳馬：** 这对债券投资者来说其实是个好消息——意味着债券在两个方向上的表现都优于久期估算。

---

### 第七节：凸性

[ANIMATION: Parabola fitting to the bond price-yield curve]

**小魚：** 为了修正这一问题，我们加入一个二阶修正项——这就是凸性。

**陳馬：** 从数学上讲，把它想象成泰勒展开。久期给你的是一阶导数（斜率），凸性给你的是二阶导数（曲率）。

**小魚：** 加入凸性后，完整的价格变动公式为：

$$\Delta P \approx -D_{修正} \times \Delta y \times P + \frac{1}{2} \times C \times (\Delta y)^2 \times P$$

其中 *C* 为凸性。

**陳馬：** 对于普通债券，凸性始终为正——因此第二项始终增加价格，改善估算结果。

**小魚：** 我们来计算一个简单案例的凸性。

[VISUAL: Convexity calculation table]

$$C = \frac{1}{P \times (1+y)^2} \sum_{t=1}^{n} \frac{t(t+1) \times CF_t}{(1+y)^t}$$

**陳馬：** 在大多数实际应用中，你可以用以下方式近似计算凸性：

$$C \approx \frac{P_{上行} + P_{下行} - 2P_0}{P_0 \times (\Delta y)^2}$$

**小魚：** 其中 *P_上行* 和 *P_下行* 分别是收益率上升和下降某一小幅Δy时的债券价格。

**陳馬：** 假设我们的债券：
- *P_0* = $1,000（当前价格）
- *P_上行* = $973.77（收益率上升1%）
- *P_下行* = $1,027.75（收益率下降1%）

$$C = \frac{973.77 + 1027.75 - 2(1000)}{1000 \times (0.01)^2} = \frac{1.52}{0.10} = 15.2$$

**小魚：** 所以凸性约为15.2。

---

### 第八节：综合运用

[ANIMATION: Side-by-side comparison of duration-only estimate vs duration + convexity estimate]

**陳馬：** 现在，我们同时用久期和凸性来估算收益率上升2%时的价格变动。

**小魚：** 已知条件：
- 修正久期 = 2.724
- 凸性 = 15.2
- Δy = 0.02
- P = $1,000

**陳馬：** 仅用久期估算：

$$\Delta P_{久期} = -2.724 \times 0.02 \times 1000 = -\$54.48$$

**小魚：** 加入凸性修正：

$$\Delta P_{凸性} = \frac{1}{2} \times 15.2 \times (0.02)^2 \times 1000 = \$3.04$$

**陳馬：** 总估算价格变动：

$$\Delta P \approx -\$54.48 + \$3.04 = -\$51.44$$

**小魚：** 与仅用久期的估算−$54.48相比，凸性修正给出了更精确、更有利的估算结果。

**陳馬：** 债券的凸性越高，在利率上升和下降的环境中，其实际表现相对久期估算都越好。

---

### 第九节：负凸性

[ANIMATION: Mortgage-backed security vs regular bond, showing different price-yield curves]

**小魚：** 并非所有债券都具有正凸性。含有嵌入期权的债券——如可赎回债券或抵押贷款支持证券——可能呈现负凸性。

**陳馬：** 对于可赎回债券，当利率下降时，发行人可以赎回债券并以更低的利率再融资。这限制了价格的上行空间。

**小魚：** 结果是：在利率下降的环境中，价格-收益率曲线弯向了*错误*的方向——这就是负凸性。

**陳馬：** 抵押贷款支持证券是最典型的例子。当利率下降时，房主提前还款再融资——实际上相当于提前"赎回"了抵押贷款。这产生了提前还款风险和负凸性。

**小魚：** 因此，抵押贷款支持证券的投资者要求更高的收益率，以补偿这种负凸性。

---

### 第十节：实际应用

[ANIMATION: Portfolio manager at a desk with rate change scenarios]

**陳馬：** 那么，专业债券基金经理实际上是如何运用这些指标的呢？

**小魚：** 第一——**免疫策略**。如果你5年后有一笔负债，可以将投资组合的久期匹配至5年，从而对冲利率风险。

**陳馬：** 第二——**风险度量**。久期和凸性能精确告诉你，投资组合对利率变动的敏感程度。

**小魚：** 第三——**相对价值**。在其他条件相同的情况下，凸性更高的债券更有价值，因为它在利率上升和下降的环境中都有更优的表现。

**陳馬：** 第四——**对冲**。利用DV01，你可以使用国债、利率期货或利率互换来对冲投资组合的利率风险敞口。

---

### 结尾总结

[ANIMATION: Visual recap of all concepts]

**陳馬：** 我们来回顾一下。

**小魚：** 久期衡量债券价格对利率变化的敏感程度。麦考利久期是收到现金流的加权平均时间。修正久期给出的是收益率每变动1%时价格的百分比变化。

**陳馬：** DV01告诉你每个基点变动对应的美元价格变化。投资组合久期是各只债券久期的加权平均值。

**小魚：** 凸性捕捉了价格-收益率关系的曲率，改善了久期估算——尤其是在利率大幅变动时。

**陳馬：** 正凸性是有利的——意味着债券在两个方向上的实际表现均优于久期估算。可赎回债券和抵押贷款支持证券中出现的负凸性则是一种风险。

**小魚：** 这些指标是任何认真的债券投资者或基金经理的基础工具。在第2部分中，我们将着眼于真实债券投资组合，探讨基金经理在实践中如何运用久期管理目标和凸性优化策略。

**陳馬：** 如果本期内容对你有帮助，点击订阅，我们第2部分见！

[CUT TO: End screen with subscribe button and links to Week 14 Part 2 and Week 13]

---

## 核心公式参考

| 公式 | 说明 |
|------|------|
| $D_{mac} = \sum \frac{t \cdot PV(CF_t)}{P}$ | 麦考利久期 |
| $D_{mod} = \frac{D_{mac}}{1 + y/m}$ | 修正久期 |
| $\Delta P \approx -D_{mod} \cdot \Delta y \cdot P$ | 久期价格近似公式 |
| $DV01 = \frac{D_{mod} \cdot P}{10000}$ | 1个基点的美元价值 |
| $D_{port} = \sum w_i D_i$ | 投资组合久期 |
| $C \approx \frac{P_{up} + P_{down} - 2P_0}{P_0 \cdot (\Delta y)^2}$ | 凸性近似公式 |
| $\Delta P \approx -D_{mod} \cdot \Delta y \cdot P + \frac{1}{2} C (\Delta y)^2 P$ | 久期+凸性近似公式 |

---

## 所需视觉素材

1. **跷跷板动画** —— 硬币与时钟（冷开场）
2. **价格-收益率曲线** —— 反向关系图示
3. **1年期与30年期债券对比** —— 不同敏感度展示
4. **麦考利久期时间轴** —— 带平衡点的现金流时间轴
5. **修正久期箭头图** —— 利率变动→价格变动
6. **美元久期/DV01动画** —— 美元符号与债券合并
7. **投资组合久期柱状图** —— 三只债券及其权重
8. **带切线的价格-收益率曲线** —— 展示久期的局限性
9. **价格-收益率曲线上叠加的抛物线** —— 凸性修正
10. **可赎回债券与普通债券曲线对比** —— 负凸性展示
11. **基金经理情景演示** —— 实际应用

---

## 教师注记

- 重点强调麦考利久期作为"重心"的直觉理解——学生普遍觉得这个视觉化表达非常有帮助
- 凸性的泰勒展开类比对有微积分背景的学生很有共鸣；对于其他学生，只需聚焦于"一阶修正与二阶修正"的概念即可
- 负凸性往往是最令人意外的概念——用抵押贷款再融资的故事来让它变得具体生动
- 免疫策略的应用与养老基金管理直接相关——对于有志于机构投资领域的学生，值得重点强调