# DISCRIMINATOR-1 — Structural specificity holdout

Status: **CLOSED / significant result**  
Date: 2026-09-21

## Gate verdict

`STRUCTURAL_SEPARATION_FAIL / RESIDUAL_HC_SIGNAL_NOT_DEMONSTRATED`

A seven-dimensional high-information structural discriminator was frozen **before** detailed scoring of a new six-text holdout.

The result is adverse to Christ-specificity:

- none of the three NH-positive holdouts reaches the preregistered strong threshold;
- two of three controls do;
- the strongest scores belong to Joseph and Jeremiah, not to NH-labelled Christ reflections.

This does **not** prove HC false. It shows that the current high-information structural features still do not isolate NH Christ-reflection texts from controls.

## Frozen method

Specification:
`methods/DISCRIMINATOR_1_SPEC.md`

Seven equal-weight dimensions, each 0–2:

- R — same-protagonist preservation
- O — multi-event order preservation
- P — prediction → fulfilment
- C — causal integration
- N — narrative centrality
- L — source locality
- S — selector specificity

Maximum:
`D=14`

Thresholds frozen before scoring:
- `D>=10`: strong
- `D=7..9`: ambiguous
- `D<=6`: weak/non-specific

Alternative-generator flag:
- A=0: none identified
- A=1: plausible genre/intertextual generator
- A=2: explicit imitation/model or direct generator

Scores:
`data/discriminator_1_scores.csv`

Reproduction:
`scripts/discriminator_1.py`

## Frozen holdout

### NH-positive

From the official NH book *Lost Gospels*:
1. Apollo
2. Esau/Jacob
3. Isaiah

The official contents explicitly state that Apollo, Esau, Jacob and Isaiah are reflections of Christ:
https://chronologia.org/evangelia/

### Controls

1. Orpheus — mythic/religious hero control
2. Joseph — **internal NH negative from the same book**
3. Jeremiah — prophetic/persecution control

Joseph is especially important: the same NH contents assign Joseph primarily to Joseph Volotsky and Dmitry-Mordecai rather than to Christ.

## Scores

| Case | Class | R | O | P | C | N | L | S | D/14 | A | Classification |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Apollo | NH+ | 1 | 0 | 0 | 0 | 2 | 0 | 1 | **4** | 0 | weak |
| Esau/Jacob | NH+ | 1 | 1 | 1 | 1 | 2 | 1 | 1 | **8** | 1 | ambiguous |
| Isaiah | NH+ | 1 | 0 | 1 | 1 | 2 | 1 | 1 | **7** | 2 | ambiguous |
| Orpheus | control | 1 | 0 | 1 | 1 | 2 | 2 | 1 | **8** | 1 | ambiguous |
| Joseph | internal NH negative | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 1 | strong |
| Jeremiah | control | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 1 | strong |

NH-positive mean:
`6.3333 / 14`

Control mean:
`11.3333 / 14`

Difference:
`controls - NH+ = +5.0 points`

Strong threshold:
- NH-positive: `0/3`
- controls: `2/3`

An exact one-sided permutation calculation gives `p=0.10` on only 20 allocations. This is **descriptive only**: the holdout is purposive and n=3+3, not a random sample from a defined population.

## Apollo

Apollo was scored generously.

NH themselves expose the key structural defect in their Apollo mapping. Their official chapter states that the expected execution of Apollo is absent, then supplies the Passion from the myth of **Marsyas**, and explicitly says the classical tradition "mixed" Marsyas=Judas with Apollo=Christ and that the names/roles must be swapped.

Official NH source:
https://chronologia.org/evangelia/1_77.html

Therefore:
- R receives 1, not 0, to give the positive case benefit of doubt;
- O=0 because the proposed Gospel sequence is not a continuous ordered Apollo biography;
- P=0;
- C=0 because the matched elements are assembled from separate mythic episodes;
- N=2 generously recognizes that birth/Python/Marsyas material is important in the mythic complex;
- L=0 because the crucial Passion element requires a different character and mythic source;
- S=1 generously.

