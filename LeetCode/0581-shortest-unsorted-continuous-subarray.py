from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = n
        end = 0
        if n > 1:
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    if end < i:
                        end = i
                    while i > 0 and nums[i] < nums[i-1]:
                        nums[i-1], nums[i] = nums[i], nums[i-1]
                        i -= 1
                        # print("apple")
                    if start > i:
                        start = i
                # print(nums)
            # print(end, start)
        return max(end - start + 1, 0)

b = Solution()
# print(b.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
# print(b.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 1]))
# print(b.findUnsortedSubarray([2, 1, 7]))
print(b.findUnsortedSubarray([1,3,5,2,4]))
