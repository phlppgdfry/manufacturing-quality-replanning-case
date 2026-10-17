# Bronnen en herkomst

Voor lezers die feiten, aannames en ontwerp van elkaar willen scheiden. Werkgeverspecifiek onderzoek staat uitsluitend in het privédossier; deze case beschrijft geen intern systeem van een bestaande onderneming.

## Technische referenties
- [SAP ERP: usage decision](https://help.sap.com/docs/SAP_ERP/250374f0514e4e0f9057066374265eba/6440b853dcfcb44ce10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=6.18.latest): kwaliteitsbesluit bij productie-inspecties. Geraadpleegd via Context7 op 17 oktober 2026.
- [SAP ERP: quality management process](https://help.sap.com/docs/SAP_ERP/248c3cdd7e6548999a7f5b95118f4522/328dbf53f106b44ce10000000a174cb4.html?locale=en-US&state=PRODUCTION&version=6.18.latest): inspecties en voorraadbestemming na kwaliteitsbesluit.
- [OMG BPMN 2.0.2](https://www.omg.org/spec/BPMN/2.0.2/): modelnotatie, lanes, gateways en diagram interchange.
- [OpenAPI 3.1.0](https://spec.openapis.org/oas/v3.1.0): ontwerpcontract van de eigen ERP-facade, geen officiële SAP-API.
- [Scrum Guide](https://scrumguides.org/scrum-guide.html): Product Owner prioriteert; de analist verduidelijkt gedrag, afhankelijkheden en acceptatie. De analist is geen afzonderlijke verplichte Scrum-rol.

- [RFC 9110, If-Match](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1): een niet voldane HTTP-preconditie wordt onderscheiden van een zakelijk conflict; het facadeontwerp gebruikt daarvoor 412. Geraadpleegd 17 oktober 2026.

## Interpretatiegrens
De SAP-bronnen beschrijven ERP-documentatie; ze bewijzen geen specifiek SAP-product, release, configuratie of modulegebruik bij een werkgever. De simulator gebruikt een vereenvoudigd dossier-snapshotmodel. Een kwaliteitsbesluit is niet hetzelfde als een voorraadboeking. De mapping naar inspectielot, voorraadstatus en boekingsdocument moet in de doelomgeving worden onderzocht en getest.

## Data en auteurschap
Alle oefendata zijn nieuw gegenereerd. Geen persoonsgegevens, klantdata, logo's of technische interne documentatie gebruikt. De case en code zijn met AI uitgewerkt op verzoek van de kandidaat. Een uitgewerkt artefact is geen bewijs dat de kandidaat dit zelfstandig beheerst.

Code: MIT. Documentatie en eigen oefendata: CC BY 4.0. Het conceptbeeld is AI-gegenereerd voor dit project; er wordt geen bestaand bedrijfsmerk gereproduceerd. Het prototype gebruikt alleen browser-API's en eigen code, geen runtime-CDN's of trackers.
