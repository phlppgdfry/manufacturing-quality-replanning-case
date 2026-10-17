# Batchline — het volledige verhaal

Een onafhankelijke, AI-ondersteunde portfoliocase over een fictieve fabrikant. De case volgt het werk van een functioneel analist van onduidelijke vraag tot toetsbare oplossing en beheerste releasevoorwaarden.

## 1. De vraag achter de vraag
“Kwaliteit houdt orders tegen” klinkt als een verzoek om sneller vrij te geven. De discovery onderzoekt eerst wie welke feiten nodig heeft om een besluit te nemen. Leverdruk maakt productconformiteit niet anders. Daarom is het centrale probleem de ontbrekende verbinding tussen kwaliteit, capaciteit en ERP-bevestiging. [Discovery](docs/01-discovery/discovery.md)

## 2. Een concreet conflict
Een order vraagt 100 m², waarvan 40 geblokkeerd. De gesimuleerde stakeholders willen andere dingen: Sales wil de levering halen, Kwaliteit wil bewijs, Planning wil een vrije slot en Operator wil niet dubbel invoeren. Het besluit verdeelt verantwoordelijkheid: Quality lead beslist over materiaal, Planner over herstelcapaciteit en Sales over nieuwe klantbelofte. [Specificatie](docs/02-requirements/functional-specification.md)

## 3. Van betekenis naar regels
Het standaardbesluit 10 vrij, 20 herwerk, 10 afkeur laat een lokaal tekort van 30 over. Herwerk is nog niet vrijgegeven. Nieuwe productie wacht op herkeuring. Een gereedmelding verandert dus geen kwaliteitsoordeel. Iedere overgang heeft een actor, hoeveelheidcontrole en versie. [Proces](docs/03-processes/process-design.md)

## 4. Een ongemakkelijke maar juiste uitkomst
Het beschikbare uur tussen opdrachten is te kort als omstellen en controle worden meegeteld. De alternatieven vallen later op de dag en halen het oorspronkelijke levermoment niet. De applicatie maakt dit zichtbaar; ze verzint geen capaciteit. De planner moet Sales betrekken of een expliciet vervolgscenario voor herschikking starten. [Planning](docs/04-solution/planning.md)

## 5. ERP-standaard eerst
Voor een echte implementatie wordt eerst aangetoond welke inspectie-, productie- en planningsfuncties het bestaande ERP al biedt. SAP-documentatie is referentiecontext; er is geen aangesloten SAP-omgeving. De workbench is pas een verantwoorde uitbreiding als een standaardgap bewezen is. Voorraad en boekingsdocumenten blijven in ERP. [Fit-gap](docs/05-erp/fit-gap.md)

## 6. Vertrouwen in de overdracht
Een timeout kan optreden nadat het ERP al verwerkt heeft. Daarom behoudt een bericht dezelfde sleutel bij herhaling. Een ontvangstregister herkent duplicaten; oudere snapshots mogen een nieuwere stand niet terugdraaien. Lokale vrijgave en administratieve bevestiging zijn afzonderlijke signalen. De simulator bewijst dit gedrag, geen echte ERP-transactie. [Integratie](docs/05-erp/integration-design.md)

## 7. Validatie en gecontroleerde invoering
Tests richten zich op hoeveelheden, rollen, versies, capaciteit, idempotentie en herstel. Businessacceptatie vraagt daarnaast echte key users en een sandbox. De pilot start klein met nulmeting, schaduwmodus, expliciete go/no-go en rollback die boekingen niet heimelijk terugdraait. [Teststrategie](docs/06-validation/test-strategy.md) en [uitrol](docs/07-delivery/rollout.md)

## 8. Een eerlijk investeringsadvies
Vrijgespeelde afstemtijd is niet automatisch cash. Op de illustratieve invoer is tijdwaarde alleen onvoldoende om maatwerk te rechtvaardigen. Het advies is standaard eerst, extensie beperken en pilotdata verzamelen. Dit is juist een resultaat van goede analyse: ook kunnen adviseren om niet te bouwen. [Businesscase](docs/09-value/business-case.md)

## Wat deze case toont
De analyse verbindt bedrijfsbehoefte, proces, systeemgrenzen, exacte regels, tests, delivery en beheer. Ze toont geen echte stakeholderworkshops, SAP-implementatie, productcertificatie, gebruikersacceptatie of gerealiseerde besparing. De persoonlijke beheersing van de kandidaat moet afzonderlijk worden getoetst. [Bewijsmatrix](EVIDENCE.md)
