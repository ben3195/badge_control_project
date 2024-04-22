from abc import ABC, abstractmethod


class ILecteur(ABC):

    @abstractmethod
    def badge_detecte(self) -> bool:
        pass
