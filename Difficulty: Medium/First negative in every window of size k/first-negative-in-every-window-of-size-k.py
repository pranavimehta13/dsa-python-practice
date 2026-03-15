from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        q = deque() # Stores indices of negative elements
        result = []
        
        for i in range(n):
            # 1. Add current element's index if it's negative
            if arr[i] < 0:
                q.append(i)
            
            # 2. Remove indices that are out of the current window (k)
            if q and q[0] <= i - k:
                q.popleft()
            
            # 3. If we've reached at least the first window size
            if i >= k - 1:
                if q:
                    # The first index in q is the first negative in the window
                    result.append(arr[q[0]])
                else:
                    # No negative number found in this window
                    result.append(0)
                    
        return result