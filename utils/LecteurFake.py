from dataclasses import dataclass
from .ILecteur import ILecteur


@dataclass(eq=True)
class LecteurFake(ILecteur):
    _detection_simulee: bool = False

    def badge_detecte(self) -> bool:
        returnedValue = self._detection_simulee
        self._detection_simulee = False
        return returnedValue

    def simuler_detection_badge(self):
        self._detection_simulee = True

    def __hash__(self):
        return hash(object())