# Interface web (HTML, CSS, JavaScript)

Stack volontairement simple pour correspondre aux attendus du cours : pas de framework (pas de React). Les fichiers sont lisibles et commentés pour la soutenance.

## Fichiers

- `index.html` — structure de la page (sections performances, comparaison, prédiction).
- `css/styles.css` — mise en page et thème clair/sombre automatique.
- `js/app.js` — remplissage du tableau et des barres, liste déroulante des modèles, gestion du formulaire.

## Lancement local

Ouvrir `index.html` dans un navigateur, ou servir le dossier avec un petit serveur statique pour éviter les blocages CORS lors des futurs appels `fetch()` vers l’API Python :

```powershell
# exemple avec Python 3
python -m http.server 8080 --directory frontend
```

Puis ouvrir `http://localhost:8080`.

## Intégration ultérieure

Remplacer les données d’exemple dans `js/app.js` par des requêtes `fetch()` vers votre backend (Flask ou FastAPI, selon choix du projet).
