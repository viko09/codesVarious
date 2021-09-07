import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x_1, m, b):
    return m*x_1 + b


f = 23.5
# Data
x = np.array([166 - f, 116.5 - f, 53 - f, 48 - f, 46 - f, 36 - f,
              31.25 - f, 32.8 - f, 29.5 - f, 26 - f, 24 - f])
y = x * 0.04113215

# Curve
popt, pcov = curve_fit(fun, x, y)
print(popt)
print(pcov)

# Values for the fitted fun
xFit = np.arange(0.001, 142.0, 0.01)

plt.plot(x, y, 'bo', label='Datos')
plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste = 0.000175x + 0.0726')


plt.title('Cambio de variable en los datos experimentales')
plt.xlabel('X')
plt.ylabel('X')
plt.grid()
plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/tarearecta.png")
plt.show()
