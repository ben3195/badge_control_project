from dataclasses import dataclass


@dataclass
class Badge:
    badge_count = 0
    numero: int
    is_pass_all: bool = False

    def __init__(self, pass_all: bool = False):
        Badge.badge_count += 1
        self.numero = Badge.badge_count
        self.is_pass_all = pass_all

    def __eq__(self, other: 'Badge'):
        return self.numero == other.numero

    def __hash__(self):
        return hash(self.numero)
