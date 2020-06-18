class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ind = []
        ilen = len(board)
        for i in range(ilen):
        	jlen = len(board[i])
        	for j in range(jlen):
        		if((i == 0 or j == 0 or i == ilen or j == jlen) and board[i][j] == "o"):
        			ind.append((i,j))
        		else:
        			

        