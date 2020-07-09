t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    list.sort(arr)
    print(arr[k-1])