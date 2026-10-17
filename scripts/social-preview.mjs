// Code-native share card; derived from the actual interface, not a mock screenshot.
import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'..');
const screenshot=(await fs.readFile(path.join(root,'site/media/desktop.png'))).toString('base64');
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:1200,height:630},deviceScaleFactor:1});
await page.setContent(`<!doctype html><html lang="nl"><head><meta charset="utf-8"><style>*{box-sizing:border-box}body{margin:0;width:1200px;height:630px;background:#fff;color:#162a36;font-family:Arial,sans-serif;padding:52px 58px}header{font-size:26px;font-weight:700;border-bottom:1px solid #dce4e9;padding-bottom:22px}header span{float:right;color:#476078;font-size:15px;font-weight:400;margin-top:8px}main{display:grid;grid-template-columns:470px 1fr;gap:30px;align-items:center;height:430px}h1{font-size:55px;line-height:1.1;letter-spacing:-2px;margin:0 0 25px}p{font-size:21px;line-height:1.5;color:#476078;margin:0}img{width:100%;height:auto;border:1px solid #dce4e9;border-radius:5px}footer{font-size:14px;color:#476078;border-top:1px solid #dce4e9;padding-top:18px}b{color:#bc4224}</style></head><body><header>Batchline<span>Functionele analyse Operations</span></header><main><div><h1>Kwaliteit,<br>planning<br>en ERP.</h1><p>Een kwaliteitsblokkade vertalen naar een onderbouwd herstelplan.</p></div><img src="data:image/png;base64,${screenshot}" alt="De werkende Batchline-interface"></main><footer><b>Onafhankelijke portfolio-case</b> · Fictieve fabrikant · ERP gesimuleerd</footer></body></html>`);
await page.locator('img').evaluate(img=>img.decode());
await page.screenshot({path:path.join(root,'site/media/social.png')});
await browser.close();
console.log('Created 1200×630 social preview from the actual interface.');
