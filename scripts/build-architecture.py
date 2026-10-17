"""Build editable vector evidence for system boundaries and logical entities."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent.parent
D=R/'docs/diagrams'
def svg(name,title,subtitle,nodes,edges,width,height):
 a=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#476078"/></marker></defs><rect width="100%" height="100%" fill="white"/><text x="24" y="35" font-size="22" font-weight="bold" font-family="Arial" fill="#162a36">{escape(title)}</text><text x="24" y="64" font-size="13" font-family="Arial" fill="#476078">{escape(subtitle)}</text>']
 for f,t,label in edges:
  fx,fy,fw,fh,*_=nodes[f];tx,ty,tw,th,*_=nodes[t]
  if ty>fy:
   x1,y1=fx+fw/2,fy+fh;x2,y2=tx+tw/2,ty
  else:x1,y1=fx+fw,fy+fh/2;x2,y2=tx,ty+th/2
  a.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#476078" stroke-width="1.5" marker-end="url(#arrow)"/>')
  if label:a.append(f'<text x="{(x1+x2)/2+6}" y="{(y1+y2)/2-7}" fill="#476078" font-family="Arial" font-size="11">{escape(label)}</text>')
 for x,y,w,h,title,lines in nodes.values():
  a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#f3f6f7" stroke="#cbd8df"/><text x="{x+14}" y="{y+27}" font-size="15" font-weight="bold" font-family="Arial" fill="#162a36">{escape(title)}</text>')
  for i,l in enumerate(lines):a.append(f'<text x="{x+14}" y="{y+51+i*19}" font-size="12" font-family="Arial" fill="#476078">{escape(l)}</text>')
 a.append('</svg>');(D/name).write_text(''.join(a))
svg('architecture.svg','Systeemgrenzen en ERP-eigenaarschap','Doelontwerp: eerst standaard-fit aantonen. De browserdemo simuleert deze grenzen.',{
 'roles':(25,110,180,110,'Werkvloer',['Operator · Kwaliteit','Planning · Support']),
 'ui':(255,110,180,110,'Workbench',['Signaal en afweging','Geen voorraadwaarheid']),
 'service':(485,110,180,110,'Domeinservice',['Bevoegdheid · versie','Besluit + outbox']),
 'adapter':(715,110,180,110,'ERP-adapter',['Vaste effect-sleutel','Boekingsreferentie']),
 'erp':(945,110,195,110,'ERP / QMS',['Orders en voorraad','Inspectie / besluit']),
 'receipt':(715,300,425,100,'Ontvangst en reconciliatie',['Controleer versie, hoeveelheid en bestemming','Timeout is geen bewijs van niet verwerkt'])},[('roles','ui',''),('ui','service',''),('service','adapter',''),('adapter','erp',''),('erp','receipt','bevestiging')],1170,450)
svg('data-model.svg','Logisch datamodel','Sleutels en relaties; een inspectielot is niet automatisch dezelfde eenheid als een voorraadpartij.',{
 'order':(25,110,210,110,'Klantorder',['orderId · product · vraag','levermoment · site']),
 'po':(315,110,210,110,'Productieorder',['productionOrderId','orderId · lijn · planversie']),
 'batch':(605,110,240,110,'Partij',['batchId · parentBatchId','eenheid · hoeveelheid']),
 'inspection':(605,300,240,110,'Inspectie / besluit',['inspectionId · batchId','bestemming · reden · versie']),
 'plan':(315,300,210,110,'Herstelplan',['planId · decisionId','slot · machine · versie']),
 'message':(920,300,240,110,'Outbox / receipt',['effectKey · payloadhash','correlationId · postingref'])},[('order','po','1 : n'),('po','batch','1 : n'),('batch','inspection','1 : n'),('plan','inspection','verwijst naar'),('inspection','message','1 : n')],1190,450)
print('Architecture and logical data SVGs built')
