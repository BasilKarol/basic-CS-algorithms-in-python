import numpy as np
from numpy.random import randint as randints

def v_sum( *vectors ):
    dim = len( vectors[0] )
    return ( sum(vector[i] for vector in vectors) for i in range(dim))


def PARTITION3(A, p, k):    
    ## chce aby 'x' byl po lewej stronie, a 'y' po prawej
    if A[k] < A[k-1]:
        A[k], A[k-1] = A[k-1], A[k]
        
    x = A[k-1]
    y = A[k]
    
    i = p - 1
    for j_x in range(p, k-1):
        if A[j_x] <= x:
            i = i + 1
            A[i], A[j_x] = A[j_x], A[i]
    A[i + 1], A[k-1] = A[k-1], A[i + 1]
    i_x = i
    
    
    for j_y in range(i+1, k):
        if A[j_y] <= y:
            i = i + 1
            A[i], A[j_y] = A[j_y], A[i]
    A[i + 1], A[k] = A[k], A[i + 1]
    i_y = i
    
    return i_x+1, i_y+1

def QUICK_SORT3(A, p, k):
    if p < k:
        s_x, s_y = PARTITION3(A, p, k)
        ## A[s] juz jest prawidlowo ustawiony
        QUICK_SORT3(A, p, s_x - 1) 
        QUICK_SORT3(A, s_x + 1, s_y-1)
        QUICK_SORT3(A, s_y + 1, k)


########################### QUICK_SORT_PLUS ###############

def PARTITION3_PLUS(A, p, k):
    por=0
    przyp=0
    
    if A[k] < A[k-1]:
        A[k], A[k-1] = A[k-1], A[k]
        przyp += 3
    por += 1
        
    x = A[k-1]
    y = A[k]
    

    i = p - 1
    
    for j_x in range(p, k-1):
        por += 1
        if A[j_x] <= x:
            i = i + 1
            A[i], A[j_x] = A[j_x], A[i]
            przyp += 3
    A[i + 1], A[k-1] = A[k-1], A[i + 1]
    przyp += 3
    i_x = i
        
    for j_y in range(i+1, k):
        por += 1
        if A[j_y] <= y:
            i = i + 1
            A[i], A[j_y] = A[j_y], A[i]
            przyp += 3
    A[i + 1], A[k] = A[k], A[i + 1]
    przyp += 3
    i_y = i

    return i_x+1, i_y+1, por, przyp

def QUICK_SORT3_PLUS(A, p, k):
    por=0
    przyp=0
    if p < k:
        s_x, s_y, por, przyp = PARTITION3_PLUS(A, p, k)
        ## A[s] juz jest prawidlowo ustawiony
        por, przyp = v_sum(
            QUICK_SORT3_PLUS(A, p, s_x - 1),
            QUICK_SORT3_PLUS(A, s_x + 1, s_y-1),
            QUICK_SORT3_PLUS(A, s_y + 1, k),
            (por, przyp)
            )
    return por, przyp

if __name__ == "__main__":
    A = [81, 89, 9, 11, 14, 76, 54, 22]
    por, przyp = QUICK_SORT3_PLUS(A, 0, len(A)-1)
    print(A, por, przyp)








