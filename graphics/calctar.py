import numpy as np
import matplotlib.pyplot as plt


def f(y):
    return y - y ** 2 + 2


yDat = np.arange(-1, 2, 0.0001)
yPl = range(-5, -5, 1)

plt.plot([f(i) for i in yDat], yDat, 'orangered', linewidth=2.0, label='f(y) en el intervalo [-1, 2]')
plt.fill([f(i) for i in yDat], yDat, label='Área bajo la curva', color='green', alpha=0.5)

plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-1, 3)
plt.ylim(-3, 3)

# Datos del gráfico
plt.title("Área bajo la curva de la función (a)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
# plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/Calc. Integral/hw/funcionA.png")

# Mostrarlo.
plt.show()
