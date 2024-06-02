from collections import defaultdict
from typing import Set, Tuple, Iterable, Dict
from utils.IPorte import IPorte
from utils.ILecteur import ILecteur
from utils.badge import Badge


class Lecteur:
    def __init__(self, portes: Iterable[IPorte], badge_detecte: Badge | None):
        self.portes = portes
        self.badge_detecte = badge_detecte


class AssociationsLecteurPorte:
    _associations: Set[Tuple[ILecteur, IPorte]] = set()

    @property
    def lecteurs_ayant_detecte_un_badge(self) -> Iterable[Lecteur]:
        groupes: Dict[ILecteur, Iterable[IPorte]] = self._group_associations()
        for lecteur, portes in groupes.items():
            badge_detecte = lecteur.badge_detecte()
            if badge_detecte is None:
                continue
            yield Lecteur(portes, badge_detecte)

    def enregistrer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.add((lecteur, porte))

    def _group_associations(self) -> Dict[ILecteur, Iterable[IPorte]]:
        groupes = defaultdict(list)
        for lecteur, porte in self._associations:
            groupes[lecteur].append(porte)
        return groupes
