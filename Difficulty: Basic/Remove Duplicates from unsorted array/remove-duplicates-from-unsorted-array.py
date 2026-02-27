#User function Template for python3

class Solution:
    def removeDuplicate(self, arr):
        n = len(arr)
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num,0) + 1
        return list(freq_map.keys())
    

