"""Publish project documentation as static, readable pages without runtime dependencies."""
from pathlib import Path
import re, html, shutil, os
from urllib.parse import urlsplit, urlunsplit
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/library'
current_source=ROOT/'README.md'
current_target=OUT/'README.html'
def slug(text):
 return re.sub(r'[^\w\-]+','-',text.lower()).strip('-')
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
   diagrams={'architecture.md':'architecture.svg','data-model.md':'data-model.svg'}
   if language=='mermaid' and current_source.name in diagrams:
    image=OUT/'docs/diagrams'/diagrams[current_source.name]
    out.append('<figure class="doc-diagram"><img src="'+os.path.relpath(image,current_target.parent)+'" alt="'+html.escape('Architectuur' if current_source.name=='architecture.md' else 'Logisch datamodel')+'"><figcaption>Open de SVG of het bronmodel voor detailinspectie.</figcaption></figure>')
   else:out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>')
  elif line.startswith('#'):
   level=min(6,len(line)-len(line.lstrip('#')));title=line[level:].strip();out.append(f'<h{level} id="{slug(title)}">'+inline(title)+f'</h{level}>')
  elif line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    cells=lines[i].strip('|').split('|')
    if not all(re.match(r'^\s*:?-+:?\s*$',c) for c in cells):rows.append(cells)
    i+=1
   head='<thead><tr>'+''.join('<th scope="col">'+inline(c.strip())+'</th>' for c in rows[0])+'</tr></thead>'
   body='<tbody>'+''.join('<tr>'+''.join('<td>'+inline(c.strip())+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody>'
   out.append('<div class="table-scroll"><table>'+head+body+'</table></div>');i-=1
  elif re.match(r'^[-*] ',line) or re.match(r'^\d+\. ',line):
   ordered=bool(re.match(r'^\d+\. ',line));pattern=r'^\d+\. ' if ordered else r'^[-*] ';items=[]
   while i<len(lines) and re.match(pattern,lines[i]):
    items.append('<li>'+inline(re.sub(pattern,'',lines[i]))+'</li>');i+=1
   kind='ol' if ordered else 'ul';out.append('<'+kind+'>'+''.join(items)+'</'+kind+'>');i-=1
  elif line.startswith('> '):out.append('<blockquote>'+inline(line[2:])+'</blockquote>')
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
  content=render(p.read_text())
  headings=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',content)
  if headings:
   toc='<nav class="doc-toc" aria-label="In dit document">'+''.join('<a href="#'+anchor+'">'+label+'</a>' for anchor,label in headings)+'</nav>'
   content=re.sub(r'(</h1>)',r'\1'+toc,content,count=1)
  target.write_text('<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+' — Batchline</title><meta name="description" content="'+html.escape(title,quote=True)+' — functionele-analysecase met fictieve data"><link rel="stylesheet" href="'+base+'assets/style.css"><style>pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f6f7;padding:18px;font-size:12px}td,th{min-width:100px}code{overflow-wrap:anywhere}h2{margin-top:32px}.list-item{padding-left:16px}h1{font-size:36px}</style></head><body><main class="reading"><a class="brand" href="'+base+'index.html">Batchline</a><nav class="doc-nav"><a href="'+base+'case.html">Case & bewijs</a><a href="'+base+'index.html?tour">Demo</a></nav>'+content+'<footer class="footer">Onafhankelijke portfoliocase · fictieve organisatie · ERP gesimuleerd</footer></main></body></html>')
 else:shutil.copyfile(p,target)
 count+=1
print(f'Static documentation library: {count} artifacts')
