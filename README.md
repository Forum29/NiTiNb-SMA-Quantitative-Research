# Ni-Ti-Nb SMA Quantitative Re-analysis
Literature-based quantitative re-analysis of Ni-Ti-Nb Shape Memory Alloy (SMA) behaviour using published experimental data and Python.

## 1. Project Overview
Shape Memory Alloys can recover deformation when subjected to appropriate thermal conditions. The extent of recovery can depend on factors such as prestrain, prestraining temperature, material composition and thermal history.
This project investigates the reported deformation and recovery behaviour of a Ni-Ti-Nb Shape Memory Alloy using numerical data extracted from a published experimental study.
The project does **not** reproduce the original laboratory experiment. Instead, it uses published experimental results as the basis for a quantitative re-analysis.
The main objective was to examine:
- how prestrain affects recovered and residual strain;
- how prestraining temperature affects recovery behaviour;
- the relationship between recovered and residual strain;
- the trade-off between deformation recovery and residual deformation;
- how the observed trends can be used to formulate questions for a future experiment.

## 2. Nature of the Project
This is a **literature-based quantitative re-analysis**.
The primary numerical dataset contains nine observations manually digitised from Fig. 9(a-c) of the primary Ni-Ti-Nb study.
The project therefore consists of:
1. identifying relevant published experimental results;
2. manually extracting approximate numerical values from published graphs;
3. recording the extracted values with their source information;
4. analysing the data using Python;
5. comparing the effects of prestrain and prestraining temperature;
6. examining recovery and residual strain together;
7. using a second published study for additional recovery-stress context;
8. proposing a follow-up experimental design based on the observed trends.
No claim is made that the original experiments were performed by the project author.

# 3. Research Questions
The analysis was structured around the following questions:
### Q1. How does prestrain affect recovered strain?
The analysis examines whether increasing prestrain is associated with an increase in recovered strain.
### Q2. How does prestrain affect residual strain?
The analysis examines whether increasing prestrain is also associated with greater residual deformation.
### Q3. How does prestraining temperature affect recovery?
The extracted data are compared across 253 K, 263 K and 273 K for each prestrain level.
### Q4. Is there a relationship between recovered and residual strain?
Recovered and residual strain are analysed together to examine whether higher recovery is accompanied by changes in residual deformation.
### Q5. Can the observed behaviour be framed as a recovery-residual trade-off?
The tested conditions are compared using both recovered and residual strain rather than considering recovered strain alone.
### Q6. What experiments could be performed next?
The observed trends are used to formulate a follow-up factorial experimental design involving prestrain and prestraining temperature.

# 4. Primary Literature Source
## P1 — Quantitative Data Source
Kusagawa, M., Nakamura, T., & Asada, Y. (2001).
**"Fundamental Deformation and Recovery Behaviors of Ni-Ti-Nb Shape Memory Alloy."**
*JSME International Journal, Series A, 44(1), 57-63.*
The nine numerical observations used in the quantitative analysis were manually digitised from **Fig. 9(a-c)** of this study.
The extracted observations correspond to:
- Prestrain: 1%, 3% and 7%
- Prestraining temperature: 253 K, 263 K and 273 K
- Recovered strain
- Residual strain
The extracted values are approximate values read from plotted experimental points. They are therefore not treated as newly measured laboratory data.

# 5. Secondary Literature Source
## P2 — Recovery-Stress Context
Tobushi, H., Ohashi, Y., Saida, H., Hori, T., & Shirai, S. (1992).
**"Recovery Stress and Recovery Strain of TiNi Shape Memory Alloy (Cyclic Properties under Constant Residual Strain and Constant Maximum Stress)."**
This paper was used as a separate literature source to broaden the interpretation of:
- recovery stress;
- recovery strain;
- residual strain;
- heating temperature;
- thermal cycling behaviour.
The P2 data were **not combined statistically with the P1 dataset** because P2 concerns a TiNi system rather than the Ni-Ti-Nb system analysed quantitatively in this project.

# 6. Dataset
The primary dataset is stored in:
`data/sma_extracted_data.csv`
It contains exactly nine observations extracted from the primary literature source.
Each observation records source information such as:
- source paper;
- source figure;
- journal page;
- PDF page;
- prestrain;
- prestraining temperature;
- recovered strain;
- residual strain;
- extraction status.
The dataset is intentionally small because it represents the specific experimental points selected from the published figure.
The values should be interpreted as **figure-extracted approximations**, not original laboratory measurements.

# 7. Data Extraction
The numerical values were obtained by manually reading the plotted data points from Fig. 9(a-c) of the primary paper.
The extraction process was:
1. identify the relevant experimental curves;
2. identify the plotted points corresponding to the required conditions;
3. read the approximate numerical values from the graph;
4. enter the observations into a structured CSV dataset;
5. record the source figure and page information for traceability;
6. use the resulting dataset for quantitative analysis.
No automated image-recognition or computer-vision method was used for the extraction.

