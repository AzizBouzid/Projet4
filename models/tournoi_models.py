from views.tournoi_views import TournoiView
from tinydb import TinyDB, Query

Valider = Query()
BDD = TinyDB('data/tournois.json', indent=4)
tournoi = BDD.table('Tournois')
BD = TinyDB('data/joueurs.json', indent=4)
joueur = BD.table('Joueurs')


class Tournoi():
    '''Création du tournoi'''
    def __init__(self):
        self.tournoi = TournoiView().ajout_tournoi()

    def ajout_tournoi(self):
        tournoi.insert(self.tournoi)

    def run(self):
        self.ajout_tournoi()


class JoueurTournoi():
    '''Ajout joueur au tournoi'''
    def __init__(self):
        self.nom = TournoiView().ajout_joueur_tournoi()

    def ajout_joueur_tournoi(self):
        identifiant = tournoi.get(Valider.Nom == self.nom[0]).get(
            'Identifiant_national')
        Ajout = [self.nom[1], 0
                 ]
        identifiant.insert(0, Ajout)
        tournoi.update({
            'Identifiant_national': identifiant},
            Valider.Nom == self.nom[0])
