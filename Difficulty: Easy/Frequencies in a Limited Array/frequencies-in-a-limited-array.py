class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        hash_list = [0]*(n+1)
        for num in arr:
            hash_list[num]+=1
        return hash_list[1:]

