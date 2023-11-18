from math import log2
import numpy as np
from numpy.random import randint as randints

'''
                   81[0]
        89[1]             9[2]            11[3]
11[4]  14[5] 76[6]   54[7]  22[8]

'''
def v_sum( *vectors ):
    dim = len( vectors[0] )
    return ( sum(vector[i] for vector in vectors) for i in range(dim))


def HEAPIFY3(A, i, i_stop):
    left_i = i*3 + 1
    middle_i = i*3 + 2
    right_i = i*3 + 3
    Largest = i

    if left_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][left_i]:
            Largest = left_i

    if middle_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][middle_i]:
            Largest = middle_i

    if right_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][right_i]:
            Largest = right_i

    if i != Largest:
        A[i], A[Largest] = A[Largest], A[i]
        HEAPIFY3(A, Largest, i_stop)

def BUILD_HEAP3(A):
    for i in reversed(range(len(A) // 3)):
        HEAPIFY3(A, i, len(A))

def HEAP_SORT3(A):
    BUILD_HEAP3(A)
    for i in reversed(range(1, len(A))):
        A[0], A[i] = A[i], A[0]
        HEAPIFY3(A, 0, i)


############## HEAP_SORT3_PLUS ###################

def HEAPIFY3_PLUS(A, i, i_stop):
    przyp=0
    por=0
    
    left_i = i*3 + 1
    middle_i = i*3 + 2
    right_i = i*3 + 3
    Largest = i

    if left_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][left_i]:
            Largest = left_i

    if middle_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][middle_i]:
            Largest = middle_i

    if right_i < len(A[:i_stop]):
        if A[:i_stop][Largest] < A[:i_stop][right_i]:
            Largest = right_i
    por += 3
    
    if i != Largest:
        A[i], A[Largest] = A[Largest], A[i]
        przyp += 3 
        przyp, por = v_sum(
            HEAPIFY3_PLUS(A, Largest, i_stop),
            (przyp, por)
            )
    return przyp, por

def BUILD_HEAP3_PLUS(A):
    przyp = 0
    por = 0
    for i in reversed(range(len(A) // 3)):
        przyp, por = v_sum(
            HEAPIFY3_PLUS(A, i, len(A)),
            (przyp, por)
            )
    return przyp, por

def HEAP_SORT3_PLUS(A):
    przyp, por = BUILD_HEAP3_PLUS(A)
    for i in reversed(range(1, len(A))):
        A[0], A[i] = A[i], A[0]
        przyp += 3  
        przyp, por = v_sum(
            HEAPIFY3_PLUS(A, 0, i),
            (przyp, por)
            )
    return przyp, por

if __name__ == "__main__":
    A = [81, 89, 9, 11, 14, 76, 54, 22]
    przyp, por = HEAP_SORT3_PLUS(A)
    print(A,  przyp, por)