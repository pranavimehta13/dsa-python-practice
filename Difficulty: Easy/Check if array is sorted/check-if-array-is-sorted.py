class Solution:
    def isSorted(self, arr) -> bool:
        flag = 0
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False