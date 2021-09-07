import numpy as np
import matplotlib.pyplot as plt

#  Datos

x = [400, 369.9, 340.9, 308.6, 277.9, 248.9, 221.4, 188.4, 161.4, 130.5]
y = [3.54, 3.27, 3.02, 2.76, 2.46, 2.2, 1.96, 1.67, 1.43, 1.16]

n = len(x)
x = np.array(x)
y = np.array(y)

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x*y)
sum_x2 = sum(x*x)
sum_y2 = sum(y*y)
promedio_x = sum_x/n
promedio_y = sum_y/n

m = (sum_x*sum_y - n*sum_xy)/(sum_x**2 - n*sum_x2)
b = promedio_y-(m*promedio_x)

print(m, b)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m*x+b, label='Ajuste')
plt.xlabel('Área de la placa')
plt.ylabel('Capacitancia (x10^-13)')
plt.title('Datos obtenidos al mantener la separación constante')
plt.grid()
plt.legend()
plt.show()
