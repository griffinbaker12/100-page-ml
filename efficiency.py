import time

import numpy as np


def linear_operation(X, W):
    return np.dot(X, W)


def non_linear_operation(X):
    return np.sin(X) + np.sqrt(np.abs(X))


# Setup
n = 1000
X = np.random.rand(n, n)
W = np.random.rand(n, n)

# Benchmark linear operation
start_time = time.time()
for _ in range(100):
    linear_operation(X, W)
linear_time = time.time() - start_time

# Benchmark non-linear operation
start_time = time.time()
for _ in range(100):
    non_linear_operation(X)
non_linear_time = time.time() - start_time

print(f"Linear operation time: {linear_time:.4f} seconds")
print(f"Non-linear operation time: {non_linear_time:.4f} seconds")
print(f"Speed-up factor: {non_linear_time / linear_time:.2f}x")
