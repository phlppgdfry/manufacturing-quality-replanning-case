# ADR-05 — ERP-standaard vóór eigen voorraadlogica

Status: vastgesteld als portfolio-ontwerp, 17 oktober 2026. Geen besluit van echte stakeholders.

## Context
Een nieuwe workbench kan bestaande ERP/QMS-functies dupliceren.

## Opties
A: volledig eigen ERP bouwen; B: standaard configureren; C: beperkte cross-role extensie.

## Besluit en reden
B onderzoeken vóór C. Prototype C bewijst functionele regels, niet dat maatwerk nodig is.

## Consequenties en risico
Fit-gap en sandboxspike kosten tijd maar verminderen dubbele voorraadwaarheid.

## Beslisbevoegdheid
ERP owner + PO; Quality lead tekent procesfit.

## Wanneer herzien
Alleen bij bewezen standaardgap en beheersbare integratie C doorzetten.

## Trace en validatie
FR-06/FR-09; fit-gap en sandbox-gate. Zie [acceptatiegevallen](../06-validation/test-strategy.md) en de uitvoerbare domeintests.

Terug: [besluitenregister](README.md).
