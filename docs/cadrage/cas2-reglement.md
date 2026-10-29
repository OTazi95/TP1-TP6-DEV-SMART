# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Pouvoir repondre a n'importe quelle question en relation avec le réglement intérieur.

## Utilisateur final (obligatoire)
L'utilisateur qui a eu la reponse a sa question sur le réglement interieur. 

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(b) Il facilement fesable de verifier si la reponse est correct ou pas car nous disposant de l'ensemble des régles (d) Une mauvaise reponse peut provoqué un malentendue, la conséquence est assez grave.

## Données nécessaires et leur origine (obligatoire)
L'import des diferents données issue du reglement interieur (Ce qui est permis ce qui ne l'est pas, les conséquances des differentes actions).

## Métrique de succès et seuil d'acceptation (obligatoire)
F1 macro sur un jeu de test tenu à l'écart ; acceptation à partir de 0,85, avec un rappel d'au moins 0,90 sur les regles tres importantes et essentielles.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une erreur de reponse sur le reglement interieur peut provoquer un malentendue et des incomprehension majeur, Il faut imperativement ce refere aux regles si une reponse parait suspect.

## Risques éthiques ou de confidentialité (obligatoire)
Les regles sont applicable a tout le monde abstraction faite suir la peronne ou l'entite en question.

## Approche écartée et pourquoi (facultatif)

