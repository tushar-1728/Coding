n = int(input())
for i in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    t0 = sum(arr)
    t1 = t0//(t+1)
    for i in arr:
        print(i-t1, end=" ")
    print()