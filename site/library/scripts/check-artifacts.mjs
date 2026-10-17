import { readFileSync, readdirSync } from 'node:fs';
import assert from 'node:assert/strict';
import path from 'node:path';
import { BpmnModdle } from 'bpmn-moddle';
import SwaggerParser from '@apidevtools/swagger-parser';
const root=path.resolve(import.meta.dirname,'..');
const read=p=>readFileSync(path.join(root,p),'utf8');
for(const name of ['as-is','to-be']) {
 const xml=read(`docs/diagrams/${name}.bpmn`), result=await new BpmnModdle().fromXML(xml);
 assert.equal(result.warnings.length,0,JSON.stringify(result.warnings));
 const process=result.rootElement.rootElements.find(e=>e.$type==='bpmn:Process');
 const nodes=process.flowElements.filter(e=>e.$type!=='bpmn:SequenceFlow');
 const shapes=result.rootElement.diagrams[0].plane.planeElement;
 for(const n of nodes) assert.ok(shapes.some(x=>x.bpmnElement.id===n.id),`No DI for ${n.id}`);
 for(const g of nodes.filter(n=>n.$type==='bpmn:ExclusiveGateway')) assert.ok(g.outgoing.length>=2);
 console.log(`${name}: semantic BPMN parse + DI, no warnings`);
}
await SwaggerParser.validate(path.join(root,'contracts/openapi.json'));
console.log('OpenAPI 3.1: validated with reference resolution');
const c=JSON.parse(read('data/case.json')), tests=read('tests/domain.test.mjs'), uat=read('docs/06-validation/test-strategy.md');
assert.deepEqual(JSON.parse(read('site/assets/case-data.json')).requirements,c.requirements);
for(const r of c.requirements){assert.ok(read('docs/02-requirements/traceability.md').includes(r.id));for(const id of r.uat.split(',')){assert.ok(uat.includes(id),`Missing UAT ${id}`);if(id!=='UAT-15')assert.ok(tests.includes(id),`Missing executable example ${id}`);}}
for(const r of c.requirements)assert.ok(read(r.path).trim().length>250);
const seed=(await import('../site/assets/domain.mjs')).seed();assert.equal(seed.batch.produced,c.scope.originalQuantity);assert.equal(seed.batch.held,c.scope.initialHeld);assert.equal(seed.orders[1].demand,c.scope.demand);
console.log('Catalog, canonical specs, UAT references, executable examples and site model consistent.');
