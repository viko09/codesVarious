import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Function
def fun(x, m, b):
    return m*x + b


x_1 = np.array([1.885618083, 21.08185107])
y = np.array([1, 3])

yDat = np.arange(-10, 20, 0.001)
xDat = (2/3)*(yDat**2 + 1)**(3/2)

# Curve
popt, pcov = curve_fit(fun, x_1, y)
print(popt)
print(pcov)

# Values for the fitted fun
xFit = np.arange(1.885618083, 21.08185107, 0.01)

plt.plot(xDat, yDat, 'orangered', linewidth=2.0, label='Función')
plt.plot(x_1, y, 'bo', linewidth=2.0, label='Puntos')
plt.plot(xFit, fun(xFit, *popt), 'green',
         label='Longitud', alpha=0.7)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-1, 24)
plt.ylim(0, 3.5)

# Datos del gráfico
plt.title("Longitud de la función g(y)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/"
            "Calc. Integral/hw/tar12_pt.png")

# Mostrarlo.
plt.show()
