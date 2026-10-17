# Export- en afleverstatus

| Artefact | Bron | Aflevering |
|---|---|---|
| One-pager | executive/one-page-summary.md | [PDF](exports/one-pager.pdf), één A4 |
| Casebook | CASE_STUDY en canonieke documenten | [PDF](exports/casebook.pdf), zeven pagina's |
| Presentatie | data/slides.json en spreeknotities | [PDF](exports/deck.pdf), acht slides; [bewerkbare HTML-bron](../site/deck.html) |
| Case en bewijs | docs en data/case.json | [Website](../site/case.html) en statische documentbibliotheek |
| Demo | site/assets/domain.mjs en app.mjs | [Achtstappenrondleiding](../site/index.html?tour) |

Er is geen PPTX-export: de voorgeschreven gebundelde presentation-runtime en load_workspace_dependencies-tool zijn in deze omgeving niet beschikbaar. De presentatie is daarom geleverd als PDF en bewerkbare HTML met afzonderlijke spreeknotities, zonder een vervangende PowerPoint-library te installeren.

PDF-herbouw: python3 scripts/export-pdfs.py (ReportLab vereist). Statische bibliotheek: python3 scripts/build-library.py. Regels/traceability/rekenmodel: npm run build. BPMN en contract: python3 scripts/build-process-contracts.py. De exports zijn visueel te controleren met pdftoppm; runtimebeperkingen staan in de bronverantwoording.
