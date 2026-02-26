class Solution:
    def findMedian(self, arr):
        n = len(arr)
        sorted_arr = sorted(arr)
        if n%2 == 1:
            median = sorted_arr[n//2]
        else:
            median = float((sorted_arr[n//2] + sorted_arr[(n//2)-1])/2)
        return median
            
