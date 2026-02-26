class Solution:
    def equilibrium(self, arr):
        total = sum(arr)
        left_sum = 0

        for num in arr:
            total -= num
            if left_sum == total:
                return "true"
            left_sum += num

        return "false"