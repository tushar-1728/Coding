t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = lst[::-1]
    print(*lst)