class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        max_sum = float('-inf')
        for i in range(n):
            total = total + nums[i]
            max_sum = max(total,max_sum)
            if total < 0:
                total = 0
        return max_sum



        