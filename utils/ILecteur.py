from abc import ABC, abstractmethod
from utils.badge import Badge


class ILecteur(ABC):

    @abstractmethod
    def badge_detecte(self) -> Badge | None:
        pass
