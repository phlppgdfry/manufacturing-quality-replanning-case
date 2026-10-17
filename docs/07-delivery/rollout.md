# Pilot, cutover, rollback en adoptie

Voor Operations owner, Quality lead en releasecoördinator. Dit is een uitvoerbaar voorbereidingsplan, geen claim dat er een echte uitrol heeft plaatsgevonden.

## Fasering en go/no-go
Discovery en fit-gap → sandboxspike → schaduwmodus op één lijn → pilot op één ploeg → evaluatie → tweede lijn → pas daarna andere vestiging. Lokale varianten worden onderzocht, niet opgelost met een ongetoetste groepsbrede standaard.

GO vereist: geen ernstige open defecten; partij-/eenheidsmapping gereconcilieerd; rechten getest; key users tekenen UAT; support heeft recovery drill uitgevoerd; training en fallback beschikbaar; ERP-bevestiging correct zichtbaar; monitoring met eigenaar en rooster. NO-GO bij onverklaard voorraadverschil, ontbrekende inspectie-/boekingsreferentie of bevoegdheidslek.

## Migratie en cutover
Inventariseer open blokkades met partij, hoeveelheid, bestemming, eigenaar en laatste ERP-versie. Reconcile aantallen én bestemmingen; onduidelijke records blijven apart, geen automatische vrijgave. Bevries alleen de benodigde wijzigingsroute in afgesproken tijdvak, niet de volledige fabriek zonder noodzaak. Maak baseline-export, controleer checksum/tellingen, laad staging, laat Quality lead en Inventory owner tekenen en open pilotgebruik. Geen historisch auditspoor verzinnen.

## Rollback
Trigger: Sev-1, onterecht vrijgegeven voorraad, herhaald onverklaard verschil of onbruikbare werkpostflow. Releasecoördinator stopt nieuwe writes, bewaart ontvangen en pending berichten, schakelt naar de vastgelegde ERP-noodprocedure en communiceert blokkades. Reconcile alle besluiten sinds baseline vóór herstart. Reeds uitgevoerde ERP-boekingen worden via gecontroleerde compensatie gecorrigeerd, nooit met database restore of een resetknop teruggedraaid. Bewaar originele correlation-ID's.

## Training en weerstand
Operator: 15 minuten één afwijking registreren met eigen werkpostwoorden. Planner: 30 minuten tekort, opties, late levering en stale voorstel. Kwaliteit: 30 minuten verdeling, bewijs en herkeuring. Integratie: 30 minuten lost-ack, dead-letter en reconciliatie. Meet taakvoltooiing, niet alleen aanwezigheid.

Ervaren medewerker: “Ik bel al jaren de supervisor.” Antwoord: laat het huidige pad zien, meet de wachttijd samen, maak het formulier minimaal en probeer het met één echte afwijking. Feedback over extra invoer krijgt prioriteit als het traceerbaarheid niet schaadt. Geen training als oplossing voor een slecht proces.

## Hypercare en benefits review
Eerste vijf werkdagen: twee korte afstemmingen per dag, één incidentkanaal, Quality lead en ERP-support bereikbaar, afwijkingstotalen dagelijks reconciliëren. Na twee weken: vergelijk mediane en p90 beslisduur, ontbrekende gegevens en achterstallige berichten met de nulmeting; beoordeel seizoens-/volumeverschillen. Uitrol stoppen of aanpassen als het proces slechter wordt. Hypotheses worden vervangen door gemeten pilotcijfers.

Vorige: [Backlog](backlog.md). Volgende: [Runbook](../08-operations/runbook.md).
