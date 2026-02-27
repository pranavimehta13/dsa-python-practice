#User function Template for python3

class Solution:
    def replaceWithRank(self, N, arr):
        sorted_arr = sorted(set(arr))
        freq_map = {}
        for i in range(len(sorted_arr)):
            freq_map[sorted_arr[i]] = i
        result = []
        for num in arr:
            result.append(freq_map[num]+1)
        return result