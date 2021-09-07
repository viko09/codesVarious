import matplotlib.pyplot as plt
import numpy as np

# Function
# def fun(x, a, b, c, d):
#    return a*x**3 + b*x**2 + c*x + d

# Data
xData = np.array([0, 0.2588, 0.5, 0.7071, 0.8660, 0.9659, 1])
yData = np.array([0, 0.1993, 0.3842, 0.5446, 0.6665, 0.7431, 0.7693])

# Plot data
plt.plot(xData, yData, 'orangered')
plt.plot(xData, yData, 'bo', label='Datos')
plt.title('Refracción para el agua')
plt.xlabel('Sen θi')
plt.ylabel('Sen θt')
plt.grid()
plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/funcionagua.png")
plt.show()
