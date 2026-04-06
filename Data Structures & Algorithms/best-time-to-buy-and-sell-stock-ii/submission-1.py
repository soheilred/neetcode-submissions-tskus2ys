class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        cur_max = 0
        N = len(prices)
        cache = {}

        def bt(day, own):
            if (day, own) in cache:
                return cache[(day, own)]

            if day >= N:
                cache[(day, own)] = 0
                return 0
            
            # if you own a share
            prof = 0
            if own:
                prof = max(prices[day] + bt(day + 1, False), bt(day + 1, True))
            
            else:
                prof = max(prof, -prices[day] + bt(day + 1, True), bt(day + 1, False))
            
            cache[(day, own)] = prof

            return prof
        
        return bt(0, False)

        # min_price = float('inf')

        # for p in prices:
        #     if p < min_price:
        #         min_price = p
            
        #     if p - min_price > cur_max:
        #         cur_max = p - min_price
        
        # return max_prof
        