import numpy as np
import matplotlib.pyplot as plt


def x1(y1):
    return y1/25


y1 = np.arange(0, 4.99999, 0.0001)


def x2(y2):
    return (2/5) - (y2*(1/25))


y2 = np.arange(5, 10, 0.0001)


y3 = np.arange(-3, 0, 0.0001)
x3 = 0*y3
y4 = np.arange(10.00001, 13, 0.0001)
x4 = 0*y4

plt.plot(x1(y1), y1, 'orangered', linewidth=2.0, label='f(y) para 0 ≤ y < 5')
plt.plot(x2(y2), y2, 'purple', linewidth=2.0, label='f(y) para 5 ≤ y ≤ 10')

plt.plot(x3, y3, 'cyan', linewidth=3.0, label='f(y) para y < 0 o y > 10')
plt.plot(x4, y4, 'cyan', linewidth=3.0)
# Limitar los valores de los ejes.
plt.xlim(-0.5, 0.75)
plt.ylim(-3, 12)

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
plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/PYE/imagenes/grafica8.png")

# Mostrarlo.
plt.show()
