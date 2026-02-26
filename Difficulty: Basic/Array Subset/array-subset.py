#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freq_map = {}
    
        for num in a:
            freq_map[num] = freq_map.get(num, 0) + 1
    
        for num in b:
            if num not in freq_map or freq_map[num] == 0:
                return False
            freq_map[num] -= 1
    
        return True
    
    
    
