from math import log, sqrt
t = int(input())
for i in range(1, t+1):
    n = int(input())
    if n == 3:
        print("Case #", i, ": ", 2, sep="")
    else:
        arr1 = []
        arr2 = []
        temp_n = int(sqrt(n))
        flag = 0
        for j in range(1, temp_n):
            if (n-1)%j == 0:
                arr1.append(j)
                arr2.insert(0, (n-1)//j)
        if (n-1)%temp_n == 0:
            arr1.append(temp_n)
        arr1.pop(0)
        # print(arr1)
        # print(arr2)
        arr = arr1 + arr2
        # print(arr)
        for j in arr:
            temp = log(n*(j-1)+1, j)
            if temp%1 == 0:
                res = j
                break
        print("Case #", i, ": ", res, sep="")