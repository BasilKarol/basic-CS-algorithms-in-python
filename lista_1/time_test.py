import numpy as np
import time
from numpy.random import randint as randints

from insertion_sort import INSERTION_SORT, INSERTION_SORT_PLUS
from bubble_sort import BUBBLE_SORT, BUBBLE_SORT_PLUS
from merge_sort import MERGE_SORT, MERGE_SORT_PLUS
from merge_sort_21 import MERGE_SORT_21, MERGE_SORT_21_PLUS




def get_time(function, A, **func_args):
    start = time.time()
    porownania, przypisania = function(A, **func_args)
    end = time.time()
    time_result = round(end-start, 5)    
    return time_result, porownania, przypisania


function_list = [ INSERTION_SORT_PLUS, BUBBLE_SORT_PLUS,
                 MERGE_SORT_PLUS, MERGE_SORT_21_PLUS ]

## wiem ze przesadzilem.... ale trudno, przynajmniej (jakos) dziala
def get_time_matrix(function_list, TEST=False, sizes=[2, 3, 4]):
    time_matrix = []
    for size in sizes:
        size_matrix = [10**size]
        for my_func in function_list:
            name = str(my_func )[10:-23]
            func_matrix = [name]            
            A = randints( 1, 100, 10**size )
            time_result, porownania, przypisania = get_time(my_func, A, full_size=True)
            func_matrix.append(  [time_result, porownania, przypisania ] )
            size_matrix.append( func_matrix )
        time_matrix.append(  size_matrix  )
    if TEST:
        print(f"{time_result: <10}\t|\t{name: <20}|{porownania: <7}|{przypisania: <7}")
    return np.array( time_matrix, dtype=object ) 
    
# time_matrix = get_time_matrix(function_list)
# print(time_matrix )

        



