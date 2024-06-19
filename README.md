Présentation:

L'application est un programme autonome et hors ligne. Qui permet aux organisateurs d'un club d'échec de la mise en place de tournois.
Le programme nous permet de sauvegarder et charger l'état du programme à tout moment entre deux actions de l'utilisateur.


Prérequis

- Installer python selon votre OS: https://www.python.org/downloads/
- Télécharger le répertoire et l'extraire: https://github.com/AzizBouzid/Projet4
- Créer votre environnement virutel avec la commande: py -m venv venv
- Activer votre environnement avec la commande:
	- Windows: source env/Scripts/activate
	- Mac ou Linux: source env/bin/activate
- Installation des packages: pip install -r requirements.txt


Exécution

Pour executer le programme il faut lancer: mai.py

Menu principal (Use shortcuts)
 » 1) Gestion des joueurs
   2) Gestion des tournois
   3) Rapports
   4) Quiter
   
- Le premier choix permet d'ajouter un joueur ou le modifier
- Le second permet d'ajouter et lancer un tournoi
- Le troisième permet d'avoir des rapports


Rapport Flake8

Pour générer le rapport flake8: flake8 --format=html --htmldir=flake-report 
Qu'on peux trouver dans le répertoire: flake-report