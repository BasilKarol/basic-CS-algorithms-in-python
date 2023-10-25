import numpy as np
import random
import time
import sys

## zadanie 2
# n_length = int( input("Rozmiar tablicy (N): ") )
# A = []
# for index in range(n_length):
#     i_value = int( input(f"Podaj wartosc o indeksu {index}: ") )    
#     A.append(i_value)
# A = np.array(A)
# print(A)    


## zadanie 3
# file = sys.stdin
# data = list( map( float, file.readlines()[1:] ) )
# A = np.array(data)
# print(A)    


## zadanie 4 i 5
# n = 10**7
# start = time.time()
# pseudo_A = np.array( [random.randint(-100, 101) for _ in range(n) ] )
# end = time.time()
# time_result = round(end-start, 5)
# print(pseudo_A, time_result, 'sec')


## zadanie 6
def is_ascending(A):
    for index in range(0, len(A)-1):
        if A[index] > A[index+1]:
            return False
    return True


## zadanie 7
def my_max(A):
    maximum = A[0]
    for value in A:
        if maximum < value:
            maximum = value
    return maximum 

def my_min(A):
    minimum = A[0]
    for value in A:
        if minimum > value:
            minimum = value
    return minimum 

def my_sum(A):
    counter = 0
    for value in A:
        counter += value
    return counter  

# n = 10**6
# pseudo_A = np.array( [random.randint(-100, 101) for _ in range(n) ] )
def get_time(function):
    start = time.time()
    function(pseudo_A)
    end = time.time()
    time_result = round(end-start, 5)    
    print( f'time for {function} function: {time_result }' )

# function_list = [ (my_max, max), (my_min, min), (my_sum, sum) ]
# for my_func, python_func in function_list:
#     get_time(my_func)
#     get_time(python_func)
#     print()



## zadanie 8
my_list = [5, 8, 4, 7, 6, 2, 3]
# print(my_list)
def my_reverse(A):
    for index in range(0, int((len(A)-1)/2)+1 ):
        A[index], A[len(A)-index-1] = A[len(A)-index-1], A[index]
# my_reverse(my_list )
# print(my_list )
        








