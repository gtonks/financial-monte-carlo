import matplotlib.pyplot as plt

from Inflation import Inflation
from InflationFactor import InflationFactor


def run_path(start_value: float, t: float, dt: float, factors: list()) -> list:
    path = [start_value]
    end = t
    t = dt
    while t <= end:
        for factor in factors:
            start_value = factor.affect(start_value, dt)
        path.append(start_value)
        t += dt
    return path

n_paths = 10#0
start_value = 10_000
t = 10
dt = 1
factors = [InflationFactor(Inflation(0.04))]

paths = list()
for n_path in range(n_paths):
    paths.append(run_path(start_value, t, dt, factors))

for path in paths:
    plt.plot(path)
plt.show()
