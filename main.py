import matplotlib.pyplot as plt

from VariableInflation import VariableInflation
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

n_paths = 200
start_value = 10_000
countdown = 10
dt = 1 / 12
factors = [InflationFactor(VariableInflation(0.04, 0.02))]

paths = list()
for n_path in range(n_paths):
    paths.append(run_path(start_value, countdown, dt, factors))

for path in paths:
    plt.plot(path)
plt.show()
