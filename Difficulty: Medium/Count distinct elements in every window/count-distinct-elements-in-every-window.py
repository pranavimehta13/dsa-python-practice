class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        answer = []
        freq_map = {}
        for i in range(n):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
            if i >= k:
                freq_map[arr[i-k]] -= 1
                if freq_map[arr[i-k]] == 0:
                    freq_map.pop(arr[i-k])
            if i >= k-1:
                answer.append(len(freq_map.keys()))
        return answer
        