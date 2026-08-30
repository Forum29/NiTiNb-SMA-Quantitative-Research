# SMA Project — Defence / Presentation Notes

## 60-second explanation

“I conducted a quantitative, literature-based re-analysis of published Ni-Ti-Nb shape-memory-alloy experiments.My primary dataset contains nine observations digitised from Fig. 9(a-c) of Kusagawa, Nakamura and Asada's study, covering 1%, 3% and 7% prestrain at 253, 263 and 273 K. I built a reproducible Python workflow to quantify recovered strain, residual strain and temperature effects. The strongest relationship was between prestrain and recovered strain, with r = 0.992. But residual strain also increased with prestrain, so I treated recovery and residual deformation as competing engineering objectives. I calculated a clearly labelled recovery-fraction indicator and added a Pareto analysis instead of claiming a false optimum. I then used a second TiNi recovery-stress paper by Tobushi and co-workers as comparative literature to show why recovery stress, residual strain and thermal cycling matter. Finally, I designed a larger factorial experiment that would measure recovery strain, residual strain and recovery stress together.”

## If asked: “Did you perform the experiments?”

“No. The nine numerical observations are digitised from the published Ni-Ti-Nb paper. I am presenting this honestly as a computational literature re-analysis. The original experimental work belongs to the paper authors.”

## If asked: “Why did you use two papers?”

“The first paper is the quantitative Ni-Ti-Nb source. The second paper is a TiNi recovery-stress study. I used it to extend the engineering question toward recovery stress, residual strain and thermal cycling. I did not mix its numerical values into the Ni-Ti-Nb dataset because the material systems are different.”

## If asked: “Why only nine data points?”

“They come directly from the three panels of Fig. 9 in the primary source. I did not invent additional observations. The small dataset is a limitation, so I used it for exploratory quantitative analysis and then designed a larger factorial experiment as the next step.”

## If asked: “What is your strongest result?”

“Prestrain and recovered strain have r = 0.992 in the nine extracted observations. But the more interesting engineering result is that residual strain also rises with prestrain, while mean recovery fraction falls from about 92.6% at 1% prestrain to about 85.4% at 7%.”

## If asked: “Why is the pooled temperature correlation weak?”

“Prestrain creates a much larger separation between the groups. When I analyse temperature inside each prestrain group, recovered strain decreases consistently from 253 K to 273 K. So I treated the temperature effect as a within-group and interaction question rather than relying only on one pooled correlation.”

## If asked: “What is the Pareto analysis?”

“I treated higher recovered strain as better and lower residual strain as better. A condition is Pareto-optimal when no other extracted condition improves one objective without worsening the other. I used this to show the trade-off without claiming that one of the nine conditions is a universal optimum.”

## If asked: “What is recovery fraction?”

“It is a project-defined comparison metric: recovered strain divided by recovered plus residual strain. I clearly label it as project-defined; I am not claiming that it is a standardised SMA material property.”

## If asked: “What did the second paper teach you?”

“It showed why recovery strain alone is not enough for some engineering applications. Its TiNi experiments examined recovery stress, residual strain, heating temperature and thermal cycling. In particular, it reports that recovery stress decreases as residual strain increases under thermal cycling.”

## If asked: “Why did you not put the second paper's data in the same CSV?”

“Because it is TiNi rather than the Ni-Ti-Nb material in the primary study. Combining them would mix material composition and experimental conditions. I kept the second paper as a separate literature-context table.”

## If asked: “What is your actual contribution?”

“My contribution is the quantitative re-analysis and research design: I converted a published figure into a traceable dataset, reproduced the trends quantitatively, analysed the recovery–residual trade-off, separated pooled from within-group temperature behaviour, added a Pareto analysis, and designed a larger experiment that would test the hypotheses.”

## If asked: “What would you do experimentally next?”

“I would use multiple prestrain levels and temperatures with repeated specimens, then measure recovered strain, residual strain, recovery stress and transformation temperatures. If the lab allows it, I would add DSC, XRD, EBSD or microscopy to connect the macroscopic trends with transformation and microstructure.”

## If asked: “What is the optimum prestrain?”

“I would not claim a universal optimum from nine figure-extracted observations. The 7% condition gives the largest recovered strain, but also the largest residual strain and lower mean recovery fraction. The optimum depends on the application objective and requires a larger experimental dataset.”

## If asked: “Why is recovery stress important?”

“Recovery strain tells me how much deformation is recovered. Recovery stress tells me how much force the SMA can develop under constraint. For applications such as prestressing or actuation, that force can be the more important engineering output.”

## If asked: “What would make this a stronger MITACS project?”

“The next step is not adding random plots. It is validating the hypotheses experimentally with a factorial design, repeats and recovery-stress measurements, then linking the results to transformation and microstructure.”

## Slides to show

1. Research problem and motivation
2. Two source papers and why their roles are different
3. Ni-Ti-Nb primary dataset extraction from Fig. 9
4. Traceable dataset: 3 prestrains × 3 temperatures
5. Prestrain vs recovered strain
6. Prestrain vs residual strain
7. Within-prestrain temperature effect
8. Recovery fraction
9. Recovery–residual Pareto trade-off
10. What the TiNi recovery-stress paper adds
11. Research gap and hypotheses
12. Proposed factorial experiment
13. Limitations and scientific boundary
14. Conclusion

## If someone asks “What is original about your project?”

The underlying experimental observations are published, so I am not claiming to have discovered those phenomena. My contribution was to build a reproducible quantitative re-analysis from the published data, preserve source provenance, examine the prestrain–temperature effects and recovery–residual trade-off, apply a Pareto framework without claiming a universal optimum, and use the second paper to formulate a testable follow-up experimental design.