# 8. Quantitative Analysis
The Python workflow performs the following analyses.
### Descriptive statistics
Mean and standard deviation are calculated for recovered and residual strain at each prestrain level.
### Pearson correlation
Pearson correlation is used to examine linear association between:
- prestrain and recovered strain;
- prestrain and residual strain;
- prestraining temperature and recovered strain;
- prestraining temperature and residual strain;
- recovered strain and residual strain.
### Descriptive regression
Simple linear regression and R² values are used to describe relationships within the extracted dataset.
Because the primary dataset contains only nine observations, these regressions are treated as **exploratory/descriptive relationships rather than validated predictive models**.
### Temperature comparison
For each prestrain level, recovered strain is compared across the three tested prestraining temperatures.
### Recovery fraction
A project-defined recovery fraction is calculated as:
`Recovered Fraction = Recovered Strain / (Recovered Strain + Residual Strain) × 100`
This quantity is used only as a comparative measure within this project. It is **not presented as a standardized SMA material property**.
### Recovery-residual trade-off
Recovered and residual strain are considered together to examine how the two quantities change across the tested conditions.
### Pareto analysis
A Pareto-style comparison is performed within the tested conditions to identify observations that are not simultaneously dominated in both recovered and residual strain.
This analysis is limited to the nine tested conditions and is **not intended to identify a universal optimum for Ni-Ti-Nb SMA processing**.
### Exploratory interaction analysis
Prestrain and prestraining temperature are examined together to identify possible interaction patterns that could be investigated experimentally in a larger dataset.

# 9. Main Quantitative Results
The analysis produced the following relationships.
### Prestrain and recovered strain
- Pearson r = 0.9920
- R² = 0.9840
Within the extracted dataset, higher prestrain is strongly associated with higher recovered strain.
### Prestrain and residual strain
- Pearson r = 0.9039
- R² = 0.8171
Higher prestrain is also associated with higher residual strain within the tested observations.
### Temperature and recovered strain
- Pearson r = -0.1145
- R² = 0.0131
The pooled linear relationship between prestraining temperature and recovered strain is weak in this small dataset.
### Temperature and residual strain
- Pearson r = 0.2964
- R² = 0.0878
The pooled linear relationship is also relatively weak.
### Recovered and residual strain
- Pearson r = 0.8473
- R² = 0.7179
Recovered and residual strain show a positive association within the extracted observations.
These results describe the behaviour of the selected published observations and should not be interpreted as universal material laws.

# 10. Observed Temperature Trends
Recovered strain changes with prestraining temperature differently at different prestrain levels.
| Prestrain | 253 K | 263 K | 273 K |
|-----------|------:|------:|------:|
| 1% | 0.50% | 0.42% | 0.21% |
| 3% | 2.20% | 2.05% | 1.67% |
| 7% | 5.50% | 5.20% | 4.65% |
For the extracted observations, recovered strain decreases as prestraining temperature increases at all three prestrain levels.
The relative change is approximately:
- 1% prestrain: -58%
- 3% prestrain: -24.1%
- 7% prestrain: -15.5%
These changes are descriptive observations from the published data and are not interpreted as a general temperature law.

# 11. Recovery-Residual Analysis
The mean recovered strain and residual strain were:
| Prestrain | Mean Recovered Strain | Mean Residual Strain |
|-----------|----------------------:|---------------------:|
| 1% | 0.377% | 0.030% |
| 3% | 1.973% | 0.253% |
| 7% | 5.117% | 0.867% |
The project-defined recovered fraction of observed deformation was:
| Prestrain | Recovered Fraction |
|-----------|-------------------:|
| 1% | 92.56% |
| 3% | 88.34% |
| 7% | 85.45% |
The results indicate that increasing prestrain in the tested observations is accompanied by both greater recovered strain and greater residual strain.
This provides the basis for treating recovery and residual deformation as two quantities that should be considered together rather than evaluating recovery alone.

# 12. Pareto Analysis
A Pareto-style analysis was performed within the nine tested conditions using recovered strain and residual strain.
Four tested conditions were identified as non-dominated within the selected dataset:
- 1% prestrain / 253 K
- 1% prestrain / 263 K
- 3% prestrain / 253 K
- 7% prestrain / 253 K
This result is specific to the tested observations and the objectives defined for this project.
It should **not** be interpreted as a universal optimum for Ni-Ti-Nb SMA processing.

# 13. Follow-up Experimental Design
The literature analysis suggested a follow-up experiment in which the effects of:
- prestrain;
- prestraining temperature
could be studied systematically.
A factorial design would allow the interaction between these factors to be examined rather than changing one variable at a time.
Possible response variables include:
- recovered strain;
- residual strain;
- recovery fraction;
- recovery stress, where measurement equipment is available.
The purpose of this section is to formulate a research question for future experimental work rather than claim that the proposed experiment has already been performed.

# 14. Project Structure
```text
NiTiNb-SMA-Quantitative-Research/
│
├── data/
│   └── sma_extracted_data.csv
│
├── figures/
│   └── generated analysis figures
│
├── references/
│   └── literature sources
│
├── report/
│   └── project documentation and audit files
│
├── results/
│   ├── quantitative results
│   └── figure inventory
│
├── src/
│   └── SMA_quantitative_analysis.py
│
├── README.md
├── RUN_PROJECT.bat
├── SMA_Project_Final_Results.pdf
└── requirements.txt


