# Final SMA Project Audit — Final v5

## Status

**READY TO FREEZE after the v5 terminology and presentation cleanup.** The scientific content is retained, while the execution and presentation problems visible in the supplied PDFs are repaired.

## Scientific audit

- Primary quantitative source: Kusagawa, Nakamura & Asada (2001), Fig. 9(a-c).
- Primary dataset: 9 figure-extracted observations covering 1%, 3% and 7% prestrain at 253 K, 263 K and 273 K.
- P2 is Tobushi et al. (1992), a TiNi recovery-stress literature source; its observations are kept separate and are not merged with P1.
- Recovered fraction of observed deformation is explicitly labelled as a project-defined comparison metric and is not presented as a standardised SMA material property.
- Correlations, regressions and the interaction model are descriptive/exploratory only.
- Pareto analysis is a non-dominated comparison of the nine tested conditions, not a universal optimum claim.

## Repairs in v4

1. Refactored the Python workflow into functions with a standard `main()` entry point.
2. Added deterministic cleanup of stale PNG files: only the eight files in the current figure inventory are retained.
3. Replaced wide DataFrame terminal printing with a narrow, sectioned research summary.
4. Kept the eight intended figures and removed the standalone duplicate trade-off figure from the generated set.
5. Regenerated the final visual PDF from the eight current PNGs, exactly one figure per page.
6. Preserved the existing nine-row primary dataset and all numerical conclusions.
7. Kept provenance, data dictionary, paper-use matrix and defence notes.

## Current figure set

1. `prestrain_vs_recovered_strain.png`
2. `prestrain_vs_residual_strain.png`
3. `temperature_recovered_grouped.png`
4. `temperature_residual_grouped.png`
5. `recovery_fraction_vs_prestrain.png`
6. `recovery_residual_pareto.png`
7. `normalized_temperature_sensitivity.png`
8. `recovered_vs_residual_strain.png`

## Reproducibility

Run from the project root:

```text
python src/SMA_quantitative_analysis.py
```

The command should complete without errors and regenerate the eight PNG figures, result CSV files and `SMA_Project_Final_Results.pdf`.

## Presentation boundary

The project is a literature-based computational re-analysis, not an original laboratory experiment. The strongest defensible claim is that the extracted Ni-Ti-Nb observations show a prestrain-associated increase in recovered strain accompanied by increasing residual strain, with a consistent within-group decrease in recovered strain as prestraining temperature rises from 253 K to 273 K.
