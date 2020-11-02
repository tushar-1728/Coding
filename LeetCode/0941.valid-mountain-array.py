#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
from typing import List
class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n >= 3:
            i = 0
            while i < n-1 and nums[i] < nums[i+1]:
                i += 1
            if i == n-1 or i == 0:
                return False
            while i < n-1 and nums[i] > nums[i+1]:
                i += 1
            if i == n-1:
                return True
        return False

# @lc code=end

