class Solution:
    def lowerBound(self, arr, target):
        n = len(arr)
        lb = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upperBound(self, arr, target):
        n = len(arr)
        ub = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    
    def countFreq(self, arr, target):
        lb = self.lowerBound(arr, target)
        ub = self.upperBound(arr, target)
        if [ub,lb] == [-1,-1]:
            return 0
        if lb!=-1 and ub == -1:
            ub = len(arr)
        return ub - lb
        