`D=4`

The result is weak even under positive-favoring coding.

## Esau/Jacob

NH's own chapter title calls Esau and Jacob **intertwined reflections of Christ, John the Baptist and Judas Iscariot**.

Their contents additionally state:
- birth of Esau/Jacob = birth of Jesus/John;
- Esau-figure is used for John in one block;
- Esau is used for Jesus in the birthright-sale block;
- Jacob is used for Judas;
- murder of Esau = execution of Christ;
- Jacob's ladder = Crucifixion and Resurrection.

Most importantly, the official contents acknowledge that canonical Scripture does **not** contain the murder of Esau and that this decisive event is supplied by "other sources."

Official NH source:
https://chronologia.org/evangelia/

The score deliberately gives the positive claim benefit of doubt:
- R=1 rather than 0 despite explicit role splitting;
- O=1;
- P=1;
- C=1;
- N=2;
- L=1 rather than 0 despite the imported murder;
- S=1.

`D=8`

Ambiguous, not strong.

## Isaiah

NH label Isaiah another "Lost Gospel" and map his martyrdom/ascension to Jesus.

But the *Ascension of Isaiah* is a composite Christian work. Scholarly summaries distinguish the Martyrdom (chapters 1–5) from the Vision (6–11). In the Vision, **Isaiah sees the descent, life, death, resurrection and ascension of the Lord**.

Thus one of the strongest resurrection/ascension-looking structures in the document concerns the Lord in Isaiah's vision, not Isaiah undergoing the same biographical sequence.

Sources:
https://chronologia.org/evangelia/
https://www.cambridge.org/core/books/abs/outside-the-old-testament/martyrdom-of-isaiah/5C6BBD9FCD1275605D7DCCB51F64FBC9
https://www.cambridge.org/core/books/abs/cambridge-edition-of-early-christian-writings/ascension-of-isaiah-611-ethiopic-version/710A7ED2BAE1A70E6596FD0C1B1D1C79

Positive-favoring score:
- R=1 rather than 0;
- O=0;
- P=1;
- C=1;
- N=2;
- L=1;
- S=1.

`D=7`

A=2 because the source itself is Christian and explicitly contains Christological visionary material.

This is exactly the sort of case where Gospel resemblance can be genuine while **identity of protagonist is false**.

## Orpheus control

Ovid supplies:
- ominous wedding foreshadowing;
- Eurydice's death;
- Orpheus' descent to the underworld;
- attempted return of Eurydice;
- later death of Orpheus;
- reunion of Orpheus and Eurydice in the underworld.

Primary source:
https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0028%3Abook%3D10
https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0028%3Abook%3D11

The control is deliberately scored downward:
- R=1 because death/recovery roles split between Orpheus and Eurydice;
- O=0 because Orpheus descends to Hades before his own death;
- P=1;
- C=1;
- N=2;
- L=2;
- S=1.

`D=8`

This lands only in the ambiguous range.

## Joseph — decisive internal NH negative

Joseph is the most important control because NH themselves classify him differently in the **same book**.

Their contents say the biblical patriarch Joseph reflects Joseph Volotsky and Dmitry-Mordecai.

NH source:
https://chronologia.org/evangelia/

Yet Genesis contains an unusually disciplined structural package in one continuous source:

1. Joseph dreams that his brothers/family bow to him.
2. The dreams intensify brotherly hostility.
3. His brothers plot his death.
4. He is cast into a pit.
5. He is sold and displaced to Egypt.
6. He undergoes humiliation and later elevation.
7. His brothers arrive and bow before him.
8. The narrator explicitly says Joseph **remembered the dreams**.

Primary source:
https://www.biblegateway.com/passage/?search=Genesis+37-42&version=NIV

The scoring is conservative:
- R=2;
- O=2;
- P=2;
- C=2;
- N=2;
- L=2;
- S=1 rather than 2.

