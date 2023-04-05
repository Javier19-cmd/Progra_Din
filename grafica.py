import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('registros_dac.csv')

plt.scatter(df['Discos'], df['Tiempo'])
plt.xlabel('Discos')
plt.ylabel('Tiempo')
plt.show()
