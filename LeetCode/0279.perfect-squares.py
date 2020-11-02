#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math, sys
class Solution:
    def numSquares(self, n: int) -> int:
        def helper(n, arr):
            if arr[n] != -1:
                return arr[n]
            else:
                if int(math.sqrt(n))**2 == n:
                    arr[n] = 1
                    return arr[n]
                else:
                    ans = sys.maxsize
                    i = 1
                    while i*i < n:
                        ans = min(ans, 1 + helper(n-i*i, arr))
                        i += 1
                    arr[n] = ans
                    return arr[n]
        
        arr = [-1] * (n+1)
        for i in range(min(4, n+1)):
            arr[i] = i
        return helper(n, arr)


# b = Solution()
# print(b.numSquares(3))
# print(b.numSquares(4))
# print(b.numSquares(75))
# print(b.numSquares(64))
# @lc code=end

