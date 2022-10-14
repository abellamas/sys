import numpy as np
import matplotlib.pyplot as plt
import gen
import graf

frequencies = [40, 80, 120]
sines = []
t = np.linspace(0, 1, 16000)

for f in frequencies:
    sines.append([gen.sin_generator(f, t), f'y(t)=sen(2$\pi${str(f)}t)'])
    
graf.grapher(t, *sines)

