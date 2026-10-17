# Batchline — kwaliteit en productieplanning

**Een kwaliteitsblokkade vertalen naar een onderbouwd herstelplan en een bevestigde ERP-status.**

Onafhankelijke, AI-ondersteunde portfoliocase voor een fictieve fabrikant van metalen dak- en gevelpanelen. Alle bedrijfsgegevens en workshops zijn fictief; geen klantimplementatie of SAP-praktijkervaring geclaimd.

[Open demo met rondleiding](site/index.html?tour) · [Start in 2/5/15 minuten](START-HERE.md) · [Bewijs per activiteit](EVIDENCE.md) · [Volledige case](CASE_STUDY.md) · [Samenvatting](application-kit/executive/one-page-summary.md)

## Het probleem
Een order vraagt 100 m². Van de geproduceerde partij is 40 m² geblokkeerd wegens coatingbeschadiging. Kwaliteit, Planning en ERP moeten dezelfde feiten gebruiken, terwijl hun beslisrechten verschillen. De beschikbare herstelcapaciteit haalt de oorspronkelijke leverbelofte niet: de case verbergt die uitkomst niet.

## Het traject
Discovery → requirements → proces → ERP-fit-gap → beslisregels → prototype → acceptatie → pilot → beheer → waarde.

## Wat is uitgewerkt
- Gesimuleerde discovery met conflicterende belangen en besluiten per eigenaar.
- Functionele specificatie met hoeveelheidbalans, rollen, statusmodel en traceability.
- AS-IS/TO-BE als BPMN met DI, een logisch datamodel en eigen OpenAPI-facadeontwerp.
- Werkende domeinregels: gedeeltelijke vrijgave, herwerk, capaciteit, versiecontrole, ERP-duplicaten en veilige herstart.
- Teststrategie, UAT-scenario's, backlog, change request, uitrol, rollback, training en runbook.
- Businesscase die op de gekozen aannames maatwerk niet met tijdsbesparing alleen rechtvaardigt.

## Drie keuzes
1. [Kwaliteit beslist over vrijgave](docs/adr/01-quality-ownership.md), ook bij leverdruk.
2. [Een plan is geen voorraad](docs/adr/02-stock-vs-plan.md): uitvoering, herkeuring en ERP-bevestiging zijn aparte feiten.
3. [Vaste sleutels en versies](docs/adr/04-erp-delivery.md) voorkomen dubbel effect en terugdraaien door oude snapshots.

## Openen en controleren
Node.js 22+ en Python 3.11+. Het prototype heeft geen runtime-afhankelijkheden. De development packages zijn voor validatie en browsertests.

```sh
npm ci
npm run build
npm run check
npm run dev
```

Open http://127.0.0.1:8078/index.html?tour. Gebruik demonstratierol Kwaliteit voor een besluit, Planning voor planbevestiging, Operator voor gereedmelding en Integratie voor ERP-herstel. De rolkiezer is geen echte beveiliging.

```sh
npx playwright install chromium
npm run test:ui
```

Browsertests vereisen een draaiende server op poort 8078. CI start die automatisch. Het sitebestand is statisch te hosten onder een subpad; geen backend of tokens nodig. GitHub Pages is voorbereid, publicatie gebeurt pas na afzonderlijk akkoord.

## Als de demo niet laadt
Open [de statische case](site/case.html) of [fallback-screenshots](docs/screenshots/README.md). De [one-pager](application-kit/exports/one-pager.pdf) en [presentatie](application-kit/exports/deck.pdf) werken offline.

## Repositorykaart
| Pad | Inhoud |
|---|---|
| docs/00-context–09-value | Context, analyse, specs, ERP, validatie, delivery, beheer en waarde |
| docs/adr | Besluiten met alternatieven en herzieningscriteria |
| docs/diagrams | BPMN-bronnen met DI en SVG-renders |
| data/case.json | Canonieke requirements, voorbeeldhoeveelheden en rekenaannames |
| contracts | Eigen OpenAPI-contract en voorbeeldbericht |
| site/assets/domain.mjs | Zuivere domeinregels; dezelfde functies in demo en tests |
| tests en scripts | Domeintests, documentconsistentie, BPMN/OpenAPI en browserchecks |
| application-kit | Samenvatting, casebook, demo's en presentatie |

## Bronnen, data en licenties
[Bronverantwoording](docs/00-context/sources.md). Nieuwe synthetische data; geen bestaande projectrepo gekopieerd. Code MIT, documentatie en eigen data CC BY 4.0. Afhankelijkheden zijn gepind in package-lock.json; geen externe fonts, trackers of runtime-CDN's.

## Grenzen en status
Een browserprototype, geen SAP-, MES- of productiesysteem. Voorraadsnapshots zijn een eigen vereenvoudigd demonstratiemodel, geen officiële SAP-postings. Kindpartijen zijn zichtbaar, volledige fysieke genealogie is niet gebouwd. Gehele m², twee lijnen, één getroffen order, handmatige retryklikken. Geen serverauthenticatie, multi-usertransacties, productiebelasting of eindgebruikers-UAT aangetoond. Lokaal auditspoor is wijzigbaar. De [releasevoorwaarden](docs/07-delivery/rollout.md) blijven verplicht voor een echte implementatie.

De kandidaat moet de AI-ondersteund gemaakte artefacten nog zelfstandig uitleggen, aanpassen en diagnosticeren. Deze case is geen claim van senior werkervaring.
