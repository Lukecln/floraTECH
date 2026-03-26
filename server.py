#!/usr/bin/env python3
"""
Serveur Python pour la présentation 3D du projet boîtier électronique.
Sert les fichiers STL et les fichiers statiques du site.
"""

import http.server
import json
import os
import mimetypes
from pathlib import Path

# Ajouter le type MIME pour les fichiers STL
mimetypes.add_type('model/stl', '.stl')
mimetypes.add_type('application/json', '.json')

# Configuration
PORT = 8080
STL_FOLDER = "stl"   # Dossier contenant les fichiers STL
STATIC_FOLDER = "."  # Dossier racine pour les fichiers statiques


class ProjectHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_FOLDER, **kwargs)

    def do_GET(self):
        # Route pour les fichiers STL
        if self.path.startswith('/stl/'):
            self.serve_stl()
        else:
            super().do_GET()

    def serve_stl(self):
        """Sert un fichier STL avec les bons en-têtes CORS."""
        filename = self.path[5:]  # Enlève '/stl/'
        filepath = Path(STL_FOLDER) / filename

        if not filepath.exists():
            self.send_error(404, f"Fichier STL non trouvé: {filename}")
            return

        file_size = filepath.stat().st_size

        self.send_response(200)
        self.send_header('Content-Type', 'model/stl')
        self.send_header('Content-Length', str(file_size))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'public, max-age=3600')
        self.end_headers()

        with open(filepath, 'rb') as f:
            self.wfile.write(f.read())

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # Log coloré
        print(f"\033[36m[Serveur]\033[0m {self.address_string()} - {format % args}")


def check_files():
    """Vérifie la présence des fichiers nécessaires."""
    required_stl = [
        "_base.stl",
        "_tirroir.stl",
        "_cache.stl",
        "_plaque ecran.stl",
        "_boite a terre2.0.stl",
        "final.stl"
    ]

    stl_dir = Path(STL_FOLDER)
    if not stl_dir.exists():
        print(f"\033[33m[Avertissement]\033[0m Dossier '{STL_FOLDER}/' non trouvé. Création...")
        stl_dir.mkdir(exist_ok=True)

    missing = []
    for f in required_stl:
        if not (stl_dir / f).exists():
            missing.append(f)

    if missing:
        print(f"\033[33m[Avertissement]\033[0m Fichiers STL manquants dans '{STL_FOLDER}/':")
        for f in missing:
            print(f"  - {f}")
    else:
        print(f"\033[32m[OK]\033[0m Tous les fichiers STL sont présents.")

    # Vérifier les fichiers HTML/JSON
    for f in ["index.html", "content.json"]:
        if Path(f).exists():
            print(f"\033[32m[OK]\033[0m {f} trouvé.")
        else:
            print(f"\033[31m[ERREUR]\033[0m {f} manquant !")


def main():
    print("\033[1m\033[34m" + "=" * 50)
    print("  Serveur Présentation 3D - Boîtier Électronique")
    print("=" * 50 + "\033[0m")
    print()

    check_files()
    print()
    print(f"\033[32m[Démarrage]\033[0m Serveur lancé sur \033[1mhttp://localhost:{PORT}\033[0m")
    print("Appuyez sur Ctrl+C pour arrêter.\n")

    with http.server.HTTPServer(("", PORT), ProjectHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[31m[Arrêt]\033[0m Serveur stoppé.")


if __name__ == "__main__":
    main()
