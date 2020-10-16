#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for i in A:
            res.append(i*i)
        res.sort()
        return res
# @lc code=end

