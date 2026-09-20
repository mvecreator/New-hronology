# 03. Исследовательские gates

## SAXO-PACKAGE-1 — CLOSED
**Result:** `DISTINCTIVE_MATCH_PASS / UNIQUENESS_FAIL`

## MDL-1 — CLOSED
**Result:** `RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

## MDL-CONTROL-1 — CLOSED
**Result:** `GRAMMAR_TRANSFER_PASS / CHRIST_SPECIFICITY_FAIL`

## DISCRIMINATOR-1 — CLOSED

**Result:** `STRUCTURAL_SEPARATION_FAIL / RESIDUAL_HC_SIGNAL_NOT_DEMONSTRATED`

Frozen before scoring:
- `methods/DISCRIMINATOR_1_SPEC.md`

Artifacts:
- `results/DISCRIMINATOR_1.md`
- `data/discriminator_1_scores.csv`
- `scripts/discriminator_1.py`
- `results/DISCRIMINATOR_1_VALIDATION.txt`

Key result:
- NH positives: Apollo 4/14, Esau/Jacob 8/14, Isaiah 7/14; mean 6.33; 0/3 strong.
- controls: Orpheus 8/14, Joseph 13/14, Jeremiah 13/14; mean 11.33; 2/3 strong.
- exact one-sided permutation p=0.10 is descriptive only (n=3+3 purposive holdout).

Important methodological result:
DISCRIMINATOR-1 successfully removes much of the old free metaphor/source-hopping behavior, but structural discipline alone is not Gospel-specific. Prophetic narratives such as Jeremiah can score highly without being Gospel biographies.

The frozen six-text holdout must not be reused for tuning.

## JOINT-HOLDOUT-1 — NEXT PRIMARY GATE

Preregister on a **completely new holdout** a conjunction of two already-developed components:

1. semantic Gospel coverage from the pre-existing nine-complex anchor scale;
2. structural discipline from DISCRIMINATOR-1.

The core hypothesis is:

`HC candidate = high Gospel-semantic coverage AND high structural discipline`

A generic prophetic story may score high structurally but low on Gospel-specific anchors.
A loose analogy may score on anchors but low structurally.
An explicit imitatio Christi control may score high on both but must carry an alternative-generator flag and therefore tests whether the conjunction itself is still non-specific.

No threshold or weighting may be chosen after viewing the new holdout.

## CHRISTIAN-CONTROL-1

Expand openly Christian controls:
- at least 20 saints' lives;
- 5–10 moralities;
- 5 explicit imitatio Christi texts.

## MANUSCRIPT-SURVIVAL-1

For each medieval text store:
`date_range`, `surviving_manuscripts`, `known_lost_witnesses`, `earliest_print`, `transmission_notes`, `uncertainty_grade`.

## TRUE-HOLDOUT-1

After the joint semantic+structural classifier is frozen, run a larger blind/preregistered unseen set.

## RULE-SATURATION-1

Continue tracking `DeltaF_n`, but saturation alone is no longer evidence of HC without differential specificity.

## DATE-GATE — QUEUED

Independently test dating of strong ancient controls and relevant NH sources. Structural similarity and chronological priority remain separate variables.
