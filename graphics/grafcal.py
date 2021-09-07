import matplotlib.pyplot as plt
import numpy as np

# Data
xData = np.array([0, 1, 2, 5, 7])
yData = np.array([5, 7, 9, 15, 19])

# Plot data
plt.plot(xData, yData, 'bo', label='Datos')
plt.title('Gráfica de los puntos')
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.grid()
plt.legend()
plt.show()
