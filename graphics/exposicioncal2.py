import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0000000001, 10, 0.000001)
y = (1 / x**3)
yy = -1/(2*x**2)

plt.plot(x, y, 'orangered', linewidth=2.0, label='f(x)')
plt.plot(x, yy, 'blue', linewidth=2.0, label='F(x)')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-1, 10)
plt.ylim(-20, 20)

# Datos del gráfico
plt.title("Función f(x) con su primitiva F(x)")
plt.xlabel("X")
plt.ylabel("Y")

# Ajustes del gráfico
plt.grid(color='b', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/"
            "Calc. Integral/hw/expo/dosfunciones.png")

# Mostrarlo.
plt.show()
