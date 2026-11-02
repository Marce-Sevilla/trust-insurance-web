# Trust Insurance Services — sitio web

Sitio estático multipágina (HTML, CSS y JavaScript puro, sin build). Bilingüe: español / inglés.

```
index.html · nosotros.html · servicios.html · blog.html · contacto.html
seguro-auto.html · seguro-hogar.html · seguro-comercial.html · seguro-salud.html
css/styles.css     Sistema de diseño
js/layout.js       Header, footer e iconos compartidos
js/main.js         Idioma, menú, animaciones, cotizador y asistente
assets/            Logos
tools/pages.py     Genera las páginas internas y artículos
tools/import_content.py  Importa artículos de la web actual
content/blog/      Artículos (JSON)
docs/brand.md      Identidad y guía de diseño
```

## Desarrollo

```bash
python3 -m http.server 5173
```

Abrir http://localhost:5173. Para regenerar las páginas internas: `python3 tools/pages.py`.

Detalles de diseño y pendientes en [docs/brand.md](docs/brand.md).
