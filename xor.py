import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def neuron_output(x, y, z, w1, w2, w3, b):
    return w1 * x + w2 * y + w3 * z + b


# Define neuron parameters
w1, w2, w3, b = 1, -1, 1, 0  # This defines the plane x - y + z = 0

# Create a grid of points
x = y = z = np.linspace(-2, 2, 30)
X, Y, Z = np.meshgrid(x, y, z)

# Compute neuron output
output = neuron_output(X, Y, Z, w1, w2, w3, b)

# Create the plot
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection="3d")

# Plot the hyperplane
ax.plot_surface(
    X, Y, Z, output, cmap="coolwarm", alpha=0.8, linewidth=0, antialiased=False
)

# Add a contour where the output is zero (the hyperplane)
ax.contour(X, Y, Z, output, levels=[0], colors="k", linestyles="solid")

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.set_title("3D Visualization of Neuron Hyperplane")

plt.show()
