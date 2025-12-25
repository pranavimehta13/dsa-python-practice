class Solution:
    def reverseSubArray(self, arr, l, r):
        # convert to 0-based indexing
        l -= 1
        r -= 1
        
        self.helper(arr, l, r)
        return arr

    def helper(self, arr, l, r):
        if l >= r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        self.helper(arr, l + 1, r - 1)
