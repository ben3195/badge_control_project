from abc import ABC, abstractmethod


class IPorte(ABC):

    @abstractmethod
    def ouvrir(self) -> None:
        pass
