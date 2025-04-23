class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(len(prices)):
            profit = max(profit, prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]

        return profit
