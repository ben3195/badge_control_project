from abc import ABC, abstractmethod
from datetime import time


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


class RegleAccesTemps(RegleDeBase):
    def __init__(self, start_time: time, end_time: time, current_time: time):
        self.start_time = start_time
        self.end_time = end_time
        self.current_time = current_time

    def is_valid(self) -> bool:
        return self.start_time <= self.current_time <= self.end_time
