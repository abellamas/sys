import numpy as np
import matplotlib.pyplot as plt

def grapher(x,*functions):
    '''
    x: independent variable -> numpy.ndarray
    functions: [function:numpy.ndarray, label:str]
    '''
    fig, ax = plt.subplots()
    
    for graphic, label in functions:
        ax.plot(x, graphic, label=label)
    
    ax.set_xlabel('Tiempo [s]')
    ax.set_ylabel('Amplitud')
    ax.legend(loc='upper right')
    ax.grid()
    plt.show()  

    