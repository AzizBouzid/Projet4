from questionary import ValidationError
from questionary import Validator
import os
import re
from genericpath import exists
from tinydb import TinyDB, Query

if not exists(f"{'data'}"):
    repertoire = os.mkdir(f"{'data'}")
if not exists(f"{'rapports'}"):
    repertoire = os.mkdir(f"{'rapports'}")

Valider = Query()
BDD = TinyDB('data/joueurs.json')
joueur = BDD.table('Joueurs')
BD = TinyDB('data/tournois.json')
tournoi = BD.table('Tournois')


class IdentifiantNationalJoueur(Validator):
    def validate(self, document):
        ok = re.match(
            r'^[A-Za-z]{2}[0-9]{5}$',
            document.text,
        )
        if not ok:
            raise ValidationError(
                message="Format Identité national invalide."
                "Format exemple AB12345",
                cursor_position=len(document.text),
            )
        if joueur.get(Valider.Identifiant_national == document.text.upper()):
            raise ValidationError(
                message="Le joueur existe déjà",
                cursor_position=len(document.text),
            )


class IdentifiantNationalTournoi(Validator):
    def validate(self, document):
        ok = re.match(
            r'^[A-Za-z]{2}[0-9]{5}$',
            document.text,
        )
        if not ok:
            raise ValidationError(
                message="Format Identité national invalide."
                "Format exemple AB12345",
                cursor_position=len(document.text),
            )
        if not joueur.get(Valider.Identifiant_national == document.text
                          .upper()):
            raise ValidationError(
                message="Le joueur n'existe pas",
                cursor_position=len(document.text),
            )


class NomTournoi(Validator):

    def validate(self, document):

        if not tournoi.get(Valider.Nom == document.text.upper()):
            raise ValidationError(
                message="Le tournoi n'existe pas",
                cursor_position=len(document.text),
            )


class IdJoueur(Validator):
    def validate(self, document):
        ok = re.match(
            r'^[A-Za-z]{2}[0-9]{5}$',
            document.text,
        )
        if not ok:
            raise ValidationError(
                message="Format Identité national invalide."
                "Format exemple AB12345",
                cursor_position=len(document.text),
            )
        if not joueur.get(Valider.Identifiant_national == document.text
                          .upper()):
            raise ValidationError(
                message="Le joueur existe déjà",
                cursor_position=len(document.text),
            )


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = re.match(
            r"^([01])?[-.\s]?\(?(\d{3})\)?"
            r"[-.\s]?(\d{3})[-.\s]?(\d{4})\s?"
            r"((?:#|ext\.?\s?|x\.?\s?)(?:\d+)?)?$",
            document.text,
        )
        if not ok:
            raise ValidationError(
                message="Le numéro de mobile est invalid",
                cursor_position=len(document.text),
            )
