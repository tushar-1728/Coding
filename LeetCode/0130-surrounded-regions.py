# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
def check(i, j, n, m, board):
    flag = 0
    res = []
    result = []
    if(board[i][j] == "O"):
        flag = 1
        res.append((i,j))
    if(board[n-i-1][j] == "O"):
        flag = 1
        res.append((n-i-1,j))
    if(board[i][m-j-1] == "O"):
        flag = 1
        res.append((i,m-j-1))
    if(board[n-i-1][m-j-1] == "O"):
        flag = 1
        res.append((n-i-1,m-j-1))
    if(flag == 1):
        result.append(True)
        result.append(res)
    else:
        result.append(False)
    return result

def check2(ordinate, board, ind):
    i = ordinate[0]
    j = ordinate[1]
    n = len(board)
    m = len(board[0])
    if(i == 0):
        if(j == 0):
            if(board[i][j+1] == "O"):
                ind.append((i,j+1))
        elif(j == m-1):
            if(board[i][j-1] == "O"):
                ind.append((i,j-1))
        else:
            if(board[i][j+1] == "O"):
                ind.append((i,j-1))
            if(board[i][j-1] == "O"):
                ind.append((i,j-1))
        if(board[i+1][j] == "O"):
            ind.append((i+1,j))
    elif(j == 0):
        if(i != n-1):
            if(board[i+1][j] == "O"):
                ind.append((i+1,j))
        if(board[i][j+1] == "O"):
            ind.append((i,j+1))
        if(board[i-1][j] == "O"):
            ind.append((i-1,j))
    elif(i == n-1):
        if(j != m-1):
            if(board[i][j+1] == "O"):
                ind.append((i,j+1))
        if(board[i-1][j] == "O"):
            ind.append((i-1,j))
        if(board[i][j-1] == "O"):
            ind.append((i,j-1))
    elif(j == m-1):
        if(board[i+1][j] == "O"):
            ind.append((i+1,j))
        if(board[i-1][j] == "O"):
            ind.append((i-1,j))
        if(board[i][j-1] == "O"):
            ind.append((i,j-1))
    else:
        print(i,j)
        if(board[i+1][j] == "O"):
            ind.append((i+1,j))
        if(board[i-1][j] == "O"):
            ind.append((i-1,j))
        if(board[i][j-1] == "O"):
            ind.append((i,j-1))
        if(board[i][j+1] == "O"):
            ind.append((i,j+1))


board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","O","O","X"],
         ["X","O","X","X"]]
ind = []
n = len(board)
ilen = n//2
for i in range(n):
    m = len(board[i])
    jlen = m//2
    for j in range(m):
        if((i == 0 or j == 0 or i == n-1 or j == m-1) and board[i][j] == "O"):
            ind.append((i,j))

        # flag = check(i, j, n, m, board)
        # if(flag[0]):
        #     ordinates = flag[1]
        #     for i in ordinates:
        #         if(i[0] == 0 or i[0] == n-1 or i[1] == 0 or i[1] == m-1):
        #             ind.append(i)
for i in ind:
    check2(i, board, ind)

print(ind) 