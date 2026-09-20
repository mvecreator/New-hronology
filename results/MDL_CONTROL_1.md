# MDL-CONTROL-1 — Differential compression control

Status: **CLOSED / significant result**  
Date: 2026-09-21

## Gate verdict

`GRAMMAR_TRANSFER_PASS / CHRIST_SPECIFICITY_FAIL`

The frozen MDL-1 transformation dictionary transfers successfully to negative/control corpora. That is a real positive result for the existence of a reusable literary transformation grammar.

However, it does **not** discriminate the NH Christ-positive corpus from internal NH-negative corpora. In the adversarial control test, the frozen grammar compresses King Lear + Don Quixote more strongly than the later NH-positive holdout Eulenspiegel + Don Juan.

Therefore the current grammar is not a Christ-specific identifier.

This does **not** imply that HC is false. It implies that the present transformation dictionary cannot by itself distinguish HC from a broad analogy/desacralization engine compatible with HB.

## Control design

The control test is intentionally hostile to the critique.

For controls, the analyst is allowed to choose the **strongest plausible Gospel-like mappings** under the already frozen MDL-1 dictionary.

No new transformation families are introduced for the internal negative controls.

This is an adversarial specificity test, not an estimate of the prevalence of Gospel motifs in literature.

Machine-readable claims:
`data/mdl_control_1_claims.csv`

Reproduction:
`scripts/mdl_control_1.py`

## Internal NH-negative controls

The strongest internal controls are especially valuable because NH themselves assign them to a different prototype:

- **King Lear** → Ivan the Terrible / Basil the Blessed
- **Don Quixote** → Ivan the Terrible

NH classification sources:
https://chronologia.org/en/shakespeare/
https://chronologia.org/charskii_rim/lit.html

Thus, under NH's own classification, these texts should not behave as strong Christ-code positives.

### King Lear control mappings

Examples coded under the frozen dictionary:

- Lear degraded into a mad wandering king → R1
- Kent/Fool/Edgar as follower group → R2
- close-circle betrayals → direct Judas-like betrayal
- Lear's mock trial → N11 role reversal
- exposure and suffering in the storm → R5 Passion inversion
- plot to kill Lear → R5
- prison + secret assassination order → R5
- Gloucester's fake cliff death / apparent divine rescue → R6
- Poor Tom as degraded sacred hero → R1
- final death / innocent execution scenes → R5

Primary text:
https://www.folger.edu/explore/shakespeares-works/king-lear/read/

Relevant textual facts include:
- Lear's daughters turn against him;
- Edmund betrays Gloucester;
- Lear conducts a mock trial in madness;
- Gloucester warns that Lear's death is being plotted;
- Lear and Cordelia are imprisoned and secretly marked for death;
- Gloucester's staged cliff fall produces an apparent death/rescue sequence.

### Don Quixote control mappings

Examples:

- mad protagonist → R1
- Sancho as stable follower → R2
- Don Quixote instructs Sancho → R2
- Dulcinea enchantment trick → R4
- Clavileño staged supernatural journey → R4
- Altisidora's staged death/resurrection → R6
- Sancho's suffering is represented as causally restoring Altisidora → R4
- Sierra Morena penance → R5
- cave descent/return → R6
- final defeat/death → R5
- repeated ducal supernatural pageants → R4

Primary text:
https://www.gutenberg.org/cache/epub/996/pg996-images.html

The Altisidora episode is particularly diagnostic because the text itself explicitly calls the staged event a "resurrection"; she is placed on a catafalque, declared dead, then rises alive, while Sancho's inflicted suffering is presented inside the joke as the causal mechanism.

## Differential MDL result

### NH later positive holdout

From MDL-1:

Training:
`Hamlet + Faust`

Holdout:
`Eulenspiegel + Don Juan`

- claims: 16
- transformed: 14
- independent baseline: `113.7384 bits`

Frozen grammar:

- no order penalty: `103.9639 bits` = **−8.59%**
- `log2(7!)` Eulenspiegel order cost: `116.2631` = **+2.22%**
- `log2(10!)`: `125.7550` = **+10.57%**

### Internal NH-negative controls

`King Lear + Don Quixote`

- claims: 24
- direct: 2
- transformed: 22
- base structural operations: 30
- selector lower bound: `43.7549 bits`
- independent baseline: `162.8526 bits`

Because all required families already exist in the frozen NH dictionary, new-family cost is zero.

Frozen grammar:

#### No order penalty

`121.3038 bits`

Difference:

`−41.5489 bits = −25.51%`

#### Conservative `log2(7!)` per control text

`145.9022 bits`

Difference:

`−16.9505 bits = −10.41%`

#### `log2(10!)` per control text

`164.8859 bits`

Difference:

`+2.0332 bits = +1.25%`

## Direct comparison

