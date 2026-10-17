# Runbook: ERP-status blijft achter

Voor functioneel beheer en integration support. De demo laat de logica oefenen; echte logging, toegang en boekingsdocumenten moeten in de omgeving worden ingericht.

## Detectie en triage
Signalen: oudste pending ouder dan 10 minuten (voorstel), dead-letter >0, sleutelconflict >0, verschil in bestemmingen >0. Prioriteit Sev-1 bij onterecht leverbaar product; Sev-2 bij meerdere geblokkeerde leveringen zonder workaround. Functioneel beheer bepaalt businessimpact met Planner; Integratie onderzoekt transport en ontvangst.

1. Noteer dossier, partij, event-ID, correlation-ID, versie, tijd en getroffen orders.
2. Bepaal of het ERP onbereikbaar is, de payload ongeldig is, of alleen bevestiging ontbreekt.
3. Vraag ontvangstregister en ERP-document op. “Geen lokale ack” betekent niet “niet geboekt”.
4. Controleer product/plant/eenheid en hoeveelheidbalans; vergelijk geen totale voorraad zonder bestemmingen.
5. Bij tijdelijke storing: herstel bereikbaarheid; herhaal dezelfde sleutel, geen nieuw effect creëren.
6. Bij inhoudsconflict: stop replay; bepaal waarom dezelfde sleutel verschillende inhoud kreeg. Nieuw besluit alleen met eigenaar en nieuwe versie.
7. Reconcile de nieuwste bevestigde status, sluit incident na businessbevestiging en leg preventie vast.

## Oefenscenario INC-017
Fictieve drill: kwaliteitsbesluit maakt EV-2; ERP-simulator verwerkt EV-2 maar de bevestiging gaat verloren. Tweede levering met dezelfde sleutel geeft duplicate; de ontvangstprojectie blijft hetzelfde. Na drie mislukte transportpogingen ontstaat dead-letter. Integratie legt diagnose vast, reset de pogingsteller en herhaalt gecontroleerd. Testcode controleert beide routes. Deze drill is lokaal, geen externe ERP-storing.

## Logging en prestaties
Doelvelden: event-ID, objectversie, correlation-ID, actorrol, duur, status, foutcategorie en poging. Geen persoonsgegevens of vrije tekst in metrics-labels. Dashboard: p50/p95 responstijd; foutpercentage per actie; oldest pending; dead-letters; duplicate/conflict; voorraadverschillen. De browser heeft geen productie-telemetrie. NFR-doelen vragen een aparte loadtest, hersteltest en securitytest.

## Automatisering
Automatisch: somvalidatie, tekort, haalbaarheidscontrole, outbox, duplicate-detectie en technische alerts. Menselijk: kwaliteit, planbevestiging, nieuwe klantbelofte en dead-letterdiagnose. Geen AI voor kwaliteitsvrijgave of voorraadboeking: deze beslissingen vragen expliciete regels en bevoegde gebruikers. Een latere beschrijvingsassistent mag hoogstens tekst structureren en moet aantoonbare meerwaarde hebben.

Vorige: [Uitrol](../07-delivery/rollout.md). Volgende: [Waarde](../09-value/business-case.md).
