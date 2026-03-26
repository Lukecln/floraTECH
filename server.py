#!/usr/bin/env python3
"""
Serveur Python pour la présentation 3D du projet boîtier électronique.
"""

import http.server
import mimetypes
import os
from pathlib import Path

mimetypes.add_type('model/stl', '.stl')
mimetypes.add_type('application/json', '.json')

PORT = 8080
STL_FOLDER = "stl"


class ProjectHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

    def do_GET(self):
        if self.path.startswith('/stl/'):
            self.serve_stl()
        else:
            super().do_GET()

    def serve_stl(self):
        filename = self.path[5:]
        # Decode URL encoding (%20 etc.)
        from urllib.parse import unquote
        filename = unquote(filename)
        filepath = Path(STL_FOLDER) / filename

        if not filepath.exists():
            self.send_error(404, f"STL not found: {filename}")
            return

        self.send_response(200)
        self.send_header('Content-Type', 'model/stl')
        self.send_header('Content-Length', str(filepath.stat().st_size))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'public, max-age=3600')
        self.end_headers()
        with open(filepath, 'rb') as f:
            self.wfile.write(f.read())

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"  {self.address_string()}  {format % args}")


def check_files():
    required = [
        "base.stl",
        "tirroir.stl",
        "cache.stl",
        "plaque ecran.stl",
        "boite a terre2.0.stl",
        "final.stl",
    ]
    stl_dir = Path(STL_FOLDER)
    stl_dir.mkdir(exist_ok=True)

    missing = [f for f in required if not (stl_dir / f).exists()]
    if missing:
        print("Fichiers STL manquants dans stl/ :")
        for f in missing:
            print(f"  — {f}")
    else:
        print("Tous les fichiers STL sont présents.")

    for f in ("index.html", "content.json"):
        status = "OK" if Path(f).exists() else "MANQUANT"
        print(f"  {f} : {status}")


def main():
    print()
    print("  Présentation 3D — Boîtier Électronique")
    print("  " + "─" * 40)
    check_files()
    print()
    print(f"  Serveur démarré → http://localhost:{PORT}")
    print("  Ctrl+C pour arrêter.")
    print()

    with http.server.HTTPServer(("", PORT), ProjectHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Serveur arrêté.")


if __name__ == "__main__":
    main()
