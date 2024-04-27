'''
 Zaimplementuj algorytm przydziału zajęć za pomocą 
 programowania dynamicznego.
'''
from math import inf
from generator import GENERATE

################ Programowanie Dynamiczne #####################
## https://www.techiedelight.com/activity-selection-problem-using-dynamic-programming/
def DP_ACTIVITY_SEARCH(s, f):
    activities = list( zip(s, f) )
    L = [[] for _ in range(len(activities))]
 
    for i in range(len(activities)):
        for j in range(i):
            start_i, finish_j = (activities[i][0], activities[j][1])
            if start_i >= finish_j and len(L[i]) < len(L[j]):
                L[i] = L[j].copy()
        L[i].append(activities[i])
        # print(L, '\n')
 
    return max(L, key=lambda l: len(l) ) 

gen_s = [31, 30, 71, 40, 23, 66, 55, 34, 100, 100]
gen_f = [49, 67, 73, 76, 79, 80, 83, 88, 101, 101, 0]
print( DP_ACTIVITY_SEARCH(gen_s, gen_f) )

##################### Rekurencja #################################
def REC_ACTIVITY_SEARCH(s, f, k=-1):
    m = k + 1
    n = len(s)-1
    while (m <= n) and (s[m] < f[k]): ## f[-1]==0
        m += 1
    if m <= n:
        print(m)
        return [m] + REC_ACTIVITY_SEARCH(s, f, m)
    else:
        return []

gen_s, gen_f = GENERATE(10)
" 'f_0 = 0' w pythonie to 'f[-1] = 0' "
result = REC_ACTIVITY_SEARCH(gen_s, gen_f+[0])
print(result)

##################### Iretacyjnie #################################
def ITER_ACTIVITY_SEARCH(s, f):
    n = len(s) - 1
    out = []
    k = -1
    m = 0
    
    while m <= n:
        m = k + 1
        while m <= n and s[m] < f[k]:
            m += 1
        if m <= n:
            out.append(m)
            k = m
        else:
            break

    return out


# for _ in range(10**3):
#     gen_s, gen_f = GENERATE(10)
    
#     result = ITER_ACTIVITY_SEARCH(gen_s, gen_f)
#     result_1 = [ (gen_s[i], gen_f[i]) for i in result ]
    
#     result = REC_ACTIVITY_SEARCH(gen_s, gen_f)
#     result_2 = [ (gen_s[i], gen_f[i]) for i in result ]
    
#     result_3 = DP_ACTIVITY_SEARCH( gen_s, gen_f )
    
#     if result_1 != result_3: #len(result_1) != len(result_3)
#         print(gen_s)
#         print(gen_f)
#         print()
#         print(len(result_1), result_1)
#         print(len(result_3), result_3)
#         break
    

# gen_s = [31, 30, 71, 40, 23, 66, 55, 34, 100, 100]
# gen_f = [49, 67, 73, 76, 79, 80, 83, 88, 101, 101, 0]

# result = ITER_ACTIVITY_SEARCH(gen_s, gen_f)
# result = [ (gen_s[i], gen_f[i]) for i in result ]
# print(result)

# result = REC_ACTIVITY_SEARCH(gen_s, gen_f)
# result = [ (gen_s[i], gen_f[i]) for i in result ]
# print(result)

# activities = list( zip( gen_s, gen_f ) )
# result = DP_ACTIVITY_SEARCH( activities )
# print(result)



