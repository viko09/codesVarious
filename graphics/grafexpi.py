import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, m, b):
    return m*x + b


# Data
xData = np.array([0.95, 1.64, 2.67, 3.61, 4.49, 6.36, 7.25, 8.24, 9.62, 15])**-1
yData = np.array([5.26, 3.05, 1.87, 1.39, 1.11, 0.786, 0.69, 0.603, 0.52, 0.333])

# Plot data
plt.plot(xData, yData, 'bo', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(0.0666, 1.05, 0.01)


plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste: 4.998x - 2.211')
plt.title('Gráfica: Área vs Resistencia')
plt.ylabel('Resistencia (Ωcm²)')
plt.xlabel('Área (cm²)')
plt.grid()
plt.legend()
plt.show()