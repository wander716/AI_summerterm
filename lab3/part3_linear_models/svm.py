import numpy as np
import scipy

def svm(X, y):
    '''
    SVM Support vector machine.

    INPUT:  X: training sample features, P-by-N matrix.
            y: training sample labels, 1-by-N row vector.

    OUTPUT: w: learned perceptron parameters, (P+1)-by-1 column vector.
            num: number of support vectors

    '''
    P, N = X.shape
    w = np.zeros((P + 1, 1))

    # YOUR CODE HERE
    # Please implement SVM with scipy.optimize. You should be able to implement
    # it within 20 lines of code. The optimization should converge wtih any method
    # that support constrain.
    #TODO
    # begin answer
    # end answer
    C = 1
    X = np.vstack((np.ones((1, N)), X))  # 变成 (P+1)-by-N

    def unpack(theta):
        w = theta[:P+1].reshape(P+1, 1)
        z = theta[P+1:P+1+N]
        return w, z
    
    def objective(theta):
        w, z = unpack(theta)
        return (1/2) * np.sum(w[1:]**2) + C * np.sum(z)
    
    constraints = []

    for i in range(N):
        def cons_margin(theta, i=i):
            w, z = unpack(theta)
            return y[0, i] * (w.T @ X[:, i]) - 1 + z[i]
        constraints.append({
            'type': 'ineq',
            'fun': cons_margin
        })
        
        def cons_slack(theta, i=i):
            w, z = unpack(theta)
            return z[i]
        constraints.append({
            'type': 'ineq',
            'fun': cons_slack
        })

    theta0 = np.zeros(P + 1 + N)
    result = scipy.optimize.minimize(
        objective, 
        theta0, 
        constraints=constraints, 
        method='SLSQP'
    )

    w, z = unpack(result.x)

    margin = y * (w.T @ X)
    sv = np.where(margin <= 1 + 1e-5)
    num = len(sv[0])

    return w, num

