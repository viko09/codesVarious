import matplotlib.pyplot as plt
import numpy as np
import math

for i in range(0, 91, 15):
    ar1 = math.sin(math.radians(i))

x = np.array([0, 0.25881904510252074, 0.49999999999999994, 0.7071067811865475, 0.8660254037844386, 0.9659258262890683,
              1])
y = np.array([math.sin(math.radians(0)), math.sin(math.radians(9.9)), math.sin(math.radians(19.5)),
              math.sin(math.radians(28.1)), math.sin(math.radians(35.3)), math.sin(math.radians(40.1)),
              math.sin(math.radians(41.8))])

print(x)
print(y)

xData = np.array([0, 0.2588, 0.5, 0.7071, 0.8660, 0.9659, 1])
yData = np.array([0, 0.1993, 0.3842, 0.5446, 0.6665, 0.7431, 0.7693])

# Plot data
plt.plot(x, y, 'orangered')
plt.plot(x, y, 'bo', label='Datos del vidrio')

plt.plot(xData, yData, 'green')
plt.plot(xData, yData, 'ro', label='Datos del agua')

plt.title('Refracción de ambos casos')
plt.xlabel('Sen θi')
plt.ylabel('Sen θt')
plt.grid()
plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/funciontotal.png")
plt.show()
