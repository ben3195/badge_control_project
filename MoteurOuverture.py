from dataclasses import dataclass, field
from typing import Dict
from utils.ILecteur import ILecteur
from utils.IPorte import IPorte

@dataclass
class MoteurOuverture:
    _associations: Dict[ILecteur, IPorte] = field(default_factory=dict)

    def interroger(self):
        for lecteur, porte in self._associations.items():
            if lecteur.badge_detecte():
                porte.ouvrir()

    def associer(self, lecteur: ILecteur, porte: IPorte):
        self._associations[lecteur] = porte

