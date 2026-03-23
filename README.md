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
Machine Learning : RandomForest, SVM, XGBoost, Logistic Regression
Web App : Flask / FastAPI / Streamlit
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
Tests de plusieurs algorithmes :

Régression Logistique
Random Forest
XGBoost
SVM

4) Évaluation

Matrice de confusion
Accuracy, Precision, Recall, F1-score
Sélection du meilleur modèle pour l’application

5) Application web
Interface permettant de :

Entrer les informations d’un profil
Obtenir une prédiction → Faux profil / Profil légitime
