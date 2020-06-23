def getSmallestDivNum(n):
    l = []
    for i in range(1, n+1):
        l.append(i)
    n = len(l)
    mul = 1
    for i in range(n):
        for j in range(i+1,n):
            if(l[j]%l[i] == 0):
                l[j] //= l[i]
        mul *= l[i]
    return mul


print(getSmallestDivNum(12))