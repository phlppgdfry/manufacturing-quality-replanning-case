# ADR-03 — Verklaarbare haalbaarheid vóór optimalisatie

Status: vastgesteld als portfolio-ontwerp, 17 oktober 2026. Geen besluit van echte stakeholders.

## Context
Planner heeft een uitvoerbare keuze nodig, geen magische optimale lijst.

## Opties
A: globale APS-solver; B: eerste vrije slot per geschikte lijn, vaste rangorde; C: vrij starttijdveld.

## Besluit en reden
B. Tijdige opties eerst, dan weinig nieuwe productie, dan vroeg einde.

## Consequenties en risico
Geen globale optimaliteit; bestaande orders worden niet verplaatst. Controle telt conservatief in hetzelfde slot. Een aparte labkalender en materiaalbeschikbaarheid zijn vervolgonderzoek.

## Beslisbevoegdheid
Planning owner, PO bepaalt scope.

## Wanneer herzien
Bij veel gekoppelde lijnen, omstellingen en tijdvensters eerst APS-standaard onderzoeken.

## Trace en validatie
R-05/R-06; UAT-05/UAT-06/UAT-07. Zie [acceptatiegevallen](../06-validation/test-strategy.md) en de uitvoerbare domeintests.

Terug: [besluitenregister](README.md).
