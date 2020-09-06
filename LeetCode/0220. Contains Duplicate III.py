from typing import List
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        lst = SortedList()
        for i in range(len(nums)):
            if i > k:
                lst.remove(nums[i-k-1])
            pos1 = lst.bisect_left(nums[i] - t)
            pos2 = lst.bisect_right(nums[i] + t)
            if(pos2 - pos1 > 0):
                return True
            lst.add(nums[i])
        return False


b = Solution()
print(b.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))