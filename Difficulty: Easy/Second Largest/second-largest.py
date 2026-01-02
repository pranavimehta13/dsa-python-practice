class Solution:
    def getSecondLargest(self, arr):
        largest = max(arr)
        second_largest = -1
        for i in range(len(arr)):
            if arr[i] > second_largest and arr[i] != largest:
                second_largest = arr[i]
        return second_largest