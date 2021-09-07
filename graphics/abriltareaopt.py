import matplotlib.pyplot as plt
import numpy as np

f = 23.5

xdato = np.array([47, 70.5, 94, 117.5])
ydato = np.array([74.5, 66.5, 58.5, 51])

plt.plot(xdato, ydato, color='orangered', label='Datos')
plt.plot(xdato, ydato, 'bo', label='Datos')
plt.title('Distancia Objeto vs Distancia Imagen')
plt.xlabel('Distancia objeto')
plt.ylabel('Distancia imagen')
plt.grid()
plt.legend()
plt.savefig('/home/vikoluna/Documents/BUAP/4 - Cuarto Semestre/Optics/tarealunes.png')
plt.show()
