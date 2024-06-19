import questionary


class ChoixJoueurView():
    '''Verification du nom de tournoi'''
    def ajout_nom_tournoi(self):
        nom = questionary.text(
            "Entrez le nom du tournois: ",
            # validate=NomTournoi,
        ).ask().upper()
        return nom

    def choix_joueurs(self):
        '''Choix du résultat d'un match'''
        choix = (
            questionary.rawselect(
                "Votre choix",
                choices=["Le premier joueur gagnant",
                         "Le deuxieme joueur gagnant",
                         "Match null",
                         ]).ask()
        )
        return choix

    def continuer():
        question = questionary.confirm(
            "Voulez vous continuer?", default=True
        )
        return question.ask()

    def export(self):
        reponse = questionary.confirm(
            "Voulez vous exporter le résultat?", default=True
        ).ask()
        return reponse
