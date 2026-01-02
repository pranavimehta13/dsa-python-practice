class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1,-1,-1):
            for j in range(0,i+1):
                if arr[j] > arr[i]:
                    arr[i],arr[j] = arr[j],arr[i]
        return 