# Backlog, refinement en projectopvolging

Voor PO, analist en Scrum-team. Dit is een uitgewerkte planningssimulatie; geen echt uitgevoerd Scrum-project. PO prioriteert; het team schat en kiest sprintcapaciteit.

## Twee increments en releasevoorwaarden
Sprint 1-doel: één partij van blokkade tot onderbouwd kwaliteitsbesluit en zichtbare leverimpact. Stories FR-01/02/03/08, schema spike en begrippenbaseline. Demonstratie: foutieve hoeveelheid en onbevoegde vrijgave worden geweigerd. Geen release naar echte voorraad.

Sprint 2-doel: verklaarbare herstelkeuze, herkeuring en veilige ERP-overdracht. Stories FR-04/05/06/07, contractreview, runbook en reconciliatie. SAP-sandboxspike is een afhankelijkheid; integratie kan niet Done worden verklaard op browsertests alleen. FR-09 loopt over beide increments.

## Refinement-log (gesimuleerd)
| Vraag | Verduidelijking | Effect |
|---|---|---|
| Developer: is ready hetzelfde als vrij? | Nee; gereed creëert inspectievoorraad | FR-05 krijgt tweede Quality-stap |
| Tester: wat als timeout na ERP-boeking? | Bericht met dezelfde sleutel opnieuw verwerken | UAT-10 en ontvangstregister |
| Planner: mag ik gewoon een eerdere start intypen? | Nee; model bepaalt haalbare slots, commit controleert versies | FR-04 en R-06 |
| PO: waarom geen automatische beste keuze? | Klantbelofte, restherwerk en ploegrealiteit vragen menselijk besluit | ADR-03 |

## CR-01: “Maak prioriteitsklanten automatisch vrij”
Aanvraag van fictieve Sales lead na eerste demo. Impact: functiescheiding wordt doorbroken, kwaliteit kan onterecht beschikbaar lijken. Opties: A automatisch vrijgeven (afwijzen); B kwaliteitsbeoordeling escaleren met duidelijk tijdstip en zichtbare leverimpact (aanbeveling); C leverbelofte verruimen na afstemming. Beslisser: Quality lead voor bevoegdheid, PO voor backlogprioriteit, Sales voor klantafspraak. Acceptatie van B vraagt een aparte notificatie/SLA-story; niet stil toevoegen aan deze baseline.

## Voorbeeldstatusrapport (gesimuleerde projectweek 2)
Doel: requirements en ERP-fit-gate afronden. Groen: begrippen, regels en domeinprototype. Amber: SAP-interface en inspectielotmapping nog te bewijzen. Rood voor productie: key-user-UAT en recovery drill ontbreken. Besluit gevraagd: ERP-consultant één dag voor sandboxspike. Volgende mijlpaal: integratiekeuze pas na spike. Scopewijziging CR-01 afgewezen voor automatische vrijgave; escalatie apart prioriteren.

## RACI
Quality lead A voor bestemming; planner R/A voor operationeel herstelplan binnen afgesproken kaders; operator R voor melding en uitvoering; analist R voor specificatie/trace en C voor procesbesluiten; developer R voor implementatie; ERP owner A voor integratie-/boekingsfit; PO A voor prioriteit; Operations owner A voor pilot-go/no-go. Niet één persoon overal verantwoordelijk maken.

Vorige: [Teststrategie](../06-validation/test-strategy.md). Volgende: [Uitrol](rollout.md).
