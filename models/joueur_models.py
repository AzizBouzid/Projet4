from views.joueur_views import PlayerView
from tinydb import TinyDB, Query

Valider = Query()
BDD = TinyDB('data/joueurs.json', indent=4)
joueur = BDD.table('Joueurs')


class Joueur():
    def __init__(self):
        '''Initialise une instance de joueur'''
        self.view = PlayerView()
        self.player = PlayerView().ajout_joueur()

    def add_joueur(self):
        '''Création du joueur'''
        joueur.insert(self.player)

    def run(self):
        self.add_joueur()


class ModifierAdresseJoueur():
    '''Permet de modifier l'adresse du joueur'''
    def __init__(self):
        self.id = PlayerView().Id_joueur()
        self.player = PlayerView().modifier_adresse_joueur()

    def modif_adresse_joueur(self):
        adresse = self.player
        id = self.id
        joueur.update({'Adresse': adresse}, Valider.Identifiant_national == id)

    def run(self):
        self.modif_adresse_joueur()


class ModifierEmailJoueur():
    '''Permet de modifier l'email du joueur'''
    def __init__(self):
        self.id = PlayerView().Id_joueur()
        self.player = PlayerView().modifier_mail_joueur()

    def modif_mail_joueur(self):
        mail = self.player
        id = self.id
        joueur.update({'Email': mail}, Valider.Identifiant_national == id)

    def run(self):
        self.modif_mail_joueur()


class ModifierMobileJoueur():
    '''Permet de modifier le numéro de téléphone du joueur'''
    def __init__(self):
        self.id = PlayerView().Id_joueur()
        self.player = PlayerView().modifier_mobile_joueur()

    def modif_mobile_joueur(self):
        mobile = self.player
        id = self.id
        joueur.update({'Mobile': mobile}, Valider.Identifiant_national == id)

    def run(self):
        self.modif_mobile_joueur()


class ModifierStatutJoueur():
    '''Permet de modifier le statut du joueur'''
    def __init__(self):
        self.id = PlayerView().Id_joueur()
        self.player = PlayerView().modifier_statut_joueur()

    def modif_statut_joueur(self):
        statut = self.player
        id = self.id
        joueur.update({'Active': statut}, Valider.Identifiant_national == id)

    def run(self):
        self.modif_statut_joueur()
