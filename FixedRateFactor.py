import math

from Factor import Factor


class FixedRateFactor(Factor):
    """
    Useful for fixed rates: CDs, many loans, etc.
    """
    def __init__(self, rate: float) -> None:
        self.rate = rate

    def affect(self, val_before_change: float, t: float) -> float:
        return val_before_change * math.e ** (self.rate * t)
