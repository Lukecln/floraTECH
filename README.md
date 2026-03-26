# Présentation 3D — Boîtier Électronique

## Structure

```
projet/
├── server.py        ← Serveur Python (aucune dépendance externe)
├── index.html       ← Site web
├── content.json     ← Textes et métadonnées
└── stl/
    ├── base.stl
    ├── tirroir.stl
    ├── plaque ecran.stl
    ├── cache.stl
    ├── boite a terre2.0.stl
    └── final.stl
```

## Lancement

```bash
# 1. Placer les fichiers STL dans le dossier stl/
mkdir stl
cp base.stl tirroir.stl cache.stl "plaque ecran.stl" "boite a terre2.0.stl" final.stl stl/

# 2. Lancer le serveur
python3 server.py

# 3. Ouvrir dans le navigateur
# http://localhost:8080
```

## Personnalisation

Modifier `content.json` pour changer les textes, titres et noms de fichiers.

## Contrôles 3D

| Glisser          | Rotation  |
|------------------|-----------|
| Molette          | Zoom      |
| ⇧ + Glisser      | Déplacer  |
