# ADR-01 — Kwaliteit houdt het vrijgaverecht

Status: vastgesteld als portfolio-ontwerp, 17 oktober 2026. Geen besluit van echte stakeholders.

## Context
Sales wil leverdruk oplossen door Planner te laten vrijgeven.

## Opties
A: Planner mag overrulen; B: Quality lead beslist met escalatie; C: alles blokkeren tot management.

## Besluit en reden
B. Alleen Kwaliteit bepaalt bestemming; Planning beheert capaciteit.

## Consequenties en risico
Meer afstemming en mogelijk vertraging, maar leverdruk verandert productconformiteit niet. Escalatie versnelt beoordeling zonder bevoegdheid te wijzigen.

## Beslisbevoegdheid
Quality lead; Operations owner voor escalatie.

## Wanneer herzien
Bij andere formeel vastgelegde rollen opnieuw RBAC bepalen, nooit impliciet overrulen.

## Trace en validatie
R-02/R-03; UAT-02/UAT-03. Zie [acceptatiegevallen](../06-validation/test-strategy.md) en de uitvoerbare domeintests.

Terug: [besluitenregister](README.md).
