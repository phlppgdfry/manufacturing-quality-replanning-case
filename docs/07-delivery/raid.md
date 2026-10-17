# RAID-log en escalaties

Voor PO en projectteam. Alle entries zijn fictieve projectrisico's; eigenaren zijn rollen. Wekelijks reviewen en na elke scopewijziging bijwerken.

| ID | Type | Punt | Impact / mitigatie | Eigenaar / besluitmoment |
|---|---|---|---|---|
| RSK-01 | Risico | Dubbele voorraadwaarheid | ERP leidend; postingreferentie en reconciliatie; geen levering op lokale vrijgave alleen | ERP owner, vóór spike-sign-off |
| RSK-02 | Risico | Vrijgave onder leverdruk | RBAC, kwaliteitsrecht en escalatie | Quality lead, vóór UAT |
| ASM-01 | Aanname | Gehele m² volstaan | In echt proces lengte/stuk/oppervlakte en conversie aantonen | Masterdata owner, discovery |
| ASM-02 | Aanname | Controle duurt 20 min in hetzelfde slot | Echte lab-/lijncapaciteit meten | Planning owner, pilotontwerp |
| ISS-01 | Issue | ERP-interface en versie onbekend | Geen productie-fit claim; sandboxspike | ERP consultant, vóór buildbesluit |
| DEP-01 | Afhankelijkheid | Machinegeschiktheid ontbreekt in stamdata | Geen voorstel bij ontbrekende mapping; eigenaar en onderhoudsproces vastleggen | Production engineering, vóór pilot |
| DEP-02 | Afhankelijkheid | Key users niet ingepland | UAT en training reserveren; geen sign-off verzinnen | Operations owner, vóór go/no-go |
| RSK-03 | Risico | Maatwerk economisch niet verantwoord | Businesscase toont negatieve tijds-ROI; standaard eerst onderzoeken | Sponsor, investeringsbesluit |

Escalatie: binnen team ophelderen; eigenaar schrijft opties en gevolg; PO prioriteert; sponsor besluit over budget. Analist registreert besluit en trace, maar neemt geen kwaliteits- of budgetbevoegdheid over.
