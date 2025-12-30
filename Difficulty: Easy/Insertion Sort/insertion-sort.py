class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        if n <= 1: return arr

        # Step 1: Find the minimum and move it to the front
        min_idx = 0
        for i in range(1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[0], arr[min_idx] = arr[min_idx], arr[0]

        # Step 2: Now we don't need to check "j >= 0"
        for i in range(2, n):
            key = arr[i]
            j = i - 1
            while arr[j] > key:  # No j >= 0 check needed!
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
            
                    
