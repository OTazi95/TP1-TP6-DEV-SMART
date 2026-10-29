# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Détécter et completer les ordonnances pharmaceutique incomplettes.

## Utilisateur final (obligatoire)
Le pharmacien recoit une ordonnance complete afin d'attribué le traitement nécessaire

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
(a) Plusieurs ordonnances de plusieurs patient avec des maladies similaires a traités : des données étiquetées existent. (c) Plusieurs milliers d'ordonnances par jour : un classifieur coûte presque rien par requête, un LLM coûterait à chaque appel. (d) Une ordonnance errone peut provoquer de donné un traitement inadapté pour le patient, la conséquence est grave.

## Données nécessaires et leur origine (obligatoire)
importer les données essentielles telque (l'age, la pathologie, l'historique médicale, les rythme alimentaire et activite physiques, le type de maladie et son niveau de gravite).
Ces informations peuvent etre extraites depuis le medcin traitant, et anonymisé les donnes non essentiel telque le nom, prenom, adresse et origine.

## Métrique de succès et seuil d'acceptation (obligatoire)
F1 macro sur un jeu de test tenu à l'écart ; acceptation à partir de 0,85, avec un rappel d'au moins 0,90 sur les maladies a forte risque (la plus urgente).

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une ordonnance erroné doit toujours etre verifié par le pahrmacien avnt de lui donné les médicament pour s'assurer de la compatibilité de la pathologie avec le traitement.

## Risques éthiques ou de confidentialité (obligatoire)
Les ordonnaces et préscription médiacale contiennent parfois des données personnelles c'est pour ça qu'il faut assuré une anonymisation avant le stockage, modèle hébergé en interne et pas d'envoi à un service tiers.

## Approche écartée et pourquoi (facultatif)

