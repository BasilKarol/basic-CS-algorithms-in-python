from generator import GENERATE
from activity_selector import REC_ACTIVITY_SEARCH
from random import randint
'''
## pseudocode:
    len(s), len(f) = n
    f = sorted(f)
    
def GREEDY_ACTIVITY_SELECTOR(s, f):
    A = {1}
    m = 1
    for k in range(2, n+1):
        if s[k] >= f[m]:
            A = A 'sum' {k}
            m = k
    return A
'''
 
def GREEDY_ACTIVITY_SELECTOR(s, f):
    A = {0}
    m = 0
    n = len(s)
    
    for k in range(1, n):
        if s[k] >= f[m]:
            A = A | {k}
            m = k
    return A

gen_s, gen_f = GENERATE(10)
# print(gen_s)
# print(gen_f)

'''
## BF Testing :))
while_n = 0
while while_n < 10**4:
    while_n += 1
    
    n = randint(0, 10**3)
    max_f = randint(1, 10**4)
    gen_s, gen_f = GENERATE(n, max_f)
    
    g_list = GREEDY_ACTIVITY_SELECTOR( gen_s, gen_f )
    r_list = set( REC_ACTIVITY_SEARCH( gen_s, gen_f+[0] ) )
    if g_list != r_list:
        print( g_list, r_list )
print('ok')
'''
# list_answer = GREEDY_ACTIVITY_SELECTOR( gen_s, gen_f )
# print( list_answer )
















