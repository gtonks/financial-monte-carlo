import matplotlib.pyplot as plt


def run_path(start_value: float, t: float, dt: float) -> list:
    path = [start_value]
    end = t
    t = dt
    while t <= end:
        path.append(start_value+1)
        t += dt
    return path

n_paths = 10#0
start_value = 10_000
t = 10
dt = 1

paths = list()
for n_path in range(n_paths):
    paths.append(run_path(start_value, t, dt))

for path in paths:
    plt.plot(path)
plt.show()
