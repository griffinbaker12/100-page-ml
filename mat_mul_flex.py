import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])

# b is treated as column vector
r1 = A @ B
print(f"r1: {r1}")
