class Inflation:
    def __init__(self, mean_rate: float) -> None:
        self.mean_rate = mean_rate

    def get_rate(self) -> float:
        return self.mean_rate
