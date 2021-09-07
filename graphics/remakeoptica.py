import matplotlib.pyplot as plt
import numpy as np

# Data
xData = np.array([35.25, 41.125, 47, 70.5, 94, 117.5, 141, 164.5, 188, 211.5, 235])
yData = np.array([166, 116.5, 53, 48, 46, 36, 31.25, 32.8, 29.5, 26, 23])

# Plot data
plt.plot(xData, yData, 'bo', label='Datos')

plt.title('Datos experimentales')
plt.xlabel('Sob')
plt.ylabel('Sim')
plt.grid()
plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/tarea2opt.png")
plt.show()
