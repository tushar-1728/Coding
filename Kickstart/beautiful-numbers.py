from math import log
t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = []
    narr = []
    for i in range(1, n):
        if n%i == 1:
            arr.append(i)
    for i in arr:
        temp = log(n*(i-1)+1, i)
        # if temp%1 == 0:
        #     narr.append(temp)
    print(arr)
    print(narr)