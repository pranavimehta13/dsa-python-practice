class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_profit = 0
        min_prize = float('inf')
        for i in range(n):
            min_prize = min(prices[i], min_prize)
            profit = prices[i] - min_prize
            max_profit = max(profit, max_profit)
        return max_profit