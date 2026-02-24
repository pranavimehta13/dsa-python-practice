class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        hash_list = {}
        for i in range(n):
            hash_list[arr[i]] = arr[i]
        return list(hash_list.keys())