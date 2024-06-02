from abc import ABC, abstractmethod


class RegleDeBase(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass


class RegleAccesParDefaut(RegleDeBase):
    def is_valid(self) -> bool:
        return True


class ReglePassePartout(RegleDeBase):

    def is_valid(self) -> bool:
        return True
