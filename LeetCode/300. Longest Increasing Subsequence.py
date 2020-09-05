from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        res = 0
        for i in range(len(nums)):
            dp.append([0]*len(nums))
            dp[i][i] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if(nums[j] < nums[i]):
                    dp[i][i] = max(dp[i][i], dp[j][j]+1)
            res = max(res, dp[i][i])
        return res


b = Solution()
print(b.lengthOfLIS([10,9,2,5,3,7,101,18]))