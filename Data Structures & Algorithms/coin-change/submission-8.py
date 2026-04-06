class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = []
        if amount == 0:
            return 0
        
        n = len(coins)
        memo = {}
        
        def dfs(i, rem):
            if rem < 0:
                return float('inf')
            
            if rem == 0:
                memo[(i, rem)] = 0
                return 0
                
            if (i, rem) in memo:
                return memo[(i, rem)]
            
            res = float('inf')
            for j in range(i, n):
                res = min(res, 1+dfs(j, rem - coins[j]))
            
            memo[(i, rem)] = res
            
            return res
        
        res = dfs(0, amount)
        return res if res != float('inf') else -1




        # n = len(coins)
        # memo = {}

        # def bt(rem):
        #     if rem in memo:
        #         return memo[rem]

        #     if rem == 0:
        #         return 0
            
        #     res = float('inf')

        #     for j in range(n):
        #         if rem - coins[j] >= 0:
        #             res = min(res, 1 + bt(rem - coins[j]))
        #     memo[rem] = res
        #     return res
            
        # res = bt(amount) 
        # return res if res != float('inf') else -1
            
