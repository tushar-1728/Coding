t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if (max(arr) == 0):
        print(0)
    else:
        print(len(set(arr)))