| Scenario | NH-positive later holdout | Internal NH-negative controls |
|---|---:|---:|
| no order cost | −8.59% | **−25.51%** |
| moderate order cost | +2.22% | **−10.41%** |
| strong order cost | +10.57% | **+1.25%** |

The controls outperform the positive holdout in every matched sensitivity regime.

This is the central result of MDL-CONTROL-1.

## Why this matters

A Christ-specific code would require approximately:

`compression(NH Christ-positive) >> compression(internal non-Christ controls)`

The observed direction is the opposite:

`compression(internal controls) >= compression(positive holdout)`

Therefore the frozen grammar's transferability cannot be interpreted as evidence that it specifically decodes Christ.

It behaves more like a reusable literary analogy/inversion grammar.

## Christian controls

A second control class tests a different alternative mechanism: explicit Christian imitation.

### Martin of Tours

Sulpicius Severus explicitly gives:
- Martin's baptism;
- confrontation with the devil;
- eighty disciples;
- common communal meals;
- public scourging and exile;
- healings;
- exorcisms;
- resurrection of a dead catechumen;
- resurrection of a hanged slave;
- a false-Christ temptation scene;
- prophetic foreknowledge;
- imprisonment / willingness to face danger unarmed.

Primary text:
https://www.newadvent.org/fathers/3501.htm

Examples:
- eighty disciples: chapter 10;
- resurrection of catechumen: chapter 7;
- healings/exorcisms: chapters 16–17;
- false Christ: chapter 24.

### Francis of Assisi

Bonaventure explicitly supplies:
- twelve brethren;
- Gospel preaching;
- conscious imitation of Gospel poverty;
- stigmata identified as the wounds of Christ;
- explicit "crucified with Christ" framing;
- advance knowledge of his death;
- farewell discourse to gathered brethren;
- reading John 13 immediately before death;
- naked death explicitly modeled on Christ Crucified;
- postmortem bodily appearances and healings.

Primary text:
https://www.ecatholic2000.com/bonaventure/assisi/francis.shtml

Most importantly, Bonaventure **states the imitation mechanism openly**. The text is not hiding the relation.

## Christian-control numbers

Combined Martin + Francis:

- claims: 24
- **direct mappings: 18**
- transformed mappings: 6
- direct-hit rate: **75%**

For comparison, the entire 54-claim NH MDL-1 set had 14 direct claims:

`14/54 = 25.9%`

Thus openly Christian imitation generates a substantially denser Gospel-like signal than the NH literary corpus.

Among the six transformed Christian-control claims:

- independent baseline: `38.7744 bits`
- frozen grammar, no order penalty: `26.0947 bits`
- apparent compression: **−32.70%**

This transformed-only result is order-sensitive if the analyst is allowed arbitrary episode selection, so it is not used as the principal Christian-control statistic.

The principal statistic is the 75% direct-match rate.

## Interpretation

MDL-CONTROL-1 separates two questions.

### Does a reusable transformation grammar exist?

**Yes.**

The same dictionary maps across NH-positive and negative texts.

### Is the grammar Christ-specific?

**No evidence of that at present.**

Internal NH negatives compress at least as well as the positive holdout.

And openly Christian literature produces even stronger direct Gospel structure through an independently known mechanism: deliberate imitation.

## Effect on hypotheses

### H0

Still insufficient.

There is genuine structured transfer and reuse.

### HB

**Strongly strengthened.**

HB naturally predicts:
- reusable desacralization/inversion families;
- broad selector freedom;
- good transfer to unrelated literature;
- strong Gospel resemblance in explicit Christian imitation.

### HC

Not logically excluded.

But the present frozen grammar fails the specificity requirement.

For HC to regain evidential force, it needs discriminators that:
1. are not common in internal NH negatives;
2. are not generated by ordinary imitatio Christi;
3. preserve role/order/causal structure;
4. predict unseen NH-positive material before inspection.

## Important limitation

The control claims were selected adversarially by the analyst to maximize false-positive pressure.

Therefore these numbers are **not population prevalence estimates** and should not be treated as a conventional randomized statistical sample.

But for a specificity test this asymmetry is intentional: the existence of well-matched negative controls that compress better than the positive holdout is sufficient to show that the current code is not diagnostic.

## Gate verdict

`MDL-CONTROL-1 = GRAMMAR_TRANSFER_PASS / CHRIST_SPECIFICITY_FAIL`

## Next gate

**DISCRIMINATOR-1**

Freeze a small set of features that HC predicts should distinguish Christ-reflection texts from:
- internal NH negatives;
- secular controls;
- explicit Christian imitation.

Candidate discriminators:
- same-protagonist preservation;
- multi-event order preservation;
- prediction → fulfilment linkage;
- event centrality;
- low source hopping;
- low selector entropy;
- low role swapping;
- out-of-sample prediction.

The new discriminator must be frozen before looking at the next positive/negative holdout set.
