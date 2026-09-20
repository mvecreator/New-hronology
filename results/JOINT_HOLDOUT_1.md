# JOINT-HOLDOUT-1 — Semantic × structural conjunction

Status: **CLOSED / significant result**  
Date: 2026-09-21

## Gate verdict

`GENERIC_STRUCTURE_FILTER_PASS / NH_POSITIVE_VALIDATION_FAIL / OPEN_CHRISTIAN_CONTROL_PASS`

The preregistered conjunction successfully fixes a defect revealed by DISCRIMINATOR-1:
high structural discipline alone is no longer sufficient.

However:
- none of the three frozen NH-positive candidates passes the joint criterion;
- Moses and Samson are correctly rejected despite high structural scores;
- Saint Benedict passes both axes, but carries `A=2` because the source is explicitly Christian hagiography.

Therefore the joint criterion improves filtering, but still does **not** produce a residual HC-specific signal.

This does not prove HC false. It means the first fresh semantic×structural holdout fails to validate the NH-positive class.

## Frozen method

Specification:
`methods/JOINT_HOLDOUT_1_SPEC.md`

Selection:
`methods/JOINT_HOLDOUT_1_SELECTION.md`

Semantic pass:
`G >= 9 AND K >= 3`

where:
- `G` = total over the frozen 9 Gospel anchors (max 27)
- `K` = number of anchors scored >=2

Structural pass:
`D >= 10`

Joint pass:
`semantic_pass AND structural_pass`

Alternative-generator flag:
- A=0 no identified generator
- A=1 plausible genre/intertextual generator
- A=2 explicit Christian/imitation/source generator

## Frozen holdout

### NH-positive
1. Job
2. Prince Igor
3. Muhammad — Christ/Gospel layer

### Controls
1. Moses
2. Samson
3. Saint Benedict

All six were frozen before numerical scoring and were not replaced.

## Results

| Case | Class | G/27 | K>=2 | D/14 | Semantic | Structural | JOINT | A |
|---|---|---:|---:|---:|---|---|---|---:|
| Job | NH+ | 7 | 2 | 12 | FAIL | PASS | **FAIL** | 1 |
| Prince Igor | NH+ | 7 | 2 | 5 | FAIL | FAIL | **FAIL** | 1 |
| Muhammad Christ layer | NH+ | 8 | 2 | 3 | FAIL | FAIL | **FAIL** | 1 |
| Moses | control | 8 | 1 | 13 | FAIL | PASS | **FAIL** | 1 |
| Samson | control | 7 | 2 | 12 | FAIL | PASS | **FAIL** | 1 |
| Saint Benedict | Christian control | 16 | 5 | 13 | PASS | PASS | **PASS** | 2 |

NH-positive mean:
- `G = 7.3333`
- `D = 6.6667`
- joint pass: `0/3`

Controls mean:
- `G = 10.3333`
- `D = 12.6667`
- joint pass: `1/3`

Descriptive exact one-sided permutation:
- G controls−positives: +3.0, p=0.35
- D controls−positives: +6.0, p=0.10

These p-values are descriptive only: n=3+3 and the holdout is purposive.

## Job

NH officially include Job among Christ reflections and specifically call the Book of Job a possible reflection of the Passion of Andronicus-Christ.

NH source:
https://chronologia.org/evangelia/

The primary narrative strongly supports:
- a direct Satanic test/temptation;
- extreme innocent suffering;
- accusations and confrontation by companions;
- final restoration.

But Job is explicitly **not killed** in the ordeal. God orders that his life be spared; after restoration Job lives another 140 years and dies only later.

Primary sources:
https://www.biblegateway.com/passage/?search=Job+2&version=NIV
https://www.biblegateway.com/passage/?search=Job+42&version=NIV

Frozen semantic coding:
- Temptation = 3
- Judas/betrayal = 1
- Passion = 2
- Resurrection = 1
- all other anchors = 0

`G=7, K=2`

