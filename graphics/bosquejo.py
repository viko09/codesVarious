import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.09375*(4 - x**2)


xDat = np.arange(-2, 2, 0.0001)

xOt = np.arange(-3, -2.00001, 0.0001)
y = 0*xOt
xOt1 = np.arange(2.00001, 3, 0.0001)
y1 = 0*xOt1

plt.plot(xDat, [f(i) for i in xDat], 'orangered', linewidth=2.0, label='f(x) cuando -2 ≤ x ≤ 2')
plt.plot(xOt, y, 'cyan', linewidth=3.0, label='f(x) de lo contrario')
plt.plot(xOt1, y1, 'cyan', linewidth=3.0)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-3, 3)
plt.ylim(-1, 1)

# Datos del gráfico
plt.title("Gráfica de f(x)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/PYE/imagenes/graf3.png")

# Mostrarlo.
plt.show()

