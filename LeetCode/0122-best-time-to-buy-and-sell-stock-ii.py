class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        profit = 0
        if n <= 1:
            return profit
        i = 0
        while i < (n-1):
            while i < n-1 and prices[i+1] <= prices[i]:
                i += 1
            buy = i
            while i < n-1 and prices[i+1] >= prices[i]:
                i += 1
            sell = i
            profit += (prices[sell] - prices[buy])
        return profit


b = Solution()
print(b.maxProfit([1,2]))
