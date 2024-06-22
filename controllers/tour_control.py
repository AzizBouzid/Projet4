from views.tour_views import ChoixJoueurView
from models.tour_models import ChoixJoueurModel
from tinydb import TinyDB, Query
import json
from datetime import datetime

Valider = Query()
BDD = TinyDB('data/tournois.json', indent=4)
tournoi = BDD.table('Tournois')
BD = TinyDB('data/joueurs.json', indent=4)
joueur = BD.table('Joueurs')
tour = BDD.table('Tour')
tourtmp = BDD.table('TourTmp')


class ChoixJoueurControl():
    '''Début du tour'''
    def __init__(self):
        self.nom = ChoixJoueurView().ajout_nom_tournoi()

    def tour(self):
        nom = self.nom
        identifiant = tournoi.get(Valider.Nom == nom).get(
            'Identifiant_national')
        Nombre_tours = tournoi.get(Valider.Nom == nom).get(
            'Nombre_tours')
        Nombre_tours_actuel = tournoi.get(Valider.Nom == nom).get(
            'Nombre_tours_actuel')
        if Nombre_tours == Nombre_tours_actuel:
            return
        liste_id = []
        a = 0
        while a < len(identifiant):
            liste_id.append(identifiant[a][0])
            a += 1
        listes_joueur = []
        data = json.load(open("data/joueurs.json"))
        x = 0
        while x < len(liste_id):
            for id in data:
                for player in data[id]:
                    liste = []
                    if data[id][player]['Identifiant_national'] == liste_id[x]:
                        liste.append(data[id][player]['Identifiant_national'])
                        liste.append(data[id][player]['Nom'])
                        liste.append(data[id][player]['Prenom'])
                        liste.append(
                            int(data[id][player]['Score_Total']))
                        listes_joueur.append(liste)
                x += 1
        if len(tourtmp) > 0:
            liste_tmp = tourtmp.get(Valider.Nom == nom).get('Id')
        else:
            liste_tmp = []
        nombre = 1
        if nombre > 1:
            resultat = tour.get(Valider.Tour == nombre).get(
                'List_match')
            listes_joueur = resultat
        listes_joueur_trier = sorted(
            listes_joueur, key=lambda k: k[3], reverse=True)
        listes_comb = ChoixJoueurControl.combinliste(listes_joueur_trier, 2)
        nombre = len(tour) + 1
        while nombre < len(identifiant):
            while True:
                date_d = datetime.now().strftime("%d/%m/%Y")
                heure_d = datetime.now().strftime("%H:%M")
                ChoixJoueurControl.matche(
                    self, nom, identifiant, liste_tmp, listes_comb,
                    listes_joueur, nombre, date_d, heure_d)
                reponse = ChoixJoueurView.continuer()
                if reponse is False:
                    return
                nombre += 1
                if nombre == len(identifiant):
                    BDD.drop_table('TourTmp')
                    return

    def matche(self, nom, identifiant, liste_tmp, listes_comb, listes_joueur,
               nombre, date_d, heure_d):
        '''Début du match'''
        i = 0
        liste_match = []
        Liste = []
        while i < len(listes_comb):
            adversaire = [listes_comb[i][0][0], listes_comb[i][1][0]]
            Id1 = listes_comb[i][0][0]
            Id2 = listes_comb[i][1][0]
            if not ChoixJoueurControl.doublon(liste_tmp, adversaire):
                if not ChoixJoueurControl.listeMatch(liste_match, Id1, Id2):
                    print(listes_comb[i][0][1] + ' ' + listes_comb[i]
                          [0][2], 'Contre', listes_comb[i][1][1] + ' ' +
                          listes_comb[i][1][2])
                    liste_tmp.append(adversaire)
                    liste_match.append(Id1)
                    liste_match.append(Id2)
                    choice = ChoixJoueurView().choix_joueurs()
                    match choice:
                        case 'Le premier joueur gagnant':
                            for match in listes_joueur:
                                if listes_comb[i][0][0] in match:
                                    Li = [[Id1, listes_comb[i][0][1],
                                           listes_comb[i][0][2], 1],
                                          [Id2, listes_comb[i][1][1],
                                           listes_comb[i][1][2], 0]]
                                    Liste.append(Li)
                        case 'Le deuxieme joueur gagnant':
                            for match in listes_joueur:
                                if listes_comb[i][1][0] in match:
                                    Li = [[Id1, listes_comb[i][0][1],
                                           listes_comb[i][0][2], 0],
                                          [Id2, listes_comb[i][1][1],
                                           listes_comb[i][1][2], 1]]
                                    Liste.append(Li)
                        case 'Match null':
                            for match in listes_joueur:
                                if listes_comb[i][0][0] in match:
                                    Li = [[Id1, listes_comb[i][0][1],
                                           listes_comb[i][0][2], 0.5],
                                          [Id2, listes_comb[i][1][1],
                                           listes_comb[i][1][2], 0.5]]
                                    Liste.append(Li)
            i += 1
        date_f = datetime.now().strftime("%d/%m/%Y")
        heure_f = datetime.now().strftime("%H:%M")
        for score_id in identifiant:
            for score in Liste:
                for i in score:
                    if score_id[0] == i[0]:
                        score_id[1] = score_id[1] + i[3]
        for iddentfiant in Liste:
            for score in iddentfiant:
                score_j = joueur.get(Valider.Identifiant_national ==
                                     score[0]).get('Score_Total')
                score_j = score_j + score[3]
                joueur.update({'Score_Total': score_j},
                              Valider.Identifiant_national == score[0])
        ChoixJoueurModel.choix_joueurs_model(self, nom, identifiant, Liste,
                                             liste_tmp, nombre, date_d,
                                             heure_d, date_f, heure_f)

    def doublon(liste, adversaire):
        '''Vérification du doublon'''
        for d in liste:
            if d == adversaire:
                return True

    def combinliste(seq, k):
        '''Création de la liste combinaison'''
        p = []
        i, imax = 0, 2**len(seq)-1
        while i <= imax:
            s = []
            j, jmax = 0, len(seq)-1
            while j <= jmax:
                if (i >> j) & 1 == 1:
                    s.append(seq[j])
                j += 1
            if len(s) == k:
                p.append(s)
            i += 1
        return p

    def listeMatch(liste, j, j1):
        '''Vérification des couples'''
        for d in liste:
            if d == j or d == j1:
                return True
