"""
Week 20 - Earnings Quality Visualization
==========================================
Bar chart comparing Reported EPS vs Operating EPS vs Free Cash Flow
per share for a hypothetical company across quarters, showing how
these metrics can diverge and signal earnings quality issues.
Output: week20_earnings_quality.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define quarterly data for a hypothetical company
# ---------------------------------------------------------------------------
quarters = ['Q1\n2024', 'Q2\n2024', 'Q3\n2024', 'Q4\n2024',
            'Q1\n2025', 'Q2\n2025', 'Q3\n2025', 'Q4\n2025']

# Reported EPS (GAAP) - includes one-time items, can be inflated
reported_eps = [1.20, 1.35, 1.50, 1.80, 1.95, 2.10, 2.30, 2.50]

# Operating EPS (Non-GAAP) - excludes one-time items, more stable
operating_eps = [1.10, 1.25, 1.30, 1.40, 1.50, 1.55, 1.60, 1.65]

# Free Cash Flow per share - the real cash generated
fcf_per_share = [1.00, 1.15, 1.05, 0.90, 0.85, 0.70, 0.55, 0.40]

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9),
                                gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Earnings Quality: When Reported EPS Diverges from Cash Flow',
             fontsize=15, fontweight='bold', y=0.97)

x = np.arange(len(quarters))
width = 0.25

# -- Top panel: bar chart --
bars1 = ax1.bar(x - width, reported_eps, width, label='Reported EPS (GAAP)',
                color='#2196F3', edgecolor='white', linewidth=1)
bars2 = ax1.bar(x, operating_eps, width, label='Operating EPS (Non-GAAP)',
                color='#FF9800', edgecolor='white', linewidth=1)
bars3 = ax1.bar(x + width, fcf_per_share, width,
                label='Free Cash Flow / Share',
                color='#4CAF50', edgecolor='white', linewidth=1)

# Add value labels on top of bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height + 0.03,
                 f'${height:.2f}', ha='center', va='bottom', fontsize=7.5)

# Highlight the divergence zone
ax1.axvspan(4.5, 7.5, alpha=0.08, color='red')
ax1.text(6, 2.55, 'Warning Zone:\nEPS rising but\ncash flow falling',
         ha='center', fontsize=10, color='red', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffebee',
                   edgecolor='red', alpha=0.8))

# Arrow showing divergence
ax1.annotate('', xy=(7, 2.50), xytext=(7, 0.40),
             arrowprops=dict(arrowstyle='<->', color='red',
                             lw=2, ls='--'))
ax1.text(7.35, 1.45, 'Growing\ngap', fontsize=9, color='red',
         fontweight='bold')

ax1.set_ylabel('$ per Share', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(quarters, fontsize=9)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_title('Hypothetical Company XYZ: Three Measures of Earnings',
              fontsize=12)
ax1.grid(True, axis='y', alpha=0.25)
ax1.set_ylim(0, 2.8)

# -- Bottom panel: FCF/EPS ratio (quality score) --
quality_ratio = np.array(fcf_per_share) / np.array(reported_eps) * 100

colors = ['#4CAF50' if q >= 70 else '#FF9800' if q >= 50 else '#F44336'
          for q in quality_ratio]

ax2.bar(x, quality_ratio, 0.5, color=colors, edgecolor='white', linewidth=1)
ax2.axhline(y=70, color='green', linestyle='--', linewidth=1, alpha=0.7,
            label='Good quality (>70%)')
ax2.axhline(y=50, color='red', linestyle='--', linewidth=1, alpha=0.7,
            label='Poor quality (<50%)')

for i, q in enumerate(quality_ratio):
    ax2.text(i, q + 2, f'{q:.0f}%', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color=colors[i])

ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('FCF / Reported EPS (%)', fontsize=10)
ax2.set_title('Earnings Quality Ratio (FCF as % of Reported EPS)', fontsize=12)
ax2.set_xticks(x)
ax2.set_xticklabels(quarters, fontsize=9)
ax2.legend(loc='upper right', fontsize=9)
ax2.set_ylim(0, 110)
ax2.grid(True, axis='y', alpha=0.25)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week20_earnings_quality.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
