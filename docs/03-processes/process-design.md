# Procesontwerp: AS-IS, TO-BE en uitzonderingen

Voor Operations owner en analist. De BPMN-bestanden zijn beschrijvende, niet-uitvoerbare modellen met lanes en DI. Procesowner: Operations owner; kwaliteitsbesluiten blijven bij Quality lead.

## AS-IS (fictieve onderzoekshypothese)
Operator meldt afwijking mondeling → supervisor informeert Kwaliteit → beoordeling op aparte lijst → Planner vraagt status → herstel wordt ingeschoven → ERP wordt achteraf bijgewerkt. Pijnpunten: geen gedeelde partijstatus, onvolledige hoeveelheid, onduidelijke versie, besluit/posting niet onderscheiden. Dit is een scenario, geen geobserveerd proces.

## TO-BE
1. Operator registreert partij, hoeveelheid en reden; blokkade wordt zichtbaar.
2. Quality lead bepaalt bestemming van de gehele geblokkeerde hoeveelheid.
3. Applicatie toont tekort en berekent verklaarbare herstelopties.
4. Planner kiest met actuele versie en reden; bij onhaalbare levering stemt Sales de klantbelofte af.
5. Operator meldt herstel gereed; vervangende partij blijft in controle.
6. Quality lead controleert en geeft herstel vrij.
7. Integratie verwerkt outbox, controleert bevestiging en reconcilieert de laatste voorraadstatus.
8. Alleen bevestigde voorraad geeft een leverbaar signaal. Transport blijft buiten de prototype-uitvoering.

## Statussen (verschillende objecten)
| Object | Overgang | Wie / voorwaarde |
|---|---|---|
| Afwijking | open → rework of closed | Quality lead; geldige verdeling |
| Herstelplan | geen → committed | Planner; actueel haalbaar voorstel |
| Herstelplan | committed → awaiting-quality | Operator; uitvoering gereed |
| Herstelplan | awaiting-quality → complete | Quality lead; bevinding ingevuld |
| Bericht | pending → retry → dead-letter | Integratie; maximaal drie pogingen |
| Bericht | pending/retry → acked of superseded | Ontvangstregister bevestigt of nieuwer snapshot bestaat |

## Uitzonderingspaden
Onvolledige melding terug naar melder. Geen kwaliteitsbesluit: wacht en escaleer naar Quality lead, nooit automatisch vrijgeven. Geen vrije capaciteit: geen voorstel fabriceren; Planner bespreekt nieuwe leverafspraak met Sales. Versie gewijzigd: opnieuw vergelijken. Bericht niet bevestigd: replay op dezelfde sleutel. Langdurige storing: lokaal blokkades beheren volgens gecontroleerde noodprocedure, geen onbevestigde verzending.

In de BPMN is “ERP-overdracht bevestigd?” een expliciete gateway met diagnose/herhaling als teruglus. De uitgebreide technische idempotentie staat in het integratieontwerp. Het getekende proces toont het herwerkpad; de variant volledige vervanging gebruikt hetzelfde controlepunt, met restherwerk als apart open werkpakket.

Modellen: [AS-IS BPMN](../diagrams/as-is.bpmn), [TO-BE BPMN](../diagrams/to-be.bpmn), [TO-BE SVG](../diagrams/to-be.svg). Het model is importeertestbaar; er wordt geen uitvoerbare workflow-engine geclaimd.

Vorige: [Requirements](../02-requirements/functional-specification.md). Volgende: [Architectuur](../04-solution/architecture.md).
