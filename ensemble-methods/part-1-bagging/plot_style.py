"""Shared plot style for the figures in Part 1 of the ensemble methods series.

Figures are designed at 700 px, the width of a Medium column, and saved at
twice that resolution so they stay sharp on high density screens.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

# Colors used across the whole series
INK = "#0A1A5C"
BLUE = "#1340D8"
RED = "#C9372C"
TEAL = "#0E8C7E"
GOLD = "#F2B200"
LIGHT = "#B4BDD6"
FRAME = "#D5D9E3"
SHADE = "#EEF1FB"

WIDTH_PX = 700
DPI = 144

# Open Sans ships with the repository, so the figures look the same on any machine
FONT_DIR = Path(__file__).resolve().parents[2] / "fonts"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))


def apply_style():
    """Set the fonts, sizes and colors used in the article."""
    plt.rcParams.update({
        "font.family": "Open Sans",
        "font.size": 15,
        "axes.labelsize": 15,
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "legend.fontsize": 14,
        "lines.linewidth": 3.5,
        "axes.linewidth": 1.4,
        "xtick.major.width": 1.4,
        "ytick.major.width": 1.4,
        "xtick.major.size": 6,
        "ytick.major.size": 6,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.titlecolor": INK,
        "axes.grid": True,
        "grid.color": "#E3E6EE",
        "grid.linewidth": 1.0,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "savefig.transparent": False,
        "figure.facecolor": "white"
    })


def new_figure(height_px, **kwargs):
    """Create a figure that is 700 px wide, with the given height in px."""
    return plt.subplots(figsize=(WIDTH_PX / 72, height_px / 72), **kwargs)


def save(fig, path):
    """Save a figure at 1400 px wide with a white background."""
    fig.savefig(path, dpi=DPI, facecolor="white")
