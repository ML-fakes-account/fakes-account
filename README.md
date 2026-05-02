Description du projet
Ce projet consiste à développer une application de détection de faux profils sur les réseaux sociaux (Instagram, Facebook, Twitter…).
Les faux comptes représentent un risque majeur : désinformation, arnaques, automatisation de spam, etc.
L’objectif est de construire une solution complète allant de la collecte des données à la mise en production d’un modèle ML via une application web.

Objectifs

Collecter et préparer un grand volume de données (open data, scraping, API…).
Explorer et analyser les données pour comprendre les comportements suspects.
Sélectionner les attributs pertinents (feature engineering).
Entraîner plusieurs modèles de Machine Learning.
Évaluer les performances et choisir le modèle optimal.
Développer une application web intégrant le modèle final.


Technologies utilisées 

Python (Pandas, NumPy, Scikit-learn, Matplotlib/Seaborn)
Scraping : BeautifulSoup, Selenium, ou API des réseaux sociaux
Machine Learning (Ingé2, ML classique) : régression logistique, KNN, arbre de décision, Random Forest, SVM, Naïve Bayes
Web : backend Flask ou FastAPI + frontend HTML / CSS / JavaScript (sans framework)
Versioning : Git & GitHub

Approche méthodologique

1) Collecte des données

Open data
Scraping
Extraction via API
Nettoyage et consolidation des différentes sources

2) Analyse exploratoire (EDA)
Étude de variables telles que :

nombre de followers
nombre de comptes suivis
nombre de posts par jour
taux d’activité suspect (spam, interactions automatisées)

3) Modélisation
Plusieurs algorithmes supervisés classiques : régression logistique, KNN, arbre de décision, Random Forest, SVM, Naïve Bayes.

4) Évaluation

Matrice de confusion
Accuracy, Precision, Recall, F1-score
Sélection du meilleur modèle pour l’application

5) Application web
Interface HTML / CSS / JavaScript (sans framework) : affichage des métriques, comparaison des modèles, choix du modèle, prédiction (connectée ensuite au backend Python).

---

## Structure du dépôt

| Élément | Rôle |
|--------|------|
| `data/raw/` | Jeux de données sources (CSV, etc.) — non versionnés si volumineux |
| `data/processed/` | Données nettoyées / features pour l’entraînement |
| `models/` | Modèles sauvegardés (`joblib`) après entraînement |
| `notebooks/` | Notebook Jupyter principal : `projet_fake_profiles.ipynb` |
| `src/` | Utilitaires Python (chemins, chargement CSV) |
| `backend/` | API Flask (`/api/metrics`, `/api/predict`) |
| `frontend/` | Interface HTML / CSS / JavaScript |

---

## Environnement Python (Windows)

Python **3.11** ou **3.12** recommandé. À la racine du dépôt :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Jupyter

Lancer Jupyter **depuis la racine** `fakes-account` pour que les imports `src.*` fonctionnent :

```powershell
jupyter notebook notebooks/projet_fake_profiles.ipynb
```

Si `pip install -r requirements.txt` échoue sous Windows avec une erreur de chemin trop long, activez la **prise en charge des chemins longs** (paramètres système ou stratégie de groupe), ou réessayez après `pip install --no-cache-dir -r requirements.txt`. En dernier recours, créez un nouveau dossier projet avec un chemin plus court sur le disque.

### Backend Flask

Toujours depuis la racine du dépôt :

```powershell
.\venv\Scripts\Activate.ps1
python -m flask --app backend.app run --debug
```

API disponible sur `http://127.0.0.1:5000` — exemples : `GET /api/health`, `GET /api/metrics`, `POST /api/predict` (JSON : `model_id`, `followers`, `following` pour la démo).

### Frontend (fichiers statiques)

Dans un **second** terminal :

```powershell
python -m http.server 8080 --directory frontend
```

Ouvrir `http://localhost:8080`. Pour brancher le tableau de bord sur l’API, remplacer dans `frontend/js/app.js` les données statiques par des appels `fetch()` vers `http://127.0.0.1:5000/api/...` (même machine ; attention aux politiques CORS déjà assouplies côté Flask pour le développement).

---

## Fichier de configuration optionnel

Copier `.env.example` vers `.env` si vous centralisez des variables locales (non commitées).
