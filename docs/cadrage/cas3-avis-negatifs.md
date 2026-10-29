# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Mettre en avant les avis et retour negatives des clients pou essaye de corriger ou apporté satistfaction.

## Utilisateur final (obligatoire)
La personne qui va traiter les avis négatives des clients.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(c) Le cout est trés reduit car au maximaum il y aurai une dizaine d'avis par jour voire meme beaucoup moins (d) Une erreur de priorité se corrige en un clic par l'agent, la conséquence est faible.

## Données nécessaires et leur origine (obligatoire)
L'import des avis avec leurs informations ( sur quel produit, sa date de création, son type est il positif ou négatif)
Et anonymisé les données personnelles telque : (nom, prenom, age, adresse)

## Métrique de succès et seuil d'acceptation (obligatoire)
F1 macro sur un jeu de test tenu à l'écart ; acceptation à partir de 0,85, avec un rappel d'au moins 0,90

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une erreur de prioritisation ne peut cause de grand degat car cela ne releve qu'enn terme d'amelioration d'experience client.

## Risques éthiques ou de confidentialité (obligatoire)
Il est impérative d'anonymisé toutes les données qui sont personnelles car ils ne vont pas du tout nous aide pour dtermine la priorite de l'avis.

## Approche écartée et pourquoi (facultatif)

