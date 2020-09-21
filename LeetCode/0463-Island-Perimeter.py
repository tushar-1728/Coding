from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if(m > 0):
            n = len(grid[0])
            island = 0
            neighbour = 0
            for i in range(m):
                for j in range(n):
                    if(grid[i][j] == 1):
                        island += 1
                        if(i < m-1 and grid[i+1][j] == 1):
                            neighbour += 1
                        if(j < n-1 and grid[i][j+1] == 1):
                            neighbour += 1
            return island*4 - neighbour*2

        