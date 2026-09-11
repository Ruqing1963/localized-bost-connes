#!/usr/bin/env python3
"""
Generate the figures for the paper and README.

Outputs PDF (for LaTeX inclusion) and PNG (for the README) into ../figures/.
"""

from __future__ import annotations

import math
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bcloc.core import primes_upto, sophie_germain_upto  # noqa: E402

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIG, exist_ok=True)

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 9,
        "axes.linewidth": 0.6,
        "figure.dpi": 150,
        "savefig.bbox": "tight",
    }
)

INK = "#1b1b1b"
ACCENT = "#8c2f39"
COOL = "#2f4f8c"
GREY = "#9a9a9a"


def save(fig, name: str) -> None:
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIG, f"{name}.{ext}"))
    plt.close(fig)
    print(f"wrote figures/{name}.pdf, figures/{name}.png")


# ------------------------------------------------- fig 1: the two phase types ----

def fig_closed_vs_open() -> None:
    """
    Remark 5.3: same critical temperature, opposite behaviour at it.
    Bost-Connes: zeta has a pole at beta_c = 1, critical point in the
    high-temperature phase. Brun-summable S with beta_c = 1: zeta is finite at
    beta_c, so the low-temperature phase is closed.
    """
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7), sharey=True)

    # zeta with an Euler-Maclaurin tail so that the pole at beta = 1 is visible
    N = 2000
    ns = np.arange(1, N)
    b = np.linspace(1.02, 2.2, 400)
    zeta = np.array(
        [np.sum(ns.astype(float) ** -x) + N ** (1 - x) / (x - 1) for x in b]
    )

    ax = axes[0]
    ax.plot(b, zeta, color=COOL, lw=1.4)
    ax.axvline(1, color=ACCENT, lw=1.0, ls="--")
    ax.fill_betweenx([0, 12], 0.4, 1, color=GREY, alpha=0.18)
    ax.set_xlim(0.4, 2.2)
    ax.set_ylim(0, 12)
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\zeta_S(\beta)$")
    ax.set_title(r"all primes: $\zeta$ has a pole at $\beta_c=1$", fontsize=9)
    ax.text(0.62, 9.0, "unique\nKMS state", ha="center", fontsize=8, color=INK)
    ax.text(1.62, 9.0, r"type $\mathrm{I}_\infty$", ha="center", fontsize=8, color=INK)
    ax.plot([1], [11.6], marker="o", ms=4, color=ACCENT, clip_on=False)
    ax.annotate(
        r"$\zeta(\beta_c)=\infty$",
        xy=(1.02, 10.4),
        fontsize=8,
        color=ACCENT,
    )

    # a Brun-summable set with beta_c = 1: primes p with p_k ~ k log^2 k
    ks = np.arange(2, 60000)
    pk = ks * np.log(ks) ** 2
    ax = axes[1]
    zs = np.array([np.sum(pk ** -x) for x in np.linspace(1.0, 2.2, 400)])
    bb = np.linspace(1.0, 2.2, 400)
    ax.plot(bb, zs, color=COOL, lw=1.4)
    ax.axvline(1, color=ACCENT, lw=1.0, ls="--")
    ax.fill_betweenx([0, 12], 0.4, 1, color=GREY, alpha=0.18)
    ax.set_xlim(0.4, 2.2)
    ax.set_xlabel(r"$\beta$")
    ax.set_title(r"Brun-summable, $\beta_c=1$: $\zeta_S(\beta_c)<\infty$", fontsize=9)
    ax.plot([1], [zs[0]], marker="o", ms=4, color=ACCENT)
    ax.annotate(
        r"$\zeta_S(\beta_c)<\infty$" "\n" r"phase is closed",
        xy=(1.05, zs[0] + 1.2),
        fontsize=8,
        color=ACCENT,
    )
    ax.text(0.62, 9.0, r"$\zeta_S=\infty$", ha="center", fontsize=8, color=INK)

    for ax in axes:
        ax.tick_params(length=3, width=0.6)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)

    save(fig, "fig1_closed_vs_open_phase")


# --------------------------------------------- fig 2: obstruction group chain ----

def fig_cascade() -> None:
    """Proposition 4.15: three transitions, with residual symmetry groups."""
    b2, b1 = 0.35, 0.70
    fig, ax = plt.subplots(figsize=(7.2, 2.2))

    segments = [
        (0.02, b2, r"$\Xi_\beta=\{1\}$", r"$G_S$", "#e8eef7"),
        (b2, b1, r"$\{1,\chi_5\}$", r"$\ker\chi_5$", "#cfdcef"),
        (b1, 1.0, r"$\{1,\chi_3,\chi_5,\chi_3\chi_5\}$", r"$\ker\chi_3\cap\ker\chi_5$", "#a9c1e3"),
        (1.0, 1.35, r"$\widehat{G_S}$", r"$\{1\}$", "#7f9fd0"),
    ]
    for lo, hi, xi, res, col in segments:
        ax.axvspan(lo, hi, color=col, lw=0)
        mid = (lo + hi) / 2
        ax.text(mid, 0.68, xi, ha="center", va="center", fontsize=8.5)
        ax.text(mid, 0.30, res, ha="center", va="center", fontsize=8.5, color=ACCENT)

    for x in (b2, b1, 1.0):
        ax.axvline(x, color=INK, lw=0.9)
    ax.set_xticks([b2, b1, 1.0])
    ax.set_xticklabels([r"$\beta_2$", r"$\beta_1$", r"$\beta_c=1$"], fontsize=9)

    ax.text(0.02, 0.92, r"obstruction group $\Xi_\beta$", fontsize=8, color=INK)
    ax.text(0.02, 0.06, r"residual symmetry $\Xi_\beta^\perp$", fontsize=8, color=ACCENT)
    ax.set_xlim(0.02, 1.35)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel(r"inverse temperature $\beta$", labelpad=14)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_title("A cascade of three phase transitions (Proposition 4.15)",
                 fontsize=9, pad=10)
    save(fig, "fig2_cascade")


