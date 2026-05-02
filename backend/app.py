"""Application Flask : santé de l’API, métriques de démonstration, prédiction factice."""

from __future__ import annotations

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# Données factices alignées sur la structure attendue par le frontend (voir frontend/js/app.js).
# À remplacer par la lecture des résultats réels (fichier JSON ou base) après entraînement.
METRICS_STUB = [
    {
        "id": "logistic_regression",
        "label": "Régression logistique",
        "accuracy": 0.82,
        "precision": 0.79,
        "recall": 0.76,
        "f1": 0.775,
    },
    {
        "id": "knn",
        "label": "KNN",
        "accuracy": 0.8,
        "precision": 0.77,
        "recall": 0.74,
        "f1": 0.755,
    },
    {
        "id": "decision_tree",
        "label": "Arbre de décision",
        "accuracy": 0.78,
        "precision": 0.75,
        "recall": 0.73,
        "f1": 0.74,
    },
    {
        "id": "random_forest",
        "label": "Random Forest",
        "accuracy": 0.85,
        "precision": 0.83,
        "recall": 0.81,
        "f1": 0.82,
    },
    {
        "id": "svm",
        "label": "SVM",
        "accuracy": 0.83,
        "precision": 0.81,
        "recall": 0.78,
        "f1": 0.795,
    },
    {
        "id": "naive_bayes",
        "label": "Naïve Bayes",
        "accuracy": 0.76,
        "precision": 0.73,
        "recall": 0.71,
        "f1": 0.72,
    },
]


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/metrics")
def metrics():
    return jsonify({"models": METRICS_STUB})


@app.post("/api/predict")
def predict():
    """Placeholder : charger les ``.joblib`` depuis ``models/`` quand ils existent."""
    payload = request.get_json(silent=True) or {}
    model_id = payload.get("model_id", "")
    followers = payload.get("followers")
    following = payload.get("following")

    known = {m["id"]: m["label"] for m in METRICS_STUB}
    if model_id not in known:
        return jsonify({"error": "model_id inconnu", "known": list(known.keys())}), 400

    demo_score = 0
    if followers is not None and following is not None:
        try:
            demo_score = (int(followers) + int(following)) % 2
        except (TypeError, ValueError):
            demo_score = 0

    verdict = (
        "Profil probablement faux (démonstration)"
        if demo_score > 0
        else "Profil probablement authentique (démonstration)"
    )

    return jsonify(
        {
            "model_id": model_id,
            "model_label": known[model_id],
            "verdict": verdict,
            "note": "Remplacer par la probabilité ou la classe prédite par scikit-learn.",
        }
    )


def create_app():
    return app


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
