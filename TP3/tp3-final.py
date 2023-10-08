import math
from copy import deepcopy

import numpy as np
from matplotlib import pyplot as plt


# X = [-1, 1, 3, 5]
# Y = [7, 3, 31, 235]

def f(X):
    Y = np.sin(X)
    return Y


a = 0
b = 2 * math.pi
n = 100
n_x = 5
X = np.linspace(a, b, n_x)
Y = f(X)



def diffdivi(X,Y):
    Y_calc = deepcopy(Y)
    for k in range(len(X) - 1):
        for i in range(k + 1, len(X)):
            Y_calc[i] = (Y_calc[i] - Y_calc[k]) / (X[i] - X[k])
    return Y_calc


coeff = diffdivi(X,Y)
print(coeff)


def PolNewton(x):
    # P(x) = f + Y_calc[i]*N[i](x)+ ...
    Somme = coeff[0]
    N = 1
    for k in range(1, len(X)):
        N = N * (x - X[k - 1])
        Somme = Somme + (coeff[k] * N)
    return Somme


X_aff = np.linspace(a, b, n)
Y_aff = f(X_aff)
Y_estim = PolNewton(X_aff)

def Ajout_un_point(xaj, yaj):
    global X, Y, coeff
    X = np.append(X, xaj)
    Y = np.append(Y, yaj)
    coeff = diffdivi(X, Y)

Ajout_un_point(1, np.sin(1))

new_Y = PolNewton(X_aff)

plt.plot(X_aff, Y_aff, "r", label='Y_exact : Fonction réelle')
plt.plot(X_aff, Y_estim, "b", label='Y_estim : Polynôme interpolateur')
plt.plot(X_aff, new_Y, 'g--', label='new_Y : Polynôme après ajout du point A')
plt.plot(1, np.sin(1), marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black", label='Point A : (1,sin(1))')
plt.legend(loc='lower left', framealpha=1, frameon=True)  # Ajoute une légende
plt.title("Interpolation polynomiale base Newton de la fonction sin(x), pour n=" + str(n_x))
plt.xlabel('x')
plt.ylabel('y')
plt.show()