The story is structurally disciplined:
same protagonist, preserved sequence, strong causal integration, central suffering, one source.

`D=12`

Result:
structural pass, semantic fail, no joint pass.

The decisive point is that restoration after suffering is not the same event class as return from death.

## Prince Igor

NH explicitly call the Prince Igor narrative a partial reflection of Christ.

NH source:
https://chronologia.org/ord_rus/rus111.html

The chapter itself supplies several Passion-like analogies:
- betrayal / hostile elite;
- money motif;
- few companions at capture;
- public violent death;
- execution associated with trees/pillars;
- signs around death.

However the same NH chapter shifts between Prince Igor and Igor Olgovich and combines Tatishchev, Leo the Deacon, Karamzin and hagiographic material.

This damages:
- same-protagonist preservation;
- source locality;
- ordered biography reconstruction.

Semantic score:
- Disciples = 1
- Judas/betrayal = 2
- Passion = 3
- Resurrection/postmortem signs = 1

`G=7, K=2`

Structural:
`D=5`

No joint pass.

This is an important result because the strongest similarity is concentrated in one anchor — Passion — rather than distributed across the Gospel semantic profile.

## Muhammad — Gospel layer

NH explicitly state that Muhammad's biography is layered and includes stories about Andronicus-Christ.

Their own table of contents names:
- immaculate conception / annunciation;
- Caesarean birth;
- Bethlehem star;
- John-the-Baptist analogue;
- temple-cleansing analogue;
- descent into hell;
- ascension;
- resurrection on the third day;
- Christian-style baptism.

NH source:
https://chronologia.org/prorok/index2009.html

But the frozen nine-anchor system does not reward arbitrary Christian motifs; it only counts the pre-existing nine complexes.

Generous semantic coding:
- Baptism = 3
- Disciples = 1
- Passion = 1
- Resurrection = 3
- other frozen anchors = 0

`G=8, K=2`

Thus even a very Christian-looking list fails the preregistered semantic condition because most of its resemblance lies **outside** the frozen anchor set.

Structural weakness is stronger:
NH themselves describe the Muhammad biography as a composition of several historical layers, including Christ, Moses/Joshua, and Mehmed II. The chapter also shifts matching roles to Ibn al-Hayyaban, Omar/Paul and other figures.

`D=3`

No joint pass.

This is precisely what the conjunction was designed to detect:
many suggestive Christian parallels do not automatically form a same-protagonist ordered Gospel biography.

## Moses control

Moses is an important success of the joint filter.

The Moses narrative is structurally excellent:
- same protagonist across a long continuous arc;
- extensive prediction→fulfilment;
- causal linkage;
- centrality;
- low source hopping.

`D=13`

Primary text also contains potentially tempting Gospel analogies:
- water miracles;
- healing through the bronze serpent;
- a close leadership circle / seventy elders;
- ritual meals;
- rebellion by insiders;
- threats against Moses.

Examples:
https://www.biblegateway.com/passage/?search=Exodus+17&version=NIV
https://www.biblegateway.com/passage/?search=Numbers+21%3A4-9&version=NIV
https://www.biblegateway.com/passage/?search=Exodus+24&version=NIV
https://www.biblegateway.com/passage/?search=Numbers+16&version=NIV

But under the frozen semantic scale these are mostly broad analogies:
- Baptism = 1
- Disciples = 1
- Healings = 2
- Cana = 1
- Judas = 1
- Last Supper = 1
- Passion = 1
- Resurrection = 0

`G=8, K=1`

Therefore Moses is rejected by the joint criterion.

This is a direct methodological improvement over DISCRIMINATOR-1.

## Samson control

Samson also scores very high structurally:

`D=12`

Judges 16 contains a striking betrayal/Passion package:
- an intimate woman;
- payment in silver for betrayal;
- repeated deception;
- capture;
- blinding;
- imprisonment;
- public humiliation;
- voluntary final death in which he kills his enemies.

