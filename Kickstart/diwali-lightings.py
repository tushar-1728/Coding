t = int(input())
for i in range(t):
    patt = input()
    s = len(patt)
    l,r = map(int, input().split())
    l -= 1
    lcount = 0
    rcount = 0
    for i in range(s):
        if(patt[i] == "B"):
            lcount += (l-(i+1))//s + 1
            rcount += (r-(i+1))//s + 1
    print(rcount-lcount)