import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic(X, y):
    '''
    LR Logistic Regression.

    INPUT:  X: training sample features, P-by-N matrix.
            y: training sample labels, 1-by-N row vector.

    OUTPUT: w: learned parameters, (P+1)-by-1 column vector.
    '''
    P, N = X.shape
    w = np.zeros((P + 1, 1))
    # YOUR CODE HERE
    X = np.vstack((np.ones((1, N)), X))  # 变成 (P+1)-by-N
    
    y = y.reshape(1, N)
    grad = np.ones(w.shape)
    alpha = 0.01

    for _ in range(10000):
        z = w.T @ X # 1-by-N
        f = sigmoid(z)

        grad = (1/N) * (X @ (f - y).T)

        w -= alpha * grad
        
        if np.linalg.norm(grad) < 1e-6:
            break

    return w
