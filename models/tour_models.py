from tinydb import TinyDB, Query

Valider = Query()
BDD = TinyDB('data/tournois.json', indent=4)
tournoi = BDD.table('Tournois')
tour = BDD.table('Tour')
BD = TinyDB('data/joueurs.json', indent=4)
joueur = BD.table('Joueurs')
tourtmp = BDD.table('TourTmp')


class ChoixJoueurModel():
    '''Création du tour'''
    def choix_joueurs_model(self, nom, identifiant, Liste, liste_tmp, nombre,
                            date_d, heure_d, date_f, heure_f):
        self.nom = nom
        self.identifiant = identifiant
        self.Liste = Liste
        self.liste_tmp = liste_tmp
        self.nombre = nombre
        self.date_d = date_d
        self.heure_d = heure_d
        self.date_f = date_f
        self.heure_f = heure_f
        Ajout = {"Tour": self.nombre,
                 "Tournoi": self.nom,
                 "Date_debut": self.date_d,
                 "Heure_debut": self.heure_d,
                 "Date_fin": self.date_f,
                 "Heure_fin": self.heure_f,
                 "List_match": []
                 }
        tour.insert(Ajout)
        identifiant = tour.get(Valider.Tour == self.nombre).get(
            'List_match')
        identifiant.insert(0, self.Liste)
        tour.update({
            'List_match': identifiant},
            Valider.Tour == self.nombre)
        tournoi.update({'Identifiant_national': self.identifiant})
        tournoi.update({'Nombre_tours_actuel': self.nombre})
        if len(tourtmp) == 0:
            Ajout_d = {'Nom': self.nom, 'Id': []}
            tourtmp.insert(Ajout_d)
        id_tmp = tourtmp.get(Valider.Nom == self.nom).get(
            'Id')
        id_tmp.insert(0, self.liste_tmp)
        tourtmp.update({'Id': self.liste_tmp})

    def run(self):
        self.choix_joueurs_model()
