import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('listaled.csv')

x = data['pix']

y = data['irradiancia']

plt.plot(x, y, 'o', label='Datos')
plt.title("Espectro de luz led")
plt.xlabel("Pixeles")
plt.ylabel("Longitud de onda")
plt.legend()
plt.locator_params()
plt.grid()
plt.show()
