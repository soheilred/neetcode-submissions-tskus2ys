class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 2 for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            dp[i][0] = max(-prices[i] + dp[i+1][1], dp[i + 1][0])
            dp[i][1] = max(prices[i] + dp[i+1][0], dp[i + 1][1])
        
        return dp[0][0]
       
        # return max_prof
        
        # cache = {}

        # def bt(day, own):
        #     if (day, own) in cache:
        #         return cache[(day, own)]

        #     if day >= N:
        #         cache[(day, own)] = 0
        #         return 0
            
        #     # if you own a share
        #     prof = 0
        #     if own:
        #         prof = max(prices[day] + bt(day + 1, False), bt(day + 1, True))
            
        #     else:
        #         prof = max(prof, -prices[day] + bt(day + 1, True), bt(day + 1, False))
            
        #     cache[(day, own)] = prof

        #     return prof
        
        # return bt(0, False)

