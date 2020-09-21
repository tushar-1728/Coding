from typing import List
class Solution:
    def bfs(self, grid, queue):
        m = len(grid)
        n = len(grid[0])
        while(queue):
            i, j = queue.pop(0)
            if(0 <= i < m and 0 <= j < n and grid[i][j] == "1"):
                grid[i][j] = "3"
                queue.extend([[i+1,j],[i-1,j],[i,j+1],[i,j-1]])
        return 1


    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if(m > 0):
            n = len(grid[0])
            count = 0
            for i in range(m):
                for j in range(n):
                    if(grid[i][j] == "1"):
                        grid[i][j] = "3"
                        queue = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
                        count += self.bfs(grid, queue)
            return count
        else:
            return 0


b = Solution()
print(b.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(b.numIslands([[]]))