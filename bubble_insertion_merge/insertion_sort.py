import numpy as np
from numpy.random import randint as randints

'''
INSERTION-SORT(A) Pseudocode:
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

def INSERTION_SORT(A: list[int]) -> None:
    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
        i += 1

def INSERTION_SORT_PLUS( A: list[int], full_size=True ) -> tuple[int, int]:
    comp = 0
    rewr = 0
    i = 0
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            comp += 1
            A[j], A[j-1] = A[j-1], A[j]
            rewr += 3
            j -= 1
        i += 1        
    return comp, rewr














