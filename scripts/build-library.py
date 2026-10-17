"""Publish project documentation as static, readable pages without runtime dependencies."""
from pathlib import Path
import re, html, shutil, os
from urllib.parse import urlsplit, urlunsplit
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/library'
current_source=ROOT/'README.md'
current_target=OUT/'README.html'
def inline(s):
 s=html.escape(s)
 def link(m):
  label,url=m.groups();url=html.unescape(url)
  if not url.startswith(('http:','https:','#','mailto:')):
   u=urlsplit(url);source=(current_source.parent/u.path).resolve()
   if source.is_relative_to(ROOT/'site'):
    destination=source
   else:
    destination=OUT/source.relative_to(ROOT)
    if destination.suffix=='.md':destination=destination.with_suffix('.html')
   url=urlunsplit(('', '', os.path.relpath(destination,current_target.parent),u.query,u.fragment))
  return '<a href="'+html.escape(url,quote=True)+'">'+label+'</a>'
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 return s
def render(text):
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i]
  if line.startswith('```'):
   language=line[3:];code=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
  elif line.startswith('#'):
   level=min(6,len(line)-len(line.lstrip('#')));out.append(f'<h{level}>'+inline(line[level:].strip())+f'</h{level}>')
  elif line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    cells=lines[i].strip('|').split('|')
    if not all(re.match(r'^\s*:?-+:?\s*$',c) for c in cells):rows.append(cells)
    i+=1
   out.append('<div class="table-scroll"><table>'+''.join('<tr>'+''.join(('<th>' if idx==0 else '<td>')+inline(c.strip())+('</th>' if idx==0 else '</td>') for c in row)+'</tr>' for idx,row in enumerate(rows))+'</table></div>');i-=1
  elif re.match(r'^[-*] ',line) or re.match(r'^\d+\. ',line):out.append('<p class="list-item">'+inline(line)+'</p>')
  elif line.strip():out.append('<p>'+inline(line)+'</p>')
  i+=1
 return '\n'.join(out)
files=[]
for folder in ['docs','application-kit','contracts','data','tests','scripts']:
 files+=list((ROOT/folder).rglob('*'))
files += [ROOT/p for p in ['README.md','START-HERE.md','EVIDENCE.md','CASE_STUDY.md','LICENSE','LICENSE-DOCS.md']]
files.append(ROOT/'site/assets/domain.mjs')
count=0
for p in files:
 if not p.is_file():continue
 rel=p.relative_to(ROOT);target=OUT/rel;target.parent.mkdir(parents=True,exist_ok=True)
 if p.suffix=='.md':
  target=target.with_suffix('.html');depth=len(target.relative_to(ROOT/'site').parts)-1;base='../'*depth
  current_source=p;current_target=target
  title=p.read_text().splitlines()[0].lstrip('# ')
  target.write_text('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+' — Batchline</title><link rel="stylesheet" href="'+base+'assets/style.css"><style>pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f6f7;padding:18px;font-size:12px}td,th{min-width:100px}code{overflow-wrap:anywhere}h2{margin-top:32px}.list-item{padding-left:16px}h1{font-size:36px}</style></head><body><main class="reading"><a class="brand" href="'+base+'index.html">Batchline</a><nav class="doc-nav"><a href="'+base+'case.html">Case & bewijs</a><a href="'+base+'index.html?tour">Demo</a></nav>'+render(p.read_text())+'<footer class="footer">Onafhankelijke portfoliocase · fictieve organisatie · ERP gesimuleerd</footer></main></body></html>')
 else:shutil.copyfile(p,target)
 count+=1
print(f'Static documentation library: {count} artifacts')
