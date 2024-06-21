import questionary


class MenuViews:
    '''Affiche le menu principale et retourne le choix'''
    def menu_principal():
        choix = (
            questionary.rawselect(
                "Menu principal",
                choices=["Gestion des joueurs",
                         "Gestion des tournois",
                         "Rapports",
                         "Quitter"]).ask()
        )
        return choix

    def menu_joueur():
        '''Affiche le menu joueur et retourne le choix'''
        choix = (
            questionary.rawselect(
                "Menu Gestion des joueurs",
                choices=["Ajouter un joueur",
                         "Modifier un joueur",
                         "Retour au menu principal"]).ask()
        )
        return choix

    def menu_tournoi():
        '''Affiche le menu tournoi et retourne le choix'''
        choix = (
            questionary.rawselect(
                "Menu Gestion des tournois",
                choices=["Ajouter un tournoi",
                         "Ajouter un joueur au tournoi",
                         "Commencer un tournoi",
                         "Retour au menu principal"]).ask()
        )
        return choix

    def menu_modifier_joueur():
        '''Affiche le menu modification du joueur et retourne le choix'''
        choix = (
            questionary.rawselect(
                "Menu Modifier un joueur",
                choices=["Modifier l'adresse",
                         "Modifier l'email",
                         "Modifier le mobile",
                         "Modifier le statut",
                         "Retour au menu principal"]).ask()
        )
        return choix

    def menu_rapport():
        '''Affiche le menu des rapports et retourne le choix'''
        choix = (
            questionary.rawselect(
                "Menu Rapports",
                choices=["Liste des joueurs",
                         "Liste des tournois",
                         "Nom dates de tournoi",
                         "Liste des joureurs du tournoi",
                         "Liste des tours du tournoi",
                         "Retour au menu principal"]).ask()
        )
        return choix
