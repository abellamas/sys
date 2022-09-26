import numpy as np
import matplotlib.pyplot as plt
import time


def descriptive(data):
    """Print descriptive information about the argument 'data'

    Parameters
    ----------
    data : any
        Variable to be evaluated, this only can be `int`, `str`, `float`, `list`, `tuple`, `dict`, `np.ndarray`
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
        
        
def graph_discrete(n, f_n, title, xticks: np.ndarray = None, url:str = None, file_name:str = None):
    fig, ax = plt.subplots(1, 1)
    ax.stem(n, f_n)
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')
    
    if xticks is not None:
        ax.set_xticks(xticks)
        
    ax.set_title(title)
    ax.grid()
    
    if url is not None:
        plt.savefig(f'{url}{file_name}.png')
        print(f'Plot save in {url}{file_name}')
    
    plt.show()
    
    return ax

def save_files(title, numpy_obj, path_plot, path_values):
    file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
    if path_plot is not None:
        plt.savefig(f'{path_plot}{file_name}.png')
    elif path_values is not None:
        np.save(f'{path_values}{file_name}')
    else:
        return None
    
def numpy_save(np_values:np.ndarray, url:str = None, file_name:str = None):
    if url is not None:
        np.save(f'{url}{file_name}', np_values)
  
def control_range(t_x, t_i, t_f):

    """Analyze if a value belongs to an open interval. 
    
    Parameters
    ----------
    t_x : float or int
        Value to analyze
    t_i : float or int
        Where the interval starts
    t_f : float or int
        Where the interval ends
    
    Returns
    -------
    float or int
        Return t_x if this belong at the interval (t_i, t_f)
    bool
        return False otherwise
    """
    
    if type(t_x) is int and t_x > t_i and t_x < t_f:
        return t_x
    else: 
        return False
    
def gen_discrete_signals(signal:str, start:int, stop:int, path_plot:str = None, path_values: str = None, t_impulse:int = 0, t_step:int = 0, t_init:int = -1, t_finish:int = 1, base_factor:float = 1.0, mean:float = 0, std:float = 1):
    """Plot and return a values of impulse, step, impulse train, triangle and normal random.

    Parameters
    ----------
    signal : str
        Signal can be `impulse`, `step`, `impulse train`, `triangle` or `normal random`.
    start : int
        Determinates the starts from the plot and array returned.
    stop : int
        Determinates the end from the plot and array returned.
    path_plot : str, optional
        Relative URL where the figure will be save, by default is None.
    path_values : str, optional
        Relative URL where the numpy data will be save, by default is None.
    t_impulse : int, optional
        Value where the impulse occurs, must be between start and stop, by default 0.
    t_step : int, optional
        Value where the step function begins, must be between start and stop, by default 0.
    t_init : int, optional
        Value from the train starts, by default -1.
    t_finish : int, optional
        Value until the train occurs, by default 1.
    base_factor : float
        Modified the half base distance to zero and the height of the triangle pulse, by default 1.0.
    mean : float, optional
        Mean value for the normal random distribution, by default 0.
    std : float, optional
        Standar desviation value for the normal random distribution. This can't be a negative value, by default 1.

    Returns
    -------
    np.ndarray
        Return an numpy array which contains the values of the signal
    """
  

    if start > stop or start == stop:
        raise ValueError('The argument stop must be greater than start')
    else:
        samples = np.arange(start, stop+1) #samples are integers

    if signal == "impulse":
        t_0 = control_range(t_impulse, start, stop) #control if the t_impulse belong at the interval (start,stop)
        
        if t_0 is not False:
            zeros = np.zeros(len(samples))
            zeros[samples == t_0] = 1
            title = f'Impulse on {t_0}'
            file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
            numpy_save(zeros, path_values, file_name)
            graph_discrete(samples, zeros, title, samples, path_plot, file_name)
            return zeros
        else:
            raise ValueError("The 4th argument must be a integer value between start and stop")
                 
    
    elif signal == "step":
        t_step = control_range(t_step, start, stop) #control if the t_step belong at the interval (start,stop)
        
        if t_step is not False:
            zeros = np.zeros(len(samples))
            zeros[samples >= t_step] = 1
            title = f'Step Function from {t_step}'
            file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
            numpy_save(zeros, path_values, file_name)
            graph_discrete(samples, zeros, title, samples, path_plot, file_name)
            return zeros
        else:
            raise ValueError("The 4th argument must be a integer value between start and stop")
        
    elif signal == "impulse train":
        t_i = control_range(t_init, start, stop) # t_i is where starts the impulse train
        t_f = control_range(t_finish, start, stop) # t_f is where stops the train
        
        if t_i != False and t_f != False and t_i <= t_f:
            zeros = np.zeros(len(samples))
            zeros[(samples >= t_i) & (samples < t_f)] = 1
            title = f'Impulse train from {t_i} to {t_f}'
            file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
            graph_discrete(samples, zeros, title, samples, path_plot, file_name)
            return zeros
        else:
            raise ValueError("The 4th argument must be an integer between start and stop, also must be grater than the 5th argument")
        
    elif signal == "triangle":
        base = base_factor
        
        if (type(base) is int or type(base) is float) and (base <= stop and base >= start):
            base = abs(base)
            slope = -abs(samples) + base
            slope[(samples < -base) | (samples > base)] = 0
            
            title = f'Triangle with base factor {base}'
            file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
            
            graph_discrete(samples, slope, title, samples, path_plot, file_name)
            return slope
        else:
            raise ValueError("base_factor must be and integer or float value between start and stop values")
            
    elif signal == "normal random":
        mean = float(mean)
        std = float(std)

        if (type(std) is float and type(mean) is float) and (std >= 0):
            random_signal = np.random.normal(mean, std, len(samples))
            title = f'Normal random with $\mu$ = {mean} and $\sigma$ = {std}'
            file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'
            graph_discrete(samples, random_signal, title, samples, path_plot, file_name)
            return random_signal
        else:
            raise ValueError('The mean and std desviation must be float or integers. The std must be a non negative value.')
    else:
        raise ValueError(f"The function requerid: {signal} is no available")
    
if __name__=="__main__":
    gen_discrete_signals('impulse', -5, 5)
