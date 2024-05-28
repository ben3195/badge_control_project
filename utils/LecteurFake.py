from dataclasses import dataclass
from .ILecteur import ILecteur

@dataclass
class LecteurFake(ILecteur):
    def __init__(self):
        self._détectionSimulée = False
        self.id = id(self)

    def badge_detecte(self) -> bool:
        returnedValue = self._détectionSimulée
        self._détectionSimulée = False
        return returnedValue

    def simuler_detection_badge(self):
        self._détectionSimulée = True

    def __eq__(self, other):
        if isinstance(other, LecteurFake):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
