# 📄 Pagination Project

Ce projet consiste à implémenter différentes techniques de **pagination** en Python à partir d’un jeu de données (`Popular_Baby_Names.csv`).  
L’objectif est de gérer l’affichage partiel de grands ensembles de données de manière efficace et adaptée à différents besoins.

## Ce que le projet couvre
- **Pagination simple** avec les paramètres `page` et `page_size`.
- **Pagination avec hypermedia** (ajout de métadonnées pour guider la navigation, principe HATEOAS).
- **Pagination résiliente aux suppressions** (les pages restent cohérentes même si des éléments sont supprimés).

## Points clés
- Calcul des index de départ et de fin pour chaque page.
- Gestion des erreurs (valeurs invalides, pages hors limites).
- Fourniture d’informations supplémentaires comme `next_page`, `prev_page`, et `total_pages`.

**Dataset utilisé** : `Popular_Baby_Names.csv`
