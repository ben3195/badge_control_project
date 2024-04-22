from dataclasses import dataclass
from .ILecteur import ILecteur


@dataclass
class LecteurFake(ILecteur):
    lecteur_count = 0
    id: int
    _detection_simulee: bool = False

    def __init__(self):
        LecteurFake.lecteur_count += 1
        self.id = LecteurFake.lecteur_count

    def badge_detecte(self) -> bool:
        returnedValue = self._detection_simulee
        self._detection_simulee = False
        return returnedValue

    def simuler_detection_badge(self):
        self._detection_simulee = True

    def __eq__(self, other: 'LecteurFake'):
        return self.id == other.id

    def __hash__(self):
        return hash(object())
