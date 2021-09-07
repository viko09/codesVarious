import numpy as np
import matplotlib.pyplot as plt


def f(yb):
    return yb - (1/4)*(yb**2)


yDat = np.arange(0, 4, 0.0001)

plt.plot([f(i) for i in yDat], yDat, 'orangered', linewidth=2.0, label='f(y) en el intervalo [0, 4]')
plt.fill([f(i) for i in yDat], yDat, 'cadetblue', label='Área bajo la curva')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-2, 4)
plt.ylim(-2, 6)

# Datos del gráfico
plt.title("Área bajo la curva de la función (b)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/Calc. Integral/hw/funcionB.png")

# Mostrarlo.
plt.show()
