# Identidad y sistema de diseño — Trust Insurance Services

Los tokens viven en `:root` de `css/styles.css`.

## Logos (`assets/`)

| Archivo | Uso |
|---|---|
| `logo_horizontal.png`, `logo_vertical.png`, `isotipo.png` | Originales de marca (no editar) |
| `logo-horizontal-720.png` | Header y footer (sobre azul marino) |
| `isotipo-360.png` | Marcas de agua y decoración |
| `favicon.png`, `apple-touch-icon.png` | Iconos del navegador |

El logo tiene "INSURANCE" en gris claro: **usarlo siempre sobre fondos oscuros** (azul marino).

## Color

| Token | Valor | Uso |
|---|---|---|
| `--navy` | `#001d3d` | Texto, header, secciones oscuras |
| `--navy-deep` | `#00132b` | Footer, menú móvil |
| `--ice` | `#fafeff` | Fondo general |
| `--orange` | `#f65a13` | Acción principal y acentos |
| `--grad` | `#e8402a → #f65a13 → #f9a22b` | Cifras y banda CTA (toma el degradado del logo) |
| `--cream` | `#fff1e6` | Fondo cálido (tinte del naranja) |
| `--sky` | `#e6eff8` | Fondo frío (tinte del azul) |

Texto blanco sobre naranja ≈ 3,4:1: solo en botones de texto grande y en negrita.

## Tipografía

- **Titulares:** Playfair Display 500, con una palabra clave en *itálica naranja* (`<em>`).
- **Cuerpo, botones y etiquetas:** Montserrat; etiquetas y botones en mayúsculas con espaciado.

## Patrones (tomados de las referencias)

- Menú flotante en píldora + aviso superior en marquesina (Broworks)
- Cuadrícula de líneas finas, numeración `/ 01` y cifras animadas (BoostLab, Citadel)
- Serif con itálica de acento, tarjeta de cotización, pasos (Zenarate)
- Secciones que alternan color de fondo y bento de servicios (Broworks, Citadel)
- Carrusel de testimonios, FAQ en acordeón, footer con marca gigante

## Fotografía (`assets/img/`)

`services/` (4 fotos 1200×800, webp) · `people/` (retratos de testimonios, 220 px) · `about/` (formulario en tableta). Todas optimizadas (≈1,8 MB en total); originales de varios MB descartados.

## Estructura del sitio

`index` · `nosotros` · `servicios` · `seguro-auto` · `seguro-hogar` · `seguro-comercial` · `seguro-salud` · `contacto` (asistente de 3 pasos)

## Cómo editar

- **Bilingüe:** el texto en español va en el HTML y el inglés en el atributo `data-en` del mismo elemento.
- **Header, footer e iconos:** `js/layout.js` (un solo lugar para todas las páginas).
- **Páginas internas:** se generan con `python3 tools/pages.py`; `index.html` se edita a mano.
- **Idioma:** español por defecto; el inglés solo se activa con el botón EN (o `?lang=en`).

## Pendiente

- Confirmar licencia de las fotos: se descargaron de la web actual y parecen de banco de imágenes (servicios y formulario en tableta)
- Foto o video propio del hero (la web actual usa un video de dos personas; no se migró por peso, 6–20 MB)
- Confirmar que se puede publicar el retrato de cada testimonio
- Páginas legales: el footer enlaza a las de la web actual (privacy-policy y terms-conditions)
- Conectar el formulario a un servicio de envío (hoy abre el correo del usuario con la solicitud prellenada)
- Revisar los textos en inglés y las respuestas de FAQ
- Confirmar con el cliente las cifras (`< 5 min`, `100+`, `100%`) y los testimonios
