class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res

nums = [2,5,1,3,4,7]
n = 3
b = Solution()
print(b.shuffle(nums, n))