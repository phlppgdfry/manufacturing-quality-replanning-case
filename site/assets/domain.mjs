// All quantities are whole m². This model is deliberately not SAP stock logic.
export class DomainError extends Error {
  constructor(code, message) { super(message); this.code = code; }
}
const fail = (code, message) => { throw new DomainError(code, message); };
const roles = { quality: ['decide', 'releaseRework'], planner: ['commitPlan'], operator: ['report', 'finishJob'], integration: ['sync', 'reconcile'] };
function allow(role, action) { if (!roles[role]?.includes(action)) fail('FORBIDDEN', 'Deze demonstratierol mag deze actie niet uitvoeren.'); }
function version(s, expected) { if (s.version !== expected) fail('STALE_VERSION', 'De gegevens zijn gewijzigd. Herlaad en beoordeel opnieuw.'); }
function qty(n) { if (!Number.isSafeInteger(n) || n < 0) fail('INVALID_QUANTITY', 'Gebruik een niet-negatief geheel aantal m².'); }
function event(s, type, detail, role) {
  s.version += 1;
  s.audit.push({ sequence: s.audit.length + 1, type, detail, role, version: s.version });
}
function stockEvent(s) {
  const payload = { batchId: s.batch.id, version: s.version, released: s.batch.released, held: s.batch.held, rework: s.batch.rework, scrap: s.batch.scrap, produced: s.batch.produced };
  s.outbox.push({ id: `EV-${s.version}`, key: `${s.batch.id}:${s.version}`, payload, status: 'pending', attempts: 0, error: null });
}
export function seed() {
  return {
    schema: 1, version: 1, planVersion: 1, nextJob: 1,
    batch: { id: 'B-2401', product: 'Dakpaneel 900', profile: 'DP900', produced: 100, released: 60, held: 40, rework: 0, scrap: 0 },
    issue: { id: 'QN-017', reason: 'Coatingbeschadiging', quantity: 40, status: 'open', decision: null },
    orders: [
      { id: 'SO-1041', product: 'Dakpaneel 1060', demand: 120, ready: 120, due: 960 },
      { id: 'SO-1042', product: 'Dakpaneel 900', demand: 100, ready: 60, due: 960 },
      { id: 'SO-1043', product: 'Dakpaneel 750', demand: 60, ready: 60, due: 1020 }
    ],
    machines: [
      { id: 'A', name: 'Lijn A', profiles: ['DP900', 'DP1060'], rate: 2, setup: 20, start: 480, end: 1020 },
      { id: 'B', name: 'Lijn B', profiles: ['DP900', 'DP750'], rate: 3, setup: 30, start: 480, end: 1020 }
    ],
    jobs: [
      { id: 'PO-2401', machine: 'A', start: 480, end: 600, order: 'SO-1042', type: 'original', status: 'done', quantity: 100 },
      { id: 'PO-2402', machine: 'A', start: 600, end: 720, order: 'SO-1041', type: 'original', status: 'done', quantity: 120 },
      { id: 'PO-2403', machine: 'A', start: 780, end: 900, order: 'SO-1043', type: 'original', status: 'scheduled', quantity: 60 },
      { id: 'PO-2404', machine: 'B', start: 480, end: 660, order: 'SO-1039', type: 'original', status: 'done', quantity: 80 },
      { id: 'PO-2405', machine: 'B', start: 780, end: 900, order: 'SO-1044', type: 'original', status: 'scheduled', quantity: 60 }
    ],
    plan: null, childLots: [], outbox: [], receiver: { latestVersion: 0, stock: null, receipts: {} },
    audit: [{ sequence: 1, type: 'HOLD_REGISTERED', role: 'operator', detail: 'QN-017: 40 m² geblokkeerd op B-2401; fictieve beginsituatie', version: 1 }]
  };
}
export function assertState(s) {
  if (s?.schema !== 1 || !Number.isSafeInteger(s.version) || s.version < 1 || !Number.isSafeInteger(s.planVersion) || !s.batch || !s.issue || !s.receiver || !s.receiver.receipts || !Array.isArray(s.audit) || !Array.isArray(s.outbox) || !Array.isArray(s.childLots) || !Array.isArray(s.jobs) || !Array.isArray(s.machines) || !Array.isArray(s.orders) || s.orders.length !== 3 || !s.orders.every(o => typeof o.id === 'string' && typeof o.product === 'string' && Number.isSafeInteger(o.demand) && Number.isSafeInteger(o.due)) || !s.machines.every(m => Array.isArray(m.profiles))) fail('INVALID_STATE', 'Oefenopslag ongeldig. Reset de demo.');
  for (const f of ['produced', 'released', 'held', 'rework', 'scrap']) qty(s.batch[f]);
  if (s.batch.produced !== s.batch.released + s.batch.held + s.batch.rework + s.batch.scrap) fail('CONSERVATION', 'De hoeveelheidbalans klopt niet.');
  return s;
}
export function shortage(s) { return Math.max(0, s.orders[1].demand - s.batch.released); }
export function canShip(s) {
  const stock = s.receiver.stock;
  return shortage(s) === 0 && stock !== null && ['produced','released','held','rework','scrap'].every(k => stock[k] === s.batch[k]) && s.outbox.every(x => ['acked','superseded'].includes(x.status));
}
export function late(s) { return Math.max(s.plan?.end || 0, s.orders[1].readyAt || 0) > s.orders[1].due; }
export function metrics(s) { return { orders: s.orders.length, blocked: s.batch.held + s.batch.rework, atRisk: canShip(s) && !late(s) ? 0 : 1, shortage: shortage(s), unsynced: s.outbox.filter(x => !['acked', 'superseded'].includes(x.status)).length }; }
export function report(s, { role, expectedVersion, quantity, reason }) {
  allow(role, 'report'); version(s, expectedVersion); qty(quantity);
  if (!quantity || quantity > s.batch.released) fail('OVER_HOLD', 'Blokkade moet positief zijn en binnen de vrijgegeven hoeveelheid vallen.');
  if (!reason?.trim()) fail('REASON_REQUIRED', 'Een reden is verplicht.');
  if (s.issue.status !== 'closed' || s.plan?.status === 'committed') fail('ISSUE_OPEN', 'Rond de bestaande afwijking en het herstelplan eerst af.');
  const n = structuredClone(s); n.batch.released -= quantity; n.batch.held += quantity;
  n.issue = { id: `QN-${String(n.version + 17).padStart(3, '0')}`, reason: reason.trim(), quantity, status: 'open', decision: null }; n.plan = null;
  event(n, 'HOLD_REGISTERED', `${quantity} m²: ${reason.trim()}`, role); stockEvent(n); return assertState(n);
}
export function decide(s, { role, expectedVersion, release, rework, scrap, reason }) {
  allow(role, 'decide'); version(s, expectedVersion); [release, rework, scrap].forEach(qty);
  if (s.issue.status !== 'open') fail('ALREADY_DECIDED', 'Deze afwijking is al beoordeeld.');
  if (release + rework + scrap !== s.batch.held) fail('QUANTITY_SUM', 'Vrijgave, herwerk en afkeur moeten samen de geblokkeerde hoeveelheid vormen.');
  if (!reason?.trim()) fail('REASON_REQUIRED', 'Een onderbouwde kwaliteitsbeslissing is verplicht.');
  const n = structuredClone(s); n.batch.released += release; n.batch.rework += rework; n.batch.scrap += scrap; n.batch.held = 0;
  n.issue.status = rework > 0 ? 'rework' : 'closed'; n.issue.decision = { release, rework, scrap, reason: reason.trim() };
  event(n, 'QUALITY_DECIDED', `${release} vrij, ${rework} herwerk, ${scrap} afkeur. ${reason.trim()}`, role); stockEvent(n); return assertState(n);
}
export function firstGap(machine, jobs, duration, earliest = 720) {
  if (!Number.isFinite(duration) || duration <= 0) fail('INVALID_DURATION', 'Een tijdvak moet een positieve eindige duur hebben.');
  let cursor = Math.max(machine.start, earliest);
  for (const j of jobs.filter(j => j.machine === machine.id).sort((a, b) => a.start - b.start)) {
    if (j.end <= cursor) continue;
    if (cursor + duration <= Math.min(j.start, machine.end)) return cursor;
    cursor = Math.max(cursor, j.end);
  }
  return cursor + duration <= machine.end ? cursor : null;
}
export function alternatives(s) {
  if (s.issue.status === 'open' || shortage(s) === 0 || ['committed', 'awaiting-quality'].includes(s.plan?.status)) return [];
  const results = [];
  for (const strategy of (s.batch.rework ? ['recover', 'replace'] : ['replace'])) {
    for (const machine of s.machines) {
      if (!machine.profiles.includes(s.batch.profile)) continue;
      const recovery = strategy === 'recover' ? Math.min(s.batch.rework, shortage(s)) : 0;
      const production = shortage(s) - recovery;
      // A single combined slot includes setup, rework and replacement; QC lead time is explicit.
      const duration = machine.setup + recovery * 2 + production * machine.rate + 20;
      const start = firstGap(machine, s.jobs, duration);
      if (start === null) continue;
      const end = start + duration;
      results.push({ id: `${strategy}-${machine.id}`, strategy, machine: machine.id, start, end, duration, recovery, production, stateVersion: s.version, planVersion: s.planVersion, onTime: end <= s.orders[1].due, explanation: `${machine.name}: ${recovery} m² herwerk + ${production} m² vervanging; inclusief omstel en 20 min kwaliteitscontrole.` });
    }
  }
  return results.sort((a, b) => Number(b.onTime) - Number(a.onTime) || a.production - b.production || a.end - b.end);
}
export function commitPlan(s, { role, expectedVersion, option, reason }) {
  allow(role, 'commitPlan'); version(s, expectedVersion);
  if (!reason?.trim()) fail('REASON_REQUIRED', 'Motiveer de keuze voor het herstelplan.');
  if (['committed','awaiting-quality'].includes(s.plan?.status)) fail('RECOVERY_ACTIVE', 'Rond het actieve herstel en de herkeuring af vóór een nieuw plan.');
  const fresh = alternatives(s).find(x => x.id === option?.id);
  if (!fresh || option.planVersion !== s.planVersion || option.stateVersion !== s.version || Object.keys(option).length !== Object.keys(fresh).length || !Object.keys(fresh).every(k => option[k] === fresh[k])) fail('STALE_PLAN', 'Dit voorstel is verouderd of gewijzigd; vergelijk opnieuw.');
  const n = structuredClone(s); const id = `RP-${n.nextJob++}`;
  n.jobs.push({ id, machine: fresh.machine, start: fresh.start, end: fresh.end, order: 'SO-1042', type: 'recovery', status: 'scheduled', quantity: fresh.production + fresh.recovery });
  n.plan = { ...fresh, jobId: id, status: 'committed', reason: reason.trim() }; n.planVersion += 1;
  event(n, 'PLAN_COMMITTED', `${id} op lijn ${fresh.machine}; ${reason.trim()}`, role); return assertState(n);
}
export function finishJob(s, { role, expectedVersion }) {
  allow(role, 'finishJob'); version(s, expectedVersion);
  if (s.plan?.status !== 'committed') fail('NO_PLAN', 'Er is geen actief herstelplan.');
  const n = structuredClone(s); const p = n.plan;
  // New material waits in quality hold; existing rework remains rework until quality accepts it.
  n.batch.produced += p.production; n.batch.held += p.production;
  if (p.production) n.childLots.push({ id: `${n.batch.id}-${p.jobId}`, parent: n.batch.id, quantity: p.production, status: 'inspection' });
  n.jobs.find(j => j.id === p.jobId).status = 'done'; p.status = 'awaiting-quality';
  event(n, 'RECOVERY_PRODUCED', `${p.production} m² nieuw in controle; ${p.recovery} m² herwerk wacht op kwaliteitsvrijgave.`, role); stockEvent(n); return assertState(n);
}
export function releaseRework(s, { role, expectedVersion, reason }) {
  allow(role, 'releaseRework'); version(s, expectedVersion);
  if (s.plan?.status !== 'awaiting-quality') fail('NOT_READY', 'Herstelproductie moet eerst gereed zijn.');
  if (!reason?.trim()) fail('REASON_REQUIRED', 'Controlebevinding en vrijgavereden zijn verplicht.');
  const n = structuredClone(s); const p = n.plan;
  n.batch.held -= p.production; n.batch.rework -= p.recovery; n.batch.released += p.production + p.recovery;
  n.orders[1].readyAt = Math.max(n.orders[1].readyAt || 0, p.end);
  p.status = 'complete'; n.issue.status = n.batch.rework ? 'rework' : 'closed';
  const child = n.childLots.find(x => x.id === `${n.batch.id}-${p.jobId}`); if (child) child.status = 'released';
  event(n, 'RECOVERY_RELEASED', reason.trim(), role); stockEvent(n); return assertState(n);
}
export function receive(receiver, message) {
  const r = structuredClone(receiver); const p = message.payload;
  const fields = ['batchId','version','produced','released','held','rework','scrap'];
  if (!p || typeof p !== 'object' || Object.keys(p).length !== fields.length || !fields.every(f => Object.hasOwn(p,f))) fail('INVALID_PAYLOAD', 'Het bericht moet exact de afgesproken voorraadvelden bevatten.');
  for (const f of ['version', 'produced', 'released', 'held', 'rework', 'scrap']) qty(p[f]);
  if (p.batchId !== 'B-2401' || message.key !== `${p.batchId}:${p.version}` || p.produced !== p.released + p.held + p.rework + p.scrap) fail('INVALID_PAYLOAD', 'Ontvangst geweigerd: berichtbalans of sleutel ongeldig.');
  // Field order in JSON is not business content. Fingerprint the explicit contract fields.
  const fingerprint = JSON.stringify(fields.map(f => p[f]));
  if (Object.hasOwn(r.receipts, message.key)) {
    let stored = r.receipts[message.key];
    try { const legacy = JSON.parse(stored); if (!Array.isArray(legacy)) stored = JSON.stringify(fields.map(f => legacy[f])); } catch { fail('INVALID_PAYLOAD', 'Ontvangstregister ongeldig.'); }
    if (stored !== fingerprint) fail('IDEMPOTENCY_CONFLICT', 'Dezelfde sleutel heeft een andere inhoud.');
    return { receiver: r, duplicate: true, stale: false };
  }
  r.receipts[message.key] = fingerprint;
  if (p.version <= r.latestVersion) return { receiver: r, duplicate: false, stale: true };
  r.stock = structuredClone(p); r.latestVersion = p.version;
  return { receiver: r, duplicate: false, stale: false };
}
export function sync(s, { role, expectedVersion, mode = 'normal' }) {
  allow(role, 'sync'); version(s, expectedVersion);
  if (!['normal', 'offline', 'lost-ack'].includes(mode)) fail('INVALID_MODE', 'Ongeldige storingsmodus.');
  const n = structuredClone(s); const m = n.outbox.find(x => ['pending', 'retry'].includes(x.status));
  if (!m) fail('NO_MESSAGE', 'Geen bericht klaar. Onderzoek een dead-letter voor handmatige herstart.');
  m.attempts += 1;
  if (mode === 'offline') { m.status = m.attempts >= 3 ? 'dead-letter' : 'retry'; m.error = 'ERP niet bereikbaar'; }
  else {
    const result = receive(n.receiver, m); n.receiver = result.receiver;
    if (mode === 'lost-ack') { m.status = m.attempts >= 3 ? 'dead-letter' : 'retry'; m.error = 'ERP verwerkt; bevestiging verloren'; }
    else { m.status = result.stale ? 'superseded' : 'acked'; m.error = null; }
  }
  event(n, 'ERP_DELIVERY', `${m.id}: ${m.status}, poging ${m.attempts}, modus ${mode}`, role); return assertState(n);
}
export function reconcile(s, { role, expectedVersion, reason }) {
  allow(role, 'reconcile'); version(s, expectedVersion);
  if (!reason?.trim()) fail('REASON_REQUIRED', 'Noteer de diagnose vóór herstart.');
  const n = structuredClone(s); const failed = n.outbox.filter(m => m.status === 'dead-letter');
  if (!failed.length) fail('NO_DEAD_LETTER', 'Er is geen dead-letter.');
  for (const m of failed) { m.status = 'retry'; m.attempts = 0; m.error = null; }
  event(n, 'REPLAY_APPROVED', reason.trim(), role); return assertState(n);
}
export const clock = minutes => `${String(Math.floor(minutes / 60)).padStart(2, '0')}:${String(minutes % 60).padStart(2, '0')}`;
