from datetime import datetime
import questionary
from controllers.valid import IdentifiantNationalTournoi, NomTournoi
from tinydb import TinyDB, Query
Valider = Query()
BDD = TinyDB('data/tournois.json', indent=4)
tournoi = BDD.table('Tournois')


class TournoiView:
    '''Permet la saisie des données d'un nouveau tournoi
       et retourne la réponse'''
    def ajout_tournoi(self):
        while True:
            nom = questionary.text("Entrez le nom du tournoi: ").ask().upper()
            if not nom:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            lieu = questionary.text(
                "Entrez le lieu du tournoi: ").ask().capitalize()
            if not lieu:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            date_debut = questionary.text(
                "Entrez la date de debut du tournoi (format JJ/MM/AAAA): "
                ).ask()
            try:
                datetime.strptime(date_debut, '%d/%m/%Y')
                break
            except ValueError:
                print("Format de date invalide. format JJ/MM/AAAA")
        while True:
            date_fin = questionary.text(
                "Entrez la date de fin du tournoi (format JJ/MM/AAAA): "
                ).ask()
            try:
                datetime.strptime(date_fin, '%d/%m/%Y')
                break
            except ValueError:
                print("Format de date invalide. format JJ/MM/AAAA")
        nombre_tour = questionary.text(
            "Entrez le nombre du tour: ", default='4').ask()
        if not nom:
            print("La saisie ne peut pas être vide.")
        while True:
            description = questionary.text(
                "Entrez la description: ").ask().capitalize()
            if not description:
                print("La saisie ne peut pas être vide.")
            else:
                break
        tournoi = {'Nom': nom,
                   'Lieu': lieu,
                   'Date_debut': date_debut,
                   'Date_fin': date_fin,
                   'Nombre_tours': nombre_tour,
                   'Nombre_tours_actuel': 0,
                   'Description': description,
                   'Identifiant_national': []
                   }
        return tournoi

    def ajout_joueur_tournoi(self):
        '''Permet la saisie des données pour ajouter un joueur au tournoi'''
        nom = questionary.text(
            "Entrez le nom du tournoi: ",
            validate=NomTournoi,
            ).ask().upper()
        if not nom:
            print("La saisie ne peut pas être vide.")
        identifiant_national = questionary.text(
            "Entrez l'identifiant national du joueur: ",
            validate=IdentifiantNationalTournoi,
        ).ask().upper()
        return nom, identifiant_national

    def commencer_tour_tournoi(self):
        '''Permet la saisie du nom d'un tournoi'''
        nom = questionary.text(
            "Entrez le nom du tournoi: ",
            validate=NomTournoi,
        ).ask().upper()
        if not nom:
            print("La saisie ne peut pas être vide.")
        return nom

    def confirmation():
        reponse = questionary.confirm(
            "Voulez ajouter un autre tournoi?", default=True).ask()
        return reponse

    def confirmation_joueur():
        reponse = questionary.confirm(
            "Voulez ajouter un autre joueur?", default=True).ask()
        return reponse
