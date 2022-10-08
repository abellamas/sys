#%%
import numpy as np
import matplotlib.pyplot as plt
from func.Giro_desplaza import giro_desplaza

#%%
'''
★☆☆☆☆ - 3.02) Graficar la señal definida previamente de forma tal que se vea de la siguiente manera:
'''

n = np.arange(1001) # Array de 1000 muestras

x = np.sin(2*(1/1000)*np.pi*n) * np.sin(2*(1/100)*np.pi*n)
x = x/max(abs(x)) # Normalización de la señal, para que su valor máximo sea 1.

fig, ax = plt.subplots(1, 1)
ax.plot(n, x)
ax.set_title('Ejercicio 1', fontsize=18)
ax.set_xlabel('Muestras')
ax.set_ylabel('Amplitud [V]')
ax.grid()
plt.plot()
plt.show()
#%%

'''
★★☆☆☆ - 3.03) A partir de la señal creada y[n], generar un grafico que se vea de la siguiente manera:
'''

fs = 1
n = np.arange(-1000, 1000+1/fs, 1/fs)
y = (abs(n)**1.5) * np.sin(2*(1/100)*np.pi*n)
y = y/max(abs(y)) #Normalización de la señal, para que su valor máximo sea 1.
y_flip = giro_desplaza(y, fs, -100, Giro=1)

fig, axs = plt.subplots()
axs.plot(n,y)
axs.set_xlabel('Muestras')
axs.set_xticks([-1000, 0, 1000])
axs.set_ylabel('Amplitud [V]')
axs.grid()

plt.show()




# %%
