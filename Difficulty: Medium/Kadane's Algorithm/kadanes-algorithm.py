class Solution:
    def maxSubarraySum(self, arr):
        n = len(arr)
        max_sum = float('-inf')
        total = 0
        for i in range(n):
            total = total + arr[i]
            max_sum = max(total, max_sum)
            if total < 0:
                total = 0
        return max_sum
            
        