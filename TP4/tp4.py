import math
import numpy as np
import matplotlib.pyplot as plt

def binom(n, p):
    """Calcule le coefficient binomial C(n, p)"""
    return math.factorial(n) // (math.factorial(p) * math.factorial(n - p))

def bernstein(n, i, t):
    """Calcule le coefficient de Bernstein B_n,i(t)"""
    return binom(n, i) * (t ** i) * ((1 - t) ** (n - i))

def bezier(control_points, n_points=1000):
    """Calcule les points de la courbe de Bézier"""
    n = len(control_points) - 1
    curve_points = []
    for t in np.linspace(0, 1, n_points):
        x, y = 0, 0
        for i in range(n + 1):
            x += bernstein(n, i, t) * control_points[i][0]
            y += bernstein(n, i, t) * control_points[i][1]
        curve_points.append((x, y))
    return curve_points

def affichage(control_points, curve_points):
    # Affichage des points de contrôle
    control_x, control_y = zip(*control_points)

    # Affichage de la courbe de Bézier
    curve_x, curve_y = zip(*curve_points)

    # Tracer les points de contrôle et la courbe de Bézier
    plt.scatter(control_x, control_y, color='red', label='Points de contrôle')
    plt.plot(curve_x, curve_y, color='blue', label='Courbe de Bézier')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Points de contrôle
control_points = [(0, 0), (1, 3), (2, 3), (3, 0)]
curve_points = bezier(control_points)
affichage(control_points, curve_points)


