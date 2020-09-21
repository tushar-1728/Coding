from typing import List
class Solution:
    def bfs(self, grid, queue):
        m = len(grid)
        n = len(grid[0])
        area = 1
        while(queue):
            i, j = queue.pop(0)
            if(0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                grid[i][j] = 3
                area += 1
                queue.extend([[i+1,j],[i-1,j],[i,j+1],[i,j-1]])
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if(m > 0):
            n = len(grid[0])
            area = 0
            for i in range(m):
                for j in range(n):
                    if(grid[i][j] == 1):
                        grid[i][j] = 3
                        queue = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
                        temp = self.bfs(grid, queue)
                        if(temp > area):
                            area = temp
            return area
        else:
            return 0


b = Solution()
print(b.maxAreaOfIsland([
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]
]))
print(b.maxAreaOfIsland([[0,0,1,1,0,1,0,0]]))
print(b.maxAreaOfIsland([[]]))