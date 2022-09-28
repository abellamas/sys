import numpy as np
import matplotlib.pyplot as plt
import time


genelec = np.load("./files/loudspeaker_Genelec.npy")
jbl = np.load("./files/loudspeaker_JBL.npy")

frequencies = np.array([genelec[0], jbl[0]])
measures = [
    np.array([genelec[1], jbl[1]]), #array of magnitudes
    np.array([genelec[2], jbl[2]])  #array of phases
]
loudspeakers = ['Genelec', 'JBL'] # loudspeakers measured
graphics = ['Magnitude [dB]', 'Phase [deg]'] # plots that are necessary

freq_ticks = [20,100,1000,10000] # values of frequency to show 
y_ticks = [np.arange(70, 92, 3), np.arange(-180, 181, 30)] # values of magnitude and phase

fig, axs = plt.subplots(len(graphics), 1, figsize=(12, 8)) # Instance of Figure and Axes

axs[0].set_title('Response Frequency', fontsize=16) # title only at top

for graph in range(len(graphics)):
    for speaker in range(len(loudspeakers)):
        axs[graph].semilogx(frequencies[speaker], measures[graph][speaker], label=loudspeakers[speaker])

    axs[graph].legend(loc='upper right') #show the labels as a legend
    #set axes labels
    axs[graph].set_xlabel('Frequency [Hz]')
    axs[graph].set_ylabel(graphics[graph])
    #set axes ticks
    axs[graph].set_xticks(freq_ticks, freq_ticks)
    axs[graph].set_yticks(y_ticks[graph], y_ticks[graph])
    
    axs[graph].set_xlim([20,20000])
    axs[graph].grid()
    
plt.tight_layout()
plt.show()
fig.savefig(f'./images/response_freq_{time.strftime("%Y%m%d_%H%M%S")}.png')
