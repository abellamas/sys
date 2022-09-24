import numpy as np

def descriptive(data):
    print(type(data))
    if type(data)=="int":
        print(f'El dato ingresado es un int,con valor {data}')