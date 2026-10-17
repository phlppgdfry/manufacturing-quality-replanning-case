# Verklaarbare herstelplanning

Voor planners, analist en ontwikkelteam. Dit is een haalbaarheidsmodel met vaste volgorde; het is geen globaal optimale APS-planner. Instellingen zijn expliciete aannames.

## Opties
Herwerk + vervanging: herstel maximaal de herstelbare hoeveelheid en produceer alleen het resterende tekort. Volledige vervanging: produceer het hele tekort; bestaand herwerk blijft open. Beide moeten op een geschikte lijn passen.

Duur in minuten = omstel + herwerk × 2 + nieuwe productie × lijnfactor + 20 kwaliteitscontrole. Lijn A heeft factor 2 en omstel 20, lijn B factor 3 en omstel 30. Voorstellen starten niet vóór 12:00. Kalender eindigt om 17:00. Vraag en capaciteit worden niet door elkaar gedeeld; eenheid en snelheid zijn zichtbaar.

Het algoritme zoekt het eerste niet-overlappende slot tussen bestaande opdrachten. Resultaten: tijdige opties eerst, dan minste nieuwe productie, dan vroegste einde. Dit is een verklaarbare rangorde, geen onzichtbare “AI-optimalisatie”. Planner blijft beslisser.

## Standaardscenario
Na besluit 10/20/10 is het tekort 30. Herwerkvariant: 20 herwerk + 10 nieuw. Op lijn A vraagt dat 100 minuten; het gat van 12:00 tot 13:00 is te kort. Het past na 15:00 tot 16:40 en is te laat voor 16:00. Op lijn B vraagt het 120 minuten; het past na 15:00 maar eindigt om 17:00. Volledige vervanging op A duurt eveneens 100 minuten; op B 140 minuten en past niet na 15:00. De demo toont het leverrisico eerlijk: er wordt geen vrije capaciteit uitgevonden.

Dit ongemakkelijke resultaat is inhoudelijk belangrijk: een verbeterde applicatie maakt capaciteit niet groter. De planner moet Sales betrekken voor een nieuwe afspraak of een bestaande opdracht bewust herschikken. Automatisch andere orders verschuiven is buiten scope; een latere uitbreiding moet de impact op al die orders tonen en opnieuw laten bevestigen.

## Uitzonderingen
Profiel ontbreekt → niet aanbieden. Slot buiten kalender → niet aanbieden. Tegenstrijdige productie en kwaliteitsdata → geen commit vóór opheldering. Oud voorstel → nieuw voorstel berekenen, nooit stil aanpassen. Productie gereed zonder kwaliteitsvrijgave → nog niet leverbaar. Een vertraagd ERP-bericht → lokale vrijgave zichtbaar maar levering nog geblokkeerd.

## Wat de analist bespreekt
Waarom is een gekozen optie goed voor het hele bedrijf, niet alleen één order? Welke leverbelofte mag de planner wijzigen? Kan herwerk op een aparte werkpost? Is de controletijd lijncapaciteit of laboratoriumcapaciteit? Het model telt controle conservatief in hetzelfde slot; een echt tweeresource-model vraagt een aparte keuringkalender. Deze vereenvoudiging staat in ADR-03.

Vorige: [Data](data-model.md). Volgende: [ERP fit-gap](../05-erp/fit-gap.md).
