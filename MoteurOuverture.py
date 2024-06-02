from dataclasses import dataclass, field
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte
from association_lecteur_porte import AssociationsLecteurPorte, Lecteur
from utils.access_rules import RegleDeBase
from typing import Iterable, Set, List, Dict

from utils.badge import Badge


@dataclass
class MoteurOuverture:
    _associations: AssociationsLecteurPorte = AssociationsLecteurPorte()
    _liste_noire: Set[int] = field(default_factory=set)
    _regles_acces: Dict[int, List[RegleDeBase]] = field(default_factory=dict)

    def interroger(self):
        lecteurs: Iterable[Lecteur] = self._associations.lecteurs_ayant_detecte_un_badge
        portesAOuvrir: Set[IPorte] = set()

        for lecteur in lecteurs:
            badge = lecteur.badge_detecte
            if badge.numero in self._liste_noire:  # Check if the badge is blacklisted
                continue
            if not self._verifier_acces(lecteur.badge_detecte):
                continue
            for porte in lecteur.portes:
                portesAOuvrir.add(porte)

        for porte in portesAOuvrir:
            porte.ouvrir()

    def associer(self, lecteur: ILecteur, porte: IPorte):
        self._associations.enregistrer(lecteur, porte)

    def bloquer_badge(self, badge: Badge):
        self._liste_noire.add(badge.numero)

    def ajouter_regle(self, numero_badge: int, regle: RegleDeBase):
        if numero_badge not in self._regles_acces:
            self._regles_acces[numero_badge] = []
        self._regles_acces[numero_badge].append(regle)

    def _verifier_acces(self, badge: Badge) -> bool:
        if badge.is_pass_all:
            return True
        if badge.numero not in self._regles_acces:
            return False
        for rule in self._regles_acces[badge.numero]:
            if not rule.is_valid():
                return False
        return True