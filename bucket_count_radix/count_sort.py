def COUNTING_SORT(A):
    # Znajdujemy maximum A
    max_value = max(A)

    # Tworzymy liste B z samych zer (zaczynam od 0 i do max'a)
    B = [0] * (max_value + 1)

    # zapisanie ilosci elementow A w B
    for number in A:
        B[number] += 1

    # 'suma' w gore wszystkich elementow dla B:
    # dla A = [1, 3, 4, 3] B = [0, 1, 0, 2, 1] -> [0, 1, 1, 3, 4]
    for i in range(1, max_value + 1):
        B[i] += B[i - 1]

    # lista posortowana (pusta)
    A_out = [0] * len(A)

    for i in reversed( range( len(A) ) ):
        A_out[ B[ A[i] ] - 1] = A[i]
        B[ A[i] ] -= 1
        # print(A_out)
    return A_out