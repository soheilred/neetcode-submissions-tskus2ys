class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_cost = {}
        n = len(cost)

        def dp(stair):
            if stair < 2:
                total_cost[stair] = 0
                return 0
            
            if stair in total_cost:
                return total_cost[stair]
            
            total_cost[stair] = min(cost[stair - 1] + dp(stair - 1), cost[stair - 2] + dp(stair - 2))
            return total_cost[stair]
        
        return dp(n)
        