`D=13`

This is a near-maximal score for a text that NH's own classification does **not** place in the Christ-reflection class.

That result cannot be explained away by saying the old grammar was merely too metaphorically broad: Joseph wins on protagonist identity, sequence, explicit prediction→fulfilment, causal integration and source locality.

## Jeremiah control

Jeremiah 38–39 provides another highly disciplined package:

1. Jeremiah explicitly predicts that Babylon will capture Jerusalem.
2. Officials demand his death **because of that message**.
3. King Zedekiah yields him into their hands.
4. Jeremiah is lowered into a cistern where he is expected to die.
5. Ebed-melech obtains royal permission and rescues him before death.
6. Jeremiah remains confined.
7. Jerusalem is then captured as predicted.

Primary source:
https://www.biblegateway.com/passage/?search=Jer38-39&version=NIV

Conservative score:
- R=2;
- O=2;
- P=2;
- C=2;
- N=2;
- L=2;
- S=1.

`D=13`

A=1 because prophetic narrative as a genre naturally generates prediction→opposition→persecution→fulfilment structure.

Jeremiah demonstrates that the high-information discriminator can fire strongly on a non-Gospel prophetic chain without free role swapping or source hopping.

## Why this result is stronger than MDL-CONTROL-1

MDL-CONTROL-1 could be criticized because the old transformation grammar was broad.

DISCRIMINATOR-1 was designed specifically to eliminate that problem. It rewards:
- same actor;
- preserved order;
- explicit prediction;
- causal linkage;
- centrality;
- one-source locality;
- narrow selection.

Nevertheless, controls outperform the NH positives.

Therefore the specificity failure does not depend only on broad metaphorical rules.

## Important methodological defect discovered by the gate

The result also reveals a limitation of D itself.

The seven dimensions measure **structural information quality**, not uniquely Gospel semantics.

A prophetic narrative such as Jeremiah can therefore score very highly because prediction→persecution→rescue→fulfilment is intrinsically well structured.

This is not a reason to rescore DISCRIMINATOR-1. The method was frozen and the failure must stand.

It means any future classifier must require **both**:
1. semantic Gospel-anchor coverage;
2. high-information structural discipline.

Adding this conjunction now to the same holdout would be post-hoc tuning and is prohibited.

It can only be preregistered for a genuinely new holdout.

## Interpretation

### H0

Still insufficient as the sole explanation.

The data contain nontrivial structured similarities.

### HB

Further strengthened.

HB predicts that high-information patterns can arise from:
- prophetic narrative;
- typology;
- explicit Christian composition;
- ordinary mythic structures;
- later intertextual interpretation.

The Isaiah case is especially direct: the source contains the Lord's death/resurrection in Isaiah's **vision**, creating genuine Christological content without making Isaiah the same protagonist.

### HC

Not disproved.

But three increasingly strict tests have now failed to establish a Christ-specific residual signal:

1. SAXO-PACKAGE-1: distinctive but not unique.
2. MDL-CONTROL-1: transferable grammar but not Christ-specific.
3. DISCRIMINATOR-1: high-information structural features still do not separate NH positives from controls.

The burden of the next test is therefore higher.

## Gate verdict

`DISCRIMINATOR-1 = STRUCTURAL_SEPARATION_FAIL / RESIDUAL_HC_SIGNAL_NOT_DEMONSTRATED`

## Next methodological move

Do **not** tune D on these six texts.

The next valid test must use a completely new holdout and preregister a conjunction of two already-developed components:

- the pre-existing nine Gospel semantic complexes;
- the frozen DISCRIMINATOR-1 structural dimensions.

Working name:

`JOINT-HOLDOUT-1`

The hypothesis to test:
a genuine Christ-reflection should score highly on **both** Gospel-specific semantic coverage and structural discipline, whereas generic prophecy, imitatio Christi or analogy should often score highly on only one axis.

This joint criterion must be frozen before selecting/scoring the next holdout.
