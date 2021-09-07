import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a):
    return a * (1/x)


f = 23.5
# Data
xData = np.array([35.25 - f, 41.125 - f, 47 - f, 70.5 - f, 94 - f,
                  117.5 - f, 141 - f, 164.5 - f, 188 - f,
                  211.5 - f, 235 - f])
yData = np.array([166 - f, 116.5 - f, 53 - f, 48 - f, 46 - f, 36 - f,
                  31.25 - f, 32.8 - f, 29.5 - f, 26 - f, 24 - f])

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)
print(pcov)

# Values for the fitted fun
xFit = np.arange(10.8, 212.0, 0.01)

plt.plot(xData, yData, 'bo', label='Datos')
plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste')

plt.title('Ajuste de datos experimentales')
plt.xlabel('Sob')
plt.ylabel('Sim')
plt.grid()
plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/tareaajuste.png")
plt.show()
