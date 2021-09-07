import numpy as np
import matplotlib.pyplot as plt

y = np.arange(-2, 2, 0.0001)
x = np.sqrt((4 - y))

# create plot of values
plt.plot(x, y, 'orangered', linewidth=2.0, label='f(y) en el intervalo [-2, 2]')

# fill in area between the two lines
plt.fill_betweenx(y, x, color='cadetblue', label='Área bajo la curva', alpha=.5)


plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-1, 3)
plt.ylim(-3, 3)

# Datos del gráfico
plt.title("Área bajo la curva de la función (c)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Calculus/Calc. Integral/hw/funcionC.png")

# Mostrarlo.
plt.show()
