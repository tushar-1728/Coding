t = int(input())
for i in range(t):
    pattern = input()
    lindex, rindex = map(int, input().split())
    d = len(pattern)
    a_list = []
    r_count = 0
    l_count = 0
    flag = 0
    for j in range(d):
        if pattern[j] == "B":
            a_list.append(j +1)
    for j in a_list:
        temp = (rindex - j)//d + 1
        r_count += temp
        temp = (lindex - j)//d + 1
        l_count += temp
        if (lindex - j) % d == 0:
            flag = 1
    print("Case #", i+1, ": ", r_count - l_count + flag, sep="")
