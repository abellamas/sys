import numpy as np 

def giro_desplaza(x, fs, t0, Giro):
    
    N = len(x)
    d = t0*fs

    if Giro == 1:
        x = np.flip(x)

    x2 = np.zeros(N)

    if d > 0:
        for i in range(0,N-int(d)):
            x2[int(i+d)]=x[i]
    else:
        for i in range(0,N+int(d)):
            x2[i]=x[int(i-d)]

    return x2