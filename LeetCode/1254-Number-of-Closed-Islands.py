from typing import List
class Solution:
    def bfs(self, queue, grid):
        m = len(grid)
        n = len(grid[0])
        flag = 1
        while(queue):
            i, j = queue.pop(0)
            if(0 <= i < m and 0 <= j < n):
                if(grid[i][j] == 0):
                    grid[i][j] = 3
                    queue.extend([[i,j+1], [i,j-1],[i+1,j],[i-1,j]])
            else:
                flag = 0
        return flag


    def print_grid(self, grid):
        for i in grid:
            print(i)


    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    grid[i][j] = 3
                    queue = [[i,j+1], [i,j-1],[i+1,j],[i-1,j]]
                    count += self.bfs(queue, grid)
        return count


b = Solution()
print(b.closedIsland([[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]))