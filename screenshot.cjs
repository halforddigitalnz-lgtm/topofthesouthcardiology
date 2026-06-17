const puppeteer = require('./node_modules/puppeteer-core');
const { mkdirSync, readdirSync } = require('fs');
const { join } = require('path');

const url = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] ? `-${process.argv[3]}` : '';
const scrollY = parseInt(process.argv[4] || '0');

const screenshotsDir = join(__dirname, 'temporary screenshots');
mkdirSync(screenshotsDir, { recursive: true });

const existing = readdirSync(screenshotsDir).filter(f => f.startsWith('screenshot-') && f.endsWith('.png'));
const nums = existing.map(f => parseInt(f.match(/screenshot-(\d+)/)?.[1] || '0')).filter(n => !isNaN(n) && n > 0);
const nextNum = nums.length ? Math.max(...nums) + 1 : 1;
const outPath = join(screenshotsDir, `screenshot-${nextNum}${label}.png`);

const chromePath = '/Users/tomlekkerkerker/.cache/puppeteer/chrome/mac_arm-149.0.7827.22/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing';

(async () => {
  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--disable-setuid-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });

  // Block video and heavy assets to speed up load
  await page.setRequestInterception(true);
  page.on('request', req => {
    const type = req.resourceType();
    if (type === 'media') {
      req.abort();
    } else {
      req.continue();
    }
  });

  await page.goto(url, { waitUntil: 'load', timeout: 12000 }).catch(() => {});
  await new Promise(r => setTimeout(r, 1500));

  if (scrollY > 0) {
    await page.evaluate((y) => {
      // Trigger all reveal animations instantly
      document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
      document.querySelectorAll('.ecg-reveal').forEach(el => el.classList.add('drawn'));
      window.scrollTo(0, y);
    }, scrollY);
    await new Promise(r => setTimeout(r, 600));
  } else {
    await page.evaluate(() => {
      document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    });
    await new Promise(r => setTimeout(r, 400));
  }

  await page.screenshot({ path: outPath });
  await browser.close();
  console.log(`Saved: ${outPath}`);
})();
