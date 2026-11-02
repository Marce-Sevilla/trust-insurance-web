"""Servidor local con URLs limpias (igual que producción): /inicio, /nosotros, /seguro-auto...
Uso: python3 tools/serve.py [puerto]   (por defecto 5173)"""
import http.server, os, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def _redirect(self, to, code):
        self.send_response(code)
        self.send_header("Location", to)
        self.end_headers()

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        path, qs = u.path, ("?" + u.query if u.query else "")
        if path in ("/", "/index", "/index.html", "/inicio.html"):
            return self._redirect("/inicio" + qs, 302 if path == "/" else 301)
        if path.endswith(".html"):
            return self._redirect(path[:-5] + qs, 301)
        if "." not in os.path.basename(path) and os.path.isfile(os.path.join(ROOT, path.lstrip("/") + ".html")):
            self.path = path + ".html" + qs
        return super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
