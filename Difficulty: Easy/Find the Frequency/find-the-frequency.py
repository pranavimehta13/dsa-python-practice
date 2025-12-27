"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        freq_map = {}
        for ele in arr:
            freq_map[ele] = freq_map.get(ele, 0) + 1
        if x not in freq_map.keys():
            return 0
        return freq_map[x]