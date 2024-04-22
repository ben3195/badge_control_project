from dataclasses import dataclass
from .IPorte import IPorte


@dataclass(eq=True)
class PorteSpy(IPorte):
    ouverture_demandee: bool = False

    def ouvrir(self):
        self.ouverture_demandee = True

    def __hash__(self):
        return hash(object())

