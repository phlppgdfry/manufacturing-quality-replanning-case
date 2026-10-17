# ERP-integratie: contract, volgorde en herstel

Voor developer, ERP-consultant en support. [OpenAPI](../../contracts/openapi.json) beschrijft een eigen facade. Het is geen SAP-API en er draait geen HTTP-backend achter de publieke demo.

## Eigenaarschap en berichttypen
| Data | Bron → doel | Trigger | Foutafhandeling |
|---|---|---|---|
| Order, partij, product, machinekalender | ERP/MES → workbench | Snapshot/event, frequentie na spike | Versie vastleggen; ontbrekende masterdata blokkeert voorstel |
| Kwaliteitsbesluit | Bevoegde kwaliteitstransactie → ERP | Expliciet besluit | Transactionele outbox; geen levering vóór bevestiging |
| Herstelplan | Planning → ERP/MES | Planner bevestigt | Optimistic concurrency; ERP-acceptatie vereist |
| Voorraadbevestiging | ERP → workbench | Posting/receipt | Boekingsreferentie en reconciliatie |

Doel: één databasecommit schrijft besluit én outbox. Worker levert at-least-once. Unieke sleutel is dossier-ID + versie; payload wordt inhoudelijk gefingerprint. Zelfde sleutel/inhoud geeft hetzelfde resultaat; andere inhoud geeft 409. Een ouder compleet snapshot wordt als superseded erkend, zonder actuele voorraad terug te draaien. Delta-boekingen kunnen dit niet overnemen: die vragen eigen effect-ID's en boekingsdocumentcontrole.

## Afwijking tussen doel en simulator
De simulator verstuurt complete dossierbalansen, bewaart alle sleutels en gebruikt een apart ontvangstregister in dezelfde browser. Hij test idempotentie, niet echte netwerkduurzaamheid of SAP-boeking. De “ERP” past een projectie toe. In productie vertaalt een adapter een kwaliteitsbesluit naar ondersteunde ERP-acties, legt documentreferenties vast en controleert de resulterende voorraad. Geen blind voorraad-snapshot naar SAP boeken.

## Statuscodes en herstel
200: ontvangen, duplicate of oude versie erkend met expliciete uitkomst. 400: schema/hoeveelheid onjuist. 401/403: ontbrekende authenticatie/bevoegdheid. 409: sleutelconflict of een actief herstel dat een nieuw plan blokkeert. 412: niet voldane If-Match-voorwaarde; ververs dossier en voorstel vóór opnieuw bevestigen. 429/503: tijdelijke storing, respecteer Retry-After waar aanwezig. Onbekende uitkomst na timeout: eerst ontvangstregister/boekingsdocument opvragen, dan dezelfde sleutel herhalen. Nooit een nieuwe sleutel gebruiken alleen omdat de bevestiging ontbreekt.

Retrydoel: 30 s, 2 min, 10 min met jitter, daarna dead-letter en alert. Browserdemo gebruikt handmatige klikken, drie pogingen, geen echte wachttijden. Een dead-letter vereist diagnose, eigenaar en herstartreden. Permanent onjuist bericht wordt gecorrigeerd als nieuw expliciet besluit, niet heimelijk herschreven onder dezelfde sleutel.

De volgorde van JSON-velden is geen zakelijke inhoud: dezelfde sleutel en dezelfde veldwaarden blijven hetzelfde effect. De facade weigert onbekende voorraadvelden conform het strikte schema. Zie [transactiegrenzen en ERP-bewijs](transaction-boundaries.md) voor de voorwaarde waaronder dit werkelijk op ERP-boekingen toepasbaar is.

## Legacy-variant
Als geen API bestaat: ondertekend/gecontroleerd bestandsmanifest met sequence, totaal, hash en ontvangstbestand; stagingvalidatie vóór import, geen directe database-write in ERP. Nadeel is extra vertraging; leverbaar signaal wacht op ontvangst en reconciliatie. RPA alleen laatste optie na support- en foutanalyse.

## Reconciliatie
Vergelijk de laatst volledig bevestigde beslisversie, partijsegmenten en hoeveelheden met ERP. Een gelijk totaal zonder gelijke bestemmingen is onvoldoende. Backlog, oudste berichtleeftijd, conflicts en dead-letters zijn operationele signalen. ERP-voorraad blijft leidend; afwijkingen gaan naar verantwoordelijke, niet automatisch “meest recente systeem wint”.

Vorige: [Fit-gap](fit-gap.md). Volgende: [Teststrategie](../06-validation/test-strategy.md).
