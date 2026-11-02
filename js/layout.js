// Header, aviso superior, footer y barra móvil compartidos por todas las páginas.
(function () {
  var stroke = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"';
  window.TRUST_ICONS = {
    auto: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M5 17H3v-5l2-5h14l2 5v5h-2"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M5 12h14M9.5 17h5"/></svg>',
    home: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
    business: '<svg viewBox="0 0 24 24" ' + stroke + '><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>',
    health: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M12 20s-8-4.8-8-10.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 8 2.5C20 15.200 12 20 12 20Z"/><path d="M12 10v4M10 12h4"/></svg>',
    shield: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M12 3 4 6v6c0 4.500 3.400 7.800 8 9 4.600-1.200 8-4.500 8-9V6l-8-3Z"/><path d="m8.500 12 2.500 2.500 4.500-5"/></svg>',
    bolt: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/></svg>',
    people: '<svg viewBox="0 0 24 24" ' + stroke + '><circle cx="9" cy="8" r="3.500"/><path d="M2.500 20c0-3.500 2.900-6 6.500-6s6.500 2.500 6.500 6"/><path d="M16 4.500a3.500 3.500 0 0 1 0 7M18 14.500c2 .8 3.500 2.700 3.500 5.500"/></svg>',
    water: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M12 3s6 6.500 6 11a6 6 0 0 1-12 0c0-4.500 6-11 6-11Z"/></svg>',
    doc: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M6 3h9l4 4v14H6V3Z"/><path d="M14 3v5h5M9 13h7M9 17h7"/></svg>',
    scale: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M12 3v18M6 21h12M5 7h14"/><path d="m5 7-3 7a3.500 3.500 0 0 0 6 0L5 7ZM19 7l-3 7a3.500 3.500 0 0 0 6 0l-3-7Z"/></svg>',
    wrench: '<svg viewBox="0 0 24 24" ' + stroke + '><path d="M14.500 6.500a4 4 0 0 0 5 5L21 13l-8 8-4-4 8-8-2.500-2.500Z" transform="translate(-3 -2)"/></svg>'
  };
  var I = window.TRUST_ICONS;

  var page = (location.pathname.split('/').pop() || 'index.html');
  function cur(f) { return page === f ? ' aria-current="page"' : ''; }
  if (page === 'contacto.html') document.body.classList.add('page-contact');
  var inServices = /^seguro-|^servicios/.test(page);

  var tick = [
    ['Cotización gratis en menos de 5 minutos', 'Free quote in under 5 minutes'],
    ['Comparamos más de 100 opciones', 'We compare 100+ options'],
    ['Asesoría personalizada en Florida', 'Personalized advice in Florida'],
    ['Llámanos al (786) 807-8559', 'Call us at (786) 807-8559']
  ];
  var tickHtml = tick.map(function (t) { return '<span data-en="' + t[1] + '">' + t[0] + '</span>'; }).join('');

  var header =
    '<div class="topbar" aria-label="Avisos"><div class="topbar-track" aria-hidden="false">' + tickHtml + tickHtml + tickHtml + tickHtml + '</div></div>' +
    '<header class="site-header"><div class="container"><div class="header-inner">' +
      '<a class="brand" href="index.html" aria-label="Trust Insurance Services — Inicio"><img src="assets/logo-horizontal-720.png" width="720" height="284" alt="Trust Insurance"></a>' +
      '<nav class="nav" id="nav" aria-label="Principal">' +
        '<a href="index.html"' + cur('index.html') + ' data-en="Home">Inicio</a>' +
        '<a href="nosotros.html"' + cur('nosotros.html') + ' data-en="About">Nosotros</a>' +
        '<div class="nav-drop' + (inServices ? ' current' : '') + '"><button type="button" aria-haspopup="true" data-en="Services">Servicios</button>' +
          '<div class="drop-menu">' +
            '<a href="seguro-auto.html"><span class="ico">' + I.auto + '</span><span><strong data-en="Auto insurance">Seguro de Auto</strong><small data-en="Fair price on the road">Precio justo al conducir</small></span></a>' +
            '<a href="seguro-hogar.html"><span class="ico">' + I.home + '</span><span><strong data-en="Home insurance">Seguro de Hogar</strong><small data-en="Protect your biggest asset">Protege tu mayor patrimonio</small></span></a>' +
            '<a href="seguro-comercial.html"><span class="ico">' + I.business + '</span><span><strong data-en="Commercial insurance">Seguro Comercial</strong><small data-en="Cover what you built">Cubre lo que construiste</small></span></a>' +
            '<a href="seguro-salud.html"><span class="ico">' + I.health + '</span><span><strong data-en="Health insurance">Seguro de Salud</strong><small data-en="You and your family">Tú y tu familia</small></span></a>' +
          '</div></div>' +
        '<a href="contacto.html"' + cur('contacto.html') + ' data-en="Contact">Contacto</a>' +
        '<a class="btn nav-cta" href="contacto.html" data-en="Get a quote">Cotizar ahora</a>' +
      '</nav>' +
      '<div class="header-actions">' +
        '<button class="lang-toggle" id="lang-toggle" type="button" aria-label="Cambiar idioma / Change language">English</button>' +
        '<a class="btn btn-sm" href="contacto.html" data-en="Get a quote">Cotizar ahora</a>' +
        '<button class="menu-toggle" id="menu-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menú / Menu"><span></span></button>' +
      '</div>' +
    '</div></div></header>';

  var fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.500 21v-7.500H16l.5-3h-3V8.700c0-.9.300-1.500 1.600-1.500h1.500V4.500C16.300 4.400 15.400 4.300 14.500 4.300c-2.300 0-3.900 1.400-3.900 4v2.200H8v3h2.600V21h2.900Z"/></svg>';
  var ig = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.500 3h9A4.500 4.500 0 0 1 21 7.500v9a4.500 4.500 0 0 1-4.500 4.500h-9A4.500 4.500 0 0 1 3 16.500v-9A4.500 4.500 0 0 1 7.500 3Zm0 1.800A2.700 2.700 0 0 0 4.800 7.500v9a2.700 2.700 0 0 0 2.700 2.700h9a2.700 2.700 0 0 0 2.700-2.700v-9a2.700 2.700 0 0 0-2.700-2.700h-9ZM12 7.500a4.500 4.500 0 1 1 0 9 4.500 4.500 0 0 1 0-9Zm0 1.800a2.700 2.700 0 1 0 0 5.400 2.700 2.700 0 0 0 0-5.400Zm4.900-2.600a1.050 1.050 0 1 1 0 2.100 1.050 1.050 0 0 1 0-2.100Z"/></svg>';

  var yt = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.600 7.200a2.500 2.500 0 0 0-1.800-1.800C18.200 5 12 5 12 5s-6.200 0-7.800.4a2.500 2.500 0 0 0-1.800 1.800C2 8.800 2 12 2 12s0 3.200.4 4.800a2.500 2.500 0 0 0 1.800 1.800C5.800 19 12 19 12 19s6.200 0 7.800-.4a2.500 2.500 0 0 0 1.800-1.800c.4-1.600.4-4.800.4-4.800s0-3.200-.4-4.800ZM10 15V9l5.200 3-5.200 3Z"/></svg>'; var tk = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.500 3c.3 2.300 1.600 3.700 3.800 3.900v3a7 7 0 0 1-3.700-1.100v6.100a6 6 0 1 1-6-6c.3 0 .6 0 .9.100v3.100a3 3 0 1 0 2.100 2.800V3h2.900Z"/></svg>';

  var footer =
    '<footer class="site-footer"><div class="container">' +
      '<div class="footer-grid">' +
        '<div class="footer-brand"><img src="assets/logo-horizontal-720.png" width="720" height="284" alt="Trust Insurance" loading="lazy">' +
          '<p data-en="Insurance agency in Florida. We compare 100+ options so you get the right balance of price and protection.">Agencia de seguros en Florida. Comparamos más de 100 opciones para darte el equilibrio justo entre precio y respaldo.</p>' +
          '<div class="social"><a href="https://www.facebook.com/trustinsuranceserv" rel="noopener" target="_blank" aria-label="Facebook">' + fb + '</a><a href="https://www.instagram.com/trustinsuranceserv/" rel="noopener" target="_blank" aria-label="Instagram">' + ig + '</a><a href="https://www.youtube.com/@TrustInsuranceservices" rel="noopener" target="_blank" aria-label="YouTube">' + yt + '</a><a href="https://www.tiktok.com/@trustinsuranceservices" rel="noopener" target="_blank" aria-label="TikTok">' + tk + '</a></div></div>' +
        '<div><h4 data-en="Services">Servicios</h4><ul>' +
          '<li><a href="seguro-auto.html" data-en="Auto insurance">Seguro de Auto</a></li><li><a href="seguro-hogar.html" data-en="Home insurance">Seguro de Hogar</a></li>' +
          '<li><a href="seguro-comercial.html" data-en="Commercial insurance">Seguro Comercial</a></li><li><a href="seguro-salud.html" data-en="Health insurance">Seguro de Salud</a></li></ul></div>' +
        '<div><h4 data-en="Company">Empresa</h4><ul>' +
          '<li><a href="nosotros.html" data-en="About us">Nosotros</a></li><li><a href="servicios.html" data-en="All services">Todos los servicios</a></li>' +
          '<li><a href="contacto.html" data-en="Contact">Contacto</a></li></ul></div>' +
        '<div><h4 data-en="Contact">Contacto</h4><ul>' +
          '<li><a href="tel:+17868078559">(786) 807-8559</a></li>' +
          '<li><a href="mailto:hello@trustinsuranceservices.com">hello@trustinsuranceservices.com</a></li>' +
          '<li><a href="https://maps.google.com/?q=10505+NW+112th+Ave+Ste+11+Miami+FL+33178" target="_blank" rel="noopener">10505 NW 112th Ave Ste 11,<br>Miami, FL 33178</a></li></ul></div>' +
      '</div>' +
      '<div class="footer-bottom"><span>© <span id="year"></span> Trust Insurance Services. <span data-en="All rights reserved.">Todos los derechos reservados.</span></span>' +
      '<span><a href="https://trustinsuranceservices.com/privacy-policy" rel="noopener" target="_blank" data-en="Privacy policy">Política de privacidad</a> · <a href="https://trustinsuranceservices.com/terms-conditions" rel="noopener" target="_blank" data-en="Terms &amp; conditions">Términos y condiciones</a></span></div>' +
    '</div><div class="footer-big" aria-hidden="true">TRUST</div></footer>' +
    '<nav class="mobile-bar" aria-label="Acciones rápidas"><a class="btn btn-sm btn-noarrow" href="tel:+17868078559" data-en="Call">Llamar</a><a class="btn btn-sm" href="contacto.html" data-en="Get a quote">Cotizar ahora</a></nav>' +
    '<div class="progress" id="progress" aria-hidden="true"></div>';

  var h = document.getElementById('site-header'); if (h) h.outerHTML = header;
  var f = document.getElementById('site-footer'); if (f) f.outerHTML = footer;
})();
