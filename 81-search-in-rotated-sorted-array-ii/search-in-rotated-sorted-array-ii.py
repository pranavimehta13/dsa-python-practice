class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low += 1
                else:
                    high -= 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high -= 1
                else:
                    low += 1
        return False
        
        