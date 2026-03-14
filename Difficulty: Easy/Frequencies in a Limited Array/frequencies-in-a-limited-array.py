class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        hash_list = [0]*n
        for num in arr:
            if num <= n:
                hash_list[num-1] += 1
        return hash_list