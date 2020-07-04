t = int(input())
for i in range(t):
    t1 = int(input())
    t2 = list(map(int, input().split()))
    t3 = dict()
    t4 = 0
    for i in t2:
        if i in t3.keys():
            t3[i] += 1
        else:
            t3[i] = 1
    for i in t3.keys():
        t4 += (t3[i]//2)
    print(t4*2)