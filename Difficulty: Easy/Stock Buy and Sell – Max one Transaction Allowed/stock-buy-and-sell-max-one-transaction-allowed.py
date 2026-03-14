class Solution:
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0
        min_sofar = prices[0]
        for i in range(len(prices)):
            sell = prices[i]
            min_sofar = min(prices[i], min_sofar)
            profit = sell - min_sofar
            max_profit = max(profit, max_profit)
        return max_profit