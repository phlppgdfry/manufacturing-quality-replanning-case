# ADR-04 — Herhaling zonder dubbel effect

Status: vastgesteld als portfolio-ontwerp, 17 oktober 2026. Geen besluit van echte stakeholders.

## Context
Een timeout zegt niet of het ERP al verwerkt heeft.

## Opties
A: nieuwe sleutel per poging; B: at-most-once; C: duurzame outbox, vaste sleutel en ontvangstregister.

## Besluit en reden
C. At-least-once delivery, idempotent effect, oudere snapshots erkend zonder terugdraaien.

## Consequenties en risico
Meer opslag en beheer; nodig voor onbekende uitkomst. Complete snapshots in de simulator zijn geen SAP-postings.

## Beslisbevoegdheid
Integration lead + ERP owner.

## Wanneer herzien
Bij officiële ERP-idempotentie daarop aansluiten, met dezelfde effectgaranties en documentcontrole.

## Trace en validatie
R-08/R-09/R-11; UAT-10/UAT-11/UAT-12/UAT-13. Zie [acceptatiegevallen](../06-validation/test-strategy.md) en de uitvoerbare domeintests.

Terug: [besluitenregister](README.md).
