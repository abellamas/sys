import numpy as np
import matplotlib.pyplot as plt
# from scipy import signal


#grafica de funciones
T = 0.001 # intervalo de muestreo
t = np.arange(0, 10+T, T) # vector tiempo
fig, axs = plt.subplots(ncols= 2, nrows=2) #se define las dimensiones del ploteo

#se configura cada ubicacion 
axs[0,0].plot(t, np.sin(t), '-y') #tiempo, funcion, trazo
axs[0,0].set_title('y(t)=sen(t)')
axs[0,0].set_xlabel('Tiempo [s]')
axs[0,0].set_ylabel('Amplitud')
axs[0,0].grid()

axs[0,1].plot(t, np.cos(t), '--r')
axs[0,1].set_title('y(t)=cos(t)')
axs[0,1].set_xlabel('Tiempo [s]')
axs[0,1].set_ylabel('Amplitud')
axs[0,1].grid()

axs[1,0].plot(t, np.sin(2*t), '.b')
axs[1,0].set_title('y(t)=sen(2t)')
axs[1,0].set_xlabel('Tiempo [s]')
axs[1,0].set_ylabel('Amplitud')
axs[1,0].grid()


axs[1,1].plot(t, np.cos(2*t),'-.y')
axs[1,1].set_title('y(t)=cos(2t)')
axs[1,1].set_xlabel('Tiempo [s]')
axs[1,1].set_ylabel('Amplitud')
axs[1,1].grid()


fig.tight_layout() #acomoda los plots
plt.show() #muestra los plots