class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        freq_map = {}
        max_val = 0
        max_char = s[0]
        for char in s:
            freq_map[char] = freq_map.get(char,0) + 1
        for char,val in freq_map.items():
            if val > max_val:
                max_val = val
                max_char = char
            elif val == max_val:
                if char < max_char:
                    max_char = char
        return max_char
                