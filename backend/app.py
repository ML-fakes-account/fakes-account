from __future__ import annotations
from pathlib import Path
import numpy as np
import joblib
from flask import Flask, request, render_template_string

app = Flask(__name__)

MODELS_DIR = Path(__file__).parent.parent / "models"
MODEL_PATH  = MODELS_DIR / "random_forest.joblib"
SCALER_PATH = MODELS_DIR / "scaler.joblib"
MODEL  = joblib.load(MODEL_PATH)  if MODEL_PATH.exists()  else None
SCALER = joblib.load(SCALER_PATH) if SCALER_PATH.exists() else None

FEATURES = [
    "followers_count", "favourites_count", "friends_count", "statuses_count",
    "average_tweets_per_day", "account_age_days", "verified", "geo_enabled",
    "default_profile"
]

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head><meta charset="UTF-8"><title>Détection faux profils</title></head>
<body>
  <h1>Détection de faux profils Twitter</h1>
  <form method="POST">
    <p>Followers : <input type="number" name="followers_count" value="{{ vals.followers_count }}"></p>
    <p>Comptes suivis : <input type="number" name="friends_count" value="{{ vals.friends_count }}"></p>
    <p>Nombre de tweets : <input type="number" name="statuses_count" value="{{ vals.statuses_count }}"></p>
    <p>Tweets par jour : <input type="number" name="average_tweets_per_day" step="0.01" value="{{ vals.average_tweets_per_day }}"></p>
    <p>Age du compte (jours) : <input type="number" name="account_age_days" value="{{ vals.account_age_days }}"></p>
    <p>Nombre total de tweets likés depuis la création : <input type="number" name="favourites_count" value="{{ vals.favourites_count }}"></p>
    <p>Compte vérifié : <input type="checkbox" name="verified" value="1" {{ 'checked' if vals.verified else '' }}></p>
    <p>Profil par défaut : <input type="checkbox" name="default_profile" value="1" {{ 'checked' if vals.default_profile else '' }}></p>
    <p>Géolocalisation activée : <input type="checkbox" name="geo_enabled" value="1" {{ 'checked' if vals.geo_enabled else '' }}></p>
    <p><input type="submit" value="Analyser"></p>
  </form>
  {% if verdict %}
    <h2>Résultat : {{ verdict }}</h2>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    verdict = None
    vals = {f: "" for f in FEATURES}

    if request.method == "POST":
        vals["followers_count"]        = request.form.get("followers_count", 0)
        vals["friends_count"]          = request.form.get("friends_count", 0)
        vals["statuses_count"]         = request.form.get("statuses_count", 0)
        vals["average_tweets_per_day"] = request.form.get("average_tweets_per_day", 0)
        vals["account_age_days"]       = request.form.get("account_age_days", 0)
        vals["favourites_count"]       = request.form.get("favourites_count", 0)
        vals["verified"]               = 1 if request.form.get("verified") else 0
        vals["geo_enabled"]            = 1 if request.form.get("geo_enabled") else 0
        vals["default_profile"]        = 1 if request.form.get("default_profile") else 0
        features = np.array([[float(vals[f] or 0) for f in FEATURES]])
        features = SCALER.transform(features)
        pred = MODEL.predict(features)[0]
        verdict = "Faux profil" if pred == 1 else "Profil réel"

    return render_template_string(HTML, verdict=verdict, vals=vals)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
