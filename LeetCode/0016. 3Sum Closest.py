from typing import List
from sys import maxsize
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        c_sum = maxsize
        nums.sort()
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = len(nums)-1
            while(l < r):
                temp = nums[i] + nums[l] + nums[r]
                temp = temp - target
                if(abs(temp) < c_sum):
                    c_sum = abs(temp)
                    res = nums[i] + nums[l] + nums[r]
                if(temp < 0):
                    l += 1
                elif(temp > 0):
                    r -= 1
                else:
                    l += 1
                    r -= 1
        return res


b = Solution()
print(b.threeSumClosest(nums = [-1,2,1,-4], target = 1))