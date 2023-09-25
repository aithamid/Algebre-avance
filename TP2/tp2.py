import math
import matplotlib.pyplot as plt
import numpy as np

# Paramètre 
a = -4
b = 4
n = 8
'''en sortie [-4 -2 0 2 4 ]'''
#On recupère les valeurs x 
X = np.linspace(a, b, n)

#autre fonction de test (1/(1+10*x**2))
#def test(x):
#    return (1/(1+10*x**2))

#On recupère les resultat de sin(x)
'''Fonction de test sin''' 

# Y = np.sin(X)
def test(x):
    return (1/(1+10*x**2))


Y = test(X)

#TP2
#Question 1

def lag(k,x):
    res=1
    for i in range(len(X)):
        if(i!=k):
            res*=(x-X[i])/(X[k]-X[i])
    return res

def Lagrange(x):
    s=0
    for k in range(len(X)):
        s+=Y[k]*lag(k,x)
    return s

Xaff = np.linspace(a, b, 2000)
Yexa = test(Xaff)
Yestim = []

for k in range(2000):
    Yestim.append(Lagrange(Xaff[k]))
    # y_k = P(X_k)

# Partie pour connaître l'erreur
E = np.abs(Yexa - Yestim)
Erreur = np.max(E)
print(Erreur)


plt.plot(Xaff, Yexa, label='Fonction réelle')
plt.plot(Xaff, Yestim, label='Polynôme interpolateur')
plt.legend()  # Ajoute une légende
plt.title("Interpolation polynomiale base Lagrange de la fonction sin(x), pour n="+str(n))
plt.xlabel('x')
plt.ylabel('y')
plt.show()