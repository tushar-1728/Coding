class Solution:
    def calc_profit(self, prices, l, r):
        if l >= r:
            return 0
        profit = 0
        for i in range(l, r):
            for j in range(i+1, r+1):
                if prices[j] > prices[i]:
                    curr_profit = prices[j] - prices[i] + self.calc_profit(prices, l, i-1) + self.calc_profit(prices, j+1, r)
                    profit = max(profit, curr_profit)
        return profit


    def maxProfit(self, prices):
        n = len(prices)
        profit = self.calc_profit(prices, 0, n-1)
        return profit


b = Solution()
print(b.maxProfit([]))
