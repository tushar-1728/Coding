t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split(" ")))
    d = {}
    maxi = 0
    for j in lst:
       if (j > maxi):
           maxi = j
       d[j] = d.get(j, 0) + 1
    for k in d.keys():
       temp = k + d[k] - 1
       if (temp > maxi):
           maxi = temp
    print(maxi)