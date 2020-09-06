class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = []
        for i in range(n1+1):
            dp.append([0]*(n2+1))
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if(word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        res = n1 + n2 - 2*dp[n1][n2]
        return res


b = Solution()
print(b.minDistance("sea", "eat"))