from dataclasses import dataclass


@dataclass
class Badge:
    badge_count = 0
    numero: int

    def __init__(self):
        Badge.badge_count += 1
        self.numero = Badge.badge_count

    def __eq__(self, other: 'Badge'):
        return self.numero == other.numero

    def __hash__(self):
        return hash(object())
