import random

from Inflation import Inflation


class VariableInflation(Inflation):
    def __init__(self, mean_rate: float, std: float) -> None:
        super().__init__(mean_rate)
        self.std = std
        self.countdown = 0

    def get_rate(self, dt: float, **kwargs) -> float:
        self.countdown -= dt
        if self.countdown <= 0:
            self.rate = random.gauss(self.mean_rate, self.std)
            self.countdown = 1
        return self.rate
