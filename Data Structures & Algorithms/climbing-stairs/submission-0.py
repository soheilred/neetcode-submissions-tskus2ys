class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def dp(stairs):
            if stairs < 3:
                cache[stairs] = stairs
                return stairs
            
            if stairs in cache:
                return cache[stairs]
            
            cache[stairs] = dp(stairs - 1) + dp(stairs - 2)
            return cache[stairs]
        
        return dp(n)
        