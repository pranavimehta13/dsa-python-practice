class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        req_sum = (n*(n+1))//2
        add = 0
        act_sum = sum(nums)
        return req_sum - act_sum

        
        