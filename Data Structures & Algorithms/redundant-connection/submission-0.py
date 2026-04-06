class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj_list = [[] for _ in range(n+1)]
        seen = []

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        def dfs(cur, par, path):
            if cur in path:
                seen.append(cur)
                return False

            seen.append(cur)
            path.append(cur)

            for n in adj_list[cur]:
                if n == par:
                    continue
                if dfs(n, cur, path) == False:
                    return False
            path.pop()
            seen.pop()
        
        dfs(1, 1, [])
        end = seen.pop()
        cycle = [end]
        while seen[-1] != end:
            cycle.append(seen.pop())

        print(cycle)

        for i in range(n - 1, -1, -1):
            a, b = edges[i]
            if a in cycle and b in cycle:
                return edges[i]
        return 

        