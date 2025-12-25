class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 0
        curr = 1
        next_ = 0
        for i in range(n):
            prev = curr
            curr = next_
            next_ = prev + curr
        return next_