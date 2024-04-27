from math import log2
import numpy as np
from numpy.random import randint as randints


def v_sum( *vectors ):
    dim = len( vectors[0] )
    return ( sum(vector[i] for vector in vectors) for i in range(dim))


## HEAPIFY
'''
               81[0]
         89[1]         9[2]
     11[3]  14[4]   76[5]  54[6]
  22[7]
'''
def print_heap(heap_list: list) -> None:
    n = len(heap_list)
    height = int(log2(n))  
    
    index = 0
    for level in range(height+1):
        elements_in_level = 2**level
        for _ in range(elements_in_level):
            if index < n:
                width = 2**(height-level+1)
                print(f"{heap_list[index]:^{width}}", end='')
                index += 1
        print()
    print('_'*elements_in_level*2)

        
def HEAPIFY(A, i, i_stop, TEST=False):
    if TEST:
        print_heap(A[:i_stop])
        print()
    ## left(i) = i*2 + 1
    ## right(i) = i*2 + 2
    left_i = i*2 + 1
    right_i = i*2 + 2
    Largest = i
    
    if left_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][left_i]:
            Largest = left_i
    if right_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][right_i]:
            Largest = right_i
    if i != Largest:
        A[i], A[Largest] = A[Largest], A[i]
        HEAPIFY(A, Largest, i_stop)

    
def BUILD_HEAP(A, TEST=False):
    ## (2i+1 >= n) -> (i >= (n-1)/2) -> (i_x = floor( (n-1)/2 ) )
    for i in reversed( range( (len(A))//2 ) ):
        HEAPIFY(A, i, len(A), TEST)


def HEAP_SORT(A, TEST=False):
    BUILD_HEAP(A, TEST)
    for i in reversed( range(1, len(A)) ):
        A[0], A[i] = A[i], A[0]
        HEAPIFY(A, 0, i, TEST)

############## HEAP_SORT_PLUS ###################

def HEAPIFY_PLUS(A, i, i_stop):
    przyp=0
    por=0
    
    left_i = i*2 + 1
    right_i = i*2 + 2
    Largest = i
    
    if left_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][left_i]:
            Largest = left_i
    if right_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][right_i]:
            Largest = right_i
    por += 2
    if i != Largest:
        A[i], A[Largest] = A[Largest], A[i]
        przyp += 3  
        przyp, por = v_sum(
            HEAPIFY_PLUS(A, Largest, i_stop),
            (przyp, por)
            )

    return przyp, por

def BUILD_HEAP_PLUS(A):
    przyp = 0
    por = 0
    for i in reversed( range( (len(A))//2 ) ):
        przyp, por = v_sum(
            HEAPIFY_PLUS(A, i, len(A)),
            (przyp, por)
            )
        
    return przyp, por

def HEAP_SORT_PLUS(A):
    przyp, por = BUILD_HEAP_PLUS(A)
    for i in reversed( range(1, len(A)) ):
        A[0], A[i] = A[i], A[0]
        przyp += 3  
        przyp, por = v_sum(
            HEAPIFY_PLUS(A, 0, i),
            (przyp, por)
            )
    return przyp, por

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    przyp, por = HEAP_SORT_PLUS(A)
    print(A)



