# 03. Исследовательские gates

## SAXO-PACKAGE-1 — CLOSED
**Result:** `DISTINCTIVE_MATCH_PASS / UNIQUENESS_FAIL`

## MDL-1 — CLOSED
**Result:** `RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

## MDL-CONTROL-1 — CLOSED
**Result:** `GRAMMAR_TRANSFER_PASS / CHRIST_SPECIFICITY_FAIL`

Key finding:
the frozen NH transformation dictionary compresses the internal NH-negative controls `King Lear + Don Quixote` more strongly than the later NH-positive holdout `Eulenspiegel + Don Juan` under every matched order-cost regime tested.

Artifacts:
- `results/MDL_CONTROL_1.md`
- `data/mdl_control_1_claims.csv`
- `scripts/mdl_control_1.py`
- `results/MDL_CONTROL_1_VALIDATION.txt`

This does not imply `HC=false`. It shows that the current grammar is not Christ-specific.

## DISCRIMINATOR-1 — NEXT PRIMARY GATE

Freeze a small set of features that HC predicts should distinguish Christ-reflection texts from:
- internal NH negatives;
- secular literary controls;
- explicit Christian imitation.

Candidate dimensions:
- same-protagonist preservation;
- multi-event order preservation;
- prediction → fulfilment linkage;
- narrative centrality;
- low source hopping;
- low selector entropy;
- low role swapping;
- out-of-sample prediction.

The feature set and weights must be frozen **before** the next positive/negative holdout is examined.

## CHRISTIAN-CONTROL-1

Expand the openly Christian control set to at least:
- 20 saints' lives;
- 5–10 moralities;
- 5 explicit imitatio Christi texts.

The current small control already shows a 75% direct Gospel-match rate for Martin + Francis.

## MANUSCRIPT-SURVIVAL-1

For each medieval text store:
`date_range`, `surviving_manuscripts`, `known_lost_witnesses`, `earliest_print`, `transmission_notes`, `uncertainty_grade`.

## TRUE-HOLDOUT-1

After a final discriminator freeze, preregister expected patterns and run blind scoring on unseen material.

## RULE-SATURATION-1

Continue tracking:
`DeltaF_n = number of genuinely new transformation rules`.

Rule-family saturation is no longer sufficient by itself; it must be paired with differential specificity.

## DATE-GATE — QUEUED

Independently test dating of strong ancient controls (especially Inanna, Alcestis, Savitri). Structural similarity and chronological priority remain separate variables.
