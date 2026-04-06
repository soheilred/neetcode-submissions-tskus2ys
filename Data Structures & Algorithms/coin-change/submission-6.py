class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = []
        if amount == 0:
            return 0

        # coins.sort(reverse=True)
        # while coins and coins[0] > amount:
        #     coins.pop(0)

        # print(coins)
        n = len(coins)
        memo = {}

        # def bt(i, rem, path):
        def bt(rem):
            if rem in memo:
                return memo[rem]

            if rem == 0:
                return 0
            
            res = float('inf')

            for j in range(n):
                if rem - coins[j] >= 0:
                    res = min(res, 1 + bt(rem - coins[j]))
            memo[rem] = res
            return res
            
        res = bt(amount) 
        return res if res != float('inf') else -1
            
