# Présentation 3D — Boîtier Électronique

## Structure des fichiers

```
projet/
├── server.py          ← Serveur Python
├── index.html         ← Site web
├── content.json       ← Textes descriptifs
└── stl/               ← Dossier des modèles 3D
    ├── _base.stl
    ├── _tirroir.stl
    ├── _cache.stl
    ├── _plaque ecran.stl
    ├── _boite a terre2.0.stl
    └── final.stl
```

## Installation & Lancement

### 1. Préparer les fichiers

Copier tous les fichiers STL dans un dossier `stl/` :

```bash
mkdir stl
cp _base.stl _tirroir.stl _cache.stl "_plaque ecran.stl" "_boite a terre2.0.stl" final.stl stl/
```

### 2. Lancer le serveur

```bash
python3 server.py
```

### 3. Ouvrir le site

Ouvrir un navigateur et aller sur :
```
http://localhost:8080
```

## Personnaliser les textes

Modifier le fichier `content.json` pour changer :
- Le titre et la description du projet (section `"project"`)
- Le texte de chaque pièce (section `"steps"`)
- Le texte de l'assemblage final (section `"final"`)

## Fonctionnement

- **Page d'accueil** : présentation générale du projet
- **Bouton "Voir la présentation"** : démarre la visite guidée
- **Viewer 3D** : chaque pièce se charge en 3D, interactive (rotation, zoom, déplacement)
- **Bouton "Suivant"** : passe à la pièce suivante dans l'ordre
- **Bouton "Voir l'assemblage final"** : affiche le fichier `final.stl` en overlay

## Contrôles 3D

| Action | Contrôle |
|--------|----------|
| Rotation | Clic gauche + glisser |
| Zoom | Molette de la souris |
| Déplacement | Shift + clic + glisser (ou clic droit) |

## Dépendances

- Python 3.x (bibliothèque standard uniquement, aucune installation requise)
- Navigateur moderne (Chrome, Firefox, Edge)
- Three.js chargé automatiquement depuis CDN