Primary source:
https://www.biblegateway.com/passage/?search=Judges+16&version=NIV

Semantic:
- Temptation = 1
- Judas/betrayal = 3
- Passion = 3
- Resurrection = 0

`G=7, K=2`

Thus a very strong Passion/Judas pair is not enough to pass a Gospel-biography classifier.

Again, the joint filter works as intended.

## Saint Benedict — decisive open-Christian control

Gregory the Great's *Dialogues II* produces the only joint pass.

The source contains:
- explicit temptation by the tempter and a woman-memory;
- a stable body of monk disciples;
- twelve monasteries, each populated by twelve monks;
- exorcisms and healings;
- revival of a dead child;
- betrayal by monks who poison his wine;
- final Eucharistic reception while supported by disciples;
- explicit foreknowledge of the day of his death;
- postmortem visionary ascent.

Primary source:
https://ccel.org/ccel/pearse/morefathers/files/gregory_02_dialogues_book2.htm

Specific evidence:
- temptation: chapter 2
- poisoned wine by monks: chapter 3
- twelve monasteries / disciples: chapter 3 following material
- raising a dead boy: chapter 11
- healings/exorcisms: chapters 16, 26, 30, 32
- prediction of death and final Eucharist among disciples: chapter 37

Frozen semantic score:
- Temptation = 3
- Disciples = 3
- Healings = 3
- Cana/wine-associated miracle = 1
- Judas/betrayal = 2
- Last Supper/final Eucharistic death scene = 2
- Passion = 1
- Resurrection/postmortem ascent = 1

`G=16, K=5`

Structural:
`D=13`

Therefore:
`JOINT_PASS = true`

But:
`A=2`

because this is an explicitly Christian hagiographic text. Gregory repeatedly explains Benedict's powers through Christ and compares saintly miracles with apostolic/Christian models.

Thus the conjunction still cannot be interpreted as a historical-identity detector.

## What the gate actually established

### Positive methodological result

The semantic×structural conjunction fixes a real failure mode.

Moses and Samson:
- high D;
- low Gospel-semantic coverage;
- correctly rejected.

So the method no longer confuses every disciplined prophecy/suffering narrative with a Gospel duplicate.

### Negative result for HC validation

None of the three frozen NH-positive candidates passes.

That means the new joint classifier did not recover an HC-specific residual signal on its first fresh holdout.

### Persistent HB challenge

Saint Benedict passes strongly and transparently because Christian hagiography can produce:
- Gospel anchor coverage;
- same-protagonist order;
- causal structure;
- prediction;
- centrality;
- source locality.

Therefore:
`JOINT_PASS` is not sufficient for HC.

The alternative-generator flag remains essential.

## Effect on hypotheses

### H0
Still insufficient as a complete explanation.

There are real non-random structured similarities.

### HB
Further strengthened.

HB predicts both observed behaviors:
1. generic strong narratives can score structurally but fail Gospel semantics;
2. explicit Christian hagiography can score high on both axes without historical identity.

### HC
Not disproved.

But after this gate:
- no frozen NH-positive holdout member produced a residual candidate;
- the sole joint pass is an explicit Christian control.

Therefore HC remains unsupported by this line of evidence.

## Gate verdict

`JOINT-HOLDOUT-1 = GENERIC_STRUCTURE_FILTER_PASS / NH_POSITIVE_VALIDATION_FAIL / OPEN_CHRISTIAN_CONTROL_PASS`

## Next gate

**TRUE-HOLDOUT-1**

The next valid move should be larger and more blinded/preregistered.

Requirements:
- freeze a larger set before scoring;
- include NH positives, internal NH negatives, secular controls and explicit Christian controls;
- retain the exact same G/K/D conjunction;
- do not alter thresholds;
- report A separately;
- aim for enough texts that group-level uncertainty becomes meaningful.

JOINT-HOLDOUT-1 must not be reused for threshold tuning.
