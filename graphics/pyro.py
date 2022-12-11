import matplotlib.pyplot as plt
import numpy as np


# Function
def fun(x, a, b):
    return a*x + b


# Data
xData = np.array([0, 2])
yData = np.array([280, 256])


# Plot data
plt.plot(xData, yData, 'orangered')
plt.plot(xData, yData, 'bo', label='Datos')
plt.title('Linea')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
# plt.savefig("/home/vikoluna/Documents/BUAP/funcionagua.png")
plt.show()
