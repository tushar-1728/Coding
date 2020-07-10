import math  

def findTriplet(arr, n):
    flag = 0
    for i in range(n): 
        arr[i] = arr[i] * arr[i] 
    arr.sort() 

    for i in range(n-1, 1, -1):   # fix a
        b = 0                       # fix b
        c = i - 1                   # fix c
        while (b < c): 
            if (arr[b] + arr[c] == arr[i]): 
                flag = 1
                b+=1
                c-=1
            else: 
                if (arr[b] + arr[c] < arr[i]): 
                    b = b + 1
                else: 
                    c = c - 1
    if flag == 1:
        print("Yes")
    else:
        print("No")
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    findTriplet(arr, n)
    