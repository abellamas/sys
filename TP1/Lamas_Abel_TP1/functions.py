import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time


def descriptive(data):
    """Print descriptive information about the argument 'data'

    Parameters
    ----------
    data : any
        Variable to be evaluated, this only can be `int`, `str`, `float`, `list`, `tuple`, `dict` or `np.ndarray`
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
        
        
def graph_discrete(n, f_n, title, xticks: np.ndarray = None):
    """Show and return a plot of signal
    
    Parameters
    ----------
    n : np.array
        Samples axis
    f_n : np.array
        Signal axis
    title : str
        Title for the signal plot
    xticks: np.ndarray
        Values for the samples axis (x-axis), by default is None. 
        
    Returns
    -------
    matplotlib.figure.Figure
        Figure object with the plot of signal
    """
    fig, ax = plt.subplots(1, 1)
    ax.stem(n, f_n)
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')
    if xticks is not None:
        ax.set_xticks(xticks)
    ax.set_title(title)
    ax.grid()    
    plt.show()
    
    return fig

def save_files(title:str, plot:matplotlib.figure.Figure, x:np.array, y:np.array, path_plot:str = None, path_values:str = None):
    """Allows save a png and npy with data about a signal

    Parameters
    ----------
    title : str
        Title for the files
    plot : matplotlib.figure.Figure
        Figure Object that can be saved
    x : np.array
        x-axis values of the signal
    y : np.array
        y-axis values of the signal
    path_plot : str, optional
        Relative URL where save a image, by default None
    path_values : str, optional
        Relative URL where save a npy file, by default None
    """

    file_name = f'{title.replace(" ","_")}_{time.strftime("%Y%m%d_%H%M%S")}'

    if path_values is not None:
        np.save(f'{path_values}{file_name}.npy', np.array([x, y]) )
        print(f'Array values saved in {path_plot}{file_name}.npy')

    if path_plot is not None:
        plot.savefig(f'{path_plot}{file_name}.png')
        print(f'Plot save in {path_plot}{file_name}.png')

  
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
        t_0 = control_range(t_impulse, start, stop)
        
        if t_0 is not False:
            impulse = np.zeros(len(samples))
            impulse[samples == t_0] = 1
            title = f'Impulse on {t_0}'
            plot_signal = graph_discrete(samples, impulse, title, samples) #plot the signal and return an Figure object to be saved
            save_files(title, plot_signal, samples, impulse, path_plot, path_values) #allows save the plot and arrays samples and impulse
            
            return impulse
      
        else:
            raise ValueError("The 4th argument must be a integer value between start and stop")
                 
    
    elif signal == "step":
        t_step = control_range(t_step, start, stop)
        
        if t_step is not False:
            step = np.zeros(len(samples))
            step[samples >= t_step] = 1
            title = f'Step Function from {t_step}'
            plot_signal = graph_discrete(samples, step, title, samples)
            save_files(title, plot_signal, samples, step, path_plot, path_values)

            return step

        else:
            raise ValueError("The 4th argument must be a integer value between start and stop")
        
    elif signal == "impulse train":
        t_i = control_range(t_init, start, stop) # t_i is where starts the impulse train
        t_f = control_range(t_finish, start, stop) # t_f is where stops the train
        
        if t_i != False and t_f != False and t_i <= t_f:
            impulse_train = np.zeros(len(samples))
            impulse_train[(samples >= t_i) & (samples < t_f)] = 1
            title = f'Impulse train from {t_i} to {t_f}'
            plot_signal = graph_discrete(samples, impulse_train, title, samples)
            save_files(title, plot_signal, samples, impulse_train, path_plot, path_values)
            return impulse_train
        else:
            raise ValueError("The 4th argument must be an integer between start and stop, also must be grater than the 5th argument")
        
    elif signal == "triangle":
        base = base_factor
        
        if (type(base) is int or type(base) is float) and (base <= stop and base >= start):
            base = abs(base)
            triangle = -abs(samples) + base
            triangle[(samples < -base) | (samples > base)] = 0
            title = f'Triangle with base factor {base}'
            plot_signal = graph_discrete(samples, triangle, title, samples)
            save_files(title, plot_signal, samples, triangle, path_plot, path_values)
            return triangle
        else:
            raise ValueError("base_factor must be and integer or float value between start and stop values")
            
    elif signal == "normal random":
        mean = float(mean)
        std = float(std)

        if (type(std) is float and type(mean) is float) and (std >= 0):
            random_signal = np.random.normal(mean, std, len(samples))
            title = f'Normal random with $\mu$ = {mean} and $\sigma$ = {std}'
            plot_signal = graph_discrete(samples, random_signal, title, samples)
            save_files(title, plot_signal, samples, random_signal, path_plot, path_values)
            return random_signal
        else:
            raise ValueError('The mean and std desviation must be float or integers. The std must be a non negative value.')
    else:
        raise ValueError(f"The function requerid: {signal} is no available")

def gen_n_sin(t_start:float, t_end:float, f_sample:float, frequencies:list):
    """For each entered frequency generate a sine signal 

    Parameters
    ----------
    t_start : float
        Time to start the vector time
    t_end : float
        Time to start the vector time
    f_sample : float
        Sample frequency
    frequencies : list
        Contains the diferent values of frecuencies for each signal

    Returns
    -------
    list
        Return a list composed for tuples for each frequency in the next order:
        (array time, array sine at f frequency, label of signal) 
    """
    freq = frequencies
    t = np.arange(t_start, t_end + 1/f_sample, 1/f_sample)
    sin_array = np.empty((0, len(t))) # create an empty np array with dimensions 0 and the quantity of samples t
    label_sin = []
    output_array = [] # will be contain tuples for each frequency
    n = 0
    
    for f in freq:
        
        sin_array = np.append(sin_array, np.array([np.sin(2*np.pi*f*t)]), axis=0) #appends each sin at f frequency in an array
        label_sin.append(f'sin_{n}_freq_{f}') #append the label of each sin in a list
        n=n+1
        
    for i in range(len(freq)):
        #concatenate the results in a list of tuples
        output_array.append((t, sin_array[i], label_sin[i]))
        
    return output_array

    
def plot_sin_list(sines:list, **kwargs):
    """Graphs many sines signals on a same plot

    Parameters
    ----------
    sines : list
        List composed for tuples for each frequency in the next order:
        (array time, array sine at f frequency, label of signal)  
    color: list, optional
        Color for each sine signal can be modified in respective order
    linestyle: list, optional
        Linestyle for each sine signal can be modified in respective order
    linewidth: list, optional
        Linewidth for each sine signal can be modified in respective order
    """
    options_plot = kwargs
    fig, ax = plt.subplots()
    ax.set_title('Plot Sines')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')
    i=0
    for sin in sines:
        ax.plot(sin[0], sin[1], label = sin[2], 
                color = options_plot['color'][i] if 'color' in options_plot else None,
                linestyle = options_plot['linestyle'][i] if 'linestyle' in options_plot else None,
                linewidth = options_plot['linewidth'][i] if 'linewidth' in options_plot else None
                )
        i=i+1
    
    ax.legend(loc='upper right')
    ax.grid()   
    plt.show()