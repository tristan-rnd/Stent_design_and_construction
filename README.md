# Stent_design_and_construction

## Introduction
Ce projet contribue à un projet plus vaste financé par l'Agence Nationale de la Recherche : le projet VSTENT a pour objet de simuler le déploiement de stent dans les artères coronaires. Pour effectuer des simulations temps-réel, il faut disposer de modèles CAO des différents stents. Il en existe de nombreux modèles proposés par plusieurs manufacturiers (Abbott, Boston scientific, Medtronic, Terumo...).

Un stent métallique est composé de couronnes reliées par des connecteurs, chaque couronne étant constituée de mailles. 

Le but de ce projet est de combiner les mailles du projet précédent en couronnes et les couronnes en stent. Le modèle génère le stent à partir de la donnée du manufacturier, du modèle, du diamètre et de la longueur sur stent.

## Utilisation

L'arbre des répertoires est important à respecter pour le fonctionnement du programme.

Le dossier principal contenant les fichiers utilisés est le dossier parent "Mailles", le sous dossier suivant correspond au nom du manufacturier (ex : Terumo) et le sous dossier suivant correspond au nom du modèle (ex : Synergy).
Dans ce dernier répertoire doit se trouver le fichier contenant les points de la maille (format .csv). On y retrouve également le sous dossier "connecteur" qui doit obligatoirement contenir les 4 connecteurs de la maille (haut, droit, bas, gauche au format .csv).

### GUI

```shell
python .\interface.py
```
L'interface graphique est basée sur tkinter.
Il suffit d'aller chercher la maille souhaitée (ex : Mailles\Terumo\Synergy\Maille.csv) puis de saisir la longueur et le diamètre souhaités.
Le stent est généré en cliquant sur "Ok" et une fenêtre s'ouvre lorsque l'exportation a bien eu lieu.

### Invite de commande
```shell
python .\no-gui.py
```
Pour utiliser le programme sans GUI, il suffit de rentrer, dans l'ordre : le constructeur (correspondant au nom du dossier constructeur), le modèle (correspondant au nom du dossier du modèle), le diamètre et la longueur.
Par exemple, pour un stent du constructeur Terumo, modèle Ultimaster Nagomi et avec un diamètre 3.5mm et une longueur de 24mm :
```shell
python .\no-gui.py Terumo Ultimaster_Nagomi 3.5 24
```

## Ajout de modèle
Pour ajouter un nouveau modèle, il faut ajouter dans le sous répertoire correspondant (Mailles/Constructeur/Modèle/) le fichier des points de la maille (ils sont considérés connectés deux à deux : le point de la ligne 1 forme une arête avec le point de la ligne 2) et ses 4 connecteurs.

Ensuite, dans le code source, dans le constructeur de la classe Stent (\__init__) ajouter les indications du nombre de couronnes en fonction du fabricant/modèle/diamètre/longueur (voir implémentation existante pour quelques modèles du fabricant Terumo).
Puis faire de même dans la classe Couronne pour indiquer le nombre de mailles par couronne en fonction du fabricant/modèle/diamètre/longueur (voir implémentation existante pour quelques modèles du fabricant Terumo).
