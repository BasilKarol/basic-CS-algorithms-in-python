import numpy as np
import time
from numpy.random import uniform as randfloats
from numpy.random import randint
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sns

from activity_selector import DP_ACTIVITY_SEARCH, REC_ACTIVITY_SEARCH, ITER_ACTIVITY_SEARCH
from generator import GENERATE

sns.set(style="whitegrid", context="notebook")

def get_time(function, A: list, *args) -> float:
    start = time.time()
    function(*A, *args)
    end = time.time()
    time_result = round(end-start, 5)    
    return time_result

def calculate_avg(sample_size, function, *args, stop=100, avg_number=10):
    ## 10 prob na kazdy rozmiar
    avg_time = 0
    for _ in range(avg_number):
        gen_s, gen_f = GENERATE(sample_size, stop)
        avg_time += get_time( function, [gen_s, gen_f], *args )
        
    avg_time /= avg_number
    return avg_time

SIZE_MAX = 10**4
STEP = SIZE_MAX // 10

############# activity_search test ############
algorytmy = [REC_ACTIVITY_SEARCH, ITER_ACTIVITY_SEARCH] ## DP_ACTIVITY_SEARCH
plt.xlabel('Rozmiar Dannych')
plt.ylabel('Czas')
plt.title( 'ITER_, DP_ i REC_ACTIVITY_SEARCH' )
    
for ALG in algorytmy:
    time_data = []
    
    label = str(ALG )[10:-23]        
    for size in tqdm( range( 1, SIZE_MAX+1, STEP ), label):
        avg_time = calculate_avg(size, ALG, stop=100, avg_number=20)
        time_data.append( avg_time )
    
    plt.plot( np.arange(0, SIZE_MAX, STEP) , time_data, label=label )
    plt.legend()

