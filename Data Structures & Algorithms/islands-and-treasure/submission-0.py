class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        INF = 2147483647

        # def dfs(i, j, level):
        #     if -1 < i < n and -1 < j < m and grid[i][j] == INF: # grid[i][j] != 0 and grid[i][j] != -1:
        #         grid[i][j] = min(grid[i][j], level)
        #         # grid[i][j] =  level
        #         dfs(i+1, j, level+1)
        #         dfs(i-1, j, level+1)
        #         dfs(i, j+1, level+1)
        #         dfs(i, j-1, level+1)
        

        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 0:
        #             for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        #                 new_i, new_j = i + di, j + dj
        #                 dfs(new_i, new_j, 1)
        q = deque([((i, j), 0) for i in range(n) for j in range(m) if grid[i][j] == 0])
        # print(q)

        while q:
            # print(q)
            cur, level = q.popleft()
            i, j = cur
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if -1 < new_i < n and -1 < new_j < m and grid[new_i][new_j] == INF:
                    grid[new_i][new_j] = level + 1
                    q.append(((new_i, new_j), level + 1))

            
         