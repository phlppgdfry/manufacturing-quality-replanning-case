from pathlib import Path
import json, html
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
R=Path(__file__).resolve().parent.parent;out=R/'application-kit/exports';out.mkdir(parents=True,exist_ok=True)
INK=HexColor('#162a36');MUTED=HexColor('#476078');ACCENT=HexColor('#bc4224');LINE=HexColor('#dce4e9')
body=ParagraphStyle('body',fontName='Helvetica',fontSize=11.5,leading=17,textColor=INK,spaceAfter=10)
small=ParagraphStyle('small',parent=body,fontSize=9,leading=13,textColor=MUTED)
def para(c,text,x,y,w,style=body):
 p=Paragraph(html.escape(text),style);pw,ph=p.wrap(w,1000);p.drawOn(c,x,y-ph);return y-ph-14

def base(c,title,n,total,size=A4):
 w,h=size;c.setFillColor(INK);c.setFont('Helvetica-Bold',15);c.drawString(42,h-42,'Batchline');c.setStrokeColor(ACCENT);c.setLineWidth(2);c.line(42,h-53,75,h-53)
 c.setFont('Helvetica',8);c.setFillColor(MUTED);c.drawRightString(w-42,h-40,'FICTIEVE PORTFOLIO-CASE')
 c.setFillColor(INK);c.setFont('Helvetica-Bold',25);c.drawString(42,h-100,title)
 c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(42,43,w-42,43);c.setFillColor(MUTED);c.setFont('Helvetica',8);c.drawString(42,29,'Onafhankelijk - AI-ondersteund - ERP gesimuleerd - 17 oktober 2026');c.drawRightString(w-42,29,f'{n} / {total}')
 return h-128
c=canvas.Canvas(str(out/'one-pager.pdf'),pagesize=A4);y=base(c,'Kwaliteit en productieplanning',1,1)
for title,text in [
('Het probleem','Van 100 m² geproduceerd product is 40 m² geblokkeerd. Kwaliteit moet beslissen, Planning moet de leverimpact kennen en ERP moet dezelfde toestand bevestigen.'),
('De aanpak','Discovery, functionele specificatie, proces, ERP-fit-gap, herstelplanning, acceptatie en beheer vormen een traceerbare keten.'),
('Het bewijs','BPMN-modellen, quantity- en statusregels, capaciteitsvergelijking, versiecontrole, eigen OpenAPI-facade, outbox en ontvangstregister, automatische tests en een werkende browserdemo.'),
('De belangrijkste beslissingen','Alleen Kwaliteit geeft vrij. Een plan is geen voorraad. Herhaal een onbekende ERP-uitkomst met dezelfde sleutel. Onderzoek ERP-standaard voordat maatwerk wordt gekozen.'),
('De uitkomst','Alle voorbeeldopties missen de oorspronkelijke levering. De illustratieve tijdwaarde rechtvaardigt maatwerk niet op zichzelf. Advies: standaardonderzoek en een beperkte pilot met nulmeting.'),
('De grenzen','Fictieve organisatie en workshopscenario’s. Geen SAP-runtime, machinebesturing of uitgevoerde eindgebruikers-UAT. Persoonlijke beheersing moet afzonderlijk worden getoetst.')]:
 c.setFont('Helvetica-Bold',12);c.setFillColor(ACCENT);c.drawString(42,y,title);y-=10;y=para(c,text,42,y,511)
