# Functionele specificatie en acceptatiebaseline

Voor business owner, ontwikkelaars en testers. Deze baseline legt zichtbaar gedrag vast; de concrete stories en traceabilitymatrix worden uit [de catalogus](../../data/case.json) gegenereerd. Status: portfolio-baseline, geen akkoord van echte stakeholders.

## Business requirements
BR-01: planning en kwaliteit gebruiken dezelfde partijhoeveelheid en herkenbare status. BR-02: herstelkeuzes zijn haalbaar en uitlegbaar. BR-03: overdrachtsstoringen mogen geen dubbele of oudere voorraadwaarheid creëren. BR-04: een beslissing moet terug te vinden zijn van behoefte tot acceptatietest en KPI.

## UC-01: kwaliteitsbesluit
Actor: Quality lead. Trigger: een geregistreerde open afwijking. Voorwaarden: partij bekend, positieve blokkade, versie actueel. Stappen: open afwijking; bekijk geproduceerde en geblokkeerde hoeveelheid; verdeel vrijgave/herwerk/afkeur; noteer bevinding; bevestig; registreer besluit en outboxbericht; toon leverimpact. Na afloop: som blijft gelijk, alleen vrijgave verhoogt beschikbare voorraad.

Uitzonderingen: ontbrekende reden → geen mutatie; som wijkt af → geen mutatie; negatieve/fractieve/oneindige hoeveelheid → weigeren; onbevoegde rol → weigeren; oud versienummer → 409 in doelcontract; dubbel besluit → weigeren. Het origineel blijft behouden bij elke weigering. Bestemming bij ERP-storing is pending/retry, niet stilzwijgend “verwerkt”.

## UC-02: herstelplan
Actor: Planner. Trigger: beoordeelde blokkade veroorzaakt een tekort. Systeem berekent per geschikte lijn vrije slots inclusief omstel en kwaliteitscontrole. Planning vergelijkt minimale nieuwe productie met volledige vervanging. Bevestiging controleert opnieuw dossier- én planningsversie. Een laat voorstel blijft zichtbaar als leverrisico, en kan geen klantbelofte autonoom aanpassen.

Na bevestiging mag alleen Operator uitvoering gereedmelden; daarna kan Quality lead vrijgeven. Nieuwe productie krijgt een eigen kindpartijreferentie. Het demo-object batch is een dossieraggregaat van bron- en kindpartijen, geen fysiek samenvoegen van voorraadpartijen. Fysieke partijsegmenten en ERP-documentreferenties zijn vereist in een productie-implementatie.

## Regels
| Regel | Controle | Reden |
|---|---|---|
| R-01 | Positieve blokkade ≤ vrije hoeveelheid; partij en reden verplicht | Geen ongedekte of niet-herleidbare blokkade |
| R-02 | Alleen Quality lead beslist; Planner kan geen kwaliteitsvrijgave geven | Functiescheiding |
| R-03 | Geproduceerd = vrij + in controle + herwerk + afkeur | Geen verdwenen of dubbel getelde hoeveelheid |
| R-04 | Tekort = max(0, vraag − lokaal vrijgegeven hoeveelheid) | Gepland/herwerk is geen beschikbare voorraad |
| R-05 | Alleen geschikte lijnen; geen overlap; binnen kalender | Fysiek uitvoerbaar plan |
| R-06 | Snapshot en planversie moeten nog actueel zijn | Geen stil overschrijven van recenter werk |
| R-07 | Gereedmelding creëert controlevoorraad; Quality lead geeft opnieuw vrij | Uitvoering is geen kwaliteitsgoedkeuring |
| R-08 | Zelfde berichtsleutel + zelfde payload = één effect; andere payload = conflict | Veilige herhaling |
| R-09 | Lagere berichtversie overschrijft hogere niet | Bescherming tegen omgekeerde aflevering |
| R-10 | Leverbaar vereist lokaal voldoende vrij én gelijk ERP-snapshot zonder open berichten | Geen levering op een onbevestigde lokale toestand |
| R-11 | Drie mislukte pogingen → dead-letter; diagnose vóór herstart | Geen oneindige stille retries |
| R-12 | Acties krijgen volgorde, type, detail en versie | Herleidbaar besluitspoor |
| R-13 | Pilot heeft business-sign-off, reconciliatie en terugvalprocedure nodig | Technische tests zijn geen businessacceptatie |

## Beslistabel: disposition van 40 m²
| Vrij | Herwerk | Afkeur | Actor | Uitkomst |
|---:|---:|---:|---|---|
| 10 | 20 | 10 | Kwaliteit | Geldig: 70 vrij, 20 herwerk, 10 afkeur; tekort 30 |
| 40 | 0 | 0 | Kwaliteit | Geldig mits controlebevinding; tekort nul lokaal, ERP nog te bevestigen |
| 10 | 20 | 0 | Kwaliteit | Weigeren: 10 ontbreekt |
| 10 | 20 | 10 | Planning | Weigeren: rol |
| -10 | 40 | 10 | Kwaliteit | Weigeren: negatieve hoeveelheid |

## Non-functional requirements
NFR-01: doel p95 read ≤2 s bij 30 gelijktijdige gebruikers; te toetsen met productieachtige dataset, niet bewezen door deze browserdemo. NFR-02: geen actie verloren na servercrash, transactionele outbox; demo localStorage is geen bewijs. NFR-03: gebruikersrol serverzijdig afdwingen, audit append-only. NFR-04: WCAG AA-gericht toetsenbordpad en 375 px leesbaarheid; geen volledige conformiteitsaudit geclaimd. NFR-05: back-up/hersteldoel RPO 15 min en RTO 4 uur zijn pilotvoorstellen, eigenaar IT Operations moet akkoord geven.

## Ready en Done
Ready: eigenaar bekend, proces en definities helder, ERP-fit besproken, uitzonderingen en voorbeeldhoeveelheden gereviewd, acceptatiecriteria toetsbaar. Done: code/contracttests groen, integratie in sandbox bewezen, autorisatietests, business-UAT ondertekend, monitoring en runbook gereviewd. De portfolio voldoet niet aan de sandbox- en eindgebruikersvoorwaarden; die blijven releasevoorwaarden.

Vorige: [Discovery](../01-discovery/discovery.md). Volgende: [Proces](../03-processes/process-design.md).
