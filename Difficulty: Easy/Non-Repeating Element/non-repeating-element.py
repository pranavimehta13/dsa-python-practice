#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        n = len(arr)
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num,0) + 1
        for num in freq_map:
            if freq_map[num] == 1:
                return num
        return 0
