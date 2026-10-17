# ERP fit-gap: eerst standaard aantonen

Voor ERP-consultant, analist en Product Owner. SAP is relevante ontwerpcontext, maar er is geen SAP-systeem aangesloten en geen specifieke release of configuratie verondersteld. Deze matrix is een onderzoekshypothese, geen gevalideerde productfit.

| Behoefte | Mogelijke standaardrichting te onderzoeken | Voorgestelde classificatie | Bewijs vóór besluit | Beslisser |
|---|---|---|---|---|
| Partij en voorraadstatus beheren | ERP-partijbeheer en inspectievoorraad | Standaard/configuratie onderzoeken | Eén partij door echte inspectie en boeking volgen | Inventory + ERP owner |
| Kwaliteitsbesluit | QM-inspectielot en usage decision, indien aanwezig | Standaard eerst | Gedeeltelijke bestemmingen en bevoegdheid tonen | Quality lead |
| Herwerkopdracht | Productieorder/routing voor herstel | Standaard/configuratie onderzoeken | Routing, kosten en voorraadrelatie in sandbox | Production owner |
| Leverimpact | Beschikbaarheidscontrole en planning | Fit onzeker | Gehele keten tot transportcut-off tonen | Planning + Sales |
| Cross-role overzicht | Bestaande standaardrapporten of uitbreidbaar scherm | Kleine extensie kandidaat | Key users toetsen twee opties op hetzelfde scenario | PO |
| Veilige externe overdracht | Beschikbare API/event/middleware | Integratie kandidaat | Dubbel bericht, volgorde en ontvangst aantonen | Integration lead |
| Geen live API | Gecontroleerde bestanden met manifest en ontvangstregister | Tijdelijke workaround | Export/import, reconciliatie en hersteltest | ERP owner |
| Automatisch quality overrulen bij spoed | Niet doen | Procesregel | Bevoegdheidsbesluit vastleggen | Quality lead |

## Make/buy/configure-keuze
Optie A: bestaande ERP/QMS-functionaliteit configureren. Voorkeur als gebruikers de keten en statussen voldoende kunnen volgen. Optie B: een beperkt overzicht naast bestaande transacties; financieel en voorraadbeheer blijft ERP. Optie C: zelfstandige voorraad- en keuringsapp bouwen; afgewezen zonder harde gap omdat dit dubbele boekingslogica creëert.

De portfolio kiest B uitsluitend om functionele regels en interactie te demonstreren. In een echt project volgt de keuze pas na spike, licentie-/supportimpact, securityreview en key-userproef. De “facade” is een eigen contractgrens; geen belofte dat een SAP-standaard-API exact hetzelfde payloadmodel accepteert.

## Onderzoeksvragen
Welke ERP-release en deploymentvorm? Worden inspectielots gebruikt? Wat is de officiële bron van kwaliteitsbesluit en voorraadposting? Mag vrijgave synchroon, of volgt een aparte workflow? Hoe wordt voorraad gereserveerd? Welke material/plant/batch-sleutels en eenheden? Hoe zijn transportcut-offs vastgelegd? Welke middleware en wie ondersteunt storingen?

## Acceptatie van de spike
Vier bewijsstukken nodig: een echte gedeeltelijke bestemming; een gekoppeld boekingsdocument; een duplicate/lost-ack test; een voorraadreconciliatie. Alleen met die feiten kan “standaard”, “configuratie” of “maatwerk” definitief worden ingevuld.

Vorige: [Planning](../04-solution/planning.md). Volgende: [Integratieontwerp](integration-design.md).
