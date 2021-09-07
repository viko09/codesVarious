import numpy as np
import matplotlib.pyplot as plt

#  Datos

x = [10, 9.5, 9, 8.6, 8.1, 7.4, 7.1, 6.5, 6, 5.5]
y = [3.54, 3.74, 3.95, 4.11, 4.38, 4.79, 5.02, 5.42, 5.89, 6.45]

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
plt.xlabel('Separación de la placa')
plt.ylabel('Capacitancia (x10^-13)')
plt.title('Datos obtenidos al mantener área constante')
plt.grid()
plt.legend()
plt.show()
