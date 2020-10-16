#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        if nums:
            for i in nums:
                length = len(str(i))
                if length%2 == 0:
                    count += 1
        return count
# @lc code=end

