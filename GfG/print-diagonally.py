t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    if n == 1:
        print(*lst)
    else:
        matrix = []
        l = 0
        for j in range(n):
            matrix.append([])
            for k in range(n):
                matrix[j].append(lst[l])
                l += 1
        j, k = (0,0)
        res = []
        while k < n:
            res.append(matrix[j][k])
            if k == 0:
                k = j+1
                j = 0
            else:
                j += 1
                k -= 1
        j, k = (1, n-1)
        while j != n-1 or k != n-1:
            # print(j, k)
            res.append(matrix[j][k])
            if j == n-1:
                j = k+1
                k = n-1
            else:
                j += 1
                k -= 1
        res.append(matrix[n-1][n-1])
        print(*res)
