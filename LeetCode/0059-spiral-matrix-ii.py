from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        lst = []
        if n > 0:
            element = 1
            for i in range(n):
                lst.append([0]*n)
            i = 0; j = n; k = n; l = 0;
            while i < k and l < j:
                for t in range(l, j):
                    lst[i][t] = element
                    element += 1
                i += 1
                if i < k and l < j:
                    for t in range(i, k):
                        lst[t][j-1] = element
                        element += 1
                    j -= 1
                if i < k and l < j:
                    for t in range(j-1, l-1, -1):
                        lst[k-1][t] = element
                        element += 1
                    k -= 1
                if i < k and l < j:
                    for t in range(k-1, i-1, -1):
                        lst[t][l] = element
                        element += 1
                    l += 1
        return lst

b = Solution()
print(b.generateMatrix(3))