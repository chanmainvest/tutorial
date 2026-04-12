"""
Week 29: Option Greeks Visualisation (2x2 Grid)
=================================================
Four panels showing how each Greek behaves:
  Top-left:     Delta vs Stock Price
  Top-right:    Theta vs Time to Expiry
  Bottom-left:  Vega  vs Implied Volatility
  Bottom-right: Gamma vs Stock Price

Uses simplified Black-Scholes-style shapes for clarity.

Output: week29_greeks_visual.png
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------------------------------------------------------
# Black-Scholes helper functions
# -------------------------------------------------------------------
def bs_d1(S, K, T, r, sigma):
    """Calculate d1 in the Black-Scholes formula."""
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def bs_delta(S, K, T, r, sigma):
    """Call delta."""
    return norm.cdf(bs_d1(S, K, T, r, sigma))

def bs_gamma(S, K, T, r, sigma):
    """Call/put gamma."""
    d1 = bs_d1(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def bs_theta(S, K, T, r, sigma):
    """Call theta (per year, negative value)."""
    d1 = bs_d1(S, K, T, r, sigma)
    d2 = d1 - sigma * np.sqrt(T)
    term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    term2 = -r * K * np.exp(-r * T) * norm.cdf(d2)
    return (term1 + term2) / 365  # per-day theta

def bs_vega(S, K, T, r, sigma):
    """Call/put vega."""
    d1 = bs_d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T) / 100  # per 1% vol change

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------
K = 100       # strike
r = 0.05      # risk-free rate
sigma = 0.25  # implied vol (baseline)
T_base = 0.25 # 3 months to expiry (baseline)

# -------------------------------------------------------------------
# Create the 2x2 figure
# -------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# ---- Panel 1: Delta vs Stock Price --------------------------------
ax = axes[0, 0]
S_range = np.linspace(60, 140, 300)
for t_label, t_val in [("90 days", 90/365), ("30 days", 30/365), ("7 days", 7/365)]:
    delta_vals = bs_delta(S_range, K, t_val, r, sigma)
    ax.plot(S_range, delta_vals, linewidth=2, label=t_label)

ax.axvline(K, color="grey", linestyle=":", linewidth=1)
ax.axhline(0.5, color="grey", linestyle="--", linewidth=0.8, alpha=0.5)
ax.set_title("Delta vs Stock Price", fontsize=12, fontweight="bold")
ax.set_xlabel("Stock Price ($)")
ax.set_ylabel("Delta")
ax.legend(title="Time to Expiry", fontsize=8)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)
ax.annotate("ATM", xy=(K, 0.5), xytext=(K + 8, 0.3),
            fontsize=9, arrowprops=dict(arrowstyle="->", lw=1))

# ---- Panel 2: Theta vs Time to Expiry ----------------------------
ax = axes[0, 1]
T_range = np.linspace(1/365, 1.0, 300)  # 1 day to 1 year
for moneyness_label, s_val in [("ITM ($110)", 110), ("ATM ($100)", 100), ("OTM ($90)", 90)]:
    theta_vals = bs_theta(s_val, K, T_range, r, sigma)
    ax.plot(T_range * 365, theta_vals, linewidth=2, label=moneyness_label)

ax.set_title("Theta vs Days to Expiry", fontsize=12, fontweight="bold")
ax.set_xlabel("Days to Expiration")
ax.set_ylabel("Theta ($ / day)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.invert_xaxis()  # more intuitive: time counts down
ax.annotate("Decay accelerates\nnear expiry", xy=(15, -0.12),
            fontsize=9, fontweight="bold", color="#F44336",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFEBEE", alpha=0.8))

# ---- Panel 3: Vega vs Implied Volatility -------------------------
ax = axes[1, 0]
sigma_range = np.linspace(0.05, 0.80, 300)
for moneyness_label, s_val in [("ITM ($110)", 110), ("ATM ($100)", 100), ("OTM ($90)", 90)]:
    vega_vals = bs_vega(s_val, K, T_base, r, sigma_range)
    ax.plot(sigma_range * 100, vega_vals, linewidth=2, label=moneyness_label)

ax.set_title("Vega vs Implied Volatility", fontsize=12, fontweight="bold")
ax.set_xlabel("Implied Volatility (%)")
ax.set_ylabel("Vega ($ per 1% vol)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.annotate("ATM options have\nhighest Vega", xy=(25, 0.25),
            fontsize=9, fontweight="bold", color="#1565C0",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E3F2FD", alpha=0.8))

# ---- Panel 4: Gamma vs Stock Price -------------------------------
ax = axes[1, 1]
S_range = np.linspace(60, 140, 300)
for t_label, t_val, clr in [("90 days", 90/365, "#2196F3"),
                              ("30 days", 30/365, "#FF9800"),
                              ("7 days",   7/365, "#F44336")]:
    gamma_vals = bs_gamma(S_range, K, t_val, r, sigma)
    ax.plot(S_range, gamma_vals, linewidth=2, label=t_label, color=clr)

ax.axvline(K, color="grey", linestyle=":", linewidth=1)
ax.set_title("Gamma vs Stock Price", fontsize=12, fontweight="bold")
ax.set_xlabel("Stock Price ($)")
ax.set_ylabel("Gamma")
ax.legend(title="Time to Expiry", fontsize=8)
ax.grid(True, alpha=0.3)
ax.annotate("Gamma peaks ATM\nand near expiry", xy=(K, 0.06),
            xytext=(K + 12, 0.05),
            fontsize=9, fontweight="bold", color="#F44336",
            arrowprops=dict(arrowstyle="->", color="#F44336", lw=1))

# -------------------------------------------------------------------
# Final layout
# -------------------------------------------------------------------
fig.suptitle("The Option Greeks", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week29_greeks_visual.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week29_greeks_visual.png")
