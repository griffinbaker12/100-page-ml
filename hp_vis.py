import matplotlib.pyplot as plt
import numpy as np


def neuron_boundary(x, w1, w2, b):
    return -(w1 * x + b) / w2


# Define 3 neurons
neurons = [
    {"w1": 1, "w2": -1, "b": 0},  # x - y = 0
    {"w1": -0.5, "w2": 1, "b": 1},  # -0.5x + y = -1
    {"w1": 0.2, "w2": 1, "b": -2},  # 0.2x + y = 2
]

x = np.linspace(-5, 5, 100)

plt.figure(figsize=(10, 8))

for i, neuron in enumerate(neurons):
    y = neuron_boundary(x, neuron["w1"], neuron["w2"], neuron["b"])
    plt.plot(x, y, label=f"Neuron {i+1}")

plt.title("Multiple Neuron Hyperplanes (2D Representation)")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(y=0, color="k", linestyle="--", alpha=0.5)
plt.axvline(x=0, color="k", linestyle="--", alpha=0.5)
plt.legend()
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.show()
