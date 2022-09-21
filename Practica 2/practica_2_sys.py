#%%
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal, misc
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
'''
★★☆☆☆ - 2.02) Generar y graficar 2 señales continuas periódicas de distinto tipo. Debe generar el vector tiempo correspondiente para un intervalo entre -2s y 2s. Adopte una frecuencia de muestreo adecuada de acuerdo a las señales que vaya a generar
'''

T = 1/1000
t = np.arange(-2, 2+T, T)

fig, axs = plt.subplots(2,1)
axs[0].plot(t, np.sin(2*np.pi*3*t))
axs[1].plot(t, np.sin(2*np.pi*5*t+np.pi/3), color="red")
axs[0].grid()
axs[1].grid()
plt.show()
# %%
'''
★★☆☆☆ - 2.03) Generar y graficar 2 señales continuas no periódicas de distinto tipo. Debe generar el vector tiempo correspondiente para un intervalo entre -2s y 2s. Adopte una frecuencia de muestreo adecuada de acuerdo a las señales que vaya a generar.
'''

T = 1/1000
t = np.arange(-2, 2+T, T)
delta_array = np.ones(len(t))
delta_array[t!=1] = 0 

fig, axs = plt.subplots(2,1)
axs[0].plot(t, signal.chirp(t+2, f0=2, f1=20, t1=2))
axs[1].plot(t, signal.unit_impulse(len(t), 'mid'))
axs[0].grid()
axs[1].grid()
plt.show()

# %%
'''
Calcule y grafique la senoidal compleja  y[n]=e^{𝑗𝜋𝑛/5 - 𝜋3} .

★☆☆☆☆ - 2.04) Grafique las partes real e imaginaria de y[n]. ¿Cuál es el período de la señal?. Justifique su respuesta gráfica y analíticamente.
'''
T = 1/2
n = np.arange(0,30+T, T)
y = np.exp((1j*np.pi*n)/5 - np.pi/3)
fig, axs = plt.subplots(2,1)
axs[0].stem(n, y.real)
axs[1].stem(n, y.imag)
axs[0].grid()
axs[1].grid()
plt.show()
# %%

'''
Calculemos la función  z[n]=x[n]y[n]
Donde x[n] = (0.9)^n

'''
T = 1/2
n = np.arange(0,30+T, T)
x = 0.9**n
y = np.exp((1j*np.pi*n)/5 - np.pi/3)
z = x*y
fig, axs = plt.subplots(4,1)
axs[0].stem(n, x, label="x[n]")
axs[1].stem(n, y, label="y[n]")
axs[2].stem(n, z.real, label="Re{z[n]}")
axs[3].stem(n, z.imag, label="Im{z[n]}")
axs[0].grid()
axs[1].grid()
axs[2].grid()
axs[3].grid()
axs[0].legend()
axs[1].legend(loc='upper right')
axs[2].legend()
axs[3].legend()
plt.tight_layout()
plt.show()
# %%
'''
Generamos dos senoidales reales similares a las del caso continuo.
Grafique v1, su parte par y su parte impar, v2 y sus partes par e impar usando subplot
'''

T = 1/2
n = np.arange(0,30+T, T)

v1 = np.cos(np.pi*n/5 - np.pi/3)
v2 = np.sin(np.pi*n/5 - np.pi/4)

v1par = 0.5*(v1 + np.flip(v1))
v1impar = 0.5*(v1 - np.flip(v1))
v2par = 0.5*(v1 + np.flip(v2))
v2impar = 0.5*(v1 - np.flip(v2))


fig, axs = plt.subplots(3,1)
axs[0].stem(n, v1)
axs[0].set_ylim(-1,1)
axs[0].set_title('v1')
axs[1].stem(n, v1impar)
axs[1].set_ylim(-1,1)
axs[1].set_title('v1 impar')
axs[2].stem(n, v1par)
axs[2].set_ylim(-1,1)
axs[2].set_title('v1 par')
axs[0].grid()
axs[1].grid()
axs[2].grid()

plt.tight_layout()
plt.show()


fig, axs = plt.subplots(3,1)
axs[0].stem(n, v2)
axs[0].set_ylim(-1,1)
axs[0].set_title('v2')
axs[1].stem(n, v2impar)
axs[1].set_ylim(-1,1)
axs[1].set_title('v2 impar')
axs[2].stem(n, v2par)
axs[2].set_ylim(-0.3,0.3)
axs[2].set_title('v2 par')
axs[0].grid()
axs[1].grid()
axs[2].grid()

plt.tight_layout()
plt.show()
# %%

'''
★☆☆☆☆ - 2.05) Desarrolle v1 usando la siguiente identidad trigonométrica:

cos(A-B) = cos(A)cos(B)+sen(A)sen(B)
Grafique las señales involucradas.
'''

T = 1/2
n = np.arange(0,30+T, T)

v1 = np.cos(np.pi*n/5 - np.pi/3)

a = np.pi*n/5
b = np.pi/3
v1_desarrollo = np.cos(a)*np.cos(b) + np.sin(a)*np.sin(b)

fig, axs = plt.subplots(2,1)

axs[0].stem(n, v1)
axs[0].set_ylim(-1,1)
axs[0].set_title('v1')
axs[0].grid()

axs[1].stem(n, v1_desarrollo)
axs[1].set_ylim(-1,1)
axs[1].set_title('v1 desarrollo')
axs[1].grid()

plt.tight_layout()
plt.show()

# %%
'''
★☆☆☆☆ - 2.06) Generar y graficar una señal discreta periódica y una no periódica. Para ello, generar un vector n en el intervalo [0, 500]
'''

N = 8
n = np.arange(0, 500+N, N)

fig, axs = plt.subplots(2,1)
axs[0].stem(n, signal.sawtooth(0.05*n, width=1))
axs[1].stem(n, np.exp(-abs(n - 200)/50))
plt.show()
# %%
