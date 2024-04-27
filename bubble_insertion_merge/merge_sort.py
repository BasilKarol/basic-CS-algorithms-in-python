import numpy as np
'''
idea: divide & conquer
visualization: 
    A = [3, 7, 2, 1] -> 
    [3, 7]      i     [2, 1] ->
    [3] i [7]        [2] i [1] ->
    [3, 7] i [1, 2] ->
    [1, 2, 3, 7]

Pseudocode:
    MERGE( A, p-start, s-middle, k-end ): 
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

def MERGE( A: list[int], p: int, s: int, k: int) -> None:
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

def MERGE_SORT(A: list[int], p=0, k=0, full_size=False) -> None:
    if full_size:
        p, k = 0, len(A)-1
    if p < k:
        # s = int( (p+k)/2 )
        s = int((k - p)/2) + p
        MERGE_SORT( A, p, s )
        MERGE_SORT( A, s+1, k )
        MERGE( A, p, s, k )
        
def v_sum(*vectors):
    a, b = 0, 0
    for aa, bb in vectors:
        a += aa
        b += bb
    return (a, b)

def MERGE_PLUS(A: list[int], p: int, k: int) -> None:
    comp, rewr = 0, 0
    L = A[p:s+1] 
    R = A[s+1:k+1] 
    L = np.append( L, np.inf )
    R = np.append( R, np.inf )
    
    i, j = 0, 0
    
    for l in range(p, k+1):        
        rewr += 1
        if L[i] <= R[j]:
            A[l] = L[i]
            i += 1
        else:
            A[l] = R[j]
            j += 1
        comp += 1
    return comp, rewr

def MERGE_SORT_PLUS(A: list[int], p=0, k=0, full_size=False) -> tuple[int, int]:
    if full_size:
        p, k = 0, len(A)-1
    if p < k:
        s = int((k - p)/3)*2 + p
        comp_1, rewr_1 = MERGE_SORT_PLUS( A, p, s )
        comp_2, rewr_2 = MERGE_SORT_PLUS( A, s+1, k )
        comp_3, rewr_3 = MERGE_PLUS( A, p, s, k )
        return v_sum( 
            (comp_1, rewr_1),
            (comp_2, rewr_2) ,
            (comp_3, rewr_3)
            )
    return 0, 0
