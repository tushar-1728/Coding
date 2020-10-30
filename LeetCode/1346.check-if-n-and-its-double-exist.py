#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
from typing import List
class Solution:
    def bin_src(self, arr, target, l, r):
        while l <= r:
            m = (l+r)//2
            if target == arr[m]:
                return m
            elif target < arr[m]:
                r = m-1
            else:
                l = m+1
        return -1

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(0, len(arr)):
            temp = self.bin_src(arr, arr[i]*2, 0, len(arr)-1)
            if temp != -1 and temp != i:
                return True
        return False
# @lc code=end

