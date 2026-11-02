"""Importa los artículos y páginas legales de la web actual a content/*.json.
Uso: python3 tools/import_content.py   (requiere red; solo lectura de páginas públicas)."""
import json, os, re, urllib.request
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://trustinsuranceservices.com"

# Fecha y lectura tomadas del listado https://trustinsuranceservices.com/blogs
POSTS = {
    "revisar-seguro-auto-florida": ("2026-10-19", 9),
    "como-bajar-precio-seguro-auto-florida": ("2026-10-05", 9),
    "seguro-auto-temporada-lluvias-florida": ("2026-09-23", 8),
    "glosario-terminos-seguros-auto-florida": ("2026-09-01", 10),
    "seguro-auto-georgia-hispanos-espanol": ("2026-08-19", 3),
    "seguro-auto-hijo-joven-conductor-florida": ("2026-08-05", 3),
}
KEEP = {"h2", "h3", "h4", "p", "ul", "ol", "li", "strong", "em", "b", "i", "br", "blockquote", "table", "thead", "tbody", "tr", "th", "td"}
VOID = {"br", "hr", "img", "input", "meta", "link", "source", "area", "col"}
SKIP = {"script", "style", "svg", "img", "button", "iframe", "nav", "form", "noscript", "figure"}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

class Extract(HTMLParser):
    """Recoge el contenido dentro del primer elemento cuyo class contiene `marker`."""
    def __init__(self, marker):
        super().__init__(convert_charrefs=True)
        self.marker, self.depth, self.out, self.skip, self.title, self._in_h1 = marker, 0, [], 0, None, False
        self.active = False
    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class") or ""
        if not self.active and self.marker in cls.split():
            self.active, self.depth = True, 0
        if not self.active:
            return
        if tag in VOID:
            if tag == "br" and not self.skip: self.out.append("<br>")
            return
        self.depth += 1
        if tag in SKIP: self.skip += 1; return
        if self.skip: return
        if tag == "h1":
            self._in_h1 = True
            if self.title is None: self.title = ""
            return
        if tag in KEEP:
            self.out.append(f"<{tag}>")
    def handle_endtag(self, tag):
        if not self.active or tag in VOID: return
        self.depth -= 1
        if tag in SKIP: self.skip = max(0, self.skip - 1)
        elif not self.skip:
            if tag == "h1": self._in_h1 = False
            elif tag in KEEP and tag != "br": self.out.append(f"</{tag}>")
        if self.depth <= 0: self.active = False
    def handle_data(self, data):
        if not self.active or self.skip: return
        if self._in_h1:
            if self.title == "" : self.title = data.strip()
            return
        self.out.append(data.replace("<", "&lt;").replace(">", "&gt;"))

def clean(html):
    html = re.sub(r"<(p|li|h[2-4]|strong|em|b|i|td|th)>\s*</\1>", "", html)
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r"</(p|ul|ol|h[2-4]|li|blockquote|table|tr)>", lambda m: m.group(0) + "\n", html)
    return html.strip()

def main():
    for slug, (date, mins) in POSTS.items():
        page = fetch(f"{BASE}/post/{slug}")
        ex = Extract("blog-html"); ex.feed(page)
        t = re.search(r'<h1[^>]*class="[^"]*blog-content-title[^"]*"[^>]*>(.*?)</h1>', page, re.S)
        title_src = re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else (ex.title or slug)
        body = clean("".join(ex.out))
        # elimina cierres de contacto y firma duplicados al final del contenido de origen
        body = re.sub(r"<p>\s*(📞|Tu paz, asegurada\.|Trust Insurance Services)[^<]*</p>\n?", "", body)
        title = re.sub(r"\s*\(\d+\s*car\.?\)\s*", "", title_src).strip()
        m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', page) or re.search(r'<meta[^>]+content="([^"]*)"[^>]+name="description"', page)
        desc = re.sub(r"\s*\(\d+\s*car\.?\)\s*", "", m.group(1)).strip() if m else ""
        with open(os.path.join(ROOT, "content", "blog", slug + ".json"), "w", encoding="utf-8") as f:
            json.dump({"slug": slug, "title": title, "date": date, "read": mins, "desc": desc, "html": body}, f, ensure_ascii=False, indent=1)
        print(slug, "->", len(body), "chars |", title)

    for slug, marker in (("privacy-policy", "blog-html-container"), ("terms-conditions", "blog-html-container")):
        pass

if __name__ == "__main__":
    main()
