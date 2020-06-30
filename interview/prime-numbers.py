def sieve(A):
    import math
    l = []
    res = []
    a = int(math.sqrt(A))
    for i in range(A+1):
        l.append(1)
    l[0] = 0
    l[1] = 0
    for i in range(a+1):
        if(l[i] == 1):
            for j in range(i+i, A+1, i):
                l[j] = 0
    for i in range(A+1):
        if(l[i] == 1):
            print(i, end=" ")
    print()

sieve(13)