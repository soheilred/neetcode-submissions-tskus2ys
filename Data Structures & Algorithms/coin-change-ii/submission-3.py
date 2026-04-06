class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # res = 0
        coins.sort()
        memo = {}
        n = len(coins)

        def bt(i, rem):
            # nonlocal res
            # print(rem)
            if (i, rem) in memo:
                return memo[(i, rem)]

            if rem == 0:
                memo[(i, rem)] = 1
                return 1

            if i >= n:
                return 0    

            res = 0
            # for j in range(i, n):
                # if rem - coins[j] >= 0:
                    # res += bt(j, rem - coins[j])

            if rem >= coins[i]:
                res = bt(i, rem - coins[i]) + bt(i + 1, rem)
            memo[(i, rem)] = res
            # print(rem, res)
            return res

        
        return bt(0, amount)
        # return memo[(0, amount)]
            
        # return res
        