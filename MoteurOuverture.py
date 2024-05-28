from typing import Iterable, Set
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte
from utils.badge import Badge
from association_lecteur_porte import AssociationsLecteurPorte, Lecteur

class MoteurOuverture:
    def __init__(self, associations: AssociationsLecteurPorte = AssociationsLecteurPorte()):
        self._associations = associations
        self._liste_noire: Set[int] = set()

    def interroger(self):
        lecteurs: Iterable[Lecteur] = self._associations.lecteurs_ayant_detecte_un_badge
        portesAOuvrir: Set[IPorte] = set()

        for lecteur in lecteurs:
            if lecteur.badge_detecte() in self._liste_noire:
                return
            for porte in lecteur.portes:
                portesAOuvrir.add(porte)

        for porte in portesAOuvrir:
            porte.ouvrir()

    def associer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.enregistrer(lecteur, porte)

    def bloquer_badge(self, badge: Badge):
        self._liste_noire.add(badge.numero)

    def __eq__(self, other):
        if not isinstance(other, MoteurOuverture):
            return False
        return self._associations == other._associations and self._liste_noire == other._liste_noire

    def __hash__(self):
        return hash((self._associations, tuple(self._liste_noire)))