# FORENSIC-IDENTITY-1A — Hamlet names and family graph

Status: **CLOSED / significant concrete result**  
Case: `CASE-001 Amleth/Hamlet ↔ Jesus/Andronicus`  
Date: 2026-09-21

## Verdict

`CORE_KINSHIP_OVERLAP_PASS / ONE_TO_ONE_IDENTITY_FAIL / NAME_CORROBORATION_WEAK / LATE_LAYER_DEPENDENCE_HIGH`

This is not a verdict on the entire anti-Gospel hypothesis.

It is a concrete forensic result about the first identity layer:
- the Herod/brother's-wife/victim complex is genuinely relevant;
- but the core four-person family graph does not preserve one-to-one identity;
- much of the apparent match is recovered only by fusing Philip with John and Herodias with Mary;
- the strongest explicit NH name arguments depend on names introduced only in Shakespeare, not present in Saxo.

## 1. Source family graph

Internet Shakespeare Editions summarizes Saxo's source narrative:

- Horwendil and Feng are brothers.
- Horwendil marries Gurutha/Gerutha.
- Their son is Amleth.
- Feng murders his brother Horwendil.
- Feng takes the widowed Gurutha as wife.

Source:
https://internetshakespeare.uvic.ca/doc/Ham_Sources/complete/index.html

Schematic:

```
Horwendil ── brother ── Feng
    │                   │
 husband              kills
    │                   │
 Gerutha ── later wife ─┘
    │
  mother
    │
 Amleth
    ▲
  father
    │
Horwendil
```

## 2. NH strict mapping

NH explicitly propose:

- Horwendil / Old Hamlet = John the Baptist
- Feng / Claudius = Herod
- Gerutha / Gertrude = Herodias
- Amleth / Prince Hamlet = Christ

NH source:
https://knigalit.ru/avtori/gleb-nosovskiy/book75495/chitat/

Apply this as a strict one-person-to-one-person map to six selected core relation edges:

| Source relation | Strict NH target relation | Preserved? |
|---|---|---|
| Horwendil brother of Feng | John brother of Herod | no |
| Horwendil husband of Gerutha | John husband of Herodias | no |
| Feng kills Horwendil | Herod kills John | **yes** |
| Feng marries Gerutha | Herod marries Herodias | **yes, broad relation** |
| Horwendil father of Amleth | John father of Jesus | no |
| Gerutha mother of Amleth | Herodias mother of Jesus | no |

Thus the strict map preserves only **2 of 6** selected central relation types.

This is not a probability estimate; it is a graph-consistency audit.

## 3. Why the resemblance still feels strong

The Gospel Herodias complex contains a different but nearby graph:

- Herodias is/was the wife of Herod's brother Philip.
- Herod takes/marries Herodias.
- John condemns this union.
- Herod arrests and ultimately executes John.

Working Gospel reference:
https://www.biblegateway.com/passage/?search=Mark+6%3A17-29

This creates a striking **crossed alignment**.

To preserve the Saxo relations:

### Horwendil must split

For kinship:
`Horwendil -> Philip`

because Philip is Herod's brother and Herodias's husband.

For victim role:
`Horwendil -> John the Baptist`

because John is the man killed by Herod in the Herodias conflict.

### Gerutha must split

For marital triangle:
`Gerutha -> Herodias`

For motherhood of the Christ figure:
`Gerutha -> Virgin Mary`

With these two role fusions, five of the six selected source edges can be approximately reconstructed:

1. brother edge through Philip;
2. first-husband edge through Philip;
3. murder edge through John;
4. second-union edge through Herodias;
5. mother-of-hero edge through Mary.

The remaining edge:
`Horwendil father of Amleth`
has no corresponding John/Philip → Jesus relation.

This is the main forensic finding.

The resemblance is real, but it is produced by **conflating two Gospel men into one Saxo man and two Gospel women into one Saxo woman**.

That supports a possible literary-composite model much more naturally than a strict one-to-one biographical duplicate.

## 4. NH themselves use this kind of identity multiplicity

The multiplicity is not inferred only by this audit.

NH later reuse Gertrude as:
- Herodias;
- Virgin Mary;
- Mary Magdalene;
- in a death scene, Lucretia / Dormition of Mary.

Their Hamlet chapter also maps:
- Rosencrantz + Guildenstern -> Judas;
- Laertes -> Judas again;
- Polonius -> Pontius Pilate;
- Ophelia -> the adulteress and later Procla;
- Prince Hamlet -> Christ, but a later NH reconstruction also lists Prince Hamlet partially among John-the-Baptist reflections.

Sources:
https://knigalit.ru/avtori/gleb-nosovskiy/book75495/
https://history.wikireading.ru/amp163034
https://history.wikireading.ru/amp163030
https://history.wikireading.ru/84189

Therefore the proposed decoder is not a bijection:

`source person -> one historical person`

It is a scene-dependent many-to-many mapping.

Again, this does not refute a composite anti-Gospel hypothesis. It changes what must be demonstrated: one now needs evidence that the **same fusion rules recur predictively**, not merely that suitable roles can be reassigned scene by scene.

## 5. Earlier source vs Shakespeare-added names

Internet Shakespeare Editions explicitly distinguishes what is inherited from Saxo and what Shakespeare supplies.

In Saxo:
- the young woman corresponding to Ophelia is unnamed;
- the spying counsellor corresponding to Polonius is unnamed;
- the two escorts corresponding to Rosencrantz and Guildenstern are unnamed;
- there is no Laertes revenge character comparable to Shakespeare's Laertes.

