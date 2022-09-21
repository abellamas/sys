# SEÑALES Y SISTEMAS

## Scipy

Del modulo _signal_ que viene en _scipy_ se puede utilizar distintas señales bajo la siguiente sintaxis

````py
import numpy as np
from scipy import signal
t = np.arange(0,1,16000)
signal.square(t)
````

Las siguientes señales vienen en el modulo _signal_

- square : señal cuadrada
- sawtooth : diente de sierra

Mas pueden encontrarse en la documentación https://docs.scipy.org/doc/scipy/reference/signal.html


Mientras que de _numpy_ es posible hacer las siguientes señales

- sign : función signo
