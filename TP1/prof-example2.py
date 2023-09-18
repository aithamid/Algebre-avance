import math
import matplotlib.pyplot as plt
import numpy as np

a = -4
b = 4
n = 29
X = np.linspace(a, b, n)
def test(x):
    return (1/(1+10*x**2))


Y = test(X)

V = np.vander(X, increasing=True)
A = np.linalg.solve(V, Y)


def pol_interp(A, x):
    S = 0
    for k in range(n):
        S += A[k] * x ** k
    return S
''' '''


Xaff = np.linspace(a,b,1000)
Yexa = test(Xaff)
Yestim = []
for k in range(1000):
    Yestim.append(pol_interp(A, Xaff[k]))
    #y_k = P(X_k)

#Affichage des 2 courbes, couleurs etc.
E = np.abs(Yexa-Yestim)
Erreur = np.max(E)
print(Erreur)
#pour n=7, erreur vaut 0.08293762292804946
plt.plot(Xaff, Yexa)
plt.plot(Xaff, Yestim)
plt.xlim((a,b))
plt.ylim((-2,2))
plt.show()