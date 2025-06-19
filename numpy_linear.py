import numpy as np

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

weights = np.array([0.1, 0.2, 0.3])

bias = 0.5
# y=X⋅w+b
y_pred = np.dot(X, weights) + bias

print(y_pred)
