from dataclasses import dataclass, field
from typing import Iterable, Set
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte
from utils.badge import Badge
from association_lecteur_porte import AssociationsLecteurPorte, Lecteur


@dataclass
class MoteurOuverture:
    _associations: AssociationsLecteurPorte = AssociationsLecteurPorte()
    _liste_noire: Set[int] = field(default_factory=set)

    def interroger(self):
        lecteurs: Iterable[Lecteur] = self._associations.lecteurs_ayant_detecte_un_badge
        portesAOuvrir: Set[IPorte] = set()

        for lecteur in lecteurs:
            if lecteur.badge_detecte in self._liste_noire:
                return
            for porte in lecteur.portes:
                portesAOuvrir.add(porte)

        for porte in portesAOuvrir:
            porte.ouvrir()

    def associer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.enregistrer(lecteur, porte)

    def bloquer_badge(self, badge: Badge):
        self._liste_noire.add(badge.numero)
