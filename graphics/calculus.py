import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


# Data
xData = np.array([-3, -1, 0.5, 1, 3, 4, 5])
yData = np.array([-51, -11, -9.875, -11, -3, 19, 61])

# Plot data
plt.plot(xData, yData, 'go', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(-3.0, 5.0, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste: x³ - 2x² - x - 9')
plt.title('Ajuste con los puntos encontrados añadidos')
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.grid()
plt.legend()
plt.show()
