# Context, probleem en grenzen

Dit is de probleembaseline voor business owner, analist en ontwikkelteam. Alle organisaties, rollen, processen, aantallen en gesprekken zijn fictief. De case is zelfstandig ontworpen en gebruikt geen bestaande projectrepo.

## Opdracht
Een fabrikant van metalen dak- en gevelpanelen wil kwaliteitsblokkades verbinden met een verklaarbare herstelplanning. Een planner mag geen blokkade opheffen om een levering te halen. Een werkorder, een kwaliteitsbesluit en een ERP-boeking moeten als afzonderlijke feiten herkenbaar blijven.

De fictieve aanleiding is een partij met coatingbeschadiging die pas na productie beoordeeld wordt. Sales heeft de levering al toegezegd. Kwaliteit weet nog niet hoeveel herstelbaar is; Planning heeft intussen een vrije machineslot nodig. De opdracht is het beslismoment en de overdrachten betrouwbaar maken.

## Afbakening en aannames
| Onderwerp | Baseline | Te valideren in een echt traject |
|---|---|---|
| Organisatie | Eén vestiging, twee lijnen, één productfamilie | Proceseigenaar, vestigingsverschillen en lokale bevoegdheden |
| Eenheid | Gehele m²; één order gebruikt de getroffen partij | Stuks, lengtes, oppervlakteconversie en tolerantie per product |
| Beginsituatie | 100 m² geproduceerd; 60 vrij en 40 geblokkeerd | Of gedeeltelijke beoordeling technisch en procedureel is toegestaan |
| Klantorder | SO-1042 vraagt 100 m² tegen 16:00 | ATP/leverbelofte en transportcut-off in het ERP |
| Tijd | Voorstellen vanaf 12:00; machinekalenders tot 17:00 | Onderhoud, pauzes, bezetting en beschikbaar materiaal |
| Controle | 20 minuten per herstelopdracht | Werkelijk keuringsplan en eventuele wachttijd |
| Besluit | 10 vrij, 20 herwerk, 10 afkeur in het standaardvoorbeeld | Meetmethode, bevoegdheid en onderbouwing door kwaliteitsdienst |
| Systeem | ERP blijft in het doelontwerp voorraadadministratie beheren | Product, versie, modules, uitbreidingen en beschikbare interfaces |

## Succes en niet-doelen
Succes: van afwijking tot aantoonbaar besluit, haalbaar plan en gereconcilieerde ERP-status kunnen volgen. Businessdoelen zijn minder beslisvertraging en minder onterecht beschikbare voorraad. Het prototype bewijst de regels; het bewijst geen gerealiseerde besparing.

Buiten scope: lijnbesturing/PLC, recepturen, volledige APS-optimalisatie, productcertificatie, financiële afkeurboekingen en echte SAP-customizing. Een productie-integratie vereist functioneel consultant, security, key users en leverancierreview.

## Realistische wrijving
Een spoedorder van Sales botst met een blokkade. Een operator meldt liever mondeling. Stamdata mist machinegeschiktheid. Er is maar een kort vrij tijdvak. Een verouderd plan circuleert. Het ERP verwerkt een bericht terwijl de bevestiging verloren gaat. Elke situatie krijgt een regel, eigenaar en test; een niet-opgeloste afhankelijkheid blijft zichtbaar in het RAID-log.

Volgende: [Discovery en besluiten](../01-discovery/discovery.md).
