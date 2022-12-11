# Created by. Viko Luna

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np

# Upload Experimental Data
dats = pd.read_csv("measures.csv")
xDat = dats['tiempo']
yDat = xDat*37.5
print(yDat)

# Velocity Plot
plt.scatter(xDat, yDat, color='purple', alpha=0.65, label=f'Datos')
plt.title("Datos experimentales")
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()
# Save as png
# plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/vel1.png")
plt.show()

# Binomial Distribution
mu = np.mean(yDat)
std = np.std(yDat)
# This is the fitted func
# fit = stats.norm.pdf(yDat, mu, std)
print("mu = ", mu, " std = ", std)
# Histogram Plot
plt.hist(yDat, density=True, edgecolor='black', ls='dotted', facecolor='b', alpha=0.24)
xmin, xmax = plt.xlim()
x = np.sort(yDat)
p = norm.pdf(x, mu, std)
print(x, p)
plt.plot(x, p, 'b', linewidth=1, label='Distribución')
plt.axvline(mu, color='g', label="Media: 55.385")
plt.errorbar(x, p, yerr=np.arange(40, 70, 101), label='both limits', color='y')
title = "Mediciones Obtenidas: "
plt.title(title)
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Porcentaje de repeticiones')
plt.grid(axis='y', alpha=0.75)
plt.legend()
plt.show()
