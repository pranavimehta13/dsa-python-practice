#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        a = n
        rev = 0
        while n > 0:
            rem = n%10
            rev = rev + rem**3
            n = n//10
        if a == rev:
            return True
        return False