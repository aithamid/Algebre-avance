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

B=[]
def Spline():
    n = len(X)-1
    B[0]=(3/d)*(Y[1]-Y[0])
    for i in range(n):
        if i>0:
            d=X[i+1]-X[i]
            B[i]=(3/d)*(Y[i+1]-Y[i-1])

    for i in range(n):
        


X=[7,0,-8,-8,0,7]  
Y=[0,4,-3,3,-4,0]
T=[0,1,2,3,4,5]  

