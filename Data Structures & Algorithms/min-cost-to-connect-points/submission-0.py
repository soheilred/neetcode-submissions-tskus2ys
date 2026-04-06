class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i:[] for i in range(len(points))}
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                # heapq.heappush(graph[i], (dist, j))
                # heapq.heappush(graph[j], (dist, i))
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        print(graph)

        total = 0
        cur = 0
        minH = [(0, cur)]
        seen = set()

        while len(seen) < n:
            # print(cur, seen, total)
            cost, next_p = heapq.heappop(minH)
            if next_p in seen:
                continue

            seen.add(next_p)
            total += cost
            for child in graph[next_p]:
                if child[1] not in seen:
                    heapq.heappush(minH, child)
        
        return total
        