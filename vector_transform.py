# import matplotlib.pyplot as plt
# import numpy as np
#
# rotation_2d = np.array([-1, -1])
#
# vector_2d = np.array([3, 4])
# rotated_2d = rotation_2d * vector_2d
#
# origin = [0, 0]
#
# plt.quiver(
#     origin[0], origin[1], vector_2d[0], vector_2d[1], color="r", units="xy", scale=1
# )
# plt.quiver(
#     origin[0], origin[1], rotated_2d[0], rotated_2d[1], color="b", units="xy", scale=1
# )
# plt.title("Rotated Vector")
#
# plt.xlim(-8, 8)
# plt.ylim(-8, 8)
# plt.grid()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define the rotation matrix for 180 degrees
rotation_matrix = np.array([[-1, 0], [0, -1]])

# Original vector
vector_2d = np.array([3, 4])

# Perform rotation using matrix multiplication
rotated_2d = rotation_matrix @ vector_2d

print(vector_2d, rotated_2d)

# Plotting
origin = [0, 0]
plt.figure(figsize=(10, 10))
plt.quiver(
    origin[0],
    origin[1],
    vector_2d[0],
    vector_2d[1],
    color="r",
    units="xy",
    scale=1,
    label="Original Vector",
)
plt.quiver(
    origin[0],
    origin[1],
    rotated_2d[0],
    rotated_2d[1],
    color="b",
    units="xy",
    scale=1,
    label="Rotated Vector",
)

plt.title("180-Degree Rotation using Matrix Multiplication")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid(True)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.legend()

# Annotate points
plt.annotate(
    f"({vector_2d[0]}, {vector_2d[1]})",
    xy=(vector_2d[0], vector_2d[1]),
    xytext=(3.1, 4.1),
)
plt.annotate(
    f"({rotated_2d[0]}, {rotated_2d[1]})",
    xy=(rotated_2d[0], rotated_2d[1]),
    xytext=(-3.1, -4.1),
)

plt.show()
