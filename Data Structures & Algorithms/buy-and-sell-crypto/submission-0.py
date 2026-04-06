class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_heap = heapq.heapify([])
        n = len(prices)
        max_suf = [0] * n
        min_pref = [0] * n
        max_elem = 0
        min_elem = float('inf')
        res = 0
        for i in range(n - 1, -1, -1):
            max_elem = max(prices[i], max_elem)
            max_suf[i] = max_elem
        
        for i in range(n):
            min_elem = min(prices[i], min_elem)
            min_pref[i] = min_elem
        
        print(min_pref, max_suf)


        for i in range(len(prices)):
            # heapq.heappush(min_heap, prices[i])
            # min_elem = min_heap[0]
            res = max(res, max_suf[i] - min_pref[i])
        
        return res



        