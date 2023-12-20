from math import inf
from random import randint

def GENERATOR(length=10):
    return sorted( [randint(1, 20) for _ in range(length)] )

########################## MEMORIZED_CUT_ROD ################
def CUT_ROD_AUX(n, r, n_len):
    if r[n_len-1] >= 0:
        return r[n_len-1]
    if n_len == 0:
        return 0
    
    q = -inf
    for i in range(n_len):
        q = max( (q, n[i] + CUT_ROD_AUX(n, r, n_len-1-i) ) )
    ## zapamietywanie wartosci:
    r[n_len-1] = q
    return q

def MEMORIZED_CUT_ROD(n, n_len):
    r = [-inf]* n_len
    return CUT_ROD_AUX(n, r, n_len)



########################## ITER_CUT_ROD ############

def ITER_CUT_ROD(n, n_len):
    r = [0]*(n_len+1)
    
    for j in range(n_len):
        q = -inf
        for i in range(j): # +1
            q = max( (q, n[i] + r[j-i]) )
        r[j] = q
    return r[n_len]


################### EXT & PRINT #############

def EXT_CUT_ROD(n, n_len):
    s = [0]*n_len
    r = [0]*(n_len+1)
    for j in range(n_len):
        q = -inf
        for i in range(j): # +1
            if q < n[i] + r[j-i]:
                q = n[i] + r[j-i]
                s[j-1] = i
            r[j] = q
    return r[1:], s

def PRINT_SOLUTION(n, n_len):
    r,s = EXT_CUT_ROD(n, n_len)
    while n_len > 0:
        print( s[n_len-1] )
        n_len -= s[n_len-1] 
        break
        
    
    

# Przykład użycia
price_list = [1, 5, 8, 9, 10, 17, 17, 20] #GENERATOR()
print("Ceny kawałków pręta:", price_list)

max_value = ITER_CUT_ROD(price_list, len(price_list)) ##  MEMORIZED_CUT_ROD
print("Maksymalna wartość:", max_value)

# optimal_solution = EXT_CUT_ROD(price_list, len(price_list) )
# print("Optymalne rozwiązanie:", optimal_solution)
# PRINT_SOLUTION(price_list, len(price_list))
