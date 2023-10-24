##BUBBLR-SORT

import numpy as np
from numpy.random import randint as randints


'''
BUBBLESORT(A)
    for i ← 1 to N − 1 do
        for j ← N downto i + 1 do
            if A[j] < A[j − 1] then
                zamień A[j] z A[j − 1]
'''

def BUBBLE_SORT(A):
    for i in range( len(A) ):
        for j in reversed( range( i+1, len(A) ) ):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] ##3 zamiany

# A = randints( 1, 100, 10 )
# BUBBLE_SORT( A )
# print(A)

# for _ in range(10**4):    
#     A = randints( 1, 100, 10 )
#     B = A.copy()
#     BUBBLE_SORT( A )
#     B.sort()
#     if not np.array_equal(A, B):
#         print('Uff')

def BUBBLE_SORT_PLUS(A):
    porownania = 0
    przypisania = 0
    for i in range( len(A) ):
        for j in reversed( range( i+1, len(A) ) ):
            porownania += 1
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] ##3 zamiany
                przypisania += 3
    return porownania, przypisania


