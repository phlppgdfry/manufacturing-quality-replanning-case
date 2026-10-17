# ADR-02 — Een plan is geen voorraad

Status: vastgesteld als portfolio-ontwerp, 17 oktober 2026. Geen besluit van echte stakeholders.

## Context
Een mooie herplanning kan een order ten onrechte groen maken.

## Opties
A: geplande hoeveelheid meetellen; B: gereedmelding voldoende; C: kwaliteitsvrijgave plus ERP-bevestiging vereist.

## Besluit en reden
C. Elke fase krijgt een apart feit; herstel blijft geblokkeerd tot controle.

## Consequenties en risico
Statusmodel en UI worden iets uitgebreider; onterecht leverbaar product wordt vermeden.

## Beslisbevoegdheid
Quality lead + Inventory owner.

## Wanneer herzien
Bij reservering met expliciet toekomstig ATP een apart beloftesignaal tonen, nooit voorraadstatus vervalsen.

## Trace en validatie
R-04/R-07/R-10; UAT-04/UAT-08/UAT-09. Zie [acceptatiegevallen](../06-validation/test-strategy.md) en de uitvoerbare domeintests.

Terug: [besluitenregister](README.md).
