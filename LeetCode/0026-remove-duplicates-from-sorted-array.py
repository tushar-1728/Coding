class Solution:
    def removeDuplicates(self, nums):
        i = 0
        curr = prev = None
        while(i < len(nums)):
            prev = curr
            curr = nums[i]
            if prev == curr:
                nums.pop(i)
            else:
                i += 1
        return i

b = Solution()
print(b.removeDuplicates([1,1,2,2,3,3,4,4]))