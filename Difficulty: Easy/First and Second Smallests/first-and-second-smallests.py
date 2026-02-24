class Solution:
    def minAnd2ndMin(self, arr):
        smallest = arr[0]
        second_smallest = float('inf')

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                second_smallest = smallest   # save old smallest first
                smallest = arr[i]
            if arr[i] != smallest and arr[i] < second_smallest:
                second_smallest = arr[i]

        if second_smallest == float('inf') or second_smallest == smallest:
            return [-1]
        return smallest, second_smallest