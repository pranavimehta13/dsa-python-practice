#User function Template for python3

class Solution:
    def isSorted(self, arr):
        n = len(arr)
        increasing = True
        decreasing = True
        for i in range(1,n):
            if arr[i]<=arr[i-1]:
                increasing = False
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                decreasing = False
        return increasing,decreasing
        
    def sortedCount(self,N,M,Mat):
        count = 0
        for i in range(N):
            increasing,decreasing = self.isSorted(Mat[i])
            if increasing == True or decreasing == True:
                count+=1
        return count
        