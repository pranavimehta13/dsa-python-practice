#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        if n == 0:
            return 0 
        return n**3 + self.sumOfSeries(n-1)