from pathlib import Path
import json, xml.etree.ElementTree as E, html
R=Path(__file__).resolve().parent.parent
# Own XML and vector render; no template or existing case copied.
NS={'bpmn':'http://www.omg.org/spec/BPMN/20100524/MODEL','bpmndi':'http://www.omg.org/spec/BPMN/20100524/DI','dc':'http://www.omg.org/spec/DD/20100524/DC','di':'http://www.omg.org/spec/DD/20100524/DI'}
for p,u in NS.items(): E.register_namespace(p,u)
def tag(p,n):return '{'+NS[p]+'}'+n
def model(name,nodes,edges):
 root=E.Element(tag('bpmn','definitions'),{'id':'Definitions_'+name,'targetNamespace':'https://batchline.example/portfolio'})
 proc=E.SubElement(root,tag('bpmn','process'),{'id':'Process_'+name,'isExecutable':'false','name':name})
 lanes=E.SubElement(proc,tag('bpmn','laneSet'),{'id':'LaneSet_'+name})
 for role in dict.fromkeys(n[3] for n in nodes):
  lane=E.SubElement(lanes,tag('bpmn','lane'),{'id':name+'_lane_'+role,'name':role})
  for i,t,label,r in nodes:
   if r==role:E.SubElement(lane,tag('bpmn','flowNodeRef')).text=name+'_'+i
 for i,t,label,role in nodes:
  elem=E.SubElement(proc,tag('bpmn',t),{'id':name+'_'+i,'name':label})
  for k,(a,b,l) in enumerate(edges):
   if a==i:E.SubElement(elem,tag('bpmn','outgoing')).text=f'{name}_flow_{k}'
   if b==i:E.SubElement(elem,tag('bpmn','incoming')).text=f'{name}_flow_{k}'
 for k,(a,b,l) in enumerate(edges):E.SubElement(proc,tag('bpmn','sequenceFlow'),{'id':f'{name}_flow_{k}','sourceRef':name+'_'+a,'targetRef':name+'_'+b,**({'name':l} if l else {})})
 diagram=E.SubElement(root,tag('bpmndi','BPMNDiagram'),{'id':name+'_diagram'});plane=E.SubElement(diagram,tag('bpmndi','BPMNPlane'),{'id':name+'_plane','bpmnElement':'Process_'+name})
 pos={};roles=list(dict.fromkeys(n[3] for n in nodes));width=len(nodes)*165+80
 for idx,role in enumerate(roles):
  shape=E.SubElement(plane,tag('bpmndi','BPMNShape'),{'id':name+'_lane_di_'+role,'bpmnElement':name+'_lane_'+role,'isHorizontal':'true'});E.SubElement(shape,tag('dc','Bounds'),{'x':'0','y':str(idx*150),'width':str(width),'height':'150'})
 for idx,(i,t,label,role) in enumerate(nodes):
  x=70+idx*165;y=roles.index(role)*150+48;w,h=(36,36) if t in ['startEvent','endEvent'] else (50,50) if 'Gateway' in t else (130,60);pos[i]=(x,y,w,h)
  shape=E.SubElement(plane,tag('bpmndi','BPMNShape'),{'id':name+'_di_'+i,'bpmnElement':name+'_'+i});E.SubElement(shape,tag('dc','Bounds'),dict(zip(['x','y','width','height'],map(str,[x,y,w,h]))))
 for k,(a,b,l) in enumerate(edges):
  ax,ay,aw,ah=pos[a];bx,by,bw,bh=pos[b];edge=E.SubElement(plane,tag('bpmndi','BPMNEdge'),{'id':name+'_edge_'+str(k),'bpmnElement':f'{name}_flow_{k}'})
  for x,y in [(ax+aw,ay+ah/2),(bx,by+bh/2)]:E.SubElement(edge,tag('di','waypoint'),{'x':str(x),'y':str(y)})
 E.indent(root);E.ElementTree(root).write(R/f'docs/diagrams/{name}.bpmn',encoding='utf-8',xml_declaration=True)
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {len(roles)*150}" role="img" aria-label="{name} procesmodel"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#476078"/></marker></defs><rect width="100%" height="100%" fill="white"/>']
 for idx,role in enumerate(roles):svg.append(f'<rect x="1" y="{idx*150+1}" width="{width-2}" height="148" fill="#f8fafb" stroke="#dce4e9"/><text x="8" y="{idx*150+22}" font-family="Arial" font-size="14" fill="#476078">{role}</text>')
 for a,b,l in edges:
  ax,ay,aw,ah=pos[a];bx,by,bw,bh=pos[b];svg.append(f'<path d="M{ax+aw} {ay+ah/2}L{bx} {by+bh/2}" stroke="#476078" fill="none" marker-end="url(#arrow)"/>')
  if l:svg.append(f'<text x="{(ax+aw+bx)/2}" y="{(ay+ah/2+by+bh/2)/2-7}" font-family="Arial" font-size="12" fill="#476078">{html.escape(l)}</text>')
 for i,t,label,r in nodes:
  x,y,w,h=pos[i]
  if t in ['startEvent','endEvent']:svg.append(f'<circle cx="{x+w/2}" cy="{y+h/2}" r="18" fill="white" stroke="#162a36" stroke-width="{3 if t=="endEvent" else 1.5}"/>')
  elif 'Gateway' in t:svg.append(f'<path d="M{x+w/2} {y}L{x+w} {y+h/2}L{x+w/2} {y+h}L{x} {y+h/2}Z" fill="white" stroke="#bc4224"/>')
  else:
   svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="white" stroke="#162a36"/>')
  words=label.split();lines=[];line=''
  for word in words:
   if len(line+' '+word)>18:lines.append(line);line=word
   else:line=(line+' '+word).strip()
  if line:lines.append(line)
  for j,line in enumerate(lines):svg.append(f'<text x="{x+w/2}" y="{y+h+18+j*15 if t in ["startEvent","endEvent"] or "Gateway" in t else y+23+j*16}" text-anchor="middle" font-family="Arial" font-size="12" fill="#162a36">{html.escape(line)}</text>')
 svg.append('</svg>');(R/f'docs/diagrams/{name}.svg').write_text(''.join(svg))
