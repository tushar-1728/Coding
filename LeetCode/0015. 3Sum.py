from typing import List
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            lindex = i+1
            rindex = len(nums) - 1
            while(lindex < rindex):
                temp = nums[i] + nums[lindex] + nums[rindex]
                if(temp < 0):
                    lindex += 1
                elif(temp > 0):
                    rindex -= 1
                else:
                    res.append([nums[i], nums[lindex], nums[rindex]])
                    while(lindex < rindex and nums[lindex] == nums[lindex+1]):
                        lindex += 1
                    while(lindex < rindex and nums[rindex] == nums[rindex-1]):
                        rindex -= 1
        return res


b = Solution()
print(b.threeSum([0,0,0]))