"""
Week 19 - Capital Structure Visualization
===========================================
Stacked bar chart showing Debt vs Equity for different leverage
ratios, with a WACC (Weighted Average Cost of Capital) curve overlay.
Output: week19_capital_structure.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# 1. Define capital structure scenarios
# ---------------------------------------------------------------------------
# Debt-to-total-capital ratios
debt_ratios = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
equity_ratios = 100 - debt_ratios

labels = [f'{d}%' for d in debt_ratios]

# Cost of equity rises with leverage (Modigliani-Miller with taxes)
cost_equity_base = 8.0  # unlevered cost of equity
cost_debt_base   = 4.0  # base cost of debt
tax_rate         = 0.25

# Cost of equity increases as leverage rises
cost_equity = cost_equity_base + 0.06 * debt_ratios + 0.002 * debt_ratios**1.5

# Cost of debt increases at higher leverage (credit risk)
cost_debt = cost_debt_base + 0.001 * debt_ratios**1.3

# WACC = E/V * Ke + D/V * Kd * (1 - T)
wacc = (equity_ratios / 100 * cost_equity +
        debt_ratios / 100 * cost_debt * (1 - tax_rate))

# Find optimal (minimum WACC)
optimal_idx = np.argmin(wacc)

# ---------------------------------------------------------------------------
# 2. Plot
# ---------------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(12, 7))

x = np.arange(len(debt_ratios))
bar_width = 0.6

# Stacked bars: equity on bottom, debt on top
bars_eq = ax1.bar(x, equity_ratios, bar_width,
                  label='Equity', color='#2196F3', alpha=0.85,
                  edgecolor='white', linewidth=1.2)
bars_dt = ax1.bar(x, debt_ratios, bar_width, bottom=equity_ratios,
                  label='Debt', color='#FF5722', alpha=0.85,
                  edgecolor='white', linewidth=1.2)

# Add percentage labels inside bars
for i, (eq, dt) in enumerate(zip(equity_ratios, debt_ratios)):
    if eq > 8:
        ax1.text(i, eq / 2, f'{eq}%', ha='center', va='center',
                 fontsize=9, fontweight='bold', color='white')
    if dt > 8:
        ax1.text(i, eq + dt / 2, f'{dt}%', ha='center', va='center',
                 fontsize=9, fontweight='bold', color='white')

ax1.set_xlabel('Debt / Total Capital', fontsize=12)
ax1.set_ylabel('Capital Structure (%)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=10)
ax1.set_ylim(0, 115)
ax1.legend(loc='upper left', fontsize=11)

# -- WACC curve on secondary axis --
ax2 = ax1.twinx()
ax2.plot(x, wacc, color='#4CAF50', linewidth=3, marker='o',
         markersize=8, label='WACC', zorder=5)
ax2.plot(x, cost_equity, color='#2196F3', linewidth=1.5,
         linestyle='--', marker='s', markersize=5,
         label='Cost of Equity', alpha=0.7)
ax2.plot(x, cost_debt * (1 - tax_rate), color='#FF5722', linewidth=1.5,
         linestyle='--', marker='^', markersize=5,
         label='After-Tax Cost of Debt', alpha=0.7)

# Highlight optimal capital structure
ax2.scatter(optimal_idx, wacc[optimal_idx], s=250, color='gold',
            edgecolors='black', linewidths=2, zorder=6)
ax2.annotate(f'Optimal WACC\n{wacc[optimal_idx]:.1f}%\n'
             f'(D/C = {debt_ratios[optimal_idx]}%)',
             xy=(optimal_idx, wacc[optimal_idx]),
             xytext=(optimal_idx + 1.5, wacc[optimal_idx] - 1.5),
             fontsize=10, fontweight='bold', color='#4CAF50',
             arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=2),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#e8f5e9'))

ax2.set_ylabel('Cost of Capital (%)', fontsize=12, color='#4CAF50')
ax2.tick_params(axis='y', labelcolor='#4CAF50')
ax2.set_ylim(2, 22)
ax2.legend(loc='upper right', fontsize=10)

ax1.set_title('Capital Structure: Debt vs Equity & WACC',
              fontsize=15, fontweight='bold', pad=15)
ax1.grid(True, axis='y', alpha=0.2)

plt.tight_layout()

# ---------------------------------------------------------------------------
# 3. Save
# ---------------------------------------------------------------------------
output_path = os.path.join(os.path.dirname(__file__),
                           'week19_capital_structure.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {output_path}")
