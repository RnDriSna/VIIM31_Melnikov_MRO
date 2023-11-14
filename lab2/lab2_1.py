import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def ho_kashyap(X, y, alpha=0.1, max_iter=1000):
    X = np.hstack([X, np.ones((X.shape[0], 1))])

    w = np.zeros(X.shape[1])
    b = 0

    for i in range(max_iter):
        z = np.dot(X, w) + b
        e = y - np.sign(z)
        w += alpha * np.dot(X.T, e)
        b += alpha * np.sum(e)

        if np.all(np.abs(e) < 1e-6):
            break

    return w, b

X, y = make_blobs(n_samples=100, centers=2, random_state=42)

w, b = ho_kashyap(X, y)

print("Weight vector:", w)
print("Bias term:", b)

plt.scatter(X[:, 0], X[:, 1], c=y)
x1 = np.linspace(-10, 10, 100)
x2 = -(w[0] * x1 + b) / w[1]
plt.plot(x1, x2)
plt.show()
