import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b, c):
    return a * x ** 2 + b * x + c


# Data
xIncidente = np.array([3, 8, 15.3, 19, 27, 33.25, 38, 45.5, 49, 58.5, 65])
yEmergente = np.array([62, 52, 44, 40, 32, 26, 20.5, 16, 12, 5, 1])
yDiedro = np.array([21, 19, 16.5, 16, 16, 17, 16, 18, 17, 20.5, 23])


# Plot data 1
plt.plot(xIncidente, yEmergente, 'go', label='Emergente')
# Plot data 2
plt.plot(xIncidente, yDiedro, 'bo', label='Diedro')

# Curve 1
popt1, pcov1 = curve_fit(fun, xIncidente, yEmergente)
print(popt1)

# Curve 2
popt2, pcov2 = curve_fit(fun, xIncidente, yDiedro)
print(popt2)


# Values for the fitted function
xFit = np.arange(3.0, 65.0, 0.01)

plt.plot(xFit, fun(xFit, *popt1), 'orangered', label='Ajuste: Ángulo Emergente')
plt.plot(xFit, fun(xFit, *popt2), 'purple', label='Ajuste: Ángulo Diedro')
plt.xlim(-5, 70)
plt.ylim(-5, 65)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title('Prisma Óptico')
plt.xlabel('Ángulo de incidencia (i)')
plt.ylabel('Ángulo emergete (e) y diedro (δ)')
plt.grid()
plt.legend()
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/FEXPIII/prismaoptix.png', dpi=300)
plt.show()
