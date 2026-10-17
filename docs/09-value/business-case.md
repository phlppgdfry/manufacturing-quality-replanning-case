# Waarde, KPI's en investeringsbesluit

Voor sponsor en Operations owner. Alle invoer is illustratief; er is geen echte nulmeting of gerealiseerde besparing. [Rekenmodel](../../data/case.json) is de bron van de getallen; de berekende uitkomst staat in de [gegenereerde rekentabel](calculation.md).

## KPI-specificatie
| ID | Maatstaf | Bron / eigenaar | Pilotdoel en beperking |
|---|---|---|---|
| KPI-01 | Mediaan en p90 melding → kwaliteitsbesluit | Audit UTC-timestamps / Quality lead | Richtwaarde -20%; alleen na nulmeting definitief |
| KPI-02 | Besluit → bevestigd haalbaar herstelplan; aantal late leveringen | Planningsversies / Planning | Minder beslisvertraging, geen belofte van extra machinecapaciteit |
| KPI-03 | Oudste pending, conflicts, dead-letters en gereconcilieerde berichten | Outbox + ERP-document / IT Operations | Geen onverklaarde voorraadverschillen; alerts volgens runbook |
| KPI-04 | Volledige meldingen en taakvoltooiing zonder hulp | Audit + observatie / Operations owner | 95% volledig is een pilotvoorstel, niet gemeten |

## Businesscase en stopcriterium
Het fictieve sponsorcriterium is terugverdienen binnen drie jaar op de meegetelde baten. Dit is een expliciete aanname, geen universele investeringsregel.
Invoer: 18 relevante afwijkingen per maand, 25 minuten minder afstemming per afwijking, €48 per uur en 70% adoptie. Dit levert vrijgespeelde tijd, geen automatisch realiseerbare cash. Implementatie: 12 dagen à €650, plus €1.200 support per jaar. Geen besparing op afval, claims, voorraad of omzet meegeteld om dubbeltelling en schijnprecisie te vermijden.

Het standaardscenario verdient zich met tijdsbesparing alleen niet terug. De aanbeveling is dus: eerst standaard ERP-configuratie toetsen en de benodigde extensie beperken; geen volledig maatwerkproject op deze cijfers goedkeuren. Een pilot moet aantonen of volume, afstemtijd of aantoonbaar vermeden schade een andere beslissing rechtvaardigen.

## Gevoeligheid en meetplan
Varieer afwijkingsvolume en bespaarde minuten afzonderlijk, en toon adoptie als factor. Voor beslissing ook implementatiekosten en jaarlijkse support vergelijken. Een optimistische hoek is geen forecast. Meet twee weken baseline en twee weken pilot, normaliseer per relevante afwijking, inspecteer uitzonderingen en publiceer range. Sponsor besluit na benefits review: doorgaan, versmallen of stoppen.

Vorige: [Runbook](../08-operations/runbook.md). Volgende: [Beslissingen](../adr/README.md).
