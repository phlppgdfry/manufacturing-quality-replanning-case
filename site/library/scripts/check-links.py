"""Check project-relative Markdown/HTML links, image sources and local module imports."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re, sys
ROOT=Path(__file__).resolve().parent.parent
errors=[]; checked=0
for p in ROOT.rglob('*'):
 if not p.is_file() or any(x in p.parts for x in ['node_modules','.git','test-results','.firecrawl','tmp']): continue
 if p.suffix not in ['.md','.html','.mjs','.css']:continue
 s=p.read_text()
 links=[]
 if p.suffix=='.md':links=re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)',s)
 elif p.suffix=='.html':links=re.findall(r'(?:href|src)=[\"\']([^\"\']+)',s)
 elif p.suffix=='.mjs':links=re.findall(r'(?:from\s+|import\s*)[\"\'](\.[^\"\']+)',s)
 for link in links:
  link=link.strip('<>');u=urlsplit(link)
  if u.scheme or link.startswith('//'):continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  checked+=1
  if not target.exists():errors.append(f'{p.relative_to(ROOT)} -> {link}');continue
  if p.suffix=='.html' and u.fragment and target.suffix=='.html':
   fragment=unquote(u.fragment)
   ids=re.findall(r'id=[\"\']([^\"\']+)',target.read_text())
   if fragment not in ids:errors.append(f'{p.relative_to(ROOT)} -> ontbrekend anker {link}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'Local links/modules: {checked} checked, no missing targets.')
