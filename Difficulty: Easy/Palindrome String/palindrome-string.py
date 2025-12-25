class Solution:
    def isPalindrome(self, s):
        old = s
        new = s[::-1]
        if old == new:
            return True
        return False
        
