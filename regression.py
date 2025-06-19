import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 2 * np.random.rand(100, 1)
true_slope = 3.5
true_intercept = 1.2
noise = np.random.randn(100, 1)
y = true_slope * X + true_intercept + noise

X_b = np.c_[np.ones((100, 1)), X]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

plt.scatter(X, y, color="blue", label="Training data")
plt.plot(X_new, y_predict, color="red", linewidth=2, label="Prediction")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression")
plt.show()

predictions = X_b.dot(theta_best)
mse = np.mean((predictions - y) ** 2)
print("Learned parameters:", theta_best.ravel())
print("Mean Squared Error:", mse)
