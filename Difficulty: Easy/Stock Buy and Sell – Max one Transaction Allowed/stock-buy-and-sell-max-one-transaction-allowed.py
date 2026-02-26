class Solution:
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0
        minsofar = prices[0]
        n = len(prices)
        for i in range(n):
            sell = prices[i]
            profit = sell - minsofar
            minsofar = min(prices[i],minsofar)
            max_profit = max(profit,max_profit)
        return max_profit