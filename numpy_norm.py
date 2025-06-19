import numpy as np

data = np.array([
    [10, 200, 0.5],
    [15, 180, 0.7],
    [12, 210, 0.6],
    [14, 190, 0.8],
    [13, 205, 0.55]
])

X = data[:, :-1]
y = data[:, -1]

X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_norm = (X - X_min) / (X_max - X_min)

y = y.reshape(-1, 1)

print("Normalized features:\n", X_norm)
print("Labels:\n", y)
