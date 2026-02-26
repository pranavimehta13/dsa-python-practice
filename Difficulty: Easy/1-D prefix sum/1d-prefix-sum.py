class Solution:
    def prefSum(self, arr):
        n = len(arr)
        add = 0
        pref_sum = []
        for num in arr:
            add = add+num
            pref_sum.append(add)
        return pref_sum
        