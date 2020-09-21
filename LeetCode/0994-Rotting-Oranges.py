from typing import List
class Solution:
    def bfs(self, grid, queue):
        count = 0
        m = len(grid)
        n = len(grid[0])
        while(len(queue) > 1):
            temp = queue.pop(0)
            if(temp == "$"):
                count += 1
                queue.append("$")
            else:
                i, j = temp
                if(0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                    grid[i][j] = 2
                    queue.extend([[i+1,j], [i-1,j], [i,j-1], [i,j+1]])
        return count    


    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # count = 0
        queue = []
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    queue.extend([[i+1,j], [i-1,j], [i,j-1], [i,j+1]])
        if(len(queue) != 0):
            queue.append("$")
        # print(queue)
        count = self.bfs(grid, queue)
        # print(grid)
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    return -1
        return count
        # print(count)


b = Solution()
print(b.orangesRotting([[2,1,0,1],[1,1,0,1],[0,0,0,1],[1,1,1,1]]))