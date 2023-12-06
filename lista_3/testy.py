import numpy as np
import time
from numpy.random import uniform as randfloats
from numpy.random import randint
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sns

from radix_sort import RADIX_SORT
from bucket_sort import BUCKET_SORT
from archive.heap_sort import HEAP_SORT
from archive.quick_sort import QUICK_SORT_test

sns.set(style="whitegrid", context="notebook")

def get_time(function, A: list, *args) -> float:
    start = time.time()
    function(A, *args)
    end = time.time()
    time_result = round(end-start, 5)    
    return time_result

def calculate_avg(sample_size, function, *args, start=0, stop=1, 
                  sample_type=float, avg_number=10):
    ## 10 prob na kazdy rozmiar
    avg_time = 0
    for _ in range(avg_number):
        if sample_type is float:
            A = randfloats( start, stop, sample_size )
        elif sample_type is int:
            A = randint( start, stop, sample_size )
        else:
            raise TypeError
        avg_time += get_time( function, A, *args )
    avg_time /= avg_number
    return avg_time

SIZE_MAX = 10**5
STEP = SIZE_MAX // 10

############# bucket_sort test ############
algorytmy = [HEAP_SORT, QUICK_SORT_test, BUCKET_SORT]
plt.xlabel('Rozmiar Dannych')
plt.ylabel('Czas')
plt.title( 'HEAP_, QUICK_ i BUCKET_SORT' )
    
for ALG in algorytmy:
    time_data = []
    
    label = str(ALG )[10:-23]        
    for size in tqdm( range( 1, SIZE_MAX+1, STEP ), label):
        avg_time = calculate_avg(size, ALG)
        time_data.append( avg_time )
    
    plt.plot( np.arange(0, SIZE_MAX, STEP) , time_data, label=label )
    plt.legend()

############# radix_sort test ############

# bases = [2, 4, 7, 10, 16]
# plt.xlabel('Rozmiar Dannych')
# plt.ylabel('Czas')
# plt.title( str(RADIX_SORT )[10:-23] )
    
# for base in bases:
#     time_data = []
    
#     title = f"podstawa {base}"
#     for size in tqdm( range( 1, SIZE_MAX+1, STEP ), title):
#         avg_time = calculate_avg(size, RADIX_SORT, base, start=0, stop=10**3, 
#                                  sample_type=int)
#         time_data.append( avg_time )
    
#     plt.plot( np.arange(0, SIZE_MAX, STEP) , time_data, label=title )
#     plt.legend()