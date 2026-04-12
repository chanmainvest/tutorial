"""
Week 48 - Buffered ETF Payoff Diagram
=======================================
Shows the payoff structure of a buffered (defined outcome) ETF:
  - X-axis: S&P 500 return over the outcome period
  - Y-axis: ETF return delivered to the investor
  - Buffer zone: absorbs first N% of downside (e.g., 10%)
  - Cap: maximum upside is capped (e.g., 15%)
  - Beyond buffer: investor bears remaining downside
Output: week48_buffered_payoff.png
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Buffered ETF parameters
# ---------------------------------------------------------------------------
buffer = 0.10   # 10% downside buffer
cap = 0.15      # 15% upside cap

# S&P 500 returns range
sp_returns = np.linspace(-0.40, 0.40, 1000)

# Calculate ETF returns based on buffered structure
etf_returns = np.zeros_like(sp_returns)
for i, r in enumerate(sp_returns):
    if r >= cap:
        # Capped at the upside limit
        etf_returns[i] = cap
    elif r >= 0:
        # Participate 1:1 up to cap
        etf_returns[i] = r
    elif r >= -buffer:
        # Buffer absorbs this loss; investor gets 0%
        etf_returns[i] = 0.0
    else:
        # Beyond buffer: investor bears losses past the buffer
        etf_returns[i] = r + buffer

# 1:1 reference line (unprotected S&P)
ref_returns = sp_returns.copy()

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))

# Reference line (1:1 S&P)
ax.plot(sp_returns * 100, ref_returns * 100, color="#BDBDBD", linewidth=1.5,
        linestyle="--", label="S&P 500 (no protection)", alpha=0.7)

# Buffered ETF payoff
ax.plot(sp_returns * 100, etf_returns * 100, color="#1976D2", linewidth=3,
        label="Buffered ETF Payoff")

# Shade the buffer zone
buffer_mask = (sp_returns >= -buffer) & (sp_returns < 0)
ax.fill_between(sp_returns[buffer_mask] * 100, ref_returns[buffer_mask] * 100,
                etf_returns[buffer_mask] * 100,
                color="#4CAF50", alpha=0.25, label=f"Buffer Zone ({buffer:.0%} protection)")

# Shade the cap region
cap_mask = sp_returns >= cap
ax.fill_between(sp_returns[cap_mask] * 100, etf_returns[cap_mask] * 100,
                ref_returns[cap_mask] * 100,
                color="#FF9800", alpha=0.2, label=f"Capped Upside (max {cap:.0%})")

# Zero lines
ax.axhline(y=0, color="gray", linewidth=0.8, alpha=0.5)
ax.axvline(x=0, color="gray", linewidth=0.8, alpha=0.5)

# Buffer boundary
ax.axvline(x=-buffer * 100, color="#4CAF50", linewidth=1.5, linestyle=":",
           alpha=0.7)
ax.text(-buffer * 100 - 1, cap * 100 - 2, f"Buffer\nEdge\n({-buffer:.0%})",
        fontsize=9, color="#2E7D32", ha="right", fontweight="bold")

# Cap boundary
ax.axhline(y=cap * 100, color="#FF9800", linewidth=1.5, linestyle=":",
           alpha=0.7)
ax.text(35, cap * 100 + 1, f"Cap = {cap:.0%}",
        fontsize=10, color="#E65100", fontweight="bold")

# Key point annotations
ax.annotate("Buffer absorbs\nfirst 10% of loss",
            xy=(-5, 0), xytext=(-25, 10),
            fontsize=10, color="#2E7D32", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#2E7D32"))

ax.annotate("Beyond buffer:\ninvestor bears loss",
            xy=(-25, -15), xytext=(-35, -25),
            fontsize=10, color="#C62828", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#C62828"))

# Formatting
ax.set_xlabel("S&P 500 Return (%)", fontsize=12)
ax.set_ylabel("Buffered ETF Return (%)", fontsize=12)
ax.set_title("Buffered ETF Payoff Structure:\n10% Buffer, 15% Cap",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="upper left")
ax.grid(True, alpha=0.3)
ax.set_xlim(-40, 40)
ax.set_ylim(-35, 35)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week48_buffered_payoff.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
