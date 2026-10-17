# Discovery: van klacht naar beslisprobleem

Werkdocument voor de analist en domeinverantwoordelijken. De gesprekken hieronder zijn gesimuleerde scenario's, geen echte interviews. Het doel is onduidelijkheden en conflicten expliciet maken vóór requirements worden vastgezet.

## Probleemstelling
De melding “kwaliteit houdt onze orders tegen” veronderstelt al een schuldige. De te onderzoeken vraag is: op welk moment weet wie welke hoeveelheid vrij is, welke levering geraakt wordt en wie een herstelkeuze mag bevestigen? Te meten zijn tijdstippen van melding, besluit, planbevestiging, uitvoering, kwaliteitsvrijgave en ERP-bevestiging.

## Stakeholders
| Rol | Belang / weerstand | Beslisrecht | Betrokkenheid |
|---|---|---|---|
| Productieplanner | Levermoment halen zonder onhaalbare sloten; vreest extra administratie | Herstelplan binnen capaciteit | Dagelijkse walkthrough met werkelijk productieorder |
| Quality lead | Productspecificatie en onderbouwde vrijgave | Gebruik / herwerk / afkeur | Keuringsvoorbeelden, uitzonderingen en acceptatie |
| Operator | Snel een afwijking melden; niet dubbel invoeren | Waarneming en gereedmelding | Korte proef aan de werkpost |
| Sales / transport | Betrouwbare klantbelofte en laadmoment | Klantafspraak, niet kwaliteitsvrijgave | Impactoverleg bij overschrijding cut-off |
| ERP-consultant | Geen tweede voorraadwaarheid | ERP-fit en boekingsontwerp | Fit-gap vóór maatwerkbesluit |
| Developer / tester | Bouwbaar en toetsbaar gedrag | Technisch ontwerp / technische kwaliteit | Refinement van grensgevallen |
| Operations owner / PO | Waarde, prioriteiten en risico | Scope, prioriteit en pilotbesluit | Wekelijkse review |

## Onderzoek en workshop
Vooraf: een order met afwijking reconstrueren, statusvelden en timestamps verzamelen, processtappen meelopen, een storingsgeval opvragen. Geen productiegegevens in dit publieke portfolio opnemen.

Workshop van 90 minuten: 0–10 doel en begrippen; 10–30 feitelijke tijdlijn; 30–45 hoeveelheid- en statusverschillen; 45–60 scenario gedeeltelijke vrijgave; 60–75 foutpaden en verantwoordelijkheden; 75–85 opties en pilot; 85–90 eigenaar en datum per open punt. Gebruik een concrete partij en leg telkens vast: feit, interpretatie, wens of besluit.

## Gesimuleerde conflicten en vastlegging
| Signaal | Analyse | Besluit / open punt |
|---|---|---|
| Sales: “De planner moet voor een vaste klant kunnen vrijgeven.” | Leverprioriteit wordt verward met productconformiteit | D-01: alleen Quality lead geeft vrij; Operations owner bevestigt escalatiepad |
| Operator: “Ik heb dat al aan de supervisor gezegd.” | Informele melding heeft geen herleidbare partij of tijd | D-02: minimale melding partij + hoeveelheid + reden; werkpostpilot toetst invoerlast |
| Kwaliteit: “Goedgekeurd betekent niet dat ERP al bijgewerkt is.” | Besluit en administratieve posting zijn twee feiten | D-03: toon beide statussen, levering pas na ERP-bevestiging |
| Planner: “Herwerk past er wel tussen.” | Omstellen en controle ontbreken in tijdsinschatting | D-04: beide zijn expliciete capaciteit; kalendertolerantie blijft een open onderzoeksvraag |
| ERP-consultant: “Waarom geen standaard inspectieproces?” | Er is nog geen fit-gap uitgevoerd | D-05: standaard eerst; aparte app alleen bij aantoonbare cross-role zichtbaarheidsgap |

## Onderliggende oorzaken en vragen
5 Whys op late herplanning: tekort laat zichtbaar → status niet gedeeld → besluit en posting vermengd → geen eigenaar voor overdracht → succes gemeten per afdeling. Dit is een onderzoekshypothese, niet een vastgestelde bedrijfsoorzaak.

Open vragen: mag gedeeltelijke keuring per verpakking? Welke voorraad kan omgealloceerd worden? Zijn kleur/coating en dikte allemaal machinebeperkingen? Wie beheert routingtijden? Wat gebeurt er met een betwiste afkeur? De MVP neemt geen omallocatie of afwijkende productspecificatie toe.

Trace: P-01 ontbrekende gedeelde blokkadestatus → BR-01 leverbetrouwbaarheid → FR-02 kwaliteitsbesluit → R-03 balans → UAT-03 foutieve som geweigerd → KPI-01 beslisdoorlooptijd.

Vorige: [Context](../00-context/context.md). Volgende: [Functionele specificatie](../02-requirements/functional-specification.md).
