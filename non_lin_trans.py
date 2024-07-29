import matplotlib.pyplot as plt
import numpy as np

# Original vector
vector_2d = np.array([1.5, 2])


# Non-linear transformation (squaring)
def square_transform(v):
    return np.array([v[0] ** 2, v[1] ** 2])


def linear_transform(v):
    return np.array([v[0] * 2, v[1] * 2])


def affine_transform(v):
    return v + 2


# Apply transformation
transformed_2d = square_transform(vector_2d)
transformed_2d_linear = linear_transform(vector_2d)
transformed_affine = affine_transform(vector_2d)

# Plotting
origin = [0, 0]
plt.figure(figsize=(10, 10))

# Plot original vector
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

# Plot transformed vectors
for i, transformed_v in enumerate(
    (transformed_2d, transformed_2d_linear, transformed_affine)
):
    plt.quiver(
        origin[0] if i != 2 else 2,
        origin[1] if i != 2 else 2,
        transformed_v[0],
        transformed_v[1],
        color="b" if i == 0 else "r" if i == 1 else "g",
        units="xy",
        scale=1,
        label="Transformed Vector",
    )

plt.title("Non-Linear Transformation: f(x) = x^2")
plt.xlim(0, 5)
plt.ylim(0, 10)
plt.grid(True)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.legend()

# Annotate points
plt.annotate(
    f"({vector_2d[0]}, {vector_2d[1]})",
    xy=(vector_2d[0], vector_2d[1]),
    xytext=(vector_2d[0] + 0.1, vector_2d[1] + 0.1),
)
plt.annotate(
    f"({transformed_2d[0]:.2f}, {transformed_2d[1]:.2f})",
    xy=(transformed_2d[0], transformed_2d[1]),
    xytext=(transformed_2d[0] + 0.1, transformed_2d[1] + 0.1),
)

plt.show()

print(f"Original vector: {vector_2d}")
print(f"Transformed vector: {transformed_2d}")

# Demonstrate non-linearity
scalar = 2
scaled_vector = scalar * vector_2d
transformed_scaled = square_transform(scaled_vector)

print(f"\nScaled vector: {scaled_vector}")
print(f"Transformed scaled vector: {transformed_scaled}")
print(f"Scalar * Transformed original: {scalar * transformed_2d}")
