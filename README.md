# Ni-Ti-Nb SMA Literature
## Nature of the research contribution

This project is a **literature-based quantitative re-analysis**, not an original laboratory experiment.

The primary quantitative dataset consists of nine observations digitised from Fig. 9(a-c) of the P1 Ni-Ti-Nb study. The research contribution is the reproducible extraction and analysis workflow, quantitative comparison of prestrain and temperature effects, recovery–residual trade-off analysis, Pareto framing, synthesis with a separate TiNi recovery-stress paper, and design of a follow-up factorial experiment.

No claim is made that the original experiments were performed by the project author.

## The two papers

### P1 — quantitative source
Kusagawa, M., Nakamura, T., & Asada, Y. (2001), *Fundamental Deformation and Recovery Behaviors of Ni-Ti-Nb Shape Memory Alloy*.

Used for the nine numerical observations digitised from **Fig. 9(a-c)**.

### P2 — comparative recovery-stress source
Tobushi, H., Ohashi, Y., Saida, H., Hori, T., & Shirai, S. (1992), *Recovery Stress and Recovery Strain of TiNi Shape Memory Alloy (Cyclic Properties under Constant Residual Strain and Constant Maximum Stress)*.

Used as a separate literature-context benchmark for recovery stress, residual strain, heating temperature and thermal cycling.

**P2 is not merged into the P1 Ni-Ti-Nb dataset because it is a TiNi material system.**

## Primary dataset

`data/sma_extracted_data.csv` contains exactly 9 observations and explicitly identifies:

- source paper;
- source figure;
- journal page;
- PDF page;
- prestrain;
- prestraining temperature;
- recovered strain;
- residual strain;
- extraction status.

The values are figure-extracted approximations, not original laboratory measurements.

## Main analysis

The Python workflow demonstrates:

- source-aware data extraction;
- data validation;
- grouped statistics;
- Pearson correlation;
- descriptive regression;
- within-prestrain temperature sensitivity;
- project-defined recovered fraction of observed deformation;
- recovery/residual trade-off analysis;
- Pareto-frontier analysis;
- exploratory prestrain × temperature interaction;
- literature synthesis using a second primary paper;
- hypothesis generation;
- factorial experimental design.

## Main quantitative results

- Prestrain vs recovered strain: **r = 0.9920, R² = 0.9840**.
- Prestrain vs residual strain: **r = 0.9039, R² = 0.8171**.
- Temperature vs recovered strain, pooled: **r = -0.1145, R² = 0.0131**.
- Temperature vs residual strain, pooled: **r = 0.2964, R² = 0.0878**.
- Recovered vs residual strain: **r = 0.8473, R² = 0.7179**.
- Mean recovered fraction of observed deformation: **92.56% at 1%, 88.34% at 3%, 85.45% at 7% prestrain**.

## Important scientific boundary

Do not claim:

- original laboratory measurements;
- a universal optimum prestrain;
- a universal temperature law;
- a validated predictive model;
- a new alloy or constitutive law;
- that P2 TiNi data were statistically combined with P1 Ni-Ti-Nb data.

## Run

From the project root:

```text
python src/SMA_quantitative_analysis.py
```

Results are written to `results/` and figures to `figures/`.

## Best one-line CV description

> Quantitatively re-analysed published Ni-Ti-Nb SMA recovery data in Python, identifying a prestrain–recovery/residual-deformation trade-off and temperature-dependent recovery behaviour, and extended the analysis with recovery-stress literature synthesis and Pareto-based experimental design.

## Best interview description

> “I digitised a published Ni-Ti-Nb experimental figure, preserved exact source provenance for the nine observations, reproduced the main recovery trends quantitatively, identified a recovery–residual trade-off, used a separate TiNi recovery-stress study to broaden the engineering question, and designed a factorial experiment to test the resulting hypotheses.”

## Frozen figure set

The repaired version generates exactly **8 current figures**. Before generation, stale PNG files are removed unless they belong to the current figure inventory. See `results/figure_inventory.csv` and `report/FINAL_AUDIT.md`. `SMA_Project_Final_Results.pdf` contains exactly one page for each current figure.

The nine P2 records are literature findings used for contextual synthesis; they are not nine additional experimental observations and are not part of the quantitative Ni-Ti-Nb dataset.”


