import numpy as np
import matplotlib.pyplot as plt


def f(y1):
    return y1*(1/25)


yDat = np.arange(0, 4.99999, 0.0001)


def f(y2):
    return (2/5) - (y2*(1/25))


yDat2 = np.arange(5, 10, 0.0001)


xOt = np.arange(-3, -2.00001, 0.0001)
y = 0*xOt

xOt1 = np.arange(2.00001, 3, 0.0001)
y1 = 0*xOt1

plt.plot([f(i) for i in yDat], yDat, 'orangered', linewidth=2.0, label='f(y)')
plt.plot([f(i) for i in yDat2], yDat2, 'purple', linewidth=2.0, label='f(y)')
# plt.fill([f(i) for i in yDat], yDat, label='Área bajo la curva', color='green', alpha=0.5)

plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Datos del gráfico
plt.title("Gráfica de la función f(y)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
# plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/Calc. Integral/hw/funcionA.png")

# Mostrarlo.
plt.show()
