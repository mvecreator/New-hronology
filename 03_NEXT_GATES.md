# 03. Исследовательские gates

## SAXO-PACKAGE-1 — CLOSED
**Result:** `DISTINCTIVE_MATCH_PASS / UNIQUENESS_FAIL`

## MDL-1 — CLOSED
**Result:** `RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

## MDL-CONTROL-1 — CLOSED
**Result:** `GRAMMAR_TRANSFER_PASS / CHRIST_SPECIFICITY_FAIL`

## DISCRIMINATOR-1 — CLOSED
**Result:** `STRUCTURAL_SEPARATION_FAIL / RESIDUAL_HC_SIGNAL_NOT_DEMONSTRATED`

## JOINT-HOLDOUT-1 — CLOSED

**Result:** `GENERIC_STRUCTURE_FILTER_PASS / NH_POSITIVE_VALIDATION_FAIL / OPEN_CHRISTIAN_CONTROL_PASS`

Frozen method:
- `methods/JOINT_HOLDOUT_1_SPEC.md`

Frozen text selection:
- `methods/JOINT_HOLDOUT_1_SELECTION.md`

Artifacts:
- `results/JOINT_HOLDOUT_1.md`
- `data/joint_holdout_1_scores.csv`
- `scripts/joint_holdout_1.py`
- `results/JOINT_HOLDOUT_1_VALIDATION.txt`

Joint rule:
`G>=9 AND K>=3 AND D>=10`

Result:
- NH positives Job / Prince Igor / Muhammad-Christ layer: `0/3` joint pass.
- generic controls Moses / Samson: both structurally strong but correctly rejected by Gospel-semantic threshold.
- Saint Benedict: joint pass, but `A=2` explicit Christian hagiographic generator.

The conjunction is methodologically better than structure alone, but it does not validate HC on the first fresh holdout and is not by itself HC-specific.

## TRUE-HOLDOUT-1 — NEXT PRIMARY GATE

Run the exact frozen joint classifier on a larger preregistered unseen corpus.

Requirements:
- freeze all members before scoring;
- include NH-positive Christ-reflection claims;
- include internal NH negatives;
- include secular/mythic controls;
- include explicit Christian/hagiographic controls;
- do not change `G>=9`, `K>=3`, `D>=10`;
- report alternative-generator flag A separately;
- target enough texts for group-level uncertainty to become more meaningful.

The purpose is now confirmatory:
`Does the frozen joint classifier produce more A=0 joint passes in NH-positive material than in controls?`

## CHRISTIAN-CONTROL-1

Expand openly Christian controls:
- at least 20 saints' lives;
- 5–10 moralities;
- 5 explicit imitatio Christi texts.

## MANUSCRIPT-SURVIVAL-1

For each medieval text store:
`date_range`, `surviving_manuscripts`, `known_lost_witnesses`, `earliest_print`, `transmission_notes`, `uncertainty_grade`.

## RULE-SATURATION-1

Continue tracking `DeltaF_n`, but saturation alone is no longer evidence of HC without differential specificity.

## DATE-GATE — QUEUED

Independently test dating of strong ancient controls and relevant NH sources. Structural similarity and chronological priority remain separate variables.
