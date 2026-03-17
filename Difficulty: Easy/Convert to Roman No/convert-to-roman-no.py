class Solution:
    def convertRoman(self, n):
        # We include the subtraction cases (9, 4, 90, 40, etc.) in descending order
        roman_lookup = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        ans = ""
        
        for value, symbol in roman_lookup:
            # While the current value can fit into n, add the symbol
            while n >= value:
                ans += symbol
                n -= value
                
        return ans