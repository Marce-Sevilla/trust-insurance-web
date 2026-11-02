(function () {
  var dict = window.TRUST_I18N;
  var lang = 'es';

  try {
    var saved = localStorage.getItem('trust-lang');
    if (saved && dict[saved]) lang = saved;
    else if ((navigator.language || '').toLowerCase().indexOf('en') === 0) lang = 'en';
  } catch (e) {}

  function t(key) { return dict[lang][key] || key; }

  function applyLang() {
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      el.textContent = t(el.getAttribute('data-i18n'));
    });
    document.getElementById('lang-toggle').textContent = lang === 'es' ? 'EN' : 'ES';
    try { localStorage.setItem('trust-lang', lang); } catch (e) {}
  }

  document.getElementById('lang-toggle').addEventListener('click', function () {
    lang = lang === 'es' ? 'en' : 'es';
    applyLang();
  });

  var nav = document.getElementById('nav');
  var menuToggle = document.getElementById('menu-toggle');
  menuToggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    menuToggle.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', function () {
    nav.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
  });

  document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var f = e.target;
    var status = document.getElementById('form-status');
    var ok = f.name.value.trim() && /^\S+@\S+\.\S+$/.test(f.email.value.trim());
    status.textContent = ok ? t('contact.sent') : t('contact.invalid');
    if (ok) f.reset();
  });

  document.getElementById('year').textContent = new Date().getFullYear();
  applyLang();
})();