model('as-is',[('s','startEvent','Afwijking','Operator'),('n','userTask','Mondeling melden','Operator'),('q','userTask','Los beoordelen','Kwaliteit'),('p','userTask','Status navragen','Planning'),('r','userTask','Herstel inschuiven','Planning'),('e','userTask','ERP bijwerken','Integratie'),('z','endEvent','Afgerond','Integratie')], [('s','n',''),('n','q',''),('q','p',''),('p','r',''),('r','e',''),('e','z','')])
model('to-be',[('s','startEvent','Afwijking','Operator'),('n','userTask','Blokkade melden','Operator'),('q','userTask','Hoeveelheid beoordelen','Kwaliteit'),('p','userTask','Opties vergelijken','Planning'),('g','exclusiveGateway','Levering tijdig?','Planning'),('a','userTask','Leverafspraak afstemmen','Planning'),('c','userTask','Plan bevestigen','Planning'),('r','userTask','Herstel uitvoeren','Operator'),('k','userTask','Herstel controleren','Kwaliteit'),('e','serviceTask','ERP overdragen','Integratie'),('h','exclusiveGateway','Bevestigd?','Integratie'),('d','userTask','Diagnose en replay','Integratie'),('z','endEvent','Gereconcilieerd','Integratie')], [('s','n',''),('n','q',''),('q','p',''),('p','g',''),('g','a','te laat'),('a','c','afgestemd'),('g','c','tijdig'),('c','r',''),('r','k',''),('k','e',''),('e','h',''),('h','d','nee'),('d','e','zelfde sleutel'),('h','z','ja')])
# OpenAPI, internal facade only, production target security made explicit.
stock={'type':'object','additionalProperties':False,'required':['batchId','version','produced','released','held','rework','scrap'],'properties':{'batchId':{'type':'string','minLength':1},**{k:{'type':'integer','minimum':0} for k in ['version','produced','released','held','rework','scrap']}}}

api = {
 'openapi':'3.1.0',
 'info':{'title':'Batchline ERP facade — design contract','version':'1.0.0','description':'Fictional target interface. Not a SAP API. No HTTP backend is running.'},
 'servers':[{'url':'https://batchline.example/api','description':'Example domain, no service'}],
 'security':[{'bearerAuth':[]}],
 'paths':{},
 'components':{'securitySchemes':{'bearerAuth':{'type':'http','scheme':'bearer','bearerFormat':'JWT'}},'schemas':{'StockSnapshot':stock}}
}
post = {
 'operationId':'receiveSnapshot', 'summary':'Receive a complete dossier snapshot idempotently',
 'description':'Quantity conservation and version ordering are mandatory. Adapter must use supported ERP business transactions, not blindly overwrite stock.',
 'parameters':[
 {'name':'Idempotency-Key','in':'header','required':True,'schema':{'type':'string','minLength':1}},
 {'name':'X-Correlation-ID','in':'header','required':True,'schema':{'type':'string','format':'uuid'}}],
 'requestBody':{'required':True,'content':{'application/json':{'schema':{'$ref':'#/components/schemas/StockSnapshot'}}}},
 'responses':{str(code):{'description':desc} for code,desc in [(200,'Accepted, duplicate or superseded'),(400,'Invalid payload or quantity balance'),(401,'Authentication required'),(403,'Permission denied'),(409,'Idempotency conflict'),(429,'Rate limited'),(503,'Temporary failure; retry same key')]}
}
post['responses']['200']['content']={'application/json':{'schema':{'type':'object','required':['status','version'],'properties':{'status':{'type':'string','enum':['accepted','duplicate','superseded']},'version':{'type':'integer'}}}}}
api['paths']['/stock-snapshots']={'post':post}
api['paths']['/recovery-plans']={'post':{
 'operationId':'commitRecoveryPlan', 'summary':'Commit a recovery proposal with version check',
 'parameters':[{'name':'If-Match','in':'header','required':True,'schema':{'type':'string'},'description':'Quoted dossier and plan version ETag'}],
 'requestBody':{'required':True,'content':{'application/json':{'schema':{'type':'object','additionalProperties':False,'required':['optionId','reason'],'properties':{'optionId':{'type':'string'},'reason':{'type':'string','minLength':1,'pattern':r'\S'}}}}}},
 'responses':{'201':{'description':'Plan committed'},'400':{'description':'Invalid proposal'},'401':{'description':'Authentication required'},'403':{'description':'Planner required'},'409':{'description':'Active recovery or business conflict'},'412':{'description':'If-Match precondition failed; refresh the dossier and proposal'}}
}}
(R/'contracts/openapi.json').write_text(json.dumps(api,indent=2)+'\n')
(R/'contracts/stock-example.json').write_text(json.dumps({'batchId':'B-2401','version':2,'produced':100,'released':70,'held':0,'rework':20,'scrap':10},indent=2)+'\n')
print('BPMN with DI, matching SVGs and OpenAPI generated')
