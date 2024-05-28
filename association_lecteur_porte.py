from typing import Iterable
from collections import defaultdict
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte

class AssociationsLecteurPorte:
    def __init__(self):
        self._associations = set()

    @property
    def lecteurs_ayant_detecte_un_badge(self) -> Iterable['Lecteur']:
        groupes = defaultdict(list)
        for lecteur, porte in self._associations:
            groupes[lecteur].append(porte)

        for lecteur, portes in groupes.items():
            if lecteur.badge_detecte():
                yield Lecteur(portes)

    def enregistrer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.add((lecteur, porte))

class Lecteur:
    def __init__(self, portes: Iterable[IPorte]):
        self.portes = portes

    def badge_detecte(self) -> bool:
        pass
