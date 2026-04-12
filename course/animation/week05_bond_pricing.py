"""
Week 05: Bond Pricing - Yield vs Price Inverse Relationship
=============================================================
Shows the inverse relationship between bond yield and bond price.
As yield rises from 2% to 8%, the price of a 5% coupon, 10-year bond falls.
Clearly labels the key insight: "Yield Up = Price Down".

Output: week05_bond_pricing.png
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Bond pricing formula ---
# Price = sum of PV of coupons + PV of face value
# Price = C * [1 - (1+y)^-n] / y + F / (1+y)^n

def bond_price(coupon_rate, face_value, yield_rate, years):
    """Calculate the price of a bond given its parameters."""
    coupon = coupon_rate * face_value
    if yield_rate == 0:
        return coupon * years + face_value
    pv_coupons = coupon * (1 - (1 + yield_rate) ** (-years)) / yield_rate
    pv_face = face_value / (1 + yield_rate) ** years
    return pv_coupons + pv_face

# --- Parameters ---
coupon_rate = 0.05     # 5% coupon
face_value = 1000      # $1,000 par value
years = 10             # 10-year bond
yields = np.linspace(0.02, 0.08, 100)  # Yield from 2% to 8%

# Calculate bond prices across the yield range
prices = [bond_price(coupon_rate, face_value, y, years) for y in yields]

# Key points to annotate
key_yields = [0.02, 0.05, 0.08]
key_prices = [bond_price(coupon_rate, face_value, y, years) for y in key_yields]
key_labels = [
    f"Yield=2%\nPrice=${key_prices[0]:,.2f}\n(Premium)",
    f"Yield=5%\nPrice=${key_prices[1]:,.2f}\n(Par Value)",
    f"Yield=8%\nPrice=${key_prices[2]:,.2f}\n(Discount)",
]

# --- Create figure ---
fig, ax = plt.subplots(figsize=(12, 7))

# Main price curve
ax.plot(yields * 100, prices, color="#1565C0", linewidth=3)

# Fill above and below par
ax.fill_between(yields * 100, prices, face_value, where=np.array(prices) > face_value,
                color="#4CAF50", alpha=0.15, label="Premium (price > par)")
ax.fill_between(yields * 100, prices, face_value, where=np.array(prices) < face_value,
                color="#F44336", alpha=0.15, label="Discount (price < par)")

# Par value reference line
ax.axhline(y=face_value, color="gray", linestyle="--", alpha=0.6, linewidth=1)
ax.text(7.5, face_value + 8, "Par Value ($1,000)", fontsize=10, color="gray")

# Annotate key points
colors_key = ["#2E7D32", "#1565C0", "#C62828"]
for ky, kp, kl, kc in zip(key_yields, key_prices, key_labels, colors_key):
    ax.scatter(ky * 100, kp, s=120, color=kc, zorder=5, edgecolors="white", linewidths=2)
    offset_y = 30 if kp > face_value else -50
    ax.annotate(
        kl,
        xy=(ky * 100, kp),
        xytext=(ky * 100, kp + offset_y),
        fontsize=10,
        fontweight="bold",
        color=kc,
        ha="center",
        arrowprops=dict(arrowstyle="->", color=kc, lw=1.5),
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=kc, alpha=0.9),
    )

# Big arrow showing the relationship
ax.annotate(
    "",
    xy=(7, min(prices) + 20),
    xytext=(3, max(prices) - 20),
    arrowprops=dict(arrowstyle="->, head_width=0.4", color="#FF5722", lw=3, alpha=0.3),
)
ax.text(5, np.mean(prices) + 40, "YIELD UP = PRICE DOWN",
        fontsize=14, fontweight="bold", color="#FF5722", ha="center", rotation=-25,
        bbox=dict(boxstyle="round", facecolor="#FFF3E0", edgecolor="#FF5722", alpha=0.8))

# --- Formatting ---
ax.set_title("Bond Pricing: Inverse Yield-Price Relationship\n(5% Coupon, 10-Year Bond, $1,000 Face Value)",
             fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel("Market Yield (%)", fontsize=14)
ax.set_ylabel("Bond Price ($)", fontsize=14)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.legend(fontsize=11, loc="upper right")
ax.grid(True, alpha=0.3, linestyle="--")

fig.tight_layout()

# --- Save output ---
output_path = "B:/chanmainvest/tutorial/course/animation/week05_bond_pricing.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
