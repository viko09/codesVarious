import numpy as np
import matplotlib.pyplot as plt


y = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x = [0, 9.6, 14, 17.5, 20, 22, 23, 25.3, 27.4]


num = len(x)

x = np.array(x)
y = np.array(y)

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x*y)
sum_x2 = sum(x*x)
sum_y2 = sum(y*y)
prom_x = sum_x/num
prom_y = sum_y/num

m = (sum_x*sum_y - num*sum_xy)/(sum_x**2 - num*sum_x2)
b = prom_y-(m*prom_x)

print(m, b)

plt.plot(x, y, 'o', label='Datos')
plt.xlabel('t_m')
plt.ylabel('y_m')
plt.title('Relación: m(lambda/2) vs y')
plt.grid()
plt.legend()
plt.show()
