from math import inf
from random import randint

def NAIVE_CUT_ROD(n, n_len):
    if n_len == 0:
        return 0
    q = -inf
    for i in range(n_len):
        q = max( (q, n[i]+ NAIVE_CUT_ROD(n, n_len-1-i) ) )
    return q


def GENERATOR(length=10):
    return sorted( [randint(1, 20) for _ in range(length)] )


price_list = [1, 5, 8, 9, 10, 17, 17, 20] #GENERATOR(10)
print("Ceny kawałków pręta:", price_list)
print("Maksymalna wartość:", NAIVE_CUT_ROD(price_list, len(price_list) ) )

'''
Z wykładu:
Algorytm NAIVE_CUT_ROD ma złożoność czasową O(2^n)
Więc dla turbo malych dannycj wejsciowych jeszcze dziala ok (n_len ~< 9-10)
'''






