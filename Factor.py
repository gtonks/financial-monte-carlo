class Factor:
    """
    A Factor is anything that affects your assets.
    """
    def affect(self, val_before_change: float, t: float) -> float:
        raise NotImplementedError
    