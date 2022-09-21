#%%
import numpy as np
from matplotlib import pyplot as plt
# import scipy.signal as signal
#%%
'''
★★☆☆☆ - 2.01) Para el signo y el escalón, que son funciones que solo toman valores de 0, y -1, es posible construirlas haciendo uso de las funciones `zeros` y `ones` para crear los valores de 'y', y usando la funcion 'concatenate' de NumPy para unir segmentos. Lea la documentación de esta función y cree un escalón idéntico a los anteriores concatenando un array de unos y un array de ceros. 
'''


def signo(t):
    sign = np.ones(shape=t.__len__(), dtype=np.int8)
    sign[t==0] = 0
    sign[t<0] = -1
    return sign

def unitary_step(t):
    zeros = np.zeros(shape=t.__len__())
    ones = np.ones(shape=t.__len__())
    ones[t<0] = 0
    u_step = zeros + ones
    return u_step

T = 0.001
t = np.arange(-1, 1+T, T)

fig, axs = plt.subplots(2, 1, figsize=(10,5))
axs[0].plot(t, signo(t-0.5))
axs[0].set_title('Función Signo')
axs[1].plot(t, unitary_step(t+0.5))
axs[1].set_title('Escalon unitario')
plt.show()
# %%
