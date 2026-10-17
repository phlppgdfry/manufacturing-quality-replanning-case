# Requirements traceability

Gegenereerd uit [de catalogus](../../data/case.json). Per requirement: regel, acceptatiegeval, KPI en canoniek document. Dit toont artefactdekking, geen kandidaatervaring of echte UAT-sign-off.

| ID | Requirement | Regels | Acceptatie | KPI | Specificatie |
|---|---|---|---|---|---|
| FR-01 | Blokkeer een positieve hoeveelheid binnen de beschikbare voorraad; leg reden, partij en versie vast. | R-01 | UAT-01 | KPI-01 | [Kwaliteitsafwijking registreren](../../docs/02-requirements/functional-specification.md) |
| FR-02 | Alleen Kwaliteit verdeelt de volledige blokkade in vrijgave, herwerk en afkeur met een reden. | R-02,R-03 | UAT-02,UAT-03 | KPI-01 | [Geblokkeerde hoeveelheid beoordelen](../../docs/02-requirements/functional-specification.md) |
| FR-03 | Bereken tekort uitsluitend uit lokaal vrijgegeven product; toon ERP-bevestiging afzonderlijk. | R-04,R-10 | UAT-04 | KPI-02 | [Leverimpact bepalen](../../docs/04-solution/data-model.md) |
| FR-04 | Toon geschikte lijnen met vrije capaciteit, omstel- en controletijd; controleer versies opnieuw bij bevestiging. | R-05,R-06 | UAT-05,UAT-06,UAT-07 | KPI-02 | [Herstelopties vergelijken en bevestigen](../../docs/04-solution/planning.md) |
| FR-05 | Operator meldt gereed; Kwaliteit geeft pas daarna de herstelde en vervangende hoeveelheid vrij. | R-07 | UAT-08,UAT-09 | KPI-01 | [Herstel uitvoeren en opnieuw keuren](../../docs/03-processes/process-design.md) |
| FR-06 | Bewaar berichten in outbox; ontvang met unieke sleutel en inhoudscontrole; oude versies mogen actuele voorraad niet overschrijven. | R-08,R-09 | UAT-10,UAT-11,UAT-12 | KPI-03 | [Voorraadstatus veilig overdragen](../../docs/05-erp/integration-design.md) |
| FR-07 | Na drie mislukte pogingen dead-letter; alleen Integratie mag na diagnose herstarten. | R-11 | UAT-13 | KPI-03 | [ERP-storing herstellen](../../docs/08-operations/runbook.md) |
| FR-08 | Leg actorrol, actie, versie, planreferentie en berichtsleutel vast; productie vereist append-only serveraudit. | R-12 | UAT-14 | KPI-04 | [Besluiten herleiden](../../docs/04-solution/security.md) |
| FR-09 | Bereid businessacceptatie, training, go/no-go, rollback en benefits review voor. | R-13 | UAT-15 | KPI-04 | [Beheerste pilot en feedback](../../docs/07-delivery/rollout.md) |
