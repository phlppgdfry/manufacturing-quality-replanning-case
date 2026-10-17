# Transactiegrenzen en ERP-bewijs

Voor de functioneel analist, ERP-consultant en technische lead. Dit document bepaalt wanneer een lokaal besluit een bevestigd ERP-feit wordt. Het is een doelontwerp; de browserdemo bewijst de regels en ontvangstprojectie, geen transactie in een ERP.

## Een eigenaar per feit

| Feit | Bevoegde eigenaar | Wat de werkbank mag tonen |
|---|---|---|
| Klantorder en leverbelofte | Sales in het ERP | Versiegebonden kopie; geen stil gewijzigde leverdatum |
| Kwaliteitsoordeel | Quality lead via het gekozen ERP/QMS-proces | Ingediend besluit en bevestigingsstatus afzonderlijk |
| Voorraadbestemming en boekingsdocument | ERP | Alleen een bevestigde posting als administratief feit |
| Herstelcapaciteit | Planning via de overeengekomen planningsbron | Voorstel, bevestigde reservering en gereedmelding apart |
| Technische aflevering | Integratieservice | Pogingen, ontvangstbewijs en herstelspoor |

De voorkeur is standaard ERP/QMS-functionaliteit. Als Kwaliteit haar besluit daar al registreert, leest de werkbank het resultaat in. Een extra applicatie mag geen tweede onafhankelijke kwaliteits- of voorraadadministratie introduceren. Alleen bij een bewezen standaardgap wordt een commandoflow vanuit de werkbank overwogen.

## Vier afzonderlijke commits

1. **Command accepteren.** Controleer bevoegdheid, dossier- en planningsversie, eenheid en hoeveelheidbalans. Bewaar het verzoek en outboxrecord atomair in dezelfde database. Het command heeft een vaste effect-ID. De UI toont ‘ingediend’, niet ‘ERP geboekt’.
2. **ERP-handeling uitvoeren.** De adapter gebruikt uitsluitend ondersteunde businesshandelingen. Een kwaliteitsbesluit, gebruiksbesluit en voorraadposting zijn niet automatisch één technische call. De ERP-consultant legt de werkelijke samenhang vast in de spike.
3. **Effect bevestigen.** Leg ERP-documentnummer, status, beslisversie en partijbestemmingen vast. Bij een timeout wordt de bestaande effect-ID opgezocht. Een ontvangst op de netwerklaag is onvoldoende bewijs dat alle boekingen geslaagd zijn.
4. **Projectie bijwerken en reconciliëren.** Pas de lokale bevestigde projectie aan vanuit het ERP-bewijs. Vergelijk versie én hoeveelheid per bestemming. Een nieuw kwaliteits- of voorraadfeit maakt een oud leverbaar signaal ongeldig.

Er is geen gedistribueerde atomaire transactie over de werkbankdatabase en ERP verondersteld. De browser comprimeert deze grenzen tot lokale voorbeelden; de UI maakt het verschil tussen lokale vrijgave en ERP-bevestiging zichtbaar.

## De garantie bij een onbekende uitkomst

Een transactionele outbox voorkomt verlies van het lokale command. Zij voorkomt op zichzelf geen dubbele ERP-boeking. Voor een veilig herhaalbaar effect is daarnaast één van deze bewezen eigenschappen nodig:

- Het ERP ondersteunt dezelfde unieke externe effect-ID bij verwerken én opnieuw opvragen.
- Een ondersteunde ERP-transactie bewaart effect-ID en boeking samen atomair.
- Een alternatief boekingsprotocol geeft aantoonbaar uitsluitsel over het reeds uitgevoerde effect voordat opnieuw wordt geboekt.

Een los adapterregister is niet voldoende als het proces kan crashen tussen ERP-boeking en het schrijven van dat register. Als geen van de eigenschappen aantoonbaar is, wordt een timeout een **onbekende uitkomst voor menselijke reconciliatie**. Dan geen automatische nieuwe boeking en geen productie-GO voor het voorgestelde retrygedrag.

De demo beschikt wel over een atomair lokaal ontvangstregister. Daardoor kan zij idempotente verwerking demonstreren. Dit is geen bewijs dat een nog onbekende SAP-interface dezelfde garantie biedt.

## Volledig snapshot versus boekingsdelta

De simulator ontvangt complete, versiegebonden dossierbalansen. Een ouder snapshot mag worden erkend zonder de nieuwere projectie terug te draaien. Dit protocol mag niet zonder meer worden gebruikt voor voorraadmutaties: bij een delta van ‘+10 vrij’ moet iedere afzonderlijke effect-ID behouden blijven. Een lagere volgorde kan nog een ontbrekende echte boeking vertegenwoordigen.

## Spike en beslisgate

| Te bewijzen | Benodigd bewijs | Beslisser |
|---|---|---|
| Gedeeltelijke bestemming | Inspectiereferentie, vrij/herwerk/afkeur en betrokken partijen | Quality lead |
| Voorraadposting | ERP-document en teruggelezen hoeveelheid per bestemming | Inventory owner |
| Timeout ná verwerking | Dezelfde effect-ID terugvinden zonder tweede effect | ERP + Integration lead |
| Crash tussen twee commits | Herstel naar een verklaarbare status, zonder verloren of dubbele boeking | Technische lead |
| Late of oudere berichten | Juiste behandeling voor het gekozen snapshot- of deltaprotocol | Integration lead |
| Herstelplan tijdens herkeuring | Geen nieuw plan dat het actieve herstel vervangt | Planning + Quality lead |

Zonder deze bewijzen blijft de integratie een ontwerpvoorstel. Dat is een releasevoorwaarde, geen beperking die met een extra tekstveld wordt opgelost.

Vorige: [Integratieontwerp](integration-design.md). Volgende: [Teststrategie](../06-validation/test-strategy.md).
