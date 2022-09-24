import numpy as np

def sin_generator(f,t):
    '''
    This function generates a sinusoidal signal of a certain frequency.
    
    f: frequency -> int
    t: time -> numpy.ndarray
    '''
    
    return np.sin(2*np.pi*f*t)