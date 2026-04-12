"""
Week 21 - DCF Model Waterfall Chart
=====================================
Waterfall chart showing DCF components:
  Year 1-5 cash flows, terminal value, minus debt, equals equity value per share.
Output: week21_dcf_model.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define DCF components (in $ millions, except per-share)
# ---------------------------------------------------------------------------
components = {
    'Year 1 FCF':       150,
    'Year 2 FCF':       170,
    'Year 3 FCF':       195,
    'Year 4 FCF':       220,
    'Year 5 FCF':       250,
    'Terminal Value':    1800,
    'Net Debt':         -600,   # subtracted (negative)
}

shares_outstanding = 100  # millions

# ---------------------------------------------------------------------------
# 2. Compute waterfall positions
# ---------------------------------------------------------------------------
labels = list(components.keys()) + ['Equity Value']
values = list(components.values())

# Running totals for waterfall
running = []
cumulative = 0
bottoms = []

for v in values:
    if v >= 0:
        bottoms.append(cumulative)
        cumulative += v
    else:
        cumulative += v
        bottoms.append(cumulative)
    running.append(cumulative)

# Final total bar
equity_value = cumulative
labels_full = labels
values_full = values + [equity_value]
bottoms_full = bottoms + [0]  # total bar starts from 0

# Colours: positive = green, negative = red, total = blue
colors = []
for v in values:
    colors.append('#4CAF50' if v >= 0 else '#F44336')
colors.append('#2196F3')  # total bar

# ---------------------------------------------------------------------------
# 3. Plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(13, 7))

x = np.arange(len(labels_full))
bar_width = 0.6

# Draw bars
bars = ax.bar(x, [abs(v) for v in values_full], bar_width,
              bottom=bottoms_full, color=colors, edgecolor='white',
              linewidth=1.5, zorder=3)

# Connector lines between bars (except before total)
for i in range(len(values)):
    if i < len(values) - 1:
        ax.plot([x[i] + bar_width / 2, x[i + 1] - bar_width / 2],
                [running[i], running[i]],
                color='gray', linewidth=1, linestyle='--', alpha=0.5)
    elif i == len(values) - 1:
        # Connect last component to total
        ax.plot([x[i] + bar_width / 2, x[i + 1] - bar_width / 2],
                [running[i], running[i]],
                color='gray', linewidth=1, linestyle='--', alpha=0.5)

# Value labels on bars
for i, (v, b) in enumerate(zip(values_full, bottoms_full)):
    y_pos = b + abs(v) / 2
    prefix = '+' if v > 0 and i < len(values) else ''
    if i == len(values):  # total
        prefix = ''
    label_text = f'{prefix}${abs(v):,.0f}M'
    ax.text(i, y_pos, label_text, ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

# Per-share value annotation on the total bar
per_share = equity_value / shares_outstanding
ax.annotate(f'= ${per_share:.2f} / share\n({shares_outstanding}M shares)',
            xy=(len(labels_full) - 1, equity_value),
            xytext=(len(labels_full) - 1.5, equity_value + 200),
            fontsize=11, fontweight='bold', color='#2196F3',
            arrowprops=dict(arrowstyle='->', color='#2196F3', lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E3F2FD',
                      edgecolor='#2196F3'))

# Annotations for sections
# PV of Cash Flows bracket
ax.annotate('', xy=(0, -80), xytext=(4, -80),
            arrowprops=dict(arrowstyle='<->', color='#4CAF50', lw=1.5))
ax.text(2, -130, 'PV of Free Cash Flows\n(Years 1-5)',
        ha='center', fontsize=9, color='#4CAF50', fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(labels_full, fontsize=10, rotation=15, ha='right')
ax.set_ylabel('Enterprise Value ($ Millions)', fontsize=12)
ax.set_title('DCF Valuation: Waterfall from Cash Flows to Equity Value',
             fontsize=15, fontweight='bold')
ax.grid(True, axis='y', alpha=0.2)
ax.set_xlim(-0.5, len(labels_full) - 0.3)

# Add a legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#4CAF50', label='Cash Flow (positive)'),
    Patch(facecolor='#F44336', label='Net Debt (subtracted)'),
    Patch(facecolor='#2196F3', label='Equity Value (total)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

plt.tight_layout()

# ---------------------------------------------------------------------------
# 4. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week21_dcf_model.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
