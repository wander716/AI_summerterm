import numpy as np

def linear_regression(X, y):
    '''
    LINEAR_REGRESSION Linear Regression.

    INPUT:  X: training sample features, P-by-N matrix.
            y: training sample labels, 1-by-N row vector.

    OUTPUT: w: learned perceptron parameters, (P+1)-by-1 column vector.
    '''
    P, N = X.shape
    w = np.zeros((P + 1, 1))
    # YOUR CODE HERE
    # begin answer
    X = np.vstack((np.ones((1, N)), X))  # 变成 (P+1)-by-N
    y = np.array(y).reshape(1, -1)

    w = np.linalg.pinv(X @ X.T) @ X @ y.T

    # end answer
    return w

