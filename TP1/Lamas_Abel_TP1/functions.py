import numpy as np
import matplotlib.pyplot as plt

def descriptive(data):
    """Return descriptive information about the argument 'data'

    Args:
        data (any): variable to be evaluated
    """    
    type_data = type(data)
    if type_data is int:
        print(f'El dato ingresado es un objeto int con valor: {data}')
    elif type_data is str:
        print(f'El data ingresado es un objeto str con valor: {data}')
    elif type_data is float:
        print(f'El dato ingresado es un objeto float con valor: {data}')
    elif type_data is list:
        print(f'El dato ingresado es un objeto list con valor: {data}')
    elif type_data is tuple:
        print(f'El dato ingresado es un objeto tuple con valor: {data} \n Cantidad de elementos: {len(data)}')
    elif type_data is dict:
        print(f'El dato ingresado es un objeto dict con pares clave valor: \n')
        for key, value in data.items():
            print(f'{key} : {value} \n')
    elif type_data is np.ndarray:
        print(f'El dato ingresado es un objeto numpy.ndarray con valor: {data} \n Dimensiones: {data.ndim} \n Tamaño de cada dimension: {data.shape} \n Cantidad de elementos: {data.size}')
    else:
        print('No es un tipo de dato reconocible')
        
        
def graph(n, f_n):
    fig, ax = plt.subplots(1, 1)
    ax.stem(n, f_n)
    ax.grid()
    plt.show()
    
def gen_discrete_signals(signal, start, stop, *args):
# def gen_discrete_signals(*args):
    """

    Args:
        signal (str): _description_
    Returns:
        _type_: _description_
    """
    
    samples = np.arange(start, stop+1)

    
    if signal == "impulso":
        t_0 = args[0]
        if type(t_0) is int and t_0 > start and t_0 < stop:
            zeros = np.zeros(len(samples))
            zeros[samples == args[0]] = 1
            graph(samples, zeros)
        else:
            raise ValueError("El 3er argumento debe ser un valor entero ubicado entre start y stop")
        
    elif signal == "escalon":
        t_0 = args[0]
        if type(t_0) is int and t_0 > start and t_0 < stop:
            zeros = np.zeros(len(samples))
            zeros[samples >= args[0]] = 1
            graph(samples, zeros)
        else:
            raise ValueError("El 3er argumento debe ser un valor entero ubicado entre start y stop")
        
    elif signal == "tren_impulsos":
        t_i = args[0]
        t_f = args[1]
        
        if type(t_i) is int and t_i > start and t_i < stop:
            if type(t_f) is int and t_f > start and t_f < stop:
                if t_i <= t_f:
                    zeros = np.zeros(len(samples))
                    zeros[(samples >= args[0]) & (samples < args[1])] = 1
                    graph(samples, zeros)
                else:
                    raise ValueError("El 3er argumento debe ser mayor que el 4to argumento")
            else:
                raise ValueError("El 3er argumento debe ser un valor entero ubicado entre start y stop")
    elif signal == "triangular":
        pass
    elif signal == "aleatoria":
        pass
    else:
        return f"no se encuentra la función {signal}"
    
    
if __name__=="__main__":
    # gen_discrete_signals("impulso", -2, 10, 5)
    # gen_discrete_signals("escalon", -2, 10, 5)
    gen_discrete_signals("tren_impulsos", -10, 10, 9, 100)