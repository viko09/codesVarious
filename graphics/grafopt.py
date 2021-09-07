import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b):
    return a*x + b


data = pd.read_csv('listachida.csv')

x = data['pixels']
print(x)

y = data['longitud']
print(y)


# Plot data
plt.plot(x, y, 'bo', label='Datos')

# Curve
popt, pcov = curve_fit(fun, x, y)
print(popt)

# Values for the fitted fun
xFit = np.arange(900.0, 1250.0, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'red', label='Ajuste')
plt.title('Espectro visible de lampara')
plt.xlabel('pixel')
plt.ylabel('longitud')
plt.grid()
plt.legend()
plt.show()
