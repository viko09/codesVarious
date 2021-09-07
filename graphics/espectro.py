import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('nueva.csv')

# Plot data
plt.plot(data, 'or', label='Datos')
plt.title('Espectro de luz de un foco')
plt.xlabel('Pixeles')
plt.ylabel('Longitud de onda')
plt.legend()
plt.grid()
plt.show()
