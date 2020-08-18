t = int(input())
for _ in range(t):
    n = int(input())
    temp = ['!', '#', '$', '%', '&', '*', '@', '^', '~']
    res = []
    d = dict()
    lst1 = list(input().split())
    lst2 = list(input().split())
    for i in lst1:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in lst2:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in temp:
        if d.get(i, 0) == 2:
            res.append(i)
    print(*res)
    print(*res)