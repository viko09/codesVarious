import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b, c):
    return a * x ** 2 + b * x + c


# Data
xData = np.array([5, 5.3, 5.5, 6.0, 6.5, 7.1, 7.6, 8.1, 9.5, 10])
yData = np.array([1.77, 1.66, 1.61, 1.47, 1.35, 1.26, 1.17, 1.09, 0.93, 0.89])



# Plot data
plt.plot(xData, yData, 'go', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(5.0, 10.0, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste')
plt.title('Capacitancia bajo area constante (100mm²)')
plt.xlabel('Separación (mm)')
plt.ylabel('Capacitancia (F)x10⁻¹³')
plt.grid()
plt.legend()
plt.show()
