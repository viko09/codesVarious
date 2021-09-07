import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('listasol.csv')

x = data['pixeles']

y = data['longitud']

n = 4
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x*y)
sum_x2 = sum(x*x)
sum_y2 = sum(y*y)
promedio_x = sum_x/n
promedio_y = sum_y/4

m = (sum_x*sum_y - n*sum_xy)/(sum_x**2 - n*sum_x2)
b = promedio_y-(m*promedio_x)

print(m, b)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m*x+b, label='Ajuste: 0.2609x + 346.0124')
plt.title("Espectro del sol")
plt.xlabel("Pixeles")
plt.ylabel("Longitud de onda")
plt.legend()
plt.locator_params()
plt.grid()
plt.show()
