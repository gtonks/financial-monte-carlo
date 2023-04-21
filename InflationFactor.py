from Factor import Factor
from Inflation import Inflation


class InflationFactor(Factor):
    def __init__(self, inflation: Inflation) -> None:
        self.inflation = inflation

    def affect(self, val_before_change: float) -> float:
        rate = self.inflation.get_rate()
        return val_before_change - val_before_change * rate
    