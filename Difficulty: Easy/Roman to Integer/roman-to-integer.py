class Solution:
    def romanToDecimal(self, s): 
        # Added 'L': 50 which was missing!
        r_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        n = len(s)
        
        for i in range(n):
            # Get the value of the current Roman numeral
            current_val = r_map[s[i]]
            
            # If not at the last char AND current is less than the next one
            if i + 1 < n and current_val < r_map[s[i+1]]:
                result -= current_val
            else:
                result += current_val
                
        return result