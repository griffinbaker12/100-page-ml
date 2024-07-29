import numpy as np


def sig(x):
    return 1 / (1 + np.exp(-x))


I = np.array(
    [
        0.5,
        0.3,
        0.1,
    ]
)
X = np.array(
    [
        [0.1, 0.1, 0.1],
        [0.2, 0.2, 0.2],
    ]
)
A = np.dot(X, I)
O = sig(A)
print(A, O)
