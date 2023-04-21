import matplotlib.pyplot as plt
import statistics

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


def report(paths: list):
    ends = [path[-1] for path in paths]
    deciles = statistics.quantiles(ends, n=10)
    quartiles = statistics.quantiles(ends)
    print(f"Minimum end value: {min(ends)               :.2f}")
    print(f"Lower 10%:         {deciles[0]              :.2f}")
    print(f"Lower 75%:         {quartiles[0]            :.2f}")
    print(f"Median end value:  {quartiles[1]            :.2f}")
    print(f"Upper 75%:         {quartiles[-1]           :.2f}")
    print(f"Upper 10%:         {deciles[-1]             :.2f}")
    print(f"Maximum end value: {max(ends)               :.2f}")
    print(f"Mean end value:    {statistics.mean(ends)   :.2f}")


def graph(paths: list):
    for path in paths:
        plt.plot(path)
    plt.show()


n_paths = 200
start_value = 10_000
countdown = 10
dt = 1 / 12
factors = [InflationFactor(VariableInflation(0.04, 0.02))]

paths = list()
for n_path in range(n_paths):
    paths.append(run_path(start_value, countdown, dt, factors))

report(paths)
graph(paths)
