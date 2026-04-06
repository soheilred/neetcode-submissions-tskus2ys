class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i: float('inf') for i in range(1, n+1)}
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t)) 
        
        q = deque([([k], 0)])

        while q:
            path, cost = q.pop()
            last = path[-1]
            dist[last] = min(dist[last], cost)
            for child, c_cost in graph[last]:
                if child in path:
                    continue
                path.append(child)
                q.append((path.copy(), cost + c_cost))
                path.pop()
        max_dist = max([dist[i] for i in dist])
        return max_dist if max_dist != float('inf') else -1
        