"""
Ni-Ti-Nb SMA — literature-based quantitative re-analysis

Primary quantitative source:
Kusagawa, Nakamura & Asada (2001), Fig. 9(a-c).

Comparative literature source:
Tobushi et al. (1992).

The two material systems are deliberately kept separate.
P2 is used only for literature context and is never merged
into the P1 Ni-Ti-Nb dataset.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# ============================================================
# 1. PROJECT PATHS
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_DIR / "data"
FIG_DIR = PROJECT_DIR / "figures"
RESULT_DIR = PROJECT_DIR / "results"

DATA_FILE = DATA_DIR / "sma_extracted_data.csv"
P2_FILE = DATA_DIR / "paper2_literature_findings.csv"

FINAL_PDF = PROJECT_DIR / "SMA_Project_Final_Results.pdf"


# ============================================================
# 2. COMMON FOOTER FOR ALL GRAPHS
# ============================================================

FOOTER_TEXT = (
    "Ni-Ti-Nb SMA literature-based quantitative re-analysis | "
    "P1 Fig. 9(a-c) primary dataset"
)


# ============================================================
# 3. EXPECTED FIGURES
# ============================================================

EXPECTED_FIGURES = [
    (
        "prestrain_vs_recovered_strain.png",
        "Prestrain vs recovered strain",
        "Core relationship"
    ),

    (
        "prestrain_vs_residual_strain.png",
        "Prestrain vs residual strain",
        "Core relationship"
    ),

    (
        "temperature_recovered_grouped.png",
        "Recovered strain vs temperature",
        "Within-prestrain temperature effect"
    ),

    (
        "temperature_residual_grouped.png",
        "Residual strain vs temperature",
        "Within-prestrain temperature effect"
    ),

    (
        "recovery_fraction_vs_prestrain.png",
        "Recovery fraction vs prestrain",
        "Project-defined derived metric"
    ),

    (
        "recovery_residual_pareto.png",
        "Recovery-residual trade-off and Pareto frontier",
        "Multi-objective analysis"
    ),

    (
        "normalized_temperature_sensitivity.png",
        "Normalized temperature sensitivity",
        "Within-group comparison"
    ),

    (
        "recovered_vs_residual_strain.png",
        "Recovered vs residual strain",
        "Trade-off relationship"
    ),
]


# ============================================================
# 4. PREPARE DIRECTORIES
# ============================================================

def prepare_directories():

    FIG_DIR.mkdir(exist_ok=True)
    RESULT_DIR.mkdir(exist_ok=True)

    # Remove old PNG files that are not part of the current project
    expected_names = {
        name for name, _, _ in EXPECTED_FIGURES
    }

    for path in FIG_DIR.glob("*.png"):

        if path.name not in expected_names:
            path.unlink()


# ============================================================
# 5. LOAD PRIMARY DATA
# ============================================================

def load_primary_data():

    df = pd.read_csv(DATA_FILE)

    required = {
        "source_paper_id",
        "source_figure",
        "prestrain_percent",
        "prestrain_temperature_k",
        "recovered_strain_percent",
        "residual_strain_percent"
    }

    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    if len(df) != 9:
        raise ValueError(
            f"Expected 9 primary observations; found {len(df)}"
        )

    if set(df["prestrain_percent"]) != {1, 3, 7}:
        raise ValueError(
            "Primary prestrain levels do not match the audited source subset."
        )

    if set(df["prestrain_temperature_k"]) != {253, 263, 273}:
        raise ValueError(
            "Primary temperatures do not match the audited source subset."
        )

    return df


# ============================================================
# 6. ADD DERIVED METRICS
# ============================================================

def add_derived_metrics(df):

    df = df.copy()

    df["total_observed_strain_percent"] = (
        df["recovered_strain_percent"]
        + df["residual_strain_percent"]
    )

    df["recovery_fraction_percent"] = (
        df["recovered_strain_percent"]
        / df["total_observed_strain_percent"]
        * 100
    )

    df["residual_fraction_percent"] = (
        df["residual_strain_percent"]
        / df["total_observed_strain_percent"]
        * 100
    )

    return df


# ============================================================
# 7. BUILD RESULTS
# ============================================================

def build_results(df, p2):

    # --------------------------------------------------------
    # Data quality
    # --------------------------------------------------------

    quality = pd.DataFrame({
        "missing_values": df.isna().sum(),
        "unique_values": df.nunique(),
    })

    quality.to_csv(
        RESULT_DIR / "data_quality.csv"
    )


    # --------------------------------------------------------
    # Data provenance
    # --------------------------------------------------------

    provenance = pd.DataFrame([

        [
            "primary_source",
            "P1",
            "Kusagawa, Nakamura & Asada (2001)",
            "Ni-Ti-Nb",
            "Fig. 9(a-c), journal p. 62 / PDF p. 6",
            "9 digitised observations"
        ],

        [
            "comparative_source",
            "P2",
            "Tobushi, Ohashi, Saida, Hori & Shirai (1992)",
            "Ti-55.3 wt% Ni",
            "Figs. 2-9 and experimental discussion",
            "Qualitative/contextual use only; not merged with P1"
        ],

    ],
        columns=[
            "source_role",
            "paper_id",
            "citation",
            "material_system",
            "source_location",
            "dataset_role"
        ]
    )

    provenance.to_csv(
        RESULT_DIR / "data_provenance.csv",
        index=False
    )


    # --------------------------------------------------------
    # Group statistics
    # --------------------------------------------------------

    group_stats = (

        df.groupby("prestrain_percent")

        .agg(
            recovered_mean=(
                "recovered_strain_percent",
                "mean"
            ),

            recovered_std=(
                "recovered_strain_percent",
                "std"
            ),

            residual_mean=(
                "residual_strain_percent",
                "mean"
            ),

            residual_std=(
                "residual_strain_percent",
                "std"
            ),

            recovery_fraction_mean=(
                "recovery_fraction_percent",
                "mean"
            ),

            recovery_fraction_std=(
                "recovery_fraction_percent",
                "std"
            ),

            observations=(
                "prestrain_temperature_k",
                "count"
            ),
        )

        .reset_index()
    )

    group_stats.to_csv(
        RESULT_DIR / "prestrain_group_statistics.csv",
        index=False
    )


    # --------------------------------------------------------
    # Correlation and regression analysis
    # --------------------------------------------------------

    pairs = [

        (
            "prestrain_percent",
            "recovered_strain_percent"
        ),

        (
            "prestrain_percent",
            "residual_strain_percent"
        ),

        (
            "prestrain_temperature_k",
            "recovered_strain_percent"
        ),

        (
            "prestrain_temperature_k",
            "residual_strain_percent"
        ),

        (
            "recovered_strain_percent",
            "residual_strain_percent"
        ),

    ]

    rows = []

    for x, y in pairs:

        tmp = df[[x, y]].dropna()

        r = tmp[x].corr(tmp[y])

        slope, intercept = np.polyfit(
            tmp[x],
            tmp[y],
            1
        )

        yhat = (
            slope * tmp[x]
            + intercept
        )

        ss_res = float(
            ((tmp[y] - yhat) ** 2).sum()
        )

        ss_tot = float(
            ((tmp[y] - tmp[y].mean()) ** 2).sum()
        )

        r2 = (
            1 - ss_res / ss_tot
            if ss_tot
            else np.nan
        )

        rows.append({

            "predictor": x,

            "response": y,

            "pearson_r": r,

            "slope": slope,

            "intercept": intercept,

            "R2": r2,

            "n": len(tmp),

            "interpretation":
                "descriptive only; not causal or predictive",
        })


    correlations = pd.DataFrame(rows)

    correlations.to_csv(
        RESULT_DIR / "correlation_regression_summary.csv",
        index=False
    )


    # --------------------------------------------------------
    # Temperature effects
    # --------------------------------------------------------

    temperature_rows = []

    for p, g in df.groupby("prestrain_percent"):

        g = g.sort_values(
            "prestrain_temperature_k"
        )

        slope_rec, _ = np.polyfit(
            g["prestrain_temperature_k"],
            g["recovered_strain_percent"],
            1
        )

        slope_res, _ = np.polyfit(
            g["prestrain_temperature_k"],
            g["residual_strain_percent"],
            1
        )

        rec_253 = g.loc[
            g["prestrain_temperature_k"].eq(253),
            "recovered_strain_percent"
        ].iloc[0]

        rec_273 = g.loc[
            g["prestrain_temperature_k"].eq(273),
            "recovered_strain_percent"
        ].iloc[0]

        temperature_rows.append({

            "prestrain_percent": p,

            "recovered_slope_percent_per_K":
                slope_rec,

            "residual_slope_percent_per_K":
                slope_res,

            "recovered_change_253_to_273_percent":
                (rec_273 / rec_253 - 1) * 100,

            "recovered_drop_253_to_273_absolute_percent_points":
                rec_253 - rec_273,
        })


    temperature_effects = pd.DataFrame(
        temperature_rows
    )

    temperature_effects.to_csv(
        RESULT_DIR / "within_prestrain_temperature_effects.csv",
        index=False
    )


    # --------------------------------------------------------
    # Exploratory interaction model
    # --------------------------------------------------------

    df["prestrain_centered"] = (
        df["prestrain_percent"]
        - df["prestrain_percent"].mean()
    )

    df["temperature_centered"] = (
        df["prestrain_temperature_k"]
        - df["prestrain_temperature_k"].mean()
    )

    df["interaction"] = (
        df["prestrain_centered"]
        * df["temperature_centered"]
    )

    X = np.column_stack([

        np.ones(len(df)),

        df["prestrain_centered"],

        df["temperature_centered"],

        df["interaction"],

    ])


    interaction_rows = []

    for response in [
        "recovered_strain_percent",
        "residual_strain_percent"
    ]:

        y = df[response].to_numpy()

        beta, *_ = np.linalg.lstsq(
            X,
            y,
            rcond=None
        )

        yhat = X @ beta

        ss_res = float(
            np.sum((y - yhat) ** 2)
        )

        ss_tot = float(
            np.sum((y - y.mean()) ** 2)
        )

        interaction_rows.append({

            "response": response,

            "intercept_at_mean_conditions":
                beta[0],

            "prestrain_effect_per_percent":
                beta[1],

            "temperature_effect_per_K":
                beta[2],

            "prestrain_temperature_interaction":
                beta[3],

            "R2_descriptive":
                1 - ss_res / ss_tot
                if ss_tot
                else np.nan,

            "n": len(df),

            "status":
                "exploratory descriptive fit only; "
                "not validated for prediction",
        })


    pd.DataFrame(
        interaction_rows
    ).to_csv(
        RESULT_DIR / "exploratory_interaction_model.csv",
        index=False
    )


    # --------------------------------------------------------
    # Pareto analysis
    # --------------------------------------------------------

    pareto_flags = []

    for i, row in df.iterrows():

        dominated = False

        for j, other in df.iterrows():

            if i == j:
                continue

            better_or_equal_recovery = (
                other["recovered_strain_percent"]
                >= row["recovered_strain_percent"]
            )

            better_or_equal_residual = (
                other["residual_strain_percent"]
                <= row["residual_strain_percent"]
            )

            one_strict = (

                other["recovered_strain_percent"]
                > row["recovered_strain_percent"]

                or

                other["residual_strain_percent"]
                < row["residual_strain_percent"]
            )

            if (
                better_or_equal_recovery
                and better_or_equal_residual
                and one_strict
            ):

                dominated = True
                break

        pareto_flags.append(
            not dominated
        )


    df["pareto_optimal_recovery_residual"] = (
        pareto_flags
    )


    pareto_table = df[[

        "source_figure",

        "prestrain_percent",

        "prestrain_temperature_k",

        "recovered_strain_percent",

        "residual_strain_percent",

        "recovery_fraction_percent",

        "pareto_optimal_recovery_residual",

    ]]


    pareto_table.to_csv(
        RESULT_DIR / "pareto_frontier.csv",
        index=False
    )


    # --------------------------------------------------------
    # Recovery-residual trade-off
    # --------------------------------------------------------

    tradeoff = df[[

        "source_figure",

        "prestrain_percent",

        "prestrain_temperature_k",

        "recovered_strain_percent",

        "residual_strain_percent",

        "recovery_fraction_percent",

        "residual_fraction_percent",

    ]].sort_values([

        "prestrain_percent",

        "prestrain_temperature_k"

    ])


    tradeoff.to_csv(
        RESULT_DIR / "recovery_residual_tradeoff.csv",
        index=False
    )


    # --------------------------------------------------------
    # Save analyzed dataset
    # --------------------------------------------------------

    df.to_csv(
        RESULT_DIR / "analyzed_sma_dataset.csv",
        index=False
    )


    # --------------------------------------------------------
    # Literature source summary
    # --------------------------------------------------------

    summary = pd.DataFrame([

        [
            "P1 primary quantitative dataset",
            len(df),
            "Ni-Ti-Nb",
            "Fig. 9(a-c)"
        ],

        [
            "P2 comparative literature findings",
            len(p2),
            "Ti-55.3 wt% Ni",
            "Figs. 2-9 / text"
        ],

    ],
        columns=[
            "module",
            "records",
            "material_system",
            "source_scope"
        ]
    )


    summary.to_csv(
        RESULT_DIR / "literature_source_summary.csv",
        index=False
    )


    # --------------------------------------------------------
    # Project summary
    # --------------------------------------------------------

    project_summary = pd.DataFrame([

        [
            "Primary observations",
            9,
            "P1 Fig. 9(a-c)"
        ],

        [
            "Primary material",
            "Ni-Ti-Nb SMA",
            "P1"
        ],

        [
            "Primary source figure",
            "Fig. 9(a-c)",
            "P1 journal p. 62 / PDF p. 6"
        ],

        [
            "Prestrain vs recovered strain Pearson r",
            round(
                correlations.loc[0, "pearson_r"],
                4
            ),
            "Descriptive correlation"
        ],

        [
            "Prestrain vs recovered strain R2",
            round(
                correlations.loc[0, "R2"],
                4
            ),
            "Descriptive regression only"
        ],

        [
            "Prestrain vs residual strain Pearson r",
            round(
                correlations.loc[1, "pearson_r"],
                4
            ),
            "Descriptive correlation"
        ],

        [
            "Prestrain vs residual strain R2",
            round(
                correlations.loc[1, "R2"],
                4
            ),
            "Descriptive regression only"
        ],

        [
            "Temperature vs recovered strain pooled Pearson r",
            round(
                correlations.loc[2, "pearson_r"],
                4
            ),
            "Pooled; within-group trend is more informative"
        ],

        [
            "Temperature vs residual strain pooled Pearson r",
            round(
                correlations.loc[3, "pearson_r"],
                4
            ),
            "Pooled; insufficient for a general law"
        ],

        [
            "Recovered vs residual strain Pearson r",
            round(
                correlations.loc[4, "pearson_r"],
                4
            ),
            "Descriptive association only"
        ],

        [
            "Mean recovery fraction at 1% prestrain",
            round(
                group_stats.loc[
                    group_stats.prestrain_percent.eq(1),
                    "recovery_fraction_mean"
                ].iloc[0],
                2
            ),
            "Project-defined metric"
        ],

        [
            "Mean recovery fraction at 3% prestrain",
            round(
                group_stats.loc[
                    group_stats.prestrain_percent.eq(3),
                    "recovery_fraction_mean"
                ].iloc[0],
                2
            ),
            "Project-defined metric"
        ],

        [
            "Mean recovery fraction at 7% prestrain",
            round(
                group_stats.loc[
                    group_stats.prestrain_percent.eq(7),
                    "recovery_fraction_mean"
                ].iloc[0],
                2
            ),
            "Project-defined metric"
        ],

        [
            "Pareto-optimal observations",
            int(sum(pareto_flags)),
            "Higher recovery and lower residual strain"
        ],

        [
            "P2 role",
            "Comparative recovery-stress literature",
            "TiNi paper kept separate from P1 dataset"
        ],

        [
            "Project status",
            "Frozen after v5 terminology cleanup",
            "Final scientific terminology and presentation cleanup"
        ],

    ],
        columns=[
            "metric",
            "value",
            "source_or_note"
        ]
    )


    project_summary.to_csv(
        RESULT_DIR / "project_summary.csv",
        index=False
    )


    return (
        group_stats,
        correlations,
        temperature_effects,
        pareto_table,
        df
    )


# ============================================================
# 8. SAVE FIGURE WITH COMMON FOOTER
# ============================================================

def save_figure(fig, filename):

    # Leave space at the bottom for the footer
    fig.tight_layout(
        rect=[0, 0.06, 1, 1]
    )

    # --------------------------------------------------------
    # COMMON FOOTER
    # --------------------------------------------------------
    #
    # This same footer is automatically added to EVERY PNG.
    #

    fig.text(
        0.04,
        0.025,
        FOOTER_TEXT,
        fontsize=8.5,
        ha="left",
        va="bottom",
        family="sans-serif"
    )


    # Save the PNG
    fig.savefig(
        FIG_DIR / filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)


# ============================================================
# 9. GENERATE ALL FIGURES
# ============================================================

def generate_figures(df, group_stats):


    # ========================================================
    # FIGURE 1
    # Prestrain vs Recovered Strain
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )

    for temp, g in df.groupby(
        "prestrain_temperature_k"
    ):

        ax.scatter(
            g["prestrain_percent"],
            g["recovered_strain_percent"],
            s=65,
            label=f"{temp} K"
        )


    ax.set_xlabel(
        "Prestrain (%)"
    )

    ax.set_ylabel(
        "Recovered strain (%)"
    )

    ax.set_title(
        "Prestrain vs Recovered Strain"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend(
        title="Prestraining temperature"
    )


    save_figure(
        fig,
        "prestrain_vs_recovered_strain.png"
    )


    # ========================================================
    # FIGURE 2
    # Prestrain vs Residual Strain
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )

    for temp, g in df.groupby(
        "prestrain_temperature_k"
    ):

        ax.scatter(
            g["prestrain_percent"],
            g["residual_strain_percent"],
            s=65,
            label=f"{temp} K"
        )


    ax.set_xlabel(
        "Prestrain (%)"
    )

    ax.set_ylabel(
        "Residual strain (%)"
    )

    ax.set_title(
        "Prestrain vs Residual Strain"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend(
        title="Prestraining temperature"
    )


    save_figure(
        fig,
        "prestrain_vs_residual_strain.png"
    )


    # ========================================================
    # FIGURE 3
    # Recovered Strain vs Temperature
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )

    for p, g in df.groupby(
        "prestrain_percent"
    ):

        g = g.sort_values(
            "prestrain_temperature_k"
        )

        ax.plot(
            g["prestrain_temperature_k"],
            g["recovered_strain_percent"],
            marker="o",
            linewidth=1.8,
            markersize=6,
            label=f"{p}% prestrain"
        )


    ax.set_xlabel(
        "Prestraining temperature (K)"
    )

    ax.set_ylabel(
        "Recovered strain (%)"
    )

    ax.set_title(
        "Recovered Strain vs Prestraining Temperature"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend(
        title="Prestrain"
    )


    save_figure(
        fig,
        "temperature_recovered_grouped.png"
    )


    # ========================================================
    # FIGURE 4
    # Residual Strain vs Temperature
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )

    for p, g in df.groupby(
        "prestrain_percent"
    ):

        g = g.sort_values(
            "prestrain_temperature_k"
        )

        ax.plot(
            g["prestrain_temperature_k"],
            g["residual_strain_percent"],
            marker="o",
            linewidth=1.8,
            markersize=6,
            label=f"{p}% prestrain"
        )


    ax.set_xlabel(
        "Prestraining temperature (K)"
    )

    ax.set_ylabel(
        "Residual strain (%)"
    )

    ax.set_title(
        "Residual Strain vs Prestraining Temperature"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend(
        title="Prestrain"
    )


    save_figure(
        fig,
        "temperature_residual_grouped.png"
    )


    # ========================================================
    # FIGURE 5
    # Recovery Fraction vs Prestrain
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )

    x = group_stats[
        "prestrain_percent"
    ].astype(str)

    bars = ax.bar(
        x,
        group_stats[
            "recovery_fraction_mean"
        ]
    )


    ax.set_xlabel(
        "Prestrain (%)"
    )

    ax.set_ylabel(
        "Mean recovered fraction of observed deformation (%)"
    )

    ax.set_title(
        "Recovered Fraction of Observed Deformation vs Prestrain"
    )

    ax.set_ylim(
        0,
        100
    )

    ax.grid(
        True,
        axis="y",
        alpha=0.25
    )


    for bar, value in zip(
        bars,
        group_stats[
            "recovery_fraction_mean"
        ]
    ):

        ax.text(
            bar.get_x()
            + bar.get_width() / 2,

            value + 1.2,

            f"{value:.1f}%",

            ha="center",

            va="bottom",

            fontsize=9
        )


    save_figure(
        fig,
        "recovery_fraction_vs_prestrain.png"
    )


    # ========================================================
    # FIGURE 6
    # Recovery-Residual Trade-off
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(9.6, 6.2)
    )


    offsets = {

        (1, 253): (-50, 12),

        (1, 263): (-52, -24),

        (1, 273): (10, 12),

        (3, 253): (10, 12),

        (3, 263): (10, -24),

        (3, 273): (10, 12),

        (7, 253): (10, 12),

        (7, 263): (10, -24),

        (7, 273): (10, 12),

    }


    for _, r in df.iterrows():

        key = (
            int(r["prestrain_percent"]),
            int(r["prestrain_temperature_k"])
        )

        is_pareto = bool(
            r["pareto_optimal_recovery_residual"]
        )


        ax.scatter(

            r["residual_strain_percent"],

            r["recovered_strain_percent"],

            marker="D"
            if is_pareto
            else "o",

            s=72,

            zorder=3
        )


        dx, dy = offsets[key]


        ax.annotate(

            f"{key[0]}% / {key[1]} K",

            (
                r["residual_strain_percent"],
                r["recovered_strain_percent"]
            ),

            xytext=(dx, dy),

            textcoords="offset points",

            fontsize=8,

            arrowprops=dict(
                arrowstyle="-",
                lw=0.7,
                alpha=0.5
            ),

            bbox=dict(
                boxstyle="round,pad=0.18",
                fc="white",
                ec="0.75",
                alpha=0.9
            ),

            zorder=4
        )


    pareto_df = (

        df[
            df[
                "pareto_optimal_recovery_residual"
            ]
        ]

        .sort_values(
            "residual_strain_percent"
        )
    )


    ax.plot(

        pareto_df[
            "residual_strain_percent"
        ],

        pareto_df[
            "recovered_strain_percent"
        ],

        linestyle="--",

        linewidth=1.5,

        label="Pareto frontier",

        zorder=2
    )


    ax.set_xlabel(
        "Residual strain (%) — lower is better"
    )

    ax.set_ylabel(
        "Recovered strain (%) — higher is better"
    )

    ax.set_title(
        "Recovery–Residual Trade-off and Pareto Frontier"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend()


    ax.text(

        0.02,
        0.02,

        "Pareto-optimal = no other tested condition "
        "has both higher recovery and lower residual strain.",

        transform=ax.transAxes,

        fontsize=8.3,

        va="bottom",

        bbox=dict(
            boxstyle="round,pad=0.3",
            fc="white",
            ec="0.75",
            alpha=0.92
        )
    )


    save_figure(
        fig,
        "recovery_residual_pareto.png"
    )


    # ========================================================
    # FIGURE 7
    # Normalized Temperature Sensitivity
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(7.6, 5.2)
    )


    for p, g in df.groupby(
        "prestrain_percent"
    ):

        g = g.sort_values(
            "prestrain_temperature_k"
        )

        baseline = (
            g[
                "recovered_strain_percent"
            ].iloc[0]
        )

        normalized = (
            g[
                "recovered_strain_percent"
            ]
            / baseline
            * 100
        )


        ax.plot(

            g[
                "prestrain_temperature_k"
            ],

            normalized,

            marker="o",

            linewidth=1.8,

            markersize=6,

            label=f"{p}% prestrain"
        )


    ax.axhline(
        100,
        linestyle="--",
        linewidth=1
    )


    ax.set_xlabel(
        "Prestraining temperature (K)"
    )

    ax.set_ylabel(
        "Recovered strain relative to 253 K (%)"
    )

    ax.set_title(
        "Within-Group Temperature Sensitivity of Recovery"
    )

    ax.grid(
        True,
        alpha=0.25
    )

    ax.legend(
        title="Prestrain"
    )


    save_figure(
        fig,
        "normalized_temperature_sensitivity.png"
    )


    # ========================================================
    # FIGURE 8
    # Recovered vs Residual Strain
    # ========================================================

    fig, ax = plt.subplots(
        figsize=(9.6, 6.2)
    )


    offsets_rr = {

        (1, 253): (-54, 12),

        (1, 263): (-54, -24),

        (1, 273): (10, 12),

        (3, 253): (10, 12),

        (3, 263): (10, -24),

        (3, 273): (10, 12),

        (7, 253): (10, 12),

        (7, 263): (10, -24),

        (7, 273): (10, 12),

    }


    for _, r in df.iterrows():

        key = (

            int(r["prestrain_percent"]),

            int(r["prestrain_temperature_k"])

        )


        ax.scatter(

            r["recovered_strain_percent"],

            r["residual_strain_percent"],

            s=72,

            zorder=3
        )


        dx, dy = offsets_rr[key]


        ax.annotate(

            f"{key[0]}% / {key[1]} K",

            (

                r["recovered_strain_percent"],

                r["residual_strain_percent"]

            ),

            xytext=(dx, dy),

            textcoords="offset points",

            fontsize=8,

            arrowprops=dict(

                arrowstyle="-",

                lw=0.7,

                alpha=0.5

            ),

            bbox=dict(

                boxstyle="round,pad=0.18",

                fc="white",

                ec="0.75",

                alpha=0.9

            ),

            zorder=4
        )


    ax.set_xlabel(
        "Recovered strain (%)"
    )

    ax.set_ylabel(
        "Residual strain (%)"
    )

    ax.set_title(
        "Recovered Strain vs Residual Strain"
    )

    ax.grid(
        True,
        alpha=0.25
    )


    save_figure(
        fig,
        "recovered_vs_residual_strain.png"
    )


# ============================================================
# 10. FIGURE INVENTORY
# ============================================================

def build_figure_inventory():

    inventory = pd.DataFrame(

        EXPECTED_FIGURES,

        columns=[
            "filename",
            "title",
            "purpose"
        ]
    )


    inventory.to_csv(

        RESULT_DIR / "figure_inventory.csv",

        index=False
    )


    return inventory


# ============================================================
# 11. BUILD FINAL PDF
# ============================================================

def build_final_pdf(inventory):

    with PdfPages(FINAL_PDF) as pdf:

        for _, item in inventory.iterrows():

            image_path = (
                FIG_DIR
                / item["filename"]
            )

            image = plt.imread(
                image_path
            )


            fig = plt.figure(
                figsize=(11.69, 8.27)
            )


            ax = fig.add_axes(
                [0.04, 0.09, 0.92, 0.86]
            )


            ax.imshow(
                image
            )

            ax.axis("off")


            # The footer is already present inside
            # the PNG, so we do NOT add another footer here.


            pdf.savefig(
                fig
            )

            plt.close(fig)


# ============================================================
# 12. PRINT CLEAN SUMMARY
# ============================================================

def print_clean_summary(
    df,
    p2,
    group_stats,
    correlations,
    temperature_effects,
    pareto_table
):

    print(
        "=" * 72
    )

    print(
        "NI-TI-NB SMA RESEARCH ANALYSIS"
    )

    print(
        "=" * 72
    )


    print(
        "\nDATASET"
    )

    print(
        "-" * 72
    )

    print(
        f"Primary observations             : {len(df)}"
    )

    print(
        "Prestrain levels                 : 1%, 3%, 7%"
    )

    print(
        "Prestraining temperatures        : 253 K, 263 K, 273 K"
    )

    print(
        f"Comparative P2 literature findings          : {len(p2)}"
    )


    print(
        "\nRECOVERED STRAIN"
    )

    print(
        "-" * 72
    )


    for _, r in group_stats.iterrows():

        print(

            f"Mean recovered strain at "
            f"{int(r['prestrain_percent'])}% prestrain : "
            f"{r['recovered_mean']:.3f}%"

        )


    print(

        f"Prestrain vs recovered strain r  : "
        f"{correlations.loc[0, 'pearson_r']:.4f}"

    )


    print(

        f"Descriptive R2                   : "
        f"{correlations.loc[0, 'R2']:.4f}"

    )


    print(
        "\nRESIDUAL STRAIN"
    )

    print(
        "-" * 72
    )


    for _, r in group_stats.iterrows():

        print(

            f"Mean residual strain at "
            f"{int(r['prestrain_percent'])}% prestrain   : "
            f"{r['residual_mean']:.3f}%"

        )


    print(

        f"Prestrain vs residual strain r   : "
        f"{correlations.loc[1, 'pearson_r']:.4f}"

    )


    print(

        f"Descriptive R2                   : "
        f"{correlations.loc[1, 'R2']:.4f}"

    )


    print(
        "\nTEMPERATURE EFFECT"
    )

    print(
        "-" * 72
    )


    for _, r in temperature_effects.iterrows():

        print(

            f"{int(r['prestrain_percent'])}% prestrain, "
            f"253 to 273 K recovery change : "
            f"{r['recovered_change_253_to_273_percent']:.1f}%"

        )


    print(

        f"Pooled temperature vs recovery r : "
        f"{correlations.loc[2, 'pearson_r']:.4f}"

    )


    print(
        "Interpretation                   : "
        "within-prestrain trends are more informative"
    )


    print(
        "\nRECOVERY FRACTION"
    )

    print(
        "-" * 72
    )


    for _, r in group_stats.iterrows():

        print(

            f"Mean recovery fraction at "
            f"{int(r['prestrain_percent'])}% prestrain : "
            f"{r['recovery_fraction_mean']:.2f}%"

        )


    print(

        f"Observed recovery-fraction range : "
        f"{df['recovery_fraction_percent'].min():.2f}% "
        f"to "
        f"{df['recovery_fraction_percent'].max():.2f}%"

    )


    print(
        "\nRECOVERY-RESIDUAL TRADE-OFF"
    )

    print(
        "-" * 72
    )


    print(

        f"Recovered vs residual strain r   : "
        f"{correlations.loc[4, 'pearson_r']:.4f}"

    )


    print(

        f"Pareto-optimal tested conditions : "
        f"{int(pareto_table['pareto_optimal_recovery_residual'].sum())}"

    )


    print(
        "Interpretation                   : "
        "no universal optimum is claimed"
    )


    print(
        "\n" + "=" * 72
    )

    print(
        "Analysis completed successfully."
    )

    print(
        "=" * 72
    )


# ============================================================
# 13. MAIN PROGRAM
# ============================================================

def main():

    prepare_directories()

    df = load_primary_data()

    df = add_derived_metrics(
        df
    )

    p2 = pd.read_csv(
        P2_FILE
    )


    (
        group_stats,
        correlations,
        temperature_effects,
        pareto_table,
        analyzed
    ) = build_results(
        df,
        p2
    )


    generate_figures(
        analyzed,
        group_stats
    )


    inventory = build_figure_inventory()


    build_final_pdf(
        inventory
    )


    print_clean_summary(

        analyzed,

        p2,

        group_stats,

        correlations,

        temperature_effects,

        pareto_table

    )


# ============================================================
# 14. RUN
# ============================================================

if __name__ == "__main__":

    main()