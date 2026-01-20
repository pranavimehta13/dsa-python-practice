class Solution(object):
    def lowerBound(self, nums, target):
        lb = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upperBound(self, nums, target):
        ub = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lb = self.lowerBound(nums, target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = self.upperBound(nums, target)

        if ub == -1:                # ✅ no element > target
            return [lb, len(nums) - 1]

        return [lb, ub - 1]

            