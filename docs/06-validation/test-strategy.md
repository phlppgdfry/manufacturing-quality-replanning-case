# Teststrategie en acceptatie

Voor tester, key users en PO. Automatische checks zijn uitvoerbaar; business-UAT, SAP-sandbox en productiebelasting zijn niet uitgevoerd. Het bewijsrapport legt vast wat werkelijk is getest.

## Risicogestuurde lagen
Domeintests: hoeveelheidconservering, rollen, versies, capaciteit, dubbele berichten en volgorde. Browsertest: hoofdflow, foutmeldingen, rolwissels, bevestigingen, herladen, rondleiding, desktop en 375 px. Artefactchecks: traceability, BPMN met DI, OpenAPI, lokale links en afgeleide documenten. Sandbox: nog nodig voor ERP-documenten, autorisaties, echte timing en transacties. UAT: door echte operator, planner en kwaliteitsmedewerker te ondertekenen.

## Acceptatiegevallen
| ID | Given / When | Then |
|---|---|---|
| UAT-01 | Gesloten afwijking, 10 vrije m²; Operator meldt 11 | Weigeren zonder wijziging |
| UAT-02 | 40 geblokkeerd; Kwaliteit verdeelt 10/20/10 | Balans 100; vrij 70; tekort 30 |
| UAT-03 | 40 geblokkeerd; verdeling 10/20/0 of rol Planner | Som- of autorisatiefout; geen besluit |
| UAT-04 | 30 tekort en alleen herstel gepland | Tekort blijft 30; nog niet leverbaar |
| UAT-05 | Kort vrij gat of ongeschikte lijn | Geen overlappend of ongeschikt voorstel |
| UAT-06 | Snapshot v2; ander besluit wijzigde versie | Commit weigeren als verouderd |
| UAT-07 | Alle voorstellen na transportcut-off | Leverrisico zichtbaar; geen tijdige belofte |
| UAT-08 | Operator meldt herstel gereed | Nieuw product in controle; geen automatische vrijgave |
| UAT-09 | Kwaliteit geeft gecontroleerd herstel vrij | Lokaal tekort nul, ERP nog te bevestigen |
| UAT-10 | ERP verwerkt maar bevestiging verdwijnt | Herhaal zelfde sleutel: één effect |
| UAT-11 | Zelfde sleutel, andere payload | Conflict; geen stil overschrijven |
| UAT-12 | Nieuwe versie ontvangen vóór oude | Actuele voorraad blijft staan |
| UAT-13 | Drie transportfouten; diagnose en herstart | Dead-letter, daarna gecontroleerde replay |
| UAT-14 | Volledige keten | Auditsequence strikt stijgend; balans sluit |
| UAT-15 | Techniek groen maar key-user-sign-off ontbreekt | Geen productie-go-live |

## Defecten en feedback
Werkelijk ontwerpissue gevonden in review: alleen lokaal voldoende vrijgegeven voorraad zou de order als veilig tonen terwijl ERP nog achterloopt. Fix: R-10/canShip eist ook gelijk bevestigd snapshot en geen open overdracht. Regressiecontrole: vrijgave zonder sync blijft leverrisico. Dit is een analyse-/implementatiereview, geen verzonnen key-userfeedback.

Tweede inhoudelijk inzicht: alle herstelopties kunnen te laat zijn; de demo mag daar geen “groen” resultaat van maken. De planningtests controleren haalbaarheid en cut-off, niet alleen dat een optie verschijnt.

Voorbereide UAT-sign-off: testerrol, datum, build/commit, scenario-ID, verwacht/werkelijk, bewijs, defect-ID, ernst, workaround, hertest en handtekening van Quality lead én Operations owner. Open Sev-1/Sev-2 of voorraadverschil → NO-GO.

Vorige: [Integratie](../05-erp/integration-design.md). Volgende: [Delivery](../07-delivery/backlog.md).
