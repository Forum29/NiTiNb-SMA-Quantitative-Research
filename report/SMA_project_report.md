# Quantitative Literature Re-analysis of Prestrain–Temperature–Recovery Behaviour in Ni-Ti-Nb Shape Memory Alloy

## Project status

**FINAL / FROZEN VERSION — third-year B.Tech research-project level**

This project is a reproducible literature-based computational study. It does **not** claim original laboratory measurements or a new alloy law.

The project deliberately uses two papers in different roles:

- **P1 — primary quantitative source:** Kusagawa, Nakamura & Asada (2001), *Fundamental Deformation and Recovery Behaviors of Ni-Ti-Nb Shape Memory Alloy*. The nine numerical observations used for the main analysis are digitised from **Fig. 9(a–c), journal p. 62 / supplied PDF p. 6**.
- **P2 — comparative recovery-stress source:** Tobushi, Ohashi, Saida, Hori & Shirai (1992), *Recovery Stress and Recovery Strain of TiNi Shape Memory Alloy (Cyclic Properties under Constant Residual Strain and Constant Maximum Stress)*. This paper is used to establish the importance of recovery stress, residual strain and thermal cycling. Its TiNi numerical observations are **not mixed into the Ni-Ti-Nb dataset**.

That separation is intentional because P1 and P2 are different material systems.

---

## 1. Research problem

For a shape memory alloy, maximum recovered strain is not automatically the same as best engineering performance. Increasing prestrain can increase the amount of recoverable deformation while also increasing residual deformation. In constrained applications, recovery stress is another important performance metric.

The project therefore asks:

> **Within the conditions represented by the extracted Ni-Ti-Nb literature data, how do prestrain and prestraining temperature influence recovered strain, residual strain and a project-defined recovery-fraction indicator?**

A second, literature-driven question is:

> **Why should recovery stress and residual strain be considered alongside recovery strain when evaluating SMA performance?**

P2 is used to motivate this second question rather than to create a mixed-material statistical model.

---

## 2. Source papers and exactly how they are used

### P1 — primary quantitative source

**Kusagawa, M., Nakamura, T., & Asada, Y. (2001).** *Fundamental Deformation and Recovery Behaviors of Ni-Ti-Nb Shape Memory Alloy*. JSME International Journal, Series A, 44(1), 57–63.

The paper's Fig. 9 contains recovered-strain and residual-strain curves for **1%, 3% and 7% prestrain** at **253 K, 263 K and 273 K**. The project digitises the plotted points from these three panels.

P1 is therefore the source of the nine rows in `data/sma_extracted_data.csv`.

### P2 — comparative recovery-stress source

**Tobushi, H., Ohashi, Y., Saida, H., Hori, T., & Shirai, S. (1992).** *Recovery Stress and Recovery Strain of TiNi Shape Memory Alloy (Cyclic Properties under Constant Residual Strain and Constant Maximum Stress)*. JSME International Journal, Series I, 35(1), 84–90.

P2 studies TiNi wire and examines recovery stress, recovery strain, residual strain, heating temperature and thermal-cycle effects. It reports, among other findings, that recovery stress under thermal cycling decreases as residual strain increases and that recovery-stress behaviour changes with heating temperature and repeated cycling.

P2 is stored in `data/paper2_literature_findings.csv` as a **traceable literature-context table**. No P2 numerical point is inserted into the P1 Ni-Ti-Nb dataset.

---

## 3. Data provenance

### Primary quantitative dataset

- **Observations:** 9
- **Material:** Ni-Ti-Nb SMA
- **Prestrain:** 1%, 3%, 7%
- **Prestraining temperature:** 253 K, 263 K, 273 K
- **Responses:** recovered strain and residual strain
- **Source:** P1, Fig. 9(a–c)
- **Status:** figure-extracted literature observations

The values are approximate readings from plotted markers. They are not claimed to have the precision of the original experimental measurements.

### Why the second paper is not mixed into the main CSV

P2 concerns Ti-55.3 wt% Ni TiNi wire, whereas P1 concerns Ni-Ti-Nb SMA. Combining the two directly would confound material composition, processing history and experimental conditions. Keeping them separate is scientifically stronger than forcing a larger but invalid dataset.

---

## 4. Primary dataset

