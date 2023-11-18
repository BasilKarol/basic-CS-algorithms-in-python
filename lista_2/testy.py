import numpy as np
import time
from numpy.random import uniform as randfloats
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sns

## algorytmy:
from heap_sort import HEAP_SORT_PLUS
from heap_sort_3 import HEAP_SORT3_PLUS
from quick_sort import QUICK_SORT_PLUS
from quick_sort_3 import QUICK_SORT3_PLUS

sns.set(style="whitegrid", context="notebook")

def get_time(function, A, size_args=False):
    start = time.time()
    
    if size_args:
        porownania, przypisania = function(A, 0, len(A)-1)
    else:
        porownania, przypisania = function(A)
    end = time.time()
    time_result = round(end-start, 5)    
    return time_result, porownania, przypisania


function_list = [ (HEAP_SORT_PLUS, False), (HEAP_SORT3_PLUS, False),
                 (QUICK_SORT_PLUS, True), (QUICK_SORT3_PLUS, True) ]

## zależności czasu, liczy porównań, liczby przypisań 
##          od wielkości danych

N_MAX = 7
n_size = [ 10**n for n in range(3, N_MAX) ]
labels = [ f'10**{n}' for n in range(3, N_MAX) ]
print(n_size)

plot_data = {}
for algorytm, arg in function_list:
    name = str(algorytm )[10:-23]
    # print(f"\n\t{name}:")
    time_list, por_list, przyp_list = [], [], []
    for size in tqdm(n_size, f"{name} progress"):
        A = randfloats(0, 1000, size )
        time_result, por, przyp = get_time( algorytm, A, arg )
        time_list.append( time_result )
        por_list.append( por )
        przyp_list.append( przyp )
        # print(f"{time_result} | {por} | {przyp}")
    plot_data[name] = [ (time_list, 'Czas (s)', 'red'), 
                       (por_list, 'Porownania', 'lawngreen'),
                       (przyp_list, 'Przypisania', 'dodgerblue')]
# print( plot_data )

for title, data in plot_data.items():
    plt.figure(figsize=(15, 15))
    i = 0
    for values, value_label, color in data:
        i+= 1
        plt.subplot(3, 1, i)
        plt.plot(labels, values, color=color)
        
        plt.xlabel('Rozmiar Dannych')
        plt.ylabel(value_label)
        plt.title(title)
        
    plt.savefig(f'PLOTS/{title}_performance.pdf')
    plt.show()
    plt.close()









