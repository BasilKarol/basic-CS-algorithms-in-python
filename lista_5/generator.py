'''
Stwórz generator danych dla problemu przydziału zajęć. Dane, to
dwie tablice rozmiaru n. W tablicy s[1..n] zapisane są czasy rozpoczęcia 
zajęć, a w tablicy f[1..n] czasy ich zakończenia. Obie tablice mają 
składać się z nieujemnych liczb rzeczywistych, dodatkowo s[i]<f[i]. 
Posortuj dane względem tablicy f.
'''
from random import uniform as randfloat
from random import randint
from math import inf

def GENERATE(n, max_f=100, inf_zero=True):
    s, f = [], []
        
    for _ in range(n):
        s_i = randint(0, max_f)
        f_i = randint(s_i+1, max_f+1)
        s.append(s_i)
        f.append(f_i)
    s_f = sorted( zip( s, f ), key=lambda x: x[1] )
    s, f = zip( *s_f )
    return list(s), list(f)+[0]

# a = [('a', 1), ('b', 2), ('c', 3)]
# print( *list(zip(*a) ) )
    
gen_s, gen_f = GENERATE(10)
# print(gen_s)
# print(gen_f)