# --------------------------------------- fig 3: existence versus abundance ----

def fig_density_vs_measure() -> None:
    """
    Section 4.2: density of Theta_S needs one detecting prime; uniqueness needs
    a divergent weighted sum over them.
    """
    fig, ax = plt.subplots(figsize=(7.2, 2.9))

    bound = 4000
    P1 = [p for p in primes_upto(bound) if p % 3 == 1]
    R = [11, 257, 65537 % bound if False else 1031]  # illustrative sparse set

    ax.scatter(P1, [1] * len(P1), s=3, color=COOL, label=r"$P_1$: $\ell\equiv1\ (3)$, undetected")
    ax.scatter(R, [1] * len(R), s=42, marker="v", color=ACCENT, zorder=5,
               label=r"$R$: detects $\chi$, but $\beta$-summable")
    ax.set_yticks([])
    ax.set_xscale("log")
    ax.set_xlim(2, bound)
    ax.set_xlabel(r"$\ell$ (log scale)")
    ax.legend(frameon=False, fontsize=8, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.32))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)

    ax.annotate(
        "density of $\\Theta_S$  $\\Leftrightarrow$  $R\\neq\\emptyset$   (existence)\n"
        "uniqueness  $\\Leftrightarrow$  $\\sum_{\\ell\\in R}\\ell^{-\\beta}=\\infty$   (abundance)",
        xy=(0.5, -0.62),
        xycoords="axes fraction",
        ha="center",
        fontsize=9,
    )
    save(fig, "fig3_density_vs_measure")


# ------------------------------------------------ fig 4: Sophie Germain data ----

def fig_sophie_germain() -> None:
    """Theorem 5.5(1): the Brun-type bound and the convergence of sum 1/p."""
    bound = 400_000
    SG = sophie_germain_upto(bound)
    xs = np.array(SG, dtype=float)
    counts = np.arange(1, len(SG) + 1)

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7))

    ax = axes[0]
    ax.plot(xs, counts, color=COOL, lw=1.2, label=r"$\pi_{\mathcal{SG}}(x)$")
    C2 = 0.6601618158
    ref = 2 * C2 * xs / np.log(xs) ** 2
    ax.plot(xs, ref, color=ACCENT, lw=1.0, ls="--", label=r"$2C_2\,x/\log^2 x$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("count")
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Sophie Germain counting function", fontsize=9)

    ax = axes[1]
    partial = np.cumsum(1.0 / xs)
    ax.plot(xs, partial, color=COOL, lw=1.2)
    ax.set_xscale("log")
    ax.set_xlabel("$x$ (log scale)")
    ax.set_ylabel(r"$\sum_{p \leq x,\ p \in SG} 1/p$")
    ax.set_title(r"Brun-summable: the sum converges", fontsize=9)
    ax.annotate(
        f"partial sum at $x={bound:,}$: {partial[-1]:.4f}",
        xy=(0.05, 0.12),
        xycoords="axes fraction",
        fontsize=8,
        color=INK,
    )

    for ax in axes:
        ax.tick_params(length=3, width=0.6)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    save(fig, "fig4_sophie_germain")


# -------------------------------------------- fig 5: the structure of G_S ----

def fig_exact_sequence() -> None:
    """Proposition 2.4: the two structures absent over Q."""
    fig, ax = plt.subplots(figsize=(7.2, 2.2))
    ax.axis("off")

    boxes = [
        (0.04, r"$1$", "#ffffff", None),
        (0.20, r"$U_S/\overline{\mathcal{O}^{\times}_{K,+}}$", "#e8eef7", "units"),
        (0.48, r"$G_S$", "#cfdcef", "symmetry group"),
        (0.76, r"$\mathrm{Cl}^{+}_S$", "#f3dcdf", "narrow class group"),
        (0.95, r"$1$", "#ffffff", None),
    ]
    for x, lab, col, sub in boxes:
        ax.text(
            x, 0.58, lab, ha="center", va="center", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.45", fc=col, ec=INK, lw=0.6),
        )
        if sub:
            ax.text(x, 0.38, sub, ha="center", va="center", fontsize=7.5,
                    color=GREY, style="italic")

    for x0, x1 in ((0.07, 0.12), (0.30, 0.40), (0.56, 0.66), (0.87, 0.92)):
        ax.annotate("", xy=(x1, 0.58), xytext=(x0, 0.58),
                    arrowprops=dict(arrowstyle="->", lw=0.8, color=INK))

    ax.text(0.20, 0.14, "aids uniqueness\n(shrinks $G_S$)",
            ha="center", fontsize=7.5, color=COOL)
    ax.text(0.76, 0.14, "unramified obstruction\nwhen $h^{+}_K>1$",
            ha="center", fontsize=7.5, color=ACCENT)
    ax.text(0.5, 0.94,
            r"over $\mathbb{Q}$ both ends are trivial: $G_S=\widehat{\mathbb{Z}}_S^{\times}$",
            ha="center", fontsize=8, color=INK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save(fig, "fig5_exact_sequence")


def main() -> int:
    fig_closed_vs_open()
    fig_cascade()
    fig_density_vs_measure()
    fig_sophie_germain()
    fig_exact_sequence()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
