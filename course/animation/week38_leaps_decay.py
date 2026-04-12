"""
Week 38: LEAPS Time Decay -- Theta vs Days to Expiration
==========================================================
Shows the theta (time decay) curve for an ATM option from 2 years
out to expiration. Highlights how decay is nearly flat for LEAPS
but accelerates dramatically in the last 30-60 days.

Output: week38_leaps_decay.png
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------------------------------------------
# Black-Scholes theta calculation
# -------------------------------------------------------------------
def bs_theta_per_day(S, K, T, r, sigma):
    """
    Daily theta for an ATM call option.
    Returns a negative value (time costs money for long options).
    """
    if T <= 0:
        return 0.0
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    theta_annual = (
        -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        - r * K * np.exp(-r * T) * norm.cdf(d2)
    )
    return theta_annual / 365  # convert to per-day

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
S = 100       # stock price
K = 100       # ATM strike
r = 0.05      # risk-free rate
sigma = 0.25  # implied vol

# Days from 730 (2 years) down to 1
days = np.arange(730, 0, -1)
T_values = days / 365.0

# Calculate theta for each day
theta_values = np.array([bs_theta_per_day(S, K, t, r, sigma) for t in T_values])
theta_abs = np.abs(theta_values)  # plot as positive for clarity

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(days, theta_abs, color="#1565C0", linewidth=2.5)

# Shade LEAPS zone (> 365 days)
leaps_mask = days >= 365
ax.fill_between(days[leaps_mask], 0, theta_abs[leaps_mask],
                color="#4CAF50", alpha=0.15, label="LEAPS Zone (>1 year)")

# Shade moderate decay zone (60-365 days)
moderate_mask = (days >= 60) & (days < 365)
ax.fill_between(days[moderate_mask], 0, theta_abs[moderate_mask],
                color="#FFC107", alpha=0.15, label="Moderate Decay (60d-1yr)")

# Shade accelerated decay zone (< 60 days)
accel_mask = days <= 60
ax.fill_between(days[accel_mask], 0, theta_abs[accel_mask],
                color="#F44336", alpha=0.20, label="Accelerated Decay (<60d)")

# Key vertical lines
ax.axvline(365, color="#4CAF50", linewidth=1.5, linestyle="--", alpha=0.7)
ax.axvline(60, color="#FF9800", linewidth=1.5, linestyle="--", alpha=0.7)
ax.axvline(30, color="#F44336", linewidth=1.5, linestyle="--", alpha=0.7)

# Annotations
ax.annotate("1 Year", xy=(365, 0.01), xytext=(400, 0.05),
            fontsize=10, color="#4CAF50", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#4CAF50", lw=1.2))

ax.annotate("60 Days:\nDecay starts\naccelerating",
            xy=(60, 0.04), xytext=(120, 0.08),
            fontsize=9, color="#FF9800", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#FF9800", lw=1.2))

ax.annotate("30 Days:\nSteepest\ndecay",
            xy=(30, 0.07), xytext=(80, 0.12),
            fontsize=9, color="#F44336", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#F44336", lw=1.2))

# LEAPS advantage box
ax.text(0.72, 0.95,
        "LEAPS Advantage:\nMinimal daily theta cost.\n"
        "Buy time cheaply when >1 year out.",
        transform=ax.transAxes, fontsize=9, fontweight="bold",
        verticalalignment="top", color="#2E7D32",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#E8F5E9", alpha=0.9))

# Theta formula note
ax.text(0.72, 0.60,
        r"$\Theta \propto \frac{1}{\sqrt{T}}$"
        "\nTheta grows as square root\nof time shrinks.",
        transform=ax.transAxes, fontsize=9, verticalalignment="top",
        color="#555",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF9C4", alpha=0.8))

# Labels and formatting
ax.set_title("Time Decay (Theta) vs Days to Expiration",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Days to Expiration", fontsize=12)
ax.set_ylabel("Theta ($ lost per day, absolute value)", fontsize=12)
ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.3)
ax.set_xlim(730, 0)  # countdown towards expiration (right to left)
ax.set_ylim(0, max(theta_abs) * 1.15)

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week38_leaps_decay.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week38_leaps_decay.png")
