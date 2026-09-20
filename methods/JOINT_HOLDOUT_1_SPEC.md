# JOINT-HOLDOUT-1 — preregistered specification

Frozen after DISCRIMINATOR-1 and before detailed scoring of the new holdout.

## Purpose

Test a conjunction that was motivated **before** seeing the new holdout:

1. Gospel-specific semantic coverage from the pre-existing nine-complex scale.
2. High-information structural discipline from DISCRIMINATOR-1.

The failure mode addressed is explicit:
- generic prophecy can score structurally high while being semantically non-Gospel-specific;
- loose Gospel analogy can score semantically while being structurally weak.

A candidate must pass **both axes**.

## Semantic axis G

Use the already frozen nine complexes:

1. Baptism
2. Temptation
3. Disciples
4. Healings
5. Cana / water-wine
6. Judas / close-circle betrayal
7. Last Supper
8. Passion
9. Resurrection / return after death-state

Each anchor keeps the old scale:
- 3 = close structural event with same role carrier
- 2 = systematic inversion under already frozen F0.1
- 1 = partial/broad or role-transferred match
- 0 = absent

Maximum:
`G = 27`

Also record:
`K = number of anchors scored >=2`

### Semantic pass

Frozen threshold:

`G >= 9 AND K >= 3`

Rationale:
- 9/27 is one third of the maximum possible semantic information;
- requiring at least three anchors >=2 prevents one or two spectacular scenes from carrying the result.

No semantic threshold is changed after holdout scoring.

## Structural axis D

Use DISCRIMINATOR-1 unchanged:

- R same-protagonist preservation
- O multi-event order preservation
- P prediction→fulfilment
- C causal integration
- N narrative centrality
- L source locality
- S selector specificity

Each 0–2, maximum 14.

Structural pass remains:

`D >= 10`

## Joint classification

`JOINT_PASS = (G>=9) AND (K>=3) AND (D>=10)`

No weighted sum is used.

This is deliberate: strong semantics cannot compensate for weak structure and strong structure cannot compensate for weak Gospel semantics.

## Alternative-generator flag A

Retain the existing A flag:

- 0 = no documented direct alternative generator identified
- 1 = plausible genre/intertextual/ritual generator
- 2 = explicit imitation/model or source relation

Interpretation:

- JOINT_PASS + A=0 → residual HC candidate
- JOINT_PASS + A>=1 → strong Gospel-like structure, but not HC-specific
- no JOINT_PASS → no residual HC signal in this gate

A does not alter G or D.

## Holdout selection rule

The new holdout must contain material not previously numerically scored in:
- the original 9-anchor exploratory matrix;
- MDL-1;
- MDL-CONTROL-1;
- DISCRIMINATOR-1.

The holdout will contain:
- 3 NH-positive/Christ-reflection candidates from official NH materials;
- 3 controls, including at least one explicit Christian imitation or hagiographic control.

No member may be replaced after detailed scoring because its score is inconvenient.

## No-tuning rule

After this file is frozen:
- no anchor is added/removed;
- G threshold cannot change;
- K threshold cannot change;
- D threshold cannot change;
- no weights are introduced;
- no text is replaced after scoring;
- discovered defects are recorded and deferred to JOINT-HOLDOUT-2 or another fresh gate.
