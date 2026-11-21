// usage: node render.js <page.html> <out.mp4> <durationSec> [fps]
// The page must define window.seek(t) that draws the frame at time t (seconds).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
(async () => {
  const [html, out, dur, fpsArg] = process.argv.slice(2);
  const fps = +(fpsArg || 30), total = Math.round(+dur * fps);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.resolve(html));
  await page.evaluate(() => document.fonts.ready);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.seek(t), i / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % (fps * 10) === 0) process.stderr.write(`frame ${i}/${total}\n`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await browser.close();
})();
