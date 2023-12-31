import numpy as np
import matplotlib.pyplot as plt

def ho_kashyap(X, y, alpha=0.1, max_iter=10000):
    # Add bias term to input data
    X = np.hstack([X, np.ones((X.shape[0], 1))])

    # Initialize weights and bias
    w = np.zeros(X.shape[1])
    b = 0

    # Run the Ho-Kashyap algorithm
    for i in range(max_iter):
        z = np.dot(X, w) + b
        e = y - np.sign(z)
        w += alpha * np.dot(X.T, e)
        b += alpha * np.sum(e)

        # Check for convergence
        if np.all(np.abs(e) < 1e-6):
            break

    # Return the weight vector and bias term
    return w, b

# Generate random input data
n_samples = 10
n_features = 5
X = np.random.rand(n_samples, n_features) * 10 - 5
y = np.random.choice([-1, 1], size=n_samples)

# Run the Ho-Kashyap algorithm
w, b = ho_kashyap(X, y)

# Print the weight vector and bias term
print("Weight vector:", w)
print("Bias term:", b)

# Plot the data and decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
x1 = np.linspace(-5, 5, 100)
x2 = -(w[0] * x1 + b) / w[1]
plt.plot(x1, x2)
plt.show()
