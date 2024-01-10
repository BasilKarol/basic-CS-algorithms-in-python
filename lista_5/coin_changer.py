'''
## pseudocode:
idea COIN_CHANGING:
    Uzywamy algorytmu zachlannego
    Przechodimy sie po zestawie monet coin_list
    Np coin_list = [5, 2, 1, ...]
    Zaczynamy od 5, jak juz sie nie miesci - zmien na 2
'''
from math import inf

coin_list = [5, 2, 1]  ## nominaly[1..k]

################ Programowanie Dynamiczne ##########
## https://www.youtube.com/watch?v=x-QkFoh-i5Y&ab_channel=Geekific

def DYNAMIC_COIN_CHANGING(coins, value):
    coins = sorted( coins, reverse=True )
    
    if not coins or not coins[-1] or coins[-1] > value:
        return None
    
    coin_memo = [0] + [inf]*value 
    for coin in reversed(coins):
        for i in range(coin, value+1):
            ##zawsze poczynamy z coin-i = coin-coin = 0
            coin_memo[i] = min(coin_memo[i], coin_memo[i - coin] + 1)

    ## odtwarzanie 
    result = []
    while value > 0:
        for coin in coins:
            if value - coin >= 0 and coin_memo[value] == coin_memo[value - coin] + 1:
                result.append(coin)
                value -= coin
                break

    return len(result), result
# print( DYNAMIC_COIN_CHANGING( [15, 7, 1], 21 ) )

################ Programowanie Zachłanne ##########
def COIN_CHANGING(coins, value):
    coins = sorted( coins, reverse=True )
    result = []
 
    for coin in coins:
        while value >= coin:
            value -= coin
            result.append( coin )
    return len(result), result

## algorytm zachłanny nie znajduje optymalnego rozwiązania:
error_value = 21
error_coins = [15, 7, 1]  

my_out = COIN_CHANGING( error_coins, error_value )
perfect_out = DYNAMIC_COIN_CHANGING( error_coins, error_value )

# print( my_out, '!=', perfect_out )












