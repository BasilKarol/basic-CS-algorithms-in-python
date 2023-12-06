from archive.insertion_sort import INSERTION_SORT


def BUCKET_SORT(A):
    ## wiadra ilosci dlugosci listy A
    buckets = [[] for _ in range(len(A))]
    
    ## wypelniamy wiadro
    for number in A:
        index = int(number * len(A))
        buckets[index].append(number)
    
    ## sortujemy wiadra
    for bucket in buckets:
        INSERTION_SORT( bucket )
    
    A_out = [item for bucket in buckets for item in bucket]
    
    return A_out

if __name__ == "__main__":
    A = [0.99, 0, 0.5]
    print(BUCKET_SORT(A) )








