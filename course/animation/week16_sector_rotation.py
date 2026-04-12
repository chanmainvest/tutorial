"""
Week 16 - Sector Rotation Diagram
===================================
Circular sector rotation diagram with business cycle phases
and corresponding sectors that outperform in each phase.
Output: week16_sector_rotation.png
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ---------------------------------------------------------------------------
# 1. Define business cycle phases and their favoured sectors
# ---------------------------------------------------------------------------
phases = [
    {
        'name': 'Early\nExpansion',
        'sectors': ['Technology', 'Consumer\nDiscretionary', 'Industrials'],
        'color': '#4CAF50',   # green
        'desc': 'GDP accelerating\nLow rates',
    },
    {
        'name': 'Mid\nExpansion',
        'sectors': ['Technology', 'Industrials', 'Materials'],
        'color': '#8BC34A',   # light green
        'desc': 'Strong growth\nRising earnings',
    },
    {
        'name': 'Late\nExpansion',
        'sectors': ['Energy', 'Materials', 'Financials'],
        'color': '#FF9800',   # orange
        'desc': 'Peak growth\nRising inflation',
    },
    {
        'name': 'Early\nRecession',
        'sectors': ['Healthcare', 'Consumer\nStaples', 'Utilities'],
        'color': '#F44336',   # red
        'desc': 'GDP declining\nFalling earnings',
    },
    {
        'name': 'Late\nRecession',
        'sectors': ['Utilities', 'Consumer\nStaples', 'Financials'],
        'color': '#9C27B0',   # purple
        'desc': 'Rates cut\nBottoming out',
    },
    {
        'name': 'Recovery',
        'sectors': ['Financials', 'Consumer\nDiscretionary', 'Real Estate'],
        'color': '#2196F3',   # blue
        'desc': 'GDP recovering\nEasy policy',
    },
]

n = len(phases)

# ---------------------------------------------------------------------------
# 2. Create the circular diagram
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'projection': 'polar'})

# Each phase occupies an equal slice
theta_width = 2 * np.pi / n

for i, phase in enumerate(phases):
    theta_start = i * theta_width - np.pi / 2  # start from top
    theta_mid   = theta_start + theta_width / 2

    # Draw the outer sector wedge
    bars = ax.bar(theta_mid, 1.0, width=theta_width * 0.95,
                  bottom=0.35, color=phase['color'], alpha=0.35,
                  edgecolor=phase['color'], linewidth=2)

    # Phase name in the middle ring
    ax.text(theta_mid, 0.72, phase['name'],
            ha='center', va='center', fontsize=12,
            fontweight='bold', color=phase['color'],
            multialignment='center')

    # Sector labels in the outer ring
    sector_text = '\n'.join(phase['sectors'])
    ax.text(theta_mid, 1.15, sector_text,
            ha='center', va='center', fontsize=8,
            color='#333333', multialignment='center',
            bbox=dict(boxstyle='round,pad=0.3',
                      facecolor=phase['color'], alpha=0.15))

    # Description near outer edge
    ax.text(theta_mid, 1.55, phase['desc'],
            ha='center', va='center', fontsize=7,
            color='#666666', fontstyle='italic',
            multialignment='center')

# Draw clockwise arrow to show cycle direction
arrow_angles = np.linspace(-np.pi / 2, -np.pi / 2 + 2 * np.pi * 0.85, 100)
arrow_r = np.full_like(arrow_angles, 0.5)
ax.plot(arrow_angles, arrow_r, color='#555555', linewidth=2, alpha=0.5)
# Arrowhead
ax.annotate('', xy=(arrow_angles[-1] + 0.15, 0.5),
            xytext=(arrow_angles[-1], 0.5),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=2))

# Centre label
ax.text(0, 0.05, 'Business\nCycle', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#333333',
        multialignment='center')

# Clean up polar axes
ax.set_ylim(0, 1.75)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['polar'].set_visible(False)

fig.suptitle('Sector Rotation Through the Business Cycle',
             fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week16_sector_rotation.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
