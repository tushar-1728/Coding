class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        total = (n*(n-1))//2
        extra_total = sum(nums)
        return extra_total - total


b = Solution()
print(b.findDuplicate([1,3,4,2,2]))