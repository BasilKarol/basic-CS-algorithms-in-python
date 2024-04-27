from coin_changer import DYNAMIC_COIN_CHANGING, COIN_CHANGING

def GENERATE_FAIL(value):
    '''Dziala dla value >= 6 '''
    if value == 7:
        return [1, 3, 4, 5]
    a = 1
    b = value // 2
    c = int( value * (3/4) )  ## chyba b+2 tez zadziala
    return [a, b, c]

value = 13
coin_set = GENERATE_FAIL(value)
print(value, coin_set)

print( DYNAMIC_COIN_CHANGING( coin_set, value ) )
print( COIN_CHANGING( coin_set, value ) )


TEST = False
if TEST:
    for value in range(6, 10**3):
        gen_coins = GENERATE_FAIL(value)
        
        dp_len, dp_result = DYNAMIC_COIN_CHANGING( gen_coins, value )
        g_len, g_result = COIN_CHANGING( gen_coins, value )
        
        if dp_len == g_len:
            print('fffff')
            print(value, gen_coins)
            print(f"DP result: {str(dp_result): <10} ")
            print(f"GR result: {str(g_result): <10}\n")












