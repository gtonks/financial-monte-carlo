from Inflation import Inflation


class FlatInflation(Inflation):
    def get_rate(self, **kwargs) -> float:
        return self.mean_rate
