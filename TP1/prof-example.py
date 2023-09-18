import math
import matplotlib.pyplot as plt
import numpy as np

a = -4
b = 4
n = 5
X = np.linspace(a, b, n)

Y = np.sin(X)

V = np.vander(X, increasing=True)
A = np.linalg.solve(V, Y)


def pol_interp(A, x):
    S = 0
    for k in range(n):
        S += A[k] * x ** k
    return S
'''  '''
