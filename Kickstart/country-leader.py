n = int(input())
for _ in range(n):
    names = []
    t = int(input())
    for i in range(t):
        name = input()
        names.append(name)
    d = dict()
    res = []
    maxl = 0
    for i in range(len(names)):
        temp = set(names[i]) - set(" ")
        temp = len(temp)
        d[i] = temp
        if temp > maxl:
            maxl = temp
    for i in range(len(names)):
        if d[i] == maxl:
            res.append(names[i])
    res.sort()
    print("Case #%d: %s" %(_+1, res[0]))