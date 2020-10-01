from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        if n >= 1:
            d = dict()
            val = n // 3
            for i in nums:
                d[i] = d.get(i, 0) + 1
            for i in d.keys():
                if(d[i] > val):
                    res.append(i)
        return res


b = Solution()
print(b.majorityElement([3,2,3]))
print(b.majorityElement([1,1,1,3,3,2,2,2]))
