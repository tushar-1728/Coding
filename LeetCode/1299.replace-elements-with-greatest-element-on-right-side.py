#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n >= 1:
            mval = arr[-1]
            arr[-1] = -1
            for i in range(n-2, -1, -1):
                temp = arr[i]
                arr[i] = mval
                if temp > mval:
                    mval = temp
        return arr
# @lc code=end

