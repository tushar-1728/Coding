from typing import List
from functools import cmp_to_key
class largest_num_key(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if n > 0:
            res = "".join(sorted(map(str, nums), key=largest_num_key))
            return 0 if res[0] == 0 else res


b = Solution()
print(b.largestNumber([3,30,34,5,9]))
print(b.largestNumber([10,2]))