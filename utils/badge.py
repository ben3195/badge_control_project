import itertools

class Badge:
    numero = itertools.count(1)

    def __init__(self):
        self.numero = next(self.numero)
