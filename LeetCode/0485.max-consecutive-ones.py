#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        if nums:
            temp = 0
            for i in nums:
                if i == 1:
                    temp += 1
                else:
                    count = max(temp, count)
                    temp = 0
            count = max(temp, count)
        return count
# @lc code=end

