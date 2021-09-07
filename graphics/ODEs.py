import matplotlib.pyplot as plt
import numpy as np

# El paquete odeint permite resolver ecuaciones diferenciales del tipo
# dy/dt = f(y,t) con condiciones iniciales y(0) = y_0

from scipy.integrate import odeint


# La función del sistema recibe como primer argumento argumento el instante (un escalar).

# Se integrará la función y' + y = 0
# f(y, t) = dy/dt = -y con condicion inicial y(0) = 1


def f(y, t):
    return -y


# Condicion inicial

y0 = 1

# Vector de tiempo donde se realiza la integración

t = np.linspace(0, 5)

# integramos y representamos la solución

sol = odeint(f, y0, t)

# Solucion aproximada con '+'

plt.plot(t, sol, '+', color='y')

# Solución exacta de color azul
yt = np.e ** (-t)
plt.plot(t, yt, color='b')
plt.grid()

plt.show()
