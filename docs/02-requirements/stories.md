# User stories en acceptatiecriteria

Gegenereerd uit de canonieke catalogus. Elke story heeft een actor, een resultaat en concrete Given/When/Then-voorbeelden. PO bepaalt prioriteit; het team schat.

## US-01 — Kwaliteitsafwijking registreren

Als operator wil ik een afwijking met partij, hoeveelheid en reden vastleggen, zodat de getroffen hoeveelheid direct herleidbaar geblokkeerd is.

### AC-01-1

**Given:** Afwijking gesloten en 100 m² vrij.
**When:** Operator meldt 10 m² met een reden.
**Then:** 90 m² blijft vrij, 10 m² komt in controle en één nieuw bericht wordt aangemaakt.

### AC-01-2

**Given:** Er is een open afwijking.
**When:** Operator meldt een tweede afwijking.
**Then:** De actie wordt geweigerd zonder verandering van hoeveelheden.

### AC-01-3

**Given:** Er is 100 m² vrij.
**When:** Operator meldt 101 m².
**Then:** De actie wordt geweigerd omdat de voorraad onvoldoende is.

Trace: FR-01 → R-01 → UAT-01 → KPI-01. Prioriteit: Must-have.

## US-02 — Geblokkeerde hoeveelheid beoordelen

Als Quality lead wil ik de volledige geblokkeerde hoeveelheid onderbouwd verdelen, zodat alleen beoordeeld product vrijkomt en geen hoeveelheid verdwijnt.

### AC-02-1

**Given:** 40 m² in controle en actuele versie.
**When:** Kwaliteit bevestigt 10 vrij, 20 herwerk en 10 afkeur met reden.
**Then:** 70 m² is lokaal vrij en het tekort is 30 m².

### AC-02-2

**Given:** 40 m² in controle.
**When:** Kwaliteit verdeelt samen 30 m².
**Then:** De somfout wordt zichtbaar en de oorspronkelijke toestand blijft behouden.

### AC-02-3

**Given:** De rol is Planning.
**When:** De gebruiker bevestigt een kwaliteitsbesluit.
**Then:** Het systeem weigert de actie wegens ontbrekende bevoegdheid.

Trace: FR-02 → R-02,R-03 → UAT-02,UAT-03 → KPI-01. Prioriteit: Must-have.

## US-03 — Leverimpact bepalen

Als planner wil ik tekort, materiaalvrijgave en ERP-bevestiging afzonderlijk zien, zodat ik een leverbelofte op de juiste feiten baseer.

### AC-03-1

**Given:** Er is 30 m² tekort.
**When:** Een herstelplan wordt bevestigd.
**Then:** Het tekort blijft 30 m² totdat herstel is gekeurd.

### AC-03-2

**Given:** Lokaal 100 m² vrij maar ERP loopt achter.
**When:** Planning bekijkt de order.
**Then:** Het scherm vermeldt dat ERP-bevestiging nog ontbreekt.

### AC-03-3

**Given:** ERP bevestigt alle vrije voorraad maar herstel eindigt na 16:00.
**When:** Planning bekijkt de order.
**Then:** De benodigde nieuwe leverafspraak blijft zichtbaar.

Trace: FR-03 → R-04,R-10 → UAT-04 → KPI-02. Prioriteit: Must-have.

## US-04 — Herstelopties vergelijken en bevestigen

Als planner wil ik verklaarbare herstelopties vergelijken en met een actuele versie vastleggen, zodat ik een uitvoerbaar herstelplan kan verantwoorden.

### AC-04-1

**Given:** Een lijn heeft slechts 60 minuten vrij.
**When:** Een hersteloptie vraagt 100 minuten.
**Then:** Het systeem gebruikt dat gat niet.

### AC-04-2

**Given:** Een voorstel is gebaseerd op een oudere dossier- of planversie.
**When:** Planning bevestigt.
**Then:** Het systeem weigert en vraagt een nieuwe vergelijking.

### AC-04-3

**Given:** Het herstel wacht op herkeuring.
**When:** Planning probeert opnieuw te plannen.
**Then:** Er verschijnt geen nieuw voorstel en het actieve herstel blijft behouden.

Trace: FR-04 → R-05,R-06 → UAT-05,UAT-06,UAT-07 → KPI-02. Prioriteit: Must-have.

## US-05 — Herstel uitvoeren en opnieuw keuren

**US-05a — Operator:** Als operator wil ik de fysieke uitvoering gereedmelden, zodat Kwaliteit de herstelde hoeveelheid opnieuw kan beoordelen.

**US-05b — Kwaliteit:** Als Quality lead wil ik het uitgevoerde herstel afzonderlijk controleren en vrijgeven, zodat alleen goedgekeurd product beschikbaar wordt.

