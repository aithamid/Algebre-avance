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


# Exemple d'utilisation avec vos données et une liste de valeurs x
X = [-5, -2, 0, 3, 6]
Y = [-4, -1, 1, 1, -1]
V = [3, 0, 3, -2, 0]

X_aff=np.linspace(-5,6,1000)
Y_aff=[foncHermite(X,Y,V,x)for x in X_aff]

# 5) Tracer les tangentes
for i in range(0, len(X)):
    xi = X[i] -1
    yi = Y[i] - V[i]

    xf = X[i] +1
    yf = Y[i] + V[i]
   
    plt.plot((xi,xf), (yi,yf))

plt.plot(X_aff,Y_aff,label='Interpolations P(x)', color='blue')

# Affichez le graphique.
plt.show()


