from views.menu_views import MenuViews
from views.tour_views import ChoixJoueurView
from views.tournoi_views import TournoiView
from models.joueur_models import Joueur, ModifierAdresseJoueur
from models.joueur_models import ModifierEmailJoueur, ModifierMobileJoueur
from models.joueur_models import ModifierStatutJoueur
from models.tournoi_models import Tournoi
from controllers.tour_control import ChoixJoueurControl
from models.tournoi_models import JoueurTournoi
from models.rapport_model import RapportJoueur, RapportNomDateTournoil, \
     RapportTournoi, RapportJoueurTournoi, RapportTourTournoi


def menu_principal_control():
    '''Menu principal'''
    choix = MenuViews.menu_principal()
    match choix:
        case "Gestion des joueurs":
            menu_joueur_control()
        case "Gestion des tournois":
            menu_tournoi_control()
        case "Rapports":
            menu_rapport_control()
        case "Quiter":
            exit()


def menu_joueur_control():
    '''Menu joueur'''
    choix = MenuViews.menu_joueur()
    match choix:
        case "Ajouter un joueur":
            while True:
                Joueur().run()
                reponse = ChoixJoueurView.continuer()
                if reponse is False:
                    menu_joueur_control()
        case "Modifier un joueur":
            modifier_joueur_control()

        case "Retour au menu principal":
            menu_principal_control()
        case "Quiter":
            exit()


def modifier_joueur_control():
    '''Menu modification d'un joueur'''
    choix = MenuViews.menu_modifier_joueur()
    match choix:
        case "Modifier l'adresse":
            ModifierAdresseJoueur().run()
            menu_joueur_control()
        case "Modifier l'email":
            ModifierEmailJoueur().run()
            menu_joueur_control()
        case "Modifier le mobile":
            ModifierMobileJoueur().run()
            menu_joueur_control()
        case "Modifier le statut":
            ModifierStatutJoueur().run()
            menu_joueur_control()
        case "Retour au menu principal":
            menu_principal_control()
        case "Quiter":
            exit()


def menu_tournoi_control():
    '''Menu tournoi'''
    choix = MenuViews.menu_tournoi()
    match choix:
        case "Ajouter un tournoi":
            while True:
                Tournoi().ajout_tournoi()
                reponse = TournoiView.confirmation()
                if reponse is False:
                    menu_tournoi_control()
        case "Ajouter un joueur au tournoi":
            while True:
                JoueurTournoi().ajout_joueur_tournoi()
                reponse = TournoiView.confirmation_joueur()
                if reponse is False:
                    menu_tournoi_control()
        case "Commencer un tournoi":
            ChoixJoueurControl().tour()
            menu_tournoi_control()
        case "Retour au menu principal":
            menu_principal_control()
        case "Quiter":
            exit()


def menu_rapport_control():
    '''Menu rapports'''
    choix = MenuViews.menu_rapport()
    match choix:
        case "Liste des joueurs":
            RapportJoueur().run()
            menu_rapport_control()
        case "Liste des tournois":
            RapportTournoi().run()
            menu_rapport_control()
        case "Nom dates de tournoi":
            RapportNomDateTournoil().run()
            menu_rapport_control()
        case "Liste des joureurs du tournoi":
            RapportJoueurTournoi().run()
            menu_rapport_control()
        case "Liste des tours du tournoi":
            RapportTourTournoi().run()
            menu_rapport_control()
        case "Retour au menu principal":
            menu_principal_control()
        case "Quiter":
            exit()
