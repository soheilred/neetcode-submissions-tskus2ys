class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = defaultdict(int)

        def bt(i, has):
            if i >= n:
                return 0
            
            # if (i, j) in memo:
                # return memo[(i, j)]
            
            # if i == j:
            
            # else:
            # for j in range(i+1, n):
                # memo[(i, j)] = max(-prices[i] + prices[j] + bt(j + 2, j + 2), bt(i + 1, i + 1))
            if has:
                return max(prices[i] + bt(i + 2, False), bt(i + 1, True))
            
            else:
                return max(-prices[i] + bt(i+1, True), bt(i+1, False))
            
            # return memo[(i, j)]

        return bt(0, 0)

        # print(memo)
            
        # return max(memo.values())
            

        