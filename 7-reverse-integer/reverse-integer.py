import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = abs(x)
            rev = int(str(x)[::-1])
            if rev<-2**31 or rev>2**31:
                return 0
            return -rev
        if x == 0:
            return 0
        rev = int(str(x)[::-1])
        if rev<-2**31 or rev>2**31:
                return 0
        return rev
