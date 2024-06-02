from dataclasses import dataclass
from .ILecteur import ILecteur
from .badge import Badge


@dataclass
class LecteurFake(ILecteur):
    lecteur_count = 0
    id: int
    _dernier_badge: Badge | None = None

    def __init__(self):
        LecteurFake.lecteur_count += 1
        self.id = LecteurFake.lecteur_count

    def badge_detecte(self) -> Badge | None:
        return self._dernier_badge

    def simuler_detection_badge(self, badge: Badge):
        if badge is not None and badge.numero is not None:
            self._dernier_badge = badge
        else:
            self._dernier_badge = None
                
    def __eq__(self, other: 'LecteurFake'):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
