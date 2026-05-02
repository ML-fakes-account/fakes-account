# Jalons du projet (corpus pour GitHub Issues)

Les fichiers `XX-etape-*.md` dupliquent le corps des issues ouvertes sur le dépôt pour pouvoir les versionner dans Git.

Pour **recréer** les issues après un nouveau fork ou clone :

```powershell
cd fakes-account
gh issue create --title "Étape 1 · Cadre du problème et périmètre du projet" --body-file .github/project-issues/01-etape-1.md
# … répéter pour 02 … 10 avec les titres utilisés sur GitHub
```

Titres utilisés : Étapes 1 à 9 comme dans les fichiers, plus « Qualité du dépôt et livrables » pour `10-depot-rendu.md`.
