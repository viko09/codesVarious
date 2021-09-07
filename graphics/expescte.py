import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b):
    return a*x + b


# Data
xData = np.array([100, 130.1, 161.0, 191.6, 220.9, 252.4, 281.7, 312.6, 340.3, 379.2])
yData = np.array([0.89, 1.15, 1.43, 1.70, 1.96, 2.24, 2.49, 2.77, 3.01, 3.36])

# Plot data
plt.plot(xData, yData, 'bo', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(100.0, 379.2, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'red', label='Ajuste')
plt.title('Capacitancia bajo separación constante (10mm)')
plt.xlabel('Área (mm²)')
plt.ylabel('Capacitancia (F)x10⁻¹³')
plt.grid()
plt.legend()
plt.show()
