import math
import numpy as np
import matplotlib.pyplot as plt

def phi0(t):
    if 0<=t<=1:
        return (1-t)**2*(2*t+1)
    else:
        return 0

def phi1(t):
    if 0<=t<=1:
        return t**2*(3-2*t)
    else:
        return 0

def phi2(t):
    if 0<=t<=1:
        return t*(1-t)**2
    else:
        return 0

def phi3(t):
    if 0<=t<=1:
        return t**2*(t-1)
    else:
        return 0


def foncHermite(X,Y,V,x):
    n = len(X)-1
    result = 0.0
    for i in range(n):
        # Calcul des termes de la base d'Hermite
       d=X[i+1]-X[i]
       t=(x-X[i])/d
       result+=Y[i]*phi0(t)+Y[i+1]*phi1(t)+d*(V[i]*phi2(t)+V[i+1]*phi3(t))
    return result


def find_B(Y, d):
    n = len(Y)
    B = [(3/d) * (Y[i+1] - Y[i-1]) for i in range(1, n-1)]
    B = [(3/d) * (Y[1] - Y[0])] + B + [(3/d) * (Y[-1] - Y[-2])]
    return B

def find_S(n):
    S = np.zeros((n, n))
    np.fill_diagonal(S, 4)
    S[0, 0] = S[-1, -1] = 2
    np.fill_diagonal(S[1:], 1)
    np.fill_diagonal(S[:, 1:], 1)
    return S

def solve(S, B):
    return np.linalg.solve(S, B)

X = [7, 0, -8, -8, 0, 7]
Y = [0, 4, -3, 3, -4, 0]
T = [0, 1, 2, 3, 4, 5]

n = len(X) - 1

d = T[1] - T[0]
S = find_S(len(Y))
print(S)

Vx = solve(S, find_B(X, d))
Vy = solve(S, find_B(Y, d))

t_vals = np.linspace(min(T), max(T), 1000)

X_spline = [foncHermite(T, X, Vx, t) for t in t_vals]
Y_spline = [foncHermite(T, Y, Vy, t) for t in t_vals]

plt.plot(X_spline, Y_spline, label='Courbe Splinée')
plt.scatter(X, Y, c='red', label='Points de contrôle')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Splines Cubiques Naturelles')
plt.grid()
plt.show()
