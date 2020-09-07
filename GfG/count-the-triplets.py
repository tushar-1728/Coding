t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    d = dict()
    lst.sort()
    for j in range(n):
        d[lst[j]] = 1
    j = 0
    tot = lst[0]
    while j < n-1 and tot <= lst[-1]:
        j += 1
        tot = lst[0] + lst[j]
    # print(j)
    # print(d)
    # print(lst)
    for k in range(j):
        for l in range(k+1, j):
            tot = lst[k] + lst[l]
            if tot in d.keys():
                d[tot] += 1
    # print(d)
    count = 0
    for j in d.keys():
        count += d[j] - 1
    if count:
        print(count)
    else:
        print(-1)