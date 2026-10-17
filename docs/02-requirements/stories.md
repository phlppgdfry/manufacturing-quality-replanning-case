# User stories en refinementbaseline

Gegenereerd uit de canonieke catalogus. PO prioriteert, team schat; de analist verduidelijkt uitzonderingen.

## US-01 — Kwaliteitsafwijking registreren

Als operator wil ik blokkeer een positieve hoeveelheid binnen de beschikbare voorraad; leg reden, partij en versie vast. zodat de partij direct herleidbaar geblokkeerd is.

Acceptatie: UAT-01; regels R-01; meetpunt KPI-01. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-02 — Geblokkeerde hoeveelheid beoordelen

Als Quality lead wil ik alleen Kwaliteit verdeelt de volledige blokkade in vrijgave, herwerk en afkeur met een reden. zodat geen hoeveelheid verdwijnt en alleen bevoegden vrijgeven.

Acceptatie: UAT-02,UAT-03; regels R-02,R-03; meetpunt KPI-01. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-03 — Leverimpact bepalen

Als planner wil ik bereken tekort uitsluitend uit lokaal vrijgegeven product; toon ERP-bevestiging afzonderlijk. zodat ik geen fictief beschikbare voorraad beloof.

Acceptatie: UAT-04; regels R-04,R-10; meetpunt KPI-02. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-04 — Herstelopties vergelijken en bevestigen

Als planner wil ik toon geschikte lijnen met vrije capaciteit, omstel- en controletijd; controleer versies opnieuw bij bevestiging. zodat ik een uitvoerbaar plan kan verdedigen.

Acceptatie: UAT-05,UAT-06,UAT-07; regels R-05,R-06; meetpunt KPI-02. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-05 — Herstel uitvoeren en opnieuw keuren

Als operator en Quality lead wil ik operator meldt gereed; Kwaliteit geeft pas daarna de herstelde en vervangende hoeveelheid vrij. zodat gereedmelding niet met goedkeuring wordt verward.

Acceptatie: UAT-08,UAT-09; regels R-07; meetpunt KPI-01. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-06 — Voorraadstatus veilig overdragen

Als integratiebeheerder wil ik bewaar berichten in outbox; ontvang met unieke sleutel en inhoudscontrole; oude versies mogen actuele voorraad niet overschrijven. zodat onbekende ontvangst geen dubbele verwerking veroorzaakt.

Acceptatie: UAT-10,UAT-11,UAT-12; regels R-08,R-09; meetpunt KPI-03. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-07 — ERP-storing herstellen

Als integratiebeheerder wil ik na drie mislukte pogingen dead-letter; alleen Integratie mag na diagnose herstarten. zodat fouten zichtbaar en beheersbaar blijven.

Acceptatie: UAT-13; regels R-11; meetpunt KPI-03. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-08 — Besluiten herleiden

Als auditor wil ik leg actorrol, actie, versie, planreferentie en berichtsleutel vast; productie vereist append-only serveraudit. zodat ik besluiten en effecten kan reconstrueren.

Acceptatie: UAT-14; regels R-12; meetpunt KPI-04. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

## US-09 — Beheerste pilot en feedback

Als Operations owner wil ik bereid businessacceptatie, training, go/no-go, rollback en benefits review voor. zodat technische voltooiing geen onbeheerste uitrol wordt.

Acceptatie: UAT-15; regels R-13; meetpunt KPI-04. Must-have behalve FR-09 die releasevoorwaarde is. Exacte Given/When/Then-voorbeelden staan in [teststrategie](../06-validation/test-strategy.md). Geen schattingen in story points zonder teamreview.

