@echo off
title Mon Serveur Python

:: 1. Vérifie si l'environnement virtuel existe et l'active
if exist venv\Scripts\activate (
    echo Activation de l'environnement virtuel...
    call venv\Scripts\activate
) else (
    echo [ATTENTION] Environnement virtuel 'venv' non trouve. Lancement direct...
)

:: 2. Lance le serveur
echo Lancement de app.py...
python app.py

:: 3. Garde la fenêtre ouverte en cas d'erreur
pause
