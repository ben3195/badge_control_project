from .IPorte import IPorte

class PorteSpy(IPorte):
    _porte_count = 0

    def __init__(self):
        PorteSpy._porte_count += 1
        self.id = PorteSpy._porte_count
        self.nombre_ouverture_demandees = 0

    @property
    def ouverture_demandee(self):
        return  self.nombre_ouverture_demandees > 0

    def ouvrir(self):
        self.nombre_ouverture_demandees += 1

    def __eq__(self, other: 'PorteSpy'):
        if not isinstance(other, PorteSpy):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
