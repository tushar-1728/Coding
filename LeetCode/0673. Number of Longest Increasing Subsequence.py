from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = []
        max_len = res = 0
        count = [1] * len(nums)
        for i in range(len(nums)):
            dp.append([0] * len(nums))
            dp[i][i] = 1
            for j in range(i):
                if(nums[j] < nums[i]):
                    if(dp[i][i] == dp[j][j] + 1):
                        count[i] += count[j]
                    if(dp[i][i] < dp[j][j] + 1):
                        dp[i][i] = dp[j][j] + 1
                        count[i] = count[j]
            if(max_len == dp[i][i]):
                res += count[i]
            elif(max_len < dp[i][i]):
                max_len = dp[i][i]
                res = count[i]
        # print(dp)
        return res


b = Solution()
print(b.findNumberOfLIS([1,3,5,4,7,9]))