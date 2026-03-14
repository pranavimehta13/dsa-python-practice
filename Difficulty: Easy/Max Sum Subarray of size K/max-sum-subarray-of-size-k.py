class Solution:
    def maxSubarraySum(self, arr, k):
        sum = 0
        max_sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if i >= k:
                sum -= arr[i-k]
            if i >= k-1:
                max_sum = max(sum, max_sum)
        return max_sum
        
        