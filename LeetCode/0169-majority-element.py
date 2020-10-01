from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict()
        max_count = 0
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0) + 1
        print(d)
        for i in d.keys():
            if d[i] > max_count:
                number = i
                max_count = d[i]
        return number

b = Solution()
print(b.majorityElement([5,6,6]))