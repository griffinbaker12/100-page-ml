import numpy as np
import matplotlib.pyplot as plt


def neuron_output(x1, x2, w1, w2, b):
    return w1 * x1 + w2 * x2 + b


# Define neuron parameters
w1, w2, b = 1, -1, 0  # This defines the line x1 - x2 = 0

# Create a grid of points
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)

# Compute neuron output for each point
Z = neuron_output(X1, X2, w1, w2, b)

# Create the plot
plt.figure(figsize=(10, 8))
plt.contourf(X1, X2, Z, levels=[-1, 0, 1], colors=["#ffaaaa", "#aaaaff"], alpha=0.5)
plt.contour(X1, X2, Z, levels=[0], colors="k", linestyles="dashed")

plt.title("Neuron Decision Boundary (Hyperplane in 2D)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.axhline(y=0, color="k", linestyle="--", alpha=0.5)
plt.axvline(x=0, color="k", linestyle="--", alpha=0.5)
plt.text(3, 3, "w1*x1 + w2*x2 + b > 0", fontsize=12)
plt.text(-4, -4, "w1*x1 + w2*x2 + b < 0", fontsize=12)
plt.text(1, -1, "w1*x1 + w2*x2 + b = 0\n(decision boundary)", fontsize=12)

plt.show()
