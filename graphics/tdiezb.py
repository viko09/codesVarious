import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.0001)
y = np.sin(x * np.pi)
y2 = 2*x
print(x[5000])

plt.plot(x, y, 'orangered', linewidth=2.0, label='f(x) en el intervalo [0, 1]')
plt.plot(x, y2, 'blue', linewidth=2.0, label='g(x) en el intervalo [0, 1]')
plt.fill_between(x, y2, y, where=x < 0.5, color='red', label='Área bajo la curva', alpha=.5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Datos del gráfico
plt.title("Área bajo la curva de las funciones")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/Calc. Integral/hw/funcion14.png")

# Mostrarlo.
plt.show()
