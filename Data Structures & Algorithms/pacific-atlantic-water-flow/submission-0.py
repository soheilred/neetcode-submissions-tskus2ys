class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        res = []

        flows = [[set() for i in range(m)] for _ in range(n)]
        seen = [[False] * m for _ in range(n)]

        # print(n, m, flows)
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    flows[i][j].add(0)
        
                if i == n - 1 or j == m - 1:
                    flows[i][j].add(1)
        print(flows)

        def dfs(i, j):
            if seen[i][j] != True:
                seen[i][j] = True

                reaches = flows[i][j]

                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_i, new_j = i + di, j + dj
                    if -1 < new_i < n and -1 < new_j < m and heights[new_i][new_j] <= heights[i][j]:
                        sea = dfs(new_i, new_j)
                        if sea is not None:
                            reaches.update(sea)
                flows[i][j].update(reaches)
            return flows[i][j]

        for i in range(n):
            for j in range(m):
                dfs(i, j)
        
        print(flows)
        for i in range(n):
            for j in range(m):
                if len(flows[i][j]) == 2:
                    res.append([i, j])
        
        return res