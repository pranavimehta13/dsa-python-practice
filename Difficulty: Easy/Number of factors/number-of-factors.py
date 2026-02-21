import math
class Solution:
    def countFactors (self, n):
        result = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                result+=1
                if n//i != i:
                    result+=1
        return result