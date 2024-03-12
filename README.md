# Algorithme MOMFO pour l'Ordonnancement de Tâches dans un Environnement Fog-Cloud 💡

Ce dépôt contient une implémentation de l'algorithme d'Optimisation des Mites-Flammes (MOMFO) pour l'ordonnancement de tâches dans un environnement fog-cloud. L'algorithme est conçu pour affecter efficacement les tâches aux machines virtuelles, en optimisant des facteurs tels que le makespan, le temps de traitement et la consommation d'énergie.

## Table des matières

- [Aperçu](#aperçu)
- [Exigences](#exigences)
- [Licence](#licence)
- [Expérience](#expérience)
- [Amélioration](#amélioration)

## Aperçu

L'algorithme d'Optimisation des Mites-Flammes (MOMFO) est une technique d'optimisation inspirée de la nature, appliquée au problème d'ordonnancement des tâches dans les environnements fog-cloud. Il vise à trouver une affectation optimale des tâches aux machines virtuelles, en tenant compte de divers objectifs tels que le makespan, le temps de traitement et la consommation d'énergie.

Implémentation à partir de l'article :
"Une méthode optimale d'ordonnancement des tâches dans un réseau IoT-Fog-Cloud utilisant l'algorithme multi-objectif Moth-Fame" rédigé par Taybeh Salehnia, Ali Seyfollahi, Saeid Raziani, Azad Noori, Ali Ghafari, Anas Ratib Alsoud et Laith Abualigah; reçu le 18 mai 2022, révisé le 20 mai 2023, et accepté le 11 septembre 2023. L'article est sous licence exclusive de Springer Science+Business Media, LLC, faisant partie de Springer Nature 2023.

## Exigences

- Python 3.x
- NumPy (pour les opérations numériques)

Installez les dépendances requises en utilisant :

```bash
pip install -r requirements.txt
```

## Expérience
Afin de réaliser une expérience veuillez :
1) Modifiez les paramètres de l'expérience dans le fichier config.json selon vos besoins.
2) Exécutez le fichier de test test.py en utilisant la commande Python suivante :
```bash
python test.py
```
Cette commande chargera les paramètres de l'expérience à partir du fichier config.json, exécutera l'algorithme MOMFO avec ces paramètres et affichera l'assignation optimale des tâches parmi les machines virtuelles. Cette assignation peut varier en fonction de l'initialisation des Moths.

## Amélioration
1) Initialisation Intelligente des Moths
L'initialisation des Moths peut grandement influencer les performances de l'algorithme. Plutôt que d'utiliser une initialisation aléatoire, envisagez de créer une heuristique intelligente basée sur la nature du problème. Par exemple, vous pourriez assigner initialement les tâches aux machines virtuelles en fonction de leur longueur, du temps d'exécution, ou d'autres caractéristiques pertinentes
2) Différentes Trajectoires pour les Moths
Diversifier les trajectoires des Moths peut aider à explorer un espace de recherche plus large. Ajoutez des variations dans la mise à jour de la position en introduisant différentes trajectoires, telles que des mouvements sinusoidaux, linéaires, ou des changements de direction basés sur des heuristiques spécifiques au problème.
3) Modifier l'attraction des Moths par les flames
Modifiez la manière dont les Moths sont attirés par les flammes en ajustant des paramètres tels que l'intensité d'attraction, la proximité aux flammes, ou en introduisant des heuristiques spécifiques au problème. Cela peut améliorer la convergence de l'algorithme vers des solutions optimales.
4) Approche Pareto Optimale
Si la nature du problème le permet, envisagez d'implémenter une approche Pareto optimale plutôt qu'aggrégée. Utilisez un algorithme multi-objectif comme NSGA-II pour explorer le front Pareto et obtenir des solutions non-dominées offrant un compromis entre différents objectifs.