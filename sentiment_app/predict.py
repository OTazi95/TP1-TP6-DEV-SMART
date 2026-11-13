#!/usr/bin/env python
"""Prédiction unitaire : la fonction que l'API de la semaine 3 appellera.

Usage :
  python src/predict.py "Livraison rapide, très satisfait"
  >>> from predict import predict ; predict("texte")
"""
import os
import sys
from functools import lru_cache
from pathlib import Path

import joblib


def chemin_modele() -> Path:
    """Renvoie le chemin du modèle, modifiable via la variable d'environnement SENTIMENT_MODELE."""
    env_path = os.getenv("SENTIMENT_MODELE")
    if env_path:
        return Path(env_path)
    # Chemin par défaut par rapport à la racine du paquet ou du projet
    return Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"

MODELE = chemin_modele()

@lru_cache(maxsize=1)
def charger_modele():
    """Chargé une seule fois par processus, pas à chaque appel."""
    if not MODELE.exists():
        raise FileNotFoundError("models/sentiment.joblib absent : lancez python src/train.py")
    return joblib.load(MODELE)


def predict(texte: str) -> dict:
    """Renvoie {'label': 'positive'|'negative', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
