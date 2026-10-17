# Toegang, audit en beheersing

Voor security, Operations en analist. De rolkiezer is demonstratie; client-side checks beschermen geen productiegegevens. De domeintests bewijzen regelgedrag, niet identity security.

| Actie | Operator | Planning | Kwaliteit | Integratie |
|---|---:|---:|---:|---:|
| Afwijking melden / uitvoering gereed | ja | nee | nee | nee |
| Herstelplan bevestigen | nee | ja | nee | nee |
| Bestemming en herkeuring vrijgeven | nee | nee | ja | nee |
| Bericht verwerken / diagnose-replay | nee | nee | nee | ja |

Alle rollen mogen de fictieve demo lezen. In productie site/plant en functie combineren; alleen het juiste quality-team beslist over zijn inspectielot. Authenticatie via enterprise identity; backend bepaalt bevoegdheid uit claims, nooit uit een browserveld. Geen gedeeld “operator”-account voor auditplichtige besluiten. Eventuele vierogenregels en afkeurgrenzen met Quality lead vastleggen; niet zonder bron uitvinden.

Audit in productie: actor-ID, rol, UTC-tijd, object, oude/nieuwe versie, reden, correlation-ID en boekingsreferentie append-only bewaren. Toegang beperkt; retentie en export door data owner goedgekeurd. De demo bewaart alleen sequence, gebeurtenistype, detail en versie in wijzigbare lokale opslag. Geen geheimen of echte persoonsdata invoeren.

Threats: onbevoegde vrijgave → serverautorisatie; stale update → conditionele write; replay → idempotentiesleutel en payloadcontrole; injectie in beschrijving → output escaping en servervalidatie; verdwenen audit → transactionele persist en back-up; gewijzigd tarief/tempo → masterdataversie en review. Browseropslag kan door gebruiker worden aangepast; gebruik dit nooit als voorraadadministratie.

Vorige: [Data](data-model.md). Volgende: [ERP-integratie](../05-erp/integration-design.md).