| Source figure | Prestrain | Temperature (K) | Recovered strain (%) | Residual strain (%) |
|---|---:|---:|---:|---:|
| Fig. 9(a) | 1% | 253 | 0.50 | 0.05 |
| Fig. 9(a) | 1% | 263 | 0.42 | 0.02 |
| Fig. 9(a) | 1% | 273 | 0.21 | 0.02 |
| Fig. 9(b) | 3% | 253 | 2.20 | 0.17 |
| Fig. 9(b) | 3% | 263 | 2.05 | 0.19 |
| Fig. 9(b) | 3% | 273 | 1.67 | 0.40 |
| Fig. 9(c) | 7% | 253 | 5.50 | 0.55 |
| Fig. 9(c) | 7% | 263 | 5.20 | 0.85 |
| Fig. 9(c) | 7% | 273 | 4.65 | 1.20 |

---

## 5. Computational workflow

The Python script performs the following reproducible steps:

1. Loads and validates the nine primary observations.
2. Preserves source figure and page information.
3. Checks missing values and expected factor levels.
4. Calculates grouped means and standard deviations.
5. Calculates Pearson correlations and descriptive linear fits.
6. Calculates temperature slopes separately within each prestrain group.
7. Calculates a clearly labelled project-defined recovery-fraction indicator.
8. Builds a recovery–residual trade-off table.
9. Identifies the Pareto-optimal observations for the two objectives: higher recovery and lower residual strain.
10. Fits an exploratory centred prestrain × temperature interaction model.
11. Generates publication-style figures.
12. Preserves P2 as a separate literature-context dataset.
13. Writes machine-readable CSV outputs for every major result.

Run from the project root:

```text
python src/SMA_quantitative_analysis.py
```

The script requires Python with `pandas`, `numpy` and `matplotlib`.

---

## 6. Derived recovered fraction of observed deformation

For this project only:

**Recovered fraction of observed deformation (%) = recovered strain / (recovered strain + residual strain) × 100**

This is a **project-defined comparison metric**, not a standardised SMA material property or a conventional recovery-ratio definition. It is used only to compare the relative balance between recovered and residual deformation within the extracted dataset.

---

## 7. Result 1 — Prestrain vs recovered strain

Mean recovered strain:

| Prestrain | Mean recovered strain (%) | Standard deviation (%) |
|---:|---:|---:|
| 1% | 0.377 | 0.150 |
| 3% | 1.973 | 0.273 |
| 7% | 5.117 | 0.431 |

Pearson correlation:

**r = 0.9920**

Descriptive linear fit:

**Recovered strain = 0.7894 × prestrain − 0.4056**

**R² = 0.9840**

Within this extracted dataset, larger prestrain is very strongly associated with larger recovered strain.

This result is consistent with the behaviour shown in P1, but it should not be treated as a universal constitutive law.

---

## 8. Result 2 — Prestrain vs residual strain

Mean residual strain:

| Prestrain | Mean residual strain (%) | Standard deviation (%) |
|---:|---:|---:|
| 1% | 0.030 | 0.017 |
| 3% | 0.253 | 0.127 |
| 7% | 0.867 | 0.325 |

Pearson correlation:

**r = 0.9039**

Descriptive linear fit:

**Residual strain = 0.1414 × prestrain − 0.1352**

**R² = 0.8171**

The important engineering implication is that higher prestrain is accompanied by both greater recovered strain and greater residual strain.

---

## 9. Result 3 — Temperature effect within each prestrain group

The pooled temperature correlation with recovered strain is weak:

**r = −0.1145, R² = 0.0131**

However, the within-group behaviour is consistent:

| Prestrain | 253 K | 263 K | 273 K | Change 253→273 K |
|---:|---:|---:|---:|---:|
| 1% | 0.50 | 0.42 | 0.21 | −58.0% |
| 3% | 2.20 | 2.05 | 1.67 | −24.1% |
| 7% | 5.50 | 5.20 | 4.65 | −15.5% |

Thus, a pooled correlation alone does not describe the structure of the dataset well. Prestrain produces a much larger separation between groups, while temperature produces a within-group decrease in recovered strain.

For residual strain, the pooled temperature relationship is weak (**r = 0.2964, R² = 0.0878**), so no general temperature law is claimed.

---
## 10. Result 4 — Recovered fraction of observed deformation

The mean recovered fraction of observed deformation decreases with prestrain:

| Prestrain | Mean recovered fraction of observed deformation |
|---:|---:|
| 1% | 92.56% |
| 3% | 88.34% |
| 7% | 85.45% |

The 7% condition produces the highest absolute recovered strain, but it does not produce the highest project-defined recovered fraction of observed deformation.

