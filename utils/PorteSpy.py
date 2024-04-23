from dataclasses import dataclass
from .IPorte import IPorte


@dataclass
class PorteSpy(IPorte):
    porte_count = 0
    id: int
    nombre_ouverture_demandees: int = 0

    def __init__(self):
        PorteSpy.porte_count += 1
        self.id = PorteSpy.porte_count

    def ouvrir(self):
        self.nombre_ouverture_demandees += 1

    def __eq__(self, other: 'PorteSpy'):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
