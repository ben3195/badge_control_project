from abc import ABC, abstractmethod


class ILecteur(ABC):

    @abstractmethod
    def badge_detecte(self) -> int | None:
        pass
