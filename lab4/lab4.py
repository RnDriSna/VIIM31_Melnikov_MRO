import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, lr=1, epochs=100):
        self.W = np.zeros(input_size+1)
        self.epochs = epochs
        self.lr = lr
    
    def activation_fn(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a
    
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)

def generate_random_data():
    X = np.random.rand(100, 2)
    d = np.zeros(100)
    for i in range(100):
        if X[i][0] + X[i][1] > 1:
            d[i] = 1
    return X, d

def plot_points(X, d, perceptron):
    for i in range(X.shape[0]):
        if d[i] == 1:
            plt.scatter(X[i][0], X[i][1], color='r')
        else:
            plt.scatter(X[i][0], X[i][1], color='b')
    plt.xlim(0, 1.5)
    plt.ylim(0, 1.5)
    
    w = perceptron.W
    x = np.linspace(0, 1, 100)
    y = -(w[0] + w[1]*x) / w[2]
    plt.plot(x, y, '-g')
    
    plt.show()

X, d = generate_random_data()
perceptron = Perceptron(input_size=2)
perceptron.fit(X, d)

plot_points(X, d, perceptron)
