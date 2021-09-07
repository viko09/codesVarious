import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b, c):
    return a * x ** 2 + b * x + c


# Data
yData = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
xData = np.array([10, 17.9, 22.5, 26.5, 30.5, 34, 37, 40.5, 43, 46])

# Plot data
plt.plot(xData, yData, 'bo', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(0.0, 46.0, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste')
plt.title('Espesor de la capa de aire como función del radio')
plt.xlabel('y_m')
plt.ylabel('t_m')
plt.grid()
plt.legend()
plt.show()
