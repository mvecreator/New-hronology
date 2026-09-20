# DISCRIMINATOR-1 — frozen specification

Frozen before detailed scoring of the new holdout set.

## Purpose

Test whether NH Christ-reflection candidates preserve a **linked biography structure** better than matched controls after the broad transformation grammar has already failed Christ-specificity.

The discriminator does **not** count motifs. It scores structural constraints that are costly to satisfy accidentally or by free hermeneutic selection.

## Structural score D

Seven dimensions, each scored 0/1/2 with equal weight.

Maximum:

`D = 14`

### R — same-protagonist preservation

- 0: fewer than half of the matched core events belong to the same source protagonist, or role transfers are essential.
- 1: a majority belong to one protagonist, but one or more major matched events require another actor/role.
- 2: nearly all core matched events are carried by the same protagonist.

### O — multi-event order preservation

- 0: no ordered chain of three matched events.
- 1: at least three matched events preserve relative order.
- 2: at least four causally/narratively linked matched events preserve relative order.

Order is evaluated in the source narrative as transmitted, not after episode rearrangement.

### P — prediction → fulfilment linkage

- 0: no advance prediction/protocol connected to a matched later event.
- 1: broad foreshadowing, preparation, or prediction exists.
- 2: an explicit future event/condition is stated in advance and later fulfilled in the same chain.

Elapsed time reported only after the event does not count as prediction.

### C — causal integration

- 0: matched events are largely independent motifs.
- 1: some matched events are causally linked.
- 2: at least three matched events form a causal chain in which earlier events materially enable or explain later ones.

### N — narrative centrality

- 0: matches are peripheral/decorative.
- 1: substantial episode but not the main arc.
- 2: matched package controls the protagonist's principal arc or climax.

Centrality must be judged inside the source before Gospel comparison.

### L — source locality

- 0: the mapping requires two or more source/version jumps or composite reconstruction across materially distinct witnesses.
- 1: one substantive source/version jump is needed.
- 2: the package is recoverable from one primary narrative source/version.

Ordinary philological comparison of translations does not count as a jump; importing a different legend/version to supply a missing event does.

### S — selector specificity

- 0: mapping depends on a broad metaphor/analogy class with more than ~8 plausible targets or unconstrained object/role selection.
- 1: mapping is constrained but still admits roughly 3–8 plausible targets.
- 2: mapping is direct or near-unique (approximately 1–2 plausible targets in context).

## Structural classification

- `D >= 10`: strong structural candidate
- `D = 7..9`: ambiguous
- `D <= 6`: weak / non-specific

These thresholds are frozen before scoring the holdout.

## Alternative-generator flag A

D alone cannot distinguish historical identity from known imitation.

A is therefore reported separately and is **not tuned into D**.

- `A=0`: no documented direct imitation/source mechanism identified in the material used.
- `A=1`: plausible genre/tradition/intertextual generator exists.
- `A=2`: explicit textual imitation/model, ritual script, or directly acknowledged source relation explains the resemblance.

Interpretation:
- `D>=10, A=0`: candidate residual signal for HC.
- `D>=10, A>=1`: structurally strong but non-specific because HB has an identified generator.
- lower D: not a strong residual HC signal regardless of A.

## Holdout selection frozen before detailed scoring

### NH-positive holdouts

Chosen from the official NH book *Lost Gospels* because they are explicitly labelled reflections of Christ and were not part of MDL-1/MDL-CONTROL-1 scoring:

1. Apollo (mythic Apollo layer distinct from Philostratus' Apollonius biography)
2. Esau/Jacob composite as NH's intertwined reflection
3. Isaiah as NH's "lost gospel"

Official classification:
https://chronologia.org/evangelia/

### Matched controls

1. Orpheus — mythic/religious hero control for Apollo
2. Joseph (Genesis) — internal NH negative from the same *Lost Gospels* book; NH explicitly assigns Joseph primarily to Joseph Volotsky / Dmitry-Mordecai rather than Christ
3. Jeremiah — prophetic/martyrdom-adjacent biblical control for Isaiah

Control eligibility rule:
a control is excluded only if the official NH corpus explicitly classifies it as a Christ reflection before scoring. No control is excluded merely because it looks Gospel-like.

## No-tuning rule

After this freeze:
- no dimensions may be added or removed;
- no weights may change;
- thresholds may not change;
- holdout members may not be replaced because of their scores;
- any methodological defect found after scoring must be documented and deferred to a new version.
