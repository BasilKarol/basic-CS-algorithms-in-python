import numpy as np

'''
BUBBLE-SORT(A) Pseudocode:
    for i ← 1 to N − 1 do
        for j ← N downto i + 1 do
            if A[j] < A[j − 1] then
                swap A[j] with A[j − 1]
'''

def BUBBLE_SORT(A: list[int]) -> None:
    for i in range( len(A) ):
        for j in reversed( range( i+1, len(A) ) ):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] 

def BUBBLE_SORT_PLUS(A: list[int], full_size=True) -> tuple[int, int]:
    comp = 0
    comp = 0
    for i in range( len(A) ):
        for j in reversed( range( i+1, len(A) ) ):
            comp += 1
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j] 
                rewr += 3
    return comp, rewr
