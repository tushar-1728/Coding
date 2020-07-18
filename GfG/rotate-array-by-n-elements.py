t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    temp_lst = lst[:k:]
    lst = lst[k::] + temp_lst
    print(*lst)