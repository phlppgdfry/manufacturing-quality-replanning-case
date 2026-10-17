# Verificatie en oplevergrenzen

De case is lokaal getest en de eerste private GitHub Actions-run is geslaagd. Openbare GitHub Pages-publicatie is voorbereid en vraagt afzonderlijk akkoord. Persoonlijke beheersing en businessacceptatie zijn niet door technische checks bewezen.

## Gecontroleerd gedrag

42 automatische domein-/artefacttests slagen. De hoeveelheidtest controleert bovendien alle 861 gehele verdelingen van de oorspronkelijke blokkade. Getoetst zijn functiescheiding, foutieve sommen, stale dossier-/planversies, capaciteit, herkeuring, kindpartijreferentie, onbekende ontvangst, sleutelconflict, oudere snapshots en dead-letterreplay.

Semantische BPMN-import met bpmn-moddle en DI-dekking: AS-IS en TO-BE zonder warnings. OpenAPI 3.1 gevalideerd met reference resolution. De linkcheck controleert relatieve document-, asset- en modulepaden. Canonieke catalogus, siteprojectie, acceptatiereferenties en rekenmodel zijn vergeleken.

## Browsercontrole

Primair IAB geprobeerd; concrete fout: `Browser is not available: iab`. Daarom Playwright Chromium gebruikt. Desktop 1536×1024 en mobiel 375×812. Geen relevante console- of runtimefouten. De test doorloopt werkelijk kwaliteit → planning → operator → herkeuring → ERP lost-ack → dead-letter → diagnose/replay → reconciliatie. Het oorspronkelijke leverrisico blijft zichtbaar na voorraadherstel. Herladen bewaart de oefensessie. Achtstappentour, toetsenbord en sluiten gecontroleerd. De tour gebruikt aparte voorbeeldtoestanden en wijzigt de eigen opgeslagen oefensessie niet.

Zie [browserresultaten](browser-results.json), [browsertestbron](../../scripts/browser-check.mjs) en [screenshots](../screenshots/README.md).

## Vergelijking met het visuele concept

Referentie: [concept](../design/concept.png), gebouwd met ingebouwde Image Gen. Referentie én laatste desktoprender zijn met view_image naast elkaar beoordeeld op dezelfde native afmetingen 1536×1024; mobiel is apart geïnspecteerd.

| Vergelijkpunt | Beoordeling / wijziging |
|---|---|
| Indeling | Linker rail, open cijferstrook, planning links, inspectie rechts en afsluitende procesband behouden |
| Typografie | Expliciete systeemfont-schaal voor titels, labels, tabellen en controls; geen browser-default knoppen |
| Kleur | Witte achtergrond en blauwgrijze vlakken behouden; accent bewust donkerder voor leesbaar tekstcontrast |
| Containers | Kleine radii en hairlines, geen bento of extra marketinghero |
| Copy | Nav- en actiebenamingen behouden; datum, hoeveelheid en tijdas inhoudelijk gecorrigeerd |
| Planning | Visuele taken komen uit het werkelijke capaciteitsmodel; tijdaslabelpositie gecorrigeerd naar minuten |
| Mobiel | Gestapelde panelen, horizontale nav en scrollbare tabel met expliciete veegaanwijzing; geen paginabrede overflow |
| Interactie | Alle zichtbare hoofdacties reageren; rol-, hoeveelheid- en versievoorwaarden blijven in de domeinlaag |

Boven-de-vouw-copy vergeleken met de toegestane lijst. Bewuste functionele toevoegingen: hoeveelheidbalans, oefenrol, versie en simulatiegrens. Bewuste correcties: 17 oktober 2026 zonder foutieve weekdag; SO-1042 vraagt 100 m²; tijdas tot 17:00. Deze afwijkingen staan in [ontwerpspecificatie](../design/design-system.md). Geen resterende materiële visuele blokkade gevonden binnen de geteste schermen. De implementatie is tegen het concept geverifieerd met deze expliciete inhoudelijke afwijkingen.

## PDF en presentatie

One-pager één A4; casebook zeven pagina's; presentatie acht slides. Selecteerbare tekst gecontroleerd met pypdf. Alle pagina's gerenderd met Poppler; de layouts zijn visueel beoordeeld, inclusief detailcontrole van one-pager, laatste casebookpagina en planningsslide. Geen zichtbare clipping, overlap of ontbrekende tekens. De presentatie heeft PDF en bewerkbare HTML-bron; geen PPTX omdat de voorgeschreven presentation-runtime in deze omgeving ontbreekt.

## Niet aangetoond

Geen echte SAP-, MES- of QMS-koppeling, geen multi-usertransacties, productieautorisatie, immutable audit, productiebelasting, werkelijke key-user-UAT of uitrol. Geen zelfstandig beheersingsniveau van de kandidaat vastgesteld. Deze punten blijven expliciete release- of leervoorwaarden; tests zijn daarvoor geen vervanging.
