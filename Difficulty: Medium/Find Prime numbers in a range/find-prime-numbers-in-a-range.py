import math

class Solution:
    def primeRange(self, M, N):
        if N < 2:
            return []
        
        # Initialize a boolean array "is_prime[0..N]" 
        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False
        
        # Sieve logic
        for p in range(2, int(math.sqrt(N)) + 1):
            if is_prime[p]:
                # Update all multiples of p starting from p*p
                for i in range(p * p, N + 1, p):
                    is_prime[i] = False
        
        # Filter results within the range [M, N]
        return [num for num in range(M, N + 1) if is_prime[num]]