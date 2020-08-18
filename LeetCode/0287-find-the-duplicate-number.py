class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        temp = [0] * n
        for i in nums:
            temp[i] += 1
            if temp[i] > 1:
                return i


b = Solution()
print(b.findDuplicate([1,3,4,2,2]))