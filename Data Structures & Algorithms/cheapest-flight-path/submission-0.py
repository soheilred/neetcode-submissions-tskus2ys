class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f,t,p in flights:
            adj[f].append((t, p))
        
        cheapest = float('inf')

        def bt(node, stops, total):
            print(node, stops, total)
            nonlocal cheapest
            if stops > k + 1:
                return

            if node == dst:
                cheapest = min(cheapest, total)
                return
            
            # check if node is visited?
            for n, cost in adj[node]:
                bt(n, stops + 1, total + cost)
        
        bt(src, 0, 0)
        return cheapest if cheapest < float('inf') else -1


        