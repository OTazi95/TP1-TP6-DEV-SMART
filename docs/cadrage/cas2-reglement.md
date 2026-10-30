# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Offrir un outil capable de répondre à toute question portant sur le règlement intérieur, de façon claire et conforme au texte officiel.

## Utilisateur final (obligatoire)
Toute personne concernée par le règlement intérieur, qui souhaite obtenir une réponse précise à sa question sur les règles en vigueur.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(b) Vérifiabilité : on peut aisément contrôler si une réponse est exacte, puisque l'intégralité du règlement est disponible et peut être comparée à ce que l'outil affirme. (d) Conséquence d'une erreur : une réponse fausse risque de créer des incompréhensions, voire des sanctions injustifiées, ce qui rend l'erreur plutôt grave.

## Données nécessaires et leur origine (obligatoire)
Le contenu complet du règlement intérieur, à importer depuis le document officiel : les comportements autorisés, ceux qui sont interdits et les sanctions prévues pour chaque manquement.

## Métrique de succès et seuil d'acceptation (obligatoire)
F1 macro calculé sur un jeu de test mis de côté ; le système est accepté à partir de 0,85, avec un rappel minimum de 0,90 pour les règles les plus importantes et essentielles.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une réponse erronée peut entraîner de graves malentendus. Lorsqu'une réponse semble douteuse, il est indispensable de la confronter au texte du règlement ou de demander l'avis d'un responsable.

## Risques éthiques ou de confidentialité (obligatoire)
Le règlement s'applique de la même façon à tous, quelle que soit la personne ou la structure concernée. Les données utilisées sont des règles générales et ne contiennent pas d'informations personnelles.

## Approche écartée et pourquoi (facultatif)
Modèle génératif seul : il pourrait inventer des règles inexistantes et ne serait pas capable d'indiquer la source de sa réponse, ce qui est risqué ici.