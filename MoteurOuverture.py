from dataclasses import dataclass
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte
from association_lecteur_porte import AssociationsLecteurPorte, Lecteur
from typing import Iterable, Set


@dataclass
class MoteurOuverture:
    _associations: AssociationsLecteurPorte = AssociationsLecteurPorte()

    def interroger(self):
        lecteurs: Iterable[Lecteur] = self._associations.lecteurs_ayant_detecte_un_badge
        portesAOuvrir: Set[IPorte] = set()

        for lecteur in lecteurs:
            for porte in lecteur.portes:
                portesAOuvrir.add(porte)

        for porte in portesAOuvrir:
            porte.ouvrir()

    def associer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.enregistrer(lecteur, porte)
