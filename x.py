import numpy as np

# Generate some random feature values
X = np.random.rand(100, 5)

# Generate some random weights
theta = np.random.rand(6)

# Add a column of ones to X for the bias term
X = np.hstack((np.ones((100, 1)), X))

# Calculate the predicted values using the linear combination of the feature values and weights
y_pred = np.dot(X, theta)

# Print the predicted values
print(y_pred)
