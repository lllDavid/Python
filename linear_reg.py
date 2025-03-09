from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

data = load_diabetes()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

lr_model = LinearRegression()
ridge_model = Ridge(alpha=1.0)
lasso_model = Lasso(alpha=0.1)

lr_model.fit(X_train_poly, y_train)
ridge_model.fit(X_train_poly, y_train)
lasso_model.fit(X_train_poly, y_train)

y_pred_lr = lr_model.predict(X_test_poly)
y_pred_ridge = ridge_model.predict(X_test_poly)
y_pred_lasso = lasso_model.predict(X_test_poly)

mse_lr = mean_squared_error(y_test, y_pred_lr)
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)

print(f'Mean Squared Error of Linear Regression: {mse_lr:.2f}')
print(f'Mean Squared Error of Ridge Regression: {mse_ridge:.2f}')
print(f'Mean Squared Error of Lasso Regression: {mse_lasso:.2f}')

cv_score_lr = cross_val_score(lr_model, X_train_poly, y_train, cv=5, scoring='neg_mean_squared_error').mean()

models = ['Linear Regression', 'Ridge Regression', 'Lasso Regression']
mse_values = [mse_lr, mse_ridge, mse_lasso]

plt.bar(models, mse_values, color=['blue', 'green', 'red'])
plt.xlabel('Model')
plt.ylabel('Mean Squared Error')
plt.title('Comparison of Model Performances')
plt.show()

print(f'Cross-Validation Mean Squared Error for Linear Regression: {-cv_score_lr:.2f}')
