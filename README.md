# Trust Insurance Services — sitio web

Sitio estático multipágina (HTML, CSS y JavaScript puro, sin build). Bilingüe: español / inglés.

```
inicio.html · nosotros.html · servicios.html · contacto.html · privacidad.html · terminos.html
seguro-auto.html · seguro-hogar.html · seguro-comercial.html · seguro-salud.html
css/styles.css     Sistema de diseño
js/layout.js       Header, footer e iconos compartidos
js/main.js         Idioma, menú, animaciones, cotizador y asistente
assets/            Logos
tools/pages.py     Genera las páginas internas
docs/brand.md      Identidad y guía de diseño
```

## Desarrollo

```bash
python3 tools/serve.py 5173
```

Abrir http://localhost:5173 (URLs limpias: `/inicio`, `/nosotros`, `/seguro-auto`…; el archivo `_redirects` hace lo mismo en producción). Para regenerar las páginas internas: `python3 tools/pages.py`.

Detalles de diseño y pendientes en [docs/brand.md](docs/brand.md).
