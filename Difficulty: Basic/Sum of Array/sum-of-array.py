#User function Template for python3
class Solution:
    def arraySum(self, arr):
        total = 0
        for i in range(len(arr)):
            total = total + arr[i]
        return total
