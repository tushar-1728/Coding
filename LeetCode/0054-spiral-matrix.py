from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        res = []
        if m > 0:
            n = len(matrix[0])
            i = 0; j = n; k = m; l = 0
            # print("size", m, n)
            while i < k and l < j:
                # print("entry",i,j,k,l)
                for t in range(l, j):
                    # print(matrix[i][t], end=" ")
                    res.append(matrix[i][t])
                i += 1
                # print("var",i,j,k,l)
                if i < k and l < j:
                    for t in range(i, k):
                        # print(matrix[t][j-1], end=" ")
                        res.append(matrix[t][j-1])
                    j -= 1
                # print("var",i,j,k,l)
                if i < k and l < j:
                    for t in range(j-1, l-1, -1):
                        # print(matrix[k-1][t], end=" ")
                        res.append(matrix[k-1][t])
                    k -= 1
                # print("var",i,j,k,l)
                if i < k and l < j:
                    for t in range(k-1, i-1, -1):
                        # print(matrix[t][l], end=" ")
                        res.append(matrix[t][l])
                    l += 1
                # print("var",i,j,k,l)
            # print()
        return res


b = Solution()
print(b.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(b.spiralOrder([[1, 2, 3, 10],[4, 5, 6, 11], [7, 8, 9, 12]]))
print(b.spiralOrder([[1, 2, 3, 10],[4, 5, 6, 11], [7, 8, 9, 12],[13,14,15,16]]))
print(b.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[13,14,15]]))

