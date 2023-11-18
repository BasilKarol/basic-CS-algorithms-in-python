import numpy as np
from numpy.random import randint as randints

def v_sum( *vectors ):
    dim = len( vectors[0] )
    return ( sum(vector[i] for vector in vectors) for i in range(dim))


def PARTITION(A, p, k):
    x = A[k]
    i = p - 1

    for j in range(p, k):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[k] = A[k], A[i + 1]
    return i + 1

def QUICK_SORT(A, p, k):
    if p < k:
        s = PARTITION(A, p, k)
        ## A[s] juz jest prawidlowo ustawiony
        QUICK_SORT(A, p, s - 1) 
        QUICK_SORT(A, s + 1, k)


########################### QUICK_SORT_PLUS ###############
def PARTITION_PLUS(A, p, k):
    por=0
    przyp=0
    x = A[k]
    i = p - 1
    
    for j in range(p, k):
        por += 1
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            przyp += 3
    A[i + 1], A[k] = A[k], A[i + 1]
    przyp += 3
    return i + 1, por, przyp

def QUICK_SORT_PLUS(A, p, k):
    por=0
    przyp=0
    if p < k:
        s, por, przyp = PARTITION_PLUS(A, p, k)
        ## A[s] juz jest prawidlowo ustawiony
        por, przyp = v_sum(
            QUICK_SORT_PLUS(A, p, s - 1), 
            QUICK_SORT_PLUS(A, s + 1, k),
            (por, przyp )
            )
    return por, przyp

if __name__ == "__main__":
    A = [81, 89, 9, 11, 14, 76, 54, 22]
    por, przyp = QUICK_SORT_PLUS(A, 0, len(A)-1)
    print(A, por, przyp)








