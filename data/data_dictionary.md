# SMA dataset dictionary

## Primary file: `sma_extracted_data.csv`

This is the only file containing the nine numerical observations used for the main Ni-Ti-Nb calculations.

| Column | Meaning |
|---|---|
| `source_paper_id` | P1 = Kusagawa et al. (2001) |
| `source_paper` | Short citation for the source paper |
| `source_figure` | Exact source figure panel: Fig. 9(a), 9(b), or 9(c) |
| `journal_page` | Printed journal page containing the figure |
| `pdf_page` | Page number in the supplied PDF |
| `material_system` | Material represented by the observation |
| `prestrain_percent` | Maximum/prestrain level represented in the figure |
| `prestrain_temperature_k` | Temperature during prestraining |
| `recovered_strain_percent` | Recovered strain read from the source figure |
| `residual_strain_percent` | Residual strain read from the source figure |
| `extraction_note` | States that the value is a digitised approximation, not a direct laboratory measurement |

## Important

The nine primary observations are **not original measurements**. They are figure-extracted literature observations from P1.

The second paper (P2) is intentionally stored separately in `paper2_literature_findings.csv`. It is a TiNi study, not Ni-Ti-Nb, so its numerical observations are **not mixed into the primary dataset**.

## Derived files

The Python script creates additional columns such as recovery fraction and residual fraction. Those are calculated from the primary source-derived observations.
