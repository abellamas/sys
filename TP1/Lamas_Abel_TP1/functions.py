import numpy as np

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