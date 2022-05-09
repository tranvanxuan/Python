import numpy as np


# file: functions.py
def predict(X, Theta):
    return X @ Theta


# function computeCost
def computeCost(X, y, Theta):
    predicted = predict(X,Theta)
    sqr_error = (predicted - y)**2
    sum_error = np.sum(sqr_error)
    m = np.size(y)
    J = (1/(2*m))*sum_error
    return J
# function computeCost_Vec


def computeCost_Vec(X, y, Theta):
    error = predict(X, Theta) - y
    m = np.size(y)
    J = (1/(2*m))*np.transpose(error)@error
    return J
