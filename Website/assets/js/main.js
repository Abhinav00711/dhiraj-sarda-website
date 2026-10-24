/* Dhiraj Sarda — site behaviour. No dependencies. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const I18N = window.I18N;
  let LANG = 'en';

  /* ---------------- loader ---------------- */
  const t0 = performance.now();
  const ready = () => setTimeout(() => document.body.classList.add('ready'), Math.max(0, (RM ? 0 : 1500) - (performance.now() - t0)));
  if (document.readyState === 'complete') ready(); else addEventListener('load', ready);
  setTimeout(() => document.body.classList.add('ready'), 3500);

  /* ---------------- split hero name into letters ---------------- */
  function split(el) {
    const txt = el.textContent;
    el.setAttribute('aria-label', txt);
    // keep Devanagari clusters together (letter-splitting breaks matras)
    const state = document.body.classList.contains('ready') ? 'running' : 'paused';
    let i = 0;
    const span = ch => `<span class="ch" aria-hidden="true" style="animation-delay:${(0.6 + i++ * (LANG === 'hi' ? .25 : .06)).toFixed(2)}s;animation-play-state:${state}">${ch}</span>`;
    // words never break apart; Devanagari animates per word (letter-splitting breaks matras)
    el.innerHTML = txt.trim().split(/\s+/).map(w => `<span class="wd">${LANG === 'hi' ? span(w) : [...w].map(span).join('')}</span>`).join(' ');
  }
  const h1 = $('.hero h1');
  split(h1);
  new MutationObserver(() => $$('.split .ch').forEach(c => c.style.animationPlayState = document.body.classList.contains('ready') ? 'running' : 'paused'))
    .observe(document.body, { attributes: true, attributeFilter: ['class'] });

  /* ---------------- starfield + embers ---------------- */
  const mouse = { x: 0, y: 0 };
  addEventListener('pointermove', e => { mouse.x = e.clientX / innerWidth - .5; mouse.y = e.clientY / innerHeight - .5; }, { passive: true });
  function sky(cv) {
    const ctx = cv.getContext('2d');
    const saffron = cv.dataset.embers === 'saffron';
    let w, h, dpr, stars = [], embers = [], on = false, raf;
    const size = () => {
      dpr = Math.min(devicePixelRatio || 1, 2);
      w = cv.clientWidth; h = cv.clientHeight;
      cv.width = w * dpr; cv.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.min(260, (w * h) / 3200 | 0);
      stars = Array.from({ length: n }, () => ({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.2 + .2, p: Math.random() * 6.28, s: Math.random() * .02 + .004, z: Math.random() * .8 + .2 }));
      embers = Array.from({ length: Math.min(46, w / 28 | 0) }, () => ember(true));
    };
    const ember = (init) => ({ x: Math.random() * w, y: init ? Math.random() * h : h + 10, r: Math.random() * 1.8 + .6, v: Math.random() * .35 + .12, a: Math.random() * .6 + .2, ph: Math.random() * 6.28, sw: Math.random() * .6 + .2,
      c: saffron && Math.random() < .55 ? '227,139,58' : '230,203,138' });
    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      for (const s of stars) {
        s.p += s.s;
        const a = .25 + Math.sin(s.p) * .35 + .35;
        ctx.globalAlpha = a; ctx.fillStyle = s.z > .8 ? '#E6CB8A' : '#ffffff';
        ctx.beginPath(); ctx.arc(s.x + mouse.x * 18 * s.z, s.y + mouse.y * 12 * s.z, s.r, 0, 6.283); ctx.fill();
      }
      for (const e of embers) {
        e.y -= e.v; e.ph += .01; e.x += Math.sin(e.ph) * e.sw * .3;
        if (e.y < -10) Object.assign(e, ember(false));
        const fade = Math.min(1, e.y / (h * .35));
        const g = ctx.createRadialGradient(e.x, e.y, 0, e.x, e.y, e.r * 5);
        g.addColorStop(0, `rgba(${e.c},${e.a * fade})`); g.addColorStop(1, `rgba(${e.c},0)`);
        ctx.globalAlpha = 1; ctx.fillStyle = g; ctx.beginPath(); ctx.arc(e.x, e.y, e.r * 5, 0, 6.283); ctx.fill();
      }
      if (on) raf = requestAnimationFrame(draw);
    };
    size(); addEventListener('resize', size);
    if (RM) { draw(); return; }
    new IntersectionObserver(([en]) => { on = en.isIntersecting; cancelAnimationFrame(raf); if (on) draw(); }).observe(cv);
  }
  $$('canvas.sky').forEach(sky);

  /* ---------------- reveal on scroll ---------------- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .14, rootMargin: '0px 0px -40px 0px' });
  $$('[data-r]').forEach(el => io.observe(el));

  /* ---------------- nav ---------------- */
  const nav = $('#nav'), fab = $('.fab');
  const onScroll = () => {
    nav.classList.toggle('solid', scrollY > 40);
    fab.classList.toggle('show', scrollY > innerHeight * .8);
    journey();
  };
  addEventListener('scroll', onScroll, { passive: true });
  $('#burger').addEventListener('click', () => { const o = nav.classList.toggle('open'); $('#burger').setAttribute('aria-expanded', o); });
  $$('.links a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));
  const secIO = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) $$('.links a').forEach(a => a.classList.toggle('act', a.getAttribute('href') === '#' + e.target.id));
  }), { rootMargin: '-45% 0px -50% 0px' });
  $$('main section[id]').forEach(s => secIO.observe(s));

  /* ---------------- parallax + tilt ---------------- */
  if (!RM && matchMedia('(pointer:fine)').matches) {
    const art = $('.hero-art');
    addEventListener('pointermove', () => {
      $$('.par').forEach(el => { const d = +el.dataset.depth || 8; el.style.transform = `translate3d(${mouse.x * d}px,${mouse.y * d}px,0)`; });
      if (art) art.style.transform = `perspective(1200px) rotateY(${mouse.x * 4}deg) rotateX(${-mouse.y * 4}deg)`;
    }, { passive: true });
    $$('.tilt').forEach(c => {
      c.addEventListener('pointermove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.transform = `rotateY(${(x - .5) * 10}deg) rotateX(${(.5 - y) * 10}deg) translateY(-6px)`;
        c.style.setProperty('--mx', x * 100 + '%'); c.style.setProperty('--my', y * 100 + '%');
      });
      c.addEventListener('pointerleave', () => c.style.transform = '');
    });
  }

  /* ---------------- healing wheel ---------------- */
  const nodes = $$('.node'), panels = $$('.wp');
  let wheelAuto = true, wi = 0;
  const pick = i => { wi = i; nodes.forEach((n, k) => n.classList.toggle('on', k === i)); panels.forEach((p, k) => p.classList.toggle('on', k === i)); };
  nodes.forEach(n => n.addEventListener('click', () => { wheelAuto = false; pick(+n.dataset.i); }));
  setInterval(() => { if (wheelAuto && !document.hidden) pick((wi + 1) % nodes.length); }, 4200);
  // size the panel area to the tallest panel
  const fitPanels = () => { const wrap = $('.w-panels'); wrap.style.minHeight = Math.max(...panels.map(p => p.scrollHeight)) + 'px'; };
  addEventListener('resize', fitPanels); setTimeout(fitPanels, 300);

  /* ---------------- journey line ---------------- */
  const stepsEl = $('#steps'), line = $('#steps .line'), stepEls = $$('.step');
  function journey() {
    const r = stepsEl.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (innerHeight * .75 - r.top) / (r.height + innerHeight * .25)));
    line.style.setProperty('--p', p.toFixed(3));
    stepEls.forEach((s, i) => s.classList.toggle('lit', p >= i / (stepEls.length - .2)));
  }

  /* ---------------- verse word reveal ---------------- */
  function splitVerse() {
    const v = $('#verse');
    v.innerHTML = window.VERSE.split('<br>').map(line => line.split(' ').map((w, i) => `<span class="w">${w}</span>`).join(' ')).join('<br>');
    $$('.w', v).forEach((w, i) => w.style.transitionDelay = (i * .18) + 's');
  }
  splitVerse();
  const vIO = new IntersectionObserver(([e]) => { if (e.isIntersecting) { $('.verse').classList.add('in'); vIO.disconnect(); } }, { threshold: .5 });
  vIO.observe($('.verse'));

  /* ---------------- sound: soft tanpura drone (generated, no files) ---------------- */
  let ac, master, droneTimer, soundOn = false;
  const SA = 138.59; // C#3, a common male tanpura pitch
  function initAudio() {
    ac = new (window.AudioContext || window.webkitAudioContext)();
    master = ac.createGain(); master.gain.value = 0;
    const comp = ac.createDynamicsCompressor();
    // simple generated reverb
    const len = ac.sampleRate * 3.2, ir = ac.createBuffer(2, len, ac.sampleRate);
    for (let ch = 0; ch < 2; ch++) { const d = ir.getChannelData(ch); for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 2.6); }
    const verb = ac.createConvolver(); verb.buffer = ir;
    const wet = ac.createGain(); wet.gain.value = .55;
    master.connect(comp); master.connect(verb); verb.connect(wet); wet.connect(comp); comp.connect(ac.destination);
    // constant pad: Sa + Pa sines with slow swell
    [[SA, .05], [SA * 1.5, .028], [SA * 2, .022]].forEach(([f, g], i) => {
      const o = ac.createOscillator(), gn = ac.createGain(), l = ac.createOscillator(), lg = ac.createGain();
      o.type = 'sine'; o.frequency.value = f; gn.gain.value = g;
      l.frequency.value = .05 + i * .03; lg.gain.value = g * .5; l.connect(lg); lg.connect(gn.gain);
      o.connect(gn); gn.connect(master); o.start(); l.start();
    });
  }
  function pluck(f, when, amp = .11) {
    const o = ac.createOscillator(), o2 = ac.createOscillator(), flt = ac.createBiquadFilter(), g = ac.createGain();
    o.type = 'sawtooth'; o2.type = 'sawtooth'; o.frequency.value = f; o2.frequency.value = f * 1.0035;
    flt.type = 'lowpass'; flt.Q.value = 7;
    flt.frequency.setValueAtTime(f * 9, when); flt.frequency.exponentialRampToValueAtTime(f * 2.2, when + 3); // the "jivari" shimmer
    g.gain.setValueAtTime(0, when); g.gain.linearRampToValueAtTime(amp, when + .03); g.gain.exponentialRampToValueAtTime(.0008, when + 4.2);
    o.connect(flt); o2.connect(flt); flt.connect(g); g.connect(master);
    o.start(when); o2.start(when); o.stop(when + 4.4); o2.stop(when + 4.4);
  }
  function cycle() {
    const t = ac.currentTime + .05, s = 1.05;
    pluck(SA * .75, t); pluck(SA, t + s, .09); pluck(SA, t + s * 2, .09); pluck(SA / 2, t + s * 3, .13);
  }
  function bell() {
    if (!soundOn) return;
    const t = ac.currentTime, o = ac.createOscillator(), g = ac.createGain();
    o.type = 'sine'; o.frequency.value = SA * 4; g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.05, t + .02); g.gain.exponentialRampToValueAtTime(.0005, t + 3);
    o.connect(g); g.connect(master); o.start(t); o.stop(t + 3.1);
  }
  const sndBtn = $('#snd');
  sndBtn.addEventListener('click', () => {
    if (!ac) initAudio();
    soundOn = !soundOn; sndBtn.setAttribute('aria-pressed', soundOn);
    const t = ac.currentTime;
    master.gain.cancelScheduledValues(t); master.gain.setValueAtTime(master.gain.value, t);
    if (soundOn) { ac.resume(); master.gain.linearRampToValueAtTime(.9, t + 2.5); cycle(); droneTimer = setInterval(cycle, 4200); }
    else { master.gain.linearRampToValueAtTime(0, t + 1.2); clearInterval(droneTimer); }
  });

  /* ---------------- breathe with me (4 in · 4 hold · 6 out) ---------------- */
  const lw = $('.lotus-wrap'), label = $('#brLabel'), prog = $('#brProg'), brBtn = $('#brBtn'), brN = $('#brN');
  const PH = [['br_in', 4000], ['br_hold', 4000], ['br_out', 6000]], TOTAL = 14000;
  let brOn = false, brStart = 0, brRaf, lastPh = -1, count = 0;
  const ease = x => .5 - Math.cos(Math.PI * x) / 2;
  function brFrame(now) {
    const t = (now - brStart) % TOTAL;
    let acc = 0, ph = 0;
    while (t >= acc + PH[ph][1]) acc += PH[ph++][1];
    const f = (t - acc) / PH[ph][1];
    const o = ph === 0 ? ease(f) : ph === 1 ? 1 : 1 - ease(f);
    lw.style.setProperty('--o', o.toFixed(4));
    prog.style.strokeDashoffset = (1 - t / TOTAL).toFixed(4);
    if (ph !== lastPh) {
      if (ph === 0 && lastPh === 2) brN.textContent = ++count;
      if (ph === 0) bell();
      lastPh = ph; label.style.opacity = 0;
      setTimeout(() => { label.innerHTML = I18N[LANG][PH[ph][0]]; label.style.opacity = 1; }, 250);
    }
    brRaf = requestAnimationFrame(brFrame);
  }
  brBtn.addEventListener('click', () => {
    brOn = !brOn;
    $('span', brBtn).innerHTML = I18N[LANG][brOn ? 'br_stop' : 'br_start'];
    $('span', brBtn).dataset.k = brOn ? 'br_stop' : 'br_start';
    if (brOn) { brStart = performance.now(); lastPh = -1; brRaf = requestAnimationFrame(brFrame); }
    else { cancelAnimationFrame(brRaf); lw.style.setProperty('--o', 0); prog.style.strokeDashoffset = 1; label.innerHTML = '&nbsp;'; }
  });
  // idle "breathing" preview until the visitor starts
  if (!RM) { let p = 0; (function idle() { if (!brOn) { p += .012; lw.style.setProperty('--o', (.35 + Math.sin(p) * .25).toFixed(3)); } requestAnimationFrame(idle); })(); }

  /* ---------------- language ---------------- */
  const waLink = lang => `https://wa.me/${window.WA_NUM}?text=${encodeURIComponent(lang === 'hi' ? 'नमस्ते धीरज जी, मैं एक सत्र बुक करना चाहता/चाहती हूँ।' : 'Namaste Dhiraj ji, I would like to book a session.')}`;
  function setLang(l) {
    LANG = l; const D = I18N[l];
    document.documentElement.lang = l; document.body.classList.toggle('hi', l === 'hi');
    $$('[data-k]').forEach(el => { const v = D[el.dataset.k]; if (typeof v === 'string') el.innerHTML = v; });
    split(h1);
    $('#concern').innerHTML = D.opts.map(o => `<option>${o}</option>`).join('');
    const mq = D.marquee.map(x => `<span>${x}</span><b>✦</b>`).join('');
    $('#mq').innerHTML = mq + mq;
    $$('[data-wa]').forEach(a => a.href = waLink(l));
    document.title = D.meta_title.replace(/&amp;/g, '&');
    if (!brOn) label.innerHTML = '&nbsp;';
    setTimeout(fitPanels, 50);
    try { localStorage.setItem('lang', l); } catch (e) {}
  }
  $('#lang').addEventListener('click', () => setLang(LANG === 'en' ? 'hi' : 'en'));
  const q = new URLSearchParams(location.search).get('lang');
  let saved = null; try { saved = localStorage.getItem('lang'); } catch (e) {}
  if ((q || saved) === 'hi') setLang('hi');

  /* ---------------- booking form -> WhatsApp ---------------- */
  $('#form').addEventListener('submit', e => {
    e.preventDefault();
    const f = e.target, D = I18N[LANG], name = f.name.value.trim();
    f.name.classList.toggle('invalid', !name);
    if (!name) { f.name.focus(); return; }
    const strip = s => s.replace(/&amp;/g, '&').replace(/&[a-z]+;/g, ' ').replace(/<[^>]+>/g, '');
    const lines = [`${D.wa_hello} 🙏`, `${D.wa_name}: ${name}`, `${strip(D.wa_concern)}: ${strip(f.concern.value)}`,
      `${D.wa_mode}: ${strip(f.mode.value === 'online' ? D.f_online : D.f_person)}`];
    if (f.time.value.trim()) lines.push(`${D.wa_time}: ${f.time.value.trim()}`);
    if (f.msg.value.trim()) lines.push(`${D.wa_note}: ${f.msg.value.trim()}`);
    window.open(`https://wa.me/${window.WA_NUM}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
  });

  onScroll();
})();
