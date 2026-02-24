#User function Template for python3

class Solution:
    def findMean(self, arr):
        add = sum(arr)
        n = len(arr)
        mean = add//n
        return mean