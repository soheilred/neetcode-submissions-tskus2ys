class Solution:
    def myPow(self, x: float, n: int) -> float:

        memo = {}

        def dp(n):
            if n == 1:
                memo[n] = x
                return memo[n]
            
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                memo[n] = dp(n // 2) * dp(n // 2)        
            else:
                memo[n] = dp(n // 2) * dp(n // 2) * x

            return memo[n]
        

        if n > 0:
            return dp(n)
        elif n == 0:
            return 1
        else:
            return 1 / dp(-n)