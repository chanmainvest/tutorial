"""
Week 47 - Tail Risk: Normal vs Fat-Tailed Distribution
========================================================
Compares a normal distribution with a fat-tailed distribution
(Student's t with low degrees of freedom). Highlights the
excess probability mass in the tails where extreme events live.
Output: week47_tail_distribution.png
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# ---------------------------------------------------------------------------
# Distributions
# ---------------------------------------------------------------------------
x = np.linspace(-6, 6, 1000)

# Normal distribution (mu=0, sigma=1)
normal_pdf = stats.norm.pdf(x, 0, 1)

# Fat-tailed: Student's t with 3 degrees of freedom (heavy tails)
t_df = 3
t_pdf = stats.t.pdf(x, df=t_df)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Main curves
ax.plot(x, normal_pdf, color="#2196F3", linewidth=2.5,
        label="Normal Distribution")
ax.plot(x, t_pdf, color="#F44336", linewidth=2.5,
        label=f"Fat-Tailed (t, df={t_df})")

# Shade the left tail difference (x < -2.5)
tail_mask = x <= -2.5
ax.fill_between(x[tail_mask], normal_pdf[tail_mask], t_pdf[tail_mask],
                where=t_pdf[tail_mask] > normal_pdf[tail_mask],
                color="#F44336", alpha=0.3, label="Excess Tail Risk")

# Shade the right tail difference (x > 2.5)
tail_mask_r = x >= 2.5
ax.fill_between(x[tail_mask_r], normal_pdf[tail_mask_r], t_pdf[tail_mask_r],
                where=t_pdf[tail_mask_r] > normal_pdf[tail_mask_r],
                color="#F44336", alpha=0.3)

# Annotations for tail difference
ax.annotate("Fat tails:\nExtreme events\nmore likely",
            xy=(-3.5, stats.t.pdf(-3.5, t_df)),
            xytext=(-5, 0.15),
            fontsize=10, color="#C62828", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#C62828", lw=1.5))

ax.annotate("Fat tails:\nExtreme events\nmore likely",
            xy=(3.5, stats.t.pdf(3.5, t_df)),
            xytext=(3.8, 0.15),
            fontsize=10, color="#C62828", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#C62828", lw=1.5))

# Probability comparison box
# P(X < -3) for each distribution
p_normal = stats.norm.cdf(-3)
p_t = stats.t.cdf(-3, df=t_df)
props = dict(boxstyle="round,pad=0.5", facecolor="#FFF9C4", edgecolor="#F9A825", alpha=0.9)
comparison = (f"P(X < -3 sigma):\n"
              f"  Normal:    {p_normal:.4f} ({p_normal*100:.2f}%)\n"
              f"  Fat-tailed: {p_t:.4f} ({p_t*100:.2f}%)\n"
              f"  Ratio:     {p_t/p_normal:.1f}x more likely!")
ax.text(0.97, 0.97, comparison, transform=ax.transAxes,
        fontsize=10, verticalalignment="top", horizontalalignment="right",
        bbox=props, family="monospace")

# Center peak annotation
ax.annotate("Higher peak\nin normal",
            xy=(0, stats.norm.pdf(0)),
            xytext=(1.3, 0.38),
            fontsize=9, color="#1565C0",
            arrowprops=dict(arrowstyle="->", color="#1565C0"))

# Formatting
ax.set_xlabel("Standard Deviations from Mean", fontsize=12)
ax.set_ylabel("Probability Density", fontsize=12)
ax.set_title("Normal vs Fat-Tailed Distribution:\nWhere Extreme Events Hide",
             fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="upper left")
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(0, 0.45)

plt.tight_layout()

# Save output
output_path = os.path.join(os.path.dirname(__file__), "week47_tail_distribution.png")
plt.savefig(output_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
