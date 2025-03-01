# Description du projet

## Objectif

L'objectif est de créer un casse brique modulable.
Dans un premier temps, nous allons créer programmer une version simple du jeu afin de nous assurer que la base du jeu fonctionne. Pars la suite, nous allons ajouter les fonctionnalitées citées ci-dessous.


## Breakout Challenge

Dans ce jeu de casse-briques revisité, votre objectif est de détruire toutes les briques colorées à l’écran à l’aide d’une balle que vous contrôlez grâce à une raquette. Faites preuve de précision et de rapidité pour éviter de perdre la balle tout en récupérant des bonus qui vous aideront à franchir les niveaux de plus en plus difficiles.

Les graphismes modernes, associés à une bande-son entraînante, rendent l’expérience à la fois immersive et accessible à tous. Idéal pour tester vos réflexes et battre vos propres records !

### Caractéristiques :

Une progression à travers plusieurs niveaux avec des défis croissants.
Des bonus et malus qui modifient le gameplay.
Un système de score pour mesurer vos performances.
Un design épuré, parfait pour des parties rapides ou prolongées.

### Objectif global du jeu:
Détruire toutes les briques, compléter chaque niveau et atteindre le meilleur score possible tout en évitant de perdre la balle.

## Cahier des charge (basic)

Comme décrit ci-dessus, voici la liste de fonctionnalitées basiques qu'il est nécessaire d'implémenter au
départ

- Une grille de brique fixe (à définir)
- Une balle à angle variable
- Une raquette à taille fixe
- Des briques pouvant subir plusieurs coups avant d'êtres détruites
- Un système de score
- Un menu permettant au joueur de _jouer_ ou _quitter_
- Au moins 3 niveaux de briques différents
- Un système de couleur permettant l'identification des vies des briques

## Cahier des charge (advanced)

Dans un deuxième temps, voici ce qui est prévu d'être implémenté

- Différents thèmes (tilesets)
- Vitesse variable de la balle
- Ajout de bonus (aggrandissement de la raquette, super balle etc...)
- Briques invincibles, mobiles
- Ajout de malus (inversion des commandes, ratraicissement de la raquette)
- Multiballe

# Gestion GIT

## Phase développement

Dans un premier temps, durant la phase dite de "développement" la totalité de l'équipe travail sur une seule branche (main). Cela permet à tout le monde de modifier les différentes classes, de ce fait, cela permet à tout le monde d'ajouter les fonctionnalitées nécessaires (les dépendances inter-classes) au bon fonctionnement de leurs tâches.
Il est extrement important d'effectuer des Pull réguliers, des commits ainsi que des push afin que tout le monde travail presque constamment sur la dernière version du projet.

## Phase secondaire

Dans cette phase, une version du jeu "stable" est disponible sur la branche main. L'ajout de nouvelles fonctionnalitées nécessitera la création de branches. De cette manière, la version stable du jeu n'est pas altérée par la création de nouvelles fonctions.
Une fois la branche stable (la fonctionnalité implémentée), un merge request est généré, analysé par l'équipe de développement, et soit validée, soit refusé selon les conflits.

# Tâches

## Integration Pygame

Ding Jérémy

- Créer une fenêtre
- Taille fixe
- Gestion d'entrées
- Gestion affichage

## Collisions

Decrausaz Marc

- Ball- brique
- Ball - murs
- Ball - raquette
- Coins ?
- Rebond ?

## Gestion Niveau

Tornare Magali

- Création du champ de brique
- Création des niveaux
- Essayer de comprendre un truc en python...

## Gestion Bonus

Chaignat Bastien

- Création des bonus
- Intégration dans les briques


# Comment utiliser le code?
Pour lancer le code, veuillez taper : "python breakout" dans le terminal en vous situant dans la base du fichier, soit "MINI_PROJET_BREAKOUT_GAME".

Ce code est utilisable en tant que jeu (car c'est un casse brique). C'est un jeu intéressant qui regorge de secret que nous pouvons lancer en allant directement dans le fichier __main_.py et faire un run du projet. Cela ouvrira un menu dans lequel vous pourrez choisir si vous voulez recommencer une nouvelle aventure, continuer la partie précédente, lire l'histoire du jeu ou quitter le jeu. 


# Comment installer et développer sur le projet ?

Comme c'est un jeu, l'objectif n'est pas de rajouter ou de modifier le code pour que le code fonctionne. 
Pour pouvoir lancer le jeu, il faut tout de même installer poetry. 