### AC-05-1

**Given:** Herstelplan is bevestigd.
**When:** Operator meldt gereed.
**Then:** Nieuwe productie krijgt een kindpartij en blijft in controle.

### AC-05-2

**Given:** Herstelplan wacht op kwaliteitscontrole.
**When:** Kwaliteit bevestigt bevinding en vrijgave.
**Then:** Alleen de geplande herstelhoeveelheden worden vrijgegeven.

### AC-05-3

**Given:** Herstel is nog niet uitgevoerd.
**When:** Kwaliteit probeert opnieuw vrij te geven.
**Then:** De actie wordt geweigerd.

Trace: FR-05 → R-07 → UAT-08,UAT-09 → KPI-01. Prioriteit: Must-have.

## US-06 — Voorraadstatus veilig overdragen

Als integratiebeheerder wil ik berichten veilig herhalen en in de juiste versie verwerken, zodat een onbekende ontvangst geen dubbele of verouderde voorraadstand veroorzaakt.

### AC-06-1

**Given:** ERP verwerkt een bericht maar de bevestiging ontbreekt.
**When:** Hetzelfde bericht wordt met dezelfde sleutel herhaald.
**Then:** Er ontstaat geen tweede effect.

### AC-06-2

**Given:** Dezelfde zakelijke payload heeft een andere JSON-veldvolgorde.
**When:** Dezelfde sleutel wordt opnieuw aangeboden.
**Then:** Het bericht wordt als hetzelfde effect herkend.

### AC-06-3

**Given:** Een nieuwe versie is al ontvangen.
**When:** Een ouder compleet snapshot komt binnen.
**Then:** De actuele voorraadprojectie blijft staan.

Trace: FR-06 → R-08,R-09 → UAT-10,UAT-11,UAT-12 → KPI-03. Prioriteit: Must-have.

## US-07 — ERP-storing herstellen

Als integratiebeheerder wil ik een dead-letter na een vastgelegde diagnose herstarten, zodat storingen aantoonbaar en beheerst worden hersteld.

### AC-07-1

**Given:** Een bericht faalt drie keer.
**When:** Integratie bekijkt de wachtrij.
**Then:** Het bericht staat in dead-letter en stopt met gewone retries.

### AC-07-2

**Given:** Een dead-letter heeft geen diagnose.
**When:** Integratie probeert herstart.
**Then:** Herstart wordt geweigerd.

### AC-07-3

**Given:** Ontvangst en oorzaak zijn gecontroleerd.
**When:** Integratie motiveert herstart.
**Then:** Hetzelfde effect wordt met dezelfde sleutel opnieuw aangeboden.

Trace: FR-07 → R-11 → UAT-13 → KPI-03. Prioriteit: Must-have.

## US-08 — Besluiten herleiden

Als auditor wil ik een besluit en zijn opvolging via versies en referenties reconstrueren, zodat ik het verband tussen kwaliteitsbesluit, herstel en ERP kan controleren.

### AC-08-1

**Given:** De volledige herstelketen is uitgevoerd.
**When:** De auditor bekijkt het spoor.
**Then:** Elke overgang heeft een oplopende volgorde, versie en actorrol.

### AC-08-2

**Given:** De ontvangen ERP-versie wijkt af van de lokale voorraad.
**When:** De auditor vergelijkt de projecties.
**Then:** Het verschil is zichtbaar; lokale vrijgave heet geen bevestigde ERP-boeking.

### AC-08-3

**Given:** Een gebruiker wijzigt lokale browseropslag.
**When:** De auditor beoordeelt het bewijs.
**Then:** De documentatie erkent dat dit geen immutable productieaudit is.

Trace: FR-08 → R-12 → UAT-14 → KPI-04. Prioriteit: Must-have.

## US-09 — Beheerste pilot en feedback

Als Operations owner wil ik een pilot met acceptatie, terugval en meetplan voorbereiden, zodat technische voltooiing niet met een beheerste productie-uitrol wordt verward.

### AC-09-1

**Given:** Technische tests slagen maar key-user-sign-off ontbreekt.
**When:** Het releaseoverleg beoordeelt de pilot.
**Then:** Het productieadvies blijft NO-GO.

### AC-09-2

**Given:** Een onverklaard voorraadverschil bestaat.
**When:** Het team beoordeelt de pilot.
**Then:** Het verschil moet eerst worden opgelost en gereconcilieerd.

### AC-09-3

**Given:** Er zijn al ERP-effecten geboekt.
**When:** Rollback is nodig.
**Then:** Het team bewaart bewijs en gebruikt gecontroleerde compensatie.

Trace: FR-09 → R-13 → UAT-15 → KPI-04. Prioriteit: releasevoorwaarde.
