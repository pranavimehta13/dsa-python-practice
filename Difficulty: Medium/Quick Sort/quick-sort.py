import random

class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            # 1. Randomized Pivot Selection
            random_idx = random.randint(low, high)
            arr[low], arr[random_idx] = arr[random_idx], arr[low]
            
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        
        while True:
            # Move i to the right as long as elements are smaller than pivot
            while i <= j and arr[i] <= pivot:
                i += 1
            # Move j to the left as long as elements are larger than pivot
            while i <= j and arr[j] >= pivot:
                j -= 1
            
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        
        # Final swap: put the pivot in its correct place
        arr[low], arr[j] = arr[j], arr[low]
        return j