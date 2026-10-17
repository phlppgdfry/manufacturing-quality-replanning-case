import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {seed,decide} from '../site/assets/domain.mjs';
const model=JSON.parse(readFileSync(new URL('../data/case.json',import.meta.url)));
test('Canonical example and domain agree on starting amounts and disposition',()=>{const s=seed(),d=model.scope.decision,n=decide(s,{role:'quality',expectedVersion:1,...d,reason:'catalog example'});assert.equal(s.batch.held,model.scope.initialHeld);assert.equal(n.batch.released,model.scope.initialReleased+d.release);assert.equal(n.batch.rework,d.rework);assert.equal(n.batch.scrap,d.scrap);});
test('Published model does not claim positive annual value exceeds investment',()=>{const b=model.businessCase;const annual=b.eventsPerMonth*b.minutesSavedPerEvent/60*b.hourlyCost*b.months*b.adoption-b.annualSupport;assert.ok(annual*model.businessCase.investmentHorizonYears<b.implementationDays*b.dayRate);});
