from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = count = 0
        for i in range(len(nums)):
            if(i == 0 or nums[i] > nums[i-1]):
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res


b = Solution()
print(b.findLengthOfLCIS([1,3,5,4,7]))