This prevents the simplistic conclusion that the maximum prestrain is automatically the best condition.

---

## 11. Result 5 — Recovery/residual trade-off

Recovered strain and residual strain have:

**r = 0.8473**

**R² = 0.7179**

The extracted observations therefore show a positive association between the amount recovered and the amount left as residual deformation.

The project does not claim that one causes the other. Instead, this result motivates a multi-objective optimisation problem.

---

## 12. Result 6 — Pareto analysis

The project treats the two engineering objectives as:

- maximise recovered strain;
- minimise residual strain.

A condition is called **Pareto-optimal** when no other extracted observation simultaneously provides at least as much recovered strain and no more residual strain, with at least one strict improvement.

The extracted Pareto-optimal observations are:

| Prestrain | Temperature | Recovered strain | Residual strain | Recovered fraction of observed deformation |
|---:|---:|---:|---:|---:|
| 1% | 253 K | 0.50% | 0.05% | 90.91% |
| 1% | 263 K | 0.42% | 0.02% | 95.45% |
| 3% | 253 K | 2.20% | 0.17% | 92.83% |
| 7% | 253 K | 5.50% | 0.55% | 90.91% |

This is **not an optimum claim**. It is a transparent way to show that the choice of operating condition depends on the relative importance assigned to recovery and residual deformation.

---

## 13. Result 7 — Exploratory prestrain × temperature interaction

The script fits a centred interaction model containing:

- prestrain;
- temperature;
- prestrain × temperature.

The purpose is to make the interaction hypothesis explicit, not to build a predictive model.

Because there are only nine observations, the interaction fit is labelled **exploratory and not validated for prediction**.

The most defensible conclusion is that temperature should be investigated jointly with prestrain rather than treated as an isolated factor.

---

## 14. What P2 adds to the research argument

The second paper is not filler. It gives the project an important engineering extension.

P2 investigates TiNi recovery stress and recovery strain under thermal cycling. It reports:

- recovery-stress behaviour under repeated thermal cycles;
- dependence of recovery stress on residual strain;
- dependence on heating temperature;
- changes during early thermal cycles before behaviour becomes more stable;
- recovery-strain experiments at different initial strains;
- strain-temperature cycling at multiple temperatures and cycle counts.

One of its important conclusions is that recovery stress under thermal cycling decreases as residual strain increases. This supports the decision to treat residual deformation as an engineering performance variable rather than a minor side observation.

The material systems remain separate: P2 is **TiNi**, while the primary dataset is **Ni-Ti-Nb**.

---

## 15. Mechanistic interpretation

P1 reports that the stress–strain response changes around 323 K and discusses different dominant deformation mechanisms below and above this temperature. It also reports that the temperature at which recovery begins depends on maximum prestrain and prestraining temperature.

P1 further reports that residual strain is always observed in the deformation–recovery tests and that larger recovery strain can be obtained at larger prestrain and lower prestraining temperature.

P2 adds a complementary recovery-stress perspective: residual strain, heating temperature and thermal cycling affect recovery-stress behaviour.

The current project does **not** claim that the nine extracted points prove a specific microscopic mechanism. The mechanism remains a hypothesis requiring additional experiments and, ideally, DSC/XRD/EBSD/microscopy where available.

---

## 16. Research gap and proposed next experiment

The literature-derived analysis suggests that a useful future experiment should measure several responses simultaneously rather than optimise recovered strain alone.

### Factors

- Prestrain: for example 1–8%
- Prestraining temperature: for example 253–293 K
- Thermal-cycle number

### Responses

- recovered strain;
- residual strain;
- recovery stress under constrained conditions;
- recovery-start temperature;
- recovery-finish temperature;
- transformation temperatures;
- stress–strain response.

At least three independent specimens per condition would be preferable for estimating experimental scatter.

If laboratory equipment permits, DSC, XRD, EBSD or microscopy could be used to connect macroscopic recovery behaviour to transformation and microstructural changes.

---

## 17. Hypotheses for future validation

**H1:** Increasing prestrain increases recovered strain over the investigated range.

**H2:** Increasing prestrain increases residual strain.

**H3:** Lower prestraining temperature increases recovered strain under otherwise comparable conditions.

**H4:** The temperature effect depends on prestrain level.

**H5:** The prestrain–recovered-strain relationship may become nonlinear outside the extracted range.

**H6:** A useful engineering operating region should balance recovery strain and residual deformation rather than maximise recovery alone.

