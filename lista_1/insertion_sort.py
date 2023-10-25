##INSERTION-SORT
'''
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
'''
import numpy as np
from numpy.random import randint as randints

# A = randints( 1, 100, 10 )

## zadanie 1
def INSERTION_SORT( A ):
    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1
# print(A)
# INSERTION_SORT(A) 
# print( A )

## zadanie 2
def INSERTION_SORT_PLUS( A, full_size=True ):
    porownania = 0
    przypisania = 0
    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            porownania += 1
            A[j], A[j-1] = A[j-1], A[j]
            przypisania += 3
            j -= 1
        i += 1        
    return porownania, przypisania














