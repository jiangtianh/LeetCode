class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
    
        @cache
        def f(i, k_rem):
            # Base case: we successfully drew all segments
            if k_rem == 0:
                return 1
                
            # Base case: we don't have enough points left. 
            # You need at least (k_rem + 1) points to draw k_rem segments.
            if n - i < k_rem + 1:
                return 0
                
            # The magical O(1) transition using exactly 2 parameters
            ans = 2 * f(i + 1, k_rem) + f(i + 1, k_rem - 1) - f(i + 2, k_rem)
            
            # Python's modulo operator safely handles negative numbers 
            # caused by the subtraction
            return ans % MOD
            
        return f(0, k)