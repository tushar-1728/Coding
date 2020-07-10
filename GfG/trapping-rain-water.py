t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    capacity = 0
    lmax = [0] * n
    rmax = [0] * n
    l_maximum = 0
    r_maximum = 0
    for i in range(n):
        if(arr[i] > l_maximum):
            l_maximum = arr[i]
        lmax[i] = l_maximum
        if arr[n-i-1] > r_maximum:
            r_maximum = arr[n-i-1]
        rmax[n-i-1] = r_maximum 
    maximum = 0
    for i in range(1, n-1):
        current_capacity = min(lmax[i], rmax[i]) - arr[i]
        capacity += current_capacity
    print(capacity)
