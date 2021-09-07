import numpy as np
import matplotlib.pyplot as plt

#  Datos

x = [0.10, 0.15, 0.20, 0.25]
y = [0.655, 0.795, 0.912, 1.012]

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
plt.xlabel('Longitud (m)')
plt.ylabel('Periodo (s)')
plt.title('Relación: Longitud vs Periodo')
plt.grid()
plt.legend()
plt.show()
