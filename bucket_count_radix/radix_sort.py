import numpy as np
from numpy.random import uniform as randfloats
from numpy.random import randint

'''
base = 10
pos = 2
        '3210'
number = 5682
then:
    
number //= 10**pos -> number = 56
number %= base -> number = 6
'''

def COUNTING_SORT(A, pos, max_value, base=10):
    # pos - pozycja w radix sort
    # Tworzymy liste B z samych zer (zaczynam od 0 i do max'a)
    B = [0] * base

    # zapisanie ilosci elementow A w B
    for number in A:
        number //= (base**pos)
        number %= base
        B[number] += 1

    # 'suma' w gore wszystkich elementow dla B:
    # dla A = [1, 3, 4, 3] B = [0, 1, 0, 2, 1] -> [0, 1, 1, 3, 4]
    for i in range(1, base):
        B[i] += B[i - 1]

    # lista posortowana (pusta)
    A_out = [0] * len(A)

    for number in reversed( A):
        n_base = number // (base**pos)
        n_base %= base
        
        A_out[ B[ n_base ] - 1] = number
        B[ n_base ] -= 1
        # print(A_out)
    
    for i in range( len(A) ):
        A[i] = A_out[i]
        
    return A

def RADIX_SORT(A, base=10):
    if A == []:
        return A
	# Znajdujemy maximum A
    max_value = max(A)
    # pos - potega bazy
    pos = 0
    while max_value // base**pos > 0:
        COUNTING_SORT(A, pos, max_value, base)
        # print(A)
        pos += 1
    


if __name__ == "__main__":
    # A = [170, 45, 75, 90, 802, 24, 2, 66]
    # A = [-1, 1]
    A = randint( 0, 2**63, 10**3, dtype=np.longlong )
    RADIX_SORT(A,10)
    # print(A)

