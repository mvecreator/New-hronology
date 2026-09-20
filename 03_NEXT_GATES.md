# 03. Исследовательские gates

## SAXO-PACKAGE-1 — CLOSED

**Result:** `DISTINCTIVE_MATCH_PASS / UNIQUENESS_FAIL`

Artifacts:
- `results/SAXO_PACKAGE_1.md`
- `data/saxo_package_1_controls.csv`

## MDL-1 — CLOSED

**Result:** `RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

The fixed 54-claim sample shows real rule-family saturation (`8→1→1→1`), but selector/source/order freedom removes robust compression.

Artifacts:
- `results/MDL_1.md`
- `data/mdl1_claims.csv`
- `scripts/mdl_selector_entropy.py`
- `results/MDL_1_VALIDATION.txt`

Important nuance: this is not `HC=false`. It means low-description-length superiority has not yet been demonstrated.

## MDL-CONTROL-1 — NEXT PRIMARY GATE

Apply the same frozen family dictionary, selector accounting and order treatment to matched negative/control corpora.

Primary question:

`Does the NH positive corpus compress materially better than non-HC literary corpora under the same code?`

This gate is necessary because a broad analogy grammar can show family saturation even when no common historical prototype exists.

Required controls should include:
- internal NH negatives (texts NH assigns to another prototype);
- secular narrative controls;
- openly Christian / imitatio Christi controls.

## CHRISTIAN-CONTROL-1

Expand to at least 20 saints' lives, 5–10 moralities and 5 explicit imitatio Christi texts.

## MANUSCRIPT-SURVIVAL-1

For each medieval text store:
`date_range`, `surviving_manuscripts`, `known_lost_witnesses`, `earliest_print`, `transmission_notes`, `uncertainty_grade`.

## TRUE-HOLDOUT-1

After a final freeze, preregister expected patterns and run blind scoring on unseen material.

## RULE-SATURATION-1

Continue tracking:
`DeltaF_n = number of genuinely new transformation rules`.

Family saturation alone is no longer sufficient; it must be accompanied by low selector entropy and differential control performance.

## DATE-GATE — QUEUED

Independently test dating of strong ancient controls (especially Inanna, Alcestis, Savitri). Structural similarity and chronological priority remain separate variables.
