class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        level = -1

        q = deque([((i, j), level) for i in range(n) for j in range(m) if grid[i][j] == 2])

        while q:
            cur, level = q.popleft()
            i, j = cur
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if -1 < new_i < n and -1 < new_j < m and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 0
                    q.append(((new_i, new_j), level + 1))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return level+1


        