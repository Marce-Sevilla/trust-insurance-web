# Identidad — Trust Insurance Services

Tomada de la landing actual (trustinsuranceservices.com). Los tokens viven en `:root` de `css/styles.css`.

## Color

| Token | Valor | Uso |
|---|---|---|
| `--navy` | `#001d3d` | Texto, secciones oscuras, header |
| `--navy-soft` | `#0a3260` | Fondo de apoyo del hero |
| `--ice` | `#fafeff` | Fondo general |
| `--orange` | `#f65a13` | Botones, acentos, numeración |
| `--orange-dark` | `#d94a0a` | Hover de botones |
| `--muted` | `#4d6078` | Texto secundario |
| `--line` | `#d9e4ee` | Bordes |

Nota de accesibilidad: texto blanco sobre naranja da ~3,4:1; usar solo en botones de texto grande y en negrita.

## Tipografía

- **Titulares:** Playfair Display (500), clamp 2–4,6 rem.
- **Cuerpo, botones, etiquetas:** Montserrat (400–800). Etiquetas en mayúsculas con espaciado.
- Ambas desde Google Fonts.

## Componentes

- Header: píldora flotante navy translúcida con blur; botón naranja "Cotizar ahora".
- Botones: píldora (radio 999 px), mayúsculas.
- Tarjetas: radio 16 px, borde fino, elevan 4 px en hover.
- Secciones alternan `--ice` y `--navy`.

## Logo

`assets/logo.svg` y `assets/favicon.svg` son una reconstrucción propia (escudo naranja con check + wordmark) a partir de lo observado en la web actual. **Reemplazar por los archivos originales de la marca.**

## Pendiente

- Foto o video real del hero (`assets/hero.jpg`)
- Logo original, fotos de servicios y testimonios
- Formulario conectado a un servicio de envío
- Revisar textos EN y FAQ
