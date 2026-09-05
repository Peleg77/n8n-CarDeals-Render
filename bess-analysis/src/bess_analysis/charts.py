"""Stage output charts: hour x month heatmap, daily spread distribution,
concentration curve, and the capex x spread-multiplier IRR sensitivity heatmap.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def plot_hour_month_heatmap(matrix: pd.DataFrame, title: str, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(matrix.to_numpy(), aspect="auto", origin="lower", cmap="viridis")
    ax.set_yticks(range(24))
    ax.set_yticklabels(range(24))
    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTH_LABELS)
    ax.set_xlabel("Month")
    ax.set_ylabel("Hour of day")
    ax.set_title(title)
    fig.colorbar(im, ax=ax, label="Mean price (NIS/MWh)")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_spread_distribution(daily: pd.DataFrame, out_path: Path, col: str = "spread_4h") -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(daily[col].dropna(), bins=50, color="#3B6E8F", edgecolor="white")
    ax.axvline(daily[col].median(), color="#D9534F", linestyle="--", label=f"median={daily[col].median():.0f}")
    ax.set_xlabel("Daily spread_4h (NIS/MWh)")
    ax.set_ylabel("Number of days")
    ax.set_title("Distribution of daily spread_4h")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_concentration_curve(daily: pd.DataFrame, out_path: Path, col: str = "spread_4h") -> None:
    s = daily[col].clip(lower=0).sort_values(ascending=False).reset_index(drop=True)
    cum_pct = s.cumsum() / s.sum() * 100
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(range(1, len(s) + 1), cum_pct, color="#3B6E8F")
    for n in (10, 20, 50):
        if n <= len(s):
            ax.axvline(n, color="gray", linestyle=":", linewidth=1)
            ax.annotate(f"{cum_pct.iloc[n-1]:.0f}% @ day {n}", (n, cum_pct.iloc[n - 1]), fontsize=8)
    ax.set_xlabel("Day rank (best to worst)")
    ax.set_ylabel("Cumulative % of annual arbitrage value")
    ax.set_title("Revenue concentration across days")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_irr_sensitivity_heatmap(grid: pd.DataFrame, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    data = grid.to_numpy() * 100
    im = ax.imshow(data, aspect="auto", cmap="RdYlGn")
    ax.set_xticks(range(len(grid.columns)))
    ax.set_xticklabels([f"{c:.2f}x" for c in grid.columns])
    ax.set_yticks(range(len(grid.index)))
    ax.set_yticklabels([f"{int(i)}" for i in grid.index])
    ax.set_xlabel("Spread multiplier")
    ax.set_ylabel("Capex (NIS/kWh)")
    ax.set_title("Unlevered IRR (%) sensitivity")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data[i, j]
            label = f"{val:.1f}" if np.isfinite(val) else "n/a"
            ax.text(j, i, label, ha="center", va="center", fontsize=8)
    fig.colorbar(im, ax=ax, label="IRR (%)")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