Shakespeare names and expands these roles.

ISE also notes that Rosencrantz and Guildenstern are names of sixteenth-century Danish aristocracy and are absent from Shakespeare's sources.

Source:
https://internetshakespeare.uvic.ca/doc/Ham_Sources/complete/index.html

This gives a crucial provenance rule:

**a Shakespeare-only proper name cannot count as independent confirmation from Saxo.**

At most, it can support a hypothesis about Shakespeare's later adaptation.

## 6. Ophelia name test

NH propose a phonetic clue:

- `OFELIA`
- substitute `F -> B`
- extract `BL`
- connect to Russian `blud` / adulteress.

NH explicitly add that this observation has no independent weight.

Source:
https://history.wikireading.ru/amp163014

Forensic problems:

1. Saxo's corresponding young woman is unnamed.
2. The derivation is not a normal whole-name transformation; it selects a consonantal fragment after substitution.
3. An independent literary provenance exists: scholarship has proposed that the name Ophelia may derive from Sannazaro's *Arcadia*.

Source:
https://www.jstor.org/stable/j.ctt1dszwps.10

Verdict:
`ONOMASTIC_WEAK + LATE_LAYER`

## 7. Polonius name test

NH explicitly compare:

`POLONIUS -> PLN`

with

`PILATE PONTIUS -> PLT PNT`

and judge the consonant sets close after vowel removal, permutations and repetitions.

NH source:
https://history.wikireading.ru/amp163037

Forensic problems:

1. Saxo's corresponding counsellor is unnamed.
2. Shakespeare's First Quarto calls the figure **Corambis**, not Polonius.
3. Therefore a cryptographic argument from the exact string `Polonius` is version-dependent.
4. Independent Shakespeare scholarship has long investigated a Polish/Polonian provenance; `Polonius` is Latin for Polish/Pole and has been linked, though not unanimously, with contemporary Polish material and *The Counsellor*.

Sources:
https://www.cambridge.org/core/books/abs/shakespeare-in-europe/bad-quarto-hamlet-and-the-polish-connection/3EE697BD91CDD39826CC257E5A636FF5
https://www.researchgate.net/publication/362412965_Polacks_Polonius_and_a_Polonian_pun_Polish_historical_and_historic_aspects_in_a_Shakespearean_tragedy

Verdict:
`ONOMASTIC_WEAK + LATE_LAYER + VERSION_DEPENDENT`

## 8. Rosencrantz and Guildenstern

NH map both men to a single Judas figure.

But the two escorts are unnamed in Saxo. Shakespeare gives them Rosencrantz and Guildenstern, names that ISE identifies with aristocratic sixteenth-century Denmark.

Source:
https://internetshakespeare.uvic.ca/doc/Ham_Sources/complete/index.html

There is no useful onomastic bridge to Judas in this argument.

Thus:
- their **function** as compromised companions may be compared with Judas;
- their **names** provide no early independent Gospel signal.

Verdict:
`FUNCTIONAL_PARALLEL / NAME_CORROBORATION_NONE / LATE_LAYER`

## 9. Laertes

NH explicitly call Laertes a second reflection of Judas.

Source:
https://history.wikireading.ru/amp163030

But Laertes is one of Shakespeare's major additions to the inherited story; ISE notes that Shakespeare adds Laertes and thereby creates a three-son revenge architecture.

Source:
https://internetshakespeare.uvic.ca/doc/Ham_Sources/complete/index.html

NH thus obtain at least two Judas realizations in one play:
- Rosencrantz + Guildenstern -> Judas;
- Laertes -> Judas.

This is `ROLE_SPLIT`, not one-to-one identity.

## 10. Name-evidence summary

For the central four-person identity:

| Source | NH target | direct name support |
|---|---|---|
| Amleth/Hamlet | Christ/Andronicus | none identified |
| Horwendil/Old Hamlet | John Baptist | none direct |
| Gerutha/Gertrude | Herodias / Mary | none |
| Feng/Claudius | Herod | none |

The explicit phonetic/name arguments examined so far are concentrated in Shakespeare-added names:
- Ophelia;
- Polonius.

Both are weak under ordinary forensic criteria and have independent literary/historical provenance candidates.

Thus the **central NH Hamlet case is not primarily an onomastic case**. It is a role/event reinterpretation case.

## 11. Concrete positive result

The audit should not erase the real overlap.

There is a genuinely nontrivial shared complex:

`ruler takes brother's wife + conflict + male victim killed by ruler`

The interesting point is that Saxo compresses the Gospel-side Philip and John roles into Horwendil.

This is exactly the sort of concrete transformation that should now be searched across other claimed duplicates.

If the same fusion pattern repeatedly appears independently — e.g. one source figure systematically combining the kinship-role and victim-role of two prototype persons — that would be strong evidence for a reproducible literary transformation.

If every case requires a different fusion, the model becomes less constrained.

## Gate result

`FORENSIC-IDENTITY-1A = CORE_KINSHIP_OVERLAP_PASS / ONE_TO_ONE_IDENTITY_FAIL / NAME_CORROBORATION_WEAK / LATE_LAYER_DEPENDENCE_HIGH`

## Next tranche

`FORENSIC-IDENTITY-1B`

Concrete object/count chain:

- death letter;
- two companions/guards;
- rewriting/substitution;
- companions die instead;
- gold / thirty silver;
- ship/sea voyage;
- marriage order;
- return.

The question will be whether this highly specific cluster has a stable one-to-one Gospel/Andronicus mapping or again requires source switching and role fusion.
