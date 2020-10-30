#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        temp = list(arr)
        i = 0
        while i < len(temp):
            if temp[i] == 0:
                temp.insert(i, 0)
                i += 2
            else:
                i += 1
        for i in range(n):
            arr[i] = temp[i]
                
# @lc code=end