c.setFillColor(MUTED);c.setFont('Helvetica',9);c.drawString(42,69,'Bronnen en detail: CASE_STUDY.md, EVIDENCE.md en data/case.json in de repository.')
c.save()
pages=[
('Opdracht en afbakening',[('De opdracht','Een kwaliteitsblokkade vertalen naar een onderbouwd herstelplan. De fictieve fabrikant maakt metalen dak- en gevelpanelen. Eén vestiging, twee lijnen, één getroffen order en gehele m² houden de case uitlegbaar.'),('Het beslisprobleem','Een order vraagt 100 m²; 60 is vrij en 40 geblokkeerd. Sales wil leveren, Kwaliteit wil bewijs en Planning wil bruikbare capaciteit. Leverdruk mag het kwaliteitsrecht niet veranderen.'),('Wat de case toont','Functionele analyse van een onduidelijke vraag tot exacte regels, systeemgrenzen, tests, acceptatie- en beheerplannen. De browser voert de regels echt uit; ERP, rollen en fabriek zijn gesimuleerd.'),('Herkomst','Nieuw uitgewerkte, AI-ondersteunde portfoliocase. Geen bestaande projectrepo hergebruikt. Gesprekken en cijfers zijn verzonnen; persoonlijke ervaring wordt niet uit deze case afgeleid.')]),
('Discovery en verantwoordelijkheden',[('Onderzoek','Reconstructeer een concrete afwijking, loop het productieproces mee en scheid feit, interpretatie en wens. Het portfolio bereidt een workshop voor met partij, hoeveelheden, statussen en tijdlijn.'),('De tegenstrijdigheden','Sales vraagt een override; Kwaliteit vraagt controle; Operator wil niet dubbel invoeren; ERP-consultant vraagt waarom een nieuwe app nodig is. Het ontwerp lost dit op met minimale melding, functiescheiding en een standaard-fit-gate.'),('Beslisrechten','Quality lead beslist over bestemming. Planner bevestigt capaciteit. Sales stemt de klantbelofte af. ERP owner bewaakt voorraadboekingen. PO prioriteert, analist maakt gedrag en gevolgen expliciet.'),('Trace','Pijnpunt P-01 leidt naar BR-01, FR-02, hoeveelheidregel R-03, UAT-03 en KPI-01. De catalogus en matrix maken iedere verbinding inspecteerbaar.')]),
('Regels, data en proces',[('Hoeveelheid','Het voorbeeldbesluit verdeelt 40 in 10 vrij, 20 herwerk en 10 afkeur. De totale 100 blijft in balans. Het lokale tekort is 30. Herwerk en een toekomstig plan tellen niet als vrije voorraad.'),('Statusovergangen','Kwaliteitsbesluit, plan, fysieke gereedmelding, herkeuring en ERP-bevestiging zijn afzonderlijke feiten. Operator kan geen kwaliteit vrijgeven. Planner kan geen oud voorstel bevestigen.'),('Partijtrace','Vervangende productie krijgt een kindpartijreferentie. De demo toont een dossieraggregaat; het doelontwerp vraagt fysieke partijsegmenten, inspectielots en boekingsdocumenten.'),('Uitzonderingen','Foutieve som, ontbrekende reden, verkeerde rol en verouderde versie worden geweigerd zonder wijziging. Het BPMN-model toont overdrachten en ERP-diagnose/replay.')]),
('Planning en ERP-fit',[('Capaciteit','Het model zoekt een vrij slot op geschikte lijnen. Omstellen, productie, herwerk en kwaliteitscontrole tellen mee. Het gat van 12:00 tot 13:00 is te kort voor de herstelopdracht.'),('Een late uitkomst','Op lijn A past herstel om 15:00 tot 16:40; de oorspronkelijke levering is 16:00. De applicatie markeert de benodigde nieuwe leverafspraak. Vrijgegeven voorraad lost een gemiste leverbelofte niet op.'),('Standaard eerst','Onderzoek ERP/QMS-inspectie, usage decision, herwerkorders en beschikbaarheid. De zelfstandige workbench is alleen verantwoord bij een bewezen standaardgap.'),('SAP-grens','SAP-documentatie vormt referentiecontext. De facade is een eigen ontwerp. Er is geen SAP-runtime aangesloten en geen concrete productversie of moduleconfiguratie aangetoond.')]),
('Integratie en beheersing',[('Onbekende ontvangst','Een timeout kan na verwerking optreden. Een vaste sleutel en payloadcontrole geven herhaling zonder dubbel effect. Een oud compleet snapshot mag een nieuwere projectie niet overschrijven.'),('Doelarchitectuur','In productie schrijft één transactie het besluit en outbox. Een worker gebruikt ondersteunde ERP-acties, bewaart postingreferenties en reconcilieert de werkelijke voorraad. De browser simuleert die rollen lokaal.'),('Herstel','Na drie mislukte pogingen wordt een bericht dead-letter. Support controleert de ontvangst, corrigeert de oorzaak, noteert diagnose en herstart met dezelfde sleutel.'),('Security en prestaties','Enterprise identity, serverautorisatie, append-only audit en production-like loadtest blijven vereist. De demo heeft geen echte authenticatie of duurzame transacties.')]),
('Acceptatie en uitrol',[('Testontwerp','Automatische controles testen hoeveelheden, functiescheiding, stale plannen, capaciteit, lost-ack, payloadconflict en omgekeerde aflevering. Browserchecks doorlopen de flow op desktop en mobiel.'),('UAT en go/no-go','Echte key users moeten scenario’s en afwijkingen ondertekenen. Geen voorraadverschil, geen ernstige defecten, gereviewde rechten, training, runbook en recovery drill zijn voorwaarden voor een pilot.'),('Rollout','Begin met één lijn en één ploeg in schaduwmodus. Reconcile open blokkades en de beginsnapshot, meet taakvoltooiing en doorlooptijd en schaal pas op bij aantoonbare verbetering.'),('Rollback','Stop nieuwe writes, behoud berichtstatussen en reconcile besluiten sinds de baseline. Reeds geboekte effecten vragen gecontroleerde compensatie; een reset of database restore is geen veilige ERP-terugval.')]),
('Waarde en aanbeveling',[('Illustratieve invoer','18 afwijkingen per maand, 25 minuten minder afstemming, 48 euro per uur, 70% adoptie. Investering: 12 dagen tegen 650 euro, met 1.200 euro jaarlijkse support.'),('Modeluitkomst','Jaarlijkse tijdwaarde is 3.024 euro; na support blijft 1.824 euro. Een investering van 7.800 euro verdient zich eenvoudig pas na ongeveer 4,3 jaar terug. Tijdwaarde is geen automatisch realiseerbare cash.'),('Advies','Geen maatwerk-go op tijdsbesparing alleen. Onderzoek standaardconfiguratie, beperk de extensie en vervang aannames met pilotmetingen. Afval-, claim- en omzetbaten zijn niet verzonnen om het advies positief te maken.'),('Grenzen en bronnen','Fictief en AI-ondersteund. Geen SAP-implementatie, echte workshops, gerealiseerde baten of uitgevoerde gebruikers-UAT. Bronnen: eigen catalogus en referenties in docs/00-context/sources.md; primaire SAP-documentatie is versiegebonden.')])]
c=canvas.Canvas(str(out/'casebook.pdf'),pagesize=A4)
for n,(title,blocks) in enumerate(pages,1):
 y=base(c,title,n,len(pages))
 for sub,text in blocks:
  c.setFont('Helvetica-Bold',13);c.setFillColor(ACCENT);c.drawString(42,y,sub);y-=13;y=para(c,text,42,y,511);y-=11
 c.showPage()
