# FORENSIC IDENTITY MATRIX v1

Purpose: test concrete historical/literary identity claims case-by-case rather than relying on aggregate motif scores.

## Units

Each dossier separates four evidence layers:

1. **PERSON** — proposed identity of named/unnamed actors.
2. **RELATION** — family, political, killer/victim, teacher/disciple and other edges.
3. **NAME** — proper-name continuity or a proposed phonetic/orthographic transformation.
4. **PROVENANCE** — whether a feature is inherited from an earlier witness or introduced only in a later retelling.

## Required labels

For every proposed correspondence record:

- `EXACT` — same relation/function without extra role reassignment.
- `PARTIAL` — real overlap but with a material mismatch.
- `ROLE_FUSION` — one source actor must represent two or more target actors to preserve different edges.
- `ROLE_SPLIT` — one target actor is represented by multiple source actors.
- `LATE_LAYER` — feature is absent from the earlier source and introduced in a later retelling.
- `ONOMASTIC_WEAK` — name claim requires permissive consonant deletion/reordering/substitution or has strong alternative provenance.
- `CONTRADICTION` — a central relation cannot be preserved under the proposed one-to-one identity.
- `UNRESOLVED` — evidence currently insufficient.

## Core rule

A historical identity map should first be tested as a function:

`source_person -> target_person`

before allowing composites.

If a good match requires:

`source_person -> {target_1, target_2, ...}`

the dossier must show this explicitly rather than hiding it inside scene-by-scene interpretation.

A composite literary hypothesis may still permit role fusion, but it is a different and weaker claim than one-to-one biographical identity.

## Name rule

Name similarity is independent evidence only when:

- the name exists in the earlier source;
- the transformation is specified before the comparison or has ordinary linguistic support;
- a plausible independent source for the later name is not ignored.

A Shakespeare-only name cannot count as independent corroboration from Saxo.

## Current case

`CASE-001 / FORENSIC-IDENTITY-1A: Amleth-Hamlet ↔ Jesus/Andronicus`

This first tranche covers:
- central family/identity graph;
- name provenance;
- multiplicity of NH person mappings.

Later tranches will cover concrete objects, numbers, letter, companions, money, voyage, geography and death mechanics.
