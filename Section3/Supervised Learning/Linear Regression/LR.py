import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]
theta_min = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_min)
lin_reg_algo = LinearRegression()
lin_reg_algo.fit(X, y)
y_estimate = lin_reg_algo.predict(X_new)
plt.plot(X_new, y_predict, "b-", label="Hypothesis func")
plt.plot(X, y, "r.", label="target varibles")
plt.scatter(X_new, y_estimate, s=50, alpha=0.7, label="Estimated values", marker="X", c="g")
plt.legend()
plt.show() 
print(y_predict)