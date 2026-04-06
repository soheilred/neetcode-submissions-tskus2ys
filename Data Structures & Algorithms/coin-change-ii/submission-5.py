class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, rem):
            if rem == 0:
                memo[(i, rem)] = 1
                return 1
            
            if rem < 0:
                return 0

            if (i, rem) in memo:
                return memo[(i, rem)]
            
            res = 0
            for j in range(i, n):
                res += dfs(j, rem - coins[j])
            
            memo[(i, rem)] = res
            
            return res
        return dfs(0, amount)

        # coins.sort()
        # memo = {}
        # n = len(coins)

        # def bt(i, rem):
        #     # nonlocal res
        #     # print(rem)
        #     if (i, rem) in memo:
        #         return memo[(i, rem)]

        #     if rem == 0:
        #         memo[(i, rem)] = 1
        #         return 1

        #     if i >= n:
        #         return 0    

        #     res = 0

        #     if rem >= coins[i]:
        #         res = bt(i, rem - coins[i]) + bt(i + 1, rem)
        #     memo[(i, rem)] = res
        #     return res

        # return bt(0, amount)
            
        # # return res
        