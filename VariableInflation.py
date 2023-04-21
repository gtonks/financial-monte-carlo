import random

from Inflation import Inflation


class VariableInflation(Inflation):
    def __init__(self, mean_rate: float, std: float) -> None:
        super().__init__(mean_rate)
        self.std = std

    def get_rate(self) -> float:
        return random.gauss(self.mean_rate, self.std)
