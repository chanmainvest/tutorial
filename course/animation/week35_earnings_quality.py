"""
Week 35: Earnings Quality Radar / Spider Chart
================================================
Compares two hypothetical companies on five earnings-quality metrics:
  1. Accruals Ratio (lower is better -- inverted for display)
  2. Cash Conversion
  3. Revenue Growth Consistency
  4. Margin Stability
  5. Debt Coverage

Output: week35_earnings_quality.png
"""

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# Metrics and data (scores out of 10)
# -------------------------------------------------------------------
categories = [
    "Accruals Ratio\n(lower = better)",
    "Cash\nConversion",
    "Revenue Growth\nConsistency",
    "Margin\nStability",
    "Debt\nCoverage",
]

# Company A: high-quality earner
company_a_scores = [9, 9, 8, 8.5, 7]
# Company B: lower-quality earner
company_b_scores = [4, 5, 6, 4.5, 3]

num_vars = len(categories)

# -------------------------------------------------------------------
# Radar chart setup
# -------------------------------------------------------------------
# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Close the polygon
company_a_scores += company_a_scores[:1]
company_b_scores += company_b_scores[:1]
angles += angles[:1]

# -------------------------------------------------------------------
# Plotting
# -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Company A
ax.plot(angles, company_a_scores, color="#4CAF50", linewidth=2.5,
        linestyle="-", label="Company A (High Quality)")
ax.fill(angles, company_a_scores, color="#4CAF50", alpha=0.15)

# Company B
ax.plot(angles, company_b_scores, color="#F44336", linewidth=2.5,
        linestyle="--", label="Company B (Low Quality)")
ax.fill(angles, company_b_scores, color="#F44336", alpha=0.10)

# Category labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9, fontweight="bold")

# Radial grid
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=8, color="grey")
ax.set_rlabel_position(30)

# Grid styling
ax.spines["polar"].set_color("#ccc")
ax.grid(color="#ddd", linewidth=0.8)

# Legend
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), fontsize=10,
          framealpha=0.9)

# Title
ax.set_title("Earnings Quality Scorecard",
             fontsize=14, fontweight="bold", pad=25)

# Interpretation note
fig.text(0.5, 0.02,
         "Scores out of 10. Larger area = higher overall earnings quality.",
         ha="center", fontsize=9, color="#555",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF9C4", alpha=0.8))

plt.tight_layout()
plt.savefig("B:/chanmainvest/tutorial/course/animation/week35_earnings_quality.png",
            dpi=150, bbox_inches="tight")
plt.close()
print("Saved week35_earnings_quality.png")
