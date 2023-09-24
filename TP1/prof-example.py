import math
import matplotlib.pyplot as plt
import numpy as np

# Paramètre 
a = -4
b = 4
n = 70
'''en sortie [-4 -2 0 2 4 ]'''
#On recupère les valeurs x 
X = np.linspace(a, b, n)

#autre fonction de test (1/(1+10*x**2))
#def test(x):
#    return (1/(1+10*x**2))

#On recupère les resultat de sin(x)
'''Fonction de test sin''' 

Y = np.sin(X)

#autre fonction de test 
#Y = test(X)



#Fabrique le matrice
'''Notre grille (X,Y), permet de fabriquer notre polynôme'''
''' Création de V matrice de vandermonde, mode increasing '''
V = np.vander(X, increasing=True)

''' Résolution puis récupération de la matrice des coeff puissances croissantes '''
A = np.linalg.solve(V, Y)

''' Nous avons tout pour écrire notre polynôme '''
''' ecrire le polynome d'interpol '''
def pol_interp(A, x):
    S = 0
    for k in range(n):
        S += A[k] * x ** k
    return S


''' print(len(A)) '''
''' A est de longueur 5 car le pol est de degré 4: a+bx+cx²+dx^3+ex^4 '''
''' A contient [a,b,c,d,e] '''
Xaff = np.linspace(a, b, 1000)
Yexa = np.sin(Xaff)
#autre fonction de test Yexa = test(Xaff)
Yestim = []
for k in range(1000):
    Yestim.append(pol_interp(A, Xaff[k]))
    # y_k = P(X_k)

# Partie pour connaître l'erreur
E = np.abs(Yexa - Yestim)
Erreur = np.max(E)
print(Erreur)


# Affichage des 2 courbes, couleurs etc.
# pour n=7, erreur vaut 0.08293762292804946

plt.plot(Xaff, Yexa, label='Fonction réelle')
plt.plot(Xaff, Yestim, label='Polynôme interpolateur')
plt.legend()  # Ajoute une légende
plt.title("Interpolation polynomiale de la fonction sin(x), pour n="+str(n))
plt.xlabel('x')
plt.ylabel('y')
#autre fonction plt.xlim((a,b))
#plt.ylim((-2,2))
plt.show()
