import matplotlib.pyplot as plt
import numpy as np

# Single vector transformation
vector = np.array([1.5, 2])
transformed_vector = np.array([vector[0] ** 2, vector[1]])

# Line transformation
t = np.linspace(-2, 2, 100)
line = np.column_stack((t, t + 1))
transformed_line = np.column_stack((t**2, t + 1))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Single vector
ax1.quiver(
    0,
    0,
    vector[0],
    vector[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="r",
    label="Original",
)
ax1.quiver(
    0,
    0,
    transformed_vector[0],
    transformed_vector[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="b",
    label="Transformed",
)
ax1.set_title("x^2 Applied to Single Vector")
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)
ax1.legend()
ax1.grid(True)

# Line
ax2.plot(line[:, 0], line[:, 1], "r", label="Original Line")
ax2.plot(transformed_line[:, 0], transformed_line[:, 1], "b", label="Transformed Line")
ax2.set_title("x^2 Applied to Entire Line")
ax2.set_xlim(-1, 4)
ax2.set_ylim(-1, 3)
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