c.save()
slides=json.loads((R/'data/slides.json').read_text());size=(960,540);c=canvas.Canvas(str(out/'deck.pdf'),pagesize=size)
slidehtml=[]
for i,(title,claim,text,notes) in enumerate(slides,1):
 w0,h=size;c.setFillColor(INK);c.setFont('Helvetica-Bold',18);c.drawString(55,491,'Batchline');c.setFillColor(MUTED);c.setFont('Helvetica',11);c.drawRightString(905,491,f'{i:02d} / 08')
 c.setFillColor(INK);c.setFont('Helvetica-Bold',35);c.drawString(55,410,title)
 c.setFillColor(ACCENT);big=ParagraphStyle('claim',fontName='Helvetica-Bold',fontSize=29,leading=36,textColor=ACCENT);y=para(c,claim,55,368,825,big)
 large=ParagraphStyle('large',fontName='Helvetica',fontSize=21,leading=30,textColor=INK);y=para(c,text,55,y-18,800,large)
 c.setFillColor(MUTED);c.setFont('Helvetica',9);c.drawString(55,31,'Onafhankelijke fictieve portfolio-case - AI-ondersteund - geen SAP-runtime')
 c.showPage()
 slidehtml.append(f'<section><small>Batchline · {i:02d}/08</small><h1>{html.escape(title)}</h1><h2>{html.escape(claim)}</h2><p>{html.escape(text)}</p><footer>Onafhankelijke fictieve portfolio-case · AI-ondersteund · ERP gesimuleerd</footer><aside>{html.escape(notes)}</aside></section>')
c.save()
(R/'site/deck.html').write_text('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Batchline — presentatie</title><style>body{margin:0;color:#162a36;font-family:Arial,sans-serif}section{box-sizing:border-box;position:relative;min-height:100vh;padding:7vw 8vw;border-bottom:1px solid #dce4e9}h1{font-size:clamp(30px,5vw,58px);margin:10vh 0 4vh}h2{font-size:clamp(24px,4vw,44px);color:#bc4224;max-width:1100px}p{font-size:clamp(19px,3vw,31px);max-width:1000px;line-height:1.5}small,footer{color:#476078}footer{margin-top:10vh;font-size:13px}aside{margin-top:30px;font-size:12px;color:#476078}@media print{@page{size:landscape;margin:0}section{height:100vh;break-after:page}aside{display:none}}</style></head><body>'+''.join(slidehtml)+'</body></html>')
print('Created one-pager.pdf (1 page), casebook.pdf (7 pages), deck.pdf (8 slides), editable HTML deck')
