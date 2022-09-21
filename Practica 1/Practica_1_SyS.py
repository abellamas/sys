#%%

import numpy as np
import matplotlib.pyplot as plt

#%% ejercicio 1.01
zc1 = 1+1j
# a través de una función de numpy
zc1_module = np.absolute(zc1)
print(zc1_module)
# through a method of a complex object
print(zc1.__abs__())

#%% ejercicio 1.02
z1 = 4 + 3j
z2 = 2 + 2j

suma = z1+z2
resta = z1-z2
mult = z1*z2
div = z1/z2
print('Suma: ', suma)
print('Resta: ', resta)
print('Multiplicación: ', mult)
print('Division: ', div)

#%% ejercicio 1.03
c = np.array([[1, 5, 2], [3, 4, 8]])
print(c.shape)

#%% ejercicio 1.04
print(c[:, 1])
#%% ejercicio 1.05
a = np.array([1, 2, 3, 4])
#%% ejercicio 1.06
b = a.reshape(2, 2)
print(b)
#%% ejercicio 1.6

T = 0.01
time = np.arange(-1, 1+T, T)
x_values = []
for t in time:
    x = 2*np.sin(2*np.pi*5*t)
    if x < 0:
        x_values.append(-x)
    else:
        x_values.append(x)
plt.plot(time, x_values)
plt.grid()
#%% ejercicio 1.07

numero_7 = 34
if numero_7 % 2 == 0:
    print(f'el número {numero_7} es par')
else:
    print(f'el número {numero_7} es impar')

#%% ejercicio 1.08

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

#%% ejercicio 1.09
numero_primo = 37
sucesion = np.arange(2, numero_primo + 1, 1)
divisores = []

for n in sucesion:
    if numero_primo % n == 0:
        divisores.append(n)

if divisores[0] == numero_primo:
    print('es primo')
else:
    print('no es primo')
#%% ejercicio 1.10
lista = [1, 4, 5, 2, 3]
lista.reverse()
print(lista)
#%% ejercicio 1.11

'''
★★★★☆ - 1.11) Dado un numero entero positivo de entrada n, 
escribir la serie de fibonacci hasta el n-ésimo elemento
'''

n = int(input())
f_1 = 0
f_2 = 1
f_n = 1
i = 0

while i < n:
    print(f_n)
    f_n = f_1 + f_2
    f_1 = f_2
    f_2 = f_n
    i = i + 1


# %%
