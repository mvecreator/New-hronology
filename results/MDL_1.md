# MDL-1 — Selector entropy correction

Status: **CLOSED / significant result**  
Date: 2026-09-21

## Gate verdict

`RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

The fixed 54-claim sample does show saturation of named transformation families, but that saturation is not sufficient to establish compression once selector freedom is charged.

The correct conclusion is deliberately narrower than a hard fail:
- a reusable grammar exists at a coarse level;
- its apparent compression is not robust to conservative selector/order costs;
- therefore the current evidence does not establish a low-description-length hidden code.

## Fixed sample

The sample was not changed during selector correction:

- Hamlet / Amleth: 22 claims
- Faust: 16 claims
- Eulenspiegel: 10 claims
- Don Juan: 6 claims
- total: 54 claims

Machine-readable coding:
`data/mdl1_claims.csv`

Reproduction script:
`scripts/mdl_selector_entropy.py`

## Frozen local operation costs

Retained from v0.1:

- `role_swap = 1`
- `event_substitution = 1`
- `order_break = 1`
- `metaphoric_jump = 1`
- `source_jump = 1`
- `new_rule = 1.5`

The original flat calculation yielded:

- total local cost = 98.5
- direct claims = 14
- F0.1 claims = 21
- claims requiring a non-F0.1 rule = 19
- new-rule-family sequence by publication corpus = `8 → 1 → 1 → 1`

This saturation remains a real observation.

## Correction 1 — dictionary cost must be paid once per family

The previous local score charged `new_rule=1.5` per claim even when the same new family was reused.

MDL requires separating:
- dictionary cost: define a transformation family once;
- invocation/residual cost: specify what that family means in the present claim.

The 19 non-F0.1 invocations collapse to 11 new families:

- N1 rite → information transfer
- N2 body-cut/birth ↔ writing composite
- N3 payment → treasure/payment object
- N4 physical detail → whole event
- N5 intermediate duplicate supplies event
- N6 topography/object substitution
- N7 iconic object identity
- N8 loose official-role chain
- N9 proximity → personal participation
- N10 lexical/semantic inversion
- N11 adversarial role reversal

Together with six frozen F0.1 families this gives 17 transformed families.

## Correction 2 — selector entropy

A broad rule is not free merely because it can be named briefly.

Example:
`iconically similar object → sacred object`
compresses many mappings into one rule name, but leaves a large choice of which object maps to which sacred object.

For each family we therefore assign a deliberately conservative lower bound on the number of admissible outputs.

Frozen lower-bound fanouts:

- R1 >= 4 → 2 bits
- R2 >= 4 → 2 bits
- R3 >= 2 → 1 bit
- R4 >= 4 → 2 bits
- R5 >= 4 → 2 bits
- R6 >= 3 → log2(3) = 1.585 bits
- N1 >= 8 → 3 bits
- N2 >= 16 → 4 bits
- N3 >= 8 → 3 bits
- N4 >= 16 → 4 bits
- N5 >= 16 → 4 bits
- N6 >= 16 → 4 bits
- N7 >= 16 → 4 bits
- N8 >= 16 → 4 bits
- N9 >= 16 → 4 bits
- N10 >= 8 → 3 bits
- N11 >= 8 → 3 bits

Every explicit external-source jump adds only a **minimum one bit**, corresponding to a binary choice. This is intentionally conservative.

Direct claims receive zero selector cost.

Result:

`selector lower bound = 113.0947 bits`

by corpus:

- Hamlet: 51.7549 bits / 22 claims = 2.3525 bits per claim
- Faust: 24.5850 / 16 = 1.5366
- Eulenspiegel: 24.1699 / 10 = 2.4170
- Don Juan: 12.5850 / 6 = 2.0975

The key result is that selector cost does **not** collapse after family saturation.

## Correction 3 — order freedom

The Eulenspiegel analysis explicitly states that the Folk Book contains 95 chapters, that the stories are only loosely connected and in essentially arbitrary order, and that the analysis will treat them separately rather than preserve Gospel order.

This introduces a genuine permutation degree of freedom.

Because the exact correct order penalty is debatable, MDL-1 does not freeze a single value. It reports sensitivity:

- no order charge: 0 bits
- conservative seven-item order: `log2(7!) = 12.2992 bits`
- full ten-claim order: `log2(10!) = 21.7911 bits`

The important point is not that 10! must be the final answer. The important point is that order freedom cannot have zero information cost if preservation of narrative order is part of the HC claim.

Working NH source:
https://wron.wordpress.com/2022/09/07/%D1%83%D0%BB%D0%B5%D0%BD%D1%88%D0%BF%D0%B8%D0%B3%D0%B5%D0%BB%D1%8C-%D0%B8-%D0%B3%D1%83%D0%BB%D0%BB%D0%B8%D0%B2%D0%B5%D1%80-%D0%B0%D0%BD%D1%82%D0%B8-%D0%B5%D0%B2%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D0%B8/

## Bit calibration

To avoid silently treating one local operation unit as one bit, the script uses:

`1 operation unit = log2(6) = 2.58496 bits`

This is deliberately favorable to grammar reuse: a larger bit value per operation increases the amount saved when several exact mappings are replaced by one family.

## Independent cheap baseline

The comparator deliberately makes independent mappings cheap.

Every transformed claim is allowed its own exact rule and pays only the already-frozen `1.5` new-rule charge.

There are 40 transformed claims.

With 70 structural operation units:

`L_independent = (70 + 1.5×40) × log2(6)`

`L_independent = 336.0451 bits`

This comparator does not attempt to assign a realistic semantic description length to 40 unique rules; it is therefore a demanding stress-test for the grammar.

## Full two-part grammar

When all 17 family definitions are charged:

Structural + dictionary portion:

`(70 + 1.5×17) × log2(6) = 246.8639 bits`

Add selector lower bound:

### No order penalty

`L = 359.9587 bits`

Difference from independent baseline:

`+23.9135 bits = +7.12%`

### Seven-item order penalty

`L = 372.2579 bits`

Difference:

`+36.2127 bits = +10.78%`

### Ten-item order penalty

`L = 381.7497 bits`

Difference:

`+45.7046 bits = +13.60%`

Under the full two-part code, the current grammar does not compress the fixed sample.

## Maximally favorable scenario for HC

A stronger concession is also tested:
- treat the six F0.1 families as already learned and free;
- charge only the 11 new N-families;
- optionally give zero order penalty.

Structural + new-family cost:

`(70 + 1.5×11) × log2(6) = 223.5993 bits`

Then:

### F0.1 free, no order penalty

`L = 336.6940 bits`

Baseline:

`336.0451 bits`

Difference:

`+0.6489 bits = +0.19%`

This is effectively a tie and is highly sensitive to coding assumptions.

### F0.1 free, seven-item order

`348.9932 bits`

`+3.85%`

### F0.1 free, ten-item order

`358.4851 bits`

`+6.68%`

Therefore even a maximally favorable treatment does **not** produce a robust compression advantage.

## Prequential check

To separate training from prediction, Hamlet+Faust are treated as training and Eulenspiegel+Don Juan as later holdout.

Holdout:
- 16 claims
- 14 transformed
- only two genuinely new families after training

Cheap independent holdout baseline:

`113.7384 bits`

Grammar with zero order cost:

`103.9639 bits`

This is a genuine apparent compression:

`-8.59%`

However:

- add `log2(7!)` order freedom → `116.2631 bits` = `+2.22%`
- add `log2(10!)` → `125.7550 bits` = `+10.57%`

Thus predictive compression is **order-sensitive**.

This is precisely relevant because the Eulenspiegel analysis explicitly abandons preservation of source/Gospel sequence.

## Break-even sensitivity

For the full dictionary with no order penalty, the selector lower-bound estimate could be reduced to approximately **78.9%** of its frozen value before the grammar begins to compress.

With a seven-item order charge the break-even factor is approximately **68.0%**.

With ten-item order it is approximately **59.6%**.

In the maximally favorable F0.1-free/no-order scenario, the break-even factor is approximately **99.4%**, confirming that the apparent result is essentially a tie.

## Why the Hamlet letter remains diagnostically important

NH's death-letter → Caesarean-birth mapping requires multiple bridges:
- Saxo/Shakespeare death letter;
- Toledot Yeshu secret writing;
- incision in the thigh;
- Caesarean interpretation;
- Tree of Jesse;
- guards of the writing.

The NH text itself explicitly moves across these sources and transformations.

Working claim source:
https://w-shakespeare.ru/library/o-chem-na-samom-dele-pisal-shekspir-ot-gamleta-hrista-do-korolya-lira-ivana-groznogo30.html

This is exactly the kind of case where a short family name such as N2 would create artificial compression unless the selector/source choices are charged.

## Why Faust remains the strongest positive corpus

Faust still has the lowest selector/local cost among the four corpora.

The final supper with students is genuinely close in structure to a Last-Supper/farewell sequence: the same source passage gives the meal, close student group, farewell speech and imminent death.

Working NH chapter:
https://history.wikireading.ru/amp149727

This remains a real positive observation.

But the Faust tradition is also explicitly Christian and moralizing, so low transformation cost does not by itself distinguish HC from HB.

## Don Juan source switching

The NH chapter list explicitly introduces a "second, little-known but very valuable Spanish version" and uses that alternate version for the live return from the tomb.

Working index:
https://knigalit.ru/avtori/gleb-nosovskiy/book3069814/

This is why source/version selection remains a necessary component of the code.

## Interpretation

MDL-1 yields two simultaneous results.

### Positive for the grammar idea

The family vocabulary does saturate:

`8 → 1 → 1 → 1`

and a prequential calculation **without** order cost can compress later texts.

Therefore the idea of a reusable anti-sacral transformation grammar is not empty.

### Negative for a low-cost hidden code

Family saturation does not make selector entropy disappear.

Once even conservative fanout/source choice is charged:
- total-sample compression disappears;
- holdout compression becomes dependent on whether order freedom is priced;
- the best HC-favorable total result is effectively a tie.

Therefore the present data do not demonstrate that the claimed correspondences are generated by a compact hidden code rather than by a broad reusable hermeneutic grammar.

## Effect on hypotheses

- **H0:** still insufficient by itself.
- **HB:** remains strong; broad literary/Christian inversion rules naturally predict reusable families with selector freedom.
- **HC:** not excluded; however HC has not yet shown robust MDL superiority.

## Gate verdict

`MDL-1 = RULE_FAMILY_SATURATION_PASS / ROBUST_COMPRESSION_NOT_DEMONSTRATED`

This is not equivalent to `HC=false`.

It means the next test must be comparative.

## Required next gate

**MDL-CONTROL-1**

Run the same frozen grammar and selector accounting on negative controls.

The decisive question is no longer:

"Can the NH corpus be compressed?"

but:

"Does the NH corpus compress substantially better than matched non-HC literary/control corpora under the same code?"

Only differential compression can distinguish a special anti-Gospel code from a generic analogy engine.