**H7:** Recovery stress and recovery strain may have different optimum conditions, so both should be measured in a future experiment.

---

## 18. Limitations

1. Only nine primary observations are available.
2. The observations were digitised from a published figure.
3. Digitisation introduces reading uncertainty.
4. Only 1%, 3% and 7% prestrain are represented in the primary dataset.
5. Only 253–273 K is represented in the extracted subset.
6. The extracted observations may not represent independent repeated experiments.
7. Correlation does not establish causation.
8. Descriptive regressions are not validated predictive models.
9. The recovery-fraction metric is project-defined.
10. The interaction model is exploratory because of the small sample size.
11. P2 is a different material system and is therefore not statistically merged with P1.
12. No original laboratory measurements were performed in this project.
13. Results should not be extrapolated beyond the represented experimental conditions.

---

## 19. What is genuinely student-level research work here?

The project demonstrates a complete research workflow rather than a collection of plots:

1. Identify a materials-science problem.
2. Read two primary research papers.
3. Decide which paper can support a quantitative dataset.
4. Digitise published experimental observations with explicit provenance.
5. Preserve the exact source figure and page for every observation.
6. Build a reproducible Python pipeline.
7. Quantify relationships using grouped statistics and correlations.
8. Detect the difference between pooled and within-group temperature effects.
9. Define and label an engineering comparison metric.
10. Frame recovery and residual strain as competing objectives.
11. Add a Pareto analysis rather than claiming a false optimum.
12. Use a second paper to connect the strain analysis to recovery stress and cyclic behaviour.
13. Formulate testable hypotheses.
14. Design a larger factorial experiment for future validation.

The research contribution is therefore the **quantitative re-analysis, synthesis and experimental research design**, not a claim of having performed the original experiments.

---

## 20. Final conclusion

Under the specific conditions represented by the P1 extracted data, increasing prestrain from 1% to 7% is strongly associated with increased recovered strain, but residual strain increases as well. Mean project-defined recovery fraction decreases from 92.56% at 1% prestrain to 85.45% at 7% prestrain.

Within every prestrain group, recovered strain decreases as prestraining temperature rises from 253 K to 273 K. The weak pooled temperature correlation therefore should not be interpreted as evidence that temperature is irrelevant.

P2 reinforces the engineering importance of residual strain and recovery stress by showing that recovery-stress behaviour is affected by residual strain, heating temperature and thermal cycling in TiNi.

The strongest defensible research statement is:

> **The extracted Ni-Ti-Nb data indicate a recovery–residual-deformation trade-off controlled by prestrain and influenced by prestraining temperature. A larger factorial experiment that measures recovery strain, residual strain and recovery stress together is required to identify an application-specific optimum.**

---

## 21. File guide

### `data/`

- `sma_extracted_data.csv` — **primary nine-row quantitative dataset**. This is the file to inspect first.
- `paper2_literature_findings.csv` — human-readable findings from the second TiNi paper; deliberately not mixed into the primary dataset.
- `paper_usage_matrix.csv` — explains exactly how each paper is used.
- `data_dictionary.md` — explains every primary CSV column.

### `src/`

- `SMA_quantitative_analysis.py` — complete reproducible analysis script.

### `results/`

Machine-readable outputs for grouped statistics, correlations, temperature effects, interaction analysis, recovery/residual trade-off, Pareto analysis and provenance.

### `figures/`

Eight generated analysis figures, including the Pareto-frontier figure.

### `report/`

- `SMA_project_report.md` — complete report.
- `DEFENCE_AND_PRESENTATION_NOTES.md` — viva/presentation preparation.

---

## References

1. Kusagawa, M., Nakamura, T., & Asada, Y. (2001). *Fundamental Deformation and Recovery Behaviors of Ni-Ti-Nb Shape Memory Alloy*. JSME International Journal, Series A, 44(1), 57–63.
2. Tobushi, H., Ohashi, Y., Saida, H., Hori, T., & Shirai, S. (1992). *Recovery Stress and Recovery Strain of TiNi Shape Memory Alloy (Cyclic Properties under Constant Residual Strain and Constant Maximum Stress)*. JSME International Journal, Series I, 35(1), 84–90.

## Data provenance statement

All nine numerical observations in the main analysis are **figure-extracted literature data from P1 Fig. 9(a–c)**. P2 is used as a separate comparative literature source. Neither paper's experimental measurements are claimed as original measurements performed by the student.
