import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 2, 0.0001)
y = (4 - x**2)**(1/2)


plt.plot(x, y, 'orangered', linewidth=2.0, label='f(x)', alpha=.5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limitar los valores de los ejes.
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Datos del gráfico
plt.title("Gráfico de la función")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Ajustes del gráfico
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Guardar gráfico como imágen PNG.
plt.savefig("/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/"
            "Calculus/Calc. Integral/hw/caltare12.png")

# Mostrarlo.
plt.show()
