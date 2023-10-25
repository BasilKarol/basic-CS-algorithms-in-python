## MERGE-SORT
'''
idea: 
    1) podziel tablicę A na dwie częsci (+-równe)
    2) posortuj każdą (rekurencja) 
    3) scal posortowane kawałki

wizualizacja: 
    A = [3, 7, 2, 1] -> 
    [3, 7]      i     [2, 1] ->
    [3] i [7]        [2] i [1] ->
    [3, 7] i [1, 2] ->
    ## porownujemy najmniejsze elemente
    ## czyli najpierw 3 i 1, potem 3 i 2
    [1, 2, 3, 7]

pseudo-code:
    MERGE( A-tablica, p-początek, s-srodek, k-koniec ): 
        ## A[p:s]=L i A[s+1:k]=R są posortowane
        ## n1 = len(L) = p-k+1 oraz n2 = len(R) = k-s
        
        for i <- 1 to n1:
            L[i] <- A[p+i-1]
        for j <- 1 to n2:
            R[j] <- A[s+j]
        L[n1+1] <- inf
        R[n2+1] <- inf
        
        i <- 1
        j <- 1
        for l <- p to k:
            if L[i] <= R[j] then:
                A[l] <- L[i]
                i <- i + 1
            else:
                A[l] <- R[j]
                j <- j + 1
    
    MERGE-SORT(A, p, k):
        if p < k then:
            s = ceil( (p+k)/2 )
            MERGE-SORT( A, p, s )
            MERGE-SORT( A, s+1, k )
            MERGE( A, p, s, k )
'''

import numpy as np
from numpy.random import randint as randints

def MERGE( A, p, s, k): 
    ## A[p:s]=L i A[s+1:k]=R są posortowane
    ## n1 = len(L) = p-k+1 oraz n2 = len(R) = k-s
    L = A[p:s+1] 
    R = A[s+1:k+1] 
    L = np.append( L, np.inf )
    R = np.append( R, np.inf )
    
    i = 0
    j = 0
    for l in range(p, k+1):            
        if L[i] <= R[j]:
            A[l] = L[i]
            i += 1
        else:
            A[l] = R[j]
            j += 1

def MERGE_SORT(A, p=0, k=0, full_size=False):
    if full_size:
        p, k = 0, len(A)-1
    if p < k:
        # s = int( (p+k)/2 )
        s = int((k - p)/2) + p
        MERGE_SORT( A, p, s )
        MERGE_SORT( A, s+1, k )
        MERGE( A, p, s, k )
        
# A = randints( 1, 100, 10 )
# MERGE_SORT( A, full_size=True)
# print(A)



def v_sum(*vectors):
    a, b = 0, 0
    for aa, bb in vectors:
        a += aa
        b += bb
    return (a, b)
        
def MERGE_PLUS( A, p, s, k): 
    porownania, przypisania = 0, 0
    ## A[p:s]=L i A[s+1:k]=R są posortowane
    ## n1 = len(L) = p-k+1 oraz n2 = len(R) = k-s
    # print( porownania, przypisania)
    L = A[p:s+1] 
    R = A[s+1:k+1] 
    L = np.append( L, np.inf )
    R = np.append( R, np.inf )
    
    i, j = 0, 0
    
    for l in range(p, k+1):        
        przypisania += 1
        if L[i] <= R[j]:
            A[l] = L[i]
            i += 1
        else:
            A[l] = R[j]
            j += 1
        porownania += 1
    return porownania, przypisania

def MERGE_SORT_PLUS(A, p=0, k=0, full_size=False):
    if full_size:
        p, k = 0, len(A)-1
    if p < k:
        s = int( (p+k)/2 )
        porownania_1, przypisania_1 = MERGE_SORT_PLUS( A, p, s )
        porownania_2, przypisania_2 = MERGE_SORT_PLUS( A, s+1, k )
        porownania_3, przypisania_3 = MERGE_PLUS( A, p, s, k )
        return v_sum( 
           ( porownania_1, przypisania_1),
            (porownania_2, przypisania_2) ,
            (porownania_3,przypisania_3)
            )
    return 0, 0

# A = randints( 1, 100, 10)
# print( MERGE_SORT_PLUS( A, 0, len(A)-1 ) )
# print(A)









