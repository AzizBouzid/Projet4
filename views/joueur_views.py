from datetime import datetime
import questionary
from controllers.valid import IdentifiantNationalJoueur, PhoneNumberValidator
from controllers.valid import IdJoueur


class PlayerView:
    def ajout_joueur(self):
        '''Permet la saisie des données données d'un nouveau joueur et
           retourne la réponse'''
        identifiant_national = questionary.text(
            "Entrez l'identifiant national du joueur: ",
            validate=IdentifiantNationalJoueur,
        ).ask().upper()
        while True:
            nom = questionary.text("Entrez le nom du joueur: ").ask().upper()
            if not nom:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            prenom = questionary.text("Entrez le prénom du joueur: ",
                                      ).ask().title()
            if not prenom:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            date_naissance = questionary.text(
                "Entrez la date de naissance du joueur (format JJ/MM/AAAA): ",
            ).ask()
            try:
                datetime.strptime(date_naissance, '%d/%m/%Y')
                break
            except ValueError:
                print("Format de date invalide. Format JJ/MM/AAAA")

        while True:
            adresse = questionary.text("Entrez l'adresse': ").ask().title()
            if not adresse:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            mail = questionary.text("Entrez l'email': ").ask()
            if not mail:
                print("La saisie ne peut pas être vide.")
            else:
                break
        while True:
            mobile = questionary.text("Entrez le numéro du mobile: ",
                                      validate=PhoneNumberValidator,
                                      ).ask()
            if not mobile:
                print("La saisie ne peut pas être vide.")
            else:
                break
        player = {'Identifiant_national': identifiant_national,
                  'Nom': nom,
                  'Prenom': prenom,
                  'Date_naissance': date_naissance,
                  'Adresse': adresse,
                  'Email': mail,
                  'Mobile': mobile,
                  'Statut': True,
                  'Score_Total': 0,
                  }
        return player

    def Id_joueur(self):
        '''Verification de l'identifiat'''
        id_national = questionary.text(
            "Entrez l'identifiant national du joueur: ",
            validate=IdJoueur,
        ).ask().upper()
        return id_national

    def modifier_adresse_joueur(self):
        '''Saisie de l'adresse pour la modification'''
        while True:
            nom = questionary.text(
                "Entrez l'adresse du joueur: ").ask().title()
            if not nom:
                print("La saisie ne peut pas être vide.")
            else:
                break
        return nom

    def modifier_mail_joueur(self):
        '''Saisie de l'adresse mail pour la modification'''
        while True:
            mail = questionary.text(
                "Entrez l'email du joueur: ",
                ).ask()
            if not mail:
                print("La saisie ne peut pas être vide.")
            else:
                break
        return mail

    def modifier_mobile_joueur(self):
        '''Saisie de numéro de mobile pour la modification'''
        while True:
            mail = questionary.text(
                "Entrez le mobile du joueur: ",
                validate=PhoneNumberValidator,
                ).ask()
            if not mail:
                print("La saisie ne peut pas être vide.")
            else:
                break
        return mail

    def modifier_statut_joueur(self):
        confirmation = questionary.confirm(
            "Activer le statut du joueur: ").ask()
        return confirmation
