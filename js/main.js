(function () {
  var doc = document, root = doc.documentElement;
  root.classList.remove('no-js');

  doc.querySelectorAll('[data-icon]').forEach(function (el) { el.innerHTML = (window.TRUST_ICONS || {})[el.dataset.icon] || ''; });

  /* ---------- Idioma (ES por defecto; EN en atributos data-en) ---------- */
  var lang = 'es';
  try {
    var qs = new URLSearchParams(location.search).get('lang');
    var saved = localStorage.getItem('trust-lang');
    lang = qs === 'en' || qs === 'es' ? qs : (saved === 'en' ? 'en' : 'es');
  } catch (e) {}

  function applyLang() {
    root.lang = lang;
    doc.querySelectorAll('[data-en]').forEach(function (el) {
      if (!el.hasAttribute('data-es')) el.setAttribute('data-es', el.innerHTML);
      el.innerHTML = lang === 'en' ? el.getAttribute('data-en') : el.getAttribute('data-es');
    });
    doc.querySelectorAll('[data-en-placeholder]').forEach(function (el) {
      if (!el.hasAttribute('data-es-placeholder')) el.setAttribute('data-es-placeholder', el.placeholder);
      el.placeholder = lang === 'en' ? el.getAttribute('data-en-placeholder') : el.getAttribute('data-es-placeholder');
    });
    var t = doc.getElementById('lang-toggle'); if (t) t.textContent = lang === 'es' ? 'EN' : 'ES';
    try { localStorage.setItem('trust-lang', lang); } catch (e) {}
  }
  function T(es, en) { return lang === 'en' ? en : es; }
  var langBtn = doc.getElementById('lang-toggle');
  if (langBtn) langBtn.addEventListener('click', function () { lang = lang === 'es' ? 'en' : 'es'; applyLang(); });
  var yr = doc.getElementById('year'); if (yr) yr.textContent = new Date().getFullYear();
  applyLang();

  /* ---------- Menú móvil ---------- */
  var menuBtn = doc.getElementById('menu-toggle'), nav = doc.getElementById('nav');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = doc.body.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { doc.body.classList.remove('menu-open'); menuBtn.setAttribute('aria-expanded', 'false'); }
    });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') doc.body.classList.remove('menu-open'); });
  }

  /* ---------- Progreso de scroll ---------- */
  var bar = doc.getElementById('progress');
  function onScroll() {
    if (!bar) return;
    var h = root.scrollHeight - innerHeight;
    bar.style.width = (h > 0 ? (scrollY / h) * 100 : 0) + '%';
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- Revelado + contadores ---------- */
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function countUp(el) {
    var end = parseFloat(el.dataset.count), pre = el.dataset.prefix || '', suf = el.dataset.suffix || '';
    if (reduce) { el.textContent = pre + end + suf; return; }
    var t0 = null, dur = 1600;
    (function step(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + Math.round(end * e) + suf;
      if (p < 1) requestAnimationFrame(step);
    })(performance.now());
  }
  var els = doc.querySelectorAll('.reveal, [data-count]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        if (en.target.dataset.count) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: .15 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); if (el.dataset.count) el.textContent = (el.dataset.prefix || '') + el.dataset.count + (el.dataset.suffix || ''); });
  }

  /* ---------- Carrusel ---------- */
  doc.querySelectorAll('[data-carousel]').forEach(function (wrap) {
    var track = wrap.querySelector('.carousel');
    wrap.querySelectorAll('[data-dir]').forEach(function (b) {
      b.addEventListener('click', function () {
        var card = track.querySelector('.quote');
        track.scrollBy({ left: (card ? card.offsetWidth + 20 : 400) * Number(b.dataset.dir), behavior: 'smooth' });
      });
    });
  });

  /* ---------- Cotizador rápido (home) → contacto ---------- */
  var qf = doc.getElementById('quick-quote');
  if (qf) {
    qf.addEventListener('submit', function (e) {
      e.preventDefault();
      var zip = qf.zip.value.trim(), err = doc.getElementById('quick-err');
      if (!/^\d{5}$/.test(zip)) {
        err.textContent = T('Ingresa un código postal de 5 dígitos.', 'Enter a 5-digit ZIP code.');
        qf.zip.focus(); return;
      }
      var tipo = qf.querySelector('input[name=tipo]:checked').value;
      location.href = 'contacto.html?tipo=' + encodeURIComponent(tipo) + '&zip=' + encodeURIComponent(zip) + (lang === 'en' ? '&lang=en' : '');
    });
  }

  /* ---------- Asistente de cotización (contacto) ---------- */
  var wz = doc.getElementById('wizard');
  if (wz) {
    var steps = wz.querySelectorAll('.wiz-step'), dots = wz.querySelectorAll('.wiz-progress i'), cur = 0;
    var params = new URLSearchParams(location.search);
    var labels = { auto: ['Seguro de Auto', 'Auto insurance'], home: ['Seguro de Hogar', 'Home insurance'], business: ['Seguro Comercial', 'Commercial insurance'], health: ['Seguro de Salud', 'Health insurance'] };

    function show(n) {
      cur = n;
      steps.forEach(function (s, i) { s.classList.toggle('active', i === n); });
      dots.forEach(function (d, i) { d.classList.toggle('on', i <= n); });
      if (n === 2) summarize();
      var top = wz.getBoundingClientRect().top + scrollY - 120;
      if (n > 0 || params.get('tipo')) scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
    }
    function val(name) { return (wz.elements[name] && wz.elements[name].value || '').trim(); }
    function err(name, msg) { var el = wz.querySelector('[data-err="' + name + '"]'); if (el) el.textContent = msg || ''; }
    function typeLabel() { var l = labels[val('tipo')] || ['', '']; return T(l[0], l[1]); }
    function summarize() {
      doc.getElementById('sum').innerHTML =
        '<div><b>' + T('Seguro', 'Insurance') + ':</b> ' + typeLabel() + '</div>' +
        '<div><b>' + T('Nombre', 'Name') + ':</b> ' + esc(val('name')) + '</div>' +
        '<div><b>' + T('Teléfono', 'Phone') + ':</b> ' + esc(val('phone')) + '</div>' +
        '<div><b>Email:</b> ' + esc(val('email')) + '</div>' +
        '<div><b>' + T('Código postal', 'ZIP') + ':</b> ' + esc(val('zip')) + '</div>';
    }
    function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

    var pre = params.get('tipo');
    if (pre && labels[pre]) { var r = wz.querySelector('input[name=tipo][value=' + pre + ']'); if (r) r.checked = true; }
    if (params.get('zip')) wz.elements.zip.value = params.get('zip').replace(/\D/g, '').slice(0, 5);

    wz.querySelectorAll('[data-next]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (cur === 0) { show(1); return; }
        if (cur === 1) {
          var ok = true;
          err('name'); err('phone'); err('email'); err('zip');
          if (val('name').length < 2) { err('name', T('Escribe tu nombre.', 'Enter your name.')); ok = false; }
          if (val('phone').replace(/\D/g, '').length < 10) { err('phone', T('Teléfono de 10 dígitos.', '10-digit phone number.')); ok = false; }
          if (val('email') && !/^\S+@\S+\.\S+$/.test(val('email'))) { err('email', T('Correo no válido.', 'Invalid email.')); ok = false; }
          if (!/^\d{5}$/.test(val('zip'))) { err('zip', T('5 dígitos.', '5 digits.')); ok = false; }
          if (ok) show(2);
        }
      });
    });
    wz.querySelectorAll('[data-prev]').forEach(function (b) { b.addEventListener('click', function () { show(Math.max(cur - 1, 0)); }); });

    wz.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!wz.elements.consent.checked) { err('consent', T('Necesitamos tu autorización para contactarte.', 'We need your permission to contact you.')); return; }
      err('consent');
      // Sin backend todavía: se abre el correo del usuario con la solicitud prellenada.
      var body = [T('Seguro', 'Insurance') + ': ' + typeLabel(), T('Nombre', 'Name') + ': ' + val('name'), T('Teléfono', 'Phone') + ': ' + val('phone'),
        'Email: ' + val('email'), T('Código postal', 'ZIP') + ': ' + val('zip'), '', val('message')].join('\n');
      location.href = 'mailto:hello@trustinsuranceservices.com?subject=' + encodeURIComponent(T('Solicitud de cotización', 'Quote request') + ' — ' + typeLabel()) + '&body=' + encodeURIComponent(body);
      steps.forEach(function (s) { s.classList.remove('active'); });
      doc.getElementById('wiz-done').classList.add('active');
      dots.forEach(function (d) { d.classList.add('on'); });
    });
    show(pre && labels[pre] ? 1 : 0);
  }
})();
