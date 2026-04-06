class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def bt(i, j):
            if i == n - 1 or j == m - 1:
                return 1

            if i > n or j > m:
                return 0
            
            res = 0
            for di, dj in [(1, 0), (0, 1)]:
                res += bt(i + di, j + dj)
            
            return res

        return bt(0, 0)

        