t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    if n == 1:
        print(*lst)
    else:
        matrix = []
        k = 0
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].insert(0, lst[k])
                k += 1
        # print(*matrix)
        for i in range(n):
            for j in range(n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = temp
        # print(*matrix)
        for i in matrix:
            print(*i)